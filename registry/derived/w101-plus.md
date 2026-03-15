# Derived Compounds (W101+)

Active growth zone. See [w001-w050.md](w001-w050.md) for entry format and validation rules.

---

**W101**
```
Form:         su-ti
Type:         compound
Class:        entity / state
Definition:   current state; instantaneous configuration; the structural condition of a
              system at a specific moment in time
Composition:  su (structure/order) + ti (time/sequence) — the structure as time-indexed;
              a snapshot of arrangement at a given moment rather than an abstract or
              ongoing arrangement. Head-final: `su` (structure) is head; `ti` specifies
              the structure is temporally located (a configuration, not a type).
Register:     standard / technical
Domain:       systems / engineering / physics / cognition
Status:       cold
First use:    not yet attested in corpus; registered as compound candidate after primitive
              validation test for "state/configuration" (March 2026).
Notes:        Resolves open-questions.md note: "The language currently expresses 'X is in
              state Y' via juxtaposition... no primitive for stable condition without
              invoking change or evaluation."
              Usage: `lo-X  su-ti  Y` = X is currently in configuration Y (state snapshot,
              no change implied). Compare `lo-X  be` = X is increasing (change reading);
              `lo-X  su-ti  be-vo` = X is currently in a high-energy configuration (state
              predication without claiming change is occurring).
              Natural extensions:
                su-ti-de  = past configuration / archived state (what the system was)
                su-ti-be  = expected future configuration / target state
              Relationship to wi-re (W099): a feedback loop is precisely the mechanism for
              moving `su-ti` from current state toward a target `su-ti`.
Related:      su (structure/order), ti (time/sequence), wi-re (W099, feedback loop),
              su-ti-de (past state), to-ko (W044, memory — stored past su-ti)
```

---

**W102**
```
Form:         nu-se
Type:         compound
Class:        process / action
Definition:   quantitative detection; measurement; to perceive a quantity;
              to obtain a number or magnitude from observation
Composition:  nu (quantity/number) + se (perception/detection) — perception that returns
              a quantity rather than a mere qualitative signal. Head-final: se (perception)
              is head; nu specifies the kind of perception — one that yields a number
              or measurable value as its output.
Register:     standard / technical / scientific
Domain:       science / engineering / mathematics
Status:       active
First use:    S187 (`la-li  ka  nu-se  lo-ra` = "The person measures the energy."
              — PMS-001-B, Physics/Mathematics sample batch)
Notes:        The canonical compound for scientific measurement. `ka  nu-se` = perform the
              act of measuring. Extension forms:
                nu-se-mu  = measuring instrument (quantity-detection device)
                nu-se-su  = measurement system / metrology framework
                nu-se-ka  = the measured result / reading (the outcome of nu-se)
              Distinction from bare `se` (qualitative detection): `se` = I perceive
              something is there / has this quality; `nu-se` = I perceive its magnitude.
              Both can take the same patient; `nu-se` asserts the output is a number.
Related:      nu (quantity), se (perception), nu-to (quantitative concept/parameter),
              nu-se-mu (measuring instrument), se-ka (W058 type, perceptual-agent)
```

---

- [x] ~~Resolve whether compound forms use hyphens in writing or run together~~ → Resolved: solid spelling is canonical; hyphens are analytic notation only. See spec/word-formation.md § Written Form.

**W103**
```
Form:         ti-re
Type:         compound
Class:        time reference
Definition:   recurring time; the next scheduled occurrence in a repeating sequence;
              the next cycle. The upcoming instance of an event that recurs on an
              established pattern.
Composition:  ti (time) + re (recurrence/cycle) — time defined by recurrence; the forward
              point in time picked out by a cycle's structure. Head-final: ti (time) is the
              head; re specifies that the temporal position is the next position in a
              cycle rather than a generic future interval.
Register:     standard / technical
Domain:       temporal reference / scheduling
Status:       active
First use:    C006 B4 (`ta-ti-re  ki` = "it's coming up in the cycle" — the recurrence
              pilot resonance training event. B uses `ti-re` where A used `ti-be` (A4),
              marking that the upcoming event is a scheduled cycle instance, not merely
              an approaching time on the open timeline.)
Notes:        Contrasts with `ti-be` (W040, proximate future) on the linear-vs-cyclic dimension:
                ti-be = the next time interval on the open forward timeline (generic "soon,"
                        "tomorrow") — no cyclical structure implied
                ti-re = the next occurrence within an established recurring sequence —
                        cyclical structure required
              Decision rule: use `ti-be` when the only claim is that time will pass; use
              `ti-re` when the event belongs to a recurrent pattern and the next instance is
              being referenced.
              Extension forms:
                ta-ti-re         = at the time of the next cycle occurrence (canonical use)
                ta-ti-re-fe      = by the next scheduled occurrence / before the cycle turns again
Related:      ti (primitive: time), re (primitive: recurrence/cycle), ti-be (W040: generic
              proximate future), ti-de (W041: past time), ti-fe (W037: deadline),
              ta (particle: temporal frame)
```

---

**W104**
```
Form:         zi-ra
Type:         compound
Class:        event / process
Definition:   physical interaction; mutual energy transformation; a coupled event in which
              two force-bearing systems each modify the other simultaneously through their
              field relation. The event in which a ne-ra resonance state produces bilateral
              change.
Composition:  zi (mutual/coupling event) + ra (energy/force) — energetic mutual transformation.
              Head-final: ra (energy) is head; zi specifies that the energy domain event
              involves simultaneous bilateral transformation rather than a one-way transfer.
Register:     technical / physics
Domain:       physics / force / field interaction
Status:       proposed
First use:    pending corpus attestation
Notes:        TRIAGE NOTE (March 2026): 3 corpus matches, all in retroactive cross-reference
              notes on S189/S193 (added when zi was admitted). No independent sentence
              yet uses zi-ra in its own right. Promote when an organic attestation exists.
              Distinct from ne-ra (W058): ne-ra describes the *state* of energetic coupling
              between two systems (the resonance condition, ongoing). zi-ra describes the
              *event* of mutual energy transformation — the interaction occurring. A system
              in ne-ra state undergoes zi-ra events. Analogous to the English distinction
              between "being in contact" (state) and "colliding" (event).
              Primary domain: gravitational interaction, electromagnetic coupling, force-pair
              interactions. The z-initial root zi carries none of the organicism of zo;
              zi-ra is clean for purely physical contexts.
              Extension forms:
                la-X  zi-ra  lo-Y     = X and Y undergo mutual energy transformation
                (note: standard patient frame; both participants may be marked lo- when
                 the coupling is symmetric and neither is agent)
Related:      zi (primitive: mutual/coupling event), ra (primitive: energy/force),
              ne-ra (W058: energetic resonance state), ne-ra-ki (W059: entering resonance),
              pa-ra (W053: spatial field)
```

