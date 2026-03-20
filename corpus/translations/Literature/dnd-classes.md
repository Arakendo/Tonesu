---
title: "D&D — The Classes"
---

# Translation Test: Dungeons & Dragons — The Classes

## Source: Dungeons & Dragons (AD&D / D&D 5e, Wizards of the Coast / TSR)
## Status: First pass — 8-class founding set

---

## Purpose

The D&D class system is a role-taxonomy: each class is a named bundle of defining activities, abilities, and narrative identity. As a translation target, it tests Tonesu's **`-li` agent-suffix pattern** as a productive role-registry mechanism and exercises the closed primitive set to cover domains of combat, magic, stealth, devotion, nature, and performance.

Primary tests:

- **`-li` as productive role-suffix** — can all eight classes be encoded as `[activity-compound]-li` without exception? The test is whether the activity-compound is always compositional from existing primitives and whether `li` as the head-type correctly marks agent/role.
- **Force-source differentiation** — Fighter, Wizard, and Cleric all mobilize `ra` (force/energy), but through different sources. The batch tests whether Tonesu can distinguish direct force (`ka`), knowledge-sourced force (`to → ra`), and worth-sourced force (`vo → ra`) without collision.
- **Nature-world differentiation** — Druid, Ranger, and Ecologist (W150, existing) all share `zo` (living thing) as lead root. The batch tests whether three distinct relationships to the living world (containment, motion, study) are expressible without overlap using different second roots.
- **`lu-` beneficiary frame** — the Bard's defining sentence requires the beneficiary frame (`lu-zo-li`). This tests whether `lu-` can mark the other-directedness of performance as a structural feature of the class, not merely a contextual implication.
- **Bi-clausal parallel for dual identity** — the Paladin's identity requires two simultaneous defining activities (oath + force). The batch tests whether `/` can encode dual load-bearing class features without either clause being subordinate.

**Scope note:** Eight classes from the AD&D / early D&D founding set: Fighter, Wizard, Rogue, Cleric, Druid, Paladin, Ranger, Bard. Excluded from this batch: Barbarian, Monk, Sorcerer, Warlock (later additions; distinct enough in mechanism to warrant a separate batch). See notes/open-questions.md for deferred class designs.

---

## Vocabulary Framework

Eight new role compounds, all `-li` agent-type:

| W# | Form | Written | Class | Construction |
|----|------|---------|-------|--------------|
| W206 | `ra-ka-li` | rakali | Fighter | `ra` (force) + `ka` (intentional action) + `li` (agent). Force applied by volitional act. Load-bearing `ka` distinguishes from non-volitional force events (`ra-ki` W038 = storm). |
| W207 | `to-ra-li` | torali | Wizard | `to` (knowledge) + `ra` (force) + `li` (agent). Knowledge IS force: the wizard's conceptual knowledge is their force capacity. |
| W208 | `se-de-li` | sedeli | Rogue | `se` (perception) + `de` (decrease) + `li` (agent). Reduces own perceptibility. Distinct from `si-de` (W098, misinformation = signal decrease). |
| W209 | `vo-ra-li` | vorali | Cleric | `vo` (worth/sacred) + `ra` (force) + `li` (agent). Force sourced in sacred worth. Parallel to W207: both `X-ra-li`; source differs (`to` vs `vo`). |
| W210 | `zo-re-li` | zoreli | Druid | `zo` (organism) + `re` (cycle) + `li` (agent). Embeddedness in living cycles. Distinct from ecologist (W150 = studies) and ranger (W212 = moves through). |
| W211 | `wi-vo-li` | wivoli | Paladin | `wi` (will) + `vo` (worth) + `li` (agent). Will consecrated to an oath of worth. The `wi` root marks the paladin's relationship to worth as volitional/sworn, not direct force-channeling. |
| W212 | `zo-ki-li` | zokili | Ranger | `zo` (organism) + `ki` (motion) + `li` (agent). Motion through the living world. Distinct from `di-ki-li` (W061, traveler = directed path). |
| W213 | `so-vo-li` | sovoli | Bard | `so` (sound) + `vo` (worth) + `li` (agent). Creates worth through sound for others. The only class defined by acoustic performance for an audience. |

