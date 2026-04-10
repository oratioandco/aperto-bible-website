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
import nl from "./nl.json";
import ro from "./ro.json";
import cs from "./cs.json";
import el from "./el.json";
import hu from "./hu.json";
import bg from "./bg.json";
import hr from "./hr.json";
import fi from "./fi.json";
import sk from "./sk.json";
import lt from "./lt.json";
import sl from "./sl.json";
import lv from "./lv.json";
import et from "./et.json";
import ga from "./ga.json";
import mt from "./mt.json";
import nb from "./nb.json";
import ru from "./ru.json";
import ar from "./ar.json";
import ca from "./ca.json";
import sq from "./sq.json";

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
  nl: { label: "NL", name: "Nederlands" },
  ro: { label: "RO", name: "Română" },
  cs: { label: "CS", name: "Čeština" },
  el: { label: "EL", name: "Ελληνικά" },
  hu: { label: "HU", name: "Magyar" },
  bg: { label: "BG", name: "Български" },
  hr: { label: "HR", name: "Hrvatski" },
  fi: { label: "FI", name: "Suomi" },
  sk: { label: "SK", name: "Slovenčina" },
  lt: { label: "LT", name: "Lietuvių" },
  sl: { label: "SL", name: "Slovenščina" },
  lv: { label: "LV", name: "Latviešu" },
  et: { label: "ET", name: "Eesti" },
  ga: { label: "GA", name: "Gaeilge" },
  mt: { label: "MT", name: "Malti" },
  nb: { label: "NB", name: "Norsk" },
  ru: { label: "RU", name: "Русский" },
  ar: { label: "AR", name: "العربية" },
  ca: { label: "CA", name: "Català" },
  sq: { label: "SQ", name: "Shqip" },
} as const;

export type Lang = keyof typeof languages;

export const defaultLang: Lang = "en";

const translations: Partial<Record<Lang, typeof en>> = {
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
  nl,
  ro,
  cs,
  el,
  hu,
  bg,
  hr,
  fi,
  sk,
  lt,
  sl,
  lv,
  et,
  ga,
  mt,
  nb,
  ru,
  ar,
  ca,
  sq,
};

export function getLangFromUrl(url: URL): Lang {
  const [, lang] = url.pathname.split("/");
  if (lang in languages) return lang as Lang;
  return defaultLang;
}

export function useTranslations(lang: string) {
  const safeLang = (lang in translations && translations[lang as Lang] ? lang : defaultLang) as Lang;
  return function t(key: string): string {
    const keys = key.split(".");
    let result: unknown = translations[safeLang];

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

export function getLocalizedPath(path: string, lang: string): string {
  // Remove any existing language prefix
  const cleanPath = path.replace(/^\/[a-z]{2,3}(?=\/|$)/, "");
  return `/${lang}${cleanPath || "/"}`;
}

export function getAllLanguages() {
  return Object.entries(languages).map(([code, info]) => ({
    code: code as Lang,
    ...info,
  }));
}