---

**W105**
```
Form:         zi-ka
Type:         compound
Class:        event / process
Definition:   transaction; intentional exchange event; a deliberate coupled event in which
              two agents mutually act on each other, with each party's action simultaneously
              responsive to and shaping the other's. The zi event in the domain of
              intentional action.
Composition:  zi (mutual/coupling event) + ka (intentional action) — intentional mutual
              transformation. Head-final: ka (intentional action) is head; zi specifies
              that the action involves simultaneous bilateral transformation rather than
              one agent acting on a patient.
Register:     standard / social / formal
Domain:       social / exchange / commerce
Status:       proposed
First use:    pending corpus attestation
Notes:        TRIAGE NOTE (March 2026): 2 corpus matches, both in retroactive cross-reference
              note on S194 (added when zi was admitted). No independent sentence yet uses
              zi-ka in its own right. Promote when an organic attestation exists.
              The social-domain zi compound. Covers negotiation, trade, ritual exchange,
              any deliberate coupled social event where both parties revise position
              simultaneously. Distinguishes the exchange-event from mere interaction
              (ne-ka = action-relation, i.e. a pattern of acting on each other) and
              from one-way action (la-X  ka  lo-Y).
              Extends naturally: zi-ka-su = institution of exchange (market, treaty body);
              zi-ka-li = exchange partner / counterpart.
Related:      zi (primitive: mutual/coupling event), ka (primitive: intentional action),
              wi-to-ki (intentional stance revision, S194), ne (relation)
```

---

**W106**
```
Form:         zi-zo
Type:         compound
Class:        event / process
Definition:   biological coupling event; any coupled biological interaction in which two
              organisms both enter and exit modified by the coupling itself, with neither
              the unilateral cause of the other's change. Covers mating and mutualistic
              symbiosis as the same ontological structure.
Composition:  zi (mutual/coupling event) + zo (living thing/organism) — the coupling event
              in the biological domain. Head-final: zo (organism) is head; zi specifies
              that the event involves simultaneous bilateral transformation rather than
              predation or parasitism (which are directional: go/du).
Register:     standard / technical / biological
Domain:       biology / reproduction / ecology
Status:       proposed
First use:    pending corpus attestation (S193 retroactive gap record; W106 assigned
              March 2026 following zi primitive admission)
Notes:        TRIAGE NOTE (March 2026): 2 corpus matches, both in retroactive cross-reference
              notes on S193 (added when zi was admitted). S193 is the gap-demonstration
              sentence, not an organic attestation. Promote when a sentence uses zi-zo
              in its own right.
              Two biological interaction types map to zi-zo:
              (1) Mating: two organisms enter a coupled biological interaction; both
                  change state (gamete transfer, hormonal shifts, etc.). Neither organism
                  is the unilateral cause of the other's change. The transformation
                  emerges from the coupling event itself.
              (2) Mutualistic symbiosis: two organisms each supply resources the other
                  cannot produce alone; both grow or sustain function through the coupling.
                  S193 demonstrated the gap; zi-zo is the correct form.
              These are ontologically identical: both are zi events in the zo domain.
              The compound does not differentiate them — context determines which is
              intended. If distinction becomes necessary, zi-zo-ki (begin coupling) vs
              zi-zo-su (the coupled system) handles temporal vs structural readings.

              Fertilization is NOT zi-zo. Gamete fusion is structurally asymmetric:
              one gamete is absorbed into another, creating a new entity. The direction
              of causation is not mutual — the event creates a single modified entity,
              not two modified entities exiting as individuals. Use: ki (inchoative of
              new-entity formation) or go/be for the development process. Biological
              lifecycle distinction:
                zi-zo          mating event (mutual, symmetric)
                ki / go-be     fertilization (asymmetric genotype fusion)
                be             development / growth (single-participant)

              Predation and parasitism are NOT zi-zo. They are directional:
              go [predator]  du [prey  de]. Use go/du.

              Extension family:
                zi-zo-su    = reproductive pair / mutualistic coupled-organism system
                zi-zo-ki    = mating/coupling begins (inchoative)
                zi-zo-de    = coupling bond dissolves
                zi-zo-go    = the go-role participant (W107)
                zi-zo-du    = the du-role participant (W108)
Related:      zi (primitive: mutual/coupling event), zo (primitive: living thing),
              ne-ra (W058: resonance state, distinct from zi-zo coupling event),
              zi-ra (W104: physical interaction), zi-ka (W105: intentional exchange),
              zo-ne-go (W077: parent), zo-ne-ru (W079: sibling),
              zi-zo-go (W107), zi-zo-du (W108)
```

---

**W107**
```
Form:         zi-zo-go
Type:         compound
Class:        role / biological attribute
Definition:   the go-role participant in a biological coupling event; the party whose
              gametic contribution is the mobile, outward-traveling, origin-of-motion
              type; male in the biological gamete-asymmetry sense.
Composition:  zi-zo (biological coupling event, W106) + go (cause/origin) — the
              participant occupying the origin/mobile-contribution role within the
              coupling. Head-final: go specifies which of the two symmetric roles this
              participant occupies.
Register:     technical / biological
Domain:       biology / reproduction
Status:       active
First use:    pending corpus attestation
Notes:        This is a biological role description, not a social category. It says
              nothing about anatomy beyond gametic contribution type. The definition
              anchors to anisogamy (gamete-size asymmetry), which is the most
              taxonomically consistent definition of biological sex across sexually
              reproducing organisms.
              Sex-neutral social identity: kinship vocabulary (W076–W081) is
              deliberately sex-neutral. zi-zo-go is a biological/scientific register
              term, not a social one. A Concordian speaker reporting biological
              observations uses this; a speaker describing kin relationships does not
              need it.
              Complementary pair: zi-zo-du (W108) is the du-role participant.
              The two forms are mutually exclusive within a given zi-zo event, and
              together they exhaust the participant roles.
              Isomorphism note: the go/du distinction here mirrors the go/du distinction
              in zo-ne-go (parent) and zo-ne-du (child): in both cases go = source/origin,
              du = result/destination. The parallelism is not accidental — both compress
              the same causal-role logic into the kin/biology domain.
Related:      zi-zo (W106), zi-zo-du (W108), go (primitive: cause/origin)
```

