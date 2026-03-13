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

**Social consequences of epistemic mislabeling:**

| Context | Act | Label | Treatment |
|---------|-----|-------|-----------|
| Casual speech | "I know" when meaning "I think" | imprecision | Tolerated; register-appropriate reduction |
| Honest error | Genuinely confuses `se` with `to` | `to-fe-ki` (boundary-crossing by motion, neutral) | Correctable; low social cost |
| Formal discourse, deliberate | Knowingly presents `se` as `to` | `to-fe-ka` (boundary-crossing by intentional action) | Epistemic fraud; equivalent to perjury in high-stakes contexts |

The `ki`/`ka` distinction (Domain 2) does the accountability work: the language forces the speaker to commit to whether a boundary-crossing was accidental or deliberate. There is no convenient grammatical ambiguity between honest error and fraud.

**Political register — how Concordian discourse handles epistemic categories strategically:**

Direct lies (`to-fe-ka` inflation) are politically dangerous because the mislabeling is visible and assertive. The dominant political maneuver instead becomes *category management*: argumentation about which epistemic level applies, rather than false claims about content.

| Political move | Mechanism | Epistemic label used |
|----------------|-----------|---------------------|
| Claim suppression | Downgrade `to-su` to `si`: "this is only a report" | Deflation `to-fe-ka` — harder to prove; requires showing what status the claim had actually reached |
| Uncertainty projection | Correctly label `si` while implying it is not worth acting on | Technically honest; politically manipulative |
| Strategic precision | Use `to` carefully: "we believe" rather than "it is established" | Stays within bounds; pressure toward epistemic transparency |
| Formal accusation | Challenge opponent's category assignment before a `to-fe-li` panel | "Your claim never crossed the `to-fe` boundary" |

The irony Monday's analysis identified: a language with precise epistemic vocabulary doesn't eliminate political manipulation; it *formalizes* it. Political argument in Concordia looks like academic peer review. The moderator's question — "Is your claim `si`, `to`, or `to-su`?" — is a realistic institutional procedure, not an absurdity.

**Note:** English frames dishonesty as a *moral* failure (lying is wrong). Tonesu frames it as a *structural* failure — violating a category boundary. This uses the same `fe` root as physical danger and warnings. Concordia's ethics and its risk-management framework are the same ontology. Intellectual dishonesty is not a separate moral domain; it is a species of boundary violation.

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

### Domain 6: Epistemic Accountability Roles

The five domains above describe *vocabulary*. This domain describes the *institutional architecture* that vocabulary implies.

If Concordia distinguishes `to-fe-ki` (honest epistemic error) from `to-fe-ka` (deliberate fraud), then some mechanism must exist for making that determination formally. That mechanism requires a recognized class of agents whose social authority is adjudicating epistemic claims. The vocabulary did not create this institution; it revealed that the institution must already have existed for the vocabulary to carry social weight.

| Role | Form | Distinction |
|------|------|-------------|
| Knower / scholar | `to-li` (W003) | produces knowledge; primary relationship to `to` is research |
| Knowledge organizer | `to-su-li` | maintains structured knowledge systems; librarian/archivist |
| Epistemic guardian | `to-fe-li` (W032) | adjudicates epistemic claims; authority over `to-fe`; certifies or contests category assignments |

**The asymmetric pair:** `to-fe-li` (uphold) / `to-fe-ka` (violate) — same root triple, structurally opposite social functions. The pair only makes sense together: the role exists because the violation is possible; the violation carries weight because the role exists.

**Institutional implication:** The body or framework within which `to-fe-li` operate would be `to-fe-su` (epistemic code / standards framework) — as yet unregistered. Register when corpus work produces a sentence that requires the institution, not just the agent.

