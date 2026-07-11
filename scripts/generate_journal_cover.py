#!/usr/bin/env python3
"""Generate a journal cover image in the "workshop" style.

Model: gemini-3.1-flash-image via generate_content — Google's migration
target now that the Imagen 4 endpoints shut down on 2026-08-17. This script
is also the migration template for the older generate_images.sh pipeline in
aperto-bible-dev (which still calls the deprecated generate_images()).

Usage:
  python3 scripts/generate_journal_cover.py <slug> <prompt-file>
  # writes public/images/journal/<slug>.png + .jpeg (quality 82)

Reads GOOGLE_API_KEY from the environment or from ../aperto-bible-dev/.env.
Style contract: docs/JOURNAL_IMAGE_STYLE.md (16:9, no people, no legible
text, no devotional iconography).
"""

import os
import pathlib
import sys


def api_key() -> str:
    key = os.environ.get('GOOGLE_API_KEY')
    if key:
        return key
    env = pathlib.Path(__file__).resolve().parents[2] / 'aperto-bible-dev' / '.env'
    if env.exists():
        for line in env.read_text().splitlines():
            if line.startswith('GOOGLE_API_KEY='):
                return line.split('=', 1)[1].strip().strip('"')
    sys.exit('GOOGLE_API_KEY not found (env or ../aperto-bible-dev/.env)')


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    slug, prompt_file = sys.argv[1], sys.argv[2]
    prompt = pathlib.Path(prompt_file).read_text()

    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key())
    resp = client.models.generate_content(
        model='gemini-3.1-flash-image',
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=['IMAGE'],
            image_config=types.ImageConfig(aspect_ratio='16:9'),
        ),
    )

    out_dir = pathlib.Path(__file__).resolve().parents[1] / 'public' / 'images' / 'journal'
    out_dir.mkdir(parents=True, exist_ok=True)
    png = out_dir / f'{slug}.png'

    for part in resp.candidates[0].content.parts:
        if getattr(part, 'inline_data', None) and part.inline_data.data:
            png.write_bytes(part.inline_data.data)
            break
    else:
        sys.exit(f'No image in response: {resp}')

    # Compressed jpeg for the page itself (png stays as the archival master)
    try:
        from PIL import Image
        img = Image.open(png).convert('RGB')
        img.save(out_dir / f'{slug}.jpeg', 'JPEG', quality=82, optimize=True)
    except ImportError:
        print('Pillow not available — skipped jpeg derivative')

    print(f'Wrote {png}')


if __name__ == '__main__':
    main()
