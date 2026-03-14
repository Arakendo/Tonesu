## Observer Paradox & Identity Persistence Stress Test (S176–S181)

Formal stress test for self-reference, recursive modeling, and identity persistence through
change. Six sentences in two sub-batches:

**OPX (Observer Paradox, S176–S179):** Tests whether the ontology can describe a system
observing itself without collapsing. Progression: self-perception → self-model →
recursive self-model → self-observing feedback loop.

**IPX (Identity Persistence, S180–S181):** Tests whether identity through change can be
expressed without a new primitive. Byproduct: discovery of the `no-go` concessive frame.

---

**S176 — Self-perception** *(OPX-001-A)*

*Target: "I observe myself."*

```
Gloss:    la-mi  se  lo-mi
Literal:  agent:I  perceive  patient:I
Natural:  I observe myself. / I am self-aware at the perceptual level.
```

**Notes:**
- First self-referential patient: `mi` appears in both the agent slot (`la-mi`) and the
  patient slot (`lo-mi`). The ontology handles this without structural strain: `la-` and
  `lo-` are distinct role-markers with no prohibition on shared referents.
- Baseline for the stress test. If this collapses, the observer paradox is fatal. It
  doesn't: `la-X  se  lo-X` is a valid general pattern for reflexive perception.
- Direct parallel to Step 3 of the observer paradox framework: observer = observed.

---

**S177 — Self-model** *(OPX-001-B)*

*Target: "I know my own structure." / "I model what I am made of."*

```
Gloss:    la-mi  to  [lo-mi  su]
Literal:  agent:I  know/model  [patient:I  structure]
Natural:  I model my own constitution. / I know what I am made of.
```

**Notes:**
- Embedded inner clause `[lo-mi  su]`: state predication with self as patient,
  predicate `su` (structure/constitution). Reads: "my structure [is a fact]" / "I have
  structure." Outer: "I hold this as a model."
- `la-X  to  [lo-X  su]` = agent knows their own constitution. The self as both the
  knower and the known structure: Step 4 of the observer paradox.
- `to` + self-patient nesting is stable: the model-layer (`to`) cleanly separates
  the knowing act from the known state without collapse.

---

**S178 — Recursive self-model** *(OPX-001-C)*

*Target: "I know that I know my own structure." / Recursive self-modeling.*

```
Gloss:    la-mi  to  [la-mi  to  [lo-mi  su]]
Literal:  agent:I  know  [agent:I  know  [patient:I  structure]]
Natural:  I know that I model my own constitution.
```

**Notes:**
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

---

**S179 — Self-observing feedback loop** *(OPX-001-D)*

*Target: "Because the system perceives itself, it regulates."*

```
Gloss:    go [la-su  se  lo-su]  la-su  wi-re
Literal:  because [agent:system  perceive  patient:system]  agent:system  feedback-loop
Natural:  Because the system perceives itself, the system regulates.
```

**Notes:**
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

**S180 — Identity through repair: concessive frame** *(IPX-001-A)*

*Target: "Despite being repaired, the device [remains] one unit."*

```
Gloss:    no-go [la-mu  de-be]  lo-mu  ru
Literal:  not-cause [agent:device  repair]  patient:device  unity
Natural:  Despite the device being repaired, the device remains one.
```

**Notes:**
- **`no-go` concessive frame — first attestation.** The `no-go` compound extends the
  causal frame family via negation: `no` (absence) + `go` (cause/origin) = "the following
  event is NOT the causal origin of the matrix clause." Operational meaning: Y holds
  independently of X. This produces a concessive: *despite X, Y.*
- Causal frame family now has three members:

  | Frame | Form | Meaning |
  |-------|------|---------|
  | Factual causal | `go [X]  Y` | X causes / grounds Y |
  | Counterfactual | `to-go [X]  Y` | non-actual X would cause Y |
  | Concessive | `no-go [X]  Y` | Y holds independent of / despite X |

- `lo-mu  ru`: patientive `lo-` on the device; `ru` = unity/singularity = the device is
  still one (numerically identical, not replaced). This is the identity claim: same unit,
  post-repair.
