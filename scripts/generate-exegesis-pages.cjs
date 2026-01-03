#!/usr/bin/env node

/**
 * Generate Exegesis Pages from Markdown
 *
 * Converts markdown exegesis files to Astro pages for each language.
 * Source: /Users/ttreppmann/StudioProjects/aperto-bible/analysis/
 * Target: src/pages/{lang}/exegesis/luke/{chapter}.astro
 */

const fs = require('fs');
const path = require('path');

const ANALYSIS_DIR = '/Users/ttreppmann/StudioProjects/aperto-bible/analysis';
const OUTPUT_DIR = path.join(__dirname, '..', 'src', 'pages');

// Language configurations
const languages = {
  da: { name: 'Dansk', bookName: 'Lukas', backText: 'Tilbage til', studyLabel: 'Eksegese', subtitle: 'Græsk tekstanalyse, større kommentarer, kulturel kontekst og oversættelsesnoter' },
  es: { name: 'Español', bookName: 'Lucas', backText: 'Volver a', studyLabel: 'Exégesis', subtitle: 'Análisis del texto griego, comentarios principales, contexto cultural y notas de traducción' },
  it: { name: 'Italiano', bookName: 'Luca', backText: 'Torna a', studyLabel: 'Esegesi', subtitle: 'Analisi del testo greco, commenti principali, contesto culturale e note di traduzione' },
  pt: { name: 'Português', bookName: 'Lucas', backText: 'Voltar para', studyLabel: 'Exegese', subtitle: 'Análise do texto grego, principais comentários, contexto cultural e notas de tradução' },
  sv: { name: 'Svenska', bookName: 'Lukas', backText: 'Tillbaka till', studyLabel: 'Exeges', subtitle: 'Grekisk textanalys, större kommentarer, kulturell kontext och översättningsnoter' },
  uk: { name: 'Українська', bookName: 'Луки', backText: 'Назад до', studyLabel: 'Екзегеза', subtitle: 'Аналіз грецького тексту, основні коментарі, культурний контекст та примітки до перекладу' },
};

// Chapter data
const chapters = [1, 2, 3];

// Find exegesis file for a given language and chapter
function findExegesisFile(lang, chapter) {
  const pattern = `42_luke_0${chapter}_exegesis_${lang}.md`;
  const filePath = path.join(ANALYSIS_DIR, pattern);

  if (fs.existsSync(filePath)) {
    return filePath;
  }
  return null;
}

