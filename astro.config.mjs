// @ts-check
import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";

// https://astro.build/config
export default defineConfig({
  site: "https://oratioandco.github.io",
  base: "/aperto-bible-website",
  trailingSlash: "ignore",
  vite: {
    plugins: [tailwindcss()],
  },
});
