# Learning Tonesu — Design Document

*Status: draft / working notes. Non-normative.*

---

## Purpose of this document

Work out how a learner would acquire Tonesu. Not a finished curriculum — a
design space exploration. The goal is to answer: what would a lesson look
like, what order do concepts go in, and what format serves learners best?

---

## Core design principles

### Tonesu is learned like a system, not a natural language

There are no irregular forms. Every word is compositional. Grammar is
minimal and fixed. The challenge is structural thinking, not memorization.

### Meaning first, system second

Learners experience language through use, not definition. The flow is:

> show → then explain

Not:

> explain → then use

Abstract structure (tier system, head-final principle, parse invariants)
is introduced *after* the learner has already encountered examples that
demonstrate it. The formal system is a reference that deepens understanding
— not the entry point.

### Patterns emerge; they are not front-loaded

Primitives are introduced through sentences, not as a map to study.
The phonosemantic map and full root inventory exist as reference — learners
reach for them when they're ready, not when the curriculum pushes them.

---

## What a learner is acquiring

Tonesu is unlike natural-language learning in key ways:

- **No irregular forms.** Every word is compositional or has a transparent
  structural reason for its shape.
- **Very small primitive set.** ~34 CV roots cover the entire conceptual
  base. Learning the roots *is* most of the vocabulary problem.
- **Grammar is minimal.** Core frame is three slots: `la-[agent]
  [verb-compound] lo-[patient]`. Particles are few and fixed in function.
- **Notation is semantic.** `~`, `'`, `()`, `[]`, `;`, `/`, `—`
  etc. are normative operators — not optional annotation, but part of
  what the language *means*.
- **The hard part is compounding.** Knowing primitives isn't enough; a
  learner needs to parse and construct compounds fluently.
- **Epistemic discipline is a skill.** Knowing when to use `se` vs `to`,
  when *not* to upgrade a claim, and how misuse looks — this is the
  philosophical core of the language, not just grammar.

So the learning problem is mostly:

1. Encounter real sentences and begin pattern-matching.
2. Progressively internalize roots through repeated use.
3. Understand head-final right-branching composition.
4. Learn grammar particles and notation marks together (they are
   experienced together — splitting them is academically clean but
   pedagogically wrong).
5. Build fluency with derived vocabulary through corpus exposure.
6. Develop the epistemic judgment to produce well-calibrated Tonesu.

---

## Learning stages

### Stage 0 — First Contact

Not "what is the formal structure" but "what does this *do*."

Give the learner 3–5 real sentences using a small subset of roots (5–8).
Supply just enough explanation to parse. No tier system, no formal
invariants — just: here's a sentence, here's what it says, here's how
the pieces fit together.

Example sentences (from the foundations corpus, C001–C008):

```
la-mi  se  lo-zo-ne
I perceived the mycelium.

to-si — la-tu  ki  pa-li-pu  ta-ti-be
Are you going to the city soon?

la-zo-su  be  lo-zo-be
A plant produces seeds.
```

Roots introduced by this stage (candidate set):
`la` `lo` `mi` `tu` `se` `to` `si` `ki` `be` `zo`

**Outcome:** learner can read a simple sentence and identify "who did
what to what." They've seen the `la-`/`lo-` frame in action before
anyone explains it formally.

---

### Stage 1 — Progressive root introduction

NOT "here are all 34 primitives, learn them as a map."

Instead: introduce roots *through sentences*, in clusters of 3–6 per
lesson. Reuse heavily. Cluster by usage context, not by phonosemantic
family or taxonomy.

Example lesson shape:

> "Here are 6 roots you need to understand these 10 sentences."

The phonosemantic map (`notes/phonosemantic-map.md`) and full primitive
inventory (`registry/primitives.md`) exist as **reference** — the learner
consults them when a root comes up, not as a study target. The map is
valuable once the learner has enough roots internalized to see the
patterns; it's not the entry point.

