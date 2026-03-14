# Semantic Primitives

## Status: Draft

This is the closed (or near-closed) set of foundational semantic roots. These are the conceptual atoms from which all other vocabulary is built. Changes here are breaking changes to the whole language.

**Target size: 30–100 roots.**
**Current count: 34 (31 starter set + `ha` added after corpus stress test, March 2026 + `fa` added as affective substrate primitive, March 2026 + `zi` added as mutual-transformation primitive, three-domain threshold reached March 2026)**

---

## Validation Rules

Before adding or accepting a root, it must pass all three checks:

### Rule 1 — Cognitively atomic
The root must not be a category, a compound idea, or a named thing. It must be an irreducible conceptual element.

Fail: `machine`, `vehicle`, `animal`, `water` — these are categories or objects, not atoms.
Pass: `move`, `living`, `tool`, `contain`, `change`, `surface`, `inside`, `think`.

Test: can this root be defined using other primitives? If yes, it is probably not a primitive.

### Rule 2 — Combines cleanly
The root must produce useful compounds without mental gymnastics.

Good combinations:
```
tool + cut    →  knife
move + water  →  river / flow
think + system →  theory / model
body + move   →  walk
```

If combining two roots produces something ambiguous or requires a third root to disambiguate every time, at least one of the roots is too broad.

### Rule 3 — No hidden metaphors
The root's meaning must be its literal meaning. Metaphorical extensions are allowed but must be explicitly documented in the `Notes` field — they are not part of the root's core definition.

Fail: encoding `understand` as a spatial relation (the English etymology "stand under") without flagging it.
Pass: root means what it sounds like; any extended use is tracked.

---

## Entry Format

```
Root:     phonetic form
Gloss:    brief English equivalent
Domain:   broad category
Includes: what falls within this root's meaning
Excludes: what must NOT be covered by this root (prevents overlap)
Notes:    design rationale, documented metaphor extensions if any
```

---

## Starter Primitives

### Entities and Substances

**Ontological model for animate entities (explicit):**

`zo` is the base class for all living things. `li` is a subtype: a living thing with social agency and intention. Every `li` is also a `zo`; not every `zo` is a `li`.

```
zo           = organism (dog, tree, bacterium)
zo + li      = human person
mu + li      = intentional agent without biology (AI, institution)
zo (no li)   = animal / creature without social agency
```

A robot that acts with intention is `mu + li`. An animal is `zo`. A human is `zo + li`. This must be composable, not re-litigated each time.

| Root | Gloss | Includes | Excludes |
|------|-------|----------|----------|
| `mu` | object / artifact | physical non-living artifacts, tools, devices | living agents, abstract concepts |
| `ma` | matter / substance | raw unformed material, physical substrate | structured objects, living tissue |
| `zo` | living thing | any organism: plant, animal, fungus, microbe | non-living matter, abstract agents |
| `li` | social agent / person | conscious intentional actor, social being | implies `zo` unless combined with `mu`; excludes non-intentional life |

---

### Processes and Change

**Process model (explicit):**

`ki` is narrowed to physical or positional motion only. General transformation is handled by compounding. `be` and `de` cover directed change (increase/decrease).

| Root | Gloss | Includes | Excludes |
|------|-------|----------|---------|
| `ki` | motion | physical movement, displacement, travel | transformation, change of state, growth — those use `be`/`de` compounds |
| `ka` | intentional action | deliberate acts, operations, exertion of will | passive or involuntary processes |
| `be` | growth / increase | building up, generation, emergence, gain | reduction, destruction, motion without change |
| `de` | decay / decrease | breaking down, ending, entropy, loss | growth, construction |

*Candidate root evaluated and rejected:*

| Root | Gloss | Notes |
|------|-------|-------|
| ~~`ce`~~ | ~~transformation / state change~~ | **Rejected — phonologically illegal.** `c` is excluded from the consonant inventory (see spec/phonology.md). Semantic need assessed: qualitative state change (`be`/`de` compounds and `ki`-compounds cover the space without ambiguity). No valid replacement form proposed; no corpus pressure identified. Closed. |

---

### Structure and Pattern

**`su` vs `to` distinction (explicit):**

`su` = physical or organizational arrangement in the world. `to` = conceptual pattern, model, or thought in a mind or formal system. A crystal lattice is `su`. A theory about crystal lattices is `to`. A musical score is `to`; the sound waves it produces are `su` + `so`.

| Root | Gloss | Includes | Excludes |
|------|-------|----------|----------|
| `su` | structure / order | physical arrangement, organization, system, spatial form | processes, raw material, mental models |
| `to` | conceptual pattern / thought | idea, plan, model, logic, knowledge, mental representation | physical structure, raw sensory data |
| `fe` | boundary / limit | edge, category, distinction, threshold | internal content, connection |

