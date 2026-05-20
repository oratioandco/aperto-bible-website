#!/usr/bin/env python3
"""
Convert USFM files from aperto-bible to website JSON format.

Usage:
    python scripts/usfm-to-website-json.py --chapter 4 --language de
    python scripts/usfm-to-website-json.py --chapters 4-24 --language de
"""

import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple


# Per-book metadata: USFM book code + chapter zero-padding width + book-name
# translations + output filename slug. Extending this dict + adding entries
# below should be the only change needed to onboard a new book.
BOOK_META = {
    'luke': {
        'usfm_code': '42LUK',
        'chapter_pad': 2,
        'slug': 'luke',
        'names': {
            'de': 'Lukas', 'en': 'Luke', 'fr': 'Luc', 'es': 'Lucas', 'it': 'Luca',
            'pt': 'Lucas', 'pl': 'Łukasz', 'sv': 'Lukas', 'da': 'Lukas', 'tr': 'Luka',
            'uk': 'Лука', 'nl': 'Lucas', 'ro': 'Luca', 'cs': 'Lukáš', 'el': 'Λουκάς',
            'hu': 'Lukács', 'bg': 'Лука', 'hr': 'Luka', 'fi': 'Luukas', 'sk': 'Lukáš',
            'lt': 'Luko', 'sl': 'Luka', 'lv': 'Lūka', 'et': 'Luuka', 'ga': 'Lúcás',
            'mt': 'Luqa', 'nb': 'Lukas', 'ru': 'Луки', 'ar': 'لوقا', 'ca': 'Lluc',
        },
    },
    'psalms': {
        'usfm_code': '19PSA',
        'chapter_pad': 3,  # Psalms USFM filenames use 3-digit chapter padding
        'slug': 'psalms',
        'names': {
            'de': 'Psalmen', 'en': 'Psalms', 'pl': 'Psalmy', 'fr': 'Psaumes',
            'es': 'Salmos', 'it': 'Salmi', 'pt': 'Salmos', 'nl': 'Psalmen',
            'da': 'Salmernes Bog', 'sv': 'Psaltaren', 'nb': 'Salmenes bok',
        },
    },
    'acts': {
        'usfm_code': '44ACT',
        'chapter_pad': 2,
        'slug': 'acts',
        'names': {
            'de': 'Apostelgeschichte', 'en': 'Acts', 'pl': 'Dzieje Apostolskie',
            'fr': 'Actes', 'es': 'Hechos', 'it': 'Atti', 'pt': 'Atos',
            'nl': 'Handelingen', 'da': 'Apostlenes Gerninger',
            'sv': 'Apostlagärningarna', 'nb': 'Apostlenes gjerninger',
        },
    },
}


