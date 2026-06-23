# How Aperto actually works

If you’ve read [our process page](/process), you know *why* we’re doing this. This page is *how* — the real machinery, including the parts still under construction.

“AI Bible translation” is a phrase that should make a careful reader pause. It makes us pause. The honest answer to that suspicion isn’t reassurance; it’s showing the seams. Nothing below is metaphor — these are real checks, real thresholds, real failures we’ve caught and fixed. Where something is provisional or unbuilt, we say so.

## The problem we’re solving

Most talk of “AI translation” quietly assumes English, and quietly assumes *good enough* is good enough. Neither holds here.

**Model quality drops off outside English.** Today’s models are strongest in the language they’ve seen most. The same model that writes fluent English can — in German or Polish, and more so in smaller languages — produce prose that is grammatically correct yet unmistakably *foreign*: the cadence of a translation, not the voice of a native writer. Left unmanaged, a translation inherits exactly those weaknesses.

**Scripture doesn’t tolerate “gist.”** A paraphrase that’s 95% right is a fine outcome for most AI products. For a Bible it means being 5% wrong about the text people build their lives on — and that 5% shows up as borrowed church-jargon, an invented meaning, a modern object dropped into a first-century scene. The bar isn’t *gist*; it’s native literary register with no avoidable defect.

So the real problem is this: how do you get an uneven, English-biased tool to produce genuinely native, genuinely accurate Scripture language after language — and *know* when you have? Our answer isn’t one clever model. It’s a system built to catch what any single model gets wrong, and to measure the result honestly. If you build with AI, you’ll recognise the shape: sample several generations, judge them with automated evaluators, block releases at hard gates, flag low-confidence output, keep humans in the loop. We name each as we reach it.

<!--DIAGRAM:pipeline-->

## We translate from Greek and Hebrew — not from English

Every passage begins with scholarship, not software. First a research pass surveys the recent academic literature on the chapter — current commentaries, journal scholarship, lexical work, not just what’s old enough to be free — and gathers it into a brief. Then a translator-scholar works the original Greek or Hebrew against that brief: the range of each weighted word, Old Testament echoes, the weight a term carries, the cultural detail a first-century hearer assumed. That becomes a written exegesis the whole pipeline is accountable to.

The point, stated plainly: **Aperto is translated from the source texts, not reworded from someone else’s translation.** The AI starts with the Greek, our exegesis, a style specification and a per-language glossary — and writes fresh literature in the target language.

## Sources and copyright

Two fair questions sit under all of this: *what* are you reading, and *is that allowed?*

Our exegesis is our own work, synthesised from the best scholarship across traditions — Catholic, Protestant, Orthodox, Pentecostal — for a genuinely ecumenical reading. We consult it the way any commentator always has: read it, weigh it, write our own analysis. **We don’t republish whole copyrighted commentaries or Bibles, and the Scripture we publish contains no third-party translation — it is our own rendering from the source languages.** Where our exegesis engages a specific source, it does so as any study Bible does: short, clearly attributed quotation. We’d rather stand on the best current scholarship than limit ourselves to whatever happens to be out of copyright and a century out of date.

> *Like any research tool: cite, quote briefly, and synthesise — without re-hosting the sources themselves.*

## Many drafts, not one

A single model has a single set of habits. So we generate several independent drafts of each chapter in parallel — currently up to four, from different providers (Anthropic, OpenAI, Google, Mistral) — each given identical inputs. Different families have different strengths; choosing among candidates beats trusting one. The drafts aren’t blended: each is a complete translation, and the next stage decides which wins — by trying to break it.

> *Ensemble sampling, to cancel out any one model’s bias.*

## The panel that tries to break the text

Each draft is read by a panel of independent critics — separate evaluators, each with one job and told to be hard to please. They hunt for: unnatural phrasing; archaism and church-jargon; calque (source grammar smuggled into the target); register drift into sermon or dryness; comprehension gaps; harmful stereotypes; theological infidelity; and mechanical errors, caught by deterministic tools rather than opinion. Each returns specific findings — verse, span, why it fails, severity — and the panel surfaces disagreement rather than averaging it away.

Selection is a single, even-handed pass: every candidate is scored the same way, and the draft with the fewest and least-severe defects wins, then enters the revision loop below. Some critics run today across our core languages; others — cross-language consistency, back-translation — are partly built, and we don’t yet lean on them everywhere.

> *LLM-as-judge evaluation: many narrow, adversarial checks instead of one vague score.*

## Gates it has to earn its way through

Critique is advisory; some checks aren’t. A few gates are hard — fail them and the passage doesn’t move.

The **mechanical gate** is strictest: any grammar, spelling, punctuation or structural error holds the text back, checked with real linguistic tooling where that tooling is mature. An **anachronism gate** catches modern objects in a first-century scene — if a twenty-eight-year-old in Berlin or Warsaw would picture a car, a phone or a euro coin, and it didn’t exist in first-century Judea, it’s rejected. A real catch: a German draft once had Zacharias “drive home” — a car where the text has a man walking. The gate now blocks that whole class of error.

