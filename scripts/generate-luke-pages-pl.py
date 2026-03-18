#!/usr/bin/env python3
"""
Generate pericopes JSON files and Astro pages for Polish Luke chapters.
Only generates files for chapters that don't already have pericopes.

Usage:
    python scripts/generate-luke-pages-pl.py --chapter 4
    python scripts/generate-luke-pages-pl.py --chapters 4-24
"""

import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Optional


# Polish chapter descriptions
CHAPTER_DESCRIPTIONS = {
    1: "Dwie niemożliwe ciąże. Dwie rewolucyjne pieśni. Historia się zaczyna.",
    2: "Dziecko się rodzi. Pasterze i Mędrcy. Chłopiec w Świątyni.",
    3: "Jan głosi na pustyni. Jezus zostaje ochrzczony. Rodowód do Adama.",
    4: "Kuszenie na pustyni. Odrzucenie w Nazarecie. Władza nad demonami.",
    5: "Niezwykły połów. Trędowaty i paralityk. Lewi naśladowuje Jezusa.",
    6: "Konflikty o szabat. Powołanie Dwunastu. Błogosławieństwa i biada.",
    7: "Setnik z Kafarnaum. Młodzieniec z Nain. Pytanie Jana.",
    8: "Kobiety naśladowują Jezusa. Przypowieści o Królestwie. Burza i demony.",
    9: "Dwunastu wysłanych. 5000 nakarmionych. Wyznanie Piotra. Przemienienie.",
    10: "Siedemdziesięciu dwóch. Miłosierny Samarytanin. Marta i Maria.",
    11: "Modlitwa Pańska. Żądanie znaku. Biada obłudnikom.",
    12: "Ostrzeżenie przed obłudą. O troskę. Czuwajcie i bądźcie wierni.",
    13: "Nawrócenie lub zguba. Skrzywiona kobieta. Wąska brama.",
    14: "Gospodarze i goście. Wielka uczta. Koszt naśladowania.",
    15: "Zgubione i odnalezione: owca, moneta, syn.",
    16: "Niewierny zarządca. Bogacz i ubogi Łazarz.",
    17: "O zgorszeniu. Dziesięciu trędowatych. O przyjściu Królestwa.",
    18: "Prosząca wdowa. Faryzeusz i celnik. Bogaty młodzieniec.",
    19: "Zacheusz. Przypowieść o talentach. Wjazd do Jerozolimy.",
    20: "Pracownicy winnicy. Kwestia podatku. Pytanie o zmartwychwstanie.",
    21: "Dar wdowy. Znaki czasów ostatecznych. Czuwajcie i módlcie się.",
    22: "Ostatnia Wieczerza. Zdrada i zaparcie. Getsemani.",
    23: "Proces. Ukrzyżowanie. Śmierć Syna Bożego.",
    24: "Pusty grób. Droga do Emaus. Objawienia i Wniebowstąpienie.",
}

# Color palette for pericopes
COLORS = [
    ("#E8E4DC", "#8B7355"),  # Warm beige
    ("#E4E8E4", "#6B8E7F"),  # Sage green
    ("#F0E8E4", "#D4A574"),  # Peach
    ("#E8E4F0", "#8B7399"),  # Lavender
    ("#E4E8F0", "#4A7C9E"),  # Steel blue
    ("#F0F0E4", "#9B8B4A"),  # Gold
    ("#E4F0E8", "#4A9B7C"),  # Emerald
    ("#F0E4E8", "#9B4A6B"),  # Rose
]


def get_chapter_data(chapter: int, content_dir: Path) -> Optional[Dict]:
    """Load chapter data from JSON file"""
    json_path = content_dir / f"luke-{chapter}-pl.json"
    if not json_path.exists():
        return None

    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def generate_pericopes(chapter: int, chapter_data: Dict) -> Dict:
    """Generate pericopes JSON from chapter sections"""
    pericopes = []

    sections = chapter_data.get('sections', [])
    for i, section in enumerate(sections):
        verses = section.get('verses', [])
        if not verses:
            continue

        first_verse = int(verses[0]['number'].split('-')[0])
        last_verse = int(verses[-1]['number'].split('-')[0])

        if first_verse == last_verse:
            verse_range = str(first_verse)
        else:
            verse_range = f"{first_verse}-{last_verse}"

        # Generate ID from heading
        heading = section.get('heading', f'Section {i+1}')
        section_id = re.sub(r'[^a-z0-9]+', '-', heading.lower()).strip('-')
        if not section_id:
            section_id = f"section-{i+1}"

        # Get color
        color, accent_color = COLORS[i % len(COLORS)]

        pericope = {
            'id': section_id,
            'title': heading,
            'subtitle': '',
            'verses': verse_range,
            'color': color,
            'accentColor': accent_color,
            'media': {},
            'image': None,
        }

        pericopes.append(pericope)

    return {
        'book': 'Łukasz',
        'chapter': chapter,
        'pericopes': pericopes
    }


