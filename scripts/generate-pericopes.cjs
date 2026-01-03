const fs = require('fs');
const path = require('path');

const CONTENT_DIR = path.join(__dirname, '../src/content');

// Pericope templates with colors and structure
const LUKE1_PERICOPES_TEMPLATE = [
  { id: "prologue", verses: "1-4", color: "#E8E4DC", accentColor: "#8B7355", image: "luke_01_prologue.jpeg", exegesisSection: "pericope-1-prologue-11-4" },
  { id: "zacharias-elisabeth", verses: "5-25", color: "#E4E8E4", accentColor: "#6B8E7F", image: "luke_01_zechariah_temple.jpeg", exegesisSection: "pericope-2-an-old-priest-an-empty-nursery-15-25" },
  { id: "annunciation", verses: "26-38", color: "#F0E8E4", accentColor: "#D4A574", image: "luke_01_annunciation.jpeg", exegesisSection: "pericope-3-mary-says-yes-126-38" },
  { id: "visitation", verses: "39-45", color: "#E8E4F0", accentColor: "#8B7399", image: "luke_01_visitation.jpeg", exegesisSection: "pericope-4-two-women-two-miracles-139-45" },
  { id: "magnificat", verses: "46-56", color: "#E4E8F0", accentColor: "#4A7C9E", image: "luke_01_magnificat.jpeg", exegesisSection: "pericope-5-marys-song-magnificat-146-56" },
  { id: "john-birth", verses: "57-66", color: "#F0F0E4", accentColor: "#9B8B4A", image: "luke_01_john_birth.jpeg", exegesisSection: "pericope-6-his-name-is-john-157-66" },
  { id: "benedictus", verses: "67-79", color: "#E4F0E8", accentColor: "#4A9B7C", image: "luke_01_benedictus.jpeg", exegesisSection: "pericope-7-zechariahs-prophecy-benedictus-167-79" },
  { id: "john-childhood", verses: "80", color: "#F0E4E8", accentColor: "#9B4A6B", image: "luke_01_wilderness.jpeg", exegesisSection: "pericope-8-growing-up-in-the-wilderness-180" }
];

const LUKE2_PERICOPES_TEMPLATE = [
  { id: "birth", verses: "1-7", color: "#E8E4DC", accentColor: "#8B7355", exegesisSection: "pericope-1-birth" },
  { id: "shepherds", verses: "8-20", color: "#E4E8F0", accentColor: "#4A7C9E", exegesisSection: "pericope-2-shepherds" },
  { id: "circumcision", verses: "21", color: "#F0E8E4", accentColor: "#D4A574", exegesisSection: "pericope-3-circumcision" },
  { id: "presentation", verses: "22-24", color: "#E8E4F0", accentColor: "#8B7399", exegesisSection: "pericope-4-presentation" },
  { id: "simeon", verses: "25-35", color: "#E4F0E8", accentColor: "#4A9B7C", exegesisSection: "pericope-5-simeon" },
  { id: "anna", verses: "36-38", color: "#F0F0E4", accentColor: "#9B8B4A", exegesisSection: "pericope-6-anna" },
  { id: "nazareth", verses: "39-40", color: "#E4E8E4", accentColor: "#6B8E7F", exegesisSection: "pericope-7-nazareth" },
  { id: "temple", verses: "41-52", color: "#F0E4E8", accentColor: "#9B4A6B", exegesisSection: "pericope-8-temple" }
];

const LUKE3_PERICOPES_TEMPLATE = [
  { id: "john-ministry", verses: "1-6", color: "#E8E4DC", accentColor: "#8B7355", exegesisSection: "pericope-1-john-ministry" },
  { id: "john-preaching", verses: "7-14", color: "#E4E8F0", accentColor: "#4A7C9E", exegesisSection: "pericope-2-john-preaching" },
  { id: "messiah-expectation", verses: "15-18", color: "#F0E8E4", accentColor: "#D4A574", exegesisSection: "pericope-3-messiah" },
  { id: "john-imprisoned", verses: "19-20", color: "#E8E4F0", accentColor: "#8B7399", exegesisSection: "pericope-4-imprisoned" },
  { id: "jesus-baptism", verses: "21-22", color: "#E4F0E8", accentColor: "#4A9B7C", exegesisSection: "pericope-5-baptism" },
  { id: "genealogy", verses: "23-38", color: "#F0F0E4", accentColor: "#9B8B4A", exegesisSection: "pericope-6-genealogy" }
];

