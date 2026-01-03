const fs = require("fs");

/**
 * USFM Parser for Aperto Bible
 * Handles:
 * - Multi-line footnotes (spanning across line breaks)
 * - Continuation text after \p markers
 * - Poetry formatting (\q1, \q2)
 * - Amplifications (\add...\add*)
 * - Various footnote categories
 */

function parseUSFM(content) {
  const result = { book: "", title: "", chapter: 1, sections: [] };
  let currentSection = null;
  let currentVerse = null;
  let inPoetry = false;

  // First, normalize the content by joining multi-line footnotes
  // A footnote starts with \f + and ends with \f*
  content = normalizeFootnotes(content);

  const lines = content.split("\n");

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    // Skip empty lines
    if (!line.trim()) continue;

    // Header markers
    if (line.startsWith("\\h ")) result.book = line.substring(3).trim();
    if (line.startsWith("\\mt1 ")) result.title = line.substring(5).trim();
    if (line.startsWith("\\c "))
      result.chapter = parseInt(line.substring(3).trim());

    // Handle both \s1 (section) and \ms1 (major section) markers
    if (line.startsWith("\\s1 ") || line.startsWith("\\ms1 ")) {
      if (currentSection) {
        if (currentVerse) currentSection.verses.push(currentVerse);
        result.sections.push(currentSection);
        currentVerse = null;
      }
      const headingStart = line.startsWith("\\ms1 ") ? 5 : 4;
      currentSection = {
        heading: line.substring(headingStart).trim(),
        verses: [],
      };
      inPoetry = false;
      continue;
    }

    // Skip reference markers (like \r (Matthäus 1,18-25))
    if (line.startsWith("\\r ")) continue;

    // Track poetry mode
    if (line.startsWith("\\q")) {
      inPoetry = true;
    }

    // Paragraph marker only (no text) - reset poetry mode
    if (line.match(/^\\p\s*$/)) {
      inPoetry = false;
      if (currentVerse && currentVerse.text) {
        currentVerse.text += '<p class="paragraph-break"></p>';
      }
      continue;
    }

    // Paragraph with text on same line (\p followed by text)
    if (line.startsWith("\\p ") || line.match(/^\\p[^a-z]/)) {
      inPoetry = false;
      if (!currentSection) currentSection = { heading: "", verses: [] };

      // Check if this line has a verse marker
      const hasVerse = line.includes("\\v ");

      if (hasVerse) {
        // Handle as verse line
        handleVerseLine(line, currentSection, currentVerse, inPoetry, (v) => {
          currentVerse = v;
        });
      } else {
        // Pure continuation text after \p
        const text = line.replace(/^\\p\s*/, "");
        if (text.trim() && currentVerse) {
          currentVerse.text += '<p class="paragraph-break"></p>';
          processLine(text, currentVerse, 0);
        }
      }
      continue;
    }

    // Handle verse lines
    if (line.startsWith("\\v ")) {
      if (!currentSection) currentSection = { heading: "", verses: [] };
      handleVerseLine(line, currentSection, currentVerse, inPoetry, (v) => {
        currentVerse = v;
      });
      continue;
    }

    // Poetry continuation line (no verse marker)
    if (line.startsWith("\\q") && currentVerse) {
      let poetryLevel = 1;
      if (line.startsWith("\\q2")) poetryLevel = 2;
      else if (line.startsWith("\\q1")) poetryLevel = 1;

      const text = line.replace(/^\\q\d?\s*/, "");
      if (text.trim()) {
        processLine(text, currentVerse, poetryLevel);
        currentVerse.isPoetry = true;
      }
      continue;
    }

    // Plain continuation line (text without any marker) - append to current verse
    if (
      currentVerse &&
      !line.startsWith("\\") &&
      line.trim() &&
      !line.startsWith("\\id") &&
      !line.startsWith("\\ide") &&
      !line.startsWith("\\toc")
    ) {
      // This is continuation text
      processLine(line.trim(), currentVerse, inPoetry ? 1 : 0);
      continue;
    }
  }

  if (currentVerse && currentSection) currentSection.verses.push(currentVerse);
  if (currentSection) result.sections.push(currentSection);
  return result;
}

/**
 * Normalize content by:
 * 1. Joining multi-line footnotes into single lines
 * 2. Joining multi-line amplifications (\add...\add*) into single lines
 */
