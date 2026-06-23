# How Aperto actually works

If you have read [our process page](/process), you know *why* we are doing this. This page is about *how* — the actual machinery, including the parts that are still under construction.

We wrote it because “AI Bible translation” is a phrase that should make a careful reader pause. It makes us pause. The honest response to that suspicion is not reassurance; it is the seams. So here they are: the multiple drafts, the panel of critics that tries to tear each one apart, the gates a translation cannot pass until it earns its way through, and where a human still has the last word — and where, for now, one does not. Nothing below is metaphor. These are real checks, real thresholds, real failures we have caught and fixed. Where a number is provisional or a system is still being built, we say so.

## The problem we are actually solving

Most conversation about “AI translation” quietly assumes English, and quietly assumes that *good enough* is good enough. Neither holds here.

**Model quality is not evenly distributed across languages.** Today’s best language models are strongest in English — the language they have seen most — and measurably weaker as you move outward: into German and Polish, then into smaller or lower-resource European languages. The same model that writes fluent English can, in another language, produce prose that is grammatically correct and yet unmistakably *foreign* — the cadence of a translation rather than the voice of a native writer. Left unmanaged, an AI translation inherits exactly the weaknesses of the model that wrote it, and those weaknesses grow the further you travel from English.

**Scripture does not tolerate “gist.”** For most AI products, a paraphrase that is 95% right is a success. A Bible that is 95% right is 5% wrong about the text people build their lives on — and that 5% is not random noise. It shows up as borrowed church-jargon, a quietly invented meaning, a modern object dropped into a first-century scene, a line that reads like a sermon where the Greek is plain reportage. The bar is not *gist*; it is *native literary register without a single avoidable defect.*

So the engineering problem is specific: **how do you get an uneven, English-biased tool to produce genuinely native, genuinely accurate Scripture in language after language — and how do you *know* when you have, rather than hoping?** Everything below is our answer. It is, deliberately, not one clever model. It is a system built to compensate for what any single model gets wrong, and to measure the result honestly.

> **If you build with AI, you will recognise the shape of this.** What follows is the standard toolkit of production AI systems, applied with unusual strictness because the cost of a quiet error is unusually high: sample several independent generations instead of trusting one; evaluate them with automated judges (LLM-as-judge); block releases at hard regression gates; flag low-confidence output instead of shipping it silently; keep humans in the loop and route real-world corrections back in. We name each pattern as we reach it.

## We don’t translate from English. We translate from Greek and Hebrew.

Every passage begins with scholarship, not software. First a focused research pass surveys the recent academic literature on the chapter — current commentaries, journal scholarship and lexical work, not just whatever is old enough to be free — and gathers it into a research brief. Then a translator-scholar works through the original Greek or Hebrew against that brief: the lexical range of each weighted word, cross-references and Old Testament echoes, the theological weight a term carries, how it has been rendered before, and the cultural detail a first-century hearer would have taken for granted. This becomes a written exegesis for the chapter — its own 2.5–3.5 hours of work on top of the research — and everything downstream is accountable to it.

This matters for one reason worth stating bluntly: **Aperto is translated from the source texts, not adapted from someone else’s translation.** The AI does not start with an English Bible and reword it. It starts with the Greek, our exegesis, a style specification and a per-language theological glossary — and it writes fresh literature in the target language. The comparison we make against existing translations, described further down, exists precisely to *guarantee* that independence.

## A note on sources, scholarship, and copyright

Two fair questions sit under all of this: *what* are you reading, and *is that allowed?* Both deserve a straight answer.

