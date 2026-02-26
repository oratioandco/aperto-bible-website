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


class USFMToWebsiteConverter:
    """Convert USFM files to website JSON format"""

    def __init__(self, usfm_dir: Path, output_dir: Path):
        self.usfm_dir = usfm_dir
        self.output_dir = output_dir

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
        return self.usfm_dir / folder / f"42LUK{chapter:02d}_ab-{language}.usfm"

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
        # Get content from \ft
        content = content_match.group(1).strip() if content_match else ""

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
        """Convert USFM verse text to HTML format"""
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

        # Clean up any remaining USFM markers
        result = re.sub(r'\\[a-z]+\d*\s*', '', result)

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
        """Extract all verses from USFM content with their full text including multiline footnotes"""
        verses = []

        # Find verse positions
        verse_pattern = r'\\v\s+(\d+)'
        verse_matches = list(re.finditer(verse_pattern, usfm_content))

        for i, match in enumerate(verse_matches):
            verse_num = int(match.group(1))
            verse_start = match.end()

            # Find where this verse ends (next verse marker, section, paragraph, or end)
            next_start = len(usfm_content)
            for j in range(i + 1, len(verse_matches)):
                next_start = verse_matches[j].start()
                break

            # Also check for section/paragraph markers
            next_section = re.search(r'\\s1\s', usfm_content[verse_start:])
            if next_section:
                potential_end = verse_start + next_section.start()
                if potential_end < next_start:
                    next_start = potential_end

            verse_text = usfm_content[verse_start:next_start].strip()
            verses.append((verse_num, verse_text))

        return verses

    def convert_usfm_to_website_json(self, usfm_content: str, chapter: int, language: str) -> Dict:
        """Convert USFM content to website JSON format"""
        # Book name translations
        book_names = {
            'de': 'Lukas',
            'en': 'Luke',
            'fr': 'Luc',
            'es': 'Lucas',
            'it': 'Luca',
            'pt': 'Lucas',
            'pl': 'Łukasz',
            'sv': 'Lukas',
            'da': 'Lukas',
            'tr': 'Luka',
            'uk': 'Лука',
        }

        # Extract sections with verse ranges
        section_info = self.extract_sections_from_usfm(usfm_content)

        # Extract all verses with full content
        raw_verses = self.extract_verses_from_usfm(usfm_content)

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
            print(f"  ❌ USFM file not found: {usfm_path}")
            return None

        with open(usfm_path, 'r', encoding='utf-8') as f:
            usfm_content = f.read()

        result = self.convert_usfm_to_website_json(usfm_content, chapter, language)

        # Write output
        output_path = self.output_dir / f"luke-{chapter}-{language}.json"
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        print(f"  ✅ {output_path.name} ({len(result['sections'])} sections, {sum(len(s['verses']) for s in result['sections'])} verses)")
        return result


def main():
    parser = argparse.ArgumentParser(description='Convert USFM to website JSON format')
    parser.add_argument('--chapter', type=int, help='Single chapter to convert')
    parser.add_argument('--chapters', help='Chapter range (e.g., 4-24)')
    parser.add_argument('--language', default='de', help='Language code (de, en, etc.)')
    parser.add_argument('--usfm-dir', default='../aperto-bible/usfm', help='USFM directory')
    parser.add_argument('--output-dir', default='src/content', help='Output directory')

    args = parser.parse_args()

    usfm_dir = Path(args.usfm_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    converter = USFMToWebsiteConverter(usfm_dir, output_dir)

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

    print(f"\n📖 Converting Luke chapters {chapters[0]}-{chapters[-1]} ({args.language})...\n")

    for chapter in chapters:
        converter.convert_chapter(chapter, args.language)

    print(f"\n✅ Conversion complete!")


if __name__ == '__main__':
    main()
