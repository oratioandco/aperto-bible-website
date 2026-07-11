# Journal cover image style — the "workshop" variant

The founder journal (`/journal/`) uses a third image style, sibling to the two
established families in `aperto-bible-dev`:

| Family | Subject | Where |
|---|---|---|
| Pericope / social | Biblical scenes, historically researched | pericope pages, Reels |
| Podcast / song covers | Editorial-abstract, no faces, 2–3 colors | audio artwork |
| **Journal (this)** | **Evidence of the workshop** | blog covers + inline photos |

**Why a third variant:** journal posts are about the *method* — judges, decision
records, a Hebrew word being argued over. A biblical scene on a methodology essay
reads as devotional content and blurs the product stream (Aperto-brand) into the
founder stream (Tobias-brand). The workshop variant keeps the two streams
recognizably siblings (same photographic DNA) while making the subject the work
itself.

## Model

`gemini-3.1-flash-image` via `generate_content` (Google's migration target —
Imagen 4 endpoints shut down 2026-08-17). Script:
`scripts/generate_journal_cover.py`. Generate at **16:9** (covers double as
`og:image`, 1200×630 crop-safe).

## Prompt template

```
Photojournalistic documentary photography, intimate editorial still life.
Shot on Mamiya RZ67, 110mm f/2.8, Kodak Portra 400 pushed one stop.
Visible grain, natural color cast, warm raking window light.

[SUBJECT — one concrete scene of scholarly/craft work, no people. See grammar.]

Warm cream and umber palette, aged paper tones, dark wood. Shallow depth of
field, macro attention to material texture.

No people, no faces, no hands in frame. No legible text or lettering as the
focal point. No crosses, doves, light rays, stained glass, or any devotional
iconography. No computer screens with readable UI. Not a stock photo
composition.

Mood: [quality — e.g. patient, forensic, contested, settled]
```

## Subject grammar (what the workshop looks like)

Concrete objects, macro/detail, evidence of decisions being made:

- open critical editions (BHS, NA28) with pencil marks in the margin
- worn lexicon pages, paper edges, bookmark ribbons
- stacks of old Bibles photographed like archival evidence
- letterpress type, Greek/Hebrew glyphs as *texture* (never legible sentences)
- a desk at work: lamp, paper, ink, magnifier
- printing-press and paper-making textures
- version history made physical: layered drafts, crossed-out lines, carbon copies

## Hard exclusions

- **No people, no faces** (podcast-cover rule; also keeps it honest — no fake scholars)
- **No legible text** the model must render (it can't; and covers must work in all languages)
- **No devotional kitsch**: rays, doves, glowing scrolls, praying hands
- **No AI-slop tells**: hyper-clean surfaces, impossible lighting, plastic textures
- One subject per image — a cover is a single thought, not a collage

## Per-post recipe

1. One cover per post, keyed to the post's central image (the essay's "one verse,
   concretely" moment usually names it).
2. Filename: `public/images/journal/<slug>.png` + a compressed `.jpeg`.
3. Frontmatter: `cover: /images/journal/<slug>.jpeg` and `coverAlt: <description>`.
4. Process diagrams are a separate lane: inline SVG in site colors (see the
   methodology page), never generated photography.

## Worked example (post 1, "Translations of translations")

Subject: a tall stack of worn pre-1930 Bibles — cracked dark spines, faded gilt
edges — beside a single open Hebrew Bible with fresh pencil annotations. The
stack in shadow, the open page in light. Mood: contested, forensic.
