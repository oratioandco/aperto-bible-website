#!/usr/bin/env python3
"""
Remove old meditation devotionals from pericope JSON files.
Keeps the new morgen devotionals (title: "Morning Devotional").
Removes old ones (title: "Meditation" and mp3 starting with "daily_devotional").
"""

import json
from pathlib import Path

def remove_old_devotionals_from_file(filepath):
    """Remove old meditation entries from a pericope JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    updated = False

    for pericope in data.get('pericopes', []):
        media = pericope.get('media', {})

        # Check if devotional exists
        if 'devotional' in media:
            devotional = media['devotional']

            # Remove if it's an old meditation (not a morgen)
            is_old = (
                devotional.get('title') == 'Meditation' or
                devotional.get('mp3', '').startswith('daily_devotional')
            )

            if is_old:
                del media['devotional']
                pericope['media'] = media
                updated = True
                print(f"  ✓ Removed old meditation from {pericope.get('id', 'unknown')}")
            else:
                print(f"  - Kept morgen devotional in {pericope.get('id', 'unknown')}")

    # Write back if updated
    if updated:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True

    return False

def main():
    """Remove old meditations from all pericope files."""
    content_dir = Path("src/content")

    # Find all pericope JSON files
    pericope_files = list(content_dir.glob("luke-1-pericopes-*.json"))

    if not pericope_files:
        print("No pericope files found!")
        return 1

    print(f"Found {len(pericope_files)} pericope files\n")

    updated_count = 0

    for filepath in pericope_files:
        print(f"Processing {filepath.name}...")

        if remove_old_devotionals_from_file(filepath):
            updated_count += 1
            print(f"  ✓ Updated\n")
        else:
            print(f"  - No changes needed\n")

    print(f"Completed: {updated_count}/{len(pericope_files)} files updated")
    return 0

if __name__ == "__main__":
    exit(main())
