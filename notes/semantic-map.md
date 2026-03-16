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
│   ├── ki  (motion)
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
│   ├── du  (result/effect)
│   └── zi  (mutual coupling event)
│
├── Space
│   ├── pa  (place/space)
│   ├── di  (direction)
│   └── ko  (containment/interior)
│
├── Time
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
│   └── pu  (plurality/collective)
│
├── Force
│   ├── ra  (energy/force)
│   └── ha  (heat/thermal state)
│
└── Organism State
    └── fa  (affective substrate — inward felt-tone of the organism)
```

*Substrate symmetry: `ha` is the thermal-state complement to `ma` (matter); `fa` is the interior-state complement to `zo` (organism). Both are irreducible properties of their substrate class — not reducible to perception (`se`), cognition (`to`), or evaluation (`vo`). Added March 2026.*

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
| `fa` (affect) | `se` (perception) | `fa` is inward-facing organism state (mood substrate, arousal, valence). `se` is outward-facing detection of the world. A chemically depressed person has active `fa` with no active `se` target. |
| `fa` (affect) | `vo` (value) | `fa` is pre-evaluative substrate — affect rises before any value judgment occurs. `fa-be` (affect increasing) with no `vo` modifier is valid and common. |
| `fa` (affect) | `to` (knowledge) | `fa` is the middle stage of the `se → fa → to` pipeline; affect can activate without producing a cognitive model (`fa-no-to` = affect without cognition). |
| `ne` (relation) | `pe` (part) | `ne` is a link between peers. `pe` is a component inside a whole. |
| `ra` (energy) | `ha` (heat) | `ra` is energy as force or capacity (electrical charge, kinetic force, structural load). `ha` is the thermal state of matter. A frozen conductor carrying high current has high `ra` and low `ha` simultaneously — they are orthogonal. `ra-de` = power failure; cold = `no-ha`. |

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
| mathematics | pattern/knowledge | structure + relation | `to-su-ne` (conceptual structural relation) |
| dimension / parameter / axis | quantity | conceptual pattern | `nu-to` (quantitative concept) |
| equation | conceptual pattern | relation | `to-ne` (conceptual relation) |
| proof | conceptual pattern | cause → result chain | `to-go-du` (causal conceptual chain) — *note: this may be the most natural use of the `go`/`du` pair in the whole language; worth a dedicated corpus stress test* |
| algorithm / procedure | conceptual pattern | intentional action + structure | `to-ka-su` (procedural conceptual structure) |
| field (physics) | energy | relation | `ra-ne` (energy relations) |
| wave | energy | cycle/repetition | `ra-re` (cyclical energy) |

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

## Emergent Cultural Orientation

Languages with clean ontologies produce emergent cultural properties. These are not designed — they are consequences of the category commitments made when the primitives were chosen. The ones below emerge from Tonesu's structure without any deliberate intent.

Many of Monday's proposed properties are already partially captured in the Domains above. This section records the full picture systematically, cross-references what is already documented, and adds the observations that are new.

### Already documented in the Domains

| Property | Basis | Location |
|----------|-------|----------|
| Accountability culture — causal responsibility is linguistically foregrounded | `ka` / `be` / `de` split forces speaker to specify intentionality of every event | Domain 2: Deliberateness of Change |
| Knowledge pipeline thinking — knowledge as developmental stages | `se → si → to → to-su → to-ko` epistemic ladder | Domain 1: Epistemic States |
| Boundary ethics / safety culture — risk as limit-proximity | `fe` consolidates all boundary types | Domain 4: Limits and Thresholds |
| Agency clarity — biology and intentionality are orthogonal | `zo` / `li` / `mu+li` separation | Domain 3: Agency Ontology |
| Institutions around knowledge — vocabulary implies epistemic governance | `to-fe-li` / `to-fe-su` emerge from the epistemic ladder | Domain 6: Epistemic Accountability Roles |
| Conflict as peer review — disputes are category-level, not assertion-level | `to-fe-ka` / `to-fe-ki` / `to-fe-li` frame arguments as epistemic classification | Domain 6 |
| System naming culture — formal compounds vs. colloquial compression | `to-ki-mu` → `to-ko` compression pattern | spec/morphology.md § Casual Register |

### New properties (not yet documented)

**Event-based worldview.** Relations are expressed as processes (`ne-ki` = become-connected) rather than static states. The inchoative slot (`ROOT + ki`) converts every quality into a transition event. A Concordian speaker does not say "they are connected" — they say "connection occurred." The implication: stability is a *result* that is maintained, not a default state that persists. Systems are always either consolidating or dissolving. Rest is a special case of motion. This shapes how Concordia thinks about infrastructure, institutions, and relationships: they are all things that must be actively sustained, not things that simply exist.

**Repair mindset.** The primitives emphasize processes (`ki`, `ka`, `be`, `de`), structures (`su`, `fe`, `ne`), and transitions — not terminal states. English asks "who broke this?" Concordian structure pushes toward "where did the process cross the boundary?" (`fe`), and then "how do we reverse the decay?" (`de-be`). Blame-assignment is structurally harder than root-cause analysis. This is not a moral claim; it is a grammatical affordance.

**Clear but slightly austere register.** The precision investment (epistemic status, agency, causation, thresholds) comes at a cost: the categories that get *consolidated* — sensation modalities (`se` covers all senses), evaluative nuance (one root `vo`), aesthetic registers — are exactly the vocabulary that expressive and poetic registers rely on. Concordian speech will be precise where accountability is in play and relatively sparse where purely emotional or aesthetic expression is needed. This is not a deficiency; it is a reflection of priorities. The language can grow in those directions through compounding — but the primitives do not bias toward them.

---

### Hidden Properties in the Primitive Root Set

These four properties are not obvious from individual roots but emerge from the *structure* of the root set as a whole.

---

#### Hidden Property A: Bilateral causation

Most languages have a causal *relation* — a particle or construction that links cause to effect. Tonesu went further: `go` (cause/origin) and `du` (result/effect) are *both primitive*. They are separate ontological categories, not a single causal relation.

The consequence: every causal event has two obligatory slots. You can name a cause without naming the result (`go {X}`) — but the grammar is then incomplete in a way that invites completion. Similarly, naming a result invites the question of what `go` produced it.

This creates what might be called **double-entry causation**: a culture where naming a cause without tracing its result, or naming a state without asking what produced it, feels like an incomplete account. Post-incident reports are not supplementary — they are the natural completion of every sentence that names a cause. Impact analysis is not an extra step — it is what `du` is waiting for.

The corpus already confirms this: S011, S013, and S027 all use `go`/`du` framing not as explicit causal particles but as the default way to structure explanations. The bilateral structure emerges naturally.

---

#### Hidden Property B: Repetition is ontologically primitive

`re` (repetition/cycle) could have been derived — "the same thing in sequence" = `ti + ru + ki` or similar. It was not derived; it is primitive. This is a commitment: pattern-identity across time is a *fundamental* category, not something you infer from sequences of events.

What this means: when a Concordian observes a pattern — the same failure mode appearing again, the same political maneuver being used, the same cycle in a system — they are not doing secondary reasoning ("I notice X has occurred repeatedly"). They are naming a primitive ontological fact: `re`.

Cultural consequence: **historical pattern recognition is native**, not a specialized skill. A civilization that treats repetition as primitive will develop strong historiography, institutional memory, and cycle-awareness. Process improvement isn't "we should learn from mistakes" — it's a natural response to naming that the pattern `re` is present. Conversely, false analogies — claiming `re` where the pattern is superficial — become a specific recognizable error (a species of `to-fe-ka` applied to time).

The `re` primitive also sets up a future distinction between `ti` (time as sequence) and `re` (the recurrence of pattern within time) that most natural languages conflate. Concordia can ask "is this the same thing happening again, or merely the next event in a sequence?" as a grammatically natural question.

---

#### Hidden Property C: Value is irreducible

`vo` (value/quality) cannot be defined in terms of utility (`mu-ki`), scarcity (`nu + de`), survival advantage (`zo-be`), social consensus (`li-ne-to`), or any other compound. It is a primitive. The language treats evaluative facts as a fundamental category.

This is a form of **built-in value realism**: the claim that things genuinely have evaluative properties that are not derived from other facts. A Concordian speaker who says "this has high vo" or "ka-vo-de" (deliberate destruction of value) is making an ontological commitment that cannot be dissolved into pragmatics.

The consequence: ethical discourse in Concordia cannot be easily dismissed as "just subjective opinion" or "just social preference." You can argue about what `vo` a thing has — but arguing that `vo` doesn't exist as a category is like arguing that `ma` (matter) doesn't exist. The language doesn't support that move.

This is especially significant paired with Domain 2 (Deliberateness): `ka-vo-de` (intentionally destroying value) is a grammatically coherent claim that carries the same accountability weight as `ka-de` (intentionally causing decay). The moral and the causal use the same framework.

What `vo` consolidates that English distinguishes: beauty, worth, ethical value, quality, intensity. These are all `vo` in Tonesu. Whether that consolidation was wise — or whether Concordia will eventually need `vo-se` (perceived quality), `vo-li` (ethical value, agent-dependent), and `vo-su` (objective systematic worth) — is an open question.

---

#### Hidden Property D: Unity and plurality are qualitative, not quantitative

The quantity cluster has three primitives: `nu` (quantity — how much, measurable), `ru` (unity — one-ness as a qualitative property), `pu` (plurality — many-ness as a collective property).

Most languages that have quantity vocabulary treat "one" as just `nu = 1` and "many" as `nu > 1`. Tonesu separated the qualitative dimension (wholeness, coherence, collectivity) from the quantitative dimension (count, measure). This means:

- `ru-su` = a *unified* system (coherent as a whole) ≠ `nu-su = 1` (there is one structure; count of one)
- `li-pu` = a *collective* of persons (social collectivity) ≠ `nu-li = 12` (twelve people; count)

The individual-collective tension — the fundamental tension of political philosophy — is built into the primitive set at the ontological level, not left to emerge from political vocabulary. **Concordia has a native, philosophically precise vocabulary for cohesion and fragmentation.**

Practical consequences:
- "The network is unified" (`ne-su-ru`) is a different claim from "there is one network" — the former asserts coherence, the latter asserts count
- "The community" (`li-pu`) is a qualitative collective entity with emergent properties; not merely "many li"
- Arguments about whether something is truly `ru` (a single coherent thing) vs. merely `nu = 1` (one thing by count) become natural and important — relevant to institutions, composite systems, political bodies

This precision likely produces a culture that is philosophically sophisticated about collective identity: when does a group of people become a community? when does a collection of components become a system? These are `ru`/`pu` vs. `nu` questions, and they are primitive enough to be asked fluently.

---

#### Hidden Property E: Model-reality stratification — the language has two ontological layers

Tonesu did not design a distinction between world and model. It inherited one from the primitive set: `su` (structure in the world) and `to` (conceptual pattern / model) are separate roots from the start. The consequence is that the language has **two ontological layers** with an explicit boundary between them, and the epistemic pipeline runs from world to model in one direction.

```
WORLD LAYER          su  (physical/organizational structure)
                     ↑ perception pipeline
