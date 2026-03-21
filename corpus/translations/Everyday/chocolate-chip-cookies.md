---
batch_codes: [CKG-001]
---
# Translation Test: Chocolate Chip Cookie Recipe

## Source: Standard chocolate chip cookie recipe (generic public-domain procedural form)
## Status: First pass — 6-step founding set

---

## Purpose

A cookie recipe is a procedural text: a sequence of physical actions, each
specifying materials, a container, a thermal or mechanical transformation,
and a terminal state. As a translation target, it tests Tonesu's ability
to handle the **instruction register**, **material-state vocabulary**, and
**agent-dropped imperatives** — domains the corpus has not exercised before.

Primary tests:

- **Instruction register (agent-dropped imperative):** Recipe instructions
  do not name an agent. In Tonesu, this tests whether the `la-` marker can
  be dropped when the agent is the immediate addressee — and whether the
  resulting bare verb-compound reads naturally as a command rather than a
  description.
- **Material state vocabulary:** Cooking divides ingredients by phase state:
  wet (liquid phase) vs. dry (solid/powder phase). Tonesu has `ki'ma` (W114,
  liquid) and `su'ma` (W113, solid state of matter). This batch tests whether
  those existing primitives cover the wet/dry ingredient distinction at
  recipe-instruction scale.
- **Double `lo-` patient with `ne` coordinator:** Combining two ingredient
  classes in one instruction requires encoding two simultaneous patients.
  This batch tests `lo-X ne lo-Y` as a joint-patient construction — the
  first in the corpus.
- **Artifact agency:** The oven (`ko-ha-mu`, W214) acts as the causal agent
  of thermal change in the baking step. This tests whether `la-ko-ha-mu`
  (artifact as agent) reads as a coherent Tonesu sentence.
- **Phase-change tracking:** The batch distinguishes `zo-ra-ma-su` (structured
  food mixture = dough, pre-thermal) from `ha-zo-ra-ma` (W216, thermally-treated
  food = baked good, post-thermal). The state change of the material is
  encoded in the compounding, not in a verb tense.

Secondary tests:

- Sequential connector `;` in procedural chaining (S663).
- `su-ne` (W174, harmony) and `be-su` (completion) as procedural goal-states.
- `lu-` result-frame marking the target state of a mixing or baking action.

Corpus sentences: S659–S664

---

## Vocabulary Framework

Three new compounds coined for this batch:

| W# | Form | Written | Reading | Notes |
|----|------|---------|---------|-------|
| W214 | `ko-ha-mu` | `kohamu` | oven / thermal containment device | `ko` (containment) + `ha` (heat) + `mu` (device). The device defined by containing heat for cooking. Right-branch: `ko-[ha-mu]` = containment-[heat-device]. |
| W215 | `ma-ne-ki` | `maneki` | mix / combine | `ma` (matter) + `ne` (relation) + `ki` (motion). The motion that brings matter into relational unity. Right-branch: `ma-[ne-ki]` = matter-[relational-motion] = the action of relating matter through physical motion. Covers mixing, folding, combining, blending. |
| W216 | `ha-zo-ra-ma` | `hazorama` | baked food / thermally-treated food | `ha` (heat) + `zo-ra-ma` (food, W144). Right-branch: `ha-[zo-ra-ma]` = thermal-[food] = food that has undergone the thermal transformation = any baked or cooked food. Distinct from `zo-ra-ma` (food, general); carries the `ha-` marker that encodes the transformative heat step. |

**Matter-state vocabulary in this batch (composable, no new W-entries):**

| Form | Written | Reading | Source |
|------|---------|---------|--------|
| `ki'ma-zo-ra-ma` | `ki'mazorama` | liquid food materials (wet ingredients) | W114 + W144 |
| `su'ma-zo-ra-ma` | `su'mazorama` | solid/powdered food materials (dry ingredients) | W113 + W144 |
| `zo-ra-ma-su` | `zoramasu` | structured food mixture (dough) | W144 + `su` (primitive) |
| `ha-su` | `hasu` | thermally set / heat-structured state | `ha` + `su` (both primitives) |
| `de-ha-ki` | `dehaki` | cooling / thermal decrease action | `de` + `ha` + `ki` (all primitives) |
| `be-su` | `besu` | completed formation / done | `be` + `su` (both primitives) |

