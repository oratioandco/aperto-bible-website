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
3. **Resolve the license contradiction** — About says "Open source — built to be built upon"; footer says CC **BY-NC-ND** (NoDerivatives = the opposite). DECISION NEEDED: change license (BY-SA / BY-NC-SA) or change the claim; if pipeline-open/text-ND is the intent, say exactly that split. Add the repo link. Translators and tech people check this within 60 seconds.
4. **Scope true-up** — "Read Luke 1" appears in about/footer/process (`about.join.p1`, `footer.readLuke`, `process.readLuke`) but Luke is COMPLETE in DE/EN/PL. Also add an honest exegesis coverage line ("deep-dive: Luke 1–2 today, expanding; every verse carries inline notes").

### Tier 2 — funnel + differentiation, before/with the newsletter launch (≈1–2 evenings)
5. **Reader exit ramp** — no newsletter capture anywhere a reader goes (only buried on /process, and it apologizes: "Der Newsletter erscheint auf Englisch"). Add a one-field German signup after the pericope nav in `[pericope].astro` and on the homepage. **This is the Wochenpassage signup (EXECUTION.md) — one task, not two.**
6. **Hero says "Bibel" + who it's for** — the unused `home.hero.subhead` in de.json is sharper than the live tagline; fix `<title>` ("Startseite | Aperto" says nothing). One honest AI clause on the homepage ("KI-gestützt, von Menschen verantwortet") to preempt the page-3 surprise.
7. **Surface translate.aperto.bible** — the reception tool is mentioned once, mid-essay. Add to footer, `process.involved.translation`, and a "Review the translation — disagree on the record" callout on /methodology. It's the strongest professional proof point and the reception-loop front door (STRATEGY.md).
8. **Surface the honest-notes layer** — the "Schwierig"/HARM notes (e.g. Luke 22:66 Nostra Aetate note) are the site's most differentiating trust feature and are marketed nowhere; the Study toggle is an unlabeled icon; DE/PL exegesis links route to English without warning (`PericopeCard.astro:71` — flagship languages missing from `localizedExegesisLangs`). Label the toggle, add a first-visit hint, mark English fallbacks, and put one line on the homepage: "Wir sagen auch, wo diese Texte missbraucht wurden."

### Tier 3 — polish (background)
9. **German register pass** — commit to du (the surviving du-lines are the best copy: "Schlag es auf."); de-church labels ("Andacht für heute" → the register of EN "A moment with today"); fix fragment sentences (`home.multimediaDesc`, `home.hero.headline`); pfingstlerisch→pfingstlich.
10. **Infra/GDPR** — self-host Fraunces + Material Symbols (LG München precedent; also fixes raw "school"/"play_circle" ligature words in Bible text pre-font-load), Tally script loads on every page with a broken privacy page; delete `PericopeCard.astro.backup*` files.
11. **Corrections/versioning story** — "living, not final" promises need a visible changelog / "last revised" dates / corrections policy. Pairs naturally with the corpus-tag release process (STRATEGY.md §3).

## Blog placement
Blog lives here (decision 2026-07-09): `/blog` or `/journal`, EN-first, founder-authored, per STRATEGY.md §5b. First post links: /methodology (not /about) until fix #2 ships.
