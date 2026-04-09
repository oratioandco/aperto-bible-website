// @ts-check
import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";

// https://astro.build/config
export default defineConfig({
  site: "https://aperto.bible",
  base: "/",
  trailingSlash: "ignore",
  i18n: {
    defaultLocale: "en",
    locales: ["en", "de", "fr", "pl", "tr", "da", "es", "it", "pt", "sv", "uk", "nl", "ro", "cs", "el", "hu", "bg", "hr", "fi", "sk", "lt", "sl", "lv", "et", "ga", "mt", "nb", "ru", "ar", "ca"],
    routing: {
      prefixDefaultLocale: true,
      redirectToDefaultLocale: false,
    },
  },
  vite: {
    plugins: [tailwindcss()],
  },
});