**Structural note — `zo-ra-ma-su`:** Read as `zo-ra-ma` (food, W144) + `su`
(structure, primitive) = structured food material = the mixed dough before
baking. The `su` suffix here marks the formation into a unified material mass
(the output of mixing = the structured substrate ready for thermal treatment).

**Structural note — `no-ne-ko-mu`:** A composable modifier for "separate vessel":
`no` (negation) + `ne` (relation) + `ko-mu` (W052, vessel). The unrelated /
unconnected vessel = the second bowl. First use in S661.

---

## Source Text

> **Standard chocolate chip cookie recipe (generic procedural form)**
>
> 1. Preheat the oven to 190°C (375°F).
> 2. In a bowl, mix the liquid ingredients (butter, eggs, vanilla) until creamy.
> 3. In a separate bowl, combine the dry ingredients (flour, sugar, salt, leavening).
> 4. Combine the wet and dry ingredients together and mix until unified.
> 5. Place portions of the dough on a baking surface in the oven; bake until set.
> 6. Remove the baked goods from the oven; cool; the cookies are complete.

---

## Step-by-Step Analysis

---

### S659 — CKG-001-A: Preheat the oven.

```
ha-ki  lo-ko-ha-mu
```

**Written:** `haki lokohamu`

**Natural reading:** Heat-change the containment-heat-device.

**Notes:** Opening instruction. Bare-verb imperative: no `la-` agent; the cook is
the immediate addressee. `ha-ki` = thermally change = heat up; composable from
`ha` (thermal state root) + `ki` (motion/change). `ko-ha-mu` (W214) first
attestation. The instruction register in Tonesu drops the agent marker when the
agent is the unambiguous immediate addressee — identical to the imperative drop
in many natural languages. Temperature specification would add `lu-ha-nu-[value]`
(result: heat-quantity-[level]); omitted here for procedural-register clarity.

---

### S660 — CKG-001-B: Mix the liquid food-materials in the vessel until structurally unified.

```
ma-ne-ki  lo-ki'ma-zo-ra-ma  pa-ko-mu  lu-su-ne
```

**Written:** `maneki loki'mazorama pakomu lusune`

**Natural reading:** Combine the liquid food-materials in the vessel, result: structural harmony.

**Notes:** W215 (`ma-ne-ki`) first attestation. `ki'ma-zo-ra-ma` = liquid food
material (W114 + W144) = the wet ingredients (butter, eggs, vanilla extract).
`pa-ko-mu` = in/at the vessel = in the bowl. `lu-su-ne` = result: structural
harmony (W174) = until the mixture is harmoniously unified (well-combined,
emulsified, creamy). The `lu-` result frame marks the target state of the
instruction: the cook is not just told to mix, but told what the successful
end-state looks like. `su-ne` (W174, harmony = structure-of-relation) earns
its meaning here: the butter-and-egg mixture reaches harmony when the components
are structurally integrated, not merely stirred together.

---

### S661 — CKG-001-C: In a separate vessel, combine the solid food-materials.

```
pa-no-ne-ko-mu  ma-ne-ki  lo-su'ma-zo-ra-ma
```

**Written:** `panonekomu maneki losu'mazorama`

**Natural reading:** At the unrelated vessel, combine the solid food-materials.

**Notes:** `no-ne-ko-mu` = un-relation-vessel = a vessel with no bond to the previous
one = a separate bowl. `pa-no-ne-ko-mu` sentence-initially marks the new location;
the topic shift from bowl-one to bowl-two is encoded in placement, not in a new
clause. `su'ma-zo-ra-ma` = solid-matter food = the dry ingredients (flour, sugar,
salt, baking soda/powder). `su'ma` (W113 = solid state of matter) + `zo-ra-ma`
(W144 = food); the juncture `'` marks it as a pre-bound subcompound: `[su'ma]-zo-ra-ma`
= solid-state-[food material] = the food materials in solid/powdered phase.

---

### S662 — CKG-001-D: Combine the wet ingredients with the dry ingredients.

```
ma-ne-ki  lo-ki'ma-zo-ra-ma  ne  lo-su'ma-zo-ra-ma
```