---

### Relations

**`zi` vs `ne` and `go`/`du` distinction (explicit):**

`ne` is a static bond — it describes a persisting connection between two entities but implies nothing about either entity changing. `go`/`du` encode a directional causal chain: argument structure flows from cause to result, one event producing another. `zi` fills the orthogonal gap: a *coupled event* in which both participants transform simultaneously by virtue of their mutual engagement, with neither transformation prior to the other and neither participant the unilateral cause.

Canonical contrast:
- `ne` → the organisms are in metabolic relation. (static state)
- `go [A ne B]  du [A ki]  du [B ki]` → A's motion results, then B's. (sequential distortion)
- `zi` → both are transformed at once by the coupling event itself. (correct ontology)

`ne-ra` (W058) is retained as distinct: `ne-ra` = *state* of energetic coupling (the resonance condition); `zi-ra` = *event* of mutual energy transformation (the interaction occurring). State and event are complementary, not competing. `ne-ra-ki` (W059, entering resonance) is likewise unaffected.

**Biological lifecycle clarity (from March 2026 admission analysis):** `zi` is precision-scoped in biology because it requires symmetry of modification. Three biological event types that look related are structurally distinct:

| Stage | Structure | Why |
|-------|-----------|-----|
| Mating | `zi-zo` | Two organisms enter coupled biological interaction; both change state; no unilateral cause |
| Symbiosis | `zi-zo` | Same ontological structure: mutual modification by coupling |
| Fertilization | `ki` / `go-be` | Asymmetric: one gamete absorbed into another; creates new entity; directional process |
| Development | `be` | Single-participant growth; no coupling partner |
| Predation | `go...du` | Directed: predator causes prey's transformation |

`zi` holds the boundary correctly: mating and symbiosis are mutual (both parties transformed by coupling); fertilization, development, and predation are not.

| Root | Gloss | Includes | Excludes |
|------|-------|----------|----------|
| `ne` | relation / connection | link, bond, membership, network | the entities themselves |
| `pe` | part / component | piece, element, member of a whole | the whole, the relation |
| `go` | cause / origin | reason, source, trigger | result, the caused event |
| `du` | result / effect | outcome, product, consequence | cause, process |
| `zi` | mutual / coupling event | bilateral transformation events; any event where two participants are simultaneously modified by their mutual engagement; reciprocal exchange | static relation (use `ne`); directed causation (use `go`/`du`); single-participant change (use `be`/`de`/`ki`); energetic resonance *state* (use `ne-ra`) |

---

### Space and Location

| Root | Gloss | Includes | Excludes |
|------|-------|----------|----------|
| `pa` | place / space | location, region, physical topology | containment/interior (use `ko`), time, abstract logical space |
| `di` | direction | toward, away, path, orientation | location itself |
| `ko` | containment / interior | inside, enclosed space, container, boundary-interior | exterior, direction, mere location |

---

### Time

| Root | Gloss | Includes | Excludes |
|------|-------|----------|----------|
| `ti` | time / sequence | moment, duration, order of events | location, abstract cycles |
| `re` | repetition / cycle | recurrence, rhythm, iteration | single events |

---

### Perception and Information

**Phonetic concern:** `se`, `so`, `su`, `si` cluster is a collision risk at normal speech speed. `su` belongs to Structure and should already be phonetically distinguished by context, but the `se`/`so`/`si` triple requires care. If any of these reassigned, update the cluster review in open questions.

**`si` scope note:** `si` covers all encoded representation — language, symbols, data, writing, code, maps. This is intentionally broad. It is a civilization-scale root. It combines with `su` for structured representation and with `to` for interpreted meaning.

| Root | Gloss | Includes | Excludes |
|------|-------|----------|----------|
| `se` | perception / sense | raw sensory awareness: sight, hearing, touch, detection | processed knowledge (use `to`), encoded signal (use `si`) |
| `so` | sound | acoustic signal, spoken signal, audio | other senses, encoded/written signal |
| `lu` | light / visibility | visual signal, illumination, electromagnetic visibility | sound, other senses |
| `si` | signal / representation | any encoded information: symbol, sign, data, language, code | raw unencoded perception (use `se`), interpreted meaning (use `to`) |

---

### Mind and Value

| Root | Gloss | Includes | Excludes |
|------|-------|----------|----------|
| `vo` | value / quality | worth, evaluation, degree, intensity | factual properties |
| `wi` | will / intention | goal, desire, purpose | knowledge, action itself |
| `no` | negation / absence | not, lack, removal | presence, addition |

