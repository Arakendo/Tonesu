# Contrast Walkthroughs

Every root in Tonesu pulls weight. This page takes pairs of roots or constructions that look similar and shows — with full sentences — exactly why they are not interchangeable.

---

## Comparison: `nu-be` / `nu-no`

Comparison is compositional: `nu` (quantity / measurable dimension) + `be` (more / growth) or `no` (less / negation). The baseline follows.

### Warmer room (S064)

```
lo-ko-pa  ha-vo  nu-be  lo-ki-pa
```
*The room is warmer than the corridor.*

| Element | Parse |
|---------|-------|
| `lo-ko-pa` | patient: contained-place (room) |
| `ha-vo` | thermal quality (warmth) |
| `nu-be` | more-than |
| `lo-ki-pa` | patient: motion-place (corridor) |

`nu-be` = "to a greater degree on this dimension." The dimension is `ha-vo`; the baseline is `lo-ki-pa`.

### Bigger machine (S065)

```
lo-mu  pa-nu  nu-be  lo-mu-ne
```
*The machine is larger than the related artifact.*

Here `pa-nu` = spatial magnitude. Same `nu-be`, different dimension. The construction doesn't care what property you measure — `nu-be` applies to any gradable quality.

### Less tired (S066)

```
lo-li-be  ta-ti-now  zo-de  nu-no  ta-ti-de
```
*The child is less tired now than yesterday.*

Now the direction flips. `nu-no` = "to a lesser degree." And the baseline isn't another entity — it's a prior time state (`ta-ti-de` = past time). Same child, different moments. Self-comparison across time.

### Stronger signal (S067)

```
lo-si  ra-vo  nu-be  lo-si-fe
```
*The signal is stronger than the threshold.*

`lo-si-fe` = signal-boundary (threshold). Comparison against a defined standard rather than another entity. The grammar doesn't distinguish "more than X" from "more than the threshold of X" — the baseline slot handles both.

### The pattern

```
lo-A  {quality}  nu-be  {baseline}   →  A has more {quality} than baseline
lo-A  {quality}  nu-no  {baseline}   →  A has less {quality} than baseline
```

The baseline can be another entity (`lo-B`), a time state (`ta-ti-de`), or a threshold (`lo-si-fe`). The construction is the same. `nu` carries the dimension; the direction marker (`be`/`no`) does the rest.

---

## Negation: five levels

Negation isn't a single operation. `no` works at five distinct scope levels, and each one produces a different meaning — even with the same words.

### Level 1 — Root prefix

`no-` directly prefixes a root to produce its absence:

| Form | Reading |
|------|---------|
| `no-de` | preservation (non-decay) |
| `no-ha` | cold (absence of heat) |
| `no-fe` | below threshold (non-boundary) |
| `no-ne-fe` | non-dependency |

These are vocabulary items. `no-ha` isn't "not hot" as a sentence — it's the *word for cold*.

### Level 2 — Action negation

`no-` prefixes a `ka`-compound to negate a directed action:

```
no-ka-ki  lo-mu
```
*Don't move the machine.*

The negation scopes over the intentional action (`ka-ki`), not over the patient. The machine still exists; the action is cancelled.

### Level 3 — Clause negation

`no` fronts an entire clause:

```
no {ka-se}
```
*Cannot be consumed.* (S036)

```
lo-si-de  no {ka-be}
```
*The signal record cannot be altered.* (S172)

Broader scope: the whole event is negated, not just the verb.

### Level 4 — Intra-clause contrast

`no` between two parallel constituents — first is actual, second is rejected:

```
lo-to-re-su  be  no  lo-wi-to
```
*Followed the doctrine, not the plan.* (S090)

```
la-mu  lo-si  se  no  lo-to
```
*The machine perceived the signal, not the pattern.* (S190)

This isn't "absence" — it's selection. "This, *not* that."

### Level 5 — Sentence-initial denial

```
no — {proposition}
```
*No. {counter-claim.}*

Flat rejection of a prior claim, optionally followed by a replacement. Used in conversation (C006 B3) and formal proceedings.

### Why it matters

The same root (`no`) at different positions produces: a vocabulary item, a cancelled action, an impossible event, a contrastive selection, and a discourse-level denial. A speaker who uses the wrong scope level says something grammatically valid but semantically different from what they intended.

---

## `se` vs `to` — perception vs established knowledge

These are the two ends of the epistemic scale, and confusing them is a category error.

- `se` — raw perception, unprocessed sensory input
- `to` — established knowledge, pattern held as certain

### In conversation (C005)

When A says `la-mi si [lo-mu zo-to]` (I hypothesize the machine has a soul), B responds:

```
la-mi  to  [lo-ze  se]
```
*I hold as established: what you experienced is raw perception.*