---

**W108**
```
Form:         zi-zo-du
Type:         compound
Class:        role / biological attribute
Definition:   the du-role participant in a biological coupling event; the party whose
              gametic contribution is the large, nutrient-rich, substrate-receiving type;
              female in the biological gamete-asymmetry sense.
Composition:  zi-zo (biological coupling event, W106) + du (result/effect) — the
              participant occupying the substrate/receiving-contribution role within
              the coupling. Head-final: du specifies which of the two symmetric roles
              this participant occupies.
Register:     technical / biological
Domain:       biology / reproduction
Status:       active
First use:    pending corpus attestation
Notes:        This is a biological role description, not a social category. Anchors to
              anisogamy: the egg contributor supplies the cell that hosts gamete fusion
              and initiates development; this is the du (result/destination) role
              because the event's developmental continuation originates in that gamete.
              Sex-neutral social identity: see W107 notes. zi-zo-du is biological
              register only.
              Complementary pair: zi-zo-go (W107) is the go-role participant.
              Species with simultaneous hermaphroditism occupy both roles sequentially
              or simultaneously — this is a role description, not an exclusive biological
              partition in all organisms.
Related:      zi-zo (W106), zi-zo-go (W107), du (primitive: result/effect)
```

---

## Temporal Deixis and Tense

**W109**
```
Form:         ti-mi
Type:         compound
Class:        temporal entity / deictic anchor
Definition:   now; the present moment; the speaker's time; temporal deictic for
              the interval coinciding with the speech act.
Composition:  ti (time/sequence) + mi (self/speaker) = time-of-me = the time
              indexed to the speaker. Parallel to pa-mi (W110: here = place-of-me).
              Both are deictic anchors formed by the same domain + self-anchoring
              pattern.
Register:     standard
Domain:       general / temporal
Status:       active
First use:    pending corpus attestation
Notes:        Deictic anchor: ti-mi is indexical — it refers to whatever time is
              current when the sentence is uttered. In written or reported speech,
              the anchor shifts to the time of the reported speaker.
              ti-mi completes the ti-[X] temporal reference family as the deictic
              member: ti-de (W041: past) / ti-mi (present) / ti-be (W040: future) /
              ti-re (W103: next cycle) / ti-fe (W037: deadline). All use ti as head.
              Replaces the placeholder 'ta-now' in spec/grammar.md § Temporal Frame.
              No CVC or CVCC form is warranted — fully compositional.
              Note: W111 and W112 (de-ti, be-ti) were registered in error with
              reversed root order and have been retired. Past = ti-de (W041);
              future = ti-be (W040).
Related:      pa-mi (W110: here), ti-de (W041: past), ti-be (W040: future),
              ti-re (W103: next cycle), ti-fe (W037: deadline),
              ti (primitive: time/sequence), mi (primitive: self/speaker),
              hulm (CVCC: Julian year — calibrated temporal anchor)
```

---

**W110**
```
Form:         pa-mi
Type:         compound
Class:        spatial entity / deictic anchor
Definition:   here; this place; the speaker's location; spatial deictic for the
              place coinciding with the speaker at utterance time.
Composition:  pa (place/territory) + mi (self/speaker) = place-of-me = here.
              Structural mirror of ti-mi (W109: now = time-of-me). The deictic
              pair is formed by the same pattern across spatial and temporal domains.
Register:     standard
Domain:       general / spatial
Status:       active
First use:    pending corpus attestation
Notes:        Both deictic anchors (W109, W110) fell out of the primitive set
              without any design effort — the self-anchoring pattern was latent.
              The symmetry of ti-mi / pa-mi was discovered in a CVCC candidacy
              evaluation (March 2026) when "now" was tested against the
              Assemblage-First Rule.
Related:      ti-mi (W109: now), pa (primitive: place), mi (primitive: self)
```

---

**W111** *(retired — root-order error)*
```
Form:         de-ti  ← INCORRECT ROOT ORDER; this entry is retired
Status:       retired (March 2026)
Notes:        Registered in error with root order reversed. The correct compound
              for past time is ti-de (W041): ti (time, head) + de (decay, directional
              qualifier). de-ti would place de as the head, which is not the
              established pattern for the ti-[X] temporal reference family.
              Use ti-de (W041) for all references to past time.
Superseded by: W041 (ti-de)
```

---

**W112** *(retired — root-order error)*
```
Form:         be-ti  ← INCORRECT ROOT ORDER; this entry is retired
Status:       retired (March 2026)
Notes:        Registered in error with root order reversed. The correct compound
              for future time is ti-be (W040): ti (time, head) + be (growth/coming,
              directional qualifier). be-ti would place be as the head, inconsistent
              with the established ti-[X] temporal reference family.
              Use ti-be (W040) for all references to proximate future time.
Superseded by: W040 (ti-be)
```

---

## States of Matter

**W113**
```
Form:         su'ma
Type:         compound
Class:        material quality / state
Definition:   solid; matter in its organized, fixed-structure state; the physical
              state of matter with both fixed shape and fixed volume.
Composition:  su (structure/organized form) + ma (matter) = structured matter.
              The apostrophe marks su as a discriminator on the base ma: the
              kind of matter defined by having organized structure.
Register:     standard
Domain:       physical / chemistry
Status:       active
First use:    pending corpus attestation
Notes:        su as "organized solid form of a substance" is consistent across all
              its corpus uses: ma-su (rock = structured mineral matter, S293),
              su'ma-ki (ice = structured flowing matter, S300), su'ma-pa (clay =
              structured soil, S293), su'zo-pe (spider = structure-building
              arthropod, S323), su'zo-ne (cap fungus = structure-producing fungus,
              S330). su'ma names the general solid state of any matter, as distinct
              from those specific-substance compounds where su also discriminates
              a particular material kind.
              su'ma is the bulk-state term. su'ma-[X] (structured matter of a
              specific kind) captures specific solid-state substances as before.
Related:      ki'ma (W114: liquid), no-su'ma (W115: gas), ma-ra (W116: plasma),
              ma-su (rock), su'ma-ki (ice), su'ma-pa (clay), su (primitive),
              ma (primitive)
```

