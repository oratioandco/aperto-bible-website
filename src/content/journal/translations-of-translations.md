---
title: Translations of translations
description: Most "AI Bible translations" are syntheses of century-old translations. What we build instead — and what it costs.
date: 2026-07-13
author: Tobias Treppmann
cover: /images/journal/translations-of-translations.jpeg
coverAlt: A stack of worn antique Bibles in shadow beside a single open Hebrew Bible with pencil annotations, lit by warm window light
---

**The demo is real**

If you follow faith-tech, you've seen the demos: one API call, and out comes a Bible passage in Swahili or Slovak or Low German, reasoned over "from multiple perspectives," with a textual basis in the original languages. I want to take these systems seriously, because they're the most interesting thing to happen to Bible translation tooling in decades, and because I've spent the last year building something that looks superficially identical and is, underneath, close to the opposite.

**What a meta-translation actually is**

Strip away the prompt engineering and the mechanism is: synthesize the target verse from a set of existing translations, checked against the original-language text. The set has to be public-domain, because everything modern is copyrighted and license negotiations don't fit in an API call. Public domain means the corpus is mostly pre-1930.

Two consequences follow, and neither is fixable with a better prompt.

First, dated philology. A century of manuscript discoveries, lexicography, and Second-Temple scholarship postdates that corpus. Where the old translations share a mistake, the synthesis inherits it with confidence, because agreement across sources is exactly what synthesis rewards.

Second, a borrowed accent. The public-domain corpus isn't theologically neutral; it has the accent of its era, which trends narrow and conservative-Protestant. "Never blindly copied" is true and beside the point. When fourteen inputs lean one way, the output leans.

This is why I call the result a meta-translation: a translation whose sources are translations. As a bootstrapping tool for languages that have nothing, it's genuinely valuable, and I mean that without condescension. But it's a generator. It has no opinion about any verse. Nobody decided anything.

**What deciding looks like**

The project I run (Aperto) inverts the order of operations. Before any target-language word exists, there's an exegesis: what does the Hebrew or Greek do, what did it do to its first audience, where do the traditions disagree. The exegesis feeds a decision document; the decision document binds the draft. AI writes the prose. A panel of adversarial AI judges, running in separate calls with hard gates, attacks it: archaisms, calques, register drift, back-translation fidelity, naturalness against the best modern published translations. And a human exegete rules on every flagged decision, in writing, in public.

Our north star is one sentence: the modern reader should be hit by the text the way the original audience was. Same clarity, and same friction. Both failure modes are real. Wooden literalism keeps friction the original never had. Smoothing removes friction the original did have. A synthesis of inherited translations can't even see this axis, because its sources already chose, mostly toward smoothing, a century ago.

**One verse, concretely**

Psalm 23:4, "thy rod and thy staff, they comfort me." The Hebrew *šēbeṭ* is a club: a shepherd's predator weapon, the thing David says he used against lions and bears. The comfort in the verse is the comfort of walking a dark valley next to someone armed. The English translation tradition softened it into pastoral furniture, and every synthesis of that tradition will reproduce the furniture, fluently, in every language it touches.

Our English draft says the club keeps the wolves off. Our Polish team rejected "różdżka" because to a secular Polish reader it sounds like a magic wand. Our German dropped Luther's "Stecken," a word that barely exists outside this one verse anymore. Three languages, three different decisions, one documented reason. You may think we ruled wrongly; the point is that you can look up who ruled, and why, and argue back. There's a verse-level record and a public comment channel, and reader pushback has already triggered re-translations.

**The honest tradeoff**

Meta-translation scales to 100+ languages in an afternoon. We've spent eight months on three languages and are still not done arguing about one psalm. If the goal is "some scripture in every language now," the generator wins and should. If the goal is a translation someone can trust, cite, and contest, provenance is the product, and provenance is precisely what a generator cannot emit.

I'd summarize the whole thing in one line: meta-translation is a generator; a translation is a set of defended decisions. Both are useful. Only one of them can be wrong in an accountable way, and being wrong accountably is what translation has always been.

Everything is public: the [methodology](/en/methodology), the judge architecture, the decision records, the text itself under a [CC license](/en/license). Next post: the day my own judges passed a text three times — and they were wrong every time.
