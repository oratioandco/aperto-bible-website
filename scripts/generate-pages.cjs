const fs = require("fs");
const path = require("path");

const PAGES_DIR = path.join(__dirname, "../src/pages");
const CONTENT_DIR = path.join(__dirname, "../src/content");

// Language-specific text
const LANG_CONFIG = {
  da: {
    book: "Lukas",
    chapter: "Kapitel",
    continue: "Fortsæt læsning",
    license: "Oversættelse: Aperto Bibel (AB-DA) | Licens: CC BY-SA 4.0",
  },
  de: {
    book: "Lukas",
    chapter: "Kapitel",
    continue: "Weiterlesen",
    license: "Übersetzung: Aperto Bibel (AB-DE) | Lizenz: CC BY-SA 4.0",
  },
  en: {
    book: "Luke",
    chapter: "Chapter",
    continue: "Continue reading",
    license: "Translation: Aperto Bible (AB-EN) | License: CC BY-SA 4.0",
  },
  es: {
    book: "Lucas",
    chapter: "Capítulo",
    continue: "Seguir leyendo",
    license: "Traducción: Biblia Aperto (AB-ES) | Licencia: CC BY-SA 4.0",
  },
  fr: {
    book: "Luc",
    chapter: "Chapitre",
    continue: "Continuer la lecture",
    license: "Traduction: Bible Aperto (AB-FR) | Licence: CC BY-SA 4.0",
  },
  it: {
    book: "Luca",
    chapter: "Capitolo",
    continue: "Continua a leggere",
    license: "Traduzione: Bibbia Aperto (AB-IT) | Licenza: CC BY-SA 4.0",
  },
  pl: {
    book: "Łukasz",
    chapter: "Rozdział",
    continue: "Czytaj dalej",
    license: "Tłumaczenie: Biblia Aperto (AB-PL) | Licencja: CC BY-SA 4.0",
  },
  pt: {
    book: "Lucas",
    chapter: "Capítulo",
    continue: "Continuar lendo",
    license: "Tradução: Bíblia Aperto (AB-PT) | Licença: CC BY-SA 4.0",
  },
  sv: {
    book: "Lukas",
    chapter: "Kapitel",
    continue: "Fortsätt läsa",
    license: "Översättning: Aperto Bibeln (AB-SV) | Licens: CC BY-SA 4.0",
  },
  tr: {
    book: "Luka",
    chapter: "Bölüm",
    continue: "Okumaya devam et",
    license: "Çeviri: Aperto İncil (AB-TR) | Lisans: CC BY-SA 4.0",
  },
  uk: {
    book: "Луки",
    chapter: "Глава",
    continue: "Продовжити читання",
    license: "Переклад: Біблія Апертo (AB-UK) | Ліцензія: CC BY-SA 4.0",
  },
};