---

**W114**
```
Form:         ki'ma
Type:         compound
Class:        material quality / state
Definition:   liquid; matter in its flowing, mobile state; the physical state of
              matter with fixed volume but no fixed shape, that flows under gravity.
Composition:  ki (motion/flow/change) + ma (matter) = moving/flowing matter.
              The apostrophe marks ki as a discriminator on the base ma: the kind
              of matter defined by flowing.
Register:     standard
Domain:       physical / chemistry
Status:       active
First use:    pending corpus attestation
Notes:        Contrast with ma-ki (water/flowing matter, MAT-002): ma-ki is the
              specific substance water — the domain-primitive compound for the
              hydrogen-oxygen fluid. ki'ma is the general state — any matter in
              the liquid phase, regardless of substance. Mercury, molten iron,
              and water at room temperature are all ki'ma; only the last is ma-ki.
              The apostrophe placement distinguishes direction of composition:
              ki'ma (ki discriminates ma = flowing-kind-of-matter) vs ma-ki
              (ma modified by ki = the matter whose nature is flow = water).
Related:      su'ma (W113: solid), no-su'ma (W115: gas), ma-ki (water, distinct),
              ki (primitive), ma (primitive)
```

---

**W115**
```
Form:         no-su'ma
Type:         compound
Class:        material quality / state
Definition:   gas; matter in its unstructured, expansive state; the physical state
              of matter with neither fixed shape nor fixed volume, expanding to fill
              any container.
Composition:  no (negation/absence) + su (structure) + ma (matter) = unstructured
              matter. The negation of organized form applied to matter: matter
              without fixed structural arrangement.
Register:     standard
Domain:       physical / chemistry
Status:       active
First use:    pending corpus attestation
Notes:        no-su = absence of structure, the negation of su. The no-* productive
              pattern (no-lu = dark, no-ki = still, no-be = erosion, no-ko =
              uncontained, S293–S303) extends here to no-su = structureless.
              no-su'ma is the general gaseous state; specific gas substances
              follow the same discriminator pattern: no-su'ma-ki = steam/water
              vapor (structureless water-matter) would be the water-gas form,
              parallel to su'ma-ki (ice = structured water-matter).
              Contrast with no-ko'ma-ki (rain = uncontained water, S303): that
              compound's no-ko discriminates containment, not structure. For bulk
              gaseous state, the defining absence is structural organization, not
              just containment — no-su'ma is the correct form.
Related:      su'ma (W113: solid), ki'ma (W114: liquid), ma-ra (W116: plasma),
              no (primitive: negation), su (primitive), ma (primitive),
              no-ko'ma-ki (rain, structurally distinct)
```

---

**W116**
```
Form:         ma-ra
Type:         compound
Class:        material quality / state
Definition:   plasma / ionized matter; matter in an energy-excited or charge-
              separated state; at atomic scale: an ion (atom with net charge);
              at bulk scale: plasma (the fourth state of matter, in which electrons
              are separated from atomic nuclei throughout the material).
Composition:  ma (matter) + ra (force/energy) = matter in a force/energy state.
Register:     standard
Domain:       physical / chemistry
Status:       active
First use:    pending corpus attestation
Notes:        ma-ra is scale-agnostic: the same compound applies whether describing
              a single ion (one ma-ra particle) or a bulk plasma (a volume of ma-ra).
              This is semantically clean — plasma is bulk ionized matter; an ion is
              an individual instance of the same condition. The compound captures
              the defining property (matter in an energy/force state) at both scales.
              Already noted in notes/anchor-inventory.md §Atomic and molecular compounds
              table as a compositional chemistry term, not requiring CVC form.
              The four-state sequence: su'ma (solid) / ki'ma (liquid) / no-su'ma
              (gas) / ma-ra (plasma) maps onto increasing energy input: adding
              energy to su'ma produces ki'ma, then no-su'ma, then ma-ra. The
              compounds encode this: structure → flow → no-structure → force-state.
Related:      su'ma (W113), ki'ma (W114), no-su'ma (W115), ra (primitive: force/
              energy), ma (primitive: matter)
```

---

---

## Ethical / Theological Domain (Matthew 5–7 intake)

**W117**
```
Form:         zo-ra
Type:         compound
Class:        entity / vital quality
Definition:   life-energy; animating vitality; the dynamic force that makes an
              organism alive and active; the felt sense of being enlivened. Equivalent
              to Hebrew nefesh in its primary biological sense: the enlivened breath-
              capacity of a living creature (Genesis 2:7: "living being"). Covers
              but is not limited to: vitality, vigor, the animating principle of life.
Composition:  zo (living thing/organism) + ra (force/energy) = the force/energy of a
              living thing = animating vitality. Head-final: ra (force) is head; zo
              specifies the domain — the force native to living things.
Register:     standard / theological / poetic
Domain:       biology / theology / phenomenology
Status:       active
First use:    S359 (GOD-RES batch; `zo-ra` = "life-energy" in three-way zo-ra / zo-to /
              zo-si contrast; resolves open-question GOD-007).
Notes:        Three-way distinction resolved in GOD-RES:
                zo-ra  = animating vitality (nefesh hayah — living being's energy)
                zo-to  = soul / organism identity-pattern (W068)
                zo-si  = spirit / disembodied living agent (W069)
              zo-ra can cease at death; whether zo-to persists is a theological open
              question Tonesu leaves open. zo-si refers to an agent that has no
              physical organism and does not cease the way zo-ra does.
              zo-ra-ma = food (energy-matter of living things; GOD-007/S359).
              zo-ra-fe = life's completion/fullness (Matthew 7 usage for "life" as
              the endpoint the narrow gate leads to).
Related:      zo (primitive), ra (primitive), zo-to (W068), zo-si (W069),
              zo-ra-ma (food compound), zo-ra-fe (life to fullness)
```

---