---

### Quantity

| Root | Gloss | Includes | Excludes |
|------|-------|----------|----------|
| `nu` | quantity / number | count, measure, amount | type, quality |
| `ru` | unity / singularity | one, individual, whole | plurality |
| `pu` | plurality / collective | many, group, set | individual |

*Note: `plu` replaced with `pu` to comply with the CV/CVC syllable rule. All prior references to `plu` should be updated.*

---

### Energy and Force

**`ra` vs `ha` distinction (explicit):**

`ra` is energy as *force or capacity* — the potential or actual ability to cause change. An electrical charge, a structural load, a kinetic impact: these are `ra`. `ha` is the *thermal state of matter* — how much heat a substance currently holds, experienced as temperature. The difference: a frozen conductor carrying high current has high `ra` and low `ha` simultaneously. They are orthogonal properties.

As a result, `ra-de` does not mean "cold" — it means "energy is decreasing" (power failure, deceleration). Cold is `no-ha` (absence/negation of thermal intensity). Hot is `ha-vo` (thermal intensity as quality), `ha-be` (heat increasing), or bare `ha` in predicate position.

| Root | Gloss | Includes | Excludes |
|------|-------|----------|----------|
| `ra` | energy / force | power, charge, capacity to cause change, kinetic force | thermal state of matter (use `ha`), structure, information, motion itself |
| `ha` | heat / thermal state | temperature, warmth, coldness as matter-property, thermal intensity | energy as force or capacity (use `ra`), light (use `lu`), sound (use `so`) |

---

### Affective Substrate

**`fa` vs `se` distinction (explicit):**

`se` is *outward-facing* detection — the organism registering signals from the world: sight, sound, touch, pressure, external-object awareness. `fa` is the *inward-facing* felt-interior of organismic state — the affective tone arising from body chemistry, mood substrate, memory activation, and arousal level. The distinction: a person who is chemically depressed but sitting in silence is not *detecting* anything (`se`), yet `fa` is clearly active and degraded. A person under anaesthesia has `se` blocked but `fa` continues as substrate until the body shuts down. They are orthogonal, not on the same axis.

This is the same logic that separated `ha` from `ra`: thermal *state of matter* is not the same as *energy as force*, even though heat and energy interact constantly.

**Substrate symmetry:** `fa` completes a pattern already present in the primitive set:

| Root | Domain | Role |
|------|--------|------|
| `ma` | matter | physical substrate |
| `ra` | energy | dynamic property |
| `ha` | heat | thermal state of matter |
| `zo` | organism | biological substrate |
| `fa` | affect | organism's interior state |

Each row is a real ontological layer, not reducible to the others. `fa` is the affective-state complement to `zo` the same way `ha` is the thermal-state complement to `ma`.

**The three-stage pipeline:** `fa` occupies the middle position in the mental processing sequence:

```
se  →  fa  →  to
perception (outward)   affect (substrate)   cognition (model)
```

A sudden loud bang: `la-mi  se  so` (I hear a sound) → `la-mi  fa-be` (affect rising) → `la-mi  to  lo-go` (I form a model of the cause). These are three distinct events on the same pipeline. `fa` is the layer that can get stuck — `fa-no-to` = the signal arrived and affect activated, but no model formed.

Concrete three-step example (thunder):
```
la-mi  se  so       I hear a sound
la-mi  fa-be        dread rises
la-mi  to  lo-go    I identify the cause
```

**Stress-test verdict (Monday, March 2026):** All three boundary zones passed:
- `se` vs `fa`: perception and affect are clearly distinct — a chemically depressed person has active `fa` without any active `se` target
- `fa` vs `vo`: `fa` is pre-evaluative; affect rises before value judgment occurs — `fa-be` with no `vo` modifier is valid and common (uneasy affect with no evaluation)
- `fa` vs `to`: the stages are sequential and separable; `fa-no-to` = affect without cognition is the most important construction

**Drift risk (logged):** Speakers may use `fa-be` as a catch-all casual emotional marker. This is acceptable colloquial drift — formal register preserves specificity. The constraint holds in normative usage.

**Phonesthetic note:** The `f`-initial open-vowel onset produces compounds (`fa-be`, `fa-no`, `fa-ki`, `fa-re`) that phonologically suggest soft interior motion — distinct from the sharper detection roots (`se`, `si`, `so`). This alignment between phonology and semantics is incidental but welcome.

**Usage guard (normative, per Principle 9):** `fa` names the substrate, not the state. `fa-vo-be` is not joy; `fa-vo-de` is not sadness. Named emotional states are still derived via process constructions. `fa` appears where the substrate itself is foregrounded: unresolved affect, numbness, arousal level, observer-mode separation.

