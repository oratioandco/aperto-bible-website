#!/usr/bin/env python3
"""Generate src/pages/{lang}/psalms/index.astro for available languages."""

import os

LANGUAGES = ['de', 'en', 'pl']

PSALMS_NAMES = {
    'de': 'Psalmen',
    'en': 'Psalms',
    'pl': 'Psalmy',
}

INTRO_LABELS = {
    'de': 'Einleitung',
    'en': 'Introduction',
    'pl': 'Wprowadzenie',
}

EYEBROWS = {
    'de': 'Das Buch der Psalmen',
    'en': 'The Book of Psalms',
    'pl': 'Księga Psalmów',
}

TEMPLATE = '''---
import BaseLayout from '../../../layouts/BaseLayout.astro';
import {{ marked }} from 'marked';
import introMd from '../../../content/introductions-psalms/{lang}.md?raw';

const bookName = '{bookName}';
const introLabel = '{introLabel}';
const html = marked(introMd);
---

<BaseLayout title={{`${{bookName}} — ${{introLabel}}`}} lang="{lang}" description={{`${{introLabel}} — ${{bookName}}`}}>
  <div class="intro-page">
    <header class="intro-header">
      <p class="intro-eyebrow">{eyebrow}</p>
      <h1 class="intro-title">{{bookName}}</h1>
      <p class="intro-subtitle">{{introLabel}}</p>
    </header>
    <article class="intro-body prose" set:html={{html}} />
  </div>
</BaseLayout>

<style>
  .intro-page {{
    max-width: 680px;
    margin: 0 auto;
    padding: 0 1.5rem 6rem;
  }}
  .intro-header {{
    padding: 4rem 0 3rem;
    border-bottom: 1px solid rgba(139, 115, 85, 0.15);
    margin-bottom: 3rem;
  }}
  .intro-eyebrow {{
    font-family: 'Switzer', sans-serif;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #8B7355;
    margin-bottom: 0.75rem;
  }}
  .intro-title {{
    font-family: 'Softcore', Georgia, serif;
    font-size: clamp(2.5rem, 6vw, 4rem);
    color: #3D3530;
    line-height: 1.1;
    margin-bottom: 0.5rem;
  }}
  .intro-subtitle {{
    font-family: 'Switzer', sans-serif;
    font-size: 1rem;
    color: #9A8A7A;
  }}
  .intro-body {{
    font-family: 'Switzer', sans-serif;
    font-size: 1.05rem;
    line-height: 1.75;
    color: #3D3530;
  }}
  :global(.intro-body h2) {{
    font-family: 'Softcore', Georgia, serif;
    font-size: 1.4rem;
    font-weight: 150;
    color: #3D3530;
    margin-top: 2.5rem;
    margin-bottom: 0.75rem;
    border-bottom: 1px solid rgba(139, 115, 85, 0.12);
    padding-bottom: 0.5rem;
  }}
  :global(.intro-body p) {{
    margin-bottom: 1.25rem;
  }}
  :global(.intro-body em) {{
    font-style: italic;
    color: #5C4F45;
  }}
  :global(.intro-body h1) {{
    display: none;
  }}
</style>
'''

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES_DIR = os.path.join(BASE_DIR, 'src', 'pages')

created = 0
for lang in LANGUAGES:
    content = TEMPLATE.format(
        lang=lang,
        bookName=PSALMS_NAMES[lang],
        introLabel=INTRO_LABELS[lang],
        eyebrow=EYEBROWS[lang],
    )

    output_path = os.path.join(PAGES_DIR, lang, 'psalms', 'index.astro')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    created += 1
    print(f"Created: {output_path}")

print(f"\nDone. Created {created} index.astro files.")
