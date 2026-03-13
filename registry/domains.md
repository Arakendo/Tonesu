# Domain Registry

## Status: Draft

This is the data registry of declared domains. Rules for domain creation are in spec/domain-creation.md.

---

## Entry Format

```
Label:      short domain identifier (da-xx form)
Name:       plain language name
Substrate:  conceptual material (primitive root)
Principle:  organizing transformation (primitive root)
Parent:     parent domain if inherited (or — if top-level)
Status:     proposed | accepted | lexicalized
Notes:      scope, examples, related domains
```

---

## General / Cross-Domain

These provide meta-structure. All other domains inherit from or compose with these.

| Label | Name | Substrate | Principle | Parent | Status |
|-------|------|-----------|-----------|--------|--------|
| `da-su` | Structure domain | `su` matter/structure | `su` order/arrangement | — | proposed |
| `da-ki` | Process domain | `ki` change | `ki` sequence/flow | — | proposed |
| `da-to` | Knowledge domain | `to` pattern | `to` organization/model | — | proposed |
| `da-li` | Agent domain | `li` person | `wi` intention/action | — | proposed |

---

## Physical Sciences

| Label | Name | Substrate | Principle | Parent | Status | Notes |
|-------|------|-----------|-----------|--------|--------|-------|
| `da-ra` | Energy domain | `ra` energy | `ki` transfer/conversion | — | proposed | thermodynamics, physics |
| `da-ki-ra` | Motion domain | `ki` motion | `ra` force/direction | `da-ra` | proposed | mechanics |
| `da-ma` | Matter domain | `ma` substance | `su` composition/state | — | proposed | chemistry, materials |
| `da-pa` | Space domain | `pa` space | `su` topology/location | — | proposed | geometry, geography |

---

## Life Sciences

| Label | Name | Substrate | Principle | Parent | Status | Notes |
|-------|------|-----------|-----------|--------|--------|-------|
| `da-zo` | Life domain | `zo` living thing | `be` growth/function | — | proposed | biology broadly |
| `da-zo-su` | Life-structure domain | `zo` living thing | `su` structure/organization | `da-zo` | proposed | anatomy, cell biology |
| `da-zo-to` | Life-information domain | `zo` living thing | `to` pattern/encoding | `da-zo` | proposed | genetics, bioinformatics |

---

## Information and Computation

| Label | Name | Substrate | Principle | Parent | Status | Notes |
|-------|------|-----------|-----------|--------|--------|-------|
| `da-to-ki` | Computation domain | `to` information/pattern | `ki` transformation/process | `da-to` | proposed | computing broadly |
| `da-to-su` | Memory domain | `to` information | `su` storage/retrieval | `da-to` | proposed | data storage, recall |
| `da-si-ne` | Communication domain | `si` signal | `ne` transfer/relation | — | proposed | networks, language |
| `da-to-fe` | Logic domain | `to` pattern | `fe` formal reasoning/boundary | `da-to` | proposed | mathematics, formal systems |

---

## Social and Human

| Label | Name | Substrate | Principle | Parent | Status | Notes |
|-------|------|-----------|-----------|--------|--------|-------|
| `da-li-ne` | Social domain | `li` person | `ne` relation/structure | `da-li` | proposed | society, governance |
| `da-to-ki-li` | Knowledge-transfer domain | `to` knowledge | `ki-li` teaching/learning | `da-to` | proposed | education |
| `da-vo` | Value domain | `vo` value | `vo` judgment/comparison | — | proposed | ethics, aesthetics |

---

## Mystic / Resonance

This domain covers mystic phenomena in the Concordia setting: resonance between will and physical systems, structured intentional practice, anomalous signal phenomena, and perceptual states beyond ordinary cognitive processing. **Proposed, not yet required.** The corpus test S072–S078 confirmed that all core mystic concepts compose from existing primitives. The domain label is reserved for use as a register/qualifier rather than as a semantic reboot.

| Label | Name | Substrate | Principle | Parent | Status | Notes |
|-------|------|-----------|-----------|--------|--------|-------|
| `da-wi-ra` | Resonance domain | `wi` will/intention | `ra` force/energy | — | proposed | mystic practices, will-resonance, ritual, perception-states; NOT evidence for a new primitive yet |

Core compounds already functioning in this domain (all from S072–S078):

| Compound | Meaning | Notes |
|----------|---------|-------|
| `pa-ra` | field (spatial energy distribution) | physics term, also mystic field |
| `wi-ka-su` | ritual | organized intentional-action structure |
| `fe-su` | ward / protective barrier | constructed boundary |
| `zo-se-ki` | entering trance | organism-perception state transition |
| `ti-mu` | relic | time-artifact (characterized by temporal depth) |
| `fe-no-ka` | forbidden boundary | prohibition encoded as boundary property |
| `se-to` | vision / perceptual insight | concept arising from direct perception |

**Primitive threshold conditions:** a mystic primitive becomes justified when three or more attested corpus sentences produce genuinely misleading readings using existing roots, and no compound resolves the ambiguity. Current watch: S075 `la-wi-ze  ka  lo-mu` (will-as-agent vs will-as-instrument ambiguity). See notes/open-questions.md.

---

## Religion / Doctrine

Religious constructs in Tonesu are treated as organized social and epistemic structures, not supernatural ontological primitives. The domain uses `to` (conceptual pattern), `re` (recurrence/tradition), `su` (organization), and `fe` (sacred boundary). **The key cultural finding from corpus testing (S079–S085): Concordian "priest" (`to-su-li`) is structurally identical to librarian/archivist.** Religious authority and knowledge authority are the same institution in this grammar.

| Label | Name | Substrate | Principle | Parent | Status | Notes |
|-------|------|-----------|-----------|--------|--------|-------|
| `da-to-re` | Doctrinal domain | `to` knowledge/pattern | `re` recurrence/preservation | `da-to` | proposed | religion, tradition, canon; doctrine as recurring organized knowledge |

Core compounds from the religious probe S079–S085:

| Compound | Meaning | Notes |
|----------|---------|-------|
| `wi-si` | prayer / will-signal | intentional signal whose content is the will itself |
| `to-re-su` | canonical doctrine / scripture | organized recurring knowledge |
| `fe-vo` | sacredness | boundary-protected value; the quality of being set apart |
| `pa-wi-ka-su` | shrine / temple | place defined by its role as a ritual institution |
| `ne-ra` | resonance / energetic coupling | relational energy state; resolves S075 will-agent ambiguity |
| `ne-ra-ki` | to attune | inchoative: entering the resonance state |
| `zo-to` | soul / identity-pattern | living-pattern; the organizing conceptual structure of a living entity |
| `zo-si` | spirit / disembodied agent | living-signal; an agent whose existence is signal without physical substrate |

**`zo-si` vs `zo-to`:** not interchangeable. `zo-si` = entity without body (ghost, spirit as separate being). `zo-to` = the organizing pattern of a living entity's identity (soul as the conceptual structure of a person). A person has `zo-to`; a ghost *is* `zo-si`.

---

## Open Questions

- [ ] Several entries have substrate == principle (e.g. `da-su`). Review whether this is meaningful or an artifact of placeholder design.
- [ ] `da-to-ki-li` is four elements deep — likely too long. Needs a better construction.
- [ ] Establish short labels (Stage 3 forms) for the domains expected to be highest-frequency
- [ ] Review whether `da-si-ne` (communication) has a clear parent or remains freestanding
