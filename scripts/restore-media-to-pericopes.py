#!/usr/bin/env python3
"""
Restore rich media metadata to pericopes files.
Merges coverArt, transcriptPath, devotional, audioBible, and spiritualPractice
from the original pre-873cd8a structure into current pericopes.

Usage:
    python scripts/restore-media-to-pericopes.py --chapter 1 --language de
    python scripts/restore-media-to-pericopes.py --chapters 1-24 --language de
"""

import argparse
import json
import re
from pathlib import Path
from typing import Dict, Optional

# Original rich media structure from commit before 873cd8a
# This maps verse ranges to their original media content
ORIGINAL_MEDIA_DE = {
    # Luke 1
    "1-4": {
        "audioBible": {
            "title": "Lukas 1 - Hörbibel",
            "mp3": "42_luke_01_audio_bible_de.mp3",
            "transcriptPath": "/transcripts/audiobible/42_luke_01_transcript_de.json"
        },
        "podcast": {
            "title": "Podcast",
            "mp3": "luke_01/de/42_luke_01_01-04_podcast_de.mp3",
            "duration": "4 min"
        }
    },
    "5-25": {
        "songs": [{
            "title": "Keine Angst",
            "mp3": "luke_01/german/keine_angst_de.mp3",
            "genre": "Pop",
            "description": "Die Geschichte von Zacharias",
            "coverArt": "/images/covers/keine_angst_de.png",
            "transcriptPath": "/transcripts/songs/luke_01/german/keine_angst_de_transcript.json"
        }],
        "podcast": {
            "title": "Podcast",
            "mp3": "luke_01/de/42_luke_01_05-25_podcast_de.mp3",
            "duration": "4 min"
        },
        "devotional": {
            "title": "Meditation",
            "mp3": "daily_devotional_01_05-25_de.mp3",
            "duration": "5 min"
        }
    },
    "26-38": {
        "songs": [{
            "title": "Hab keine Angst",
            "mp3": "luke_01/german/_Hab keine Angst_ - Luke 1_26-38 (German).mp3",
            "genre": "Piano-Pop",
            "description": "Eine Geschichte über Mut und Vertrauen",
            "coverArt": "/images/covers/annunciation_karaoke.png",
            "transcriptPath": "/transcripts/songs/luke_01/german/42_luke_01_26_38_transcript_de.json"
        }],
        "podcast": {
            "title": "Podcast",
            "mp3": "luke_01/de/42_luke_01_26-38_podcast_de.mp3",
            "duration": "3 min"
        },
        "devotional": {
            "title": "Morning Devotional",
            "mp3": "luke_01/german/42_luke_1_26-38_morgen_de.mp3",
            "duration": "5 min"
        },
        "spiritualPractice": {
            "title": "Geistliche Übung",
            "mp3": "spiritual_practice_01_26-38_de.mp3",
            "duration": "10 min"
        }
    },
    "39-45": {
        "podcast": {
            "title": "Podcast",
            "mp3": "luke_01/de/42_luke_01_39-45_podcast_de.mp3",
            "duration": "3 min"
        },
        "devotional": {
            "title": "Meditation",
            "mp3": "daily_devotional_01_39-45_de.mp3",
            "duration": "5 min"
        }
    },
    "46-56": {
        "songs": [{
            "title": "Alles in mir feiert",
            "mp3": "luke_01/german/_Alles in mir feiert_ - Luke 1_46-56 (German).mp3",
            "genre": "Pop-Rap",
            "description": "Marias Lobgesang",
            "coverArt": "/images/covers/magnificat_karaoke.png",
            "transcriptPath": "/transcripts/songs/luke_01/german/42_luke_01_46_56_transcript_de.json"
        }],
        "podcast": {
            "title": "Podcast",
            "mp3": "luke_01/de/42_luke_01_46-56_podcast_de.mp3",
            "duration": "3 min"
        },
        "devotional": {
            "title": "Morning Devotional",
            "mp3": "luke_01/german/42_luke_1_46-56_morgen_de.mp3",
            "duration": "5 min"
        },
        "spiritualPractice": {
            "title": "Geistliche Übung",
            "mp3": "spiritual_practice_01_46-56_de.mp3",
            "duration": "10 min"
        }
    },
    "57-66": {
        "podcast": {
            "title": "Podcast",
            "mp3": "luke_01/de/42_luke_01_57-66_podcast_de.mp3",
            "duration": "3 min"
        }
    },
    "67-79": {
        "songs": [{
            "title": "Das Schweigen gebrochen",
            "mp3": "luke_01/german/Luke 1_67-79 German.mp3",
            "genre": "Singer-Songwriter",
            "description": "Zacharias' Prophetie",
            "coverArt": "/images/covers/benedictus_karaoke.png",
            "transcriptPath": "/transcripts/songs/luke_01/german/42_luke_01_67_79_transcript_de.json"
        }],
        "podcast": {
            "title": "Podcast",
            "mp3": "luke_01/de/42_luke_01_67-79_podcast_de.mp3",
            "duration": "3 min"
        },
        "devotional": {
            "title": "Morning Devotional",
            "mp3": "luke_01/german/42_luke_1_67-79_morgen_de.mp3",
            "duration": "5 min"
        },
        "spiritualPractice": {
            "title": "Geistliche Übung",
            "mp3": "spiritual_practice_01_67-79_de.mp3",
            "duration": "10 min"
        }
    },
    "80": {
        "podcast": {
            "title": "Podcast",
            "mp3": "luke_01/de/42_luke_01_80_podcast_de.mp3",
            "duration": "3 min"
        }
    }
}