**W118**
```
Form:         vo-ne
Type:         compound
Class:        quality / relational state
Definition:   righteousness; right relational standing; being in a state of value
              within one's bonds and social connections. The quality of acting
              rightly within all one's relationships — not merely internal virtue
              but correct alignment with one's relational obligations. Corresponds
              to Hebrew tsedakah and Greek dikaiosynē (righteousness / justice).
Composition:  vo (value/quality) + ne (relation/bond) = value-in-relation = the
              quality of having correct value in one's relational network. Head-final:
              ne (relation) is head; vo specifies that the relational quality being
              described is one of positive value = being right in one's bonds.
Register:     standard / ethical / theological
Domain:       ethics / theology / social
Status:       active
First use:    Matthew 5–7 translation (SOM draft). Recurs throughout: Beatitudes
              (5:6, 5:10), antitheses (fulfilling the law), Lord's Prayer context, etc.
Notes:        Deliberately relational: not "being good internally" (which would be
              su-fa, W133) but "being correctly aligned in one's bonds." tsedakah
              always involves both dimensions; Tonesu captures the relational
              dimension through ne.
              vo-ne as predicate: `la-X vo-ne` = X has right-relational-quality.
              As patient: `lo-vo-ne` = the quality of righteousness as a thing to
              seek or have. "Hunger for righteousness" = `fa-wi lo-vo-ne` (Matthew 5:6).
Related:      vo (primitive: value/quality), ne (primitive: relation/bond),
              su-fa (W133: purity of inner affect), wi-no-ra (W132: meekness),
              fa-vo (compassion compound)
```

---

**W119**
```
Form:         de-su
Type:         compound
Class:        entity / moral quality
Definition:   fault; wrong; a moral or relational failure; the product of decrease
              applied to structure. The concrete result-thing of a moral failing.
              Covers: trespass, sin, wrong done, fault that requires addressing.
              Greek hamartia (sin/missing the mark) and opheilēma (debt/obligation).
Composition:  de (decrease/decay) + su (structure/product) = decay-product = the
              structured thing that results from moral decrease. Head-final: su
              (structure/organized form) is head; de specifies that the structure
              is one produced by a deficiency or decrease — a fault-shape.
Register:     standard / ethical / theological
Domain:       ethics / law / theology
Status:       active
First use:    Matthew 5–7 translation (Lord's Prayer: "forgive us our de-su").
Notes:        The compound's logic: su forms the nominal of any process. de-su =
              "the structured result of decrease" = a fault-token that now exists
              and can be addressed. This is why forgiveness is ka-no-de-su: the
              deliberate removal of the fault-product. The fault exists as an entity
              (it was produced); forgiveness removes that entity.
              Contrasts:
                de         = the process of decreasing/decaying (action/state)
                de-su      = the product of that process = the fault-record
                de-vo      = the quality of being evil (W121)
                ka-no-de-su = the act of removing the fault-record = forgiveness (W120)
Related:      de (primitive), su (primitive), ka-no-de-su (W120), de-vo (W121)
```

---

**W120**
```
Form:         ka-no-de-su
Type:         compound
Class:        action / process
Definition:   forgiveness; the deliberate act of removing a fault-record; to dissolve
              the moral debt or trespass that exists as a de-su. The volitional
              removal of a standing wrong. Greek aphiēmi (release/forgive).
Composition:  ka (deliberate action) + no (negation/removal) + de-su (fault/wrong,
              W119) = deliberately-remove-fault-structure. The agent `ka`-performs
              the `no`-removal of the `de-su` (fault-record). Four-syllable compound
              permitted as a semantically complex derived form.
Register:     standard / ethical / theological
Domain:       ethics / theology / social
Status:       active
First use:    Matthew 5–7 translation (Lord's Prayer: "remove our faults"; 6:14–15).
Notes:        The structure of the action: ka = agent does it deliberately; no = the
              act is a removal/negation; de-su = the entity removed is the fault-record.
              This is transitive: `la-X  lo-de-su  ka-no` = X removes [the specific
              fault], or (with patient as beneficiary) `la-X  lo-de-su-Y  ka-no` =
              X removes Y's fault-record. In the Lord's Prayer the beneficiary prefix
              appears: `la-tu  lo-de-su-yu  ka-no` = you: remove our fault-records.
              Lord's Prayer bilateral: `lo-de-su-yu  ka-no  go-[la-yu  lo-de-su-li-ne  ka-no]`
              = remove our faults as we remove the faults of those-in-relation-to-us.
Related:      ka (primitive: deliberate action), no (primitive: negation),
              de-su (W119: fault/wrong), de-vo (W121: evil quality)
```

---

**W121**
```
Form:         de-vo
Type:         compound
Class:        quality / moral state
Definition:   evil; the quality of moral decay; value-corrosion; the state of being
              organized around decrease in value. Not a thing but a quality: the
              property of choices, agents, or states characterized by the corruption
              of goodness. Greek ponēros (evil, wicked, harmful).
Composition:  de (decrease/decay) + vo (value/quality) = decay-of-value. Head-final:
              vo (value) is head; de specifies that the value in question is undergoing
              or has undergone decrease/corruption.
Register:     standard / ethical / theological
Domain:       ethics / theology
Status:       active
First use:    Matthew 5–7 translation (Lord's Prayer: "deliver us from de-vo"; 7:11
              "evil gifts"; Matthew 5:45 "evil person" = de-vo-li).
Notes:        Key derivatives:
                de-vo-li   = a person characterized by evil = an evil person
                de-vo-ki   = entering evil state = becoming corrupt (inchoative)
                pa-de-no-fe = place of boundless decay = Gehenna/hell (proposed;
                              SOM-002, pending corpus test)
              Contrast with:
                de-su  (W119) — a fault-product (countable, addressable wrong)
                de-vo  — the quality itself (uncountable, characterizes agents/states)
              "Evil" in the Lord's Prayer "deliver us from evil": `go-de-vo  fe` =
              bound us from the domain of evil-value = from the sphere of de-vo.
Related:      de (primitive), vo (primitive), de-su (W119), ka-no-de-su (W120),
              de-vo-li (evil person derivation)
```

---

