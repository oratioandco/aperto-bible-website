#!/usr/bin/env python3
"""Regenerate all 24 EN Luke chapter overview pages with the new BookNav design."""

import os

PAGES_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'pages', 'en', 'luke')

SUBTITLES = {
    1: "Two impossible pregnancies. Two revolutionary songs. The story begins.",
    2: "Birth in a stable. Shepherds as witnesses. An old man sees salvation.",
    3: "John preaches in the wilderness. Jesus is baptized. A genealogy back to Adam.",
    4: "Temptation in the wilderness. Rejection at Nazareth. Authority over demons.",
    5: "The catch of fish. Lepers and the paralyzed. Levi follows Jesus.",
    6: "Sabbath conflicts. The Twelve are chosen. Blessings and woes.",
    7: "The centurion's faith. The son of Nain. John's question.",
    8: "Women who followed Jesus. Parables of the kingdom. Storm and demons.",
    9: "The Twelve sent out. Five thousand fed. Peter's confession. Transfiguration.",
    10: "The seventy-two sent out. The Good Samaritan. Mary and Martha.",
    11: "The Lord's Prayer. Controversy. Woes against the religious leaders.",
    12: "Warning against hypocrisy. Do not worry. Watch and be ready.",
    13: "Repent or perish. A woman freed on the Sabbath. The narrow door.",
    14: "Hosts and guests. Humility at the table. The cost of following.",
    15: "Lost and found: sheep, coin, son.",
    16: "The shrewd manager. The rich man and poor Lazarus.",
    17: "Stumbling blocks. Ten men with leprosy. The coming kingdom.",
    18: "The persistent widow. The Pharisee and the tax collector. The rich ruler.",
    19: "Zacchaeus. The ten minas. The entry into Jerusalem.",
    20: "The wicked tenants. Taxes. The resurrection question.",
    21: "The widow's offering. Signs of the end. Watch and pray.",
    22: "The Last Supper. Betrayal and denial. Gethsemane.",
    23: "The trial. Crucifixion. The death of Jesus.",
    24: "The empty tomb. The road to Emmaus. Appearances and ascension.",
}

