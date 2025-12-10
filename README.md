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

