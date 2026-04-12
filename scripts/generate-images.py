#!/usr/bin/env python3
"""
Generate pericope images using Gemini Imagen 4.0
Uses Kinfolk/Alabaster editorial photography aesthetic

After generating images, translates imageAlt text into all available languages
and writes the results into the per-language pericope JSON files.

Usage:
  python scripts/generate-images.py --chapter 1
  python scripts/generate-images.py --chapter 2
  python scripts/generate-images.py --chapter 2 --single 0
  python scripts/generate-images.py --all
  python scripts/generate-images.py --chapter 2 --alts-only
"""

import os
import sys
import re
import json
import time
import argparse
from pathlib import Path

from google import genai
from google.genai import types

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
PROMPTS_DIR = PROJECT_DIR / "src/data/images"
CONTENT_DIR = PROJECT_DIR / "src/content"

# Rate limiting
DELAY_BETWEEN_REQUESTS = 5  # seconds

# All supported language codes
ALL_LANGS = [
    "ar", "bg", "ca", "cs", "da", "de", "el", "en", "es", "et",
    "fi", "fr", "ga", "hr", "hu", "it", "lt", "lv", "mt", "nb",
    "nl", "pl", "pt", "ro", "ru", "sk", "sl", "sq", "sv", "tr", "uk"
]

# Language names for the translation prompt
LANG_NAMES = {
    "ar": "Arabic", "bg": "Bulgarian", "ca": "Catalan", "cs": "Czech",
    "da": "Danish", "de": "German", "el": "Greek", "en": "English",
    "es": "Spanish", "et": "Estonian", "fi": "Finnish", "fr": "French",
    "ga": "Irish", "hr": "Croatian", "hu": "Hungarian", "it": "Italian",
    "lt": "Lithuanian", "lv": "Latvian", "mt": "Maltese", "nb": "Norwegian Bokmål",
    "nl": "Dutch", "pl": "Polish", "pt": "Portuguese", "ro": "Romanian",
    "ru": "Russian", "sk": "Slovak", "sl": "Slovenian", "sq": "Albanian",
    "sv": "Swedish", "tr": "Turkish", "uk": "Ukrainian"
}


def get_prompts_file(chapter: int) -> Path:
    if chapter == 1:
        return PROMPTS_DIR / "luke-1-image-prompts-v2.json"
    return PROMPTS_DIR / f"luke-{chapter}-image-prompts.json"


def get_output_dir(chapter: int) -> Path:
    return PROJECT_DIR / f"public/images/luke/{chapter}"


def get_pericopes_file(chapter: int, lang: str) -> Path:
    return CONTENT_DIR / f"luke-{chapter}-pericopes-{lang}.json"


def generate_image(client, prompt: str, filename: str, output_dir: Path) -> bool:
    try:
        print(f"  Generating with imagen-4.0-generate-001...")
        response = client.models.generate_images(
            model="imagen-4.0-generate-001",
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio="16:9",
                safety_filter_level="BLOCK_LOW_AND_ABOVE",
            )
        )
        if response.generated_images:
            generated = response.generated_images[0]
            output_path = output_dir / filename
            generated.image.save(str(output_path))
            print(f"  ✓ Saved: {filename}")
            return True
        else:
            print(f"  ✗ No image generated")
            return False
    except Exception as e:
        print(f"  ✗ Error: {str(e)[:200]}")
        return False


def translate_alts_batch(client, alts: dict, langs: list) -> dict:
    """Translate a dict of {filename: english_alt} into the given languages. Returns {lang: {filename: translation}}."""
    alt_list = "\n".join(f'{i+1}. [{fname}] {alt}' for i, (fname, alt) in enumerate(alts.items()))
    lang_list = "\n".join(f"- {code}: {LANG_NAMES[code]}" for code in langs)

    prompt = f"""Translate these {len(alts)} image alt text descriptions into these languages.

Alt texts:
{alt_list}

Target languages:
{lang_list}

Rules:
- Short and descriptive — same length as the English
- Describe what the image visually shows, not its meaning
- Natural, contemporary phrasing
- Return ONLY valid JSON, no other text:
{{
  "{langs[0]}": {{"filename1.png": "translation", "filename2.png": "translation"}},
  "{langs[1]}": {{...}},
  ...
}}"""

    response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
    raw = response.text.strip()
    raw = re.sub(r'^```json\s*', '', raw)
    raw = re.sub(r'\s*```$', '', raw)
    return json.loads(raw)