| Root | Gloss | Includes | Excludes |
|------|-------|----------|---------|
| `fa` | affective substrate | inward-facing felt tone of organism state: mood substrate, arousal level, valence of internal chemistry, pre-conceptual affect | named emotions (use process constructions), external sensory detection (use `se`), conceptual knowledge (use `to`) |

---

## Notes

- Roots should be 1–2 syllables, CV or CVC
- No two roots should be phonetically confusable at normal speaking speed
- Roots are language-internal; gloss translations are approximations only
- The primitive set is intentionally incomplete — gaps are filled by compounding, not by adding more primitives prematurely

---

## Stress-Test Compounds

These concepts must be expressible using only existing primitives. If a construction requires inventing a new root, that is a diagnostic — evaluate whether the root is genuinely missing or whether the compound is just awkward.

| Concept | Construction | Notes |
|---------|-------------|-------|
| tree | `zo + su` | living thing with vertical structure |
| river | `ma + ki + di` | matter in directed motion (water is `ma`; water-specifically requires context or a domain modifier) |
| language | `si + su` | structured system of encoded representation |
| tool | `mu + ka` | artifact for intentional action |
| government | `li + pu + su` | organized structure of many social agents |
| memory | `to + ko` | contained / stored conceptual pattern |
| computer | `to + ki + mu` | artifact that processes conceptual patterns |
| mathematics | `to-su-ne` | conceptual structural relations — composes without new roots |
| dimension / parameter | `nu-to` | quantitative concept — "axis of measurement"; composes cleanly |
| proof | `to-go-du` | conceptual causal chain: from premises (`to`) via cause (`go`) to conclusion (`du`). High-confidence compound — flag for dedicated corpus test |
| give / transfer (loss) | `la-[giver]  ne-[recipient]  lo-[object]  de` | recipient particle + release; giver loses possession. Corpus: S056. |
| copy / transfer (no loss) | `de-ki-be` or `ka-ne` (candidates) | Agentive transfer without possession-loss. S056 downgraded this from gap to candidate: `de-ki-be` (release-motion-generate) or `ka-ne` (intentional-toward-recipient). Neither fully attested. Monitor corpus for a copy/share sentence to force the decision. |
| need / dependency | `ne-fe` | Resolved S058: `lo-zo-li  ne-fe  ma` = "the person is in a dependency-condition toward substance." State predication confirmed. `ne-fe` registered as derived compound. |
| physical power / capacity | `ra` (primitive) | `ra` already covers energy-as-force-or-capacity. `ra-be` = power increasing; `ra-de` = power depleting; `ra-nu` = power level/magnitude. No gap. |
| social / institutional authority | `wi-go` (candidate compound) | Two distinct aspects: (1) the *directive* — `wi` (will/intention); (2) the *causal reach* — `go` (originates action in others). Compound: `wi-go` = directive-origination; `wi-go-li` = authority-holder / leader. Legitimacy (recognized vs unrecognized) is contextual: `wi-go-li  ne  to-li-pu` = authority-holder per the social model. Illegitimate force = `ra-go-li`. No new primitive needed. Register `wi-go` when corpus produces a sentence that requires it. |
| magnitude (physics / quantitative) | `ra-nu`, `du-nu`, `[domain]-nu` | In the physics register, magnitude = scalar size of a quantity: `ra-nu` (force magnitude), `du-nu` (effect magnitude). Pure `nu` in all quantitative contexts. |
| magnitude (scale / intensity) | `vo` / `nu-vo` | In colloquial or evaluative register, "great magnitude" = scalar intensity = `vo` or `nu-vo` (quantity-quality). No gap; the two registers split cleanly across existing roots. |
| logical possibility | `to-go [X]` | Hypothetical/counterfactual frame — already canonical. Logical possibility = the speaker's model includes X as a non-actual candidate. No gap. |
| epistemic uncertainty | `no-to` | Cannot assign even a model-floor. Already registered. The three-tier epistemic scale (`se`/`si`/`to`) carries ordinal confidence; `no-to` = below the lowest floor. No gap. |
| probability / confidence level | `nu-to` (candidate compound) | Cardinal layer on the ordinal epistemic scale: quantity-of-belief. `nu-to-be` = confidence increasing (new evidence); `nu-to-de` = confidence decreasing. "High probability" = `nu-to  vo`. Distinguishes probability (cardinal measure) from uncertainty (ordinal floor failure). Register `nu-to` when corpus produces a sentence requiring an explicit confidence quantity. |
| randomness / stochastic | `du-no-go` (candidate compound) | Result-without-traceable-cause. Correctly distinguishes randomness (causally opaque) from uncertainty (epistemically opaque): a quantum event is `du-no-go` even if you know its probability distribution. No new primitive needed. |