**Construction note — `X-ra-li` family:** Three classes share `ra` (force) as their axial root: `ra-ka-li` (fighter), `to-ra-li` (wizard), `vo-ra-li` (cleric). What differs is the positional relationship to `ra`:
- **Fighter (`ra-ka-li`):** `ra` is directly modified by `ka` (volitional action). The fighter IS the force-action agent.
- **Wizard (`to-ra-li`):** `to` modifies the `ra` → the force is sourced in knowledge. The wizard converts knowledge into force.
- **Cleric (`vo-ra-li`):** `vo` modifies the `ra` → the force is sourced in sacred worth. The cleric channels worth as force.

**Construction note — `zo-X-li` family:** Three entries share `zo` (living thing) as lead root:
- **Druid (`zo-re-li`):** `zo-re` = organism-cycle = embeddedness in living cycles. The druid IS within the cycle.
- **Ranger (`zo-ki-li`):** `zo-ki` = organism-motion = movement through living environments. The ranger MOVES through the wild.
- **Ecologist (`zo-su-ka-li` W150):** `zo-su-ka` = organism-structure-action = structured study of living systems. The ecologist STUDIES from outside.

Three stances: containment / traversal / study.

**Construction note — `vi-vo-li` avoidance:** An alternative Paladin gloss `vi-vo-li` (vow-worth-person) was considered but `vi` is not in the primitive set. `wi` (will/intention) correctly captures the volitional dimension of a sacred oath. The paladin's defining feature is willful commitment to worth, not a speech act of vowing per se.

---

## Source Text

The eight founding D&D classes and their defining characteristics:

- **Fighter** — master of weapons and armor; combat through martial skill and physical force
- **Wizard (Magic-User)** — commands arcane magic through study; knowledge is power, literally
- **Rogue (Thief)** — stealth, deception, precise strikes; evades detection and strikes from shadow
- **Cleric** — divine magic from devotion to a deity; healing and turning undead; faith as force
- **Druid** — nature magic; embodies the cycles of the natural world; wild shape; balance
- **Paladin** — holy warrior bound by a sacred oath; divine power through sworn commitment
- **Ranger** — wilderness guide and tracker; operates in the frontier between civilized and wild
- **Bard** — performer; magic through music and storytelling; inspiration as a gift to allies

---

## Batch: DND-004 (S651–S658)

### S651 — DND-004-A: Fighter

```
la-ra-ka-li  ra-ka  lo-zo-li
```

**Written:** `larakali raka lozoli`

**Natural reading:** A fighter applies force against persons.

**Notes:** W206 (`ra-ka-li`) first attestation. `ra-ka` as predicate = volitional force-application = the act of purposeful combat. `lo-zo-li` (W148, human persons) as patient = in combat, the fighter acts on others as persons. The `ka` component is essential: it marks the force as deliberate rather than incidental. Without `ka`, `la-ra-li  ra  lo-zo-li` would be indistinguishable from a natural force event acting on people — a flood, a falling tree. The fighter is identified by the intentionality of their force-application.

---

### S652 — DND-004-B: Wizard

```
la-to-ra-li  ra-be  go  to
```

**Written:** `latorali rabe go to`

**Natural reading:** A wizard's force manifests from knowledge.

**Notes:** W207 (`to-ra-li`) first attestation. `ra-be` = force-increase/emergence = force manifesting. `go to` = from/because-of knowledge. The class-defining structural claim: a wizard's magical force is the direct output of their organized knowledge. A wizard who loses their spellbook loses their `to`, and therefore their `ra`. The sentence encodes the mechanism, not just the fact. Parallel structure to S654 intentional — see Finding 2.

---

### S653 — DND-004-C: Rogue

```
la-se-de-li  se-de
```

**Written:** `lasedeli sede`

**Natural reading:** A rogue evades detection.

**Notes:** W208 (`se-de-li`) first attestation. Bare predicate `se-de` without patient — the rogue evades detection as a general activity. The absence of a patient is semantically correct: the rogue's evasion is ambient and constant, not targeted at any specific detector. The `se` root (raw perceptual input) distinguishes this from `si-de` (W098, misinformation = degradation of an encoded signal). A rogue reduces the perceptual trace they leave; a forger corrupts the signal itself. Two different attack surfaces: the detector's sense vs the signal's integrity.

---

### S654 — DND-004-D: Cleric

```
la-vo-ra-li  ra-be  go  vo
```

**Written:** `lavorali rabe go vo`

**Natural reading:** A cleric's force manifests from worth.

**Notes:** W209 (`vo-ra-li`) first attestation. Structural parallel to S652 (wizard): `ra-be go vo` vs `ra-be go to`. The variable `go [source]` captures the wizard/cleric distinction as a one-root change. A cleric who loses their faith loses their `vo`, and therefore their `ra`. The `vo` root carries the sacred/devoted register: worth, holiness, value — all expressible from a single committed primitive.

