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

## Open Questions

- [ ] Several entries have substrate == principle (e.g. `da-su`). Review whether this is meaningful or an artifact of placeholder design.
- [ ] `da-to-ki-li` is four elements deep — likely too long. Needs a better construction.
- [ ] Establish short labels (Stage 3 forms) for the domains expected to be highest-frequency
- [ ] Review whether `da-si-ne` (communication) has a clear parent or remains freestanding