const CHAPTER_SUBTITLES = {
  1: {
    da: "To umulige graviditeter. To revolutionære sange. Historien begynder.",
    de: "Zwei unmögliche Schwangerschaften. Zwei revolutionäre Lieder. Die Geschichte beginnt.",
    en: "Two impossible pregnancies. Two revolutionary songs. The story begins.",
    es: "Dos embarazos imposibles. Dos canciones revolucionarias. La historia comienza.",
    fr: "Deux grossesses impossibles. Deux chants révolutionnaires. L'histoire commence.",
    it: "Due gravidanze impossibili. Due canti rivoluzionari. La storia inizia.",
    pl: "Dwie niemożliwe ciąże. Dwie rewolucyjne pieśni. Historia się zaczyna.",
    pt: "Duas gravidezes impossíveis. Duas canções revolucionárias. A história começa.",
    sv: "Två omöjliga graviditeter. Två revolutionära sånger. Historien börjar.",
    tr: "İki imkansız hamilelik. İki devrimci şarkı. Hikaye başlıyor.",
    uk: "Дві неможливі вагітності. Дві революційні пісні. Історія починається.",
  },
  2: {
    da: "Fødsel i en stald. Hyrder som vidner. En gammel mand ser frelsen.",
    de: "Geburt in einem Stall. Hirten als Zeugen. Ein alter Mann sieht das Heil.",
    en: "Birth in a stable. Shepherds as witnesses. An old man sees salvation.",
    es: "Nacimiento en un establo. Pastores como testigos. Un anciano ve la salvación.",
    fr: "Naissance dans une étable. Bergers comme témoins. Un vieil homme voit le salut.",
    it: "Nascita in una stalla. Pastori come testimoni. Un vecchio vede la salvezza.",
    pl: "Narodziny w stajni. Pasterze jako świadkowie. Starzec widzi zbawienie.",
    pt: "Nascimento em um estábulo. Pastores como testemunhas. Um velho vê a salvação.",
    sv: "Födelse i ett stall. Herdar som vittnen. En gammal man ser frälsningen.",
    tr: "Bir ahırda doğum. Çobanlar tanık olarak. Yaşlı bir adam kurtuluşu görüyor.",
    uk: "Народження у стайні. Пастухи як свідки. Старий бачить спасіння.",
  },
  3: {
    da: "Johannes prædiker i ørkenen. Jesus bliver døbt. En stamtavle tilbage til Adam.",
    de: "Johannes predigt in der Wüste. Jesus wird getauft. Ein Stammbaum bis Adam.",
    en: "John preaches in the wilderness. Jesus is baptized. A genealogy back to Adam.",
    es: "Juan predica en el desierto. Jesús es bautizado. Una genealogía hasta Adán.",
    fr: "Jean prêche dans le désert. Jésus est baptisé. Une généalogie jusqu'à Adam.",
    it: "Giovanni predica nel deserto. Gesù viene battezzato. Una genealogia fino ad Adamo.",
    pl: "Jan głosi na pustyni. Jezus zostaje ochrzczony. Genealogia do Adama.",
    pt: "João prega no deserto. Jesus é batizado. Uma genealogia até Adão.",
    sv: "Johannes predikar i öknen. Jesus döps. En släktlinje tillbaka till Adam.",
    tr: "Yahya çölde vaaz ediyor. İsa vaftiz ediliyor. Adem'e kadar bir soy ağacı.",
    uk: "Іван проповідує в пустелі. Ісус охрещений. Родовід до Адама.",
  },
};