def generate_astro_page(chapter: int, description: str = None) -> str:
    """Generate Astro page content for a Polish chapter"""
    if description is None:
        description = CHAPTER_DESCRIPTIONS.get(chapter, f"Ewangelia Łukasza Rozdział {chapter}")

    return f'''---
import BaseLayout from '../../../layouts/BaseLayout.astro';
import PericopeCard from '../../../components/PericopeCard.astro';
import ChapterNav from '../../../components/ChapterNav.astro';
import chapterData from '../../../content/luke-{chapter}-pl.json';
import pericopes from '../../../content/luke-{chapter}-pericopes-pl.json';

// Helper to get verses for a pericope
function getVersesForPericope(verseRange: string, sections: any[]) {{
  const allVerses: any[] = [];
  sections.forEach(section => {{
    section.verses.forEach((v: any) => allVerses.push(v));
  }});

  const [start, end] = verseRange.split('-').map(Number);
  const endNum = end || start;

  return allVerses.filter(v => {{
    const vNum = v.number.includes('-') ? parseInt(v.number.split('-')[0]) : parseInt(v.number);
    return vNum >= start && vNum <= endNum;
  }});
}}

const base = '';
---

<BaseLayout title="Łukasz {chapter}" lang="pl" description="Ewangelia Łukasza Rozdział {chapter}">
  <!-- Chapter Header -->
  <header class="chapter-header min-h-[90vh] flex flex-col justify-center items-center text-center px-8 py-24" style="background: linear-gradient(180deg, #FFFBF5 0%, #F5EBE0 100%);">
    <p class="passage-reference mb-6">Ewangelia według Łukasza</p>
    <h1 class="headline-mixed text-5xl md:text-7xl lg:text-8xl mb-6">
      <span class="cap">R</span>ozdział {chapter}
    </h1>
    <p class="text-xl md:text-2xl text-warm-gray max-w-2xl mb-16">
      {description}
    </p>

    <!-- Table of Contents with Headlines -->
    <nav class="toc max-w-2xl w-full">
      <ul class="space-y-2">
        {{pericopes.pericopes.map((p) => (
          <li>
            <a
              href={{`#${{p.id}}`}}
              class="toc-item flex items-center justify-between py-3 px-4 rounded-lg transition-all hover:bg-white/50"
            >
              <span class="toc-title text-left">{{p.title}}</span>
              <span class="toc-verses text-sm">{{p.verses}}</span>
            </a>
          </li>
        ))}}
      </ul>
    </nav>

    <!-- Scroll indicator -->
    <div class="scroll-indicator mt-16 opacity-40">
      <svg class="w-6 h-6 text-warm-gray animate-bounce" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 14l-7 7m0 0l-7-7m7 7V3"></path>
      </svg>
    </div>
  </header>

  <!-- Pericopes -->
  <div class="pericopes-container">
    {{pericopes.pericopes.map((pericope, index) => (
      <PericopeCard
        id={{pericope.id}}
        title={{pericope.title}}
        subtitle={{pericope.subtitle}}
        verses={{pericope.verses}}
        color={{pericope.color}}
        accentColor={{pericope.accentColor}}
        verseData={{getVersesForPericope(pericope.verses, chapterData.sections)}}
        image={{pericope.image}}
        media={{pericope.media}}
        exegesis={{pericope.exegesis}}
        lang="pl"
        chapter={{{chapter}}}
        isFirst={{index === 0}} layoutIndex={{index}}
      />
    ))}}
  </div>

  <!-- Chapter Footer -->
  <footer class="chapter-footer py-24 px-8 text-center" style="background: #F5E6DC;">
    <ChapterNav currentChapter={{{chapter}}} lang="pl" />

    <div class="mt-12">
      <a href={{`${{base}}/pl/`}} style="background: #8B7355; color: white;" class="inline-flex items-center gap-2 px-8 py-4 rounded-full font-medium transition-all hover:opacity-90">
        ← Powrót do strony głównej
      </a>
    </div>

    <p class="mt-12 text-sm text-warm-gray">
      Tłumaczenie: Aperto Bibel (AB-PL) | Licencja: CC BY-SA 4.0
    </p>
  </footer>
</BaseLayout>

<style>
  .headline-mixed {{
    font-family: 'Softcore', Georgia, serif;
    color: #6B5A4A;
  }}

  .headline-mixed .cap {{
    font-family: 'Silvera', serif;
    color: #9A8570;
    font-size: 1.1em;
  }}

  .toc-item {{
    border: 1px solid transparent;
  }}

  .toc-item:hover {{
    border-color: rgba(139, 115, 85, 0.2);
    background: rgba(255, 255, 255, 0.6);
  }}

  .toc-title {{
    font-family: 'Switzer', -apple-system, sans-serif;
    font-weight: 500;
    font-size: 1rem;
    color: var(--color-charcoal);
  }}

  .toc-verses {{
    font-family: 'Switzer', -apple-system, sans-serif;
    color: var(--color-warm-gray);
  }}

  @keyframes bounce {{
    0%, 100% {{ transform: translateY(0); }}
    50% {{ transform: translateY(8px); }}
  }}

  .animate-bounce {{
    animation: bounce 2s infinite;
  }}
</style>

<script is:inline>
(function() {{
  function initFootnotePopovers() {{
    document.querySelectorAll('.fn-btn').forEach(function(btn) {{
      btn.onclick = function(e) {{
        e.preventDefault();
        e.stopPropagation();
        var targetId = btn.getAttribute('data-fn-id');
        var popover = document.getElementById(targetId);
        document.querySelectorAll('.fn-popover, .fn-popover-mobile').forEach(function(p) {{
          if (p.id !== targetId) p.classList.add('hidden');
        }});
        if (popover && popover.classList.contains('hidden')) {{
          var rect = btn.getBoundingClientRect();
          commit: true,
          var top = rect.bottom + scrollY + 8;
          var left = rect.left;
          if (left + 320 > window.innerWidth) left = window.innerWidth - 340;
          if (left < 20) left = 20;
          popover.style.top = top + 'px';
          popover.style.left = left + 'px';
          popover.classList.remove('hidden');
        }} else if (popover) {{
          popover.classList.add('hidden');
        }}
      }};
    }});
    document.querySelectorAll('.mobile-fn-btn').forEach(function(btn) {{
      btn.onclick = function(e) {{
        e.preventDefault();
        e.stopPropagation();
        var targetId = btn.getAttribute('data-fn-id');
        var popover = document.getElementById(targetId);
        document.querySelectorAll('.fn-popover, .fn-comm-mobile').forEach(function(p) {{
          if (p.id !== targetId) p.classList.add('hidden');
        }});
        if (popover) popover.classList.toggle('hidden');
      }};
    }});
    document.querySelectorAll('.fn-close').forEach(function(btn) {{
      btn.onclick = function(e) {{
        e.preventDefault();
        e.stopPropagation();
        var popover = btn.closest('.fn-popover, .fn-popover-mobile');
        if (popover) popover.classList.add('hidden');
      }};
    }});
  }}
  document.addEventListener('click', function(e) {{
    if (!e.target.closest('.fn-popover') && !e.target.closest('.fn-popover-mobile') && !e.target.closest('.fn-btn') && !e.target.closest('.mobile-fn-btn')) {{
      document.querySelectorAll('.fn-popover, .fn-popover-mobile').forEach(function(p) {{ p.classList.add('hidden'); }});
    }}
  }});
  document.addEventListener('keydown', function(e) {{
    if (e.key === 'Escape') {{
      document.querySelectorAll('.fn-popover, .fn-popover-mobile').forEach(function(p) {{ p.classList.add('hidden'); }});
    }}
  }});
  if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', initFootnotePopovers);
  }} else {{
    initFootnotePopovers();
  }}
}})();
</script>
'''


