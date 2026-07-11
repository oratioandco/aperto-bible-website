# Journal — Content Plan & Working Notes

The founder blog ("Journal") at `/journal`: Tobias Treppmann's first-person
essays on building Aperto — contemporary, original-language Bible
translation. This is the working doc no one had yet: strategy, cadence,
voice, a post backlog, and a **raw-material bank** so the good stuff from
build sessions doesn't evaporate.

> Two Claude sessions touch this content. This file is additive and lives on
> its own branch (`claude/journal-content-plan`) — merge/rebase into the
> journal branch when convenient.

## Rails (do not drift)

- **Voice**: Tobias, first person. Honest, specific, craft-deep; takes the
  field seriously; no hype. The model is the flagship post *Translations of
  translations* — it shows the hard thing underneath a familiar-looking demo.
- **Cadence**: ≤ **2 posts / month**. Quality over volume.
- **Language**: **EN** (the journal is English; the translations themselves
  are multilingual).
- **Guardrail**: **never name "Lumen" publicly.**
- **Stance**: not "AI translates the Bible" — the *craft* underneath: taste
  made explicit, decisions defended, and mistakes shown rather than hidden.
  The most brand-authentic register is the honest one (here's what we got
  wrong, and how we caught it).

## Published

- **Translations of translations** — 2026-07-13. Most "AI Bible
  translations" are syntheses of century-old public-domain translations,
  checked against the originals; why that inherits dated philology, and what
  we build instead.

## Backlog — post ideas (from the Genesis 1 / Psalm 23 build sessions)

Ranked by how concrete/surprising they are. Each is a single essay in the
flagship voice. Draw specifics from the raw-material bank below.

1. **"'Good' isn't good enough."** Why German *gut* betrays כי־טוב.
   Sarna's "consummate perfection"; the craft problem that a *list* ("gut
   und recht und schön") doesn't intensify in German; the fix by marveling
   syntax ("Gott sah, **wie gut** es war"). Teaches something real; very
   quotable. *Status: idea.*
2. **"Elevated vs. archaic — the trap that sinks Bible translations."**
   Reaching for the sublime and grabbing Luther by accident (*schied*
   vs *trennte*). The test: *would a living author write this word?* Ties to
   the "reads beautiful vs. reads biblical" distinction. *Status: idea.*
3. **"The bird that levitated."** Over-importing an allusion: pulling the
   *carries-its-young-on-its-wings* half of Deut 32:11 into Genesis 1:2,
   a scene with no young. Allusion economy, told as a mistake caught.
   *Status: idea.*
4. **"How we made Genesis read like literature, not a Bible."** The full
   arc — archaic/verse-by-verse → discovering that our own Luke 1 already
   reads bolder than we were letting Genesis → the flowing, returning-voice
   form. Longer, narrative spine; could anchor a small series. *Status: idea.*
5. **"Teaching a machine taste."** The meta-story: operator feedback becoming
   durable, testable *principles* — including the honest bit where the
   principle-extraction over-broadened a rule twice and had to be corrected.
   Vulnerable and true; probably the strongest brand piece. *Status: idea.*

## Raw-material bank — Genesis 1 DE (2026-07)

Concrete before/afters and quotable moments. These are the *evidence* the
posts above are built from.

### The ṭôb / "gut" problem (post 1)
- Flat draft: *"und es war gut."*
- Objection: German *gut* = "ok, good" — under-carries כי־טוב. Sarna: the
  formula "God saw that it was good" affirms **"the consummate perfection of
  God's creation."**
- Dead end: a *list* — *"gut und recht und schön"* — reads as enumeration,
  not intensity (doesn't feel stronger than plain *gut*).
- The fix (marveling **syntax**, not a bigger word): **"Gott sah, wie gut es
  war"** → escalates once at the end to **"wie überaus gut es war."** Weight
  by *how*-good, not by inflation to churchy *herrlich*.

### The levitating bird (post 3)
- Bad: *"…brütete der Geist Gottes, wie ein Adler … über den Jungen kreist
  und sie auf seinen Flügeln trägt."* — a bird levitating over nonexistent
  chicks.
- Why: Gen 1:2 shares exactly **one** verb with Deut 32:11 — רחף, the
  fluttering/brooding *hover*. The "bears its young on its wings" is a
  *different* verb (נשא) about carrying **Israel** — deliverance, not
  creation; there are no "young" in Genesis 1:2.
- Fix: **"über den Wassern brütete der Geist Gottes."** The verb carries the
  brood-image; no gloss needed. *Principle: import only the operative element
  of an allusion; strip the source-image's freight.*

### Elevated vs. archaic (post 2)
- Reaching for the sublime reintroduced **"schied … das Licht von der
  Finsternis"** — Luther. Contemporary: **"trennte."**
- Also a Hebraism: *"scheide Wasser von Wasser"* calques *mayim mi-mayim* —
  German doesn't repeat the noun. Fix: *"trenne die Wasser voneinander."*
- Principle: elevation ≠ archaism. The test is "would a living literary
  author write this word," not "does it sound lofty."

### The Luke 1 discovery (post 4)
- Genesis kept reading verse-by-verse and biblical. Turned out our own
  **certified Luke 1** already reads far bolder and stays faithful:
  *"Drinnen: still. Der Leuchter, der Vorhang, der Geruch von Weihrauch. Er
  war allein."* — fragments, atmosphere, flow. Genesis had been getting a
  *more literal* treatment than the house style.
- The unlock: refrains as a **returning voice**, not identical stamps —
  *"Wieder sprach Gott, und diesmal mitten in die Wasser hinein" / "Zum
  dritten Mal die Stimme."* Days flow into each other.

### The meta story — taste into principles (post 5)
Durable principles that came out of the session (each from a specific
correction): full-weight-not-flat · allusion economy (import only the
operative element) · illumination parsimony (illuminate only a real gap) ·
illumination by impact, not position · elevate through form, not content
(no embellishment/eisegesis) · unlock genuine latent meaning but don't
manufacture it (preserve open silences) · a required per-genre *register
anchor* (Genesis needed Schrott/Grünbein/Poschmann, not the prose
Zeh/Kermani bar). And the honest thread: the assistant twice hardened one
instance into an over-broad rule and had to be pulled back — *a principle
isn't right until it keeps the good cases, not just kills the bad one.*

---

*Seeded 2026-07-11 from the Genesis 1 DE build session in `aperto-bible-dev`
(experiments/lean_loop). Full principle text lives there in
`experiments/lean_loop/EXEGESIS_INTERROGATION.md`; the run artifacts and
before/afters are in `experiments/lean_loop/runs/`.*
