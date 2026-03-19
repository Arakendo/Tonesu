# Production Pathways

How does a Tonesu speaker get from a raw experience to a finished utterance? This page traces the cognitive path — from perception to expression — showing how the grammar reflects the stages of processing.

---

## The epistemic pipeline

Tonesu's verb system maps directly onto stages of knowledge processing. A speaker moves through these stages in order, and the grammar marks where they are in the pipeline:

```
se  →  si  →  to  →  ka-si / ka-to
perception → hypothesis → established knowledge → transmission
```

### Stage 1: `se` — raw perception

```
la-mi  se  lo-si
```
*I perceive the signal.*

No interpretation, no judgment. The speaker reports sensory contact. This is the floor — the minimum epistemic commitment available. You can't say less and still be saying something.

### Stage 2: `si` — hypothesis

```
la-mi  si  [lo-si  ne-ra  nu-be  lo-si-fe]
```
*I hypothesize: the signal's resonance exceeds the threshold.*

The speaker has processed the raw perception into a structured claim — but isn't committed to it. `si` says: "I've thought about what I perceived, and here's a pattern I see, but I'm not willing to stake my certainty on it."

### Stage 3: `to` — established knowledge

```
la-mi  to  [lo-si  ne-ra  nu-be  lo-si-fe]
```
*I hold as established: the signal's resonance exceeds the threshold.*

Same proposition, different verb. The speaker has crossed the epistemic threshold — the claim is now part of their certified knowledge. Using `to` is a commitment: if the claim proves wrong, the speaker's epistemic record takes the hit.

### Stage 4: `ka-si` / `ka-to` — transmission

```
la-mi  ka-si  lo-si  lo-to-fe-su
```
*I transmit the signal to the standards body.*

The knowledge moves outward. `ka-si` = intentional signal transmission. The speaker has processed, evaluated, committed, and now acts — publishing, testifying, reporting.

### The pipeline as design philosophy

The stages aren't arbitrary. They mirror the actual pathway from stimulus to action:

1. Something arrives at the senses (`se`)
2. The mind forms a tentative model (`si`)
3. The model crosses a threshold of confidence (`to`)
4. The agent acts on the knowledge (`ka-si` / `ka-to`)

Every sentence in the language sits *somewhere* on this pipeline. The grammar forces the speaker to declare where.

---

## Building an utterance: concept to sentence

### Step 1 — Identify the participants

Who or what is involved? Assign roles:

- **Agent** (`la-X`): who initiates, controls, or is responsible
- **Patient** (`lo-X`): what is affected, described, or undergoes
- **Beneficiary/Result** (`lu-X`): who receives the outcome

```
Agent: the pilot (ra-ki-li)
Patient: the signal record (si-de)
```

### Step 2 — Choose the verb structure

What is happening? Is it:

- A state? → property predicate: `lo-X ne Y` or `lo-X Y`
- An action? → `ka-` compound: `la-X ka-Y lo-Z`
- A process? → bare `ki`-compound: `lo-X ki`
- An epistemic claim? → `se/si/to` frame: `la-X to [proposition]`

```
Action: suppressed → ka-de (intentional decay)
```

### Step 3 — Frame the assertion

What epistemic level? Are you:

- Reporting a perception? → `la-mi se [...]`
- Offering a hypothesis? → `la-mi si [...]`
- Making a certified claim? → `la-mi to [...]`
- Making a bare statement? → no epistemic frame

```
Certified claim:
la-mi  to  [la-ra-ki-li  ka-de  lo-si-de]
```
*I hold as established: the pilot suppressed the record.*

### Step 4 — Add modifiers and frames

Does the sentence need:

- **Time?** → `ta-ti-de` (past), `ta-ti-now` (present), `ta-ti-be` (near future)
- **Purpose?** → `wi [clause]`
- **Cause?** → `go {premise} result`
- **Comparison?** → `nu-be` / `nu-no` + baseline
- **Negation?** → `no` at the appropriate scope level
- **Counterfactual?** → `to-go {premise} result`
- **Evidential hedge?** → `()` wrap

```
With past time:
la-mi  to  [la-ra-ki-li  ka-de  lo-si-de  ta-ti-de]
```
*I hold as established: the pilot suppressed the record [in the past].*

### Step 5 — Check the parse

Read the compound right-to-left to verify the head:

