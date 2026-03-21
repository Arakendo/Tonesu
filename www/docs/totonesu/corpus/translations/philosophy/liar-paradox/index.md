---
batch_codes: [LPR]
---
# Translation Test: The Liar Paradox

## Source: Epimenides / Eubulides (~600–300 BCE); canonical form attributed to Eubulides of Miletus
## Status: Draft — first pass

---

## Purpose

The Liar Paradox is the **self-referential truth-predicate stress test**. It requires three capabilities simultaneously:

1. **Self-reference** — a sentence that denotes itself as an object
2. **A propositional truth predicate** — a predicate `T(p)` that applies to individual propositions and can be negated
3. **Propositions treated as first-class objects** — proposition `p` available as the subject of a higher-level claim

The question for Tonesu:

> **Can the language form a sentence that refers to itself as false? If not, does the language have an accidental in-built protection — and does that protection correspond to anything in the known formal literature?**

Either outcome is interesting. This batch tests all three required capabilities and documents the result.

Corpus sentences from this batch: **S465–S467**.

---

## Vocabulary Framework

| Form | Reading | Notes |
|------|---------|-------|
| `tonesu` / `to-ne-su` | truth as a state; complete structured knowledge | W000; established. **NOT a propositional truth predicate** — see analysis below |
| `du-to` | obtaining fact / a proposition that holds | established WIT-001 (S461); `du` (result/actualization) + `to` (conceptual-pattern = proposition); an obtaining proposition |
| `no-du-to` | non-obtaining / false as a proposition | `no` + `du-to`; a proposition that does not hold |
| `no-tonesu` | absence of organized truth; epistemic incoherence | `no` + `tonesu`; the state of knowledge lacking coherent structure; **not "false" in the propositional sense** |
| `vund … vunds` | evidential frame | G014/G015; wraps reported/inferred content; speaker is structurally outside the frame |

---

## The Central Diagnostic: `tonesu` is not `T(p)`

`tonesu` (W000) is defined as:

> "complete structured knowledge; the condition of patterns held together in structure = truth as an organized relational whole."

This is truth-as-a-state — an epistemic condition, a property of a knowledge system. It is Aristotelian aletheia, not the logician's sentence-level truth predicate.

The Liar Paradox requires a *propositional* truth predicate: a function `T` that takes proposition `p` as argument and returns a truth value — so that `T(p)` can be negated to give "p is false." Examples from formal logic: Tarski's `Tr(p)`, Frege's assertion stroke applied to the negation of `p`.

`tonesu` does not do this job. You cannot write `T(p)` using `tonesu` with `p` = a named proposition, because `tonesu` doesn't take proposition-arguments — it describes a state of organized knowledge, not the truth value of an individual sentence.

`no-tonesu` therefore means "absence of the organized-knowledge condition" — something like ignorance, confusion, epistemic failure, or incoherence. It does not mean "this proposition is false." These are different concepts and the distinction is structural.

**The right candidate for a propositional truth predicate:** `du-to` (WIT-001). An obtaining fact is a proposition that holds — `la-X ne du-to` = X is an obtaining fact = X is true. `la-X ne no-du-to` = X does not obtain = X is false. This maps Tarski's `Tr(p)` / `¬Tr(p)` cleanly.

---

## Structural Block 1 — No Sentence Indexical

To form the Liar you need a noun phrase that means "this sentence" or "this proposition" — pointing from *inside* a sentence back to the sentence itself.

Tonesu's pronoun inventory:

| Form | Referent |
|------|---------|
| `mi` | first person |
| `tu` | second person |
| `ze` | third person singular |
| `yu` | third person plural |

No pro-form exists for "this proposition" or "the sentence currently being processed." The closest would be a demonstrative pointing to a previously-named claim — but a demonstrative points to something *already established* at a higher level; it cannot point forward to the containing clause from within it.