# Polish media (same structure but with Polish file paths)
ORIGINAL_MEDIA_PL = {
    "26-38": {
        "songs": [{
            "title": "Nie bój się",
            "mp3": "luke_01/polish/_Nie bój się_ - Luke 1_26-38 (Polish).mp3",
            "genre": "Piano-Pop",
            "description": "Historia o odwadze i zaufaniu",
            "coverArt": "/images/covers/annunciation_karaoke.png",
            "transcriptPath": "/transcripts/songs/luke_01/polish/42_luke_01_26_38_transcript_pl.json"
        }],
        "podcast": {
            "title": "Podcast",
            "mp3": "luke_01/pl/42_luke_01_26-38_podcast_pl.mp3",
            "duration": "3 min"
        }
    },
    "46-56": {
        "songs": [{
            "title": "Wszystko we mnie śpiewa",
            "mp3": "luke_01/polish/_Wszystko we mnie śpiewa_ - Luke 1_46-56 (Polish).mp3",
            "genre": "Pop-Rap",
            "description": "Pieśń Maryi",
            "coverArt": "/images/covers/magnificat_karaoke.png",
            "transcriptPath": "/transcripts/songs/luke_01/polish/42_luke_01_46_56_transcript_pl.json"
        }],
        "podcast": {
            "title": "Podcast",
            "mp3": "luke_01/pl/42_luke_01_46-56_podcast_pl.mp3",
            "duration": "3 min"
        }
    },
    "67-79": {
        "songs": [{
            "title": "Milczenie przerwane",
            "mp3": "luke_01/polish/Luke 1_67-79 Polish.mp3",
            "genre": "Singer-Songwriter",
            "description": "Proroctwo Zachariasza",
            "coverArt": "/images/covers/benedictus_karaoke.png",
            "transcriptPath": "/transcripts/songs/luke_01/polish/42_luke_01_67_79_transcript_pl.json"
        }],
        "podcast": {
            "title": "Podcast",
            "mp3": "luke_01/pl/42_luke_01_67-79_podcast_pl.mp3",
            "duration": "3 min"
        }
    }
}

def find_matching_media(pericope_verses: str, media_map: Dict) -> Optional[Dict]:
    """Find matching media for a pericope based on verse range"""
    # Parse the pericope verse range
    if '-' in pericope_verses:
        start, end = map(int, pericope_verses.split('-'))
    else:
        start = end = int(pericope_verses)

    # Look for exact match first
    if pericope_verses in media_map:
        return media_map[pericope_verses]

    # Look for overlapping ranges
    for range_str, media in media_map.items():
        if '-' in range_str:
            m_start, m_end = map(int, range_str.split('-'))
        else:
            m_start = m_end = int(range_str)

        # Check if ranges overlap
        if start <= m_end and end >= m_start:
            return media

    return None


def restore_media_to_pericopes(pericopes_data: Dict, language: str) -> Dict:
    """Restore rich media metadata to pericopes"""
    media_map = ORIGINAL_MEDIA_DE if language == 'de' else ORIGINAL_MEDIA_PL

    for pericope in pericopes_data.get('pericopes', []):
        verse_range = pericope.get('verses', '')
        matching_media = find_matching_media(verse_range, media_map)

        if matching_media:
            # Initialize media if not present
            if 'media' not in pericope or not pericope['media']:
                pericope['media'] = {}

            # Merge media content
            for key, value in matching_media.items():
                pericope['media'][key] = value

    return pericopes_data


def main():
    parser = argparse.ArgumentParser(description='Restore rich media to pericopes')
    parser.add_argument('--chapter', type=int, help='Single chapter to process')
    parser.add_argument('--chapters', help='Chapter range (e.g., 1-24)')
    parser.add_argument('--language', required=True, choices=['de', 'pl'], help='Language code')
    parser.add_argument('--content-dir', default='src/content', help='Content directory')

    args = parser.parse_args()

    content_dir = Path(args.content_dir)

    # Determine chapters to process
    chapters = []
    if args.chapter:
        chapters = [args.chapter]
    elif args.chapters:
        match = re.match(r'(\d+)-(\d+)', args.chapters)
        if match:
            chapters = list(range(int(match.group(1)), int(match.group(2)) + 1))

    if not chapters:
        print("Please specify --chapter or --chapters")
        return

    print(f"\n📖 Restoring media to {len(chapters)} chapters ({args.language})...\n")

    for chapter in chapters:
        pericopes_path = content_dir / f"luke-{chapter}-pericopes-{args.language}.json"

        if not pericopes_path.exists():
            print(f"  ⏭ Chapter {chapter}: pericopes file not found")
            continue

        # Load current pericopes
        with open(pericopes_path, 'r', encoding='utf-8') as f:
            pericopes_data = json.load(f)

        # Restore media
        original_count = sum(1 for p in pericopes_data.get('pericopes', []) if p.get('media'))
        pericopes_data = restore_media_to_pericopes(pericopes_data, args.language)
        new_count = sum(1 for p in pericopes_data.get('pericopes', []) if p.get('media'))

        # Save updated pericopes
        with open(pericopes_path, 'w', encoding='utf-8') as f:
            json.dump(pericopes_data, f, ensure_ascii=False, indent=2)

        print(f"  ✅ Chapter {chapter}: media restored ({original_count} → {new_count} pericopes with media)")

    print(f"\n✅ Media restoration complete!")


if __name__ == '__main__':
    main()
