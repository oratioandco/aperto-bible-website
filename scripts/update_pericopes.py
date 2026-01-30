#!/usr/bin/env python3
"""
Update pericope JSON files to include morgen devotionals.
Only adds devotionals that actually exist in the filesystem.
"""

import json
from pathlib import Path

# Pericope to verse mapping
PERICOPE_VERSES = {
    "zacharias-elisabeth": "05-25",
    "annunciation": "26-38",
    "magnificat": "46-56",
    "benedictus": "67-79"
}

# Languages with morgen devotionals
LANGUAGES = {
    "da": "danish",
    "de": "german",
    "en": "english",
    "fr": "french",
    "it": "italian",
    "pl": "polish",
    "pt": "portuguese"
}

def devotional_exists(lang_code, verses):
    """Check if a morgen devotional exists for this language and verses."""
    lang_folder = LANGUAGES.get(lang_code)
    if not lang_folder:
        return False

    morgen_filename = f"42_luke_1_{verses}_morgen_{lang_code}.mp3"
    morgen_path = Path(f"public/audio/devotionals/luke_01/{lang_folder}/{morgen_filename}")
    return morgen_path.exists()

def update_pericope_file(filepath, lang_code):
    """Update a single pericope JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    updated = False

    for pericope in data.get('pericopes', []):
        pericope_id = pericope.get('id')

        # Check if this pericope should have a morgen devotional
        if pericope_id in PERICOPE_VERSES:
            verses = PERICOPE_VERSES[pericope_id]

            # Check if the file actually exists
            if not devotional_exists(lang_code, verses):
                print(f"  - Skipping {pericope_id}: file doesn't exist")
                continue

            lang_folder = LANGUAGES.get(lang_code, "english")

            # Morgen devotional filename
            morgen_filename = f"42_luke_1_{verses}_morgen_{lang_code}.mp3"
            morgen_path = f"luke_01/{lang_folder}/{morgen_filename}"

            # Get media object
            media = pericope.get('media', {})

            # Check if devotional already exists
            if 'devotional' not in media:
                media['devotional'] = {}

            # Update the devotional to point to morgen file
            devotional = media['devotional']

            # Only update if it's not already pointing to morgen
            if 'morgen' not in devotional.get('mp3', ''):
                devotional['mp3'] = morgen_path
                devotional['title'] = "Morning Devotional"
                devotional['duration'] = "5 min"
                pericope['media'] = media
                updated = True
                print(f"  ✓ Updated {pericope_id}: {morgen_filename}")

    # Write back if updated
    if updated:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True

    return False

def main():
    """Update all pericope files."""
    content_dir = Path("src/content")

    # Find all pericope JSON files
    pericope_files = list(content_dir.glob("luke-1-pericopes-*.json"))

    if not pericope_files:
        print("No pericope files found!")
        return 1

    print(f"Found {len(pericope_files)} pericope files\n")

    updated_count = 0

    for filepath in pericope_files:
        # Extract language code from filename
        lang_code = filepath.stem.split('-')[-1]

        print(f"Processing {filepath.name} ({lang_code})...")

        if update_pericope_file(filepath, lang_code):
            updated_count += 1
            print(f"  ✓ Updated\n")
        else:
            print(f"  - No changes needed\n")

    print(f"Completed: {updated_count}/{len(pericope_files)} files updated")
    return 0

if __name__ == "__main__":
    exit(main())