*`tree` is the weakest — `zo+su` is structurally valid but loses the plant/non-animal distinction. `zo` subtypes decision is now settled (compound strategy: `zo-ki` / `zo-no-ki`), so this row is closed. `need/dependency` resolved by `ne-fe` (S058). `copy/transfer` still pending corpus pressure. `power/authority` and `magnitude` logged March 2026 — not primitive gaps, compounds sufficient. `probability/uncertainty/possibility` logged March 2026 — four sub-concepts, all decompose cleanly, no primitive gap.*

---

## Open Questions

- [x] ~~`zo` subtypes: should plant, animal, and fungus be distinguishable by compound, or is `zo` intentionally undifferentiated below the organism level?~~ **Resolved — compound strategy adopted. `zo-ki` (motile organism = animal), `zo-no-ki` (non-motile organism = plant/fungus). `zo` remains undifferentiated at the primitive level; subtypes are compositionally expressed. No new root needed.**
- [ ] Does `to` need to split? Current model: `to` = all conceptual pattern including knowledge. Risk: overload. Split candidate: `to` = thought/pattern, new root = stored/retrieved knowledge. **Do not split until corpus forces it — probably after ~100 more sentences.**
- [x] ~~Should `ra` (energy) cover information energy or remain strictly physical?~~ **Resolved — `ra` stays strictly physical.** Energy capacity, force, charge, kinetic impact: `ra`. The energy *carrying* a signal (the physical channel) is `ra-si`; the encoded information content is `si`. These are orthogonal. Extending `ra` into information scope would blur the `ra`/`si` boundary without adding precision. No extension needed.
- [x] ~~Phonetic cluster `se`/`so`/`si`: evaluate whether all three survive at normal speech speed or whether one needs reassignment.~~ **Resolved — S108–S113 stress test.** All three roots survive in normal compound usage. The vowels /e/, /i/, /o/ provide sufficient acoustic distance. One genuine exposure: same-frame adjacent minimal pairs (e.g. `lo-se-su  lo-si-su`) where a single vowel carries full disambiguation. No reassignment needed. Watch: if a future domain generates heavy `so-[X]` / `si-[X]` adjacent compound usage, re-evaluate in that domain. See corpus S108–S113.
- [x] ~~Evaluate candidate root `ce` (transformation/state change) after first corpus sentences are written.~~ **Rejected — `c` is not in the consonant inventory (spec/phonology.md). Phonological gate failure; closed.**
- [x] ~~Update all references from `plu` → `pu` across spec and corpus files.~~ **Complete.** All content files use `pu`. The note in the Quantity table is retained as a historical record.
- [x] ~~**Need / functional dependency — resolved by compound `ne-fe` (S058).**~~ **Closed.** `lo-zo-li  ne-fe  ma` = "the person is in a dependency-condition toward substance." State predication confirmed; no new primitive required. `ne-fe` registered as a stable compound for dependency/requirement conditions.
- [ ] **Static state / copula — slow-pressure watch.** No primitive for "X is in condition Y" without invoking change (`be`/`de`) or evaluation (`vo`). Currently handled by juxtaposition predicates (`lo-X  state`) and P-GP-001 copula patterns. Likely becomes explicit pressure after ~100–200 corpus sentences. Do not add root prematurely — monitor whether grammar formalizes the copula pattern first. Candidate compound: `su-ti` (W101).
- [x] ~~**Bidirectional coupling / interaction — ACTIVE PRIMITIVE CANDIDATE.**~~ **Resolved. `zi` admitted as primitive 34, March 2026.** Formal three-rule validation complete; three-domain corpus threshold met (S189 physics, S193 biology, S194 social). All three validation rules pass. Phonological gate: `zi` (/z/+/i/), CV form, robust vowel contrast with `zo` (/z/+/o/), no particle/suffix collisions. Full primitive-pressure test applied to S194 per revised protocol: three decompositions attempted, repair by compounding fails, wrong-reading classification across all three domains confirmed persistent. First compound registrations: `zi-ra` (W104, proposed, mutual energy interaction) and `zi-ka` (W105, proposed, intentional exchange event). `ne-ra` (W058) retained as distinct — `ne-ra` = energetic resonance *state*; `zi-ra` = mutual energy-transformation *event*. See distinction note in Relations table above. *Cross-reference: open-questions.md P-PR-002 (closed).*