- **IPX target:** identity through change. The identity is expressed by `ru` (it's still
  one), not by a dedicated "same" primitive. The change is expressed by `de-be` (repair,
  W035). The concessive `no-go` is the frame that decouples them: the unity is not derived
  from the repair; it persists through it.

---

**S181 — Identity through parts-replacement: Ship of Theseus** *(IPX-001-B)*

*Target: "Despite its parts changing, the device [remains] one."*

```
Gloss:    no-go [la-mu  pe  ki]  lo-mu  ru
Literal:  not-cause [agent:device  parts  change]  patient:device  unity
Natural:  Despite the device's parts changing, the device remains one.
```

**Notes:**
- **`no-go` second attestation.** Same concessive frame; escalated condition: not merely
  repaired (partial change) but having its parts themselves changed (`pe  ki` = parts +
  change/motion = constituent exchange). Ship of Theseus case.
- `la-mu  pe  ki`: the device (agent) has its parts (`pe`) undergoing change (`ki`). `pe`
  first use in this grammatical role: parts as the implicit argument of the predicate `ki`
  within an `la-X` clause. Reads: the device [such that its] parts change.
- **IPX verdict:** Identity persistence requires no new primitive. `ru` (unity/singularity)
  is sufficient for the numerical-identity claim; `no-go` handles the independence-from-change
  framing. The Ship of Theseus translates cleanly: an object's oneness is not derived from
  the stability of its parts.
- **Deeper implication:** in Tonesu's ontology, `ru` is primitive — which means unity is an
  irreducible conceptual atom. You can't decompose "being one thing" further. This is why
  identity persistence works without a "same" primitive: `ru` already IS the primitive for
  numerical identity. The stress test didn't break the primitive set; it revealed that `ru`
  was doing this work all along.

---

## Moral and Metaphysical Sample Batch (S182–S185)

No new primitives or grammar findings. These sentences arc through spiritual/philosophical
domain vocabulary to confirm that mystical language decomposes into compound claims rather
than requiring primitive expansion. Byproduct: first corpus attestation of W100 `wi-fe`.

---

**S182 — Intentional harm** *(MMP-001-A)*

*Target: "An agent intentionally destroys value toward a person." / "An agent does harm."*

```
Gloss:    la-li  ka  vo-de  lo-li
Literal:  agent:person  act  value-decay  patient:person
Natural:  A person acts to destroy another person's value.
```

**Notes:**
- `vo-de` (value-decay) as a directed action predicate: the action's character is
  value-diminishment toward the patient. Intentionality is supplied by `ka` (deliberate
  action root). Without `ka`, the same construction would be a stative description; with
  `ka` it becomes a deliberate act.
- This is what Concordian discourse produces where English produces "evil" or "harm" as
  moral primitives. No primitive gap: the concept is fully compositional.
- `ka vo-de lo-li` = "enact value-decay toward a person" — the Concordian rendering of
  "harm," "malice," or "evil action." Direction of harm is encoded in the patient slot, not
  in a dedicated harm primitive.

---

**S183 — Rule violation** *(MMP-001-B)*

*Target: "The person undermines the rule." / "The agent violates the law."*

```
Gloss:    la-li  de  lo-wi-fe-su
Literal:  agent:person  decay/undermine  patient:willed-boundary-structure
Natural:  The person undermines the rule. / The agent violates the law.
```

**Notes:**
- **`wi-fe-su` (W100 extension) first corpus attestation.** `wi-fe` = willed boundary
  (W100); `wi-fe-su` = willed-boundary-structure = rule / law as institution. `de`
  as predicate: the agent causes the rule to decay/lose force — violation without a
  dedicated "break" or "transgress" primitive.
- Distinct from physical boundary crossing (`la-li  ki  lo-fe` = the agent moves through
  a physical limit): this is specifically the normative/institutional structure.
- Concordian "sin" is `de  lo-wi-fe-su`. No sacred primitive required.

---