**W122**
```
Form:         ka-to-fe
Type:         compound
Class:        action / process
Definition:   to judge; the deliberate act of making an epistemic determination about
              a person or situation — rendering a verdict or assessment that places the
              subject definitively on one side of an epistemic boundary. The volitional
              act of adjudication. Greek krinō (judge, evaluate, condemn).
Composition:  ka (deliberate action) + to-fe (epistemic boundary, W028) = deliberate
              epistemic bounding = the act of performing to-fe on a person or case.
              The agent intentionally draws the epistemic line that classifies the
              subject. Head-final: to-fe (W028) is the semantic core; ka specifies
              that this is a deliberate act, not an emergent classification.
Register:     standard / ethical / legal / theological
Domain:       ethics / law / theology
Status:       active
First use:    Matthew 7:1 ("Do not judge" = `no-ka-to-fe`).
Notes:        Extends the to-fe family:
                to-fe         (W028) the epistemic boundary itself (noun: the line)
                to-fe-li      (W032) a professional adjudicator (role)
                to-fe-su      (W072) a standards body
                to-fe-su-ki   (W097) an epistemic ruling crossing to public enforcement
                ka-to-fe      (W122) the deliberate act of judging (verb)
              Matthew 7 usage: `no-ka-to-fe` = don't-judge. The point is the
              deliberateness: casual assessment is `to` (form a concept/model);
              final adjudication of a person as guilty/just is `ka-to-fe` (deliberate
              boundary-drawing).
              `to-fe  be-ki` = enters the judged-state = subject to judgment (passive
              construction — being placed on the wrong side of the boundary).
Related:      to-fe (W028), to-fe-li (W032), to-fe-su (W072), ka (primitive)
```

---

**W123**
```
Form:         fa-ra-be
Type:         compound
Class:        affect quality / process
Definition:   anger; hostile arousal; affect characterized by force increasing toward
              a target. The affective substrate state in which force-energy rises in
              a directed and hostile manner. Not just heightened arousal but organized
              toward opposing or harming. Greek orgē (anger, wrath).
Composition:  fa (affective substrate) + ra (force/energy) + be (increasing/upward) =
              affect-force-increasing. The affect-substrate is activated in the
              direction of increasing force, and this force is directed hostilely.
Register:     standard / ethical / theological
Domain:       affect / ethics
Status:       active
First use:    Matthew 5:22 ("anyone who is angry" = `fa-ra-be  lo-ne-zo-ne`).
Notes:        Extends the fa-[X] compound family:
                fa-ki  (W093) affect shifting/changing register
                fa-de  (W094) affect fading
                fa-no  (W095) affect inactive
                fa-re  (W096) affect cycling
                fa-ra-be     anger (new: affect-force-increasing)
                fa-de-ki     mourning (inchoative of W094: entering fading-affect)
              Anger is specifically fa-ra-be (versus mere fa-be = affect-rising, which
              could be positive excitement or awe). The ra component specifies that
              what is rising is force-energy, and the target is another person.
              fa-ra-be does not require external expression: it is the interior state.
              The acted form would be `ka-fa-ra-be-ki` = deliberately enter/induce
              the hostile-affect-rising state (deliberately provoke anger), but the
              simple predication `lo-X  fa-ra-be` = X has rising hostile affect.
Related:      fa (primitive: affective substrate), ra (primitive: force/energy),
              be (primitive: growing/increasing), fa-ki (W093), fa-de (W094)
```

---

**W124**
```
Form:         wi-de-li
Type:         compound
Class:        person / role
Definition:   adversary; enemy; an opposing-willed person; one whose will is directed
              toward the decrease or harm of another. Not merely a stranger or
              non-ally but one who actively opposes. Greek echthros (enemy, hostile one).
Composition:  wi (intention/will) + de (decrease/harm) + li (person) = person-of-
              harm-directed-will = a person whose intention is organized around
              causing decrease. Head-final: li (person) is head; wi-de specifies the
              kind of person — one whose will tends toward harm.
Register:     standard / ethical / military / relational
Domain:       ethics / social
Status:       active
First use:    Matthew 5:44 ("love your enemies" = `fa-vo-no-fe  lo-wi-de-li-tu`).
Notes:        Complements the ne (bond) family by specifying the opposite of a bonded
              partner. ne-li = a bonded relational person (neighbor/ally); wi-de-li =
              a person whose will is against you (enemy). The Sermon on the Mount
              explicitly requires loving wi-de-li — the compound needs to be negative
              enough that the command is genuinely demanding.
              Contrasts:
                ne-li      = person in bond-relation = neighbor
                wi-de-li   = person of harm-directed-will = enemy
                no-ne-li   = person without bond = stranger (weaker than enemy)
              "Love your enemies" in Matthew 5:44 uses fa-vo-no-fe (W series THO-001)
              = affect-value-without-limit = unconditional love directed at wi-de-li.
Related:      wi (primitive: will/intention), de (primitive: decrease), li (primitive),
              ne-li (bonded-person, from ne + li), fa-vo-no-fe (unconditional love)
```

---

**W125**
```
Form:         pa-be'ka-li-su
Type:         compound (apostrophe-marked)
Class:        entity / domain
Definition:   kingdom of heaven; the governance domain of the upper space; the
              reign associated with the celestial/divine realm. Greek basileia tōn
              ouranōn (kingdom of the heavens). The compound is the governance
              domain (ka-li-su) qualified by its origin-realm (pa-be = upper space).
Composition:  pa-be (upper space, ascending domain) + ka-li-su (governance/dominion,
              cf. Genesis 1:26) = [upper-space] governance. The apostrophe after pa-be
              marks pa-be as the pre-bound left unit: [pa-be] modifies [ka-li-su].
              Without apostrophe, default right-branching would parse: pa modifies
              [be-ka-li-su], which is not intended.
Register:     theological / liturgical
Domain:       theology / eschatology
Status:       active
First use:    Matthew 5–7 translation (Beatitudes 5:3, 5:10; prayer 6:10; 7:21).
Notes:        This is Tonesu's canonical rendering of "the Kingdom of Heaven" as
              used in Matthew's Gospel (Matthew uses "heaven" where Mark/Luke use
              "God" — i.e., "Kingdom of God" = "Kingdom of Heaven" theologically).
              Short form in prayer: `lo-pa-be'ka-li-su-tu  be-ki` = "may your
              upper-space-governance come into being" = "thy kingdom come."
              The compound uses apostrophe notation (first appearance in the compound
              registry for this notation type) — normal in writing, analytic here.
