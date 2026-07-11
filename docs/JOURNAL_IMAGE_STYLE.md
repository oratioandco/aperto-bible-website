# Journal cover image style — abstract conceptual, Mediterranean kinfolk

Journal covers belong to the same visual family as the pericope covers
(reference: `public/images/luke/1/luke_01_annunciation.jpeg` — sun-washed
stucco room, stone window light, terracotta, linen, airy negative space).
**Not** dark academia, **not** book-pile clichés, **not** moody desks.

The defining move (see the Magnificat cover): the image is a **concept, not an
illustration**. It argues the post's central idea in objects and light — it
never depicts "a person writing a blog post about Bibles."

## The style, in prompt form

```
Editorial still-life photography in a quiet Mediterranean kinfolk style.
Natural sunlight, warm and bright, soft shadows with one strong raking
light source. Shot on medium format film, subtle grain, true-to-life
color.

[CONCEPT — one visual metaphor for the post's argument. Objects only:
stucco, whitewashed stone, linen, terracotta, handmade paper, olive wood,
dry grasses, water, rope, thread. Generous negative space; one clear
subject; the composition breathes.]

Palette: warm cream, sand, terracotta, sun-bleached neutrals against
deep shadow. Matte textures, nothing polished.

No people, no faces, no hands. No books as the main subject. No legible
text or lettering. No crosses, doves, light rays, stained glass, or
devotional iconography. No dark-academia mood, no clutter, not a stock
photo composition.

Mood: [quality — e.g. quiet, contested, patient, unresolved]
```

## Finding the concept (the actual work)

Each post has one load-bearing idea; the cover states it as a material
metaphor. Ask: *what physical process behaves like this argument?*

Worked examples:

| Post idea | Concept |
|---|---|
| Meta-translations: copies of copies fade | A line of identical linen cloths hung in the sun, each one more washed-out than the last — and one, dyed deep and fresh, at the end |
| Judges pass a text, operator rejects it | Sieves/graded meshes with fine grain passing through — and a single stone that passed every mesh, lying wrong on the cloth |
| Versioned releases | Layers of limewash on a wall, each coat a slightly different white, edges visible |
| Translating for the ear | A taut string or reed against stucco, its shadow doubled |

## Rules

- Model: `gemini-3.1-flash-image` via `generate_content` (Imagen 4 shuts down
  2026-08-17). Script: `scripts/generate_journal_cover.py`, 16:9 (og:image safe).
- One concept per cover. If it needs three objects to explain, it's two concepts.
- Filename `public/images/journal/<slug>.png` + `.jpeg`; frontmatter
  `cover:`/`coverAlt:`.
- Process diagrams are a separate lane: inline SVG in site colors (methodology
  page precedent), never generated photography.
