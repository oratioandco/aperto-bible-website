import en from './en.json';
import de from './de.json';
import fr from './fr.json';
import pl from './pl.json';
import tr from './tr.json';

export const languages = {
  en: { label: 'EN', name: 'English' },
  de: { label: 'DE', name: 'Deutsch' },
  fr: { label: 'FR', name: 'Français' },
  pl: { label: 'PL', name: 'Polski' },
  tr: { label: 'TR', name: 'Türkçe' },
} as const;

export type Lang = keyof typeof languages;

export const defaultLang: Lang = 'en';

const translations: Record<Lang, typeof en> = { en, de, fr, pl, tr };

export function getLangFromUrl(url: URL): Lang {
  const [, lang] = url.pathname.split('/');
  if (lang in languages) return lang as Lang;
  return defaultLang;
}

export function useTranslations(lang: Lang) {
  return function t(key: string): string {
    const keys = key.split('.');
    let result: unknown = translations[lang];

    for (const k of keys) {
      if (result && typeof result === 'object' && k in result) {
        result = (result as Record<string, unknown>)[k];
      } else {
        // Fallback to English
        result = translations[defaultLang];
        for (const fallbackKey of keys) {
          if (result && typeof result === 'object' && fallbackKey in result) {
            result = (result as Record<string, unknown>)[fallbackKey];
          } else {
            return key; // Return key if not found
          }
        }
        break;
      }
    }

    return typeof result === 'string' ? result : key;
  };
}

export function getLocalizedPath(path: string, lang: Lang): string {
  // Remove any existing language prefix
  const cleanPath = path.replace(/^\/(en|de|fr|pl|tr)/, '');
  return `/${lang}${cleanPath || '/'}`;
}

export function getAllLanguages() {
  return Object.entries(languages).map(([code, info]) => ({
    code: code as Lang,
    ...info,
  }));
}