**Open question:** what's the best usage-based clustering?
- Group by the corpus conversations/sentences they appear in?
- Group by conceptual affinity (perception roots, agency roots, etc.)?
- Frequency-weighted: most-used roots first?

**Outcome:** after 4–5 lessons, learner knows ~20 roots from repeated
use and can recall their semantic field when encountering them.

---

### Stage 2 — Compound construction

This is where learners will actually fail. If someone quits Tonesu, it
will be here. The stage needs especially careful design.

- Head-final rule in depth. Practice: given two roots, build the compound
  and explain what it means.
- The `'` juncture marker: when and why.
- The `no-X` negation pattern.
- The `[X]-no-fe` extremal pattern.
- Common derivational patterns: `-li` (person), `-mu` (device/tool),
  `-pa` (place), `-ge` (state/quality), `-ki` (action/change).

#### Ambiguity resolution drills (critical exercise type)

Give a compound like `to-fe-su-ki`. Ask:
- What are 2–3 possible parses?
- Which is correct and why?
- What would a different parse mean?

This trains structural thinking under ambiguity — the core cognitive
skill for Tonesu fluency. These drills should appear in *every* lesson
from Stage 2 onward.

**Outcome:** learner can construct unfamiliar compounds from roots alone
and correctly parse multi-root chains, including resolving ambiguous
bracketings.

---

### Stage 3 — Grammar and notation in use

Grammar particles and notation marks are taught *together* because
learners experience them together. In real Tonesu, `go {premise}, result`
involves a particle *and* a structural bracket simultaneously; teaching
them in separate stages creates an artificial split.

