#!/usr/bin/env python3
"""
Fix .headline-mixed CSS overrides in Astro chapter pages under src/pages/*/luke/.

Rules:
1. In .headline-mixed { } blocks that contain 'Softcore': remove ONLY the
   font-family and color lines. Keep font-size, margin-bottom, line-height if present.
   If the block becomes empty after removal, remove the whole block including braces.
2. Remove entire .headline-mixed .cap { ... } blocks.
3. Do NOT touch .headline-mixed blocks that don't contain 'Softcore'.
4. Only touch files under src/pages/*/luke/*.astro.
"""

import glob
import os
import re
import sys

ROOT = "/Users/ttreppmann/StudioProjects/aperto-website"
PATTERN = os.path.join(ROOT, "src/pages/*/luke/*.astro")

# Lines to remove from .headline-mixed block (exact content match, stripped)
REMOVE_LINES_IN_HEADLINE_MIXED = {
    "font-family: 'Softcore', Georgia, serif;",
    "color: #6B5A4A;",
}


def process_file(filepath: str) -> tuple[bool, str]:
    """
    Returns (changed, new_content).
    changed=False means file was not modified (or had nothing to fix).
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Quick skip: if no 'Softcore' in file at all, nothing to do
    if "Softcore" not in content:
        return False, content

    lines = content.splitlines(keepends=True)
    result = []
    i = 0
    changed = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # --- Detect `.headline-mixed .cap {` block and remove entire block ---
        if re.match(r"\.headline-mixed\s+\.cap\s*\{", stripped):
            # Collect forward until matching closing brace
            block_lines = [line]
            j = i + 1
            depth = stripped.count("{") - stripped.count("}")
            while j < len(lines) and depth > 0:
                bl = lines[j]
                depth += bl.count("{") - bl.count("}")
                block_lines.append(bl)
                j += 1
            # Optionally remove a trailing blank line after the block
            if j < len(lines) and lines[j].strip() == "":
                j += 1  # skip the blank line too
            changed = True
            i = j
            continue

        # --- Detect `.headline-mixed {` block (NOT `.cap`) ---
        if re.match(r"\.headline-mixed\s*\{", stripped) and ".cap" not in stripped:
            # Collect the block
            block_start = i
            block_lines = [line]
            j = i + 1
            depth = stripped.count("{") - stripped.count("}")
            while j < len(lines) and depth > 0:
                bl = lines[j]
                depth += bl.count("{") - bl.count("}")
                block_lines.append(bl)
                j += 1
            block_end = j  # exclusive

            # Check if this block contains 'Softcore'
            block_text = "".join(block_lines)
            if "Softcore" not in block_text:
                # Leave it untouched
                result.extend(block_lines)
                i = block_end
                continue

            # Remove Softcore font-family and color lines from inner lines
            # block_lines[0] is the opening brace line
            # block_lines[-1] is the closing brace line
            new_inner = []
            for bl in block_lines[1:-1]:  # skip opening/closing brace lines
                bl_stripped = bl.strip()
                if bl_stripped in REMOVE_LINES_IN_HEADLINE_MIXED:
                    changed = True
                    continue
                new_inner.append(bl)

            # Check if block is now effectively empty (only whitespace lines remain)
            non_empty_inner = [bl for bl in new_inner if bl.strip() != ""]
            if not non_empty_inner:
                # Remove the entire block (opening brace line + inner + closing brace line)
                # Also remove a trailing blank line if present
                if block_end < len(lines) and lines[block_end].strip() == "":
                    block_end += 1
                changed = True
                i = block_end
                continue
            else:
                # Keep the block with the remaining lines
                result.append(block_lines[0])   # opening brace line
                result.extend(new_inner)
                result.append(block_lines[-1])  # closing brace line
                i = block_end
                continue

        # Default: keep line as-is
        result.append(line)
        i += 1

    if not changed:
        return False, content

    new_content = "".join(result)
    return True, new_content


def main():
    files = sorted(glob.glob(PATTERN))
    print(f"Found {len(files)} .astro files under src/pages/*/luke/")

    modified_count = 0
    skipped_count = 0

    for filepath in files:
        changed, new_content = process_file(filepath)
        if changed:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            rel = os.path.relpath(filepath, ROOT)
            print(f"  MODIFIED: {rel}")
            modified_count += 1
        else:
            skipped_count += 1

    print(f"\nDone. Modified {modified_count} files, skipped {skipped_count} unchanged files.")


if __name__ == "__main__":
    main()