B uses `to` (strongest stance) to assert that A's experience is `se` (weakest category). The epistemic verb and the predicate are at opposite ends of the scale — deliberately. B is saying: "I'm certain that you have no certainty."

### In observation

```
la-mi  se  lo-si
```
*I perceive the signal.* — Reports raw sensory input. No claim about what it means.

```
la-mi  to  lo-si
```
*I hold the signal as established knowledge.* — Claims the signal has been processed, verified, integrated into a knowledge structure.

Same agent, same patient, different verb — and the commitment changes completely.

---

## `ka` vs `ki` — intentional action vs motion/change

- `ka` — intentional, directed, agent-driven action
- `ki` — change, motion, process (no intentionality required)

### The pair

```
la-li  ka-ki  lo-mu       →  The person deliberately moves the machine.
lo-mu  ki                 →  The machine is in motion. (no agent, no intent.)
```

`ka-ki` compounds them: intentional change. But `ki` alone is pure process — wind moves, water flows, signals propagate. Adding `ka` asserts that someone *chose* it.

### In compounds

| Compound | Parse | Reading |
|----------|-------|---------|
| `to-ki` | knowledge-change | the process of studying, reasoning |
| `ka-to-ki` | intentional knowledge-change | deliberate study, research |
| `ra-ki-mu` | energy-change-device | engine |
| `ka-de` | intentional decay | deliberate destruction |

`ki` is the unmarked process; `ka` marks agency. A report that says `lo-si-de ki` (the record changed) is different from `la-ze ka-ki lo-si-de` (ze deliberately altered the record). In formal proceedings, the difference matters.

---

## `la-X` vs `lo-X` — agent vs patient

The prefix is the claim.

- `la-X` — X is the agent: initiates, controls, or is structurally responsible
- `lo-X` — X is the patient: receives, undergoes, or is described

### The classic pair (S033)

```
lo-pa  ha-vo       →  The room is warm. (contingent state — warm right now)
la-pa  ha-vo       →  The room has warmth. (structural property — built to be warm)
```

Same words, different prefix, different ontological claim. `lo-pa` treats warmth as a temporary condition; `la-pa` treats it as an inherent characteristic.

### In proceedings

```
la-ze  de  lo-si-de         →  Ze suppressed the record. (ze is the agent)
lo-ze  de                   →  Ze was suppressed / degraded. (ze is the patient)
```

Swapping `la-` for `lo-` flips who did what to whom. In an arbitration hearing, this is the difference between accuser and accused.

---

## `go` vs `;` — necessary connection vs conjunction

- `go {X} Y` — X is the causal mechanism that produces Y. A necessary connection is asserted.
- `X ; Y` — X, and then Y. Connected in sequence, but no causal mechanism claimed.

### Hume's distinction

`go` is for when you're asserting that X *made* Y happen. `;` is for when two things happened and you're placing them in order without claiming one caused the other.

```
go {lo-ra-ki-mu  de}  lo-ki-pa-mu  pa-ki
```
*Because the engine failed, the ship drifted.* — Causal claim: the failure produced the drifting.

```
lo-ra-ki-mu  de ; lo-ki-pa-mu  pa-ki
```
*The engine failed; the ship drifted.* — Temporal sequence only. Maybe the failure caused the drifting. Maybe not. The speaker isn't saying.

In investigation reports, the distinction is the entire point. Using `go` is a finding; using `;` is a timeline.

---

## `to-go` vs `go` — counterfactual vs factual conditional

- `go {X} Y` — factual or prospective conditional
- `to-go {X} Y` — the premise is explicitly non-actual

### The pair

```
go {lo-ra-ki-mu  de}  lo-ki-pa-mu  pa-ki
```
*If the engine fails, the ship drifts.* — General or prospective: this could happen.

```
to-go {lo-ra-ki-mu  de  ti-de}  lo-ki-pa-mu  pa-ki  ti-de
```
*If the engine had failed, the ship would have drifted.* (S130) — Past counterfactual: it didn't happen, but if it had...

`to-go` marks the entire frame as non-actual. The `to` modifier (conceptual, pattern-level) turns the causal frame into a thought experiment. `ti-de` (past time) pins it to a specific unrealized past.

---

## Summary

| Pair | Distinction | Misuse consequence |
|------|-------------|--------------------|
| `nu-be` / `nu-no` | more vs less on a dimension | reversed comparison |
| `no-` levels 1–5 | scope of negation | different semantic operation entirely |
| `se` / `to` | perception vs certainty | wrong epistemic commitment |
| `ka` / `ki` | intentional vs processual | false attribution of agency |
| `la-` / `lo-` | agent vs patient | inverted participant role |
| `go` / `;` | causal claim vs mere sequence | unwarranted causal assertion |
| `to-go` / `go` | counterfactual vs factual | claiming non-actual events happened |