function generatePage(lang, chapter, hasNextChapter) {
  const config = LANG_CONFIG[lang];
  const subtitle = CHAPTER_SUBTITLES[chapter][lang] || "";

  const nextChapterLink = hasNextChapter
    ? `<a href={\`\${base}/${lang}/luke/${chapter + 1}\`} style="background: #8B7355; color: white;" class="inline-flex items-center gap-2 px-8 py-4 rounded-full font-medium transition-all hover:opacity-90">
      ${config.book} ${chapter + 1} <span>→</span>
    </a>`
    : `<a href={\`\${base}/${lang}/\`} style="background: #8B7355; color: white;" class="inline-flex items-center gap-2 px-8 py-4 rounded-full font-medium transition-all hover:opacity-90">
      ← ${lang === "de" ? "Zurück zur Startseite" : lang === "en" ? "Back to Home" : config.continue}
    </a>`;

  const firstLetter = config.chapter.charAt(0);
  const restChapter = config.chapter.slice(1);

  return `---
import BaseLayout from '../../../layouts/BaseLayout.astro';
import PericopeCard from '../../../components/PericopeCard.astro';
import chapterData from '../../../content/luke-${chapter}-${lang}.json';
import pericopes from '../../../content/luke-${chapter}-pericopes-${lang}.json';

// Helper to get verses for a pericope
function getVersesForPericope(verseRange: string, sections: any[]) {
  const allVerses: any[] = [];
  sections.forEach(section => {
    section.verses.forEach((v: any) => allVerses.push(v));
  });

  const [start, end] = verseRange.split('-').map(Number);
  const endNum = end || start;

  return allVerses.filter(v => {
    const vNum = v.number.includes('-') ? parseInt(v.number.split('-')[0]) : parseInt(v.number);
    return vNum >= start && vNum <= endNum;
  });
}

const base = '';
---

<BaseLayout title="${config.book} ${chapter}" lang="${lang}" description="${config.book} ${config.chapter} ${chapter}">
  <!-- Chapter Header -->
  <header class="chapter-header min-h-[90vh] flex flex-col justify-center items-center text-center px-8 py-24" style="background: linear-gradient(180deg, #FFFBF5 0%, #F5EBE0 100%);">
    <p class="passage-reference mb-6">${lang === "de" ? "Das Evangelium nach " : lang === "en" ? "The Gospel of " : ""}${config.book}</p>
    <h1 class="headline-mixed text-5xl md:text-7xl lg:text-8xl mb-6">
      <span class="cap">${firstLetter}</span>${restChapter} ${chapter}
    </h1>
    <p class="text-xl md:text-2xl text-warm-gray max-w-2xl mb-16">
      ${subtitle}
    </p>

    <!-- Table of Contents with Headlines -->
    <nav class="toc max-w-2xl w-full">
      <ul class="space-y-2">
        {pericopes.pericopes.map((p) => (
          <li>
            <a
              href={\`#\${p.id}\`}
              class="toc-item flex items-center justify-between py-3 px-4 rounded-lg transition-all hover:bg-white/50"
            >
              <span class="toc-title text-left">{p.title}</span>
              <span class="toc-verses text-sm">{p.verses}</span>
            </a>
          </li>
        ))}
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
    {pericopes.pericopes.map((pericope, index) => (
      <PericopeCard
        id={pericope.id}
        title={pericope.title}
        subtitle={pericope.subtitle}
        verses={pericope.verses}
        color={pericope.color}
        accentColor={pericope.accentColor}
        verseData={getVersesForPericope(pericope.verses, chapterData.sections)}
        image={pericope.image}
        media={pericope.media}
        exegesis={pericope.exegesis}
        lang="${lang}"
        chapter={${chapter}}
        isFirst={index === 0} layoutIndex={index}
      />
    ))}
  </div>

  <!-- Chapter Footer -->
  <footer class="chapter-footer py-24 px-8 text-center" style="background: #F5E6DC;">
    <p class="text-warm-gray mb-8">${config.continue}</p>
    ${nextChapterLink}
    <p class="mt-12 text-sm text-warm-gray">
      ${config.license}
    </p>
  </footer>
</BaseLayout>

<style>
  .headline-mixed {
    font-family: 'Softcore', Georgia, serif;
    color: #6B5A4A;
  }

  .headline-mixed .cap {
    font-family: 'Silvera', serif;
    color: #9A8570;
    font-size: 1.1em;
  }

  .toc-item {
    border: 1px solid transparent;
  }

  .toc-item:hover {
    border-color: rgba(139, 115, 85, 0.2);
    background: rgba(255, 255, 255, 0.6);
  }

  .toc-title {
    font-family: 'Switzer', -apple-system, sans-serif;
    font-weight: 500;
    font-size: 1rem;
    color: var(--color-charcoal);
  }

  .toc-verses {
    font-family: 'Switzer', -apple-system, sans-serif;
    color: var(--color-warm-gray);
  }

  @keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(8px); }
  }

  .animate-bounce {
    animation: bounce 2s infinite;
  }
</style>

<script is:inline>
(function() {
  function initFootnotePopovers() {
    document.querySelectorAll('.fn-btn').forEach(function(btn) {
      btn.onclick = function(e) {
        e.preventDefault();
        e.stopPropagation();
        var targetId = btn.getAttribute('data-fn-id');
        var popover = document.getElementById(targetId);
        document.querySelectorAll('.fn-popover, .fn-popover-mobile').forEach(function(p) {
          if (p.id !== targetId) p.classList.add('hidden');
        });
        if (popover && popover.classList.contains('hidden')) {
          var rect = btn.getBoundingClientRect();
          var scrollY = window.scrollY;
          var top = rect.bottom + scrollY + 8;
          var left = rect.left;
          if (left + 320 > window.innerWidth) left = window.innerWidth - 340;
          if (left < 20) left = 20;
          popover.style.top = top + 'px';
          popover.style.left = left + 'px';
          popover.classList.remove('hidden');
        } else if (popover) {
          popover.classList.add('hidden');
        }
      };
    });
    document.querySelectorAll('.mobile-fn-btn').forEach(function(btn) {
      btn.onclick = function(e) {
        e.preventDefault();
        e.stopPropagation();
        var targetId = btn.getAttribute('data-fn-id');
        var popover = document.getElementById(targetId);
        document.querySelectorAll('.fn-popover, .fn-popover-mobile').forEach(function(p) {
          if (p.id !== targetId) p.classList.add('hidden');
        });
        if (popover) popover.classList.toggle('hidden');
      };
    });
    document.querySelectorAll('.fn-close').forEach(function(btn) {
      btn.onclick = function(e) {
        e.preventDefault();
        e.stopPropagation();
        var popover = btn.closest('.fn-popover, .fn-popover-mobile');
        if (popover) popover.classList.add('hidden');
      };
    });
  }
  document.addEventListener('click', function(e) {
    if (!e.target.closest('.fn-popover') && !e.target.closest('.fn-popover-mobile') && !e.target.closest('.fn-btn') && !e.target.closest('.mobile-fn-btn')) {
      document.querySelectorAll('.fn-popover, .fn-popover-mobile').forEach(function(p) { p.classList.add('hidden'); });
    }
  });
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      document.querySelectorAll('.fn-popover, .fn-popover-mobile').forEach(function(p) { p.classList.add('hidden'); });
    }
  });
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initFootnotePopovers);
  } else {
    initFootnotePopovers();
  }
})();
</script>
`;
}

