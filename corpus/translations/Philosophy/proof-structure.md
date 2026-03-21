---
batch_codes: [PRF-001]
---
# Translation Test: Proof Structure — Syllogism, Cogito, Reductio

## Source
Multiple canonical sources:
- The classical syllogism: Aristotle, *Prior Analytics*, Book I (~350 BCE). Canonical form: "All men are mortal; Socrates is a man; therefore Socrates is mortal."
- The Cogito: René Descartes, *Meditationes de Prima Philosophia* (1641), Meditatio II. Canonical form: *cogito ergo sum* — "I think, therefore I am."
- Hume's problem of induction: David Hume, *An Enquiry Concerning Human Understanding* (1748), § 4. Contrast between constant conjunction (sequence without grounding) and necessary connection.
- Argument from motion: Aristotle, *Physics*, Books VII–VIII; also *Metaphysics* Lambda. Informal reductio: recurrent cycles are observed; cycles require motion; therefore motion obtains.

## Status
Draft — first pass

---

## Purpose

This is a **pure grammar stress test** — no new vocabulary. All six sentences test connective structure, scope, and the grounding hierarchy between `;`, `go`, and `to-go`.

The central tests:

1. **`a-` universal scope in a deductive premise** — Does `a-zo-li` ("the universal person" = "all persons") work as the subject of a major syllogistic premise? This is the first use of `a-` as a logical universal quantifier rather than a general intensifier.

2. **Stacked `go {P}, go {P}, C`** — Is double-`go` grammatical? The stack rule says arbitrarily deep nesting is permitted; S686 is the first corpus instance of two stacked `go` clauses feeding a single conclusion.

3. **`;` vs `go` minimal pair (the Humean test)** — S687 and S688 are minimal contrast pairs on precisely the distinction Hume named: constant conjunction (S687, `;`) vs necessary connection (S688, `go`). The Cogito only works with `go`.

4. **`to-go` + `go to,` reductio** — S689 combines the counterfactual frame with an anaphoric `go to,` conclusion: "by the foregoing principle: motion." First reductio structure in corpus.

Corpus sentences: **S684–S689**

---

## Vocabulary Framework

No new entries. All forms are existing derived compounds, primitives, or spec-level operators.

| Form | W# | Reading | Context |
|------|----|---------|---------|
| `a-zo-li` | — | universal-person / all persons | `a-` scope prefix (spec) + `zo-li` (W049). First use in deductive premise. |
| `de-zo` | W178 | dying / mortality | Non-agentive death-event. Used as a predicate property ("is mortal"). |
| `zo-li` | W049 | person / individual agent | Standard. Minor-premise predicate. |
| `to-ki` | W020 | computation / reasoning process | Ongoing act of reasoning. Cogito premise. |
| `su-ti` | W101 | current configuration / present state | Used in patient frame: `lo-li su-ti` = the entity 'I' has a current state. Cogito conclusion. |
| `to-go` | W089 | counterfactual frame marker | Non-actual conditional. S689 reductio setup. |
| `no-ki` | — | no-motion / absence of change | `no` + `ki` (primitive). Compositional. S689. |
| `no-re` | — | no-recurrence / absence of cycles | `no` + `re` (primitive). Compositional. S689. |
| `re` | — | recurrence / cycle (primitive) | Bare primitive. S689 empirical observation. |
| `;` | G027 | sequential connector | Humean constant conjunction. Tested as distinct from `go`. |
| `go` | — | causal/grounding frame (primitive) | Necessary connection. Core of the Cogito and reductio conclusion. |

### The `;` / `go` distinction

The axis on which S687 and S688 differ is exactly Hume's problem of induction:

> "We have no other notion of cause and effect, but that of certain objects, which have been always conjoined together, and which in all past instances have been found inseparable. We cannot penetrate into the reason of the conjunction." — *Enquiry*, § 7

- `;` = constant conjunction only: two states are recorded in sequence. The `;` asserts nothing about why B follows A.
- `go` = necessary connection: the premise constitutively grounds the consequence. The `go` asserts that A is the reason B holds.

The Cogito requires `go` because Descartes' claim is not merely that "thinking" and "existing" co-occur as observed facts. The thinking is the *ground* — the constitutive basis — for the existence-claim. This is why S687 (`la-li to-ki ; lo-li su-ti`) is the wrong form: it records two observations in sequence, which Hume would recognize as constant conjunction and would deny proves anything about existence.

S688 (`go {la-li to-ki}, lo-li su-ti`) is the correct form: the `go` asserts the grounding relationship, not merely the sequence. This is the Cogito.

### The `a-` universal scope prefix