Our exegesis is our own work. For each passage we synthesise a fresh analysis from the original text and from the best scholarship across traditions — critical editions and lexicons, technical commentaries from Catholic, Protestant, Orthodox and Pentecostal scholars, recent peer-reviewed research, reference grammars — selected for a genuinely ecumenical reading rather than a single confessional line. We consult that scholarship the way any translator or commentator always has: we read it, weigh it, and write our own analysis. **We do not republish whole copyrighted commentaries or Bibles, and the Scripture text we publish contains no third-party translation — it is our own rendering from the source languages.** Where our exegesis engages a specific source, it does so the way any commentary or study Bible does: short, clearly attributed quotations and credited summaries, used for analysis and criticism. What we publish is our own artifact — the exegesis, and the translation built on it.

This is a deliberate choice, for two reasons. The first is quality: a translation is only as good as the scholarship beneath it, and we would rather stand on the best current scholarship than limit ourselves to whatever happens to be out of copyright and often a century out of date. The second is integrity: because every downstream decision is anchored to *our own* exegesis from the source text — not lifted from any existing translation — the result is genuinely independent work, not a derivative of someone else’s Bible. This is ordinary scholarly practice: you may read, learn from, and briefly quote a copyrighted commentary with attribution to produce your own original work; you may not republish it wholesale or pass off its translation as your own. We stay firmly on that side of the line — quoting sparingly and with credit, and never re-hosting the sources themselves.

> *Production-AI analogue: retrieval and synthesis that cite, quote briefly, and learn from sources to produce new work — without re-hosting or redistributing the sources themselves.*

## Many drafts, not one: the model ensemble

A single AI model has a single set of habits. To avoid inheriting any one model’s blind spots, we generate several independent drafts of the same chapter in parallel — each from a different model family, each given exactly the same inputs: the exegesis, the cultural map, the style specification, the theological glossary and the audience profile.

In practice that currently means up to four drafts per chapter from different providers — including models from Anthropic (Claude), OpenAI, Google and Mistral — generated simultaneously. Different families have different strengths: one reasons more literarily, another tracks context more tightly. Producing several candidates and choosing between them gives us a better starting point than trusting any one.

The drafts are **not** blended together. Each is a complete, standalone translation of the chapter. The next stage decides which one wins — by trying to find everything wrong with each of them.

> *Production-AI analogue: ensemble sampling across models to cancel out any single model’s systematic bias.*

## The panel that tries to break the text

Once we have drafts, we attack them. Each candidate is read by a panel of independent critics — separate AI evaluators, each given one job and told to be hard to please. They are adversarial by design: their task is not to approve the text but to find every place it betrays a translator’s hand.

The panel includes critics for:

- **Naturalness** — would a native literary writer actually construct this sentence, or does it merely read as *translated?*
- **Archaism & church-jargon** — words and cadences that smell of old Bibles rather than living language.
- **Calque** — sentence structure copied from the Greek or Hebrew and smuggled into the target language.
- **Register drift** — tone slipping into sermon, sentimentality or academic dryness.
- **Comprehension gaps** — places an unchurched reader would simply lose the thread.
- **Sensitivity** — language that reproduces harmful stereotypes.
- **Theological fidelity** — christological titles and key terms preserved, with no meaning quietly invented.
- **Mechanical correctness** — grammar, spelling and punctuation, checked by deterministic tools, not opinion.

Each critic returns specific findings — the verse, the offending span, why it fails, a suggested direction — tagged high, medium or low severity. Crucially, **the panel’s job is to surface disagreement, not to average it away.** No critic is silently overruled; a human or a revision step has to answer each flagged finding on its own terms.

Selection is a single, even-handed pass: **every candidate is scored by the same panel**, and the draft with the fewest and least-severe defects wins — a clean pass with zero high-severity findings being the ideal. The winning draft then enters the revision loop described below, where its remaining flagged spans are fixed and re-checked. Some of these critics run today across our core languages; others — notably cross-language consistency and back-translation checks — are designed and partially built, and we are honest that they are not yet load-bearing everywhere.

> *Production-AI analogue: LLM-as-judge evaluation and automated red-teaming — many narrow, adversarial evals instead of one vague quality score.*

## Gates a translation has to earn its way through

