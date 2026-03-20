# Learning Tonesu — Design Document

*Status: draft / working notes. Non-normative.*

---

## Purpose of this document

Work out how a learner would acquire Tonesu. Not a finished curriculum — a
design space exploration. The goal is to answer: what would a lesson look
like, what order do concepts go in, and what format serves learners best?

---

## What a learner is acquiring

Tonesu is unlike natural-language learning in key ways:

- **No irregular forms.** Every word is compositional or has a transparent
  structural reason for its shape.
- **Very small primitive set.** ~34 CV roots cover the entire conceptual
  base. Learning the roots *is* most of the vocabulary problem.
- **Grammar is minimal.** Core frame is three slots: `la-[agent]
  [verb-compound] lo-[patient]`. Particles are few and fixed in function.
- **Notation is part of the language.** `~`, `'`, `()`, `[]`, `;`, `/`, `—`
  etc. are normative marks a learner needs to read and produce.
- **The hard part is compounding.** Knowing primitives isn't enough; a
  learner needs to parse and construct compounds fluently.

So the learning problem is mostly:

1. Internalize ~34 roots and their semantic fields.
2. Understand head-final right-branching composition.
3. Learn the grammar particles and their force.
4. Read and use notation marks correctly.
5. Build fluency with derived vocabulary through corpus exposure.

---

## Candidate learning stages

### Stage 0 — Orientation (before any production)
- What kind of language is this? Why does it work this way?
- The tier system: CV / compound / CVC / CVCC — why shapes signal tier.
- The head-final principle: modifier before head, right-branching default.
- The core sentence frame.

**Outcome:** learner can parse `to-li` and `la-mi to-si lo-tu` on paper.

---

### Stage 1 — Primitives (the conceptual inventory)
- The 34 CV roots grouped by phonosemantic family or functional cluster.
- Each root: form, core meaning, canonical compound examples.
- Not flashcards — the roots need to be learned as a *map*, not a list.
  The phonosemantic map (`notes/phonosemantic-map.md`) is a key resource here.

**Open question:** what's the best grouping order?
- Phonosemantic families (all `t-` roots together, all `r-` roots, etc.)?
- Semantic clusters (mind/knowledge group, body/action group, etc.)?
- Frequency in the corpus?
- An interleaved approach: introduce roots as they appear in worked sentences?

**Outcome:** learner can look at any primitive CV form and recall its
semantic field and directional logic (e.g. `to` = knowledge/pattern,
`si` = signal/surface, `ka` = agency/cause).

---

### Stage 2 — Compound construction
- Head-final rule in depth. Practice: given two roots, build the compound
  and explain what it means.
- The `'` juncture marker: when and why.
- The `no-X` negation pattern.
- The `[X]-no-fe` extremal pattern.
- Common derivational patterns: `-li` (person), `-mu` (device/tool),
  `-pa` (place), `-ge` (state/quality), `-ki` (action/change).

**Outcome:** learner can construct unfamiliar compounds from roots alone
and correctly parse multi-root chains like `to-fe-su-ki`.

---

