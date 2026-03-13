# Semantic Map

## Status: Draft

This file maps the relationships between primitive roots: which concepts are neighbors, which are parent/child, and which must remain distinct. It is the backbone that prevents root overlap and guides compound formation.

---

## How to Read This Map

- **Parent →** the root is a specialization of the parent concept
- **Neighbors:** semantically adjacent roots that must be carefully differentiated
- **Contrast:** roots that are explicitly NOT the same despite surface similarity

---

## Top-Level Ontological Clusters

```
EXISTENCE
├── Entity
│   ├── mu  (object/thing — inanimate)
│   ├── ma  (matter/substance — raw)
│   ├── li  (person/agent — conscious)
│   └── zo  (living thing — organic)
│
├── Event / Process
│   ├── ki  (motion/change)
│   ├── ka  (intentional action)
│   ├── be  (growth/creation)
│   └── de  (decay/dissolution)
│
├── Structure
│   ├── su  (structure/order)
│   ├── to  (pattern/thought/knowledge)
│   └── fe  (boundary/limit/category)
│
├── Relation
│   ├── ne  (connection/relation)
│   ├── pe  (part/component)
│   ├── go  (cause/origin)
│   └── du  (result/effect)
│
├── Space-Time
│   ├── pa  (place/space)
│   ├── di  (direction)
│   ├── ti  (time/sequence)
│   └── re  (repetition/cycle)
│
├── Perception / Signal
│   ├── se  (perception/sense — general)
│   ├── so  (sound)
│   ├── lu  (light/visibility)
│   └── si  (signal/representation)
│
├── Mind / Will / Value
│   ├── to  (knowledge/pattern — also in Structure)
│   ├── wi  (will/intention)
│   └── vo  (value/quality)
│
├── Quantity
│   ├── nu  (quantity/number)
│   ├── ru  (unity/singularity)
│   └── plu (plurality/collective)
│
└── Force
    └── ra  (energy/force)
```

---

## Critical Distinctions

These pairs are the most likely sources of ambiguity. Their boundaries must be explicitly maintained.

| Root A | Root B | Distinction |
|--------|--------|-------------|
| `ki` (change) | `ka` (action) | `ki` is change — may be passive or physical. `ka` is intentional, agentive action. |
| `su` (structure) | `to` (pattern) | `su` is physical/organizational arrangement. `to` is abstract model, idea, or knowledge. |
| `se` (perception) | `to` (knowledge) | `se` is raw sensory input. `to` is processed, understood information. |
| `si` (signal) | `so` (sound) | `si` is any encoded representation. `so` is specifically acoustic. |
| `ma` (matter) | `mu` (object) | `ma` is unformed substance. `mu` is a formed, usable artifact. |
| `go` (cause) | `ki` (change) | `go` is the source or reason. `ki` is the change event itself. |
| `be` (creation) | `ka` (action) | `be` is emergence/growth, which may be non-intentional. `ka` is deliberate act. |
| `wi` (intention) | `ka` (action) | `wi` is the goal state. `ka` is the actual operation. |
| `vo` (value) | `to` (knowledge) | `vo` is evaluative/qualitative. `to` is descriptive/structural. |
| `ne` (relation) | `pe` (part) | `ne` is a link between peers. `pe` is a component inside a whole. |

---

## Compounds That Cross Clusters

Some compound concepts naturally span clusters. Document these explicitly to prevent competing constructions.

| Concept | Cluster A | Cluster B | Preferred construction |
|---------|-----------|-----------|----------------------|
| communication | signal | relation | `si-ne` (signal-relation) |
| memory | knowledge | structure | `to-su` (pattern-structure) |
| learning | knowledge | change | `to-ki` (knowledge-change) |
| perception system | perception | structure | `se-su` |
| energy system | energy | structure | `ra-su` |
| tool | object | action/cause | `mu-ka` |
| language | signal | structure | `si-su` |
| mind | knowledge + will | agent | `to-wi-li` or `to-li`? — *pending* |

---

## Open Questions

- [ ] `to` appears in both Structure and Mind clusters — should it split into two roots?
- [ ] Where does "emotion" live? `vo` (value), `wi` (intention), or needs its own root?
- [ ] "Time" (`ti`) and "sequence" — are these one root or two?
- [ ] Does "space" (`pa`) cover abstract topology (e.g. mathematical space) or only physical location?
- [ ] Review `plu` — three-letter root is inconsistent with CV/CVC constraint; candidate replacement needed
