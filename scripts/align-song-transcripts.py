#!/usr/bin/env python3
"""
Generate word-level timing for song transcripts using Whisper forced alignment.

Uses whisper CLI for alignment. Outputs word-level timestamps thatthat are merged into existing transcript JSON files.

Usage:
    python scripts/align-song-transcripts.py <transcript.json>
    python scripts/align-song-transcripts.py --all  # Process all song transcripts
    python scripts/align-song-transcripts.py public/transcripts/songs/luke_01/german/keine_angst_de_transcript.json

Requirements:
    pip install openai-whisper
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path


def load_transcript(transcript_path: str) -> dict:
    """Load existing transcript JSON."""
    with open(transcript_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_transcript(transcript_path: str, transcript: dict):
    """Save updated transcript JSON."""
    with open(transcript_path, 'w', encoding='utf-8') as f:
        json.dump(transcript, f, indent=2, ensure_ascii=False)


def find_audio_file(transcript_path: str, transcript: dict) -> str | None:
    """Find the audio file for a transcript."""
    # Check if audio_file is specified in transcript
    if 'audio_file' in transcript:
        audio_path = Path('public') / transcript['audio_file']
        if audio_path.exists():
            return str(audio_path)

    # Try to find based on transcript path and song_id
    song_id = transcript.get('song_id', '')
    language = transcript.get('language', 'de')
    public_dir = Path('public')

    possible_paths = [
        public_dir / 'audio' / 'songs' / 'luke_01' / language / f'{song_id}.mp3',
        public_dir / 'audio' / 'songs' / 'luke_01' / f'{song_id}.mp3',
        public_dir / 'audio' / 'songs' / f'{song_id}.mp3',
    ]

    for path in possible_paths:
        if path.exists():
            return str(path)

    return None


def run_whisper_alignment(audio_path: str, language: str, model: str = 'base') -> list[dict]:
    """
    Run whisper on audio file and extract word-level timestamps.
    Returns list of word segments with timing.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        cmd = [
            'whisper',
            audio_path,
            '--model', model,
            '--language', language,
            '--output_format', 'json',
            '--output_dir', tmpdir,
            '--word_timestamps', 'True',
        ]

        print(f"    Running whisper ({model}, {language})...")

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            print(f"    Whisper error: {result.stderr}")
            return []

        audio_name = Path(audio_path).stem
        json_path = Path(tmpdir) / f'{audio_name}.json'

        if not json_path.exists():
            print(f"    Error: Whisper output not found")
            return []

        with open(json_path, 'r') as f:
            whisper_output = json.load(f)

    # Extract word-level timestamps
    words = []
    for segment in whisper_output.get('segments', []):
        for word_info in segment.get('words', []):
            words.append({
                'word': word_info.get('word', '').strip(),
                'start_ms': int(word_info.get('start', 0) * 1000),
                'end_ms': int(word_info.get('end', 0) * 1000),
                'confidence': word_info.get('probability', 1.0)
            })

    return words


def normalize_word(word: str) -> str:
    """Normalize word for matching."""
    word = re.sub(r'[^\w]', '', word)
    return word.lower()


def match_words_to_line(line_text: str, line_start: int, line_end: int,
                        whisper_words: list[dict], start_idx: int = 0) -> tuple[list[dict], int]:
    """
    Match whisper words to a transcript line.
    Returns (matched_words, next_index)
    """
    expected_words = [normalize_word(w) for w in line_text.split() if w.strip()]
    matched = []
    idx = start_idx

    for expected in expected_words:
        if not expected:
            continue

        best_match = None
        best_score = 0

        for i in range(idx, min(idx + 15, len(whisper_words))):
            wt = whisper_words[i]
            wt_word = normalize_word(wt['word'])

            if wt['end_ms'] < line_start - 1000:
                continue
            if wt['start_ms'] > line_end + 1000:
                break

            if wt_word == expected:
                best_match = (i, wt, 1.0)
                break
            elif len(expected) >= 3 and len(wt_word) >= 3:
                if wt_word[:3] == expected[:3] or wt_word[-3:] == expected[-3:]:
                    score = 0.85
                    if score > best_score:
                        best_match = (i, wt, score)
                        best_score = score
                elif expected in wt_word or wt_word in expected:
                    score = 0.75
                    if score > best_score:
                        best_match = (i, wt, score)
                        best_score = score
            elif len(expected) >= 2 and len(wt_word) >= 2:
                if wt_word[:2] == expected[:2]:
                    score = 0.6
                    if score > best_score:
                        best_match = (i, wt, score)
                        best_score = score

        if best_match:
            _, wt, _ = best_match
            matched.append({
                'word': wt['word'],
                'start_ms': wt['start_ms'],
                'end_ms': wt['end_ms'],
                'confidence': wt.get('confidence', 1.0)
            })
            idx = best_match[0] + 1

    return matched, idx