- `ra-ki-li` → right-branching: `ra` modifies [`ki-li`] → energy-change person → pilot ✓
- `si-de` → `si` modifies `de` → signal-record ✓
- `ka-de` → `ka` modifies `de` → intentional decay → suppression ✓

If the parse doesn't match intent, restructure with `'` or split into multi-word phrasing.

---

## Worked example: from observation to report

A pilot notices something wrong with engine output, forms a hypothesis, confirms it, and reports to the standards body.

### Perception

```
la-mi  se  lo-si
```
*I perceive the signal.*

Raw input. The pilot sees a reading on the instrument but makes no claim about it.

### Hypothesis

```
la-mi  si  [lo-ra-ki-mu  de]
```
*I hypothesize: the engine is degrading.*

The pilot interprets the signal. `si` marks this as a tentative claim — "this is what I think I'm seeing."

### Verification

```
la-mi  to  [lo-ra-ki-mu  de  ta-ti-now]
```
*I hold as established: the engine is degrading now.*

After further observation, the pilot commits. `to` is a higher-stakes verb than `si` — the pilot is certifying this is real.

### Counterfactual reasoning

```
to-go {lo-ra-ki-mu  de}  lo-ki-pa-mu  pa-ki
```
*If the engine fails, the ship will drift.*

The pilot projects forward into non-actual space. `to-go` marks the entire frame as hypothetical — the engine hasn't failed yet, but this is what follows if it does.

### Report

```
la-mi  ka-si  lo-si-de  lo-to-fe-su
```
*I transmit the signal record to the standards body.*

The knowledge reaches the institution. The pipeline completes: `se` → `si` → `to` → `ka-si`.

### Institutional response

```
la-to-fe-su  to  [lo-ra-ki-mu  de]  —  la-to-fe-su  ka-si  lo-to-re-su
```
*The standards body holds as established: the engine is degrading. — The standards body transmits this to the doctrine system.*

The institution processes the report through its own pipeline and publishes to the permanent record. The pilot's personal epistemic journey becomes institutional knowledge.

---

## The causal frame: `go`

When the *mechanism* matters — not just "A, then B" but "A *caused* B" — the causal frame `go` structures the claim:

```
go {lo-ra-ki-mu  de}  lo-ki-pa-mu  pa-ki
```
*Because the engine failed, the ship drifted.*

The premise goes inside `go {}`; the result follows. The frame asserts a necessary connection — this isn't coincidence, this is causation.

### Causal vs sequential

Compare with `;` (sequential connector):

```
lo-ra-ki-mu  de ; lo-ki-pa-mu  pa-ki
```
*The engine failed; the ship drifted.*

Same events, different claim. `;` places them in temporal order. `go` asserts one *produced* the other. A speaker choosing between them is choosing whether to assert a mechanism or just a timeline.

---

## The purpose frame: `wi`

When an action is *aimed at* an outcome, `wi` frames the goal:

```
la-yu  ka-to-ki  wi [ka-to-su-ki]
```
*They study in order to comprehend.* (S018)

- `ka-to-ki` = intentional knowledge-change (studying)
- `wi [ka-to-su-ki]` = purpose: to enter the state of organized knowledge (comprehension)

The distinction between `to-ki` (the ongoing activity of reasoning) and `to-su-ki` (the threshold moment of comprehension) is visible in the compound structure. The `wi` frame connects the process to its intended crossing point.

---

## Summary: speaker choices at each stage

| Stage | Grammar | What it commits the speaker to |
|-------|---------|-------------------------------|
| Perception | `se` | Sensory contact — nothing more |
| Hypothesis | `si` | A tentative pattern — retractable |
| Established | `to` | Certified knowledge — speaker's reputation at stake |
| Transmission | `ka-si` | The claim moves to others — institutional consequences |
| Cause | `go {X} Y` | X produced Y — mechanism asserted |
| Sequence | `X ; Y` | X then Y — no mechanism claimed |
| Counterfactual | `to-go {X} Y` | Non-actual: if X had held, Y would follow |
| Purpose | `wi [Y]` | Action is directed toward outcome Y |
| Report | `()` wrap | Content is unattributed — carried, not asserted |

Every one of these is a choice with consequences. The grammar doesn't just describe what happened — it records what the speaker is willing to claim about it.
