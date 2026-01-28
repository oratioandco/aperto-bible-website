#!/usr/bin/env python3
"""
Remove ONLY old meditation devotionals (title: "Meditation").
Keep new morgen devotionals (title: "Morning Devotional").
"""

import json
from pathlib import Path

def remove_old_meditations_only(filepath):
    """Remove only old meditation entries from a pericope JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    updated = False

    for pericope in data.get('pericopes', []):
        media = pericope.get('media', {})

        # Check if devotional exists
        if 'devotional' in media:
            devotional = media['devotional']

            # Remove ONLY if title is exactly "Meditation"
            if devotional.get('title') == 'Meditation':
                del media['devotional']
                pericope['media'] = media
                updated = True
                print(f"  ✓ Removed old 'Meditation' from {pericope.get('id', 'unknown')}")
            else:
                print(f"  - Kept '{devotional.get('title')}' in {pericope.get('id', 'unknown')}")

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

        if remove_old_meditations_only(filepath):
            updated_count += 1
            print(f"  ✓ Updated\n")
        else:
            print(f"  - No changes\n")

    print(f"Completed: {updated_count}/{len(pericope_files)} files updated")
    return 0

if __name__ == "__main__":
    exit(main())