TEMPLATE = '''\
---
import BaseLayout from '../../../layouts/BaseLayout.astro';
import BookNav from '../../../components/BookNav.astro';
import pericopes from '../../../content/luke-{ch}-pericopes-en.json';

const chapter = {ch};
const prevChapter = {prev};
const nextChapter = {next};
---

<BaseLayout title="Luke {ch}" lang="en" description="Luke Chapter {ch}">
  <BookNav currentChapter={{{ch}}} lang="en" />

  <header class="chapter-header">
    <p class="passage-reference">The Gospel of Luke</p>
    <h1 class="headline-mixed">
      <span class="cap">C</span>hapter {ch}
    </h1>
    <p class="chapter-subtitle">{subtitle}</p>
  </header>

  <section class="pericope-grid-section">
    <div class="pericope-grid">
      {{pericopes.pericopes.map((p) => (
        <a href={{`/en/luke/{ch}/${{p.id}}`}} class="pericope-thumb">
          {{p.image && (
            <div class="pericope-thumb-img-wrap">
              <img src={{`/images/luke/{ch}/${{p.image}}`}} alt={{p.imageAlt || p.title}} class="pericope-thumb-img" loading="lazy" />
            </div>
          )}}
          <div class="pericope-thumb-info" style={{`background-color: ${{p.color}};`}}>
            <span class="pericope-thumb-verses">{{p.verses}}</span>
            <span class="pericope-thumb-title">{{p.title}}</span>
          </div>
        </a>
      ))}}
    </div>
  </section>

  <footer class="chapter-footer">
    <div class="chapter-footer-nav">
      {prev_link}
      {next_link}
    </div>
    <p class="license-note">Translation: Aperto Bible (AB-EN) | License: CC BY-SA 4.0</p>
  </footer>
</BaseLayout>

<style>
  .chapter-header {{
    padding: 3rem 2rem 2.5rem;
    text-align: center;
    background: linear-gradient(180deg, #FFFBF5 0%, #F5EBE0 100%);
    border-bottom: 1px solid rgba(139, 115, 85, 0.12);
  }}
  .passage-reference {{
    font-family: 'Switzer', sans-serif;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--color-accent, #8B7355);
    margin-bottom: 0.5rem;
  }}
  .chapter-subtitle {{
    font-family: 'Switzer', sans-serif;
    font-size: 1rem;
    color: var(--color-warm-gray, #9A8A7A);
    max-width: 36rem;
    margin: 0.5rem auto 0;
    line-height: 1.6;
  }}
  .headline-mixed {{
    font-family: 'Softcore', Georgia, serif;
    font-size: clamp(2.5rem, 7vw, 5rem);
    color: #6B5A4A;
    margin-bottom: 0.5rem;
    line-height: 1.1;
  }}
  .headline-mixed .cap {{
    font-family: 'Silvera', serif;
    color: #9A8570;
    font-size: 1.1em;
  }}

  .pericope-grid-section {{
    padding: 2.5rem 1.5rem;
    max-width: 1200px;
    margin: 0 auto;
  }}
  .pericope-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 1.25rem;
    align-items: start;
  }}
  .pericope-thumb {{
    border-radius: 14px;
    overflow: hidden;
    text-decoration: none;
    border: 1px solid var(--color-border, rgba(139,115,85,0.15));
    transition: transform 0.22s ease, box-shadow 0.22s ease;
    display: flex;
    flex-direction: column;
  }}
  .pericope-thumb:hover {{
    transform: translateY(-3px);
    box-shadow: 0 10px 28px rgba(0, 0, 0, 0.1);
  }}
  .pericope-thumb-img-wrap {{
    aspect-ratio: 16 / 9;
    overflow: hidden;
    flex-shrink: 0;
  }}
  .pericope-thumb-img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.35s ease;
    display: block;
  }}
  .pericope-thumb:hover .pericope-thumb-img {{ transform: scale(1.04); }}
  .pericope-thumb-info {{
    padding: 0.875rem 1.125rem 1rem;
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    min-height: 72px;
  }}
  .pericope-thumb-verses {{
    display: block;
    font-family: 'Switzer', sans-serif;
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--color-warm-gray, #9A8A7A);
    margin-bottom: 0.3rem;
  }}
  .pericope-thumb-title {{
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    font-family: 'Softcore', Georgia, serif;
    font-size: 1.05rem;
    font-weight: 150;
    color: var(--color-charcoal, #3D3530);
    line-height: 1.35;
  }}

  .chapter-footer {{
    padding: 2.5rem 2rem;
    text-align: center;
    background: #F5E6DC;
    border-top: 1px solid rgba(139, 115, 85, 0.12);
  }}
  .chapter-footer-nav {{
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 1.5rem;
  }}
  .footer-nav-btn {{
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.6rem 1.25rem;
    border-radius: 9999px;
    background: white;
    color: #6B5A4A;
    font-family: 'Switzer', sans-serif;
    font-size: 0.875rem;
    font-weight: 500;
    text-decoration: none;
    border: 1px solid rgba(139, 115, 85, 0.2);
    transition: all 0.2s ease;
  }}
  .footer-nav-btn:hover {{
    background: #8B7355;
    color: white;
    border-color: #8B7355;
  }}
  .license-note {{
    font-family: 'Switzer', sans-serif;
    font-size: 0.8rem;
    color: var(--color-warm-gray, #9A8A7A);
  }}
</style>
'''

PREV_LINK = '''\
      <a href="/en/luke/{prev}" class="footer-nav-btn">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 18l-6-6 6-6"/></svg>
        Chapter {prev}
      </a>'''

NEXT_LINK = '''\
      <a href="/en/luke/{next}" class="footer-nav-btn">
        Chapter {next}
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>
      </a>'''

for ch in range(1, 25):
    subtitle = SUBTITLES[ch]
    prev_ch = ch - 1 if ch > 1 else None
    next_ch = ch + 1 if ch < 24 else None

    prev_str = str(prev_ch) if prev_ch else 'null'
    next_str = str(next_ch) if next_ch else 'null'

    prev_link = PREV_LINK.format(prev=prev_ch) if prev_ch else ''
    next_link = NEXT_LINK.format(next=next_ch) if next_ch else ''

    content = TEMPLATE.format(
        ch=ch,
        prev=prev_str,
        next=next_str,
        subtitle=subtitle,
        prev_link=prev_link,
        next_link=next_link,
    )

    path = os.path.join(PAGES_DIR, f'{ch}.astro')
    with open(path, 'w') as f:
        f.write(content)
    print(f'✓ {ch}.astro')

print(f'\nDone. Updated 24 chapter pages.')