Related:      pa-be (upper space; used in Genesis 1 for "sky/heaven"),
              ka-li-su (governance/dominion, Genesis 1:26), pa (primitive), be (primitive)
```

---

**W126**
```
Form:         si-no-vo-li
Type:         compound
Class:        person / role
Definition:   hypocrite; a person of valueless signal; one whose outward communication
              does not match their inner state or intentions — one who signals goodness
              without possessing it. Greek hupokritēs (actor, one who plays a role).
Composition:  si (signal/representation) + no (negation) + vo (value/quality) + li
              (person) = person-of-valueless-signal = a person whose signals lack the
              value they claim. Head-final: li (person) is head; si-no-vo = the kind
              of signal-person: one whose signals are value-depleted.
Register:     standard / ethical
Domain:       ethics / social
Status:       active
First use:    Matthew 6 (6:2, 6:5, 6:16 — thrice in a single chapter).
Notes:        si-no-vo-li is the full noun. The adjective compound is si-no-vo —
              "hypocritical" or "of false-signal character." The personification `-li`
              builds on the standard person-formation pattern.
              Matthew 6 uses the word six times total (6:2, 6:5, 6:16, 23:13+); it is
              a high-frequency term for this theological corpus.
              Related construct: `si-no-zo-to` = signal-without-matching-soul-pattern
              could express the specific sense of an actor who plays a role different
              from their identity. This is a stronger/more specific reading if needed;
              si-no-vo-li is the general "false-signaler" form.
Related:      si (primitive: signal), no (primitive: negation), vo (primitive: value),
              li (primitive: person), si-de (W098: past signal)
```

---

**W127**
```
Form:         fa-wi-de
Type:         compound
Class:        affect state / process
Definition:   temptation; the affective state in which desire (will) is directed
              toward something harmful (decrease). The pull of the affective substrate
              in the direction of harm; the interior experience of being drawn toward
              wrong action. Greek peirasmos (trial, temptation, testing).
Composition:  fa (affective substrate) + wi (will/intention) + de (decrease/harm) =
              affect-will-toward-decrease = the felt directedness of desire toward
              harm. Head-final: de (decrease) is head, specifying what the affect-will
              is oriented toward.
Register:     standard / ethical / theological
Domain:       ethics / theology / affect
Status:       active
First use:    Matthew 6:13 (Lord's Prayer: "lead us not into temptation" =
              `lo-yu  fa-wi-de  no-wi`).
Notes:        fa-wi-de-ki = entering temptation state (inchoative); the most common
              form in use: "don't lead us into fa-wi-de-ki" = into the state of
              being tempted. The "-ki" form signals the onset of the temptation
              experience, not just temptation as a concept.
              Compare: fa-wi-zi (W128 area; desire-to-couple = lust) — that is a
              specific sub-type of fa-wi toward a specific target (coupling). fa-wi-de
              is the general form covering any affect-desire directed at harm.
Related:      fa (primitive: affect), wi (primitive: will), de (primitive: decrease),
              fa-wi-zi (desire-to-couple / lust, SOM translation — see Notes)
```

---

**W128**
```
Form:         ka-de-zo
Type:         compound
Class:        action / process
Definition:   to kill; the deliberate act of decreasing a living thing to the point of
              cessation. The intentional ending of the zo-ra (life-energy) of an
              organism. Greek apokteinō (to kill, slay); Hebrew ratsach (murder).
Composition:  ka (deliberate action) + de (decrease) + zo (living thing) = deliberate
              decrease of living = intentional killing. Head-final: zo (living thing)
              is the patient/head; de specifies the direction (decrease to zero); ka
              specifies the action is intentional.
Register:     standard / ethical / legal
Domain:       ethics / law / biology
Status:       active
First use:    Matthew 5:21 ("do not murder" = `no-ka-de-zo  lo-li-zo-ne`).
Notes:        ka-de-zo is murder/killing as a deliberate act (ka). Accidental or
              non-deliberate death would be `de-zo` (without ka) = organism-decrease
              = dying/death. The ka modifier makes it morally significant: intentional
              vs accidental.
              Note: "Do not kill" is `no-ka-de-zo`, but the antithesis extends to
              `fa-ra-be` (W123, anger) — the interior state that motivates ka-de-zo.
              The ethical point of the antithesis is that the interior state is as
              morally relevant as the external act.
Related:      ka (primitive), de (primitive), zo (primitive), fa-ra-be (W123: anger),
              zo-ra (W117: life-energy)
```

---

**W129**
```
Form:         no-de-ma
Type:         compound
Class:        entity / material quality
Definition:   salt; preservative matter; substance that resists or prevents decay.
              The material form notable for its decay-resisting function. Greek halas
              (salt) in its metaphorical Sermon usage: "you are the salt of the earth."
Composition:  no (negation/resistance) + de (decrease/decay) + ma (matter) = non-
              decay matter = matter that resists the decay process. Head-final: ma
              (matter) is head; no-de specifies the kind of matter — that which
              prevents decrease.
Register:     standard / culinary / metaphorical
Domain:       material / ethics (metaphorical)
Status:       active
First use:    Matthew 5:13 ("you are the salt of the earth" = `la-yu  no-de-ma  go-pa-ma`).
Notes:        The metaphorical use (Matthew 5:13) is the primary Tonesu attestation.
              The compound is structurally transparent in both directions: physical salt
              (a material that prevents rot) = no-de-ma; also the figurative sense (a
              community that prevents moral decay in the world) = `la-yu  no-de-ma
              go-pa-ma`. The compound carries both readings simultaneously.
              "If salt loses its saltiness" = "if the no-de-ma loses its no-de
              quality" = `lo-no-de-ma  no-de-vo  de` = the preservative's decay-
              resistance value decays away.
Related:      no (primitive), de (primitive), ma (primitive), ma-no-de (W046: medicine —
              note: different root order; W046 = matter that decreases-not = preventive
              substance; W129 = non-decrease-matter = preservative. Related but distinct.)
```

---

**W130**
```
Form:         se-lu
Type:         compound
Class:        entity / anatomical
Definition:   eye; the visual perception organ; the organ of light-perception. The
              biological structure that performs se (perception) in the domain of lu
              (light) = the light-perceiving organ.
