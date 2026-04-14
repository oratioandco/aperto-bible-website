#!/usr/bin/env python3
"""
Sync song transcripts in public/transcripts/songs/luke_01/ from the
whisper-large-v3 aligned sources in ../aperto-bible/audio/songs/luke_01/.

The public files keep their slugified filenames, song_id, title,
audio_file (website-style path), hooks/intro_clips — only the timing
payload (sections, duration_ms, alignment_tool, alignment_confidence,
generated_at) is replaced from the rich source transcript.

Usage:
    python scripts/sync-song-transcripts-from-source.py          # dry run
    python scripts/sync-song-transcripts-from-source.py --write  # apply
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

WEBSITE_ROOT = Path(__file__).resolve().parent.parent
PUBLIC_DIR = WEBSITE_ROOT / "public" / "transcripts" / "songs" / "luke_01"
CONTENT_DIR = WEBSITE_ROOT / "src" / "content"
BIBLE_SONGS_DIR = (
    WEBSITE_ROOT.parent / "aperto-bible" / "audio" / "songs" / "luke_01"
)

FIELDS_TO_REPLACE = (
    "sections",
    "duration_ms",
    "alignment_tool",
    "alignment_confidence",
)


def collect_referenced_transcripts() -> set:
    """Return the set of transcriptPath values referenced from pericopes JSON."""
    refs = set()

    def walk(node):
        if isinstance(node, dict):
            for k, v in node.items():
                if (
                    k == "transcriptPath"
                    and isinstance(v, str)
                    and "/songs/luke_01/" in v
                ):
                    refs.add(v)
                else:
                    walk(v)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    for p in CONTENT_DIR.glob("luke-1-pericopes-*.json"):
        try:
            walk(json.load(open(p, "r", encoding="utf-8")))
        except Exception:
            continue
    return refs


def load_json(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def build_source_index(lang_folder: str) -> dict:
    """Index rich (whisper) source transcripts by MP3 basename AND by file stem."""
    src_dir = BIBLE_SONGS_DIR / lang_folder
    index = {"by_mp3": {}, "by_stem": {}, "all": []}
    if not src_dir.exists():
        return index

    for src_path in src_dir.glob("42_luke_*_transcript.json"):
        try:
            data = load_json(src_path)
        except Exception:
            continue
        if data.get("alignment_tool") != "whisper-large-v3":
            continue
        mp3_name = Path(data.get("audio_file", "")).name
        if mp3_name:
            index["by_mp3"][mp3_name] = (src_path, data)
        index["by_stem"][src_path.stem] = (src_path, data)
        index["all"].append((src_path, data))
    return index


def match_source(public_data: dict, src_index: dict):
    """Find the best rich-source transcript for a public transcript file."""
    pub_mp3 = Path(public_data.get("audio_file", "")).name

    # 1. Exact MP3 basename match.
    if pub_mp3 and pub_mp3 in src_index["by_mp3"]:
        return src_index["by_mp3"][pub_mp3]

    # 2. MP3 stem contained in / contains a source MP3 stem.
    pub_stem = Path(pub_mp3).stem if pub_mp3 else ""
    if pub_stem:
        for src_mp3, entry in src_index["by_mp3"].items():
            src_stem = Path(src_mp3).stem
            if pub_stem in src_stem or src_stem in pub_stem:
                return entry

    # 3. song_id stem token overlap against source MP3 stems.
    song_id = public_data.get("song_id", "")
    if song_id:
        tokens = {t for t in song_id.lower().replace("-", "_").split("_") if t}
        best, best_score = None, 0
        for src_mp3, entry in src_index["by_mp3"].items():
            src_tokens = {
                t
                for t in Path(src_mp3).stem.lower().replace("-", "_").split("_")
                if t
            }
            score = len(tokens & src_tokens)
            if score > best_score:
                best, best_score = entry, score
        if best and best_score >= 2:
            return best

    return None


def sync_one(public_path: Path, src_index: dict, write: bool, force: bool = False) -> str:
    try:
        public_data = load_json(public_path)
    except Exception as exc:
        return f"ERR load {public_path.name}: {exc}"

    already_rich = public_data.get("alignment_tool") == "whisper-large-v3"
    match = match_source(public_data, src_index)
    src_sanitized = match and match[1].get("sanitized") and not public_data.get("sanitized")
    if already_rich and not force and not src_sanitized:
        return f"skip {public_path.name} (already rich)"


    if not match:
        return f"MISS {public_path.name} (no rich source)"

    src_path, src_data = match

    if src_data.get("sanitized"):
        public_data["sanitized"] = True

    for field in FIELDS_TO_REPLACE:
        if field in src_data:
            public_data[field] = src_data[field]

    if "hooks" in src_data:
        public_data["hooks"] = src_data["hooks"]
    if "intro_clips" in src_data:
        public_data["intro_clips"] = src_data["intro_clips"]
    elif "intro_clips" in public_data and "intro_clips" not in src_data:
        pass  # keep existing

    public_data["generated_at"] = datetime.now(timezone.utc).isoformat()
    public_data["source_transcript"] = str(
        src_path.relative_to(BIBLE_SONGS_DIR.parent.parent.parent)
    )

    if write:
        save_json(public_path, public_data)

    word_count = sum(
        len(line.get("words", []))
        for section in public_data.get("sections", [])
        for line in section.get("lines", [])
    )
    return (
        f"OK   {public_path.name}  <- {src_path.name}  "
        f"(words={word_count}, dur={public_data.get('duration_ms')})"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write", action="store_true", help="Apply changes (default: dry run)"
    )
    parser.add_argument(
        "--language",
        help="Only process this language folder name (e.g., german, czech)",
    )
    parser.add_argument(
        "--include-orphans",
        action="store_true",
        help="Also sync public files not referenced by any pericopes JSON",
    )
    args = parser.parse_args()

    referenced = collect_referenced_transcripts()
    print(f"referenced transcriptPath entries in pericopes: {len(referenced)}")

    if not PUBLIC_DIR.exists():
        print(f"public dir not found: {PUBLIC_DIR}", file=sys.stderr)
        return 1
    if not BIBLE_SONGS_DIR.exists():
        print(f"bible songs dir not found: {BIBLE_SONGS_DIR}", file=sys.stderr)
        return 1

    lang_folders = sorted(
        d.name for d in PUBLIC_DIR.iterdir() if d.is_dir()
    )
    if args.language:
        lang_folders = [l for l in lang_folders if l == args.language]

    totals = {"ok": 0, "miss": 0, "skip": 0, "err": 0, "orphan": 0}
    for lang in lang_folders:
        src_index = build_source_index(lang)
        pub_files = sorted((PUBLIC_DIR / lang).glob("*_transcript.json"))
        if not pub_files:
            continue
        print(
            f"\n[{lang}]  sources={len(src_index['all'])}  public={len(pub_files)}"
        )
        for pf in pub_files:
            rel_ref = "/" + str(pf.relative_to(WEBSITE_ROOT / "public"))
            if not args.include_orphans and rel_ref not in referenced:
                totals["orphan"] += 1
                print(f"  orphan {pf.name} (not referenced by any pericopes)")
                continue
            result = sync_one(pf, src_index, args.write)
            print(f"  {result}")
            tag = result.split()[0]
            if tag == "OK":
                totals["ok"] += 1
            elif tag == "MISS":
                totals["miss"] += 1
            elif tag == "skip":
                totals["skip"] += 1
            else:
                totals["err"] += 1

    mode = "APPLIED" if args.write else "DRY RUN (use --write to apply)"
    print(f"\n== {mode} ==")
    print(
        f"ok={totals['ok']}  miss={totals['miss']}  "
        f"skip={totals['skip']}  err={totals['err']}  "
        f"orphan={totals['orphan']}"
    )
    return 0 if totals["err"] == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