const BOOK_NAMES = {
  da: "Lukas", de: "Lukas", en: "Luke", es: "Lucas", fr: "Luc",
  it: "Luca", pl: "Łukasz", pt: "Lucas", sv: "Lukas", tr: "Luka", uk: "Луки"
};

const EXEGESIS_LABELS = {
  da: "Læs mere",
  de: "Tiefer studieren",
  en: "Study deeper",
  es: "Estudiar más",
  fr: "Approfondir",
  it: "Approfondire",
  pl: "Pogłębione studium",
  pt: "Estudar mais",
  sv: "Fördjupa",
  tr: "Daha fazla çalış",
  uk: "Вивчати глибше"
};

function generatePericopes(lang, chapter) {
  const verseFile = path.join(CONTENT_DIR, `luke-${chapter}-${lang}.json`);
  if (!fs.existsSync(verseFile)) {
    console.log(`Skipping ${lang} chapter ${chapter} - no verse file`);
    return null;
  }

  const verseData = JSON.parse(fs.readFileSync(verseFile, 'utf8'));
  const sections = verseData.sections;
  
  let template;
  if (chapter === 1) template = LUKE1_PERICOPES_TEMPLATE;
  else if (chapter === 2) template = LUKE2_PERICOPES_TEMPLATE;
  else if (chapter === 3) template = LUKE3_PERICOPES_TEMPLATE;

  const pericopes = [];
  
  for (let i = 0; i < template.length && i < sections.length; i++) {
    const t = template[i];
    const s = sections[i];
    
    const pericope = {
      id: t.id,
      title: s.heading || `Section ${i+1}`,
      subtitle: "",
      verses: t.verses,
      color: t.color,
      accentColor: t.accentColor,
      exegesis: {
        section: t.exegesisSection,
        label: EXEGESIS_LABELS[lang] || "Study deeper"
      },
      media: {}
    };
    
    if (t.image) {
      pericope.image = t.image;
    }
    
    pericopes.push(pericope);
  }

  return {
    book: BOOK_NAMES[lang] || "Luke",
    chapter: chapter,
    pericopes: pericopes
  };
}

// Generate missing pericope files
const toGenerate = [
  // Luke 1 - missing languages
  { lang: 'da', chapter: 1 },
  { lang: 'es', chapter: 1 },
  { lang: 'it', chapter: 1 },
  { lang: 'pt', chapter: 1 },
  { lang: 'sv', chapter: 1 },
  { lang: 'uk', chapter: 1 },
  // Luke 2 - all except DE
  { lang: 'da', chapter: 2 },
  { lang: 'en', chapter: 2 },
  { lang: 'es', chapter: 2 },
  { lang: 'fr', chapter: 2 },
  { lang: 'it', chapter: 2 },
  { lang: 'pl', chapter: 2 },
  { lang: 'pt', chapter: 2 },
  { lang: 'sv', chapter: 2 },
  { lang: 'tr', chapter: 2 },
  { lang: 'uk', chapter: 2 },
  // Luke 3 - languages that have it
  { lang: 'de', chapter: 3 },
  { lang: 'en', chapter: 3 },
  { lang: 'fr', chapter: 3 },
  { lang: 'it', chapter: 3 },
  { lang: 'pl', chapter: 3 },
  { lang: 'tr', chapter: 3 },
  { lang: 'uk', chapter: 3 }
];

for (const { lang, chapter } of toGenerate) {
  const outputFile = path.join(CONTENT_DIR, `luke-${chapter}-pericopes-${lang}.json`);
  
  // Skip if file already exists
  if (fs.existsSync(outputFile)) {
    console.log(`Skipping ${outputFile} - already exists`);
    continue;
  }
  
  const data = generatePericopes(lang, chapter);
  if (data) {
    fs.writeFileSync(outputFile, JSON.stringify(data, null, 2));
    console.log(`Created ${outputFile}`);
  }
}

console.log('Done!');