**S184 — Afterlife belief** *(MMP-001-C)*

*Target: "The person holds: despite the body dying, the person remains one."*

```
Gloss:    la-li  to  [no-go [lo-zo  de]  lo-li  ru]
Literal:  agent:person  know/model  [not-cause [patient:organism  decay]  patient:person  unity]
Natural:  The person believes: despite the body dying, the person persists.
```

**Notes:**
- **`no-go` in an epistemic frame over a metaphysical claim.** The concessive `no-go`
  (S180–S181) is here embedded inside a `to`-attribution: the language does not assert
  the afterlife claim; it asserts that someone *holds it as a model*. Tonesu makes no
  metaphysical commitment about whether `lo-li  ru` is true after `lo-zo  de`. The
  epistemic wrapper is the mechanism of ontological neutrality (see magic-primitive-trap
  principle, open-questions.md § Mystic).
- `lo-zo  de` inside the `no-go`-clause = organism-patient decays = biological death.
  `lo-li  ru` in the concessive matrix = the agent-patient [remains] unity.
- Structurally a direct exercise of S180's pattern in a new domain: identity persists
  despite change, now applied to biological death instead of mechanical repair.

---

**S185 — Omniscience claim** *(MMP-001-D)*

*Target: "The agent has all knowledge." / Omniscience.*

```
Gloss:    la-li  to  pu
Literal:  agent:person  know/model  totality/all
Natural:  The person has all knowledge. / The agent knows everything.
```

**Notes:**
- `pu` (plurality/collective = all, the complete set) in the proposition slot of a
  `to`-attribution: the agent's model covers the totality. First use of `pu` as the
  direct proposition of an epistemic predication.
- `pu` is primitive with no hidden metaphor — it means the complete collective, wherever
  the contextually relevant set is defined. Omniscience is a quantity claim about
  epistemic coverage: `to  pu` = knowledge [of] totality.
- Contrast: `la-to-su  pu` = organized knowledge [covers] totality — a claim about
  a knowledge-structure, not about an agent's epistemic access.

---

## Physics and Mathematics Sample Batch (S186–S189)

No new primitives. Tests map cleanly to existing roots and compounds across conservation,
measurement, symmetry, and interaction. `nu-se` (quantitative detection / measurement)
registered as W102. S189 is included as a **gap demonstration sentence**: it shows the
limit of current tools for expressing simultaneous bilateral interaction and directly
corroborates P-PR-002.

---

**S186 — Conservation** *(PMS-001-A)*

*Target: "Despite the energy moving, the energy remains unified." / Energy conservation.*

```
Gloss:    no-go [lo-ra  ki]  lo-ra  ru
Literal:  not-cause [patient:energy  motion]  patient:energy  unity
Natural:  Despite energy moving/changing form, energy remains one.
```

**Notes:**
- `no-go` applied to a physics conservation law. Same concessive pattern as S180
  (identity through repair) and S181 (Ship of Theseus), now in the energy domain:
  energy's unity is not derived from its remaining motionless; it persists through
  motion and form-change.
- `lo-ra  ki` inside the `no-go`-clause: energy-patient undergoing motion/change —
  energy changing form, position, or transmission mode.
- `lo-ra  ru` in the matrix: energy-patient [has/maintains] unity — the total quantity
  is preserved. Conservation as the persistence of `ru` (singularity of the total)
  through transformation.
- Extends the pattern observed in IPX: `ru` does not require stasis. A value can be `ru`
  (one, conserved, unified) while the specific configuration undergoes `ki` (change). This
  is the Concordian conceptual structure for all conservation laws, not just energy.

---

**S187 — Measurement** *(PMS-001-B)*

*Target: "The agent measures the energy." / Quantitative detection.*

```
Gloss:    la-li  ka  nu-se  lo-ra
Literal:  agent:person  act  quantity-perceive  patient:energy
Natural:  The person measures the energy.
```

