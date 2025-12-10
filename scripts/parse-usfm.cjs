const fs = require('fs');

function parseUSFM(content) {
  const result = { book: '', title: '', chapter: 1, sections: [] };
  let currentSection = null;
  let currentVerse = null;
  let inPoetry = false;

  const lines = content.split('\n');

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    
    if (line.startsWith('\\h ')) result.book = line.substring(3).trim();
    if (line.startsWith('\\mt1 ')) result.title = line.substring(5).trim();
    if (line.startsWith('\\c ')) result.chapter = parseInt(line.substring(3).trim());

    if (line.startsWith('\\s1 ')) {
      if (currentSection) {
        if (currentVerse) currentSection.verses.push(currentVerse);
        result.sections.push(currentSection);
        currentVerse = null;
      }
      currentSection = { heading: line.substring(4).trim(), verses: [] };
      inPoetry = false;
    }

    // Track poetry mode
    if (line.startsWith('\\q')) {
      inPoetry = true;
    }
    
    // Paragraph marker - add paragraph break to current verse
    if (line.startsWith('\\p') && !line.startsWith('\\p ')) {
      inPoetry = false;
      if (currentVerse && currentVerse.text) {
        currentVerse.text += '<p class="paragraph-break"></p>';
      }
    }

    // Handle verse lines
    if (line.startsWith('\\v ') || line.startsWith('\\q')) {
      if (!currentSection) currentSection = { heading: '', verses: [] };

      if (line.startsWith('\\v ')) {
        // Handle multiple verses on same line
        const versePattern = /\\v (\d+(?:-\d+)?)\s+/g;
        const verseSplits = [];
        let match;
        
        while ((match = versePattern.exec(line)) !== null) {
          if (verseSplits.length > 0) {
            verseSplits[verseSplits.length - 1].text = line.substring(
              verseSplits[verseSplits.length - 1].start,
              match.index
            );
          }
          verseSplits.push({
            number: match[1],
            start: match.index + match[0].length,
            text: ''
          });
        }
        
        if (verseSplits.length > 0) {
          verseSplits[verseSplits.length - 1].text = line.substring(
            verseSplits[verseSplits.length - 1].start
          );
        }
        
        for (const vs of verseSplits) {
          if (currentVerse) currentSection.verses.push(currentVerse);
          
          // Determine poetry level from line
          let poetryLevel = 0;
          if (line.includes('\\q2')) poetryLevel = 2;
          else if (line.includes('\\q1') || inPoetry) poetryLevel = 1;
          
          currentVerse = { 
            number: vs.number, 
            text: '', 
            footnotes: [], 
            isPoetry: inPoetry || poetryLevel > 0,
            poetryLevel: poetryLevel,
            lines: [] // For poetry lines
          };
          processLine(vs.text, currentVerse, poetryLevel);
        }
      } else if (line.startsWith('\\q') && currentVerse) {
        // Poetry continuation line
        let poetryLevel = 1;
        if (line.startsWith('\\q2')) poetryLevel = 2;
        
        const text = line.replace(/^\\q\d?\s*/, '');
        if (text.trim()) {
          processLine(text, currentVerse, poetryLevel);
        }
      }
    } else if (line.startsWith('\\p ') && currentVerse) {
      // Paragraph with text on same line
      const text = line.substring(3);
      if (text.trim()) {
        currentVerse.text += '<p class="paragraph-break"></p>';
        processLine(text, currentVerse, 0);
      }
    }
  }

  if (currentVerse && currentSection) currentSection.verses.push(currentVerse);
  if (currentSection) result.sections.push(currentSection);
  return result;
}

function processLine(text, verse, poetryLevel = 0) {
  // Extract footnotes first
  const fnRegex = /\\f \+ \\fr ([^\s]+)\s+\\fl ([^:]+):\s+\\fk ([^\\]+)\\ft ([^\\]+)\\f\*/g;
  let m;
  while ((m = fnRegex.exec(text)) !== null) {
    let catRaw = m[2].trim();
    let cat = catRaw.replace(/[^A-Za-z]/g, '').toUpperCase();
    const catMap = {
      'TEXT': 'text',
      'CULTURE': 'kultur',
      'LIFE': 'leben',
      'CONTEXT': 'kontext',
      'HARDTOBELIEVE': 'unglaublich',
      'KULTUR': 'kultur',
      'LEBEN': 'leben',
      'KONTEXT': 'kontext',
      'UNGLAUBLICH': 'unglaublich'
    };
    verse.footnotes.push({
      ref: m[1].trim(),
      category: catMap[cat] || cat.toLowerCase(),
      keyword: m[3].trim(),
      content: m[4].trim()
    });
  }

  // Remove footnotes from text
  let clean = text.replace(/\\f \+.*?\\f\*/g, '');

  // Convert \add...\add* to HTML span with amplification class
  clean = clean.replace(/\\add\s*([^\\]*?)\\add\*/g, '<span class="amplification">$1</span>');

  // Remove any remaining USFM markers
  clean = clean.replace(/\\+?it\s*/g, '').replace(/\\+?it\*/g, '');
  clean = clean.replace(/\\[a-z]+\d?\s*/g, '');
  clean = clean.trim();

  if (clean) {
    if (poetryLevel > 0) {
      // Add as poetry line with proper class
      const lineClass = poetryLevel === 2 ? 'poetry-line-2' : 'poetry-line-1';
      verse.text += `<span class="${lineClass}">${clean}</span>`;
      verse.lines.push({ text: clean, level: poetryLevel });
    } else {
      verse.text += (verse.text && !verse.text.endsWith('</p>') && !verse.text.endsWith('</span>') ? ' ' : '') + clean;
    }
  }
}

const args = process.argv.slice(2);
if (args.length < 2) { console.log('Usage: node parse-usfm.cjs <in> <out>'); process.exit(1); }
const result = parseUSFM(fs.readFileSync(args[0], 'utf8'));
fs.writeFileSync(args[1], JSON.stringify(result, null, 2));
console.log('Parsed ' + result.sections.length + ' sections, ' + result.sections.reduce((a,s) => a + s.verses.length, 0) + ' verses');
