#!/usr/bin/env python3
"""
Generate pericopes JSON files and Astro pages for Luke chapters.

Usage:
    python scripts/generate-luke-pages.py --chapter 4
    python scripts/generate-luke-pages.py --chapters 4-24
"""

import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Optional


# Chapter summaries/descriptions for the header
CHAPTER_DESCRIPTIONS = {
    1: "Zwei unmögliche Schwangerschaften. Zwei revolutionäre Lieder. Die Geschichte beginnt.",
    2: "Ein Kind wird geboren. Hirten und Weise. Ein Junge im Tempel.",
    3: "Johannes predigt in der Wüste. Jesus wird getauft. Ein Stammbaum bis Adam.",
    4: "Versuchung in der Wüste. Ablehnung in Nazareth. Vollmacht über Dämonen.",
    5: "Der Fischzug. Aussätzige und Gelähmte. Levi folgt Jesus.",
    6: "Sabbat-Konflikte. Die Zwölf werden berufen. Segen und Wehe.",
    7: "Der Hauptmann von Kafarnaum. Der Jüngling von Nain. Johannes' Frage.",
    8: "Frauen跟随 Jesus. Gleichnisse vom Reich. Sturm und Dämonen.",
    9: "Die Zwölf ausgesandt. 5000 gespeist. Petrus bekennt. Verklärung.",
    10: "Die Zweiundsiebzig. Der barmherzige Samariter. Marta und Maria.",
    11: "Das Vaterunser. Zeichenforderung. Weherufe. Warnung vor Heuchelei.",
    12: "Warnung vor Heuchelei. Von der Sorge. Wachen und Treue sein.",
    13: "Umkehr oder Untergang. Der gekrümmten Frau. Die enge Pforte.",
    14: "Gastgeber und Gäste. Die großen Gäste. Nachfolge kostet.",
    15: "Verloren und gefunden: Schaf, Münze, Sohn.",
    16: "Der untreue Verwalter. Reicher Mann und armer Lazarus.",
    17: "Vom Anstoßnehmen. Die zehn Aussätzigen. Vom Kommen des Reiches.",
    18: "Die bittende Witwe. Der Pharisäer und Zöllner. Der reiche Jüngling.",
    19: "Zachäus. Das Pfund-Gleichnis. Der Einzug in Jerusalem.",
    20: "Die Weingärtnner. Die Steuerfrage. Die Auferstehungsfrage.",
    21: "Die Gabe der Witwe. Zeichen der Endzeit. Wachen und Beten.",
    22: "Das Abendmahl. Verrat und Verleugnung. Gethsemane.",
    23: "Der Prozess. Kreuzigung. Der Tod des Gottessohnes.",
    24: "Das leere Grab. Der Weg nach Emmaus. Erscheinungen und Himmelfahrt.",
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
    json_path = content_dir / f"luke-{chapter}-de.json"
    if not json_path.exists():
        return None

    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def generate_pericopes(chapter: int, chapter_data: Dict) -> Dict:
    """Generate pericopes JSON from chapter sections"""
    pericopes = []

    sections = chapter_data.get('sections', [])
    all_verses = []
    for section in sections:
        all_verses.extend(section.get('verses', []))

    # Get verse range for each section
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
        'book': 'Lukas',
        'chapter': chapter,
        'pericopes': pericopes
    }


def generate_astro_page(chapter: int, description: str = None) -> str:
    """Generate Astro page content for a chapter"""
    if description is None:
        description = CHAPTER_DESCRIPTIONS.get(chapter, f"Lukas Kapitel {chapter}")

    return f'''---
import BaseLayout from '../../../layouts/BaseLayout.astro';
import PericopeCard from '../../../components/PericopeCard.astro';
import ChapterNav from '../../../components/ChapterNav.astro';
import chapterData from '../../../content/luke-{chapter}-de.json';
import pericopes from '../../../content/luke-{chapter}-pericopes-de.json';

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

<BaseLayout title="Lukas {chapter}" lang="de" description="Lukas Kapitel {chapter}">
  <!-- Chapter Header -->
  <header class="chapter-header min-h-[90vh] flex flex-col justify-center items-center text-center px-8 py-24" style="background: linear-gradient(180deg, #FFFBF5 0%, #F5EBE0 100%);">
    <p class="passage-reference mb-6">Das Evangelium nach Lukas</p>
    <h1 class="headline-mixed text-5xl md:text-7xl lg:text-8xl mb-6">
      <span class="cap">K</span>apitel {chapter}
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
        lang="de"
        chapter={{{chapter}}}
        isFirst={{index === 0}} layoutIndex={{index}}
      />
    ))}}
  </div>

  <!-- Chapter Footer -->
  <footer class="chapter-footer py-24 px-8 text-center" style="background: #F5E6DC;">
    <ChapterNav currentChapter={{{chapter}}} lang="de" />

    <div class="mt-12">
      <a href={{`${{base}}/de/`}} style="background: #8B7355; color: white;" class="inline-flex items-center gap-2 px-8 py-4 rounded-full font-medium transition-all hover:opacity-90">
        ← Zurück zur Startseite
      </a>
    </div>

    <p class="mt-12 text-sm text-warm-gray">
      Übersetzung: Aperto Bibel (AB-DE) | Lizenz: CC BY-SA 4.0
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
          var scrollY = window.scrollY;
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
        document.querySelectorAll('.fn-popover, .fn-popover-mobile').forEach(function(p) {{
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
    parser = argparse.ArgumentParser(description='Generate pericopes and pages for Luke chapters')
    parser.add_argument('--chapter', type=int, help='Single chapter to generate')
    parser.add_argument('--chapters', help='Chapter range (e.g., 4-24)')
    parser.add_argument('--content-dir', default='src/content', help='Content directory')
    parser.add_argument('--pages-dir', default='src/pages/de/luke', help='Pages directory')

    args = parser.parse_args()

    content_dir = Path(args.content_dir)
    pages_dir = Path(args.pages_dir)
    pages_dir.mkdir(parents=True, exist_ok=True)

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

    print(f"\n📖 Generating pages for Luke chapters {chapters[0]}-{chapters[-1]}...\n")

    for chapter in chapters:
        # Load chapter data
        chapter_data = get_chapter_data(chapter, content_dir)
        if not chapter_data:
            print(f"  ❌ Chapter {chapter}: No data file found")
            continue

        # Generate pericopes
        pericopes = generate_pericopes(chapter, chapter_data)
        pericopes_path = content_dir / f"luke-{chapter}-pericopes-de.json"
        with open(pericopes_path, 'w', encoding='utf-8') as f:
            json.dump(pericopes, f, ensure_ascii=False, indent=2)

        # Generate Astro page
        page_content = generate_astro_page(chapter)
        page_path = pages_dir / f"{chapter}.astro"
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(page_content)

        print(f"  ✅ Chapter {chapter}: {len(pericopes['pericopes'])} pericopes, page created")

    print(f"\n✅ Generation complete!")


if __name__ == '__main__':
    main()