**Notes:**
- **`nu-se` (W102) first corpus attestation.** `nu` (quantity/number) + `se`
  (perception/detection) = quantitative detection = measurement. Head-final: `se`
  (perception) is the head; `nu` specifies perception that returns a quantity rather than
  a mere qualitative signal. Registered as W102.
- `ka  nu-se` = perform the act of measuring. Without `ka`, `la-li  nu-se  lo-ra` would
  be a dispositional claim (the agent has the capacity to measure); with `ka`, it is the
  deliberate act.
- Clean compound path for all of scientific measurement: `nu-se-mu` = measuring
  instrument, `nu-se-su` = measurement system, `nu-se-ka` = the measure/result.

---

**S188 — Symmetry / invariance** *(PMS-001-C)*

*Target: "Despite the structure transforming, the structure remains one." / Symmetry.*

```
Gloss:    no-go [lo-su  ki]  lo-su  ru
Literal:  not-cause [patient:structure  change]  patient:structure  unity
Natural:  Despite the structure transforming, the structure remains one.
```

**Notes:**
- Third domain for the `no-go [lo-X  ki]  lo-X  ru` pattern (S181 was mechanical parts;
S186 was energy; S188 is abstract structure). The form has stabilised as the canonical
  expression of **invariance under transformation** — the formal concept underlying
  symmetry in physics and algebra.
- In group-theory terms: a structure is symmetric if it remains `ru` (unified, the same
  object) under a family of transformations `ki`. S188 expresses this directly.
- `lo-su  ki` = structure undergoes change. `lo-su  ru` = structure remains one. The
  concessive frame is exactly what symmetry requires: invariance despite change, not
  because change is absent.

---

## Bilateral Interaction Gap — Physics Domain (S189)

*Batch purpose: first corpus attestation of the P-PR-002 primitive-pressure gap, in the physics domain (gravitational/electromagnetic force coupling). S189 introduced the `go...ne...du...du` canonical gap structure.*

*March 2026 audit — `zi` admitted as primitive 34: see retroactive notes at S189, S193, S194 below. The three gap demonstrations are retained as historical records. All other corpus sentences examined during the audit are clean: S056 (directional giving via `ne`+`de`, unidirectional — `zi` does not apply); S083 (entering resonance STATE via `ne-ra-ki`, not a mutual transformation event — `ne-ra` / `ne-ra-ki` retained as correct); S075 (directed will-to-machine, unidirectional — `zi` does not apply); C005 (sequential epistemic turns — simultaneous mutual transformation not required). No revision needed to any sentence outside the three gap demonstrations.*

---

**S189 — Bilateral interaction gap** *(PMS-001-D)*

*Target: "Force-structure A and force-structure B act on each other."*
*Intended: simultaneous mutual transformation. Best available expression:*

```
Gloss:    go [lo-ra-su  ne  lo-ra-su]  du [lo-ra-su  ki]  du [lo-ra-su  ki]
Literal:  cause [patient:force-system  relation  patient:force-system]
          result [patient:force-system  move]  result [patient:force-system  move]
Natural:  Because force-system A is in relation with force-system B, A moves and B moves.
```

**Notes:**
- **Gap demonstration for P-PR-002.** This sentence represents the physics domain's best
  available expression of mutual interaction using current tools. It has two problems:
  (1) **Double `du` requires sequential reading**: `du [A ki]  du [B ki]` reads as A moves
  first, then B moves — but gravitational (or electromagnetic) interaction changes both
  systems simultaneously. The language has no way to mark the two outcomes as concurrent.
  (2) **`ne` captures the relation but not the transformation**: `ne` describes a static
  connection; what physics means by interaction is that A and B enter a coupled event
  that modifies both, and the `ne` relation is what enables this event — but `ne` alone
  doesn't encode the mutual transformation.
- This is the canonical corpus evidence for P-PR-002 (open-questions.md): a sentence that
  physics requires, that the language can approximate but cannot express without
  directionality distortion. Whether the frequency and variety of such sentences reaches
  the three-wrong-reading threshold remains open.
- The `go...ne...du...du` chain is grammatically well-formed and communicates the
  intended idea in context. The insufficiency is ontological, not grammatical.