**Grammar particles:**
- `la-` / `lo-` / `lu-` (agent / patient / result).
- `ne` copula — property attribution only; not identity.
- `go` causal particle — necessary connection (Hume's distinction).
- `;` sequential connector — constant conjunction without asserted mechanism.
- `/` parallel partition.
- `he` vocative · `ya` attention signal.
- `ke` pivot · `no —` denial sequence.
- `ru-fe` exclusive scope.
- `helm` / `helms` identity spectrum.

**Notation marks (semantic operators):**
- Evidential frame `()` — not asserting; reported/inferred.
- Aside frame `[]` — annotation that doesn't alter truth conditions.
- Approximation `~` / `ven`.
- Quotation `""` — direct speech, mention, titles.
- Prosodic suspension `—` / `el`.
- Scope prefixes `a- i- u- o- e-` and the `la-` merge hazard.
- Topic frame `:` — sentence-initial "as for X."

**Outcome:** learner can produce and parse multi-clause constructions
including causal chains, parallels, denials, evidential hedges, and
aside annotations.

---

### Stage 4 — Derived vocabulary and corpus fluency

- Work through the registry by domain or through corpus sentences.
- Each derived entry: parse it from roots, verify the gloss makes sense.
- Corpus sentences as the main exposure vehicle — real sentences, not
  contrived examples.
- Continue ambiguity drills with longer compounds.

**Outcome:** learner has a working vocabulary of 50–100 derived forms
and can look up unfamiliar words and parse them independently.

---

### Stage 5 — Epistemic discipline

Not just grammar — the philosophical core of the language.

- When to use `se` (perception) vs `to` (knowledge/pattern).
- When *not* to upgrade a claim — the difference matters.
- How epistemic misuse looks and why it's wrong.
- The evidential frame `()` as a tool for intellectual honesty.
- The `~` approximation mark: when precision should give way.
- `helm` vs `helms` vs `ne`: the three-way identity/attribution spectrum
  and when each is appropriate.

Corpus sentences from the fallacy batch (FAL, S374–S397) and theological
batch (THO) are rich material here — they were designed to stress-test
exactly these distinctions.

**Outcome:** learner can produce well-calibrated Tonesu: not just
grammatically correct, but epistemically honest.

---

### Stage 6 — Production and colloquial register

- Writing original sentences from prompts.
- Applying CLQ contraction rules.
- Understanding when formal vs colloquial register is appropriate.
- Translation challenges: given an English sentence, produce Tonesu
  and justify each structural choice.

**Outcome:** learner can produce grammatically correct, well-registered
Tonesu for a given communicative context.

---

## Format: Corpus-first + reference backing (C+B hybrid)

**Decided.** The other options were considered and eliminated:

- **Option A (linear lessons):** too artificial. You end up fighting the
  language's own compositional design.
- **Option B (reference + guided tour):** too passive. Good for someone
  who already knows the language, not for acquisition.
- **Option D (domain-first):** primitives appear in all domains, so you
  can't avoid front-loading them. Motivation is good but structure breaks.
- **Option C (corpus-driven inductive) + B (reference backing):** wins.

### Why C+B is right for Tonesu

Tonesu is compositional, pattern-driven, and structurally consistent.
That makes it perfect for inductive learning: show patterns, let the
learner notice them, then formalize.

The existing reference content (Grammar, Morphology, Building words,
Patterns, Notation) stays as-is — it's the backing material that
a learner links to when they want the full rule. Learning content
does not duplicate it.

### Lesson structure (each lesson = one sentence cluster)

1. **Show 2–4 real sentences.** No explanation yet.
2. **Ask the learner to notice a pattern.** What's similar? What changed?
3. **Explain:** 1 new concept + 2–3 new roots.
4. **Exercises:**
   - Parse drill: decompose a compound.
   - Build drill: construct a compound from a semantic target.
   - Ambiguity drill (Stage 2+): resolve a multi-root parse.
   - Translation prompt (Stage 3+): English → Tonesu.
5. **Link to reference** for the formal rule behind the concept.

### Advanced track: translation walkthroughs

The Bible, Tao Te Ching, and other translation files are rich
pedagogical material. A translation walkthrough can *be* a lesson:

> "In this lesson we translate Genesis 1:1–3 and encounter these
> five new compounds for the first time."

This is where Tonesu shines — forced to express genuinely hard
concepts. These walkthroughs serve as both advanced lessons and
reading material.

---

## Open design questions

1. **Who is the learner?** Conlang hobbyist? Philosopher wanting precise
   language? Someone engaging with the Bible translation project?
   Different profiles may need different entry points.

2. **What's the target fluency level?** Reading corpus sentences vs
   producing original ones vs engaging in real-time conversation
   (if that's ever a use case) — very different targets.

3. **Exercise design specifics:**
   - How many exercises per lesson? (Candidate: 3–5)
   - Self-check only. Scored evaluation would require knowing the learner's
     intended meaning — not inferrable from form alone.
   - Feedback taxonomy for build / translation drills (four types):
     - **Valid but different meaning** — the learner's answer is structurally
       correct but encodes a different claim than the target. Not an error;
       flag as alternate.
     - **Over-specified** — the learner added more structure than the target
       requires (e.g. added a scope prefix when the bare form suffices).
     - **Under-specified** — the learner's form is ambiguous where the target
       is not (e.g. missing `'` juncture in a 4-root chain).
     - **Structural error** — the form violates a rule (wrong tier, bad root
       order, parse invariant broken).
   - Answer keys: expandable sections (avoids spoiler on first read-through).

4. **Word Builder as lesson platform** (`tonesu/builder.md`). The builder
   is already a functional interactive tool — lessons should treat it as a
   first-class practice environment, not just an optional link.

   Proposed integration model:

   - **Guided building (Stage 0–1):** pre-load part of the compound chain
     in the builder; learner selects the missing root(s) to complete it.
     The builder shows the resulting gloss immediately — feedback is the
     compound's meaning, not a score.
   - **Constrained building (Stage 1–2):** restrict the builder's visible
     root palette to the roots introduced so far in the lesson sequence.
     Unlocking more roots as stages advance makes the palette itself a
     progression signal.
   - **Reverse parsing (Stage 2–3):** give the learner a complete compound
     in the builder; ask them to identify the head, the modifier, and the
     juncture. The builder's parse view is the answer key.
   - **Ambiguity mode (Stage 2+):** give a 4-root chain without `'`; ask
     the learner to build both legal bracketings and explain what each means.
   - **Translation mode (Stage 3+):** English prompt → learner builds in the
     builder → compare against the target; apply the four-type feedback
     taxonomy above.

   Root gating (restricting the palette) is the primary mechanism that
   ties the builder to the stage progression. Requires a small addition to
   the builder's JS: a parameter to accept an allowed-roots list.

5. **Spaced repetition:** Is there a role for SRS (Anki-style) for the
   34 primitives? Probably yes as a supplementary tool alongside Stage 1
   lessons. How do we author that deck?

6. **Lesson length / granularity:** One concept per lesson? Short (5 min)
   or long (30 min) sessions? Working hypothesis: short, ~10 minutes,
   one concept + one sentence cluster.

7. **Prerequisites:** Does any lesson assume another? Probably yes — the
   stages are sequential. Do we need a formal prerequisite graph or is
   "do them in order" sufficient?

8. **First lesson candidate:** Stage 0 — "First Contact." Use foundations
   corpus (C001–C008). Introduce ~8 roots. 3–5 sentences. 2 parse exercises.
   Link to Quick start and Primitives page for reference.

---

## Files / resources that feed this work

| Resource | What it provides |
|----------|-----------------|
| `spec/phonology.md` | Sound system and tier structure |
| `spec/grammar.md` | Full particle and slot reference |
| `spec/morphology.md` | Derivational affixes |
| `spec/word-formation.md` | Compound construction rules |
| `registry/primitives.md` | The 34 CV roots |
| `notes/phonosemantic-map.md` | Phonosemantic family groupings (Stage 1 reference) |
| `notes/basics.md` | Language basics summary |
| `corpus/sentences/v4-current/` | Worked sentences for exercises |
| `corpus/conversations/` | Dialogue examples (Stage 0 First Contact source) |
| `corpus/translations/` | Advanced track / translation walkthroughs |
| `notes/open-questions.md` | Edge cases learners will hit |
| `www/docs/quick-start.md` | Existing quick start — possible Stage 0 complement |
| `www/docs/cheatsheet.md` | Cheat sheet — reference companion for lessons |
| `www/docs/tonesu/builder.md` | Word Builder — interactive compound practice tool (Stage 0+) |

---

## Feedback log

### 2026-03-20 — Second pass (word builder integration)

| Issue | Resolution |
|-------|------------|
| Open Q #3: "self-check or scored?" too vague | Answered: self-check; added four-type feedback taxonomy |
| Open Q #4: builder as optional link only | Reframed as first-class lesson platform with 5-mode integration model |
| Missing: progression mechanism | Root gating identified — palette restriction drives Stage 0→1→2 advance |

---

### 2026-03-20 — Initial review

Key critique: design was "extremely well-structured but slightly too
top-down." Specific issues and resolutions:

| Issue | Resolution |
|-------|------------|
| Stage 0 too abstract (tier system, formal structure) | Replaced with "First Contact" — real sentences first |
| Stage 1: "learn 34 primitives as a map" = too heavy | Changed to progressive root introduction through sentences; map is reference |
| Grammar and notation taught separately | Merged into one stage — learners experience them together |
| Missing: ambiguity resolution drills | Added to Stage 2 as a critical exercise type, recurring thereafter |
| Missing: epistemic discipline as a skill | Added as Stage 5 — philosophical core, not just grammar |
| Format undecided | Locked in C+B hybrid (corpus-first + reference backing) |
| Translation walkthroughs undervalued | Elevated to explicit advanced track |
| Overall: reference-first instead of cognition-first | Restructured all stages to show → then explain |

> "You've designed the perfect reference manual — now tilt it 20% toward
> a learning experience."

---

*Next step: draft Stage 0 — First Contact. Select 3–5 foundation corpus
sentences, identify the ~8 roots they use, write the lesson using the
sentence-cluster format.*