Critique is advisory; some checks are not. A few gates are **hard**: a translation that fails them does not move forward, full stop.

The **mechanical-correctness gate** is strictest. Any grammar error, spelling mistake, broken punctuation or malformed file structure holds the passage back. It runs on real linguistic tooling — industrial grammar checkers and dictionaries — for the languages where that tooling is mature, with an AI fallback where it is not yet.

A second gate watches for **anachronism**: modern objects accidentally dropped into a first-century scene. The test is concrete — if a twenty-eight-year-old in Berlin or Warsaw heard this word cold, what would they picture? If the answer is a car, a phone, a wristwatch or a euro coin, and the object did not exist in first-century Judea, the word is rejected. A real example we caught and fixed: a German draft once rendered a verse so that Zacharias “drove home” — a car where the text has a man walking. The gate now blocks that whole class of error.

This is the heart of what we call **the floor**. The floor is non-negotiable: nothing grammatically broken or visibly foreign ever publishes. It is also, deliberately, *only* the floor — clearing it means the text is sound, not yet that it sings.

> *Production-AI analogue: CI/CD regression gates and deterministic guardrails — automated checks that block a release rather than merely warn.*

## From floor to vision: two standards, honestly labelled

We hold two standards, and we keep them separate on purpose.

The **floor** is mechanical soundness: correct, structurally valid, free of anachronism and obvious calque. The **vision** is native literary register — prose that reads the way a contemporary novelist in that language writes, measured against named reference authors and, where possible, against the statistical fingerprint of real native writing.

Most passages clear the floor quickly. Reaching the vision takes iteration: the critics’ findings are fed back into a revision loop that fixes the flagged spans and leaves the rest alone, then re-checks — typically a few rounds before it converges, or before we accept it has gone as far as this pass will take it.

Here is the honest part. A passage that clears the floor but has **not** fully converged toward the vision still publishes — but it carries a **low-confidence tag**, so it is surfaced first for human polishing rather than presented as finished. A passage that is grammatically broken or visibly translated never publishes at all. We would rather show you sound-but-plain text we have flagged than hide the difference between *correct* and *beautiful.* The system, in other words, is built to know what it does not yet know.

> *Production-AI analogue: explicit quality thresholds plus confidence tagging that routes weak output to human review instead of shipping it silently.*

## Comparing against other translations — to stay original, and to stay clear

Because we translate from the source texts, we also check our work *against* existing translations — and it is worth being precise about why, because “comparing to other Bibles” can sound like the opposite of what it is.

We do it for two reasons, both protective.

**The first is originality.** After a draft is written, we compare it, verse by verse, against a small set of established translations in that language. If our wording sits too close to any one of them, that is a flag, not a feature: it usually means borrowed church-phrasing has leaked in, and the passage is sent back to be rewritten in its own voice. The comparison is a *tripwire that catches accidental echoes so we can remove them.* It confirms our independence; it does not create a dependency.

**The second is accessibility.** We also look at the clearest modern translations as a benchmark — not to imitate them, but to be sure we are at least as clear as the best of them. Accessibility, for us, is a floor and not a ceiling: if a respected accessible translation reads smoothly where ours reads stiff, that is a defect to fix; if ours is harder because it deliberately keeps an edge the smoother version sanded off, that divergence is correct, and we document why.

We draw these comparison and benchmark texts from licensed scholarly Bible interfaces — including YouVersion’s platform, which we are free to use for non-commercial work like ours — and public-domain editions, used strictly for internal, verse-by-verse quality checks. Brief excerpts may sit in our internal QA notes, but the Bible we publish contains none of this third-party text — only our own rendering. We use these texts to *check* our work, never as material to copy from.

> *Production-AI analogue: benchmarking against references, plus a contamination check to confirm the output isn’t echoing its comparison set.*

## The hard part: doing this in languages other than English

This is where most of our engineering goes — because, as we said at the start, this is where models are weakest.