---

### S655 — DND-004-E: Druid

```
la-zo-re-li  ko  lo-re-zo
```

**Written:** `lazoreli ko lorezo`

**Natural reading:** A druid is contained within the life-cycle.

**Notes:** W210 (`zo-re-li`) first attestation. `ko` = containment predicate (is within / belongs to / is enclosed by). `lo-re-zo` = patient: `re` (cycle) + `zo` (organism) = cycle-of-organisms = life-cycle. Note the root-order reversal: the compound name is `zo-re-li` (organism-cycle-person) but the patient NP is `re-zo` (cycle-of-organisms) — the cycle is foregrounded as the container. The druid is not outside studying the cycle, nor moving through it — they are INSIDE it, as a belonging member of seasonal/ecological repetition.

---

### S656 — DND-004-F: Paladin

```
la-wi-vo-li  wi  lo-vo  /  ra-be
```

**Written:** `lawivoli wi lovo / rabe`

**Natural reading:** A paladin wills toward worth / and force manifests.

**Notes:** W211 (`wi-vo-li`) first attestation. The bi-clausal parallel (`/`) is required because neither clause alone captures the paladin: a being who wills toward worth but never manifests force is a monk or a saint; a being who manifests force but has no will-toward-worth is a fighter. The paladin is constitutively both, simultaneously. The second clause `ra-be` is bare — agent is the same paladin as first clause, force emerges as a consequence of the oath rather than as a separate volitional act. Contrast: a wizard PRODUCES force from knowledge through effort; a paladin's force MANIFESTS as an expression of the oath.

---

### S657 — DND-004-G: Ranger

```
la-zo-ki-li  ki  lo-pa-fe
```

**Written:** `lazokili ki lopafe`

**Natural reading:** A ranger moves to the frontier.

**Notes:** W212 (`zo-ki-li`) first attestation. `ki` as predicate = moves/travels. `lo-pa-fe` (W138, boundary-space/frontier) = the ranger's canonical spatial domain. The frontier (`pa-fe`) is the zone between the settled world and the wild — exactly where a ranger operates. The sentence encodes the ranger's spatial identity: they are defined by their relationship to the boundary, not by what lies on either side of it. Contrast `di-ki-li` (W061, traveler): the traveler moves along directed routes; the ranger navigates the living world toward its edges.

---

### S658 — DND-004-H: Bard

```
la-so-vo-li  so-vo  lu-zo-li
```

**Written:** `lasovoli sovo luzoli`

**Natural reading:** A bard creates sonic worth for persons.

**Notes:** W213 (`so-vo-li`) first attestation. `so-vo` as predicate = produces sonic worth / performs. `lu-zo-li` = beneficiary frame: the sonic worth is created FOR persons (the audience). The `lu-` particle is structural in this sentence: it moves the bard's defining activity from self-expression to gift. A bard performing in isolation is not yet a bard in action — barding is constitutively for others. This makes the bard the most socially-embedded class in the DND-004 batch: their defining predicate requires an audience as a structural beneficiary.

---

## DND-004 Batch Summary

| Entry | Written form | Class | Key vocabulary |
|-------|-------------|-------|----------------|
| S651 (DND-004-A) | `larakali raka lozoli` | Fighter | W206 first att.; `ra-ka` = volitional force; `ka` distinguishes from `ra-ki` W038 |
| S652 (DND-004-B) | `latorali rabe go to` | Wizard | W207 first att.; `ra-be go to` = force manifests from knowledge |
| S653 (DND-004-C) | `lasedeli sede` | Rogue | W208 first att.; bare predicate; `se` vs `si` distinction |
| S654 (DND-004-D) | `lavorali rabe go vo` | Cleric | W209 first att.; `ra-be go vo` = force manifests from worth; parallel to S652 |
| S655 (DND-004-E) | `lazoreli ko lorezo` | Druid | W210 first att.; `ko` containment; `re-zo` life-cycle patient |
| S656 (DND-004-F) | `lawivoli wi lovo / rabe` | Paladin | W211 first att.; bi-clausal parallel `/`; oath + force dual identity |
| S657 (DND-004-G) | `lazokili ki lopafe` | Ranger | W212 first att.; `pa-fe` W138 frontier destination |
| S658 (DND-004-H) | `lasovoli sovo luzoli` | Bard | W213 first att.; `lu-` beneficiary frame; only other-directed class |