def translate_alts(client, images: list, chapter: int) -> None:
    """Translate imageAlt texts into all languages and write into pericope JSON files."""
    alts = {img["filename"]: img["imageAlt"] for img in images if img.get("imageAlt")}
    if not alts:
        print("  No imageAlt fields found, skipping translation.")
        return

    print(f"\n  Translating {len(alts)} alt texts into {len(ALL_LANGS)} languages (in batches)...")

    # Process in batches of 8 languages to avoid response size limits
    BATCH_SIZE = 8
    all_translations = {}
    lang_batches = [ALL_LANGS[i:i+BATCH_SIZE] for i in range(0, len(ALL_LANGS), BATCH_SIZE)]

    for batch_idx, lang_batch in enumerate(lang_batches):
        print(f"  Batch {batch_idx+1}/{len(lang_batches)}: {', '.join(lang_batch)}")
        try:
            batch_result = translate_alts_batch(client, alts, lang_batch)
            all_translations.update(batch_result)
        except Exception as e:
            print(f"  ✗ Batch {batch_idx+1} failed: {str(e)[:200]}")

    # Write into each pericope JSON file
    updated_files = 0
    for lang in ALL_LANGS:
        pericopes_file = get_pericopes_file(chapter, lang)
        if not pericopes_file.exists():
            continue

        lang_translations = all_translations.get(lang, {})
        if not lang_translations:
            continue

        with open(pericopes_file) as f:
            data = json.load(f)

        changed = False
        for pericope in data.get("pericopes", []):
            img_filename = pericope.get("image") or ""
            if not img_filename:
                continue
            img_stem = Path(img_filename).stem + ".png"
            alt = lang_translations.get(img_stem) or lang_translations.get(img_filename)
            if alt and pericope.get("imageAlt") != alt:
                pericope["imageAlt"] = alt
                changed = True

        if changed:
            with open(pericopes_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            updated_files += 1

    print(f"  ✓ Updated imageAlt in {updated_files} pericope JSON files")


def wire_image_fields(images: list, chapter: int) -> None:
    """Write image filename and update .jpeg→.png into all per-language pericope JSON files."""
    # Build pericopeId → filename map
    pericope_to_file = {
        img["pericopeId"]: img["filename"]
        for img in images
        if img.get("pericopeId")
    }
    if not pericope_to_file:
        print("  No pericopeId fields found, skipping image field wiring.")
        return

    updated_files = 0
    for lang in ALL_LANGS:
        pericopes_file = get_pericopes_file(chapter, lang)
        if not pericopes_file.exists():
            continue

        with open(pericopes_file) as f:
            data = json.load(f)

        changed = False
        for pericope in data.get("pericopes", []):
            pid = pericope.get("id")
            if pid in pericope_to_file:
                new_filename = pericope_to_file[pid]
                if pericope.get("image") != new_filename:
                    pericope["image"] = new_filename
                    changed = True
            # Also fix any legacy .jpeg references to .png
            elif (pericope.get("image") or "").endswith(".jpeg"):
                pericope["image"] = pericope["image"].replace(".jpeg", ".png")
                changed = True

        if changed:
            with open(pericopes_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            updated_files += 1

    print(f"  ✓ Wired image fields in {updated_files} pericope JSON files")


def generate_chapter(client, chapter: int, single_index=None, alts_only: bool = False) -> tuple:
    prompts_file = get_prompts_file(chapter)
    if not prompts_file.exists():
        print(f"  ✗ Prompts file not found: {prompts_file}")
        return 0, 0

    output_dir = get_output_dir(chapter)
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(prompts_file) as f:
        data = json.load(f)

    style_prefix = data.get("style_notes", "")
    color_palette = data.get("color_palette", "")
    images = data["images"]

    if alts_only:
        print(f"Wiring image fields and translating alt texts for Luke {chapter} (skipping image generation)...")
        wire_image_fields(images, chapter)
        translate_alts(client, images, chapter)
        return 0, 0

    target_images = [images[single_index]] if single_index is not None else images

    if single_index is not None:
        print(f"Generating single image: {target_images[0]['filename']}\n")
    else:
        print(f"Generating {len(target_images)} images for Luke {chapter}...\n")

    success_count = 0
    for i, img in enumerate(target_images):
        full_prompt = f"{style_prefix}. Color palette: {color_palette}. {img['prompt']}"
        print(f"[{i+1}/{len(target_images)}] {img['title']} (verses {img['verses']})")

        output_path = output_dir / img["filename"]
        if output_path.exists():
            print(f"  ⏭  Already exists, skipping")
            success_count += 1
        else:
            if generate_image(client, full_prompt, img["filename"], output_dir):
                success_count += 1

        if i < len(target_images) - 1:
            print(f"  Waiting {DELAY_BETWEEN_REQUESTS}s...")
            time.sleep(DELAY_BETWEEN_REQUESTS)

    # Always wire image fields and translate alts after full chapter generation
    if single_index is None:
        wire_image_fields(images, chapter)
        translate_alts(client, images, chapter)

    return success_count, len(target_images)


def main():
    parser = argparse.ArgumentParser(description="Generate pericope images for Luke chapters")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--chapter", type=int, help="Chapter number (e.g. 1, 2)")
    group.add_argument("--all", action="store_true", help="Generate all chapters with prompt files")
    parser.add_argument("--single", type=int, help="Generate only one image by index (0-based), skips alt translation")
    parser.add_argument("--alts-only", action="store_true", help="Only translate/update alt texts, skip image generation")
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable required")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    if args.all:
        chapters = sorted(set(
            int(m.group(1))
            for f in sorted(PROMPTS_DIR.glob("luke-*-image-prompts*.json"))
            if (m := re.search(r"luke-(\d+)-image-prompts", f.name))
        ))
        if not chapters:
            print(f"No prompts files found in {PROMPTS_DIR}")
            sys.exit(1)

        print(f"Found prompts for {len(chapters)} chapters: {chapters}\n")
        total_success, total_images = 0, 0
        for chapter in chapters:
            print(f"\n{'='*50}")
            print(f"Luke Chapter {chapter}")
            print(f"{'='*50}")
            s, t = generate_chapter(client, chapter, alts_only=args.alts_only)
            total_success += s
            total_images += t

        print(f"\n{'='*50}")
        print(f"All chapters complete: {total_success}/{total_images} images generated")

    else:
        s, t = generate_chapter(client, args.chapter, args.single, alts_only=args.alts_only)
        if not args.alts_only:
            print(f"\n{'='*50}")
            print(f"Luke {args.chapter} complete: {s}/{t} images generated")
            print(f"Output: {get_output_dir(args.chapter)}")


if __name__ == "__main__":
    main()