For the Liar you'd need something like `lo-{lam}` where `lam` names the sentence. But naming the sentence requires establishing it as an object at a level *above* the sentence — which brings us to Block 2.

---

## Structural Block 2 — `vund … vunds` Instantiates Tarski's Hierarchy

The evidential frame `vund … vunds` is defined as:

> "content is reported, inferred, or unattributed — **not directly asserted by the speaker**"

The speaker who uses `vund … vunds` is *structurally outside the frame*. The frame produces an object (a reportable proposition) at level N; the framing speaker is at level N+1. The speaking/asserting act is always one level up from the framed content.

This is precisely **Tarski's object-language / metalanguage hierarchy** built into the syntax.

For the Liar to form, the frame content at level N would need to predicate falsity of the frame *as a whole* — which is the level N+1 object. To do that, a level-N expression would need to reach up and refer to its own level-N+1 container. The frame enforces a strict one-directional level boundary: you can look down (the metalanguage refers to the object language) but not up (the object language cannot refer to the metalanguage container it's inside).

This means `vund … vunds` is not merely an epistemic annotation — it is structurally paradox-resistant. You cannot form a self-referential loop through the evidential frame because the directional level constraint prevents it.

---

## Three-Way Verdict

| Requirement | Tonesu capability | Assessment |
|-------------|------------------|------------|
| Self-reference | No sentence-indexical pronoun | **Block 1 — not expressible** |
| Propositional truth predicate | `du-to` / `no-du-to` (WIT-001) | **Available, but…** |
| Frame allows self-predication | `vund…vunds` enforces level separation | **Block 2 — frame prevents it** |

Tonesu cannot form the classical Liar Paradox. It lacks the sentence-indexical (Block 1) and its evidential frame mechanically separates the asserting level from the reported level (Block 2). Both blocks are independently sufficient; together they are redundant protection.

**The correspondence:** Tarski argued that paradox-free semantic systems require a hierarchy of languages — no language can contain its own truth predicate for sentences of that language; a metalanguage is always needed. `vund … vunds` operationalizes this: every framed proposition is object-language; every truth claim about it is metalanguage. The Tonesu design appears to have implemented a Tarski hierarchy inadvertently, as a consequence of making the evidential frame a mandatory one-directional meta-operator.

---

## Source Text

> **"This sentence is false."**
> (Canonical Liar: Eubulides of Miletus, paraphrasing; formal version: "The proposition expressed by this sentence does not obtain.")

---

## Verse-by-Verse Analysis

### S465 — Naive attempt with `tonesu` (LPR-001-A)

```
vund ne no-tonesu vunds
```

**Written:** `vund ne notonesu vunds`

The most obvious first attempt: frame the claim, predicate `no-tonesu` (not-truth). This fails on two independent grounds:

1. **`no-tonesu` is the wrong predicate.** `tonesu` is the state of organized coherent knowledge — its negation is epistemic incoherence (ignorance, confusion), not propositional falsehood. `vund ne no-tonesu vunds` does not say "this content is false" — it says "reportedly: is-not-organized-knowledge." That is a claim about the epistemic condition of the reporter, not about the truth value of a proposition.

2. **No self-reference.** The frame has no subject — `ne no-tonesu` needs something to predicate over. Even if `lo-{this}` existed, pointing it at the containing frame would create a level-crossing that Block 2 prevents.

This form is grammatically marginal (subject missing from `ne` predication) and semantically wrong for the Liar's purpose. It does not express the paradox.

### S466 — Better attempt with `du-to` (LPR-001-B)

```
vund ne no-du-to vunds
```

**Written:** `vund ne noduto vunds`

Upgrading from `tonesu` to the propositional truth predicate `du-to` gives a cleaner target: "reportedly: [it] is not an obtaining fact." This is at least using the right tool. But it hits both structural blocks:

**Block 1 — missing subject:** `ne no-du-to` predicates non-factuality of something; that something needs to be a named noun phrase. The Liar requires that noun phrase to be pointing back to the containing frame. No such pointing-back pronoun exists. The subject is absent; the form is a predicate waiting for a subject it cannot acquire.

**Block 2 — level violation:** Even if you named the frame from outside (`lo-{this-claim}`), you'd be forming the subject at level N+1 (metalanguage) and then importing it into the predication at level N (object language). The frame allows the level N+1 speaker to predicate over the level N content — but the reverse isn't available. `vund … vunds` is one-directional: the wrapper observes the content; the content cannot observe the wrapper.

In pseudo-notation (not Tonesu, metalanguage only):
```
Frame(X)  where  X = {Frame(X) is not-obtaining}
```
X requires `Frame(X)` as an object from within X — that is the crossing the level-separation forbids.

This sentence can be written mechanically and is grammatically parseable as a frame with a missing subject. It does not express a paradox; it expresses an incomplete predication.

### S467 — What Tonesu CAN say: third-party truth claim (LPR-001-C)

```
lo-to-ze  ne  no-du-to
```

**Written:** `lotoze ne noduto`

This is the **legitimate, well-formed, non-paradoxical cognate**: "her proposition / the claim she made does not obtain = is false."

`lo-to-ze` = patient-proposition-hers = the conceptual-content (`to`) attributed to a third person (`ze`) = her claim / what she said. `ne no-du-to` = is not an obtaining fact = is false. The speaker making this sentence is at a higher level than the claim being evaluated — standard Tarskian object/metalanguage. No loop. Well-formed. Useful.

The Liar would require the `ze` to refer to the current sentence itself — but `ze` is a third-person agent pronoun, not a propositional indexical. It can point to a person; it cannot point to a sentence. `lo-to-ze` therefore always refers to some external person's claim, never to the sentence containing the predication.

**S467 shows the available move:** Tonesu can evaluate the truth status of other sentences without paradox because the evaluating sentence is always at a higher level. The language handles truth attribution cleanly for the case that matters (assessing external claims); it simply cannot turn that operation inward on itself.

---

## LPR-001 Batch Summary

| Entry | Form | Result |
|-------|------|--------|
| S465 (LPR-001-A) | `vund ne notonesu vunds` | Wrong predicate (`no-tonesu` ≠ false); subject missing; does not express Liar |
| S466 (LPR-001-B) | `vund ne noduto vunds` | Right predicate, wrong structure; Block 1 (no indexical) + Block 2 (Tarski level) both prevent self-reference |
| S467 (LPR-001-C) | `lotoze ne noduto` | Well-formed third-party falsehood claim; the structure Tonesu CAN express |

**Key finding:** Tonesu cannot form the Liar Paradox for two independent structural reasons. First, there is no sentence-indexical pronoun — no way to refer to the containing sentence from within it. Second, the evidential frame `vund … vunds` structurally enforces Tarski's object-language / metalanguage hierarchy: the asserting speaker is always one level above the framed content, and content inside the frame cannot reach back up to predicate over the frame itself.

Neither block was explicitly designed to prevent the Liar Paradox. Both emerged from independent design decisions (pronoun system scope; evidential-frame semantics). The paradox resistance is an emergent property. The `v`-family notation mark designed to handle epistemic reportage turns out to implement, in lightweight syntactic form, the solution to the 2,600-year-old problem that drove Russell to type theory and Tarski to hierarchical semantics.

**`tonesu` as truth predicate — verdict:** `tonesu` is not the right operand. It is truth-as-a-state (organized coherent knowledge), not a propositional T-predicate. `no-tonesu` = ignorance / epistemic failure, not propositional falsehood. The Liar requires `du-to` / `no-du-to`. The language has both words; they are doing different and non-competing jobs. This is a feature.

**New vocabulary:** none required.

**Open questions logged:** none — all three blocks are resolved within existing grammar. The analysis is complete.