- **Retroactive note (March 2026 — `zi` admitted as primitive 34):** The intended concept
  is now expressible as `lo-ra-su  zi-ra  lo-ra-su` — "force-system A and force-system B
  undergo mutual energy transformation." `zi-ra` (W104, proposed) is the compressed correct
  form. S189 is retained as the gap record showing why `zi` was needed.

---

## Temporal Event-Anchor Test (S192)

*Batch purpose: confirm the `ta  ti-[dir]  lo-[event]` event-anchored temporal construction generalizes in both directions. S092 established `ta-ti-de  lo-[event]` = "before [event]." S192 tests the mirror: `ta-ti-be  lo-[event]` = "after [event]," using a different domain (maintenance debrief vs. mission preparation) to confirm the pattern is not context-specific.*

---

**S192 — Maintenance debrief held after field inspection**

*Target: "The team debriefed after the inspection."*

*Concordian framing: standard post-event knowledge consolidation. The inspection is the reference event; the debrief happens in the temporal interval following it.*

```
Gloss:    la-yu  lo-to-su  be  ta-ti-be  lo-se-ka
Literal:  agent:group  patient:organized-knowledge  grew/consolidated  time:after  patient:examination
Natural:  The team consolidated their knowledge after the inspection.
```

**Notes:**
- **Mirror of S092's event-anchor construction.** S092: `ta-ti-de  lo-ka-wi-de` = "before the mission departure" (`ti-de` = past/prior → before). S192: `ta-ti-be  lo-se-ka` = "after the inspection" (`ti-be` = future/following → after). Both use `ta  ti-[dir]  lo-[event]` with a `lo-`-marked event as the temporal anchor. Different domain (mission preparation vs. maintenance/inspection cycle), different directional compound (`ti-de` vs `ti-be`).
- **`ta-ti-de  lo-X` = before X; `ta-ti-be  lo-X` = after X.** The directional component of the time compound (`de` = decay/prior, `be` = growth/following) sets the relative position; the `lo-[event]` bracket provides the anchor event. The structure is compositionally transparent: "at the [prior/following] time [of] [event]."
- **`be` as matrix predicate:** `lo-to-su  be` = "knowledge grows" = they consolidated their knowledge. The group's organized understanding expanded as a result of the inspection. Same `be` as all growth predicates.
- **`se-ka`** (W034, perceptual-agent/examination process) used as the anchor event. The inspection is the event they are temporalizing against. `lo-se-ka` = patient:inspection — the examination in its nominal role as a temporal anchor.
- The two examples together confirm the pair: `ta-ti-de  lo-X` / `ta-ti-be  lo-X` = before-X / after-X. The construction is general: any `lo-[event]` noun phrase can serve as the anchor.

**Verdict S192: clean.** `ta-ti-be  lo-[event]` = "after [event]" works identically to S092's `ta-ti-de  lo-[event]` = "before [event]." Event-anchor temporal construction confirmed as a general pattern. Ready to add rule to grammar.md.

---

## Bilateral Interaction Gap — Biology Domain (S193)

*Batch purpose: provide second corpus attestation of the P-PR-002 primitive-pressure gap, in the biological domain. S189 demonstrated the gap in physics (gravitational/force coupling between `lo-ra-su` force-systems). S193 tests the same structural failure in biological mutualism — whether the language can express simultaneous coupled growth without forcing a sequential causal reading.*

---

**S193 — Mutualistic symbiosis: coupled organisms each cause the other to grow**

*Target: "The two organisms each nourish the other."*

*Concordian framing: a lichen-type mutualism — the photosynthesizing organism and the structural organism each supply what the other cannot produce alone. The exchange is simultaneous and ongoing; neither party is the "cause" whose effect is the other's growth. The coupling is the event.*

```
Gloss:    go [lo-zo-su  ne  lo-zo-su]  du [lo-zo-su  be]  du [lo-zo-su  be]
Literal:  cause [patient:living-system  relation  patient:living-system]
          result [patient:living-system  grow]  result [patient:living-system  grow]
Natural:  Because living-system A is in relation with living-system B, A grows and B grows.
```