def generate_fallback_word_timing(line_text: str, line_start: int, line_end: int) -> list[dict]:
    """
    Generate word timing using character-weighted distribution.
    Longer words get proportionally more time.
    """
    words = line_text.split()
    if not words:
        return []

    total_chars = sum(len(w) for w in words)
    if total_chars == 0:
        total_chars = len(words)

    line_duration = line_end - line_start
    gap_ms = min(50, line_duration // (len(words) * 4))
    total_gap = gap_ms * (len(words) - 1)
    available_duration = line_duration - total_gap

    words_timing = []
    current_time = line_start

    for word in words:
        word_weight = len(word) / total_chars
        word_duration = int(available_duration * word_weight)

        words_timing.append({
            'word': word,
            'start_ms': current_time,
            'end_ms': current_time + word_duration,
            'confidence': 0.7
        })

        current_time += word_duration + gap_ms

    if words_timing:
        words_timing[-1]['end_ms'] = line_end

    return words_timing


def align_transcript(transcript_path: str, audio_path: str | None = None,
                     model: str = 'base') -> bool:
    """
    Align transcript to get word-level timestamps.
    """
    print(f"\n{'='*60}")
    print(f"Processing: {transcript_path}")

    transcript = load_transcript(transcript_path)

    if not audio_path:
        audio_path = find_audio_file(transcript_path, transcript)

    if not audio_path or not os.path.exists(audio_path):
        print(f"  ✗ Audio file not found")
        return False

    print(f"  Audio: {audio_path}")

    language = transcript.get('language', 'de')
    print(f"  Language: {language}")

    try:
        whisper_words = run_whisper_alignment(audio_path, language, model)

        if not whisper_words:
            print(f"  ✗ No words extracted from audio")
            return False

        print(f"  Whisper extracted {len(whisper_words)} words")

        print(f"  Matching words to transcript lines...")
        word_idx = 0
        total_whisper = 0
        total_fallback = 0

        for section in transcript.get('sections', []):
            for line in section.get('lines', []):
                line_text = line.get('text', '')
                line_start = line.get('start_ms', 0)
                line_end = line.get('end_ms', 0)

                if not line_text.strip():
                    continue

                matched_words, word_idx = match_words_to_line(
                    line_text, line_start, line_end, whisper_words, word_idx
                )

                expected_word_count = len(line_text.split())
                match_ratio = len(matched_words) / expected_word_count if expected_word_count > 0 else 0

                if match_ratio >= 0.5:
                    line['words'] = matched_words
                    total_whisper += len(matched_words)
                else:
                    line['words'] = generate_fallback_word_timing(line_text, line_start, line_end)
                    total_fallback += len(line['words'])

        transcript['alignment_tool'] = 'whisper'
        transcript['alignment_model'] = model
        transcript['alignment_confidence'] = 0.9

        save_transcript(transcript_path, transcript)
        print(f"  ✓ Aligned {total_whisper} Whisper + {total_fallback} fallback words")
        return True

    except Exception as e:
        print(f"  ✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def find_all_song_transcripts() -> list[str]:
    """Find all song transcript JSON files."""
    transcripts = []
    public_dir = Path('public/transcripts/songs')

    if public_dir.exists():
        for json_file in public_dir.rglob('*.json'):
            if '.backup' not in str(json_file):
                transcripts.append(str(json_file))

    return sorted(transcripts)


def main():
    parser = argparse.ArgumentParser(
        description='Generate word-level timing for song transcripts using Whisper',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Align a single transcript
  python scripts/align-song-transcripts.py public/transcripts/songs/luke_01/german/keine_angst_de_transcript.json

  # Align all song transcripts
  python scripts/align-song-transcripts.py --all

  # Use a larger model for better accuracy (slower)
  python scripts/align-song-transcripts.py --model small transcript.json
        """
    )
    parser.add_argument('transcript', nargs='?', help='Path to transcript JSON file')
    parser.add_argument('--all', action='store_true', help='Process all song transcripts')
    parser.add_argument('--model', default='base',
                        choices=['tiny', 'base', 'small', 'medium', 'large'],
                        help='Whisper model size (default: base)')
    parser.add_argument('--audio', help='Path to audio file (auto-detected if not provided)')

    args = parser.parse_args()

    if args.all:
        transcripts = find_all_song_transcripts()
        print(f"Found {len(transcripts)} song transcripts")

        success = 0
        failed = 0

        for transcript_path in transcripts:
            if align_transcript(transcript_path, model=args.model):
                success += 1
            else:
                failed += 1

        print(f"\n{'='*60}")
        print(f"Completed: {success} successful, {failed} failed")

    elif args.transcript:
        success = align_transcript(args.transcript, args.audio, args.model)
        sys.exit(0 if success else 1)

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
