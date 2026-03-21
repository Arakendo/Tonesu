---
title: "The Liar Paradox — Self-Referential Truth Stress Test"
---

# The Liar Paradox — Self-Referential Truth Stress Test

*Theme: [Grammar & syntax](../../grammar/overview/)* · 3 sentences.

:material-book-open-variant: [Full translation analysis](../../translations/philosophy/liar-paradox/)

[← Grammar & syntax](../../grammar/overview/) · [← Corpus](../../overview.md)

---

## LPR-001 · The Liar Paradox — Self-Referential Truth Stress Test

**Purpose:** Tests whether Tonesu can form a self-referential falsehood sentence ("This sentence is false"). Probes three required capabilities: sentence-level self-reference, a propositional truth predicate, and propositions treated as first-class objects. Documents the structural blocks that prevent paradox formation and their correspondence to Tarski's hierarchy. Also documents why `tonesu` is the wrong truth predicate for this purpose, and what `du-to` / `no-du-to` actually do.

<span id="S465"></span>
**S465**
`vund ne no-tonesu vunds`
Written: `vund ne notonesu vunds`
*"This sentence is false." — naive attempt with `tonesu`*

!!! annotation "Notes"
    `vund … vunds` = evidential frame (G014/G015). `ne no-tonesu` = is not truth-as-organized-knowledge. **Fails as a Liar construction on two grounds.** First, `no-tonesu` is the wrong predicate: `tonesu` (W000) is truth as a *state* of organized coherent knowledge — its negation gives epistemic incoherence (ignorance, confusion), not propositional falsehood. `no-tonesu` ≠ "this proposition is false." Second, `ne no-tonesu` has no subject — there is no sentence-indexical in Tonesu that can point from inside the frame back to the frame itself. The form is grammatically marginal (predication without subject) and semantically wrong for the Liar's purpose.

<span id="S466"></span>
**S466**
`vund ne no-du-to vunds`
Written: `vund ne noduto vunds`
*"This sentence is false." — improved attempt with `du-to`*

!!! annotation "Notes"
    `du-to` = obtaining fact (established WIT-001, S461); `no-du-to` = non-obtaining = false as a propositional predicate — the right tool. Grammatically parseable as a frame with missing subject. **Fails as a Liar construction on two structural grounds.** Block 1 (no sentence-indexical): there is no noun phrase in Tonesu of the form "the proposition that is this sentence" — no pro-form can point back to the containing clause from within it. Block 2 (Tarski hierarchy): the evidential frame structurally separates the asserting speaker (level N+1) from the reported content (level N). The framing speaker can predicate over the frame content; the content cannot reach up to predicate over the frame. This is Tarski's object-language / metalanguage hierarchy instantiated in the syntax: `vund … vunds` is one-directional; the content cannot observe its wrapper.

<span id="S467"></span>
**S467**
`lo-to-ze  ne  no-du-to`
Written: `lotoze ne noduto`
*Third-party falsehood claim — what Tonesu CAN say*

!!! annotation "Notes"
    `lo-to-ze` = patient-proposition-hers = the conceptual claim (`to`) attributed to third person (`ze`) = her proposition / what she said. `ne no-du-to` = is not an obtaining fact = is false. Well-formed. The speaker evaluates an external claim from a higher level — standard Tarskian object/metalanguage structure. No loop. This is the available and productive construction: Tonesu can assess the truth status of external propositions without paradox, because the evaluating sentence is always outside the proposition being evaluated. The Liar collapses because `ze` is a person-pronoun, not a sentence-indexical; `lo-to-ze` always points to someone's claim, never to the current sentence.

### Batch Summary

| Entry | Form | Result |
|-------|------|--------|
| S465 (LPR-001-A) | `vund ne notonesu vunds` | Wrong predicate — `no-tonesu` ≠ false; subject missing; does not express Liar |
| S466 (LPR-001-B) | `vund ne noduto vunds` | Right predicate, wrong structure — Block 1 (no indexical) + Block 2 (Tarski hierarchy) independently prevent self-reference |
| S467 (LPR-001-C) | `lotoze ne noduto` | Well-formed — third-party falsehood claim; structure Tonesu CAN express |

**Key finding:** Tonesu cannot form the Liar Paradox. Two structural blocks are independently sufficient. Block 1: no sentence-indexical pronoun exists — there is no way to name the current sentence as an object from within it. Block 2: `vund … vunds` enforces Tarski's hierarchy — the asserting speaker is always outside the frame; the frame content cannot reach back to predicate over its container. Both blocks are emergent: neither was designed to prevent the Liar, but both do. The paradox resistance is a structural by-product of the evidential frame design and the pronoun system scope.

**`tonesu` as truth predicate — verdict:** `tonesu` (W000) is truth-as-a-state (organized coherent knowledge). `no-tonesu` = epistemic incoherence / ignorance — not "false." The Liar requires `du-to` / `no-du-to` (propositional truth / falsehood). The two truth concepts — `tonesu` (systemic) and `du-to` (propositional) — are doing different and non-competing jobs. This is a feature.

**New vocabulary introduced:** none.

**Open questions logged:** none — LPR analysis is complete within existing grammar.

---

*Generated from [`registry/entries.yaml`](https://github.com/Arakendo/Tonesu/blob/main/registry/entries.yaml).*