PERCEPTION           se → si → to
                     ↑ (bottom layer: raw event)
EVENTS               ki, ka, be, de, go
─────────────────────────────────────────
MODEL LAYER          to  (conceptual pattern / interpreted model)
                     to-su  (organized knowledge)
                     to-go  (hypothetical causal model)
                     to-fe  (epistemic threshold / knowledge boundary)
                     to-ko  (retained knowledge / memory)
```

The pipeline flows one way. You can move from `se` toward `to`; but `to` does not automatically update `su`. Models can be wrong; structures just are. This is not the same as epistemological skepticism — the world layer exists and is accessible to perception — it is an ontological commitment that **knowing** something is a different category of fact from **the thing existing**.

**The three causal levels** (observed after CF-001):

| Form | Domain | Meaning |
|------|--------|---------|
| `go {X}  Y` | world | X causes Y (real-world causal assertion) |
| `to-go {X}  Y` | model | in the hypothetical model, X entails Y (model causation; non-actual) |
| `la-X  to  {to-go {X}  Y}` | epistemic | agent X asserts the counterfactual model |

This is a stratified causal ontology: physical causation, model causation, and attributed causal claim are formally distinct. English uses the same causal vocabulary for all three. Tonesu separates them.

**The model grammar subsystem** (all built without new primitives):

| Form | Meaning |
|------|---------|
| `to` | conceptual model / interpreted pattern |
| `to-su` (W013) | organized body of knowledge |
| `to-fe` (W028) | epistemic threshold (required evidence for promotion) |
| `to-ko` (W006) | retained knowledge / memory |
| `to-si` (W026) | query signal (reaching toward knowledge) |
| `to-go` (W089) | hypothetical causal frame (model causation) |
| `to  lo-{model}  be` | model-domain scope open (activates multi-sentence model frame) |
| `to  lo-{model}  de` | model-domain scope close (symmetric; explicit close) |
| `la-X  to  lo-{model}  be` | attributed model-domain scope (X opens the frame) |

This subsystem coheres as a complete architecture for reasoning about knowledge. The language has grown a philosophy of science vocabulary from two roots (`to` and the available compound space) without deliberate design.

**Why Path A felt wrong for counterfactuals** (the CF-001 diagnostic made this precise):  
`la-mi  to  {go {...}}` = "I assert the model." That is an epistemic action by a person.  
`to-go {X}  Y` = "in the model, the causal chain holds." That is a description of a model.  
The first introduces a *speaker stance* where none is needed. The distinction maps exactly onto the model/epistemic stratification: model-truth (`to-go`) and attributed-model-truth (`la-X  to  {to-go}`) are semantically distinct operations.

**What this means for Concordian intellectual culture:** The layered structure supports scientific reasoning in the technical sense — the ability to reason *about* models as objects, separately from reasoning about the world. A Concordian speaker can say "in the model, X causes Y" (`to-go {X}  Y`) without claiming X causes Y in reality, and can attribute the model to an assertion-holder (`la-X  to  {to-go {X}  Y}`) without claiming the model is correct. All three levels are grammatically distinguishable without any new primitives.

**Open pressure:** the model layer currently has no explicit *frame-setter* for discourse about a model. You can assert `to-go {X}  Y` (a single counterfactual), but you cannot yet open a discourse scope with "speaking within the model of the reactor..." or "according to the theory..." as a sustained frame. This appeared naturally in the CF-001 diagnostic but was deferred. See Open Questions.

---

### Domain 7: Emotional and Experiential States

**Design decision (locked, March 2026):** Tonesu does not use emotional primitive roots. Concordian culture frames emotional states as reportable system diagnostics — processual descriptions of internal state transitions — rather than as primitive expressive acts. See spec/principles.md § 9.

This means emotional vocabulary in Tonesu is always built, never given. The two roots involved are `se` (outward-facing detection — perceiving something specific) and `fa` (inward-facing affective substrate — the felt-interior tone of the organism, complete without an object). `se` constructions are culturally expected to specify an object; `fa` constructions are complete without one — the substrate itself is the full statement.

| Emotional state | `se` form (object-directed) | `fa` form (substrate, no object needed) | Notes |
|-----------------|-----------------------------|-----------------------------------------|-------|
| Fear / threat-response | `la-mi  se  fe-de  lo-{X}` | `la-mi  fa  fe-de` | `se` requires object; `fa` = free-floating dread, no target |
| Joy / positive-valence | `la-mi  se  vo-be  lo-{X}` | `la-mi  fa  vo-be` | `fa` = undirected positive affect, mood lift |
| Grief / loss | `la-mi  se  vo-de  lo-{X}` | `la-mi  fa  vo-de` | `fa` = pervasive low / depression-like state |
| Grief, persistent | — | `la-mi  fa  vo-de  re` | `re` (repetition) = sustained low without identifiable cause |
| Anxiety | `la-mi  se  fe-ki  lo-{X}` | `la-mi  fa  fe-ki` | `fa` = free-floating anxiety, no specific threat |
| Unresolved affect | — | `fa-no-to` (W090 equiv.) | felt state with no model at all — see W090 |
| Emotional numbness | — | `fa-no` | substrate absent / flat |
| Affect rising | — | `fa-be` | mood lifting, arousal increasing |
| Affect fading | — | `fa-de` | affect diminishing, dissipating |
| Observer mode | — | `la-mi  to  {la-zo-mi  fa  lo-X}` | I model that my organism's affective state is X — the SSRI/dissociation construction |
| Fatigue | `la-zo-mi  de` | — | bodily resource depletion — organism (`zo`), not affect (`fa`) |
| Hunger | `la-zo-mi  de  lo-ra` | — | energy deficit — bodily, not affective |
| Too cold | `la-zo-mi  se  no-ha` | — | thermoreceptor detection — `se` correct here, external signal |
| Too hot | `la-zo-mi  se  ha-fe` | — | thermal threshold — same |
| Comfort / ease | `la-zo-mi  ru` | — | organism coherence — structural state, not affective tone |
| Trust | `la-mi  se  vo-ne  lo-{person}` | — | always object-directed; no bare substrate form |
| Desire / longing | `la-mi  wi  lo-{X}` | — | `wi` (intention) — directed by definition |

**Cultural note:** `se` constructions are culturally expected to name *what* is feared, valued, or desired. Bare `la-mi  se  vo-be` without an object is grammatically complete but culturally thin — like saying "signal received" without content. `fa` constructions are the inverse: they are complete *without* an object by design. `la-mi  fa  vo-de` is not an incomplete grief statement; it is a precise substrate statement. Concordian culture accepts both registers without requiring object-specification for the `fa` form.

**The register gap and its narrative use:** When a Concordian speaker says `la-mi  se  fe-de  lo-ne-mi` and a non-Concordian hears it as "I'm afraid," that is the translation gap doing characterization work. The Concordian has specified (a) the type of emotional state, (b) the direction of change, and (c) the object. The non-Concordian compressed all three into a single opaque feeling-word. Neither is wrong; they are speaking different ontologies.

**What this is not:** Option B does not mean Concordians are emotionally flat, suppressed, or robotic. It means their emotional vocabulary is precise in the same way their epistemic vocabulary is precise. A Concordian who says `la-mi  se  fe-de  lo-ne-mi` is not being clinical — they are being accurate. The feeling is real and fully human. The framing is Concordian.

**Three distinct flavours of emotional expression and how the system handles each:**

The "awkward" judgment on Tonesu's emotional vocabulary is real but needs to be aimed more precisely. There are three distinct things people do when they "express emotion" and they are not all handled the same way:

| Flavour | Example | System status |
|---------|---------|---------------|
| **Reflective / relational** | "I'm afraid of losing this connection" | Handled well. `la-mi  se  fe-de  lo-ne-mi` is the Concordian form. May compress in casual register over time. |
| **Somatic / reactive** | "I'm cold", "I'm exhausted", "I'm in pain" | Handled well via `la-zo-mi` cluster. Pointing at the organism (`zo`) rather than the agent (`li`) captures the non-agentive quality of body-states correctly. These will compress earliest. |
| **Performative / expressive** | "Ugh." "Oh no." Sharp intake of breath. Crying. | **Not handled.** These are not propositional — they do not report an emotional state, they *are* an emotional act. They have no object and make no claim. The current spec has no register for this. |

The performative gap is the genuine source of awkwardness. The current system assumes all emotional expression is a structured report (`la-X  se  Y`). That is coherent for Concordian discourse culture. But even fully analytical humans emit sounds when hurt — the question is whether Tonesu commits Concordians to packaging *every* emotional signal as a diagnostic proposition, or whether a performative/expressive register exists that the spec has not yet addressed.

**The fork:** Two defensible positions:
- **(a) Performative expression is paralinguistic**, not Tonesu proper. Concordians cry, laugh, and flinch like any humans; these are pre-linguistic responses outside the scope of the grammar. The language handles propositional emotional expression; the body handles the rest. This is probably the more empirically accurate claim about real language.
- **(b) Concordian culture genuinely suppressed the performative register.** The diagnostic form is the only sanctioned emotional utterance. This makes Concordia emotionally alien in an interesting way — a working medical team more than a family — but may be too strong a cultural claim and is not supported by corpus evidence.

Position (a) is the default until corpus evidence forces a choice. The awkwardness is real and is a feature of the reflective register being the only formally-documented one — casual register compression will address it over time for the first two flavours. The performative register question is logged. See open-questions.md.

**Emotional experience as process, not state:**

The design principle in spec/principles.md § 9 has a second, less visible consequence: Tonesu encodes emotional experience not as *states* one has but as *signal-processing events* one undergoes. A signal arrives (`se`), an interpretive attempt is made, and the process either resolves into a conceptual model (`to`) or does not. This is structurally different from most natural languages, which treat emotions as named states with fixed form.

The result: Tonesu can express something most natural languages handle very poorly — **perception without interpretive resolution**. The state of feeling something without being able to name, locate, or model it. This corresponds to several well-documented psychological phenomena: alexithymia, depressive anhedonia, SSRI emotional flattening, trauma-related affect disruption. English can only gesture at these: "I feel weird," "something's wrong," "I don't know what I'm feeling." These are descriptions of a *failure to classify*, not names of the state itself.

**Canonized constructions (March 2026):**

| State | Construction | Literal |
|---|---|---|
| Unresolved affect | `se-no-to` (W090) | signal + no-model |
| "I feel something I can't identify" | `la-mi  se, no-to-mi` | I perceive; my model is empty |
| Depression-like cluster | `zo-mi  se  vo-de  re / no-go / wi-de` | organism repeatedly perceives value-decay / no identifiable cause / will-diminishing |
| Anxiety-like cluster | `zo-mi  se  fe-ki` | organism perceives approaching-boundary |
| Emotional numbness / flatness | `se-no` | signal-absence |
| Observer mode (dissociation) | `la-mi  to  {la-zo-mi  se  lo-X}` | I model analytically that my organism perceives X |

`se-no-to` is the canonical shortform for unresolved affect. Registered as W090. Compositionally unambiguous via two parse paths that converge: `{se-no}+{to}` and `{se}+{no-to}` both yield signal-without-model.

**The `zo`/`li` observer split:**

Because `zo` (organism) and `li` (social agent) are distinct, a speaker can locate emotional experience in the body or the agent's perspective:

- `la-mi  se  lo-X` — I (as agent) perceive X. Feeling is integrated into the self.
- `la-mi  to  {la-zo-mi  se  lo-X}` — I (as agent) model that my organism perceives X. Feeling held at analytical distance.

The second construction is not designed — it falls out of the ontology. It maps precisely onto dissociated emotional experience: the feeling is happening somewhere in the system, but the agent is observing rather than inhabiting it. This corresponds to what many people on SSRIs or in dissociative states report: the emotion is registered and even nameable, but not felt *from the inside*.

**`fa` — affective substrate primitive (added March 2026):**

`fa` is primitive 33. Its justification parallels `ha`: just as thermal *state* (`ha`) is not the same as *energy* (`ra`), the *inward-facing felt-interior* of organism state (`fa`) is not the same as *outward-facing sensory detection* (`se`). A person who is chemically depressed but sitting in silence is not detecting anything — yet `fa` is clearly active and degraded. `se` was defined as "sight, hearing, touch, detection" — outward-facing. `fa` fills the inward gap without crossing into named emotions.

Usage guard (normative, Principle 9): `fa` names the substrate, not the state. Named emotional states remain derived via process constructions. `fa` appears where the substrate is foregrounded:

| Construction | Meaning |
|---|---|
| `fa-be` | affect rising / emerging |
| `fa-de` | affect diminishing / fading |
| `fa-ki` | affect shifting (changing character, not just level) |
| `fa-re` | recurring affect / cyclical pattern |
| `fa-no` | affective numbness / flatness |
| `fa-no-to` | unresolved affect — substrate active, no model formed (fa-based; parallels `se-no-to` W090) |
| `la-mi  fa-no-to  lo-go` | unresolved affect with no identifiable cause — the most precise Tonesu form for "I feel something but I don't know why" |
| `la-mi  fa  fe-ki` | free-floating anxiety — affect in boundary-approach without a specific threat object |
| `la-mi  fa  vo-de  re` | persistent low — affect repeatedly registering value-decay; closest Tonesu form to sustained depression |
| `la-mi  to  {la-zo-mi  fa  lo-X}` | observer mode: I model that my organism's affective substrate is in state X |

**Three-stage pipeline:** `fa` is the middle layer between external signal and conceptual model:

```
se (perception) → fa (affect substrate) → to (model / cognition)
```

The pipeline can stall at `fa`: `fa-be` with no `to` resolving = affect activated but not understood. `fa-no-to` is the canonical name for this stall. The pipeline can also skip `fa` for purely propositional events — hearing a fact (`la-mi  se  lo-si`) goes `se → to` directly, with no affective substrate involved. `fa` is not mandatory in all mental processing; it is a layer that activates for organism-relevant signals.

**Three-stage sequence example — anxiety resolving:**
- `la-mi  fa-be` — affect is rising (pre-evaluative, no object yet)
- `la-mi  fa-no-to` — substrate active, no model formed
- `la-mi  to  lo-go` — cause identified; model forms

This sequence is more psychologically accurate than any single-word emotion label. Each stage is a valid standalone utterance.

---

### Domain 8: Mutual and Bilateral Events

English collapses: interact / exchange / collide / mate / negotiate / react — all can be expressed as one-way action (`A does X to B`) or passive constructions (`X happened to both`). Tonesu makes a structural cut most languages lack.

| Form | Meaning | Contrast |
|------|---------|----------|
| `go {X}  du {Y}` | X causes Y (directed, one priority) | asymmetric causation |
| `la-A  ka  lo-B` | A acts on B (directed agency) | asymmetric action |
| `zi` | coupling event — both participants enter and exit modified, caused by the coupling itself | symmetric mutual causation |
| `zi-ra` (W104) | mutual energy transformation event (physics) | ≠ `ne-ra` (state of coupling) |
| `zi-ka` (W105) | intentional exchange event — negotiation, trade, treaty (social) | ≠ `la-A  ka  lo-B` (one agent acting on patient) |
| `zi-zo` (W106) | biological coupling event — mating, mutualistic symbiosis | ≠ `go`/`du` predation (directed) |

**The distinction `zi` makes:** Standard causal frames in Tonesu (`go`/`du`) require directionality — a source and a result. `zi` is the case where there is no priority of causation: both participants are simultaneously cause and effect of each other's transformation. The coupling event produces the change in both; neither is doing it *to* the other.

**Key distinction from `ne` (relation):** `ne` is a static relational state — A and B are connected. `zi` is an event — the coupling produces change. A system can be in `ne-ra` state (resonance, ongoing) while undergoing `zi-ra` events (mutual energy transformation). The state/event distinction is ontologically prior to the bilateral/unilateral distinction.

**Key distinction from `go`/`du` loops:** `go {A causes B}  du {B causes A}` describes two *separate* causal chains, each directional. `zi` describes a *single* event with no internal causal direction. This is not merely grammatical shorthand — it is a genuine ontological distinction between sequential reciprocal causation and simultaneous bilateral coupling.

**Cultural claim:** Tonesu treats bilateral symmetric events as a first-class ontological category. A civilization with `zi` as primitive will naturally frame negotiation as an exchange event (not as two parties making concessions), symbiosis as a coupling (not as two organisms benefiting from each other), and force interactions as mutual (not as one object acting on another). The directionality assumption built into most agent-patient grammar is architecturally optional in Tonesu.

---

## Discourse-Level Emergence

Following C001–C004, the language has crossed from sentence-grammar into discourse grammar. The distinction matters: sentence grammar rules describe how words combine within an utterance; discourse grammar rules describe how utterances combine across turns.

**Four discourse-layer systems now active in Tonesu:**

| System | Corpus evidence | Status |
|--------|----------------|--------|
| Argument omission rules | Imperative `la-tu` drop (S019, C001, C002, C004), speaker drop `la-mi` (C001 B3), discourse-context drop (C001 A2b) | Three distinct omission environments confirmed; likely collapse to a general topic-drop rule eventually |
| Epistemic stance marking | `la-{speaker}  {epistemic-root}  {prop}` attested C001 A3, C004 B1; `la-{process}  be  {prop}` attested C004 A2 | Two epistemic framing strategies: person-based and process-based |
| Dialogue confirmation strategies | Action-commit (C001 B3), echo-restate (C003 B1), institutional routing (C004 A3) | Three strategies, none using a bare "yes" — language appears action-confirmation oriented |
| Question construction | Content question via `to-si` (C001 B1), polar question via `to-si` fronting (C003 A1) | `to-si` is load-bearing for all inquiry types; polar/content distinction unresolved |

**Boundary ontology generalization** (noted by Monday after C001):  
`fe` (boundary/limit) systematically extends across domains:  
- Physical limit → `fe` (primitive)  
- Epistemic threshold → `to-fe` (W028)  
- Temporal deadline → `ti-fe` (W037)  
- Energetic extent → `ra-ki-fe` (unregistered, available)  
- Ethical constraint → `wi-fe` (unregistered, available)  

This reuse is not incidental — it reflects a genuine ontological commitment: **limits are limits, regardless of domain.** The same boundary-crossing vocabulary (`fe-ki` = reach a limit, `no-fe` = below the threshold, `fe-si` W024 = warning signal at a boundary) applies uniformly. This is one of the language's most coherent structural choices.

**Grammar pressures introduced by discourse that sentence-grammar could not show:**  
- P-QM-001: polar question marker (see open-questions.md)  
- P-AF-001: minimal affirmative particle (see open-questions.md)  
- ~~P-GP-001: `vo`/`ru` predication slot~~ → **Resolved S162–S165.** Three strategies: `lo-X  Q` (patientive/contingent), `la-X  Q` (attributive/intrinsic), `ka  Q` (manner). See spec/grammar.md § Predication Strategies.  

---

## Open Questions

- [ ] `to` appears in both Structure and Mind clusters — should it split into two roots?
- [ ] Where does "emotion" live? `vo` (value), `wi` (intention), or needs its own root?
- [ ] "Time" (`ti`) and "sequence" — are these one root or two?
- [ ] Does "space" (`pa`) cover abstract topology (e.g. mathematical space) or only physical location?
- [x] ~~Review `plu` — three-letter root is inconsistent with CV/CVC constraint~~ → **Resolved:** replaced with `pu`. See registry/primitives.md.
- [ ] **`vo` subdivision.** The consolidation `vo` = beauty + worth + ethical value + quality may be too coarse for Concordia's precision culture. Should `vo` remain monolithic or eventually split into `vo-se` (sensory quality/beauty), `vo-li` (agent-relative ethical worth), `vo-su` (systematic/objective value measure)? Do not split until corpus produces a sentence where the ambiguity is load-bearing.
- [ ] **`re` and aspect.** If repetition is primitive, does it interact with tense/aspect to produce habitual or iterative aspect grammatically? E.g., `re-ka-be` = habitually builds vs. `ka-be` = built (once). Resolve when tense/aspect phonology is finalized.
- [ ] **False-`re` as an error class.** Is claiming `re` where the pattern is superficial (false analogy) a registered epistemic error category? Candidate: `re-fe-ka` (claiming pattern-identity across a boundary that doesn't actually hold). Do not register until corpus evidence.
- [ ] **Model-domain frame — sustained model-space discourse.** CF-001 established `to-go {X}  Y` for single counterfactual assertions. But discourse sometimes requires a sustained frame: "speaking within the reactor model..." or "according to the failure analysis..." — a scope that covers multiple sentences, not a single conditional. The language currently has no way to open a model-domain scope without re-asserting `to-go` on every sentence. Candidate: bare `to {model-name  begins}` as a discourse-frame opener, closed by returning to actuality-marked utterances. Do not formalize until a corpus conversation or multi-sentence analysis requires it. Watch.