**Notes:**
- **Second corpus attestation for P-PR-002.** S189 demonstrated the gap in physics (`lo-ra-su  ne  lo-ra-su`, force-systems). S193 repeats the same construction in biology (`lo-zo-su  ne  lo-zo-su`, living-systems in mutualistic coupling). Two domain-distinct sentences, same structural failure.
- **`zo-su`** = living-system / organized organism. Compositional parallel to `ra-su` (force-system, used in S189): `zo` (living thing) + `su` (organized structure) = organism understood as an organized biological system. Not separately registered; compositionally transparent.
- **The gap is identical to S189:** (1) Double `du` forces sequential reading — living-system A grows first, then living-system B — but mutualistic symbiosis is a continuous coupled exchange with no sequencing between the two growth events. (2) `ne` describes the static relation enabling the coupling; it does not encode the mutual-transformation event itself. The language approximates the outcome (both grow because they are in relation) but cannot say the coupling *is* the event in which both transform simultaneously.
- **Why `go...ne...du...du` is the best available:** A single `du` frame cannot take two agent-predicate pairs without coordinate structure. Using `ne` as inner coordinator (`du [lo-zo-su  be  ne  lo-zo-su  be]`) would read `ne` as a static copula between two growth-states, not as simultaneous mutual growth. The double-`du` chain is the least-distorting approximation available.
- **Biology removes the physics-abstraction objection.** One might argue that physical simultaneity is a limiting edge case that natural language need not cover. Mutualistic symbiosis is a macroscopic, everyday-scale fact about organisms. If the language cannot express it without sequentiality distortion, the gap is not domain-specific.
- The `go...ne...du...du` chain is grammatically well-formed. The insufficiency is ontological, not grammatical — the same conclusion as S189.
- **Retroactive note (March 2026 — `zi` admitted as primitive 34):** The intended concept is now expressible as `lo-zo-su  zi-zo  lo-zo-su` — "living-system A and living-system B undergo mutual biological transformation." `zi-zo` (W106, proposed) is the compressed correct form. S193 is retained as the gap record.

**Verdict S193: gap confirmed (2/3).** The P-PR-002 simultaneous-mutual-transformation gap is present in both physics (S189) and biology (S193). One further domain-varied wrong-reading is needed to reach the three-attestation threshold. Social domain (negotiation / mutual exchange) is the remaining candidate.

---

## Bilateral Interaction Gap — Social Domain (S194)

*Batch purpose: provide third corpus attestation of the P-PR-002 primitive-pressure gap, in the social domain. S189 demonstrated the gap in physics (force-system coupling); S193 demonstrated it in biology (mutualistic symbiosis). S194 tests the same structural failure in negotiation — whether the language can express simultaneous coupled revision of intentional stance without forcing a sequential causal reading. This is the three-attestation threshold.*

*Test procedure applied: full primitive-pressure test per revised protocol — three decompositions attempted, repair test applied, wrong-reading classification explicit.*

---

**S194 — Trade negotiation: both delegates revise their terms at the exchange moment**

*Target: "Each delegate revised their terms in response to the other."*

*Concordian framing: a formal trade negotiation exchange moment. Both parties enter with an established intentional-stance (`wi-to`) — their current position on terms. The exchange event couples them: both stances shift simultaneously at the moment of engagement. Neither party's revision precedes the other's; neither is the unilateral cause of the other's change. The coupled encounter is the event; both revised stances are its simultaneous results.*

```
Gloss:    go [la-li  ne  la-li]  du [la-li  wi-to-ki]  du [la-li  wi-to-ki]
Literal:  cause [agent:person  relation  agent:person]
          result [agent:person  stance-shifts]  result [agent:person  stance-shifts]
Natural:  Because delegate A is in relation with delegate B, A shifts position and B shifts position.
```

