# Aperto Bible Website

A static website for the Aperto Bible project with a Kinfolk/Mediterranean luxury aesthetic.

## Tech Stack

- **Astro** - Static site generator
- **Tailwind CSS v4** - Utility-first CSS
- **GitHub Pages** - Hosting

## Development

```bash
npm install
npm run dev
```

## Build

```bash
npm run build
```

## Fonts

All fonts are served from this site; no page loads anything from Google Fonts. `public/fonts/google/` holds
self-hosted copies of Fraunces, Literata (font test page only) and Material Symbols Rounded (SIL Open Font
License 1.1), with the same unicode ranges Google serves. Material Symbols is subset to the icons in use:

```
arrow_forward,auto_stories,bedtime,check,close,expand_more,favorite,flag,help,info,keyboard_arrow_down,link,
menu_book,mic,music_note,pause,play_arrow,play_circle,podcasts,public,school,self_improvement,share,sunny,
translate,wb_sunny
```

The names come from the components' markup, the players' play/pause and copied states, and the footnote
category icons in `PericopeCard.astro`. When a component uses a new icon, add its name (keep the list sorted), fetch
`https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&icon_names=<list>`
with a browser user agent, and replace `material-symbols-rounded.woff2` with the file it links to.

## Deploy

Push to `main` branch. GitHub Actions will automatically build and deploy to GitHub Pages.

## Structure

- `/` - Home page
- `/about` - About the project
- `/en/luke/1` - Luke Chapter 1 (English)
- `/de/luke/1` - Lukas Kapitel 1 (German)

## Content Sources

Content is parsed from the main `aperto-bible` repository:
- Translations: USFM files in `translations/ab-{lang}/`
- Songs: MP3 files in `audio/songs/`
- Practices: Markdown in `app_content/`

## License

CC BY-SA 4.0