### Stage 3 — Grammar particles in use
- `la-` / `lo-` / `lu-` (agent / patient / result).
- `ne` copula — property attribution only; not identity.
- `go` causal particle — necessary connection (Hume's distinction).
- `;` sequential connector — constant conjunction without asserted mechanism.
- `/` parallel partition.
- `he` vocative · `ya` attention signal.
- `ke` pivot · `no —` denial sequence.
- `ru-fe` exclusive scope.
- `helm` / `helms` identity spectrum.

**Outcome:** learner can produce and parse multi-clause constructions
including causal chains, parallels, and denials.

---

### Stage 4 — Notation marks in reading and writing
- Evidential frame `()` — not asserting; reported/inferred.
- Aside frame `[]` — annotation that doesn't alter truth conditions.
- Approximation `~` / `ven`.
- Quotation `""` — direct speech, mention, titles.
- Prosodic suspension `—` / `el`.
- Scope prefixes `a- i- u- o- e-` and the `la-` merge hazard.

**Outcome:** learner can read a fully notated corpus sentence and
identify what each mark is doing.

---

### Stage 5 — Derived vocabulary and registry fluency
- Work through the registry systematically or by domain.
- Each derived entry: parse it from roots, verify the gloss makes sense.
- Corpus sentences as the main exposure vehicle — real sentences, not
  contrived examples.

**Outcome:** learner has a working vocabulary of 50–100 derived forms
and can look up unfamiliar words and parse them independently.

---

### Stage 6 — Production and colloquial register
- Writing original sentences from prompts.
- Applying CLQ contraction rules.
- Understanding when formal vs colloquial register is appropriate.

**Outcome:** learner can produce grammatically correct, well-registered
Tonesu for a given communicative context.

---

## Format questions

### Option A — Linear lesson sequence
Classic: Lesson 1, Lesson 2, … Each lesson introduces a concept,
gives examples from the corpus, ends with a small exercise set.

Pros: clear progression, easy to navigate, familiar format.
Cons: the language is so compositional that "lesson order" matters a lot —
get it wrong and learners are confused. Exercises need to be designed.

### Option B — Reference + worked examples (current site model)
The site already has reference pages (Grammar, Morphology, Building words,
Patterns). "Learning" would be a guided tour pointing to these in sequence,
with exercises/prompts layered on top.

Pros: doesn't duplicate existing content. Cons: not optimized for acquisition.

### Option C — Corpus-driven inductive approach
Start with real sentences. Each sentence introduces or practices one
concept. Sentences are sequenced by concept-introduction order. The
learner encounters the rule after the example, not before.

Pros: suits the compositional nature of the language (see syntax in action,
then formalize). Cons: requires careful sequencing of the sentence corpus;
more work to design.

### Option D — Domain-first / use-case entry
Start with a domain (e.g. everyday conversation, theological discourse,
mathematical description) and learn the vocabulary + grammar needed for
that domain. Parallel tracks for different learners.

Pros: motivated learning, connects to real use. Cons: primitives appear
in all domains — hard to avoid front-loading everything anyway.

---

## Open design questions

1. **Who is the learner?** Conlang hobbyist? Philosopher wanting precise
   language? Someone engaging with the Bible translation project?
   Different profiles may need different entry points.

2. **What's the target fluency level?** Reading corpus sentences vs
   producing original ones vs engaging in real-time conversation
   (if that's ever a use case) — very different targets.

3. **Exercises: what forms work?**
   - Translation prompts (English → Tonesu)?
   - Parse drills (given a compound, decompose it)?
   - Fill-in-the-particle (given a sentence, insert the right particles)?
   - Construction challenges (given a semantic target, build the compound)?
   - Error-spotting (identify what's wrong in a malformed sentence)?

4. **Interactivity:** The Word Builder (`tonesu/builder.md`) already exists
   as an interactive tool. Could lessons link to it as a practice environment?

5. **Spaced repetition:** Is there a role for SRS (Anki-style) for the
   34 primitives? Probably yes for Stage 1. How do we author that deck?

6. **Lesson length / granularity:** One concept per lesson? One stage per
   lesson? Short (5 min) or long (30 min) sessions?

7. **Worked translations as lessons:** The Bible/Tao/etc. translation files
   are rich pedagogical material — could a translation walkthrough *be* a
   lesson? "In this lesson we translate Genesis 1:1–3 and encounter these
   five primitives for the first time."

8. **Prerequisites:** Does any lesson assume another? Do we need a
   formal prerequisite graph?

---

## Likely recommended approach (working hypothesis)

**Hybrid: Reference + structured pathway.**

- Keep the existing reference content as-is (Grammar, Morphology, etc.).
- Create a "Learning path" section with:
  - A curated sequence of concepts (Stage 0–5 from above).
  - Each stage links to the relevant reference pages but adds:
    - A short motivating intro.
    - 3–5 annotated corpus examples.
    - A small exercise set (translation + parse prompts).
  - The corpus-driven approach for vocabulary (Stage 5): use existing
    batch sentences as the primary exposure material.
- Translation walkthroughs (Stage 5–6) as standalone lessons that double
  as advanced reading material.

**First lesson candidate:** Stage 0 + 1 combined — "What Tonesu is and
the 10 most-used primitive roots" — using the foundations corpus batch
(C001–C008) as the worked example material.

---

## Files / resources that feed this work

| Resource | What it provides |
|----------|-----------------|
| `spec/phonology.md` | Sound system and tier structure |
| `spec/grammar.md` | Full particle and slot reference |
| `spec/morphology.md` | Derivational affixes |
| `spec/word-formation.md` | Compound construction rules |
| `registry/primitives.md` | The 34 CV roots |
| `notes/phonosemantic-map.md` | Phonosemantic family groupings |
| `notes/basics.md` | Language basics summary — possible Stage 0 source |
| `corpus/sentences/v4-current/` | Worked sentences for exercises |
| `corpus/conversations/` | Dialogue examples for Stage 3+ |
| `corpus/translations/` | Advanced reading / translation walkthroughs |
| `notes/open-questions.md` | Edge cases learners will hit |

---

*Next step: decide on format (Option A/B/C/D above), pick the first
lesson topic, and draft it.*
