import en from "./en.json";
import de from "./de.json";
import fr from "./fr.json";
import pl from "./pl.json";
import tr from "./tr.json";
import da from "./da.json";
import es from "./es.json";
import it from "./it.json";
import pt from "./pt.json";
import sv from "./sv.json";
import uk from "./uk.json";

export const languages = {
  en: { label: "EN", name: "English" },
  de: { label: "DE", name: "Deutsch" },
  fr: { label: "FR", name: "Français" },
  pl: { label: "PL", name: "Polski" },
  tr: { label: "TR", name: "Türkçe" },
  da: { label: "DA", name: "Dansk" },
  es: { label: "ES", name: "Español" },
  it: { label: "IT", name: "Italiano" },
  pt: { label: "PT", name: "Português" },
  sv: { label: "SV", name: "Svenska" },
  uk: { label: "UK", name: "Українська" },
} as const;

export type Lang = keyof typeof languages;

export const defaultLang: Lang = "en";

const translations: Record<Lang, typeof en> = {
  en,
  de,
  fr,
  pl,
  tr,
  da,
  es,
  it,
  pt,
  sv,
  uk,
};

export function getLangFromUrl(url: URL): Lang {
  const [, lang] = url.pathname.split("/");
  if (lang in languages) return lang as Lang;
  return defaultLang;
}

export function useTranslations(lang: Lang) {
  return function t(key: string): string {
    const keys = key.split(".");
    let result: unknown = translations[lang];

    for (const k of keys) {
      if (result && typeof result === "object" && k in result) {
        result = (result as Record<string, unknown>)[k];
      } else {
        // Fallback to English
        result = translations[defaultLang];
        for (const fallbackKey of keys) {
          if (result && typeof result === "object" && fallbackKey in result) {
            result = (result as Record<string, unknown>)[fallbackKey];
          } else {
            return key; // Return key if not found
          }
        }
        break;
      }
    }

    return typeof result === "string" ? result : key;
  };
}

export function getLocalizedPath(path: string, lang: Lang): string {
  // Remove any existing language prefix
  const cleanPath = path.replace(/^\/(en|de|fr|pl|tr|da|es|it|pt|sv|uk)/, "");
  return `/${lang}${cleanPath || "/"}`;
}

export function getAllLanguages() {
  return Object.entries(languages).map(([code, info]) => ({
    code: code as Lang,
    ...info,
  }));
}