In languages other than English, the failure modes of machine translation are more visible and more damaging. German prose can pick up the ghost-cadence of the Luther Bible; Polish can drift into a pulpit voice many readers actively resent; Arabic must read as contemporary literature without sounding either Quranic or like an archaic mission Bible; some languages arrive with almost no tradition of the Bible *as literature* at all. A translation can be perfectly grammatical and still feel unmistakably foreign.

Our mitigations are specific:

- **The critics reason in the target language.** For each language we write the critics’ instructions *in that language*, so the system evaluates as a native editor would — rather than forming its judgments in English and translating them in. Pivoting judgment through English is one of the main ways non-English quality silently degrades.
- **Every language has a literary profile.** Each is anchored to a concrete reader — a secular twenty-eight-year-old in a named neighbourhood — and a set of reference authors, plus a glossary of how every loaded theological term should be handled.
- **Onboarding is a gate, not a toggle.** Before a language goes into production it has to clear a checklist: style specifications, worked exemplars, a theological glossary, grammar tooling and a comparison set.

**Where we are:** German and Polish are furthest along — the native-language critic panel is live for both — with English close behind on its own toolchain; a wider set of European languages is in active onboarding. We would rather name a few solid languages than imply many finished ones.

> *Production-AI analogue: avoiding pivot-language degradation, and per-locale evaluation rather than one English-shaped quality bar for every language.*

## Where the human comes in

This is the question that matters most, so we will answer it without softening — including its honest tension with scale.

**Right now we are in a trial phase, and human review is hands-on.** For our core languages, a reviewer works through the translation at four points: after the exegesis, after the key word-choice decisions are made, after the literary draft is written, and before anything is published. The most important is the second — reviewing word choices *before* the prose is built around them, because a correction there costs a fraction of what the same fix costs once a whole passage has been written around it. This hands-on phase is how we calibrate the system and learn where it can be trusted.

**We are also honest that this depth cannot scale unchanged.** The whole point of Aperto is to serve languages and communities that have waited generations precisely because line-by-line human translation does not scale to them. At that scale, no team can deep-review every chapter in every language — so the system is deliberately built *not to depend on it.* What it depends on instead is durable: humans set the method, write the standards, and curate every critic; the automated floor guarantees that nothing broken or anachronistic ever publishes; weaker passages publish flagged, not hidden.

**And human review does not go away — it changes shape.** Our review and feedback tool stays open and accessible. Reviewers work in it — seeing the translation, the reasoning behind each rendering, and the critics’ findings side by side — and can approve, question, or propose an alternative for any decision. Readers can flag a verse. That feedback is taken seriously and routed back into the system: a grammar miss tightens a gate, a register problem updates a critic’s brief, a structural issue updates the architecture. Parts of that loop are live today; parts are still being wired, and we will keep this page current as that changes.

So when we say elsewhere that human judgment is *multiplied, not replaced*, this is the precise shape of it: humans decide what *good* looks like, review closely where it matters most, and answer the feedback that comes back. The machine does the volume. The judgment stays human.

> *Production-AI analogue: human-in-the-loop review with a feedback flywheel — real corrections routed back to improve the standards, gates and prompts over time.*

## What we haven’t finished

A methodology page that only described what works would be marketing. A few things are genuinely still in progress, and we would rather you hear them from us:

- Several critics — cross-language consistency, back-translation fidelity, and the statistical “does this read like native literature” check — are designed and partially built, not yet relied upon across every language.
- Full coverage is a few languages deep today, not the whole map. The rest are at varying stages of onboarding.
- The feedback loop — the path from a reader’s flag back into the system’s standards — is partly live and partly still being wired.
- Some of the publishing automation between our internal repository and this website is still done by hand.

None of this changes the floor: nothing broken or anachronistic publishes. It does mean this page describes a system **still being built** — and we will keep it current as the gaps close.