**Notes:**
- **Third corpus attestation for P-PR-002.** S189: physics/force-systems. S193: biology/mutualistic symbiosis. S194: social/negotiation. Three-wrong-reading threshold is reached.
- **`wi-to-ki`:** `wi` (intention) + `to` (conceptual pattern) + `ki` (inchoative) = entering a new intentional-conceptual configuration = revising one's stance. Head-final: the change-event (`ki`) in the domain of intentional-pattern (`wi-to`). Compositionally transparent; no registration needed for the test.
- **Wrong reading (primary decomposition):** Double `du` forces sequencing — delegate A revises first, then delegate B revises. But negotiation revision is a coupled simultaneous exchange: both parties update their positions *at the exchange moment*, which is a single event, not two sequential ones. The language has no way to mark the two outcomes as concurrent.
- **Alternative decompositions tested:**
  - *Two causal chains* (`go [la-li wi-to] du [la-li wi-to-ki]. go [la-li wi-to] du [la-li wi-to-ki].`): Loses the coupling entirely. Two independent internal revisions; the mutual-response is gone. Wrong reading: one event becomes two separate events.
  - *Relational + causal hybrid* (`la-li  ne  la-li  go  wi-to-ki`): Which party changes? Both changing is lost. Wrong reading: mutual change becomes undifferentiated one-way causation from the relation.
  - *`ne` between shift-events* (`du [la-li  wi-to-ki  ne  la-li  wi-to-ki]`): `ne` between two events reads as a static relation between two change-states, not as the assertion of their simultaneity. Wrong reading: interaction becomes static relation at the event-result level.
- **Repair test:** `ne-ki` (relation-change) = the relation itself shifts — not both parties. `wi-to-ne` = a static shared-stance state, not the dynamic revision event. No compound of existing primitives asserts "these two events are simultaneous and mutually constitutive" without that compound being exactly the new concept needed. Repair fails.
- **The social domain removes the natural-law objection.** Physics and biology involve simultaneous coupling as a matter of natural law (field interactions, metabolic mutualism). Negotiation is chosen, deliberate, one of the paradigm cases of intentional mutual transformation. If the gap persists here, it is not an edge case of physics formalisms — it is a structural gap in the language's treatment of coupled events generally.
- Same `go...ne...du...du` canonical structure as S189 and S193; results are directly comparable. The wrong reading is the same in all three domains.
- **Retroactive note (March 2026 — `zi` admitted as primitive 34):** The intended concept is now expressible as `la-li  zi-ka  lo-li` — "the delegates engage in mutual exchange / transaction." `zi-ka` (W105, proposed) is the compressed correct form. S194 is retained as the gap record showing why `zi` was needed.

**Verdict S194: gap confirmed (3/3). Three-attestation threshold reached.** The P-PR-002 simultaneous-mutual-transformation gap is persistent across physics, biology, and social domains. All alternative decompositions fail. Repair by compounding fails. A primitive slot evaluation is now triggered. See open-questions.md for the updated entry.

---

## Bilateral Interaction Gap — Biology Domain (S193)

*Batch purpose: provide second corpus attestation of `ko` with a clausal complement (first: C005 A2), using a different container type (archive vs. doctrine), in order to confirm the extension is systematic and enable formalization of the rule in spec/grammar.md § Containment Predicates.*

---

**S191 — Archive record: observation logged as propositional entry**

*Target: "The archive holds that the pilot perceived the field."*

*Concordian framing: log entries in a `si-su` (signal-archive) are propositions, not physical objects. The archive contains the report of an event, not the event itself. This is the institutional record-keeping sentence: the pilot's observation has been entered into the archive as a propositional fact.*

```
Gloss:    la-si-su  ko  [la-ra-ki-li  se  lo-pa-ra]
Literal:  agent:archive  contains  [agent:pilot  perceived  patient:field]
Natural:  The archive holds: the pilot perceived the field.
```