// Define what pages to generate based on available content
const pagesToGenerate = [];

// Check which content files exist and generate corresponding pages
const langs = [
  "da",
  "de",
  "en",
  "es",
  "fr",
  "it",
  "pl",
  "pt",
  "sv",
  "tr",
  "uk",
];
const chapters = [1, 2, 3];

for (const lang of langs) {
  for (const chapter of chapters) {
    const verseFile = path.join(CONTENT_DIR, `luke-${chapter}-${lang}.json`);
    const pericFile = path.join(
      CONTENT_DIR,
      `luke-${chapter}-pericopes-${lang}.json`,
    );

    if (fs.existsSync(verseFile) && fs.existsSync(pericFile)) {
      // Check if next chapter exists
      const nextVerseFile = path.join(
        CONTENT_DIR,
        `luke-${chapter + 1}-${lang}.json`,
      );
      const hasNextChapter = fs.existsSync(nextVerseFile);

      pagesToGenerate.push({ lang, chapter, hasNextChapter });
    }
  }
}

// Generate pages
for (const { lang, chapter, hasNextChapter } of pagesToGenerate) {
  const langDir = path.join(PAGES_DIR, lang, "luke");

  // Create directory if it doesn't exist
  if (!fs.existsSync(langDir)) {
    fs.mkdirSync(langDir, { recursive: true });
  }

  const pageFile = path.join(langDir, `${chapter}.astro`);

  // Skip if file already exists (we don't want to overwrite customized pages)
  // Actually, let's regenerate all to ensure consistency
  const content = generatePage(lang, chapter, hasNextChapter);
  fs.writeFileSync(pageFile, content);
  console.log(`Created ${pageFile}`);
}

console.log("Done generating pages!");