---

### Findings

**Finding 1: All eight founding classes reduce to 3-root `-li` agent compounds without requiring new primitives.** 12 primitives suffice: `ra`, `to`, `se`, `vo`, `zo`, `wi`, `so`, `ka`, `de`, `re`, `ki`, `li`. The closed primitive set is not strained by this vocabulary domain. The `-li` pattern is confirmed as a productive role-registry mechanism.

**Finding 2: `X-ra-li` forms a structural force-source family.** Fighter (`ra-ka-li`), Wizard (`to-ra-li`), Cleric (`vo-ra-li`) are the clearest cross-class structural group. All share `ra` (force) as axial; what differs is the relationship to force. S652 and S654 use the same predicate frame (`ra-be go [source]`) with a one-root variable change, encoding the wizard/cleric distinction maximally economically.

**Finding 3: `zo-X-li` forms a living-world relational family.** `zo-re-li` (W210, druid), `zo-ki-li` (W212, ranger), `zo-su-ka-li` (W150, existing ecologist) express three distinct modes of relationship to the living world — containment (`re` = cycles), traversal (`ki` = motion), and study (`su-ka` = structural action). The triad is complete as a relational taxonomy on the `zo` root.

**Finding 4: The Paladin requires structural complexity unavailable to simpler role-classes.** The bi-clausal parallel `/` is necessary for the paladin because their identity is constitutively dual: oath AND force, neither subordinate to the other. The paladin is the only class in this batch whose defining sentence cannot be expressed in a single predicate frame. This structural complexity in the grammar mirrors the structural complexity of the class: the paladin is defined by the conjunction of sworn will and manifested force.

**Finding 5: The `lu-` beneficiary frame structurally marks the Bard's other-directedness.** The bard is the only class in DND-004 whose defining sentence uses `lu-` (beneficiary) rather than `lo-` (patient) or `go` (source). This is not merely a contextual note — it is a grammatical marker of the bard's constitutive social embedding. Performance requires an audience. The grammar enforces this at the structural level.

**Cross-batch connections:**

- Fighter (`ra-ka-li`) and Paladin (`wi-vo-li`) contrast directly on the DND-002 alignment axis: the fighter's compound has no ethical orientation; the paladin's does (`wi-vo`). A Lawful Good Fighter and a Paladin share behavior but differ in structural composition — the paladin's will is committed to good.
- Ranger (`zo-ki-li`) and Druid (`zo-re-li`) map to DND-002 alignment exemplars: the source book gives CG for the Ranger and TN for the Druid. This aligns with their structural relationship to the living world: the ranger moves freely (CG = `wi-no-su / wi-vo`); the druid maintains balance in cycles (TN = `wi-su-fe / wi-vo-fe`).
- Wizard (`to-ra-li`) and the magic schools (DND-001) are directly connected: `wi-ra-su` (W179, magic as systematic directed force) is the broader class; the eight schools are its subspecies. The wizard is the practitioner specifically defined by `to` → `ra` conversion, whereas a cleric uses `vo` → `ra` and a sorcerer (deferred) would use something else as source.

---

## Colloquial Register Analysis

| Form used | CLQ entry | Colloquial form | Notes |
|-----------|-----------|-----------------|-------|
| `ra-ka-li` | none | — | 3-root — first attestation; no corpus pressure yet |
| `to-ra-li` | none | — | 3-root — first attestation; no corpus pressure yet |
| `se-de-li` | none | — | 3-root — first attestation; no corpus pressure yet |
| `vo-ra-li` | none | — | 3-root — first attestation; no corpus pressure yet |
| `zo-re-li` | none | — | 3-root — first attestation; no corpus pressure yet |
| `wi-vo-li` | none | — | 3-root — first attestation; no corpus pressure yet |
| `zo-ki-li` | none | — | 3-root — first attestation; no corpus pressure yet |
| `so-vo-li` | none | — | 3-root — first attestation; no corpus pressure yet |
| `ra-ka` | none | — | 2-root predicate — below 3-morpheme contraction threshold |
| `ra-be` | none | — | 2-root predicate — below 3-morpheme contraction threshold |
| `se-de` | none | — | 2-root predicate — below 3-morpheme contraction threshold |
| `re-zo` | none | — | 2-root patient NP — below 3-morpheme contraction threshold |

**Verdict:** irreducibly formal — all new compounds are first attestations with no corpus pressure; all predicates are 2-root below threshold.

*CLQ entries registered from this batch: none.*