**Notes:**
- **Second corpus attestation of `ko` with a clausal complement.** First: C005 A2 (`la-to-re-su  ko  [lo-mu  zo-to]` — doctrine contains propositional belief). Here: `la-si-su  ko  [la-ra-ki-li  se  lo-pa-ra]` — archive contains propositional observation record. Different container type (`si-su` archive vs. `to-re-su` doctrine), different propositional content (perceptual report vs. doctrinal claim), parallel grammatical structure.
- The bracketed clause `[la-ra-ki-li  se  lo-pa-ra]` is a full propositional complement: agent (`la-ra-ki-li`), predicate (`se`), patient (`lo-pa-ra`). The archive contains this proposition as an entry — not the pilot, not the field, but the propositional record of the perception event.
- **Container semantics confirm the extension principle:** `ko` asserts a containment relation between a container and its contents. The container type determines what register of contents makes sense:
  - Physical container (`ko-mu`) → physical objects
  - Archive (`si-su`) → records and logged propositions
  - Doctrine (`to-re-su`) → doctrinal claims
  In all three cases, `ko` is the same structural predicate. No special form is needed for propositional complements.
- `la-si-su  ko  lo-si-mu` (S070) was the nominal-patient form for the same archive. That sentence says "the archive holds records" (a type of nominal contents). This sentence says "the archive holds that X happened" (a specific propositional entry). The nominal form describes the archive's character; the propositional form reports a specific log entry. Both are valid.
- With two domain-varied attestations (C005 A2, S191), the `ko`-clausal complement pattern is ready to formalize.

**Verdict S191: clean.** `la-si-su  ko  [embedded-prop]` follows the same `la-X  ko  Y` pattern with full clause as Y. No strain. Generalizes from doctrine to archive. Rule may now be written.

---

## No Contrast Coordinator Test (S190)

*Batch purpose: provide second corpus attestation of `no` as an intra-clause contrast coordinator (first: S090) using a different predicate and domain, enabling formalization of the pattern in spec/grammar.md § Negation.*

---

**S190 — Machine perception ceiling: signal detected, not pattern**

*Target: "The machine detected the signal, not the conceptual pattern."*

*Concordian framing: machines have perceptual capacity (`se`) but their output is signal-level (`si`), not pattern-level (`to`). This sentence makes that epistemic ceiling explicit compositionally.*

```
Gloss:    la-mu  lo-si  se  no  lo-to
Literal:  agent:machine  patient:signal  perceived  contrast-not  patient:conceptual-pattern
Natural:  The machine detected the signal, not the pattern.
```

**Notes:**
- **Second corpus attestation of `no` as intra-clause contrast coordinator.** First use: S090 (`lo-to-re-su  be  no  lo-wi-to` = "followed the doctrine, not the plan"). Here: `lo-si  se  no  lo-to` = "perceived the signal, not the pattern." Different predicate (`se` vs `be`), different domain (machine perception vs. mission instruction), parallel structure (patient contrast in both).
- `no` in the contrast coordinator position negates only the following constituent (`lo-to`), not the predicate. The machine did perceive; what it perceived was `lo-si`, not `lo-to`. The predicate `se` is unaffected.
- **Patient contrast:** `lo-si` (raw signal / signal data) vs. `lo-to` (conceptual pattern). In the Concordian epistemic hierarchy, machines register signal-level data (`si`); only persons or sufficiently organized systems extract conceptual patterns (`to`). This sentence embodies that ceiling not as a doctrinal statement but as a bare perceptual report.
- **Bare `se` (no epistemic frame):** The machine's perception is reported without an outer `la-mu  se  [prop]` frame. That frame would attribute a personal epistemic stance to the machine, which doesn't apply. Inanimate agents simply perceive; they don't hold epistemic positions. Verb as bare predicate; machine as grammatical agent.
- With two attestations (S090, S190), the `no` contrast coordinator is ready to formalize. Structure confirmed: `[established constituent]  no  [rejected alternative]`, with both constituents grammatically parallel (`lo-` patients in both cases so far).

**Verdict S190: clean.** `no` as contrast coordinator between parallel `lo-` patients is stable with `se` predicate. Generalizes beyond `be`. Ready to add as Level 4 in § Negation.
