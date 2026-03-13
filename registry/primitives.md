# Semantic Primitives

## Status: Draft

This is the closed (or near-closed) set of foundational semantic roots. These are the conceptual atoms from which all other vocabulary is built. Changes here are breaking changes to the whole language.

**Target size: 30–100 roots.**
Current count: 31 (starter set — to be expanded carefully)

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

`ki` is narrowed to physical or positional motion only. General transformation is handled by compounding. `be` and `de` cover directed change (increase/decrease). A candidate root `ce` (transformation / state change) is flagged for evaluation if compounding proves insufficient.

| Root | Gloss | Includes | Excludes |
|------|-------|----------|---------|
| `ki` | motion | physical movement, displacement, travel | transformation, change of state, growth — those use `be`/`de` or `ce` |
| `ka` | intentional action | deliberate acts, operations, exertion of will | passive or involuntary processes |
| `be` | growth / increase | building up, generation, emergence, gain | reduction, destruction, motion without change |
| `de` | decay / decrease | breaking down, ending, entropy, loss | growth, construction |

*Candidate root pending evaluation:*

| Root | Gloss | Notes |
|------|-------|-------|
| `ce` | transformation / state change | for qualitative change that is neither motion nor growth/decay — e.g. melting, freezing, conversion. Add only if `ki+be`/`ki+de` compounds prove ambiguous. |

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

| Root | Gloss | Includes | Excludes |
|------|-------|----------|----------|
| `ne` | relation / connection | link, bond, membership, network | the entities themselves |
| `pe` | part / component | piece, element, member of a whole | the whole, the relation |
| `go` | cause / origin | reason, source, trigger | result, the caused event |
| `du` | result / effect | outcome, product, consequence | cause, process |

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

| Root | Gloss | Includes | Excludes |
|------|-------|----------|----------|
| `ra` | energy / force | power, charge, capacity to cause change | structure, information, motion itself |

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

*All seven compose without new roots. `tree` is the weakest — `zo+su` is structurally valid but loses the plant/non-animal distinction. Flagged for review once the `zo` subtypes decision is made.*

---

## Open Questions

- [ ] `zo` subtypes: should plant, animal, and fungus be distinguishable by compound, or is `zo` intentionally undifferentiated below the organism level?
- [ ] Does `to` need to split? Current model: `to` = all conceptual pattern including knowledge. Risk: overload. Split candidate: `to` = thought/pattern, new root = stored/retrieved knowledge.
- [ ] Should `ra` (energy) cover information energy or remain strictly physical? Currently excluded from `si`/`to` scope.
- [ ] Phonetic cluster `se`/`so`/`si`: evaluate whether all three survive at normal speech speed or whether one needs reassignment.
- [ ] Evaluate candidate root `ce` (transformation/state change) after first corpus sentences are written.
- [ ] Update all references from `plu` → `pu` across spec and corpus files.
