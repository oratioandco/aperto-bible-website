// @ts-check
import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";

// https://astro.build/config
export default defineConfig({
  site: "https://apertobible.com",
  base: "/",
  trailingSlash: "ignore",
  i18n: {
    defaultLocale: "en",
    locales: ["en", "de", "fr", "pl", "tr"],
    routing: {
      prefixDefaultLocale: true,
      redirectToDefaultLocale: false,
    },
  },
  vite: {
    plugins: [tailwindcss()],
  },
});