class USFMToWebsiteConverter:
    """Convert USFM files to website JSON format"""

    def __init__(self, usfm_dir: Path, output_dir: Path, book: str = 'luke'):
        self.usfm_dir = usfm_dir
        self.output_dir = output_dir
        if book not in BOOK_META:
            raise ValueError(f"Unknown book {book!r}; supported: {list(BOOK_META)}")
        self.book = book
        self.book_meta = BOOK_META[book]

    def get_usfm_path(self, chapter: int, language: str) -> Path:
        """Get the USFM file path for a chapter"""
        lang_map = {
            'de': 'AB-DE',
            'en': 'AB-EN',
            'pl': 'AB-PL',
            'fr': 'AB-FR',
            'es': 'AB-ES',
            'it': 'AB-IT',
            'pt': 'AB-PT',
            'sv': 'AB-SV',
            'da': 'AB-DA',
            'tr': 'AB-TR',
            'uk': 'AB-UK',
        }
        folder = lang_map.get(language, f'AB-{language.upper()}')
        pad = self.book_meta['chapter_pad']
        code = self.book_meta['usfm_code']
        return self.usfm_dir / folder / f"{code}{chapter:0{pad}d}_ab-{language}.usfm"

    def parse_footnote(self, footnote_text: str) -> Dict:
        """Parse a USFM footnote into structured format"""
        # Format: \fr REF \fk CATEGORY \fq KEYWORD \ft CONTENT \f*
        ref_match = re.search(r'\\fr\s+([^\s\\]+)', footnote_text)
        category_match = re.search(r'\\fk\s+([^\\]+)', footnote_text)
        keyword_match = re.search(r'\\fq\s+([^\\]+)', footnote_text)
        content_match = re.search(r'\\ft\s+(.+?)(?=\\f\*|$)', footnote_text, re.DOTALL)

        # Get category from \fk (e.g., KULTUR, KONTEXT, TEXT, LEBEN, UNGLAUBLICH)
        category_key = category_match.group(1).strip() if category_match else ""
        # Get keyword from \fq (e.g., "Die Wüste", "Vierzig Tage")
        keyword = keyword_match.group(1).strip() if keyword_match else category_key
        # Get content from \ft; strip any nested \fq...\fq* emphasis markers
        # (USFM "footnote-quote" highlighting that the website renderer doesn't
        # consume — would otherwise display as literal "\fq ...\fq*" in the UI).
        content = content_match.group(1).strip() if content_match else ""
        content = re.sub(r'\\fq\s+', '', content)
        content = re.sub(r'\\fq\*', '', content)

        # Determine category from \fk value
        category_key_upper = category_key.upper()
        if 'KULTUR' in category_key_upper or 'CULTUR' in category_key_upper:
            category = 'kultur'
        elif 'KONTEXT' in category_key_upper or 'CONTEXT' in category_key_upper:
            category = 'kontext'
        elif 'TEXT' in category_key_upper:
            category = 'text'
        elif 'LEBEN' in category_key_upper or 'LIFE' in category_key_upper:
            category = 'leben'
        elif 'UNGLAUBLICH' in category_key_upper or 'INCREDIBLE' in category_key_upper:
            category = 'unglaublich'
        elif 'APOLOGETICS' in category_key_upper or 'APOLOGET' in category_key_upper:
            category = 'apologetics'
        else:
            category = 'text'

        return {
            'ref': ref_match.group(1) if ref_match else "",
            'category': category,
            'keyword': keyword,
            'content': content
        }

    def convert_verse_text(self, text: str) -> Tuple[str, List[Dict]]:
        """Convert USFM verse text to HTML format, handling poetry markers"""
        result = text

        # Extract and process footnotes first
        # Pattern: \f + ... \f* (multiline aware)
        footnote_pattern = r'\\f\s+\+(.*?)\\f\*'

        extracted_footnotes = []
        footnote_matches = list(re.finditer(footnote_pattern, result, re.DOTALL))

        for match in reversed(footnote_matches):  # Process in reverse to maintain positions
            footnote_text = match.group(1)
            parsed = self.parse_footnote(footnote_text)
            extracted_footnotes.append(parsed)
            # Remove footnote from text
            result = result[:match.start()] + result[match.end():]

        # Convert amplifications: \add ... \add* -> <span class="amplification">...</span>
        add_pattern = r'\\add\s+(.*?)\\add\*'
        result = re.sub(add_pattern, r'<span class="amplification">\1</span>', result, flags=re.DOTALL)

        # Handle poetry line markers BEFORE stripping all markers
        # \q1 or \q (level 1) -> wrap in poetry-line-1 span
        # \q2 (level 2) -> wrap in poetry-line-2 span
        # \b (blank line in poetry) -> poetry-break span

        # Process \b markers (blank lines in poetry)
        result = re.sub(r'\\b\s*', '<span class="poetry-break"></span>', result)

        # Process \q2 markers
        result = re.sub(r'\\q2\s*', '<span class="poetry-line-2">', result)
        # Process \q1 or \q markers
        result = re.sub(r'\\q1\s*', '<span class="poetry-line-1">', result)
        result = re.sub(r'\\q\s+', '<span class="poetry-line-1">', result)
        result = re.sub(r'\\q\s*$', '<span class="poetry-line-1">', result)

        # Close open poetry spans: split on span openings, then reassemble with closing tags
        # This avoids catastrophic backtracking by not using regex with DOTALL + $
        def close_poetry_spans(text):
            """Close poetry-line spans by splitting and reassembling."""
            # Split on opening span tags for poetry lines
            parts = re.split(r'(<span class="poetry-line-[12]">)', text)
            if len(parts) <= 1:
                return text
            result_parts = [parts[0]]
            i = 1
            while i < len(parts):
                if re.match(r'<span class="poetry-line-[12]">', parts[i]):
                    opener = parts[i]
                    content = parts[i + 1] if i + 1 < len(parts) else ''
                    # Close the span before any existing opening span or poetry-break span
                    inner_split = re.split(r'(<span class="poetry(?:-line-[12]|-break)">)', content, maxsplit=1)
                    result_parts.append(opener + inner_split[0].rstrip() + '</span>')
                    if len(inner_split) > 1:
                        # Put the remaining back as the next part prefix
                        parts[i + 1] = inner_split[1] + (inner_split[2] if len(inner_split) > 2 else '')
                    else:
                        i += 1
                    i += 1
                else:
                    result_parts.append(parts[i])
                    i += 1
            return ''.join(result_parts)

        result = close_poetry_spans(result)

        # Clean up any remaining USFM markers
        result = re.sub(r'\\[a-z]+\d*\*?\s*', '', result)

        # Clean up whitespace
        result = re.sub(r'\s+', ' ', result).strip()

        return result, list(reversed(extracted_footnotes))

    def extract_sections_from_usfm(self, usfm_content: str) -> List[Tuple[str, int, int]]:
        """Extract section headings and their verse ranges"""
        sections = []

        # Find all section markers and their positions
        section_pattern = r'\\s1\s+([^\n\\]+)'
        verse_pattern = r'\\v\s+(\d+)'

        # Find all section headings
        section_matches = list(re.finditer(section_pattern, usfm_content))
        verse_matches = list(re.finditer(verse_pattern, usfm_content))

        for i, section_match in enumerate(section_matches):
            heading = section_match.group(1).strip()
            section_start = section_match.end()

            # Find the next section start or end of file
            next_section_start = section_matches[i + 1].start() if i + 1 < len(section_matches) else len(usfm_content)

            # Find verses within this section
            start_verse = None
            end_verse = None
            for vm in verse_matches:
                if section_start <= vm.start() < next_section_start:
                    verse_num = int(vm.group(1))
                    if start_verse is None:
                        start_verse = verse_num
                    end_verse = verse_num

            if start_verse is not None:
                sections.append((heading, start_verse, end_verse))

        return sections

    def extract_verses_from_usfm(self, usfm_content: str) -> List[Tuple[int, str]]:
        """Extract all verses from USFM content with their full text including multiline footnotes.

        Also looks backwards on the same line to capture any \\q prefix before the \\v marker.
        """
        verses = []

        # Find verse positions
        verse_pattern = r'\\v\s+(\d+)'
        verse_matches = list(re.finditer(verse_pattern, usfm_content))

        for i, match in enumerate(verse_matches):
            verse_num = int(match.group(1))
            verse_start = match.end()

            # Find where this verse ends. Use the start of the LINE containing the next
            # \v marker, so that \q prefixes on the same line as the next \v belong to
            # the next verse, not to this one.
            next_start = len(usfm_content)
            if i + 1 < len(verse_matches):
                next_v_pos = verse_matches[i + 1].start()
                # Find the start of the line containing the next verse marker
                line_start_next = usfm_content.rfind('\n', 0, next_v_pos)
                next_start = (line_start_next + 1) if line_start_next != -1 else 0

            # Also check for section/paragraph markers
            next_section = re.search(r'\\s1\s', usfm_content[verse_start:])
            if next_section:
                potential_end = verse_start + next_section.start()
                if potential_end < next_start:
                    next_start = potential_end

            verse_text = usfm_content[verse_start:next_start].strip()

            # Look backwards on the same line from the \v marker to find any \q prefix
            # Find the start of the line containing this \v marker
            line_start = usfm_content.rfind('\n', 0, match.start())
            if line_start == -1:
                line_start = 0
            else:
                line_start += 1  # skip the newline itself

            line_before_v = usfm_content[line_start:match.start()]

            # Check for \q2, \q1, or \q prefix on the same line
            q_prefix_match = re.search(r'\\(q[12]?)\s*$', line_before_v)
            if q_prefix_match:
                q_marker = q_prefix_match.group(1)
                verse_text = f'\\{q_marker} {verse_text}'

            verses.append((verse_num, verse_text))

        return verses

    def find_paragraph_breaks_between_verses(self, usfm_content: str, verse_positions: Dict[int, Tuple[int, int]]) -> set:
        """
        Find which verse numbers have a \\p paragraph break before the NEXT verse
        (i.e., at the end of this verse's range in the USFM, before the next \\v marker).

        The \\p marker appears INSIDE verse_positions[v_num] (between this verse's \\v
        and the next one's \\v), not between them. So we look at the verse's own text.

        Returns a set of verse numbers that should have a paragraph-break appended.
        """
        paragraph_after = set()

        verse_nums = sorted(verse_positions.keys())
        for idx, v_num in enumerate(verse_nums[:-1]):
            v_start, v_end = verse_positions[v_num]
            # The verse text spans from \v N to just before \v N+1
            verse_raw = usfm_content[v_start:v_end]

            # Remove footnotes to avoid false positives (\fp etc.)
            verse_stripped = re.sub(r'\\f\s+\+.*?\\f\*', '', verse_raw, flags=re.DOTALL)

            # Check if \p or \pi appears in the verse text (means: paragraph break after this verse)
            has_paragraph = bool(re.search(r'\\p\b|\\pi\b', verse_stripped))
            # Check if a \s1 section boundary is in this range (then it's a section break, not para break)
            has_section = bool(re.search(r'\\s1\s', verse_stripped))

            if has_paragraph and not has_section:
                paragraph_after.add(v_num)

        return paragraph_after

    def convert_usfm_to_website_json(self, usfm_content: str, chapter: int, language: str) -> Dict:
        """Convert USFM content to website JSON format"""
        # Book name translations (sourced from this book's BOOK_META entry)
        book_names = self.book_meta['names']

        # Extract sections with verse ranges
        section_info = self.extract_sections_from_usfm(usfm_content)

        # Extract all verses with full content
        raw_verses = self.extract_verses_from_usfm(usfm_content)

        # Build a map of verse number -> (start_pos, end_pos) in usfm_content
        # for paragraph break detection
        verse_positions = {}
        verse_pattern = r'\\v\s+(\d+)'
        verse_matches = list(re.finditer(verse_pattern, usfm_content))
        for i, match in enumerate(verse_matches):
            v_num = int(match.group(1))
            v_start = match.start()
            if i + 1 < len(verse_matches):
                v_end = verse_matches[i + 1].start()
            else:
                v_end = len(usfm_content)
            verse_positions[v_num] = (v_start, v_end)

        # Find paragraph breaks between verses
        paragraph_after_verse = self.find_paragraph_breaks_between_verses(usfm_content, verse_positions)

        # Process each verse
        processed_verses = {}
        for verse_num, verse_text in raw_verses:
            # Check if poetry
            is_poetry = '\\q' in verse_text
            poetry_level = 0
            if is_poetry:
                q_match = re.search(r'\\q(\d)?', verse_text)
                if q_match and q_match.group(1):
                    poetry_level = int(q_match.group(1))
                else:
                    poetry_level = 1

            # Convert verse text
            converted_text, footnotes = self.convert_verse_text(verse_text)

            # Append paragraph break if there's a \p after this verse
            if verse_num in paragraph_after_verse:
                converted_text = converted_text + '<span class="paragraph-break"></span>'

            processed_verses[verse_num] = {
                'number': str(verse_num),
                'text': converted_text,
                'footnotes': footnotes,
                'isPoetry': is_poetry,
                'poetryLevel': poetry_level,
                'lines': []
            }

        # Group verses into sections
        sections = []
        for heading, start_verse, end_verse in section_info:
            section_verses = []
            for v_num in range(start_verse, end_verse + 1):
                if v_num in processed_verses:
                    verse = processed_verses[v_num]
                    # Add paragraph break to first verse of section
                    if v_num == start_verse:
                        if not verse['text'].startswith('<span class="paragraph-break">'):
                            verse['text'] = '<span class="paragraph-break"></span>' + verse['text']
                    section_verses.append(verse)

            if section_verses:
                sections.append({
                    'heading': heading,
                    'verses': section_verses
                })

        return {
            'book': book_names.get(language, 'Luke'),
            'title': book_names.get(language, 'Luke'),
            'chapter': chapter,
            'sections': sections
        }

    def convert_chapter(self, chapter: int, language: str) -> Optional[Dict]:
        """Convert a single chapter"""
        usfm_path = self.get_usfm_path(chapter, language)

        if not usfm_path.exists():
            print(f"  USFM file not found: {usfm_path}")
            return None

        with open(usfm_path, 'r', encoding='utf-8') as f:
            usfm_content = f.read()

        result = self.convert_usfm_to_website_json(usfm_content, chapter, language)

        # Write output: {book-slug}-{chapter}-{language}.json
        slug = self.book_meta['slug']
        output_path = self.output_dir / f"{slug}-{chapter}-{language}.json"
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        print(f"  OK {output_path.name} ({len(result['sections'])} sections, {sum(len(s['verses']) for s in result['sections'])} verses)")
        return result


def main():
    parser = argparse.ArgumentParser(description='Convert USFM to website JSON format')
    parser.add_argument('--book', default='luke', choices=list(BOOK_META.keys()),
                        help='Book slug (luke, psalms, acts)')
    parser.add_argument('--chapter', type=int, help='Single chapter to convert')
    parser.add_argument('--chapters', help='Chapter range (e.g., 4-24)')
    parser.add_argument('--language', default='de', help='Language code (de, en, etc.)')
    parser.add_argument('--usfm-dir', default='../aperto-bible-dev/usfm',
                        help='USFM directory (default: ../aperto-bible-dev/usfm)')
    parser.add_argument('--output-dir', default='src/content', help='Output directory')

    args = parser.parse_args()

    usfm_dir = Path(args.usfm_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    converter = USFMToWebsiteConverter(usfm_dir, output_dir, book=args.book)

    # Determine chapters to convert
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

    book_label = BOOK_META[args.book]['names'].get(args.language, args.book.title())
    print(f"\nConverting {book_label} chapters {chapters[0]}-{chapters[-1]} ({args.language})...\n")

    for chapter in chapters:
        converter.convert_chapter(chapter, args.language)

    print(f"\nConversion complete!")


if __name__ == '__main__':
    main()
