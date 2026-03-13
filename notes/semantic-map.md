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
| memory | knowledge | containment | `to-ko` (knowledge-containment) — *Note: was incorrectly listed as `to-su`; `to-su` = organized knowledge, not memory* |
| learning | knowledge | change | `to-ki` (knowledge-change) |
| perception system | perception | structure | `se-su` |
| energy system | energy | structure | `ra-su` |
| tool | object | action/cause | `mu-ka` |
| language | signal | structure | `si-su` |
| mind | knowledge + will | agent | `to-wi-li` or `to-li`? — *pending* |

---

## Cultural Precision Domains

These are the semantic fields where Tonesu invests in finer distinctions than most natural languages. Each domain represents a cultural claim: Concordia cares enough about these concepts to name them precisely.

---

### Domain 1: Epistemic States

English collapses: know / think / feel / remember / perceive / ask.
Tonesu draws at least seven distinct states:

| Form | Meaning | Distinction |
|------|---------|-------------|
| `se` | raw sensory detection | pre-cognitive; not yet processed |
| `si` | encoded representation | symbolized; externalized information |
| `to` | conceptual pattern / knowledge | processed, understood; internal model |
| `to-su` | organized structured knowledge | systematized body of knowledge |
| `to-ko` | retained knowledge | persisting knowledge; memory |
| `to-si` | knowledge-seeking signal | query; reaching toward knowledge |
| `to-su-ki` | entering organized understanding | comprehension; the threshold moment |

**Cultural claim:** The epistemic status of information matters. There is a categorical difference between detecting (`se`), encoding (`si`), understanding (`to`), and systematizing (`to-su`). An unsupported claim is not an encoded fact is not an integrated model. Concordian speakers are expected to track these distinctions — passing off `se` as `to` is epistemically dishonest in a way the language makes explicit.

---

### Domain 2: Deliberateness of Change

English collapses: do / make / happen / grow / break down / move.
Tonesu distinguishes by *source and intentionality*:

| Form | Meaning | Distinction |
|------|---------|-------------|
| `ka` | deliberate intentional act | agent chose to do it |
| `be` | growth / emergence | may be non-intentional; organic increase |
| `de` | decay / dissolution | entropic decrease; may be non-intentional |
| `ki` | physical motion | displacement; no intentionality implied |
| `wi` | will / purpose | the intended goal; distinct from the act itself |

**Cultural claim:** Whether change was intended matters. `ka-be` (build deliberately) differs from bare `be` (something grew). Harm from `de` (entropy) differs from `ka-de` (deliberate destruction). Accountability — and the difference between accident and intent — is built into the root vocabulary.

---

### Domain 3: Agency Ontology

English handles "agent" vaguely across biology, intention, and social participation.
Tonesu's entity roots establish a precision hierarchy:

| Form | Category | Requires |
|------|----------|---------|
| `zo` | living organism | biological life only |
| `li` | social agent | intentionality + social participation |
| `zo+li` | person | both: biologically living intentional agent |
| `mu+li` | non-biological intentional agent | intentionality without organic life |
| `zo` (no `li`) | animal / creature | life without social agency |

**Cultural claim:** Biology and intentional agency are independent dimensions. A Concordian speaker is never confused by "is it alive?" versus "does it have intentions?" — these are separate questions with separate vocabulary. This anticipates AI, institutions, and hybrid entities as first-class concepts rather than edge cases.

---

### Domain 4: Limits and Thresholds

English fragments: danger / warning / edge / limit / boundary / threshold / deadline / category.
Tonesu *consolidates* under `fe` (boundary/limit):

| Form | Meaning |
|------|---------|
| `fe` | boundary / limit / category edge / threshold |
| `fe-si` | warning (a signal that a boundary exists or is being approached) |
| `fe-ki` | reach a limit; arrive at a boundary |

**Cultural claim:** Danger *is* a limit. A warning *is* a limit-signal. Tonesu does not distinguish "bad things that may happen" from "boundaries being approached" — these are the same phenomenon. Concordia frames risk as boundary-proximity, not harm-potential. This is a philosophical stance baked into the lexicon.

*Expansion direction (unregistered):* types of limits by domain — physical (`ra-fe`), ethical (`wi-fe`), epistemic (`to-fe`), temporal (`ti-fe`). Register when corpus demands it.

---

### Domain 5: Signal Mechanism and Direction

English collapses: tell / send / warn / ask / broadcast / show / communicate.
Tonesu splits by mechanism, directionality, and content type:

| Form | Meaning |
|------|---------|
| `so` | acoustic signal (spoken, heard) |
| `lu` | visual signal (shown, seen) |
| `si` | any encoded representation — the base class |
| `si-ki` (W023) | directed point-to-point transmission (outward) |
| `si-ne-ki` (W021) | networked communication (relational, broadcast) |
| `fe-si` (W024) | warning signal (content: limit-boundary) |
| `to-si` (W026) | query signal (content: knowledge-seeking, inward) |

**Cultural claim:** *How* a signal travels and *what it carries* are both semantically relevant. You do not simply "tell" someone something — the transmission method and content type are distinct dimensions. A civilization with complex communication infrastructure would track these differently.

---

### Meta-observation: Precision vs. Consolidation

Tonesu is not uniformly more precise than English — it is selectively precise in ways that reveal cultural priorities.

| Concordia is *more precise* than English about... | Concordia *consolidates* where English fragments... |
|--------------------------------------------------|-----------------------------------------------------|
| Epistemic states (7 gradations of knowing) | All boundary-types are one phenomenon (`fe`) |
| Deliberateness of change (4 roots + `wi`) | Worth, evaluation, and intensity are one root (`vo`) |
| Agency ontology (biology ≠ intentionality) | Sensation modalities (any `se` compound, not separate roots per sense) |
| Signal mechanism and direction | |

The pattern: Concordia invests precision where *accountability, epistemics, and agency* are in play. It consolidates where the distinction is a surface categorization rather than a deep one.

---

## Open Questions

- [ ] `to` appears in both Structure and Mind clusters — should it split into two roots?
- [ ] Where does "emotion" live? `vo` (value), `wi` (intention), or needs its own root?
- [ ] "Time" (`ti`) and "sequence" — are these one root or two?
- [ ] Does "space" (`pa`) cover abstract topology (e.g. mathematical space) or only physical location?
- [x] ~~Review `plu` — three-letter root is inconsistent with CV/CVC constraint~~ → **Resolved:** replaced with `pu`. See registry/primitives.md.
