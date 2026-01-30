#!/usr/bin/env python3
"""
Add ID3 tags and cover images to devotional MP3 files.
Usage: python scripts/add_id3_tags.py
"""

import os
import subprocess
from pathlib import Path

# Configuration
DEVOTIONALS_PATH = Path("public/audio/devotionals/luke_01")
COVER_IMAGE = Path("public/images/covers/morgen.png")

# Metadata mappings
LANGUAGE_NAMES = {
    "danish": "Dansk",
    "english": "English",
    "french": "Français",
    "german": "Deutsch",
    "italian": "Italiano",
    "polish": "Polski",
    "portuguese": "Português"
}

# Pericope titles for mapping
PERICOPE_TITLES = {
    "05-25": {
        "de": "Ein alter Priester",
        "en": "An Old Priest",
        "da": "En gammel præst",
        "fr": "Un vieux prêtre",
        "it": "Un vecchio sacerdote",
        "pl": "Stary kapłan",
        "pt": "Um velho sacerdote"
    },
    "26-38": {
        "de": "Maria sagt ja",
        "en": "Mary Says Yes",
        "da": "Maria siger ja",
        "fr": "Marie dit oui",
        "it": "Maria dice di sì",
        "pl": "Maria mówi tak",
        "pt": "Maria diz sim"
    },
    "46-56": {
        "de": "Meine Seele preist",
        "en": "My Soul Proclaims",
        "da": "Min sjæl priser",
        "fr": "Mon âme exalte",
        "it": "L'anima mia magnifica",
        "pl": "Moja dusza wielbi",
        "pt": "Minha alma engrandece"
    },
    "67-79": {
        "de": "Der Nachtmensch",
        "en": "The Morning Watch",
        "da": "Morgenvagten",
        "fr": "La veille du matin",
        "it": "La veglia del mattino",
        "pl": "Straż nad ranem",
        "pt": "A vigia matinal"
    }
}

def get_verse_range(filename):
    """Extract verse range from filename like 42_luke_1_26-38_morgen_de.mp3"""
    parts = filename.split("_")
    for part in parts:
        if "-" in part and any(c.isdigit() for c in part):
            return part
    return None

def get_language_code(dirname):
    """Get language code from directory name"""
    lang_map = {
        "danish": "da",
        "english": "en",
        "french": "fr",
        "german": "de",
        "italian": "it",
        "polish": "pl",
        "portuguese": "pt"
    }
    return lang_map.get(dirname.lower(), "en")

def add_id3_tags(mp3_path, cover_path, title, artist, album, genre):
    """
    Add ID3 tags and cover image to MP3 using ffmpeg.

    Args:
        mp3_path: Path to MP3 file
        cover_path: Path to cover image
        title: Track title
        artist: Artist name
        album: Album name
        genre: Genre
    """
    temp_output = mp3_path.with_suffix('.tmp.mp3')

    # Build ffmpeg metadata
    metadata = [
        f'title={title}',
        f'artist={artist}',
        f'album={album}',
        f'genre={genre}',
    ]

    # Build ffmpeg command
    cmd = [
        'ffmpeg',
        '-i', str(mp3_path),
        '-i', str(cover_path),
        '-map', '0:0',
        '-map', '1:0',
        '-c', 'copy',
        '-id3v2_version', '3',
        '-metadata:s:v', 'title="Album cover"',
        '-metadata:s:v', 'comment="Cover (front)"',
    ]

    # Add metadata
    for m in metadata:
        cmd.extend(['-metadata', m])

    cmd.append(str(temp_output))

    # Run ffmpeg
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=False
        )

        if result.returncode == 0:
            # Replace original with tagged version
            mp3_path.unlink()
            temp_output.rename(mp3_path)
            print(f"✓ Tagged: {mp3_path.name}")
            return True
        else:
            print(f"✗ Failed: {mp3_path.name}")
            print(f"  Error: {result.stderr}")
            if temp_output.exists():
                temp_output.unlink()
            return False

    except Exception as e:
        print(f"✗ Error processing {mp3_path.name}: {e}")
        if temp_output.exists():
            temp_output.unlink()
        return False

def main():
    """Main function to process all devotionals."""
    if not COVER_IMAGE.exists():
        print(f"Error: Cover image not found at {COVER_IMAGE}")
        return 1

    # Find all morgen MP3 files
    morgen_files = list(DEVOTIONALS_PATH.rglob("*morgen*.mp3"))
    morgen_files = [f for f in morgen_files if "_archive" not in str(f)]

    if not morgen_files:
        print("No morgen files found!")
        return 1

    print(f"Found {len(morgen_files)} devotional files to process\n")

    success_count = 0

    for mp3_path in morgen_files:
        # Extract language from parent directory
        lang_dir = mp3_path.parent.name
        lang_code = get_language_code(lang_dir)
        lang_name = LANGUAGE_NAMES.get(lang_dir.lower(), lang_dir)

        # Extract verse range
        verse_range = get_verse_range(mp3_path.name)

        if not verse_range:
            print(f"✗ Skipping {mp3_path.name}: couldn't determine verse range")
            continue

        # Get title for this pericope
        title_map = PERICOPE_TITLES.get(verse_range, {})
        title = title_map.get(lang_code, f"Morgen {verse_range}")

        # Build metadata
        artist = f"Aperto Bible ({lang_name})"
        album = "Aperto Morgen - Luke 1"
        genre = "Meditation"

        # Add tags
        if add_id3_tags(mp3_path, COVER_IMAGE, title, artist, album, genre):
            success_count += 1

    print(f"\nCompleted: {success_count}/{len(morgen_files)} files processed")
    return 0

if __name__ == "__main__":
    exit(main())