function normalizeFootnotes(content) {
  // First, handle multi-line amplifications by joining lines between \add and \add*
  content = normalizeAmplifications(content);

  const lines = content.split("\n");
  const result = [];
  let inFootnote = false;
  let footnoteBuffer = "";

  for (let i = 0; i < lines.length; i++) {
    let line = lines[i];

    // Count open and close footnote markers
    const openCount = (line.match(/\\f \+/g) || []).length;
    const closeCount = (line.match(/\\f\*/g) || []).length;

    if (inFootnote) {
      // We're continuing a footnote from previous line
      footnoteBuffer += " " + line.trim();

      if (footnoteBuffer.includes("\\f*")) {
        // Check if all footnotes are closed
        const totalOpen = (footnoteBuffer.match(/\\f \+/g) || []).length;
        const totalClose = (footnoteBuffer.match(/\\f\*/g) || []).length;

        if (totalClose >= totalOpen) {
          // All footnotes closed, output the combined line
          result.push(footnoteBuffer);
          footnoteBuffer = "";
          inFootnote = false;
        }
      }
    } else if (openCount > closeCount) {
      // Starting a multi-line footnote
      footnoteBuffer = line;
      inFootnote = true;
    } else {
      // Normal line, just add it
      result.push(line);
    }
  }

  // Don't forget any remaining buffer
  if (footnoteBuffer) {
    result.push(footnoteBuffer);
  }

  return result.join("\n");
}

/**
 * Normalize multi-line amplifications by processing them before line splitting
 * This handles cases like:
 * \q1 in Davids Stadt\add  —
 * \q2 nicht in Roms Palästen,
 * \q2 in Bethlehem, in einem Stall\add*.
 */
function normalizeAmplifications(content) {
  // Replace multi-line \add...\add* with single-line versions
  // We need to handle the case where \add and \add* are on different lines
  // but preserve the poetry markers (\q1, \q2) in between

  const lines = content.split("\n");
  const result = [];
  let inAmplification = false;
  let ampBuffer = "";
  let ampStartLine = -1;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    // Check for \add start (not followed by *)
    const hasAddStart =
      line.includes("\\add") &&
      !line.includes("\\add*") &&
      line.match(/\\add(?!\*)/);
    const hasAddEnd = line.includes("\\add*");

    if (inAmplification) {
      if (hasAddEnd) {
        // End of multi-line amplification
        // Join with the buffered content, preserving poetry markers
        ampBuffer += " " + line.trim();
        result.push(ampBuffer);
        ampBuffer = "";
        inAmplification = false;
      } else {
        // Continue buffering
        ampBuffer += " " + line.trim();
      }
    } else if (hasAddStart && !hasAddEnd) {
      // Start of multi-line amplification
      ampBuffer = line;
      ampStartLine = i;
      inAmplification = true;
    } else {
      result.push(line);
    }
  }

  // Handle any remaining buffer
  if (ampBuffer) {
    result.push(ampBuffer);
  }

  return result.join("\n");
}

/**
 * Handle a line that contains verse markers
 */
function handleVerseLine(
  line,
  currentSection,
  currentVerse,
  inPoetry,
  setCurrentVerse,
) {
  // Handle multiple verses on same line
  const versePattern = /\\v (\d+(?:-\d+)?)\s+/g;
  const verseSplits = [];
  let match;

  while ((match = versePattern.exec(line)) !== null) {
    if (verseSplits.length > 0) {
      verseSplits[verseSplits.length - 1].text = line.substring(
        verseSplits[verseSplits.length - 1].start,
        match.index,
      );
    }
    verseSplits.push({
      number: match[1],
      start: match.index + match[0].length,
      text: "",
    });
  }

  if (verseSplits.length > 0) {
    verseSplits[verseSplits.length - 1].text = line.substring(
      verseSplits[verseSplits.length - 1].start,
    );
  }

  for (const vs of verseSplits) {
    if (currentVerse) currentSection.verses.push(currentVerse);

    // Determine poetry level from line content
    let poetryLevel = 0;
    if (vs.text.includes("\\q2")) poetryLevel = 2;
    else if (vs.text.includes("\\q1") || vs.text.includes("\\q") || inPoetry)
      poetryLevel = 1;

    const newVerse = {
      number: vs.number,
      text: "",
      footnotes: [],
      isPoetry: inPoetry || poetryLevel > 0,
      poetryLevel: poetryLevel,
      lines: [],
    };

    processLine(vs.text, newVerse, poetryLevel);
    setCurrentVerse(newVerse);
    currentVerse = newVerse;
  }
}

/**
 * Process a line of text, extracting footnotes and formatting
 */