Composition:  se (perception/detection) + lu (light) = perception-of-light = the
              organ that detects light. Head-final: lu (light) is head; se specifies
              the relationship — this is a perception-entity in the light domain.
Register:     standard / biological / poetic
Domain:       anatomy / sensory / theology
Status:       active
First use:    Matthew 5:29–30; 6:22–23; 7:3–5 (Matthew uses "eye" extensively).
Notes:        High-frequency body term. Matthew 5:29 ("if your eye causes you to
              stumble"); 6:22 ("the eye is the lamp of the body"); 7:3–5 (speck/plank
              in the eye). The compound is needed across all three chapters.
              In 6:22: `lo-se-lu  lu-mu  go-ko-zo` = the eye is the light-body of
              the body-interior = the lamp (lu-mu) of the body (ko-zo).
              se-lu is the visual organ; for a broader sensory organ the pattern
              would be se-[domain] for each sensory modality (se-so for the sound-
              perception organ = ear, hypothetically).
Related:      se (primitive: perception), lu (primitive: light), lu-mu (light-body:
              lamp, artifact); ko-zo (body-interior compound)
```

---

**W131**
```
Form:         ne-zi-re
Type:         compound
Class:        entity / role / kinship
Definition:   spouse; bonded coupling partner; the person with whom one is in a
              recurring mutual coupling bond. The relational role of one's partner
              in an established and recognized coupling bond. Greek gunē (woman/wife)
              and anēr (man/husband) in their spousal senses.
Composition:  ne (relation/bond) + zi (mutual/coupling event) + re (recurrence) =
              bond-of-recurring-coupling = the relational bond defined by a recurring
              mutual coupling event. A `ne` (bond) characterized by `zi-re` (recurring
              coupling): a spouse is the person to whom one is bonded through this
              type of recurring mutual joining.
Register:     standard / social / legal
Domain:       kinship / social / legal
Status:       active
First use:    Matthew 5:31–32 (divorce/remarriage antithesis).
Notes:        Tonesu is sex-neutral throughout the kinship vocabulary; ne-zi-re is
              the role without biological sex specification. The biological sex of
              either party, if relevant, is expressed via zi-zo-go (W107) and
              zi-zo-du (W108) as needed.
              `ne-zi-re-ze` = their spouse (genitive suffix on the relational role).
              Key derivatives:
                ne-zi-re-de  = bond-of-recurring-coupling + dissolution = divorcing
                si-fe-ne-de  = bounded-signal-of-bond-dissolution = divorce certificate
              Opening of Matthew 5:31–32: "anyone who divorces his wife" =
              `lo-zo-li  lo-ne-zi-re-ze  no-ne  ka` = person who deliberately-removes
              the bond with their spouse.
Related:      ne (primitive), zi (primitive), re (primitive: recurrence), zi-zo (W106),
              ne-de (W091: bond dissolution), ka-ne-de (W092: deliberate dissolution)
```

---

**W132**
```
Form:         wi-no-ra
Type:         compound
Class:        quality / disposition
Definition:   meekness; gentleness; the quality of purposeful will without aggressive
              force. Being intentional and directed without dominating or overwhelming.
              Not absence of will but presence of will without force applied against
              others. Greek praus (gentle, meek, tame — of a trained horse).
Composition:  wi (will/intention) + no (negation/absence) + ra (force/energy) =
              will-without-force = the purposive quality of having intention without
              directing force against others. Head-final: ra (force) is head; wi-no
              specifies the kind of force-absence — it is the force of will that is
              absent, not all force.
Register:     standard / ethical
Domain:       ethics / affect
Status:       active
First use:    Matthew 5:5 (Beatitude: "the meek" = `lo-zo-li  wi-no-ra`).
Notes:        The Greek praus was used of a horse that had been trained to submit
              its strength to the rider — not a weak horse but a disciplined one.
              wi-no-ra captures this: not lack of will or capacity, but will that
              does not assert itself with force against others. Compare:
                wi        = will/intention alone (force may be implied)
                wi-no-ra  = will without aggressive force = meekness
                no-ra     = without force (could be mere weakness)
              The compound wi-no-ra is richer than either component: it specifies
              that the will exists but chooses not to force.
Related:      wi (primitive: will/intention), no (primitive: negation), ra (force),
              su-fa (W133: pure in heart — inner organization rather than force-type)
```

---

**W133**
```
Form:         su-fa
Type:         compound
Class:        quality / inner state
Definition:   purity of heart; structured affect; the state of one whose affective
              substrate is organized, ordered, and free from inner conflict or
              corruption. Not merely an absence of evil but a positive orderliness of
              the inner life. Greek katharos (pure, clean, unmixed). In the Beatitude:
              "pure in heart" = those whose inner affective life is well-structured.
Composition:  su (structure/order) + fa (affective substrate) = ordered-affect =
              the quality of having an organized and non-conflicted affective substrate.
              Head-final: fa (affective substrate) is head; su specifies that the
              affective substrate in question is characterized by order rather than
              disorder.
Register:     standard / ethical / theological / contemplative
Domain:       ethics / affect / theology
Status:       active
First use:    Matthew 5:8 (Beatitude: "the pure in heart" = `lo-zo-li  su-fa`).
Notes:        Three-stage pipeline recall: se → fa → to. The fa stage is the
              pre-evaluative felt-tone substrate. su-fa = fa that is ordered/clear:
              the felt substrate is not muddied by conflicting desires, self-deception,
              or disordered impulse — it is structured. This allows se (perception) to
              reach to (concept-formation) without distortion.
              In the Beatitude, su-fa is the condition that allows "seeing God" (lo-ze
              lo-be-go-li  se): only when fa is ordered (su-fa) does the perception
              (se) of the divine reach the to stage without distortion.
              Compare:
                fa-no   (W095) = affect inactive (possibly numb, not ordered)
                su-fa          = affect actively ordered, structured = purity
Related:      su (primitive: structure/order), fa (primitive: affective substrate),
              fa-ki (W093), fa-de (W094), vo-ne (W118), wi-no-ra (W132)
```

---

- [ ] Review W002 (su-mu-li) — does it conflict with the derivational marker stack order?
- [ ] Develop domain-specific sub-lists once domains are finalized (see ontology/domains.md)