**`to-fe-su` is structurally load-bearing, not optional:** The `to-fe-li` role can only adjudicate deflation charges objectively if `to-fe-su` defines epistemic promotion thresholds as a procedure. Without it, every deflation dispute collapses into "I judged the evidence insufficient" vs. "I say it was sufficient" — a stalemate, not an adjudicable charge. Deflation `to-fe-ka` can only be distinguished from legitimate conservative epistemic judgment (not a violation) if a procedural standard exists for what counts as sufficient evidence for `to-su` promotion. `to-fe-su` is what converts subjective threshold judgments into objective ones. The manufactured-doubt defense ("I was skeptical") fails when the standards body has certified that the threshold was met. See notes/open-questions.md.

**Connection to evidentiality (open question):** `to-fe-li` have the strongest functional need for evidential markers. Adjudicating a claim requires specifying *how* the arbiter established the true epistemic status. A `to-fe-li` who determines that a claim was `se` rather than `to` must be able to say: I established this by direct perception (`se-ro`), by received signal (`si-ro`), or by inference (`to-ro`). This is the clearest use case for evidentiality — and the reason the question should be left open until a corpus sentence involving adjudication makes the need concrete.

**The self-legitimation problem (quis custodiet):** If `to-fe-su` certifies epistemic claims, who certifies `to-fe-su`? The Concordian answer is not an external authority (infinite regress) but *self-application*: `to-fe-su`'s own rules are themselves published to `to-su` status — openly systematized, challengeable, revisable through the same `to-fe-li` + `to-fe-su` process they define. The circularity is intentional: the system bootstraps legitimacy through transparent, revisable procedure rather than external sanction, the same way scientific methodology is validated by track record and openness to revision rather than by a higher authority.

The practical consequence: a `to-fe-su` body that made its own rules unchallengeable would be committing `to-fe-ka` on its own standards — suppressing the epistemic status of a meta-level claim. Any `to-fe-li` could adjudicate that. The recursion is stable because the meta-level rules are subject to the object-level procedure.

Vocabulary gap this exposes: there is currently no distinction between a `to-fe-su` ruling that is internal and one that has been published to `to-su` status and is therefore openly challengeable. A standard that has been adopted but not yet published is distinguishable from a standard that has been certified as meeting its own criteria. That distinction is where institutional capture would show up. Flagged in notes/open-questions.md.

**The binding principle — unpublished rules cannot bind:** A constitutional principle that falls directly from the ontology without new vocabulary. If legitimacy comes from surviving the epistemic pipeline (from `si` → `to` → `to-su`), then a rule that has not been published to `to-su` status has not achieved the epistemic status required to make binding claims on others. Enforcing an unpublished standard is structurally identical to `to-fe-ka` deflation at the meta-level: the rule-maker is treating an internal adoption (`si`) as if it had the authority of established knowledge (`to-su`), while withholding the publication that would make it challengeable. Any `to-fe-li` could adjudicate this as meta-level inflation.

Concordian constitutional consequence: power does not come from hierarchy or secrecy. It comes from surviving public scrutiny. Unpublished standards are epistemically illegitimate by the same logic that makes ordinary `to-fe-ka` a violation — and for the exact same reason. No new vocabulary required; the existing framework covers it.

**`to-fe-su-ki` as constitutional event:** The transition from internal adoption to published `to-su` status (`to-fe-su-ki`, the inchoative) is the moment when authority becomes legitimate. Before `to-fe-su-ki`: the body has power but not legitimacy. After `to-fe-su-ki`: the standard is published, challengeable, and binding. The political consequence is that Concordia's most contested institutional space is not legislative votes but the timing and execution of publication — the ceremony that converts internal decisions into legitimate authority. Battles over *when* `to-fe-su-ki` occurs are battles over legitimacy itself.

---

## Open Questions

- [ ] `to` appears in both Structure and Mind clusters — should it split into two roots?
- [ ] Where does "emotion" live? `vo` (value), `wi` (intention), or needs its own root?
- [ ] "Time" (`ti`) and "sequence" — are these one root or two?
- [ ] Does "space" (`pa`) cover abstract topology (e.g. mathematical space) or only physical location?
- [x] ~~Review `plu` — three-letter root is inconsistent with CV/CVC constraint~~ → **Resolved:** replaced with `pu`. See registry/primitives.md.