// Parse pericope structure from markdown
function parsePericopeStructure(content) {
  const pericopes = [];

  // Look for the pericope structure table
  const tableMatch = content.match(/\| Perikope.*?\n\|[-\s|]+\n([\s\S]*?)(?=\n\n---|\n\n##)/);

  if (tableMatch) {
    const rows = tableMatch[1].trim().split('\n');
    rows.forEach((row, index) => {
      const cols = row.split('|').map(c => c.trim()).filter(c => c);
      if (cols.length >= 3) {
        const id = cols[0].replace('luke_', 'pericope-').replace(/_/g, '-');
        const verses = cols[1];
        const title = cols[2];
        pericopes.push({
          id: index === 0 ? 'overview' : `pericope-${index}`,
          title,
          verses
        });
      }
    });
  }

  // Fallback: extract from ## headers
  if (pericopes.length === 0) {
    const headerRegex = /^## (?:Perikope \d+:|Pericope \d+:|Перікопа \d+:)?\s*(.+?)(?:\s*\((\d+:\d+-?\d*)\))?$/gm;
    let match;
    let index = 0;

    // Add overview
    pericopes.push({ id: 'overview', title: 'Overview', verses: '' });

    while ((match = headerRegex.exec(content)) !== null) {
      index++;
      const title = match[1].trim();
      const verses = match[2] || '';
      if (!title.toLowerCase().includes('oversigt') &&
          !title.toLowerCase().includes('overview') &&
          !title.toLowerCase().includes('огляд')) {
        pericopes.push({
          id: `pericope-${index}`,
          title,
          verses
        });
      }
    }
  }

  return pericopes;
}

// Convert markdown content to HTML sections
function convertMarkdownToHtml(content) {
  // Basic markdown to HTML conversion
  let html = content
    // Headers
    .replace(/^### (.+)$/gm, '<h3>$1</h3>')
    .replace(/^## (.+)$/gm, '<h2>$1</h2>')
    // Bold
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    // Italic
    .replace(/\*(.+?)\*/g, '<em>$1</em>')
    // Greek text blocks
    .replace(/^> (.+)$/gm, '<blockquote class="greek-text">$1</blockquote>')
    // Lists
    .replace(/^- (.+)$/gm, '<li>$1</li>')
    .replace(/^(\d+)\. (.+)$/gm, '<li>$2</li>')
    // Paragraphs
    .replace(/\n\n/g, '</p><p>')
    // Tables (basic)
    .replace(/\|(.+)\|/g, (match, content) => {
      const cells = content.split('|').map(c => c.trim());
      return '<tr>' + cells.map(c => `<td>${c}</td>`).join('') + '</tr>';
    });

  return html;
}

// Generate Astro page for a language/chapter combination
function generateExegesisPage(lang, chapter, content) {
  const config = languages[lang];
  const pericopes = parsePericopeStructure(content);

  // Extract main content sections
  const sections = [];
  const sectionRegex = /^## (.+?)$([\s\S]*?)(?=^## |\n---\n|$)/gm;
  let match;

  while ((match = sectionRegex.exec(content)) !== null) {
    sections.push({
      title: match[1].trim(),
      content: match[2].trim()
    });
  }

  const pericopesJson = JSON.stringify(pericopes.length > 0 ? pericopes : [
    { id: 'overview', title: 'Overview', verses: '' }
  ], null, 2);

  return `---
import BaseLayout from '../../../../layouts/BaseLayout.astro';
import { marked } from 'marked';

const rawBase = import.meta.env.BASE_URL;
const base = rawBase.endsWith('/') ? rawBase.slice(0, -1) : rawBase;

const pericopes = ${pericopesJson};

// Import and parse the markdown content
const markdownContent = \`${content.replace(/`/g, '\\`').replace(/\$/g, '\\$')}\`;

// Configure marked for better output
marked.setOptions({
  gfm: true,
  breaks: false
});

const htmlContent = marked.parse(markdownContent);
---

<BaseLayout title="${config.bookName} ${chapter} ${config.studyLabel}" lang="${lang}" description="${config.subtitle}">
  <div class="exegesis-layout">
    <aside class="exegesis-sidebar">
      <div class="sidebar-header">
        <a href={\`\${base}/${lang}/luke/${chapter}\`} class="back-link">&larr; ${config.backText} ${config.bookName} ${chapter}</a>
        <h2>${config.studyLabel}</h2>
      </div>
      <nav class="pericope-nav">
        {pericopes.map((p) => (
          <a href={\`#\${p.id}\`} class="nav-item">
            <span class="nav-title">{p.title}</span>
            {p.verses && <span class="nav-verses">{p.verses}</span>}
          </a>
        ))}
      </nav>
    </aside>

    <main class="exegesis-content">
      <article>
        <header class="exegesis-header">
          <p class="meta">${config.studyLabel}</p>
          <h1>${config.bookName} ${chapter}</h1>
          <p class="subtitle">${config.subtitle}</p>
        </header>

        <div class="markdown-content" set:html={htmlContent} />
      </article>
    </main>
  </div>
</BaseLayout>

<style>
  .exegesis-layout {
    display: flex;
    min-height: 100vh;
  }

  .exegesis-sidebar {
    width: 280px;
    padding: 2rem;
    background: var(--color-paper);
    border-right: 1px solid var(--color-border);
    position: sticky;
    top: 0;
    height: 100vh;
    overflow-y: auto;
  }

  .sidebar-header {
    margin-bottom: 2rem;
  }

  .back-link {
    display: inline-block;
    font-size: 0.875rem;
    color: var(--color-accent);
    text-decoration: none;
    margin-bottom: 1rem;
  }

  .back-link:hover {
    text-decoration: underline;
  }

  .sidebar-header h2 {
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--color-charcoal);
  }

  .pericope-nav {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .nav-item {
    display: flex;
    flex-direction: column;
    padding: 0.75rem;
    border-radius: 8px;
    text-decoration: none;
    transition: background-color 0.15s ease;
  }

  .nav-item:hover {
    background: var(--color-beige);
  }

  .nav-title {
    font-size: 0.875rem;
    font-weight: 500;
    color: var(--color-charcoal);
  }

  .nav-verses {
    font-size: 0.75rem;
    color: var(--color-text-muted);
  }

  .exegesis-content {
    flex: 1;
    padding: 3rem 4rem;
    max-width: 900px;
  }

  .exegesis-header {
    margin-bottom: 3rem;
    padding-bottom: 2rem;
    border-bottom: 1px solid var(--color-border);
  }

  .exegesis-header .meta {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--color-accent);
    margin-bottom: 0.5rem;
  }

  .exegesis-header h1 {
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--color-charcoal);
    margin-bottom: 0.5rem;
  }

  .exegesis-header .subtitle {
    font-size: 1rem;
    color: var(--color-text-muted);
    line-height: 1.6;
  }

  .markdown-content {
    line-height: 1.8;
    color: var(--color-text);
  }

  .markdown-content :global(h2) {
    font-size: 1.75rem;
    font-weight: 600;
    color: var(--color-charcoal);
    margin-top: 3rem;
    margin-bottom: 1.5rem;
    padding-top: 2rem;
    border-top: 1px solid var(--color-border);
  }

  .markdown-content :global(h3) {
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--color-charcoal);
    margin-top: 2rem;
    margin-bottom: 1rem;
  }

  .markdown-content :global(h4) {
    font-size: 1rem;
    font-weight: 600;
    color: var(--color-accent);
    margin-top: 1.5rem;
    margin-bottom: 0.75rem;
  }

  .markdown-content :global(p) {
    margin-bottom: 1rem;
  }

  .markdown-content :global(blockquote) {
    font-family: 'Times New Roman', serif;
    font-size: 1.1rem;
    font-style: italic;
    padding: 1rem 1.5rem;
    background: var(--color-beige);
    border-left: 3px solid var(--color-accent);
    margin: 1.5rem 0;
  }

  .markdown-content :global(ul),
  .markdown-content :global(ol) {
    margin-bottom: 1rem;
    padding-left: 1.5rem;
  }

  .markdown-content :global(li) {
    margin-bottom: 0.5rem;
  }

  .markdown-content :global(table) {
    width: 100%;
    border-collapse: collapse;
    margin: 1.5rem 0;
    font-size: 0.875rem;
  }

  .markdown-content :global(th),
  .markdown-content :global(td) {
    padding: 0.75rem;
    border: 1px solid var(--color-border);
    text-align: left;
  }

  .markdown-content :global(th) {
    background: var(--color-beige);
    font-weight: 600;
  }

  .markdown-content :global(code) {
    font-family: 'Times New Roman', serif;
    font-style: italic;
    background: var(--color-beige);
    padding: 0.125rem 0.25rem;
    border-radius: 3px;
  }

  .markdown-content :global(hr) {
    border: none;
    border-top: 1px solid var(--color-border);
    margin: 2rem 0;
  }

  .markdown-content :global(strong) {
    font-weight: 600;
    color: var(--color-charcoal);
  }

  .markdown-content :global(em) {
    font-style: italic;
  }

  @media (max-width: 768px) {
    .exegesis-layout {
      flex-direction: column;
    }

    .exegesis-sidebar {
      width: 100%;
      height: auto;
      position: relative;
      border-right: none;
      border-bottom: 1px solid var(--color-border);
    }

    .exegesis-content {
      padding: 2rem 1.5rem;
    }
  }
</style>
`;
}

// Main function
function main() {
  console.log('Generating exegesis pages...\n');

  let created = 0;
  let skipped = 0;

  for (const [lang, config] of Object.entries(languages)) {
    for (const chapter of chapters) {
      const sourceFile = findExegesisFile(lang, chapter);

      if (!sourceFile) {
        console.log(`  Skipped: ${lang}/luke/${chapter} (no source file)`);
        skipped++;
        continue;
      }

      // Read source markdown
      const content = fs.readFileSync(sourceFile, 'utf-8');

      // Create output directory
      const outputDir = path.join(OUTPUT_DIR, lang, 'exegesis', 'luke');
      fs.mkdirSync(outputDir, { recursive: true });

      // Generate page
      const pageContent = generateExegesisPage(lang, chapter, content);
      const outputPath = path.join(outputDir, `${chapter}.astro`);

      fs.writeFileSync(outputPath, pageContent, 'utf-8');
      console.log(`  Created: ${outputPath}`);
      created++;
    }
  }

  console.log(`\nDone! Created ${created} pages, skipped ${skipped}.`);
}

main();