**Written:** `maneki loki'mazorama ne losu'mazorama`

**Natural reading:** Combine [liquid food materials] bonded-with [solid food materials].

**Notes:** **First double-patient construction in the corpus.** Two `lo-` patients
joined by `ne` (relational particle): `lo-X ne lo-Y` = patient X bonded-to patient Y
= X and Y jointly as the patient of the combining action. The `ne` between the two
`lo-NPs` marks them as jointly constituting the input — mixing is not done to X
and separately to Y, but to X-together-with-Y as a bonded pair. Compositionally:
`ma-ne-ki` (combine) requires two inputs that become one; `ne` between the patients
is semantically motivated (the `ne` in `ma-ne-ki` anticipates the `ne` that joins
its inputs). The cook folds the dry ingredients into the wet until unified.

---

### S663 — CKG-001-E: Place the dough in the oven; the oven bakes it until set.

```
ki  lo-zo-ra-ma-su  pa-ko-ha-mu ;  la-ko-ha-mu  ha-ki  lo-zo-ra-ma-su  lu-ha-su
```

**Written:** `ki lozoramasu pakohamu ; lakohamu haki lozoramasu luhasu`

**Natural reading:** Move the structured food-matter to the oven; the oven heat-changes
the structured food-matter, result: thermally set.

**Notes:** Two-clause sequential (`;`). Clause 1: bare imperative — place the dough
(`zo-ra-ma-su` = structured food material = the mixed dough, formed into the
structured mass ready for baking) in the oven. Clause 2: **first artifact-as-agent
construction in this batch** — `la-ko-ha-mu` gives the oven agent-marking. The oven
is not merely a location (`pa-ko-ha-mu`); it is the causal agent of the thermal
transformation. `ha-su` = thermally-structured = the state of being heat-set = the
physical state of baked cookies (set, structured by heat, no longer plastic dough).
`lu-ha-su` = result: heat-set = until the dough reaches the thermally-structured state.
The `;` between the clauses marks the sequence: placing comes first; the oven's
action is temporally subsequent and causally initiated by the placement.

---

### S664 — CKG-001-F: Remove the baked food; cool; the baked good is complete.

```
ki  lo-ha-zo-ra-ma ;  de-ha-ki ;  ha-zo-ra-ma  ne  be-su
```

**Written:** `ki lohazorama ; dehaki ; hazorama ne besu`

**Natural reading:** Move the thermally-treated food [from oven]; thermal decrease;
the thermally-treated food is completed-formation.

**Notes:** W216 (`ha-zo-ra-ma`) first attestation — **the phase-change transition.** In
S663 the material was `zo-ra-ma-su` (raw structured dough). In S664, after the oven's
thermal action, the same material is now `ha-zo-ra-ma` (thermally-treated food = the
baked good). The vocabulary change tracks the ontological change: the cookie is no
longer dough; it is a new entity defined by its thermal history. `de-ha-ki` = decay-
heat-change = the thermal decrease = cooling; composable from `de` (decrease/decay)
+ `ha` (thermal state) + `ki` (change). `be-su` = growth-result-structure = the
completed formation state = the state of being a fully produced artifact. The
sentence also marks a procedural completion: `ha-zo-ra-ma ne be-su` = the baked
food is [in its] completed-structure state = the cookies are done.

---

## CKG-001 Batch Summary

**Entries:** S659–S664 · **New vocabulary:** W214 (`ko-ha-mu`), W215 (`ma-ne-ki`), W216 (`ha-zo-ra-ma`)

| Entry | Written form | Step | Key vocabulary |
|-------|-------------|------|----------------|
| S659 (CKG-001-A) | `haki lokohamu` | Preheat | W214 (`ko-ha-mu`) first att. |
| S660 (CKG-001-B) | `maneki loki'mazorama pakomu lusune` | Mix wet | W215 (`ma-ne-ki`) first att. |
| S661 (CKG-001-C) | `panonekomu maneki losu'mazorama` | Mix dry | `su'ma-zo-ra-ma` first use |
| S662 (CKG-001-D) | `maneki loki'mazorama ne losu'mazorama` | Combine | Double `lo-` patient first att. |
| S663 (CKG-001-E) | `ki lozoramasu pakohamu ; lakohamu haki lozoramasu luhasu` | Bake | Artifact-agency; `ha-su` |
| S664 (CKG-001-F) | `ki lohazorama ; dehaki ; hazorama ne besu` | Remove + cool | W216 (`ha-zo-ra-ma`) first att. |

