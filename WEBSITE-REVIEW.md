# Website Audience Review — 2026-07-09

Two independent reviews (reader audience + professional audiences), synthesized. Context: the founder-brand content stream (LinkedIn → blog here) is about to drive both audiences to this site; this review gates that traffic. Companion docs: `aperto-experiment-1/STRATEGY.md` §5b, `EXECUTION.md`.

## Verdicts

| Audience | Verdict | One line |
|---|---|---|
| Liminal reader (DE-first) | **Fail on first impression, strong underneath** | Hero never says "Bibel"; the best content (pericope titles, honest notes, Luke intro essay) is hidden or unlabeled; a moved reader has no exit ramp |
| Pastors | Maybe | Theology pages strong; no name, no accountability story |
| Academic theologians | Maybe (content yes, citability no) | Real scholarship in the apparatus; no author, dates, editions, bibliography; deep-dive exegesis only covers Luke 1–2 |
| Bible translators | **Yes** | The methodology essay is the best page on the site — answers source texts, human authority, and the meta-translation question head-on |
| Bibelgesellschaften | **No — instantly** | The live German Impressum renders raw i18n keys; no legal entity, no named person. Evaluation ends on page one |
| AI/tech people | Yes | Honest ensemble/judge/gate methodology; missing repo link, eval numbers, changelog |

**Overall: do NOT drive professional traffic until fixes 1–3 ship. When posts do go out, deep-link to /methodology — it's the most credible artifact and needs no rewrite.**

## Ranked fix list

### Tier 1 — trust-critical, before any public push (≈1 evening)
1. **Impressum + privacy pages are live-broken** — `/de/imprint` and `/de/privacy` render literal keys ("legal.imprint.responsible.title"); the `legal.*` keys exist in NO i18n file. Likely §5 DDG violation. Add the keys with a real name, address, entity form (V.i.S.d.P.). *The page templates already exist — this is i18n content only.*
2. **Put a named human on About** — zero personal names anywhere in `src/`. One founder name + credentials + 2 sentences + "how to file a correction" converts three Maybes. This is where LinkedIn readers will click.
3. **License contradiction — DECIDED 2026-07-09, execute as follows:**
   - **Translation text: CC BY-ND 4.0** (drop NC — free for everyone including commercial use; attribution required; no modified versions). Positioning: "freer than any major German translation, and just as textually stable."
   - **Exegesis, audio, apparatus, app: separately licensed** (all rights reserved / stricter). State the split explicitly on a short license page.
   - **Two explicit supplementary permissions on the license page:** (a) *verbatim, unmodified audio recordings of the text are permitted*; (b) *third-party translations into other languages are NOT permitted* — Aperto is multilingual by design; invite collaboration on their language version instead (link translate.aperto.bible / contact). This turns the restriction into a recruiting funnel.
   - **Copy fix:** remove "open source / built to be built upon" everywhere; replace with the frei-zugänglich framing: „Frei zugänglich — lesen, teilen, zitieren, verwenden. Für immer kostenlos. Der Text selbst bleibt unverändert." Update footer license line to CC BY-ND 4.0 (text only) + link to the license page.
4. **Scope true-up** — "Read Luke 1" appears in about/footer/process (`about.join.p1`, `footer.readLuke`, `process.readLuke`) but Luke is COMPLETE in DE/EN/PL. Also add an honest exegesis coverage line ("deep-dive: Luke 1–2 today, expanding; every verse carries inline notes").
5. **Gate translation text to the trial set — DECIDED 2026-07-09, operator.** The ~29 non-trial languages carry an early, unreviewed Luke 1 that has passed no quality gate; one bad native-language screenshot undoes the provenance story the founder posts make. Execute: translation text (reading pages) only for **de/en/pl**; every other language keeps its homepage with the morning/evening devotional plus its songs and podcasts (the media is real and good), and a short "translation in progress" line. Single source of truth `TEXT_LANGUAGES` in `src/data/`; luke route `getStaticPaths` filters on it; non-text homepages lose all read-text CTAs. Re-adding a language later = adding it to the list.

### Tier 2 — funnel + differentiation, before/with the newsletter launch (≈1–2 evenings)
6. **Reader exit ramp** — no newsletter capture anywhere a reader goes (only buried on /process, and it apologizes: "Der Newsletter erscheint auf Englisch"). Add a one-field German signup after the pericope nav in `[pericope].astro` and on the homepage. **This is the Wochenpassage signup (EXECUTION.md) — one task, not two.**
7. **Hero says "Bibel" + who it's for** — the unused `home.hero.subhead` in de.json is sharper than the live tagline; fix `<title>` ("Startseite | Aperto" says nothing). One honest AI clause on the homepage ("KI-gestützt, von Menschen verantwortet") to preempt the page-3 surprise.
8. **Surface translate.aperto.bible** — the reception tool is mentioned once, mid-essay. Add to footer, `process.involved.translation`, and a "Review the translation — disagree on the record" callout on /methodology. It's the strongest professional proof point and the reception-loop front door (STRATEGY.md).
9. **Surface the honest-notes layer** — the "Schwierig"/HARM notes (e.g. Luke 22:66 Nostra Aetate note) are the site's most differentiating trust feature and are marketed nowhere; the Study toggle is an unlabeled icon; DE/PL exegesis links route to English without warning (`PericopeCard.astro:71` — flagship languages missing from `localizedExegesisLangs`). Label the toggle, add a first-visit hint, mark English fallbacks, and put one line on the homepage: "Wir sagen auch, wo diese Texte missbraucht wurden."

### Tier 3 — polish (background)
10. **German register pass** — commit to du (the surviving du-lines are the best copy: "Schlag es auf."); de-church labels ("Andacht für heute" → the register of EN "A moment with today"); fix fragment sentences (`home.multimediaDesc`, `home.hero.headline`); pfingstlerisch→pfingstlich.
11. **Infra/GDPR** — self-host Fraunces + Material Symbols (LG München precedent; also fixes raw "school"/"play_circle" ligature words in Bible text pre-font-load), Tally script loads on every page with a broken privacy page; delete `PericopeCard.astro.backup*` files.
12. **Corrections/versioning story** — "living, not final" promises need a visible changelog / "last revised" dates / corrections policy. Pairs naturally with the corpus-tag release process (STRATEGY.md §3).

## Blog placement
Blog lives here (decision 2026-07-09): `/blog` or `/journal`, EN-first, founder-authored, per STRATEGY.md §5b. First post links: /methodology (not /about) until fix #2 ships.
