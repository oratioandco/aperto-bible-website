#!/usr/bin/env python3
"""
Remove devotionals from pericope JSON files.
"""

import json
from pathlib import Path

def remove_devotionals_from_file(filepath):
    """Remove devotional entries from a pericope JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    updated = False

    for pericope in data.get('pericopes', []):
        media = pericope.get('media', {})

        # Remove devotional if it exists
        if 'devotional' in media:
            del media['devotional']
            pericope['media'] = media
            updated = True
            print(f"  ✓ Removed devotional from {pericope.get('id', 'unknown')}")

    # Write back if updated
    if updated:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True

    return False

def main():
    """Remove devotionals from all pericope files."""
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

        if remove_devotionals_from_file(filepath):
            updated_count += 1
            print(f"  ✓ Updated\n")
        else:
            print(f"  - No devotionals found\n")

    print(f"Completed: {updated_count}/{len(pericope_files)} files updated")
    return 0

if __name__ == "__main__":
    exit(main())