`a-` = abstract/universal scope modifier. Attaches as a prefix to the following word. `a-zo-li` = universal-person = "persons in the abstract / all persons." No new entry needed — `a-` is spec-defined.

In the syllogism, `a-zo-li` acts as a universally-quantified subject. This is the first corpus instance of `a-` in a deductive logical premise (as opposed to episodic or descriptive contexts).

### `su-ti` in the Cogito

`su-ti` (W101) is defined as "current configuration; the structural condition of a system at a specific moment in time." Canonical frame: `lo-X su-ti Y` = X is currently in configuration Y.

For the Cogito, `lo-li su-ti` (no Y specified) = the entity marked 'I' has *some* current configuration = "I have a present instantiation" = "I exist right now." The Y is left unspecified because the existential claim is not about any particular state — it is about having *a* state at all. `su-ti` without Y reads: "is in [some determinate] current configuration" = minimally and exactly "exists at this moment."

The self-certifying structure: the act of uttering S688 instantiates `la-li to-ki` (I am reasoning), which via `go` grounds `lo-li su-ti` (I have a current configuration). The sentence instantiates its own premise.

---

## Source Text

> *Aristotle, Prior Analytics I.1–4:*
> All men are mortal. Socrates is a man. Therefore Socrates is mortal.

> *Descartes, Meditatio II:*
> Cogito, ergo sum. [A thing that thinks cannot not-exist at the moment of thinking.]

> *Aristotle, Physics VIII / Metaphysics XII:*
> [Paraphrase of modus tollens from circular motion:] If there were no motion, there would be no recurrence of celestial cycles. Such cycles are observed. Therefore motion exists.

---

## Verse-by-Verse Analysis

### S684 — Major syllogistic premise

```
a-zo-li  ne  de-zo
```

**Written:** `azoli ne dezo`

**Reading:** All persons are [of the] mortal kind.

**Notes:** `a-zo-li` = universally-scoped person. `ne de-zo` = property attribution: the mortality/dying property (W178). Property attribution with `ne` reads "has the character of" — so `a-zo-li ne de-zo` = "the universally-quantified person has the character of dying." Equivalent to the classical major premise: All men are mortal. First use of `a-` to establish a universal quantified claim as a logical premise rather than an episodic description.

---

### S685 — Minor syllogistic premise

```
la-Sokrates  ne  zo-li
```

**Written:** `laSokrates ne zoli`

**Reading:** Socrates is a person.

**Notes:** Standard property attribution. `Sokrates` = conventionally adapted proper name. The minor premise is structurally identical to other property attributions in the corpus — no special treatment for proper names in the predicate frame. `la-Sokrates ne zo-li` = Sokrates has the character of being a person-agent (W049).

---

### S686 — Syllogistic conclusion via stacked `go`

```
go  a-zo-li  ne  de-zo ,  go  la-Sokrates  ne  zo-li ,  la-Sokrates  ne  de-zo
```

**Written:** `go azoli ne dezo, go laSokrates ne zoli, laSokrates ne dezo`

**Reading:** Because all persons are mortal, and because Socrates is a person: Socrates is mortal.

**Notes:** First stacked double-`go {P}, go {P}, C` in corpus. Stack trace: `go` opens clause level 1; property clause `a-zo-li ne de-zo` is syntactically complete (agent + `ne` + property NP); `,` marks the close of level 1. `go` opens level 2; property clause `la-Sokrates ne zo-li`; `,` closes level 2. Matrix clause `la-Sokrates ne de-zo` is the conclusion. The `ne` copula closes each `go` frame because the property-attribution clause is syntactically complete when the predicated property (a closed NP) is consumed. Both premises are necessary — neither alone yields the conclusion. The formal register makes all boundaries explicit via the `,` separators.

---

### S687 — Cogito, wrong form (constant conjunction)

```
la-li  to-ki ;  lo-li  su-ti
```

**Written:** `lali toki ; loli suti`

**Reading:** I am reasoning; I am in a current state.

**Notes:** Intentionally insufficient form of the Cogito. The `;` records two sequential observations without asserting that the first grounds the second. `la-li to-ki` = I am engaged in the reasoning process (W020). `lo-li su-ti` = the entity 'I' has a current configuration (W101, patient frame). The claim is semantically true but logically insufficient: it says that thinking and existing co-occur as observed facts (constant conjunction) but does not assert the constitutive relationship Descartes requires. Compare S688.

---

### S688 — Cogito, correct form (grounded entailment)

```
go {la-li  to-ki},  lo-li  su-ti
```

**Written:** `go lali toki, loli suti`

**Reading:** Because I am reasoning: I have a determinate present state.

