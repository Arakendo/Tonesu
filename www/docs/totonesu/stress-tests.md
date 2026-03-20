# Stress Tests

Translation is the hardest test a constructed language can face. Every source text brings assumptions about what a language *should* be able to do — and some of those assumptions break against Tonesu's design.

This page surveys the major stress-test categories from the [translation analyses](corpus/translations/overview.md) and highlights where the language works cleanly, where it strains, and where it forces the translator to make choices the source text didn't.

---

## Theology: identity and predication

The Bible translations are the heaviest stress tests. Ancient Hebrew and Koine Greek assume distinctions that Tonesu handles differently — or doesn't handle at all.

### "I AM WHO I AM" (Exodus 3:14)

The divine self-identification in Exodus requires an identity statement that is also a refusal to be categorized. Tonesu's three-level system (`ne` property < `helm` functional equivalence < `helms` strict identity) provides tools the source languages don't have — but the problem shifts: which level is theologically correct?

Using `helms` (strictest identity) claims definitional equality. Using `ne` (property attribution) understates. The translation must choose a precision level that Hebrew deliberately leaves open.

**See:** [Exodus 3:1–15 analysis](corpus/translations/bible/exodus-3-1-15/index.md)

### "In the beginning was the Word" (John 1:1)

Greek `logos` maps to multiple Tonesu roots depending on which aspect you emphasize: `to` (conceptual pattern), `si` (signal), `to-re-su` (ordered knowledge system). Each choice is a theological commitment the Greek original avoids by using a single polysemous word.

**See:** [John 1:1 analysis](corpus/translations/bible/john-1-1/index.md)

### "The spirit is willing but the flesh is weak" (Matthew)

The `zo-to` (soul/identity-pattern) vs `zo-se` (living organism/body) distinction maps well here — Tonesu's compound system naturally separates the pattern-level self from the biological substrate. This is a case where the language's design *helps* rather than hinders.

**See:** [Matthew 16:25 analysis](corpus/translations/bible/matthew-16-25/index.md)

### Last Supper: performative speech

"This is my body" is a performative declaration — it creates a reality by stating it. Tonesu's epistemic system (`se`/`si`/`to`) is built for *reporting* knowledge states, not for *constituting* them. The evidential machinery doesn't naturally accommodate speech acts where saying makes it so.

**See:** [Last Supper analysis](corpus/translations/bible/last-supper/index.md)

---

## Philosophy: self-reference and paradox

### The Liar Paradox

"This sentence is false." Self-referential paradoxes test whether a language can express propositions that undermine themselves. Tonesu's `ze` back-reference system can point at propositions — but can a sentence point at *itself*? The translation forces the question of whether `ze` can be self-referential or only exophoric.

**See:** [Liar Paradox analysis](corpus/translations/philosophy/liar-paradox/index.md)

### Tractatus Logico-Philosophicus

Wittgenstein's "The limits of my language mean the limits of my world" is a claim *about* language made *in* language. Tonesu has metalinguistic tools (`feld`, `helm`, `helms`) but the Tractatus pushes beyond commentary into foundational claims about the language–world relationship.

**See:** [Tractatus analysis](corpus/translations/philosophy/tractatus/index.md)

### Tao Te Ching Chapter 1

"The Tao that can be told is not the eternal Tao." This is a direct challenge to Tonesu's premise that everything expressible should be expressible *precisely*. The source text claims that ultimate reality resists linguistic capture. Translating it requires Tonesu to *say* that it can't say something — which it can do, but not without irony.

**See:** [Tao Te Ching analysis](corpus/translations/philosophy/tao-te-ching-ch1/index.md)

---

## Literature: affect and ambiguity

### "To be or not to be" (Hamlet)

Shakespeare's line depends on metrical structure, cultural resonance, and deliberate ambiguity about what "to be" means. Tonesu can express the propositional content (existence vs non-existence as a choice) but the *performance* — the pause, the rhythm, the weight — belongs to a register the language has no grammar for.

**See:** [Hamlet analysis](corpus/translations/literature/hamlet-to-be/index.md)

### Bashō's frog haiku

Seventeen syllables, three images, no explicit connections. The poem works by what it *doesn't* say. Tonesu's explicit relational grammar (`go`, `ne`, `;`) may over-specify what the haiku leaves open. The challenge: how do you translate *deliberate incompleteness* into a language that demands structural precision?

**See:** [Bashō analysis](corpus/translations/literature/basho-frog/index.md)

### Dickinson: "Because I could not stop for Death"

Personification and metaphor — treating Death as a social agent. Tonesu can put Death in `la-` (agent slot) to give it agency, but the *tone* — genteel, ironic, intimate — depends on cultural registers the language doesn't yet encode.

**See:** [Dickinson analysis](corpus/translations/literature/dickinson-death/index.md)

### "It was the best of times, it was the worst of times"

Dickens's parallel construction is a natural fit for the `/` (parallel partition) mark: two clauses, formally paired, antithetical in content. This is a case where Tonesu's structural apparatus matches the source text's rhetorical architecture well.

**See:** [Tale of Two Cities analysis](corpus/translations/literature/tale-of-two-cities/index.md)

---

## Science: precision and convention

### Newton's First Law

"An object at rest stays at rest" — a universal conditional with no temporal qualification. Tonesu's `go {premise} result` frame handles the causal structure, but the *universality* (this is true in all cases, always) may need the `a-` (abstract/universal) scope prefix or a dedicated quantifier pattern.

**See:** [Newton analysis](corpus/translations/science/newton-first-law/index.md)

---

## Patterns across stress tests

### Where Tonesu does well

- **Epistemic precision**: claims about knowledge states, belief, evidence — the core strength
- **Structural decomposition**: complex concepts that reduce cleanly to root combinations
- **Parallel constructions**: the `/` partition and comparison frames handle antithesis naturally
- **Soul/body distinction**: `zo-to` vs `zo-se` provides vocabulary most languages lack

### Where Tonesu strains

- **Polysemy and ambiguity**: source texts that *depend* on a word meaning multiple things at once resist translation into a language that demands precision
- **Performative speech**: the epistemic system reports states but doesn't constitute them
- **Deliberate incompleteness**: haiku, mystical texts, and poetry that works by *absence* push against Tonesu's structural explicitness
- **Affect and tone**: emotional register, irony, and intimacy aren't grammatically encoded

### Where Tonesu forces choices

The most interesting cases are where Tonesu requires the translator to *decide* something the source text left open. Is the Logos a pattern (`to`) or a signal (`si`)? Is the divine identity strict (`helms`) or functional (`helm`)? Is Hamlet's question about existence (`zo-ne`) or consciousness (`zo-to`)?

These forced choices aren't failures. They're the language doing what it was designed to do: making the translator face what they actually mean.

---

## Full translation analyses

All translation analyses are available in the [translation analyses](corpus/translations/overview.md) section, organized by source domain (Bible, Literature, Philosophy, Science). Each analysis includes the source text, the Tonesu translation, and a detailed walkthrough of the structural choices made.
