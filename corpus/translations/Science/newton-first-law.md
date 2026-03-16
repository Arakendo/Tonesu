# Translation Test: Newton's First Law of Motion

## Source: Isaac Newton, *Philosophiæ Naturalis Principia Mathematica* (1687), Book I, Axioms or Laws of Motion, Law I
## Reference text: Andrew Motte translation (1729), revised; as "Every body perseveres in its state of rest, or of uniform motion in a right line, unless it is compelled to change that state by forces impressed thereon."
## Status: Draft — first pass

---

## Purpose

Newton's First Law is the scientific-language stress test. It tests Tonesu against:

- **Universal quantification**: "every body" → quantifying over the class of all physical objects
- **Inertia**: a body's natural state = persistence, no action required
- **State predicate**: a body's state (rest or motion) as a structural property
- **Conditional/exception structure**: "unless" = the exception clause for force application
- **External causation**: force as an agent that acts on a body from outside
- **Disjunction gap**: Tonesu has no "or" particle; the rest/motion disjunction must be handled compositionally

This is the first scientific-law translation in the corpus. It tests whether Tonesu can express general laws of nature, not just narrative claims.

Corpus sentences from this batch: **S450–S451**.

---

## Vocabulary Framework

New compositional forms introduced in this batch:

| Form | Reading | Construction | W# |
|------|---------|--------------|-----|
| `fe-ma` | a bounded material body / a Newtonian body | `fe` (boundary/limit) + `ma` (matter/substance) = matter-with-definite-boundary = a discrete physical object. Covers all scales: particle, rock, planet. Head: `ma` (matter); modifier: `fe` (bounded). | Unregistered compositional |
| `su-ki-pa` | spatial motion-state | `su` (structure/order) + `ki` (motion) + `pa` (place/space) = the structural configuration of motion in space = the state of rest or constant motion that characterizes a body. Head: `pa`; modifiers: `su-ki` = ordered motion. | Unregistered compositional |
| `no-ko-ra` | external force | `no` (negation/absence) + `ko` (containment/interior) + `ra` (force/energy) = force-that-is-not-interior = a force acting from outside the system. Head: `ra` (force); modifier: `no-ko` (non-interior). | Unregistered compositional |

### Why `fe-ma` for "body"

Newton's "body" (Latin: *corpus*) = any bounded piece of matter, regarded as a unit. This is distinct from:
- `ma` (unformed matter/substance) — the raw material, not yet bounded
- `ma-su` (structured matter = rock/mineral, MAT-001) — matter organized into geological form
- `zo-ma` (W163, living matter = biological body) — matter that is living

`fe-ma` = matter-with-definite-boundary = a materially-delimited unit. It is matter (`ma`) that has been conceptually or physically bounded (`fe`) into an individual object. The Newtonian body is precisely this: a chunk of matter treated as a single system with a definite boundary. `fe-ma` is clean and unambiguous.

**Candidate for W registration:** `fe-ma` → a physical body / bounded material object. Block W169 or next available.

### Why `su-ki-pa` collapses "rest or uniform motion in a straight line"

Newton's disjunction ("at rest OR in uniform motion in a straight line") is actually **one physical state viewed from different frames** — inertia. Both zero velocity and constant velocity share the same causal character: no net force. In Tonesu, `su-ki-pa` = the spatial motion-structure = the body's current motion configuration, covers both:
- Rest: `su-ki-pa` where the motion component is zero
- Uniform linear motion: `su-ki-pa` where motion component is non-zero but constant

**Disjunction gap (GAP-NEW-001):** Tonesu has no dedicated "or" particle. The rest/motion disjunction is collapsed to `su-ki-pa` (motion-state), documenting the gap but making the semantics exact. The collapsing is philosophically defensible: Galilean relativity shows rest and uniform motion are the same state.

### No "unless" particle (GAP-NEW-002)

Tonesu has no dedicated "unless" particle. The law is split into two complementary sentences:
- **S450 (positive inertial case)**: "When no external force acts on a body, it maintains its motion-state." (`go no-{force-acts}` → `re su-ki-pa-ze`)
- **S451 (force case)**: "When external force acts on a body, its motion-state changes." (`go {force-acts}` → `lo-su-ki-pa-ze  ki`)

The two together constitute Newton's First Law as a biconditional. Neither sentence alone is complete; their conjunction is.

---

## Source Text

> **Law I.** Every body continues in its state of rest, or of uniform motion in a right line, unless it is compelled to change that state by forces impressed thereon.

---

## Clause-by-Clause Analysis

### S450 — Inertial persistence (the "unless absent" case)

"A body maintains its motion-state as long as no external force acts on it."