**Notes:** Correct Cogito. `go` asserts necessary connection: the reasoning is the constitutive ground for the existence-claim, not merely its temporal precursor. The `go` frame closes (`la-li to-ki` is syntactically complete) at `,`; the matrix clause `lo-li su-ti` is the conclusion. The patient frame `lo-li` is used because the Cogito's conclusion is about the entity 'I' *as a thing that has a current configuration* — `li` is the patient of the `su-ti` predicate, not the agent of an action. Self-certifying: uttering this sentence instantiates `la-li to-ki`, which via `go` grounds `lo-li su-ti`. The minimal pair S687/S688 is the sharpest expression of the Humean/Cartesian distinction in the corpus.

---

### S689 — Reductio: motion from cyclic recurrence

```
to-go {no-ki},  no-re ;  re  su-ti ;  go  to ,  ki
```

**Written:** `togo noki, nore ; re suti ; go to, ki`

**Reading:** If there were no motion, there would be no cyclic recurrence. Cyclic recurrence [currently] obtains. By the foregoing principle: motion.

**Notes:** Three-clause reductio structure. Clause 1 (`to-go {no-ki}, no-re`): the counterfactual conditional — non-actual premise "no motion" yields non-actual result "no cycles." This is the modus tollens setup: ¬motion → ¬cycles. `no-ki` = bare existential counterfactual (the no-motion state obtains, hypothetically). `no-re` = no cyclic recurrence. `;` (sequential connector) joins all three clauses as argumentative steps. Clause 2 (`re su-ti`): the empirical observation — the primitive `re` (recurrence/cycle) has a current configuration, i.e., cyclical patterns are currently instantiated and observable. Clause 3 (`go to, ki`): the logical conclusion. `to` is anaphoric (the conceptual-pattern primitive), referring to the principle established in clause 1. `go to,` = "grounded in / by the foregoing principle." `ki` = change/motion [obtains]. The `;` between steps says only that the three clauses are sequential steps in an argument — it does not assert causal connection between them. `go to,` marks only the final conclusion as logically grounded. First reductio in corpus; first anaphoric `go to,` conclusion.

---

## PRF-001 Batch Summary

| # | Source | Tonesu | Key test |
|---|--------|--------|---------|
| S684 | Syllogism — major premise | `a-zo-li  ne  de-zo` | `a-` scope prefix as logical universal |
| S685 | Syllogism — minor premise | `la-Sokrates  ne  zo-li` | Proper name in property attribution |
| S686 | Syllogism — conclusion | `go a-zo-li ne de-zo , go la-Sokrates ne zo-li , la-Sokrates ne de-zo` | First stacked double-`go {P}, go {P}, C` |
| S687 | Cogito (wrong) | `la-li  to-ki ;  lo-li  su-ti` | `;` = constant conjunction (Hume) |
| S688 | Cogito (correct) | `go {la-li  to-ki},  lo-li  su-ti` | `go` = necessary connection (Descartes) |
| S689 | Reductio from motion | `to-go {no-ki},  no-re ;  re  su-ti ;  go  to ,  ki` | Reductio; `go to,` anaphoric conclusion |

**New vocabulary:** none — pure grammar test.

**Key finding:** Tonesu has a structural commitment on the Hume/Descartes axis: `;` is a logical constant-conjunction particle (sequence without grounding); `go` is a necessary-connection particle (the premise constitutively grounds the conclusion). The Cogito requires `go`. The `;` version S687 is grammatical and true, but it is not the Cogito — it is what Hume would accept as evidence and Descartes would reject as insufficient. This distinction is irreducible inside Tonesu; no collapse is possible.

---

## Colloquial Register Analysis

| Form used | CLQ entry | Colloquial form | Notes |
|-----------|-----------|-----------------|-------|
| `a-zo-li` | none | — | `a-`-prefixed `zo-li` (2-root) — below 3-morpheme contraction threshold; prefix is spec-level, not a root |
| `de-zo` | none | — | 2-root — below threshold |
| `zo-li` | none | — | 2-root — below threshold |
| `to-ki` | none | — | 2-root — below threshold |
| `su-ti` | none | — | 2-root — below threshold |
| `to-go` | none | — | 2-root frame marker; semantically load-bearing — relaxation eliminates the counterfactual distinction |
| `no-ki` | none | — | 2-root compositional — below threshold |
| `no-re` | none | — | 2-root compositional — below threshold |
| `re` (primitive) | none | — | Primitive root — minimum possible |
| `;` | none | — | Semantically load-bearing operator — relaxation to `go` changes the claim (the entire batch tests this point) |
| `go` (particle) | none | — | Primitive — minimum possible |

**Verdict:** irreducibly formal — all forms are primitives, 2-root compounds below threshold, or semantically load-bearing operators.

*CLQ entries registered from this batch: none.*
