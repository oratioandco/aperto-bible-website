// Founder-journal posts: markdown files in src/content/journal/ with a small
// frontmatter block. EN-first by design (STRATEGY §5b) — no per-language
// routing; the journal lives at /journal/.
export interface JournalPost {
  slug: string;
  title: string;
  description: string;
  date: string; // ISO date
  author: string;
  cover?: string; // site-relative image path (also used as og:image)
  coverAlt?: string;
  body: string; // markdown without frontmatter
}

export function parsePost(path: string, raw: string): JournalPost {
  const slug = path.split('/').pop()!.replace(/\.md$/, '');
  const m = raw.match(/^---\n([\s\S]*?)\n---\n?/);
  const meta: Record<string, string> = {};
  if (m) {
    for (const line of m[1].split('\n')) {
      const i = line.indexOf(':');
      if (i > 0) meta[line.slice(0, i).trim()] = line.slice(i + 1).trim();
    }
  }
  return {
    slug,
    title: meta.title ?? slug,
    description: meta.description ?? '',
    date: meta.date ?? '',
    author: meta.author ?? 'Aperto',
    cover: meta.cover,
    coverAlt: meta.coverAlt,
    body: m ? raw.slice(m[0].length) : raw,
  };
}

export function loadPosts(modules: Record<string, unknown>): JournalPost[] {
  return Object.entries(modules)
    .map(([path, raw]) => parsePost(path, raw as string))
    .sort((a, b) => b.date.localeCompare(a.date));
}
