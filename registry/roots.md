# Root Registry

## Status: Draft

This is the formal semantic engine. Every primitive root and registered derivational marker lives here. It is the source of truth for the language's generative machinery.

For derived compounds and common words, see lexicon/derived.md.
For contracted everyday forms, see lexicon/colloquial.md.

---

## Primitive Roots

*(See ontology/primitives.md for full definitions. This registry is the quick-reference format.)*

| ID | Root | Gloss | Class | Domain |
|----|------|-------|-------|--------|
| R001 | `mu` | object / artifact | entity | general |
| R002 | `ma` | matter / substance | entity | general |
| R003 | `li` | person / agent | entity | general |
| R004 | `zo` | living thing | entity | general |
| R005 | `ki` | motion / change | process | general |
| R006 | `ka` | intentional action | process | general |
| R007 | `be` | growth / creation | process | general |
| R008 | `de` | decay / dissolution | process | general |
| R009 | `su` | structure / order | structure | general |
| R010 | `to` | pattern / knowledge | structure | general |
| R011 | `fe` | boundary / category | structure | general |
| R012 | `ne` | relation / connection | relation | general |
| R013 | `pe` | part / component | relation | general |
| R014 | `go` | cause / origin | relation | general |
| R015 | `du` | result / effect | relation | general |
| R016 | `pa` | place / space | space-time | general |
| R017 | `di` | direction | space-time | general |
| R018 | `ti` | time / sequence | space-time | general |
| R019 | `re` | repetition / cycle | space-time | general |
| R020 | `se` | perception / sense | signal | general |
| R021 | `so` | sound | signal | general |
| R022 | `lu` | light / visibility | signal | general |
| R023 | `si` | signal / representation | signal | general |
| R024 | `vo` | value / quality | mind | general |
| R025 | `wi` | will / intention | mind | general |
| R026 | `no` | negation / absence | operator | general |
| R027 | `nu` | quantity / number | quantity | general |
| R028 | `ru` | unity / singularity | quantity | general |
| R029 | `pu` | plurality / collective | quantity | general |
| R030 | `ra` | energy / force | force | general |
| R031 | `ko` | containment / interior | space | general |

---

## Grammatical Particles

| ID | Particle | Role | Notes |
|----|----------|------|-------|
| G001 | `la` | agent marker | precedes the agent NP |
| G002 | `lo` | patient marker | precedes the affected NP |
| G003 | `ra` | instrument/cause marker | precedes tool or reason |
| G004 | `pa` | location marker | precedes place NP |
| G005 | `ne` | recipient / relation | precedes beneficiary or target |
| G006 | `ta` | time reference | precedes temporal expression |
| G007 | `ka` | action marker | precedes verb root |
| G008 | `na` | proper name marker | precedes identifiers |
| G009 | `da` | domain marker | precedes domain label |

*Note: `la` (agent particle) is now phonetically distinct from `li` (person/agent root) — that collision is resolved. Remaining particles that overlap with roots (`ra`, `pa`, `ka`, `ne`) are lower priority and still under review.*

---

## Derivational Markers

| ID | Marker | Role | Attaches to | Example |
|----|--------|------|-------------|---------|
| D001 | `-li` | agent (one who does) | action, process root | build-li → builder |
| D002 | `-mu` | device / instrument | action, process root | build-mu → building tool |
| D003 | `-pa` | location | action, state root | build-pa → construction site |
| D004 | `-su` | result / state | action root | build-su → structure |
| D005 | `-to` | abstract concept | any root | build-to → concept of construction |
| D006 | `-se` | quality / property | entity or state root | energy-se → energetic |
| D007 | `-ki` | ongoing process (verbal noun) | action root | build-ki → the building (activity) |

---

## Open Questions

- [x] ~~Resolve particle/root phonetic collision for agent marker~~ → resolved: agent particle renamed `li` → `la`. Remaining overlaps: `ra`, `pa`, `ka`, `ne`.
- [ ] Add tense/aspect suffix IDs as formal markers
- [ ] Replace `plu` with a CV or CVC form to comply with syllable rules
- [ ] Assign final phonetic forms — current roots are placeholder assignments