```
pu-fe-ma  :  go  no  la-no-ko-ra  ka-ki  lo-ze  /  la-ze  re  su-ki-pa-ze
```

**Written:** `pufema : go no lanokora kaki loze / laze re sukipaze`

**Parse:**
- `pu-fe-ma` = all bounded-matter = every body [topic, with `:` frame]
- `go` = causal frame introducer: "when/if..."
- `no` = clause negation (Level 3): negates the following agent-action-patient clause
- `la-no-ko-ra` = external-force [agent]
- `ka-ki` = acts-on / applies motion to [action]
- `lo-ze` = [it] as patient — `ze` anaphoric to the `pu-fe-ma` topic
- `/` = clause boundary
- `la-ze` = [the body, anaphoric to `pu-fe-ma`]
- `re` = maintains / persists / cycles
- `su-ki-pa-ze` = its spatial motion-state

**Full reading:** For every bounded material body: when no external force acts on it, it persists in its spatial motion-state.

The `pu-fe-ma :` topic frame establishes universal quantification over the class of all physical bodies. `ze` as anaphora then refers distributively to each member. The `go no {agent ka-X lo-ze}` / `la-ze re X` structure is: [causal condition = force absent] → [inertial result = persistence].

### S451 — Force causes change (the exception case)

"When external force acts on a body, its motion-state changes."

```
go  la-no-ko-ra  ka-ki  lo-fe-ma  /  lo-su-ki-pa-ze  ki
```

**Written:** `go lanokora kaki lofema / losukipaze ki`

**Parse:**
- `go` = causal frame: "when..."
- `la-no-ko-ra` = external-force [agent]
- `ka-ki` = applies force / acts on
- `lo-fe-ma` = [a] material-body [patient]
- `/` = clause boundary
- `lo-su-ki-pa-ze` = its motion-state [patient]
- `ki` = moves / changes

**Full reading:** When external force acts on a material body, its motion-state changes.

This is the contrapositive of S450 and completes the biconditional. Together S450+S451 express: no-force ↔ state-persists; force ↔ state-changes.

---

## Structural Gap Documentation

### GAP-NEW-001: No disjunction particle

English "or" and Latin "vel" express inclusive disjunction. Tonesu has no dedicated disjunction particle. Workarounds:
1. **Collapse the disjunction** (used here): where the disjuncts are physically equivalent (inertia), a single compound covers both.
2. **Parataxis**: state both disjuncts as separate propositions without explicit connective.
3. **Semantic embedding**: `{A ro B}` constructions can sometimes express "A or B" through instrument-framing, but this is strained.

**Resolution path:** a bare `ro` between two noun phrases, when neither is an instrument, might develop an OR-reading through corpus pressure. Alternatively, a new particle could be introduced. Deferred to the 300-compound milestone vocabulary review.

### GAP-NEW-002: No "unless" particle

"Unless X, Y" = "Y holds except when X" = "if NOT X, then Y." Workaround: split into two complementary sentences. The split is mathematically equivalent but rhetorically less unified than Newton's single law. A possible particle would be `no-go` (negation-of-cause) extended to a conditional-exception role — but `no-go` currently means "despite/concessive." The semantic extension from "despite" to "unless" is non-trivial.

### GAP-NEW-003: No continuous-state verb

"Continues in its state" implies ongoing persistence without change. Tonesu's `re` = repetition/cycle — which captures the iterative aspect (the state recurs) but not the continuous-unbroken-identity of state. A body at rest *stays* at rest (no repetition needed); `re` implies cycling, not stasis. Workaround: accept `re` as "maintains through repetition" = a close approximation. The gap between "persists unchanged" and "recurs the same state" is philosophically meaningful but may not require a dedicated particle.

---

## NEW-001 Batch Summary

| Entry | Form | Key test |
|-------|------|---------|
| NEW-001-A (S450) | `pufema : go no lanokora kaki loze / laze re sukipaze` | Universal quantification via `pu-X :` topic frame; inertial persistence |
| NEW-001-B (S451) | `go lanokora kaki lofema / losukipaze ki` | Force as external agent; state-change as patient result |

**Key findings:**
- `pu-X :` (universal topic frame) is productive for scientific laws: "for all X: ..."
- Newton's "unless" requires a two-sentence biconditional split — no single-sentence encoding available
- The disjunction of "rest or uniform motion" resolves to `su-ki-pa` (motion-state) without information loss due to Galilean relativity
- `no-ko-ra` (external force) is a clean compositional form

**New composites introduced (candidates for W-registration):**
- `fe-ma` — bounded material body (Newtonian body)
- `su-ki-pa` — spatial motion-state
- `no-ko-ra` — external force