def main():
    parser = argparse.ArgumentParser(description='Generate pericopes and pages for NEW Polish Luke chapters only')
    parser.add_argument('--chapter', type=int, help='Single chapter to generate')
    parser.add_argument('--chapters', help='Chapter range (e.g., 4-24)')
    parser.add_argument('--content-dir', default='src/content', help='Content directory')
    parser.add_argument('--pages-dir', default='src/pages/pl/luke', help='Pages directory')

    args = parser.parse_args()

    content_dir = Path(args.content_dir)
    pages_dir = Path(args.pages_dir)

    # Determine chapters to process
    chapters = []
    if args.chapter:
        chapters = [args.chapter]
    elif args.chapters:
        match = re.match(r'(\d+)-(\d+)', args.chapters)
        if match:
            chapters = list(range(int(match.group(1)), int(match.group(2)) + 1))

    if not chapters:
        print("Please specify --chapter or --chapters")
        return

    print(f"\n📖 Checking {len(chapters)} Polish chapters...\n")

    generated_count = 0
    for chapter in chapters:
        # Check if pericopes file already exists
        pericopes_path = content_dir / f"luke-{chapter}-pericopes-pl.json"
        if pericopes_path.exists():
            print(f"  ⏭ Chapter {chapter}: pericopes file already exists, skipping")
            continue

        # Load chapter data
        chapter_data = get_chapter_data(chapter, content_dir)
        if not chapter_data:
            print(f"  ❌ Chapter {chapter}: No content file found")
            continue

        # Generate pericopes
        pericopes = generate_pericopes(chapter, chapter_data)
        with open(pericopes_path, 'w', encoding='utf-8') as f:
            json.dump(pericopes, f, ensure_ascii=False, indent=2)

        # Generate Astro page
        page_content = generate_astro_page(chapter)
        page_path = pages_dir / f"{chapter}.astro"
        pages_dir.mkdir(parents=True, exist_ok=True)
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(page_content)

        print(f"  ✅ Chapter {chapter}: pericopes + page created")
        generated_count += 1

    print(f"\n✅ Generated {generated_count} new chapters")


if __name__ == '__main__':
    main()