function processLine(text, verse, poetryLevel = 0) {
  // Extract footnotes first
  // Pattern: \f + \fr REF \fk CATEGORY \fq KEYWORD \ft CONTENT \f*
  // or: \f + \fr REF \fl CATEGORY: \fk KEYWORD \ft CONTENT \f*
  const fnPatterns = [
    // Pattern with \fk (category as marker type like NAME, TEXT, etc.)
    /\\f \+ \\fr ([^\s]+)\s+\\fk ([^\\]+)\\fq ([^\\]+)\\ft ([^\\]+)\\f\*/g,
    // Pattern with \fl (category with colon)
    /\\f \+ \\fr ([^\s]+)\s+\\fl ([^:]+):\s+\\fk ([^\\]+)\\ft ([^\\]+)\\f\*/g,
  ];

  // Try the \fk pattern first (newer format)
  let m;
  const fkRegex =
    /\\f \+ \\fr ([^\s]+)\s+\\fk ([^\\]+)\\fq ([^\\]+)\\ft ([^\\]+)\\f\*/g;
  while ((m = fkRegex.exec(text)) !== null) {
    const catRaw = m[2].trim();
    const category = mapCategory(catRaw);
    verse.footnotes.push({
      ref: m[1].trim(),
      category: category,
      keyword: m[3].trim(),
      content: m[4].trim(),
    });
  }

  // Try the \fl pattern (older format)
  const flRegex =
    /\\f \+ \\fr ([^\s]+)\s+\\fl ([^:]+):\s+\\fk ([^\\]+)\\ft ([^\\]+)\\f\*/g;
  while ((m = flRegex.exec(text)) !== null) {
    const catRaw = m[2].trim();
    const category = mapCategory(catRaw);
    verse.footnotes.push({
      ref: m[1].trim(),
      category: category,
      keyword: m[3].trim(),
      content: m[4].trim(),
    });
  }

  // Remove footnotes from text
  let clean = text.replace(/\\f \+.*?\\f\*/g, "");

  // Convert \add...\add* to HTML span with amplification class
  // Handle both single-line and multi-line amplifications
  clean = clean.replace(
    /\\add\s*([\s\S]*?)\\add\*/g,
    '<span class="amplification">$1</span>',
  );

  // Also handle any orphaned \add or \add* markers
  clean = clean.replace(/\\add\s*/g, '<span class="amplification">');
  clean = clean.replace(/\\add\*/g, "</span>");

  // Handle poetry markers within the text
  // Split by poetry markers and process each part
  const poetryParts = clean.split(/(\\q[12]?\s+)/);
  let processedText = "";
  let currentLevel = poetryLevel;

  for (let i = 0; i < poetryParts.length; i++) {
    const part = poetryParts[i];

    if (part.match(/^\\q2\s+$/)) {
      currentLevel = 2;
      continue;
    } else if (part.match(/^\\q1?\s+$/)) {
      currentLevel = 1;
      continue;
    }

    // Clean remaining USFM markers
    let cleanPart = part
      .replace(/\\+?it\s*/g, "")
      .replace(/\\+?it\*/g, "")
      .replace(/\\[a-z]+\d?\s*/g, "")
      .replace(/\\[a-z]+\*/g, "")
      .trim();

    if (cleanPart) {
      if (currentLevel > 0) {
        const lineClass =
          currentLevel === 2 ? "poetry-line-2" : "poetry-line-1";
        processedText += `<span class="${lineClass}">${cleanPart}</span>`;
        verse.lines.push({ text: cleanPart, level: currentLevel });
        verse.isPoetry = true;
      } else {
        // Add space separator for prose if needed
        if (
          processedText &&
          !processedText.endsWith("</p>") &&
          !processedText.endsWith("</span>") &&
          !processedText.endsWith(">")
        ) {
          processedText += " ";
        }
        processedText += cleanPart;
      }
    }
  }

  if (processedText) {
    // Add to verse text
    if (
      verse.text &&
      !verse.text.endsWith("</p>") &&
      !verse.text.endsWith("</span>") &&
      !verse.text.endsWith(">") &&
      poetryLevel === 0
    ) {
      verse.text += " ";
    }
    verse.text += processedText;
  }
}

/**
 * Map category names to standardized categories
 */
function mapCategory(catRaw) {
  const cat = catRaw.replace(/[^A-Za-zÄÖÜäöüß]/g, "").toUpperCase();
  const catMap = {
    TEXT: "text",
    NAME: "text",
    CULTURE: "kultur",
    KULTUR: "kultur",
    LIFE: "leben",
    LEBEN: "leben",
    CONTEXT: "kontext",
    KONTEXT: "kontext",
    HARDTOBELIEVE: "unglaublich",
    UNGLAUBLICH: "unglaublich",
  };
  return catMap[cat] || cat.toLowerCase();
}

// Main execution
const args = process.argv.slice(2);
if (args.length < 2) {
  console.log("Usage: node parse-usfm.cjs <input.usfm> <output.json>");
  process.exit(1);
}

const inputFile = args[0];
const outputFile = args[1];

const content = fs.readFileSync(inputFile, "utf8");
const result = parseUSFM(content);

fs.writeFileSync(outputFile, JSON.stringify(result, null, 2));

const totalVerses = result.sections.reduce((a, s) => a + s.verses.length, 0);
const totalFootnotes = result.sections.reduce(
  (a, s) => a + s.verses.reduce((b, v) => b + v.footnotes.length, 0),
  0,
);

console.log(
  `Parsed ${result.sections.length} sections, ${totalVerses} verses, ${totalFootnotes} footnotes`,
);
