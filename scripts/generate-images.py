#!/usr/bin/env python3
"""
Generate pericope images using Gemini Imagen 4.0
Uses Austurbane aesthetic - minimalist Mediterranean biblical style
"""

import os
import sys
import json
import time
from pathlib import Path

from google import genai
from google.genai import types

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
PROMPTS_FILE = PROJECT_DIR / "src/content/images/luke-1-image-prompts-v2.json"
OUTPUT_DIR = PROJECT_DIR / "public/images/luke/1"

# Rate limiting
DELAY_BETWEEN_REQUESTS = 5  # seconds

def generate_image(client, prompt: str, filename: str) -> bool:
    """Generate an image using Imagen 4.0."""
    
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
        
        # Save the generated image
        if response.generated_images:
            generated = response.generated_images[0]
            output_path = OUTPUT_DIR / filename
            
            # Use the save method on the image
            generated.image.save(str(output_path))
            
            print(f"  ✓ Saved: {filename}")
            return True
        else:
            print(f"  ✗ No image generated")
            return False
            
    except Exception as e:
        error_msg = str(e)
        print(f"  ✗ Error: {error_msg[:200]}")
        return False

def main():
    # Get API key from environment
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable required")
        print("Usage: GEMINI_API_KEY=your_key python scripts/generate-images.py")
        sys.exit(1)
    
    client = genai.Client(api_key=api_key)
    
    # Parse arguments
    single_index = None
    if len(sys.argv) > 2 and sys.argv[1] == "--single":
        single_index = int(sys.argv[2])

    # Load prompts
    with open(PROMPTS_FILE) as f:
        data = json.load(f)

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    style_prefix = data.get("style_notes", "")
    color_palette = data.get("color_palette", "")
    images = data["images"]

    if single_index is not None:
        images = [images[single_index]]
        print(f"Generating single image: {images[0]['filename']}\n")
    else:
        print(f"Generating {len(images)} Austurbane images for Luke 1...\n")

    success_count = 0
    for i, img in enumerate(images):
        full_prompt = f"{style_prefix}. Color palette: {color_palette}. {img['prompt']}"

        print(f"[{i+1}/{len(images)}] {img['title']} (verses {img['verses']})")

        if generate_image(client, full_prompt, img["filename"]):
            success_count += 1

        # Rate limiting delay between requests
        if i < len(images) - 1:
            print(f"  Waiting {DELAY_BETWEEN_REQUESTS}s...")
            time.sleep(DELAY_BETWEEN_REQUESTS)

    print(f"\n{'='*50}")
    print(f"Completed: {success_count}/{len(images)} images generated")
    print(f"Output directory: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
