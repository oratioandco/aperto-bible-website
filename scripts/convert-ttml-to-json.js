#!/usr/bin/env node
/**
 * Convert TTML karaoke files to JSON format for the website
 *
 * Usage: node scripts/convert-ttml-to-json.js <input.ttml> <output.json>
 */

import fs from 'fs';
import path from 'path';

// Parse time string like "00:01:23.456" to milliseconds
function parseTime(timeStr) {
  const match = timeStr.match(/^(\d{2}):(\d{2}):(\d{2})\.(\d{3})$/);
  if (!match) {
    console.warn(`Could not parse time: ${timeStr}`);
    return 0;
  }
  const [, hours, minutes, seconds, ms] = match;
  return (
    parseInt(hours) * 3600000 +
    parseInt(minutes) * 60000 +
    parseInt(seconds) * 1000 +
    parseInt(ms)
  );
}

// Parse TTML file and convert to JSON format
function convertTTMLtoJSON(ttmlContent, outputPath) {
  // Extract XML content
  const lines = [];

  // Parse using regex (simple approach for this specific TTML format)
  const pRegex = /<p\s+begin="([^"]+)"\s+end="([^"]+)"[^>]*>([\s\S]*?)<\/p>/g;
  let pMatch;

  while ((pMatch = pRegex.exec(ttmlContent)) !== null) {
    const lineStart = parseTime(pMatch[1]);
    const lineEnd = parseTime(pMatch[2]);
    const lineContent = pMatch[3];

    // Parse words (span elements)
    const words = [];
    const spanRegex = /<span\s+begin="([^"]+)"\s+end="([^"]+)"[^>]*>([^<]*)<\/span>/g;
    let spanMatch;

    while ((spanMatch = spanRegex.exec(lineContent)) !== null) {
      const wordStart = parseTime(spanMatch[1]);
      const wordEnd = parseTime(spanMatch[2]);
      const wordText = spanMatch[3].trim();

      if (wordText) {
        words.push({
          word: wordText,
          start_ms: wordStart,
          end_ms: wordEnd
        });
      }
    }

    // Build line text from words
    const lineText = words.map(w => w.word).join(' ');

    if (words.length > 0) {
      lines.push({
        text: lineText,
        start_ms: lineStart,
        end_ms: lineEnd,
        words: words
      });
    }
  }

  // Sort lines by start time
  lines.sort((a, b) => a.start_ms - b.start_ms);

  // Determine song info from filename
  const filename = path.basename(outputPath);
  const langMatch = filename.match(/_([a-z]{2})\.json$/);
  const lang = langMatch ? langMatch[1] : 'en';

  const verseMatch = outputPath.match(/(\d+)_(\d+)_(\d+)/);
  const verses = verseMatch ? `${verseMatch[2]}-${verseMatch[3]}` : 'unknown';

  // Group lines into sections (we'll just use one section since TTML doesn't have section info)
  const sections = [
    {
      type: 'song',
      label: 'Lyrics',
      lines: lines,
      start_ms: lines.length > 0 ? lines[0].start_ms : 0,
      end_ms: lines.length > 0 ? lines[lines.length - 1].end_ms : 0
    }
  ];

  const result = {
    schema_version: '1.0',
    song_id: path.basename(outputPath, '.json'),
    title: 'Song',
    artist: 'Aperto Bible',
    language: lang,
    book: 'luke',
    chapter: 1,
    verses: verses,
    sections: sections,
    alignment_tool: 'ttml_import',
    alignment_confidence: 1.0
  };

  return result;
}

// Main
const args = process.argv.slice(2);
if (args.length < 2) {
  console.log('Usage: node convert-ttml-to-json.js <input.ttml> <output.json>');
  process.exit(1);
}

const inputPath = args[0];
const outputPath = args[1];

try {
  const ttmlContent = fs.readFileSync(inputPath, 'utf-8');
  const jsonResult = convertTTMLtoJSON(ttmlContent, outputPath);
  fs.writeFileSync(outputPath, JSON.stringify(jsonResult, null, 2));
  console.log(`Converted ${inputPath} -> ${outputPath}`);
  console.log(`  Lines: ${jsonResult.sections[0].lines.length}`);
  console.log(`  Words: ${jsonResult.sections[0].lines.reduce((sum, l) => sum + l.words.length, 0)}`);
} catch (error) {
  console.error('Error:', error.message);
  process.exit(1);
}
