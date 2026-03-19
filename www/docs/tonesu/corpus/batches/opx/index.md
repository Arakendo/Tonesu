---
title: "Operator Extension Test"
---

# Operator Extension Test

*Theme: [Grammar & syntax](../../grammar/)* · 4 sentences.

[← Grammar & syntax](../../grammar/) · [← Corpus](../../index.md)

---

## OPX-001 · Operator Extension

<span id="S176"></span>
**S176**
`la-mi  se  lo-mi`
*I observe myself. / I am self-aware at the perceptual level.*

!!! annotation "Notes"
    - First self-referential patient: `mi` appears in both the agent slot (`la-mi`) and the
      patient slot (`lo-mi`). The ontology handles this without structural strain: `la-` and
      `lo-` are distinct role-markers with no prohibition on shared referents.
    - Baseline for the stress test. If this collapses, the observer paradox is fatal. It
      doesn't: `la-X  se  lo-X` is a valid general pattern for reflexive perception.
    - Direct parallel to Step 3 of the observer paradox framework: observer = observed.

<span id="S177"></span>
**S177**
`la-mi  to  [lo-mi  su]`
*I model my own constitution. / I know what I am made of.*

!!! annotation "Notes"
    - Embedded inner clause `[lo-mi  su]`: state predication with self as patient,
      predicate `su` (structure/constitution). Reads: "my structure [is a fact]" / "I have
      structure." Outer: "I hold this as a model."
    - `la-X  to  [lo-X  su]` = agent knows their own constitution. The self as both the
      knower and the known structure: Step 4 of the observer paradox.
    - `to` + self-patient nesting is stable: the model-layer (`to`) cleanly separates
      the knowing act from the known state without collapse.

<span id="S178"></span>
**S178**
`la-mi  to  [la-mi  to  [lo-mi  su]]`
*I know that I model my own constitution.*

!!! annotation "Notes"
    - **Three-level nesting** — deepest in the corpus. Previous deepest: S175 (two levels,
      different agents). S178 is two levels with the same agent at both outer levels, self as
      patient at the innermost.
    - Each `la-mi` cleanly re-anchors a new clause level. Boundary rule holds: the inner
      `la-mi` (matrix-level marker) terminates the middle embedding; the inner-inner `lo-mi`
      anchors the innermost state predication. No ambiguity: `la-` always opens, `lo-` anchors
      the referent in the patient position.
    - This is the structural "observer paradox" maximally activated: the knowing agent, the
      known-agent, and the known-structure all refer to the same entity at three different
      clause levels. The separation of `to` (model layer) from `se` (perception layer) from
      `su` (structure) is what prevents the levels from collapsing into each other.
    - **Step 5 verdict:** Tonesu handles recursive self-modeling stably. The predication
      strategy (role-markers provide structural slots independent of referent identity) means
      self-reference is always explicitly framed rather than implicitly looped.

<span id="S179"></span>
**S179**
`go [la-su  se  lo-su]  la-su  wi-re`
*Because the system perceives itself, the system regulates.*

!!! annotation "Notes"
    - **`wi-re` first corpus attestation** (W099). Used here as a predicate directly:
      `la-su  wi-re` = the system [instantiates/performs] feedback regulation. W099 status
      upgrades from proposed → active with this use.
    - `la-su  se  lo-su`: the same pattern as S176 (`la-mi  se  lo-mi`) applied to a system
      entity. `su` as both agent and patient — the system perceives itself. The `go`-clause
      makes this the *cause*; the matrix makes regulation the *result*.
    - **Step 6 complete:** perception (`se`) → model (implicit in `to`-chain, not restated)
      → feedback regulation (`wi-re`). The `go`-clause encodes the dependency: self-perception
      drives self-regulation. The loop is described as a causal chain, not as a primitive new
      concept.
    - **OPX verdict:** No new primitives required. Self-reference, recursive nesting, and
      causal self-observation all compose from existing structures. The key insurance is the
      three-layer separation: `se` (perception), `to` (model), `wi` (goal) — each is
      orthogonal to the others, which is exactly why they don't collapse under self-reference.

---

*Generated from [`registry/entries.yaml`](https://github.com/Arakendo/Tonesu/blob/main/registry/entries.yaml).*