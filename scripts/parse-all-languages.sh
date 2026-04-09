#!/bin/bash
# Parse all 31 language USFM files for Luke chapter 1

WEBSITE_DIR="/Users/ttreppmann/StudioProjects/aperto-website"
BIBLE_DIR="/Users/ttreppmann/StudioProjects/aperto-bible"

cd "$WEBSITE_DIR"

LANGS=(de en fr pl tr es it da sv uk pt nl ro cs el hu bg hr fi sk lt sl lv et ga mt nb ru ar ca)

for lang in "${LANGS[@]}"; do
    echo "Parsing $lang..."
    python3 scripts/usfm-to-website-json.py --chapter 1 --language $lang \
        --usfm-dir "$BIBLE_DIR/usfm" \
        --output-dir src/content
done

echo "Done!"
