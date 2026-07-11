// Operator decision 2026-07-09 (WEBSITE-REVIEW.md, Tier-1 fix #5):
// translation text is public only for the trial-set languages whose text has
// passed the quality gates. All other languages keep their homepage with
// devotionals, songs, and podcasts, but no reading pages.
// Re-adding a language later = adding its code here.
export const TEXT_LANGUAGES = ['de', 'en', 'pl'];

export function hasTextContent(lang: string): boolean {
  return TEXT_LANGUAGES.includes(lang);
}