---

### CKG-001 Findings

**Finding 1: The instruction register drops `la-` when the agent is the immediate addressee.** S659–S663 use bare verb-compound imperatives with no `la-` marker. The agent (the cook) is recoverable from context at zero cost. This is not an omission — it is the formal instruction register in Tonesu. S663 demonstrates the contrast: clause 1 has no `la-` (the cook places the dough); clause 2 has `la-ko-ha-mu` (the oven, not the cook, performs the baking). `la-` appears exactly when the agent is not the default addressee.

**Finding 2: Wet/dry ingredient distinction uses existing matter-state vocabulary without new primitives.** `ki'ma-zo-ra-ma` (liquid food = wet ingredients) and `su'ma-zo-ra-ma` (solid food = dry ingredients) compose from W114 and W113 respectively, both already attested in the materials-science batches. The matter-state system (`ki'ma`, `su'ma`, `no-su'ma`, `ma-ra`) generalizes seamlessly into the culinary domain. No new roots were needed to distinguish wet from dry.

**Finding 3: Double `lo-` patient coordination with `ne` is composable and clear.** S662's `lo-ki'ma-zo-ra-ma ne lo-su'ma-zo-ra-ma` encodes the two ingredient classes as a jointly-patient pair. The `ne` between the two patients is not a new grammar rule — it applies the relational semantics of `ne` to the patient slot. The construction reads: the combining action's input is the bonded pair of both ingredient classes. The `ne` in `ma-ne-ki` (the action) rhymes with the `ne` joining its inputs — showing how `ne` threads through multiple levels of the same sentence.

**Finding 4: Artifact agency works — the oven earns its `la-` marker.** `la-ko-ha-mu ha-ki lo-zo-ra-ma-su` = the oven heat-changes the dough. An artifact performing its designed function is a legitimate agent in Tonesu; the grammar does not restrict `la-` to animate agents. This follows from the `la-` agent frame being semantically about causal source, not animacy. The oven is the causal source of thermal change, so `la-ko-ha-mu` is structurally correct.

**Finding 5: The phase change from dough to cookie is encoded in vocabulary, not in tense or aspect.** `zo-ra-ma-su` (structured food mixture = raw dough) in S663 becomes `ha-zo-ra-ma` (thermally-treated food = cookie) in S664. Tonesu has no tense system; temporal sequencing is handled by `;` and sentence order. The vocabulary itself carries the before/after: `zo-ra-ma-su` is the pre-thermal structure; `ha-zo-ra-ma` is the post-thermal result. The ontological transformation is visible in the compound.

---

## Colloquial Register Analysis

| Form used | CLQ entry | Colloquial form | Notes |
|-----------|-----------|-----------------|-------|
| `ko-ha-mu` | none | — | 3-root — first attestation; no corpus pressure yet |
| `ma-ne-ki` | none | — | 3-root — first attestation; no corpus pressure yet |
| `ha-zo-ra-ma` | none | — | 4-root — first attestation; no corpus pressure yet |
| `ki'ma-zo-ra-ma` | none | — | 4-root: inherits W114 + W144; first use as combined form; no corpus pressure yet |
| `su'ma-zo-ra-ma` | none | — | 4-root: inherits W113 + W144; first use as combined form; no corpus pressure yet |
| `zo-ra-ma-su` | none | — | 3-root: W144 + `su`; composable; first use as combined form; no corpus pressure yet |
| `ha-ki` | none | — | 2-root — below 3-morpheme contraction threshold |
| `de-ha-ki` | none | — | 3-root composable predicate — first use; no corpus pressure yet |
| `be-su` | none | — | 2-root — below 3-morpheme contraction threshold |
| `ha-su` | none | — | 2-root — below 3-morpheme contraction threshold |

**Verdict:** irreducibly formal — all new compounds are first attestations with no corpus pressure; all 2-root predicates are below threshold.

*CLQ entries registered from this batch: none.*