This is **the floor**: nothing broken or visibly foreign ever publishes. It is also only the floor — sound, not yet singing.

> *CI regression gates: automated checks that block a release, not merely warn.*

<!--DIAGRAM:floorvision-->

## From floor to vision

We hold two standards, on purpose. The **floor** is mechanical soundness. The **vision** is native literary register — prose that reads the way a contemporary novelist in that language writes. Most passages clear the floor quickly; reaching the vision takes iteration, as the critics’ findings feed a revision loop that fixes the flagged spans and re-checks, a few rounds until it converges.

The honest part: a passage that clears the floor but hasn’t reached the vision still publishes — carrying a **low-confidence tag**, so it’s surfaced first for polishing rather than presented as finished. Text that is broken or visibly translated never publishes at all. We’d rather show you sound-but-plain text we’ve flagged than blur the line between *correct* and *beautiful*. The system is built to know what it doesn’t yet know.

> *Confidence tagging that routes weak output to review instead of shipping it silently.*

## Comparing against other translations

Because we translate from the source, we also check our work *against* existing translations — for two protective reasons.

**Originality.** We compare each draft, verse by verse, against established translations in that language. If our wording sits too close to any one of them, that’s a flag: usually borrowed phrasing has leaked in, and the passage is rewritten in its own voice. It’s a tripwire that catches accidental echoes — it confirms our independence, it doesn’t create a dependency.

**Clarity.** We also benchmark against the clearest modern translations — not to imitate them, but to be sure we’re at least as clear. If a smoother version reads better where ours is stiff, that’s a defect; if ours is harder because it keeps an edge the smoother one sanded off, that’s deliberate, and we note why.

These texts come from licensed scholarly Bible interfaces — including YouVersion’s, which we’re free to use for non-commercial work like ours — and public-domain editions, used strictly for internal checks. The Bible we publish contains none of this third-party text.

> *Benchmarking against references, plus a contamination check that the output isn’t echoing them.*

## The hard part: languages other than English

This is where most of our engineering goes, because it’s where models are weakest. German can pick up the ghost-cadence of the Luther Bible; Polish can drift into a pulpit voice readers resent; some languages have almost no tradition of the Bible *as literature*. A translation can be flawless grammar and still feel foreign.

Our mitigations are specific. **The critics reason in the target language** — their instructions are written in it, so the system evaluates as a native editor would, rather than pivoting its judgment through English (one of the main ways non-English quality silently degrades). **Each language has a literary profile** — a concrete reader, reference authors, a theological glossary. And **onboarding is a gate**: style specs, worked exemplars, glossary, grammar tooling and a comparison set, before a language goes live.

Where we are: **German and Polish are furthest along, with English close behind; a wider set of European languages is in active onboarding.** We’d rather name a few solid languages than imply many finished ones.

> *Per-locale evaluation, not one English-shaped quality bar for every language.*

## Where the human comes in

The question that matters most, answered plainly — including how it changes as we grow.

**In the trial phase we’re in now, the system carries each passage to the vision standard, and then a human reads it before it’s published** — a review with the authority to change anything, by someone who knows both the source and the target language. This is how we learn where the system can be trusted, and why we’re starting with a small set of chapters rather than rushing out a whole Bible.

**At scale, that pre-publication read can’t stay the same — and we’d argue it shouldn’t.** The point of Aperto is to reach communities that have waited generations precisely because line-by-line human translation doesn’t scale to them. So the system is built *not to depend on it*: humans set the method and the standards and curate every critic; the floor guarantees nothing broken or anachronistic is ever published; weaker passages appear flagged, not hidden.

**Here a digital translation has an advantage a printed one never had: it can be living, not final.** Every translator knows that what ultimately decides whether a rendering works is not their own judgment but the audience’s reception — whether the words land for the people reading them — and that is the one thing no pre-publication review can fully measure beforehand. A printed Bible freezes its best guess for a generation; a digital one doesn’t have to. So review becomes a conversation that continues after publishing: our tool at [translate.aperto.bible](https://translate.aperto.bible) lets anyone read a passage, see the reasoning behind a rendering, and tell us where it rings true and where it doesn’t. That feedback routes back — a recurring confusion becomes a fix, a register that grates updates a critic’s brief. Parts of that loop are live today; parts are still being wired.

So “human judgment is multiplied, not replaced” means this: humans decide what *good* looks like, review before publishing while we’re small enough to, and — at any scale — keep listening to the people the translation is actually for. The machine does the volume. The judgment stays human.

> *Human-in-the-loop with a feedback flywheel — real corrections improving the standards over time.*

## What we haven’t finished

A page that only described what works would be marketing. A few things are genuinely still in progress:

- Several critics — cross-language consistency, back-translation, the statistical “reads like native literature” check — are partly built, not yet relied on everywhere.
- Full coverage is a few languages deep, not the whole map.
- The feedback loop from a reader’s flag back into the standards is partly live, partly still being wired.
- Some publishing steps between our internal repository and this site are still done by hand.

None of it changes the floor: nothing broken or anachronistic publishes. This page describes a system still being built — and we’ll keep it current as the gaps close.
