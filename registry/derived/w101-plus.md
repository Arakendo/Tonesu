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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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
Status:       pending
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

---

## Matthew 5–7 Supplemental Intake (W134–W137)

**W134**
```
Form:         re-ka-ne-li
Type:         compound
Class:        person / role
Definition:   peacemaker; one who habitually creates or restores bonds between
              parties; a person characterized by the recurring deliberate act of
              building and healing relational connections. Greek eirēnopoios
              (peace-maker). The person whose characteristic intentional activity
              is ne-creation: bringing separated or opposing parties into mutual
              relation.
Composition:  re (recurrence/cycle) + ka (deliberate action) + ne (relation/bond)
              + li (person) = person-of-recurring-deliberate-bond-creation. Default
              right-branching: re modifies [ka-ne-li]; ka-ne-li = deliberate-bond-
              person = one whose intentional action is bond-building. re specifies
              that this is their characteristic recurring activity, not a one-off act.
Register:     standard / ethical / theological
Domain:       ethics / social / theology
Status:       pending
First use:    Matthew 5:9 (Beatitude: "blessed are the peacemakers" =
              `lo-zo-li  re-ka-ne-li  vo`).
Notes:        The active, repeated nature of the peacemaker's work is encoded in
              the compound: re-ka specifies that bond-creation is the person's
              recurrent pattern, not an isolated gesture.
              "Making peace" in Tonesu is constitutively relational: peace = the
              state of bonds existing. The peacemaker is the agent who creates
              those bonds. Contrast ka-ne (a single bond-creating act) with
              re-ka-ne-li (the person for whom this is habitual).
              Extended form: re-ka-ne-su = the institution or practice of peacemaking.
Related:      re (primitive: recurrence), ka (primitive: deliberate action),
              ne (primitive: relation/bond), li (primitive: person),
              ne-li (bonded person / neighbor), ka-ne-de (W092: bond dissolution),
              wi-de-li (W124: adversary/enemy — the opposite pole)
```

---

**W135**
```
Form:         pa-zo-li
Type:         compound
Class:        entity / domain
Definition:   the world; the inhabited realm; the place of human persons; the
              domain of human social life and presence. The territorially-bounded
              region characterized by the presence of human living-persons. Roughly
              Greek kosmos in its spatial/social sense. Complements pa-be (upper
              space / heaven) in the theological-cosmological pair.
Composition:  pa (place/territory) + zo (living thing) + li (person) = territory
              of living-persons. Default right-branching: pa modifies [zo-li];
              zo-li (W148) = human-class organism = living person. pa-[zo-li] =
              the place of human-organisms = the human inhabited world.
Register:     standard / theological
Domain:       geography / social / theology
Status:       pending
First use:    Matthew 5:14 ("you are the light of the world" — the world as the
              human realm that can be illuminated; metaphor anchored in pa-zo-li
              as the inhabited human domain).
Notes:        pa-zo-li is the social/inhabited world, not merely the physical earth.
              Contrast:
                pa-ma    = material-ground / earth-substance (the physical planet)
                pa-zo-li = the world as inhabited human territory
              In Matthew 5:13 the "earth" in "salt of the earth" uses `go-pa-ma`
              (of the material ground). pa-zo-li is the social-register "world"
              in 5:14 (light of the world) and 6:10 (thy kingdom come — the world
              that needs the coming).
              Cosmological pair: pa-be (upper space, heavenly realm) ::
              pa-zo-li (lower space, human realm). These form the Matthew 5–7
              theological axis.
Related:      pa (primitive: place/territory), zo-li (W148: human person),
              pa-be (upper-space compound), pa-ma (material earth, distinct),
              pa-be'ka-li-su (W125: kingdom of heaven)
```

---

**W136**
```
Form:         fa-wi-zi
Type:         compound
Class:        affect state / desire
Definition:   lust; the affective desire for coupling; the affect state in which
              will is oriented toward a mutual-coupling event with another person
              as its direct object. A specific sub-type of fa-wi (affect-will =
              desire) directed toward zi (mutual coupling). Contrasted with
              fa-wi-de (W127: temptation = affect-will toward harm in general).
              Greek epithumia (desire/lust) as used in Matthew 5:28.
Composition:  fa (affective substrate) + wi (will/intention) + zi (mutual/coupling
              event) = affect-will-toward-coupling = desire directed at a coupling
              event. Default right-branching: fa modifies [wi-zi]; wi-zi =
              will-toward-coupling = desire-for-coupling. fa-[wi-zi] = the
              affective substrate underlying coupling-desire = lust.
Register:     standard / ethical
Domain:       ethics / biology / affect
Status:       pending
First use:    Matthew 5:28 (5th antithesis: "anyone who looks at a woman
              lustfully has already committed adultery in his heart").
Notes:        Status: proposed — one primary corpus site. Monitor until a second
              independent attestation arises.
              fa-wi-zi is a narrower form within the fa-wi family:
                fa-wi      = desire / the will-affect state (unspecified object)
                fa-wi-de   (W127) = temptation = affect-will toward harm (general)
                fa-wi-zi   = lust = affect-will toward coupling (specific)
              In Matthew 5:28 the interior act is morally equivalent to the
              external act. This is consistent with Tonesu's perception pipeline:
              se → fa → to. fa-wi-zi lives in the fa stage, before any overt act
              reaches the to (concept/judgment) stage.
Related:      fa (primitive: affective substrate), wi (primitive: will/intention),
              zi (primitive: mutual/coupling event), fa-wi-de (W127: temptation),
              ne-zi-re (W131: spouse), zi-zo (W106: biological coupling event)
```

---

**W137**
```
Form:         vo-mu
Type:         compound
Class:        entity / artifact
Definition:   garment; clothing; a value-bearing artifact worn on the body;
              any fabric or material item worn to confer warmth, covering, or
              social-aesthetic value. The paradigmatic artifact whose purpose is
              value-expression through covering. Greek himation (outer garment /
              cloak) and the general clothing class in Matthew 6:28–30.
Composition:  vo (value/quality) + mu (artifact/physical object) = value-artifact
              = a physical object defined by its value-bearing function. Clothing
              is the canonical example: it exists to confer warmth, covering, or
              social value upon its wearer. Head-final: mu (artifact) is head;
              vo specifies that this artifact belongs to the value-domain.
Register:     standard / social
Domain:       material / social
Status:       pending
First use:    Matthew 6:28–30 ("consider the lilies... yet I tell you that not
              even Solomon in all his splendor was dressed like one of these" —
              vo-mu as clothing compared against the lily's natural display).
Notes:        Status: proposed — one primary corpus context. Monitor.
              The Matthew 6:28–30 comparison is structurally clean: both Solomon's
              vo-mu (crafted value-artifact) and the lily's display express `vo`
              (value/quality); the lily's is natural (not-mu), Solomon's is crafted.
              vo-mu covers: robes, cloaks, everyday clothing — any worn artifact
              serving value-expression functions.
Related:      vo (primitive: value/quality), mu (primitive: artifact/object),
              ka-mu (W047: tool / action-instrument — another mu-family member)
```

---

## Genesis 1 Intake (W138–W149)

### Cosmology and Physical World

**W138**
```
Form:         pa-fe
Type:         compound
Class:        entity / spatial
Definition:   vault; firmament; sky-dome; the bounded spatial region above the
              earth; the perceptible sky as a defined horizontal boundary. Hebrew
              raqia (the stretched-out dome of the sky). The upper layer of the
              visible world, conceived as the bounding edge between terrestrial
              and celestial domains.
Composition:  pa (place/territory) + fe (boundary/limit/edge) = bounded-space =
              a spatial region defined by its boundary. Head-final: fe (boundary)
              is head; pa specifies the spatial domain — a place defined by its
              bounding edge. In Genesis usage: the specific sky-dome that bounds
              the upper visible region.
Register:     standard / cosmological / theological
Domain:       geography / cosmology / theology
Status:       pending
First use:    Genesis 1:6–8 (the vault God made to separate waters above from
              waters below; God named it 'sky').
Notes:        pa-fe is the dome-as-bounded-space — the vault conceived as a
              spatial region with a defining edge. This is distinct from a generic
              spatial region: the fe is the element that makes it a vault rather
              than open space.
              Celestial light-bodies are placed "at the vault" (`pa-pa-fe` = at/in
              the sky-vault — the particle-pa and root-pa overlap is documented as
              intentional; see Grammar §Particle–Root Overlap Policy).
              Extension forms:
                be-pa-fe   = upper-vault = region above the sky
                de-pa-fe   = sub-vault = region below the sky
                lu-mu pa-pa-fe = light-bodies in/at the vault (Gen 1:17)
Related:      pa (primitive: place/territory), fe (primitive: boundary/limit),
              lu-mu (W139: light-body, placed in pa-fe),
              ma-ki (matter-in-motion / water, separated by pa-fe)
```

---

**W139**
```
Form:         lu-mu
Type:         compound
Class:        entity / celestial
Definition:   light-body; luminous celestial object; any natural light-emitting
              body in the sky. General class covering sun, moon, and stars as
              instances. Key derived forms: nu-be-lu-mu (great light-body = sun),
              nu-de-lu-mu (lesser light-body = moon), pu-lu-mu (collective light-
              bodies = stars).
Composition:  lu (light) + mu (artifact/physical object) = light-object = a
              physical body that emits or embodies light. Head-final: mu (physical
              object) is head; lu specifies the defining quality — objects defined
              by their light-emitting nature.
Register:     standard / astronomical / theological
Domain:       astronomy / cosmology / theology
Status:       pending
First use:    Genesis 1:14–19 (the two great light-bodies and the collective stars;
              placed in the vault to govern lu-ti / no-lu-ti and serve as signs).
Notes:        lu-mu covers all light-emitting celestial bodies as a class. In
              Genesis 1:16 two primary lu-mu specimens receive governing functions:
              the nu-be-lu-mu over lu-ti (W140: daytime) and the nu-de-lu-mu over
              no-lu-ti (W141: nighttime).
              mu is the artifact/physical-object root. In the Genesis context,
              celestial bodies are things God made; mu is appropriate. In a
              purely astronomical register mu still works as "physical object."
              Derived family:
                nu-be-lu-mu   = large-scale light-body = the sun
                nu-de-lu-mu   = decreasing/lesser light-body = the moon
                pu-lu-mu      = plural/collective light-bodies = stars
Related:      lu (primitive: light), mu (primitive: artifact/object),
              pa-fe (W138: vault where light-bodies placed),
              lu-ti (W140: daytime governed by nu-be-lu-mu),
              no-lu-ti (W141: nighttime governed by nu-de-lu-mu),
              se-lu (W130: eye, the light-perception organ)
```

---

**W140**
```
Form:         lu-ti
Type:         compound
Class:        temporal entity
Definition:   daytime; the light-period; the temporal interval characterized by
              the presence of light; daylight hours. The named temporal phase
              defined by lu (light). Pair: no-lu-ti (W141: nighttime).
Composition:  lu (light) + ti (time/temporal sequence) = light-time = the time-
              period defined by light. Head-final: ti (time) is head; lu specifies
              the defining quality of the temporal period — the kind of time
              characterized by light.
Register:     standard
Domain:       general / temporal
Status:       pending
First use:    Genesis 1:14–18 ("lights in the vault to separate the lu-ti from
              the no-lu-ti"; the greater light-body governs lu-ti).
Notes:        lu-ti / no-lu-ti (W141) form a minimal pair covering the two
              alternating temporal phases of the daily cycle. Together they
              partition the day into light-period and dark-period.
              Promoted from Monitor: originally marked compositional and low-
              priority, but high corpus frequency in Genesis temporal framing
              and frequent recurrence in temporal-frame contexts justifies active
              registration.
              Related temporal forms: ti-mi (W109: now), ti-de (W041: past),
              ti-be (W040: future), ti-re (W103: next cycle/day).
Related:      lu (primitive: light), ti (primitive: time/sequence),
              no-lu-ti (W141: nighttime), lu-mu (W139: light-bodies that govern
              lu-ti)
```

---

**W141**
```
Form:         no-lu-ti
Type:         compound
Class:        temporal entity
Definition:   nighttime; the dark-period; the temporal interval characterized by
              the absence of light; night hours. The negation-of-light temporal
              phase. Hebrew layil (night). Pair: lu-ti (W140: daytime).
Composition:  no (negation/absence) + lu (light) + ti (time/temporal sequence)
              = not-light-time = the time-period defined by the absence of light.
              Head-final: ti (time) is head; no-lu specifies the temporal character
              by the absence of the defining quality (light).
Register:     standard
Domain:       general / temporal
Status:       pending
First use:    Genesis 1:14–19 ("lights to govern the day and the night"; the
              lesser light-body governs no-lu-ti = the dark-period).
Notes:        no-lu-ti applies the productive no-X pattern (no-lu = dark;
              no-ki = still; no-su = structureless; etc.) to the temporal domain:
              no-lu-ti = the time that is no-lu (without-light) = night.
              "There was evening, and there was morning" in Genesis uses fe-ki
              (boundary-onset) for each phase; no-lu-ti and lu-ti (W140) are the
              named periods that those boundaries delimit.
Related:      no (primitive: negation/absence), lu (primitive: light),
              ti (primitive: time/sequence), lu-ti (W140: daytime),
              lu-mu (W139: light-bodies that govern this period)
```

---

### Botany and Food

**W142**
```
Form:         du-zo-su
Type:         compound
Class:        entity / biological
Definition:   fruit; plant-result; the structured product generated by a plant
              organism; the biological output structure of a plant — the mature
              product of plant growth. Hebrew peri (fruit) in its botanical sense.
Composition:  du (result/product) + zo (living thing) + su (structured product)
              = result-of-plant. Default right-branching: du modifies [zo-su];
              zo-su = plant (structured/organized living thing). du-[zo-su] =
              the result-product of a plant = fruit (the visible, produced output
              of plant growth).
Register:     standard / biological / culinary
Domain:       biology / botany / food
Status:       pending
First use:    Genesis 1:11–13 ("let the land produce vegetation: seed-bearing
              plants and trees on the land that bear fruit with seed in it").
Notes:        du-zo-su is the product of the plant (as a du / result). Contrast:
                zo-su        = the plant itself (structured living thing)
                zo-su-be     (W143) = seed (the growth-initiating product of a
                                       plant)
                du-zo-su     = fruit (the mature structural product of a plant)
              The pair zo-su-be / du-zo-su covers the two key botanical products:
              the reproductive structure and the mature fruit structure. In Genesis
              1, trees produce du-zo-su (`be-zo-su lo du-zo-su`) containing
              zo-su-be (`lo-zo-su-be`).
Related:      du (primitive: result/effect), zo (primitive: living thing),
              su (primitive: structure), zo-su-be (W143: seed),
              zo-ra-ma (W144: food — general class)
```

---

**W143**
```
Form:         zo-su-be
Type:         compound
Class:        entity / biological
Definition:   seed; plant-growth-product; the biological propagule of a plant;
              the structure produced by a plant that initiates new growth of its
              kind. Hebrew zera (seed). Narrower than zo-be (general organism-
              growth-product, which covers eggs and all reproductive structures);
              zo-su-be is specifically the plant-class reproductive structure.
Composition:  zo (living thing) + su (structure/organized form) + be (growth/
              development) = plant-[structured-growth-unit]. Default right-
              branching: zo modifies [su-be]; su-be = structured-growth-form =
              the organized structure that generates growth. zo-[su-be] = the
              organism's structured-growth-unit = a plant's growth-producing
              structure = seed.
Register:     standard / biological / agricultural
Domain:       biology / botany / agriculture
Status:       pending
First use:    Genesis 1:11–12 ("seed-bearing plants"; "trees that bear fruit
              with seed in it").
Notes:        zo-su-be is plant-specific. The more general organic growth-product
              is zo-be (organism-growth = any product of organismal growth,
              including eggs). zo-su-be narrows this to the plant class: the
              specific growth-initiating structure that carries the plant's
              reproductive capacity.
              In Genesis 1, the pair du-zo-su (W142: fruit) + zo-su-be (seed)
              fills the "fruit with seed in it" formula: du-zo-su containing
              zo-su-be = the reproductive completeness of a fruit-bearing plant.
Related:      zo (primitive: living thing), su (primitive: structure),
              be (primitive: growth), zo-be (general organism-growth-product),
              du-zo-su (W142: fruit)
```

---

**W144**
```
Form:         zo-ra-ma
Type:         compound
Class:        entity / material
Definition:   food; organism-energy-substrate; the material that provides energy
              and sustenance to living organisms; nutritive matter consumed to
              sustain biological energy. Covers all food types as a general class.
              Hebrew okhel (food) in its biological-provision sense (Genesis
              1:29–30).
Composition:  zo (living thing) + ra (force/energy) + ma (matter/substance)
              = organism-energy-matter. Default right-branching: zo modifies
              [ra-ma]; ra-ma = energy-matter = matter characterized by its energy
              content. zo-[ra-ma] = the organism's energy-matter = the matter
              that is the energy-source for organisms = food.
Register:     standard / biological / culinary
Domain:       biology / food / ecology
Status:       pending
First use:    Genesis 1:29–30 (God assigns all seed-bearing plants and trees as
              zo-ra-ma for humans; every green plant as zo-ra-ma for animals).
Notes:        zo-ra-ma builds on zo-ra (W117: life-energy of organisms) by adding
              ma (the material substrate that carries or provides that energy).
              zo-ra is the vitality within an organism; zo-ra-ma is the external
              material that supplies zo-ra.
              zo-ra-ma covers all food types without distinguishing: animal,
              plant, seed-based. The Genesis assignment (1:29–30) uses it for
              both human and animal provisioning.
              Extension form:
                zo-ra-ma-su   = food system / organized food supply
Related:      zo-ra (W117: life-energy / animating vitality),
              zo (primitive: living thing), ra (primitive: energy/force),
              ma (primitive: matter/substance), du-zo-su (W142: fruit — a class
              of zo-ra-ma for humans)
```

---

### Zoological Taxonomy

**W145**
```
Form:         wi-zo
Type:         compound
Class:        entity / biological
Definition:   wild animal; autonomous organism; a living thing characterized by
              self-directed will rather than human direction; an organism that
              acts according to its own instinct and purpose without domestication.
              Hebrew hayah (living creature / wild animal) as contrasted with
              livestock in Genesis 1:24–25.
Composition:  wi (will/intention) + zo (living thing/organism) = will-governed-
              organism = organism defined by self-directed behavior. Head-final:
              zo (living thing) is head; wi specifies the defining quality —
              this is the kind of organism characterized by autonomous will-
              direction.
Register:     standard / biological
Domain:       biology / ecology
Status:       pending
First use:    Genesis 1:24–25 ("let the land produce living creatures: the
              livestock, the creatures that move along the ground, and the wild
              animals" — wi-zo = wild animals, contrasted with zo-se-ne = herd/
              social animals).
Notes:        wi-zo marks the Genesis 1:24–25 three-way land-animal taxonomy:
                wi-zo      = wild (self-willed) organisms
                zo-se-ne   = social-relational herd animals = livestock (KNM-007)
                ma-zo-ki   (W146) = ground-crawling organisms
              The structural contrast is clear: wi-zo are defined by will (wi);
              zo-se-ne are defined by social-relational bonds (ne). Domestication
              is the process of transitioning a wi-zo toward zo-se-ne status —
              replacing autonomous will-direction with human-directed behavior.
Related:      wi (primitive: will/intention), zo (primitive: living thing),
              zo-se-ne (herd animals / livestock, KNM-007),
              ma-zo-ki (W146: crawlers), wi-de-li (W124: adversary — different
              domain but same wi-root)
```

---

**W146**
```
Form:         ma-zo-ki
Type:         compound
Class:        entity / biological
Definition:   crawler; ground-moving creature; any organism that moves along the
              material ground; creatures characterized by movement at or near the
              surface of the earth. Hebrew remes (creeping/crawling things) in
              Genesis 1:24–26. The class of small or low-moving organisms.
Composition:  ma (matter/material ground) + zo (living thing) + ki (motion/change)
              = ground-level-living-movement. Default right-branching: ma modifies
              [zo-ki]; zo-ki = living-movement = a living thing in characteristic
              motion. ma-[zo-ki] = ground-level living-mover = organisms that move
              at the level of the material ground = crawlers.
Register:     standard / biological
Domain:       biology / ecology
Status:       pending
First use:    Genesis 1:24–26 ("the creatures that move along the ground"
              alongside zo-se-ne = livestock and wi-zo = wild animals).
Notes:        ma-zo-ki completes the three-way land-animal taxonomy alongside
              zo-se-ne and wi-zo (W145). In Genesis 1:26 all three classes are
              objects of humanity's ka-li-su (W147: governance mandate):
              `lo-zo  ka-li-su` = exercise governance over organisms.
              The class covers: insects, worms, reptiles, and any creature whose
              characteristic motion is at ground level. Contrast: zo-se-so-di
              (birds, KNM-005) for airborne organisms.
Related:      ma (primitive: matter/ground), zo (primitive: living thing),
              ki (primitive: motion/change), wi-zo (W145: wild animals),
              zo-se-ne (herd animals, KNM-007)
```

---

### Governance, Persons, and Theology

**W147**
```
Form:         ka-li-su
Type:         compound
Class:        action / process
Definition:   governance; dominion; coordinated stewardship; the structured
              exercise of deliberate coordinated authority over persons or
              organisms within a domain. The practice of organizing and directing
              participants through intentional action. Hebrew radah (have dominion)
              in Genesis 1:26, 28. Also the base compound in pa-be'ka-li-su
              (W125: kingdom of heaven = the governance domain of the upper space).
Composition:  ka (deliberate action) + li (person/participant) + su (structure/
              organized form) = deliberate-person-organization. Default right-
              branching: ka modifies [li-su]; li-su = organized-participants /
              coordinated-person-structure. ka-[li-su] = deliberate [organized-
              participant-coordination] = the exercise of structured governance.
Register:     standard / political / theological
Domain:       governance / social / theology
Status:       pending
First use:    Genesis 1:26 ("let them have dominion over the fish of the sea and
              the birds in the sky and over all the living creatures" =
              `lo-zo  ka-li-su`).
Notes:        ka-li-su is the active predicate of governance:
                la-X  lo-Y  ka-li-su  = X governs Y
              Also: lo-ka-li-su as nominal = the governance / the dominion (as a
              thing held or enacted).
              The same compound forms the base of pa-be'ka-li-su (W125) — the
              "Kingdom of Heaven" = the governance domain of the upper space. This
              confirms ka-li-su as the canonical governance compound before W125
              was registered.
              Derived compound family:
                ka-li-su-li        = governor / one who exercises dominion
                pa-be'ka-li-su     = W125 (the governance domain of the heavens)
Related:      ka (primitive: deliberate action), li (primitive: person),
              su (primitive: structure), pa-be'ka-li-su (W125: kingdom of heaven),
              li-su-li (W001: leader / coordinator), zo-li (W148: human person,
              the governance subject in Genesis 1:26)
```

---

**W148**
```
Form:         zo-li
Type:         compound
Class:        entity / person class
Definition:   human person; a living-being-person; a member of the human kind-
              class; any person understood as a living social organism. The general
              class term for human beings — sex-neutral, role-neutral, and social-
              position-neutral. Used wherever a general person subject or patient
              is needed.
Composition:  zo (living thing/organism) + li (person) = living-person = an
              organism that is a person. Head-final: li (person) is head; zo
              specifies that this person is understood in terms of their organismal
              nature — a person who is a living thing.
Register:     standard
Domain:       general / social / biology
Status:       pending
First use:    Widely used across corpus; the standard subject-of-predication in
              Matthew 5–7 Beatitudes (`lo-zo-li  wi-no-ra`, `lo-zo-li  su-fa`,
              etc.) and Genesis 1:26–28 ("let us make mankind" = `lo-zo-li  ka-be`).
Notes:        zo-li is the unmarked general person-class term. Specific terms build
              on zo-li via modifier or compound:
                go-zo-li   = generative-role-person (biological male, Gen 1:27)
                du-zo-li   = result-role-person (biological female, Gen 1:27)
                ka-li-su-li = governor (ka-li-su, W147, + li)
              Plural/collective: `pu-zo-li` = all persons / humanity collectively.
              zo-li has been used pervasively across corpus without a formal
              registry entry. This admission retroactively registers the form and
              confirms its active status.
Related:      zo (primitive: living thing), li (primitive: person),
              zi-zo-go (W107: go-role in coupling),
              zi-zo-du (W108: du-role in coupling),
              pa-zo-li (W135: the world / place of human persons),
              be-go-li-si (W149: creator-representation / image)
```

---

**W149**
```
Form:         be-go-li-si
Type:         compound
Class:        entity / representation
Definition:   creator-representation; image; the emergent structural likeness of
              the one who brought something into being; the form in which a created
              thing bears the mark of its creator's nature. Hebrew tselem
              (image/likeness) in Genesis 1:26–27: "in our image." Any
              representation that is structurally produced by and corresponds to
              a personal creative origin.
Composition:  be (growth/emergence/generation) + go (cause/origin) + li (person)
              + si (signal/representation) = signal/image that emerges from a
              person-cause. Default right-branching: be modifies [go-li-si];
              go-li-si = person-origin-signal = a representation/signal that
              originates from a person. be-[go-li-si] = the emergent/generated
              form of a person-origin-signal = the image produced from/by its
              originating person.
Register:     theological / philosophical
Domain:       theology / philosophy / representation
Status:       pending
First use:    Genesis 1:26–27 ("let us make mankind in our image" and "God
              created mankind in his own image" — in both verses the origin-frame
              marker precedes the compound: `go-be-go-li-si` = from/after the
              creator-representation).
Notes:        In the corpus construction: `go-be-go-li-si` = from/after the
              creator-representation = "in the image of the creator." The `go`
              particle here marks origin-frame: humanity's form originates after
              / corresponds to the creator-representation.
              be-go-li-si is not a generic si (signal/representation) — it
              specifically encodes the causal relationship: be-go = generated-
              from-origin; li = person; si = representation. A representation
              produced by a creative person-origin. The Hebrew tselem covers
              images, statues, likenesses; all are structural instances of
              be-go-li-si.
              Note on "established THO-001": this compound was developed during
              the THO theological-attribute batch work (pre-Matthew), but first
              received a W-number in this intake.
Related:      be (primitive: growth/generation), go (primitive: cause/origin),
              li (primitive: person), si (primitive: signal/representation),
              zo-li (W148: human person, the entity created in this image),
              ka (primitive: deliberate action)
```

---

## Exodus 3:1–15 Intake (W150–W160)

*Batch: EXO-001. First-pass translation of Exodus 3:1–15 (burning bush / divine name). All entries proposed; corpus basis S398–S417. Full analysis in `corpus/translations/Bible/exodus-3-1-15.md`.*

---

**W150**
```
Form:         zo-su-ka-li
Type:         compound
Class:        agent
Definition:   shepherd; one who tends and maintains organized living things.
              The person whose deliberate action sustains a structured group
              of organisms. Covers any herdsman, flock-tender, or pasture-keeper.
Composition:  zo (living thing) + su (structure/order) + ka (deliberate action)
              + -li (agent suffix) = agent of deliberate structured-organism-
              maintenance. Suffix stacking order: root chain (zo-su-ka) →
              role marker (-li). zo-su = structured organism base (plant class
              / pasture); ka = deliberate action on it; -li = the one who does.
Verbal form:  zo-su-ka (without -li) used as action verb in corpus.
Register:     general
Domain:       general / agriculture
Status:       pending
First use:    S398 — la-na-Moses  lo-zon  ka-zo-su-ka  ne-na-Yitro
              (Moses shepherded Jethro's flock)
Notes:        "Flock" uses zon (CLQ-006a, zo-se-ne herd ungulates) in the
              natural casual form. zo-su-ka-li is the formal agent noun;
              zo-su-ka is used verbally.
Related:      zo (primitive: living thing), su (primitive: structure),
              ka (primitive: deliberate action), -li (agent suffix),
              zon / zo-se-ne (herd ungulate class)
```

---

**W151**
```
Form:         ra-lu-ki
Type:         compound
Class:        process
Definition:   fire; the energetic-luminous process; energy emitting light while
              in motion. Physical fire as a natural process. Distinct from
              ra (energy alone) or lu (light alone): fire is specifically the
              coupled process of energy releasing light through motion/change.
Composition:  ra (energy/force) + lu (light/visibility) + ki (motion/process)
              = energy-light-in-motion = fire as process.
Register:     general
Domain:       general / physics / theology
Status:       pending
First use:    S401 — ro-ra-lu-ki (through fire; instrument: the fire medium
              through which the angel appeared)
Notes:        Used both as noun compound (the fire) and process predicate
              (was burning / fire-process happening). S402: la-zo-su  ra-lu-ki
              no  de = the plant fire-processed but did not decrease = the
              burning bush miracle.
              Related compound: no-de'ra-lu-ki (fire-without-decrease) is a
              CLQ-EXT candidate — the miracle as a lexical chunk. Not registered
              yet; awaiting CLQ-EXT rule resolution.
Related:      ra (primitive: energy), lu (primitive: light), ki (primitive: motion),
              pa-vo-fe (W153: holy ground, the place of this fire event)
```

---

**W152**
```
Form:         ki-ne
Type:         compound
Class:        entity (artifact)
Definition:   sandal; footwear; what is bonded to the foot to enable or mark
              motion. The motion-connector worn on the body for movement.
Composition:  ki (motion) + ne (connection/bond) = motion-bond = what binds
              to the body to facilitate or mark movement.
Register:     general
Domain:       general / material culture
Status:       pending
First use:    S406 — lo-ki-ne  ka-de-ne (your sandals: deliberately unbind them)
Notes:        The command to remove sandals ("take off your shoes, for you are
              standing on holy ground") forces this compound. ki-ne as footwear
              is a clean compositional reading: sandals are literally the
              motion-bond between foot and ground.
              Removal command: ka-de-ne lo-ki-ne = deliberately-unbind the
              motion-bond = take off the sandals.
Related:      ki (primitive: motion), ne (primitive: relation/bond),
              pa-vo-fe (W153: holy ground, the reason for removal)
```

---

**W153**
```
Form:         pa-vo-fe
Type:         compound
Class:        place
Definition:   holy ground; a place whose value-status is explicitly set apart
              / bounded. A location defined by its elevated value boundary — not
              merely a good place (pa-vo) but a place whose goodness has a
              formal boundary that separates it from ordinary space.
Composition:  pa (place/space) + vo (value/quality) + fe (boundary/limit)
              = a place whose value has a defined boundary = set-apart place =
              holy ground. Structural parallel to to-fe-li (epistemic guardian:
              one who bounds knowledge) and pa-no-fe (omnipresence: place without
              boundary). pa-vo-fe is the bounded version: a place whose holiness
              is a specific, locatable boundary — not diffuse goodness but
              designated sacred space.
Register:     theological / formal
Domain:       theology / sacred space
Status:       pending
First use:    S406 — pa-mi  pa-vo-fe (this place [is] holy ground)
Notes:        Zero-copula predication: pa-mi  pa-vo-fe = my-place  value-bounded-place
              = this place is holy ground. The removal of sandals (W152) is the
              behavioral correlate of the pa-vo-fe designation.
              Contrast: pa-vo (value-place = good land, used in S410) is the
              property form without the explicit boundary marker; pa-vo-fe adds
              the sanctification boundary. fa-vo-fe would be the inward equivalent
              (pure in spirit / bounded interior value) — not yet attested.
Related:      pa (primitive: place), vo (primitive: value/quality),
              fe (primitive: boundary), ki-ne (W152: sandal, removed at holy ground),
              to-fe-li (W—: epistemic guardian, structural parallel)
```

---

**W154**
```
Form:         fa-ra
Type:         compound
Class:        state / affect
Definition:   fear; awe; forceful affect. The intense interior state of
              overwhelming force arising in the affective substrate. Covers
              both fear (aversive overwhelming force) and awe (overwhelm with
              a positive or sublime valence) — context provides the valence.
Composition:  fa (affective substrate) + ra (energy/force) = felt-interior-force
              = forceful affect = fear / awe. Distinct from fa-de-ra (W155:
              suffering = affect-decrease-force, i.e. force draining away);
              fa-ra is the presence of overwhelming force, not its diminishment.
Register:     general
Domain:       general / affect / theology
Status:       pending
First use:    S408 — fa-ra  go  ka-se  lo-Elohim (fear/awe because deliberately
              looking at Elohim = Moses was afraid to look at God)
Notes:        Moses hid his face because of fa-ra: the affect-force of the
              divine presence was overwhelming. fa-ra covers the full range from
              primal fear to profound awe — both are the same affective structure
              (intense inner force); the valence (is this threatening or sublime?)
              is context-determined, not encoded in the compound.
Related:      fa (primitive: affective substrate), ra (primitive: energy/force),
              fa-de-ra (W155: suffering, affect-decrease-force — contrasting form),
              fa-wi-zi (W136: lust, affect-desire-to-couple)
```

---

**W155**
```
Form:         fa-de-ra
Type:         compound
Class:        state / affect
Definition:   suffering; misery; the felt interior experience of diminishing
              force. The affective substrate registering the decay of capacity,
              vitality, or will. Covers physical suffering, social oppression's
              felt dimension, grief, and exhaustion as experiences — the shared
              structure is affect registering a decrease in force.
Composition:  fa (affective substrate) + de (decay/decrease) + ra (energy/force)
              = affect-decrease-force = felt interior of force draining away =
              suffering.
Register:     general
Domain:       general / affect / social / theology
Status:       pending
First use:    S409 — lo-fa-de-ra'zo-li-mi (the suffering of my people)
Notes:        The apostrophe in S409 is structurally essential: fa-de-ra'zo-li-mi
              = [fa-de-ra] modifies [zo-li-mi] = "my people's suffering."
              Without the apostrophe, fa-de-ra-zo-li-mi parses as a nonsense
              deep-right-branch. This sentence is a teaching case for when '
              is not optional at depth.
              Contrast: fa-ra (W154: fear/awe = affect + overwhelming force
              present). fa-de-ra is force decreasing; fa-ra is force overwhelming.
              Both belong to the force-affect family.
Related:      fa (primitive: affective substrate), de (primitive: decay/decrease),
              ra (primitive: energy/force), fa-ra (W154: fear/awe — contrasting)
```

---

**W156**
```
Form:         pa-ki
Type:         compound
Class:        process / concept
Definition:   liberation; place-motion; departure-from-a-place as an act or
              concept. The process of producing movement out of a confining
              location. Used as action verb (ka-pa-ki = to deliberately liberate)
              and as concept noun (pa-ki = the liberation itself).
Composition:  pa (place/space) + ki (motion/process) = place-motion = the
              act of moving from a place = departure, exodus, liberation.
Agent form:   pa-ki-li = liberator, one who produces departure-from-place.
Verbal form:  ka-pa-ki = deliberate act of place-motion = to liberate.
Register:     general / theological
Domain:       general / social / theology
Status:       pending
First use:    S410 — ka-pa-ki  lo-zo-li-mi  pa-na-Egypt (liberate my people
              from Egypt); second attestation S411.
Notes:        Liberation encoded as spatial: the Exodus is paradigmatically
              the production of place-motion. ka-pa-ki is the verbal form:
              deliberate-place-motion-action. The `ka` prefix adds the
              deliberateness (it is not accidental departure but an act of will).
              Two attestations in the same passage (S410, S411) confirm production
              of the concept under translation pressure rather than synthetic
              construction.
Related:      pa (primitive: place), ki (primitive: motion),
              -li (agent suffix: pa-ki-li = liberator),
              ka (primitive: deliberate action: ka-pa-ki = liberation act as W160)
```

---

**W157**
```
Form:         pa-su
Type:         compound
Class:        place
Definition:   mountain; hill; structured place. A location defined by its
              physical organization / elevated structure. Rocky elevated terrain
              as a place that has order and structure imposed by geological
              formation.
Composition:  pa (place/space) + su (structure/order) = structured place =
              mountain / elevated structured terrain.
Register:     general
Domain:       general / geography / theology
Status:       pending
First use:    S400 — pa-su-be-go-li (mountain of God / Horeb as the creator's
              structured-place, aside annotation)
Notes:        pa-su (mountain) is compositionally clean. Physical mountains
              are structured places — their geological form is precisely an
              organized spatial structure. Second attestation S413 (pa-su-mi =
              my structured-place = "this mountain" / the mountain of God).
              Depth: pa-su-be-go-li is 5 morphemes; apostrophe grouping
              pa-su'be-go-li recommended since be-go-li is a registered unit.
Related:      pa (primitive: place), su (primitive: structure/order),
              be-go-li (creator-agent, registered), pa-vo-fe (W153: holy ground,
              location type on a mountain)
```

---

**W158**
```
Form:         si-ki-li
Type:         compound
Class:        agent
Definition:   messenger; envoy; one who carries a signal in motion. Any agent
              whose role is to transport a communication from one point to
              another. Hebrew malach (מַלְאָךְ) = messenger/envoy/angel — the
              same word used for human messengers and divine emissaries.
Composition:  si (signal/representation) + ki (motion/process) + -li (agent
              suffix) = signal-motion-agent = one who carries a signal by moving.
              Suffix stacking: root chain (si-ki) → role marker (-li).
              si-ki = signal-in-motion = a signal being transmitted.
              si-ki-li = the agent of that transmission = messenger.
Qualified form: si-ki-li'be-go-li = messenger of the creator = divine
              messenger = angel. The apostrophe binds be-go-li as the
              possessor/origin subcompound.
Register:     general / theological
Domain:       general / theology / communication
Status:       pending
First use:    S401 — la-si-ki-li'be-go-li  lu  lo-na-Moses  ro-ra-lu-ki
              (the angel of the LORD appeared to Moses in fire)
Notes:        si-ki-li is the generic messenger compound; the qualified form
              si-ki-li'be-go-li = divine messenger = angel follows the same
              ownership/origin pattern as other be-go-li compounds. The Hebrew
              malach covers both human envoys and divine ones — si-ki-li
              correctly covers both by the same compositional reading.
Related:      si (primitive: signal), ki (primitive: motion), -li (agent suffix),
              be-go-li (creator-agent: the source in the qualified form),
              ra-lu-ki (W151: fire, the medium of appearance)
```

---

**W159**
```
Form:         go-ne
Type:         compound
Class:        relation / philosophical
Definition:   self-originating relation; reflexive causal bond. The relation
              in which an entity's existence is its own origin and referent.
              The closest available Tonesu rendering of Hebrew 'ehyeh asher
              ehyeh' (I am who I am / I will be what I will be).
Composition:  go (cause/origin) + ne (relation/connection) = cause-relation =
              a bond whose nature is causal = the relation of self-origination.
              la-mi  go-ne  lo-mi = I stand in a causal-relational bond directed
              at myself = my existence is its own origin and relation.
Register:     theological / philosophical
Domain:       theology / philosophy / identity
Status:       pending
First use:    S415 — la-mi  go-ne  lo-mi (I am who I am / I will be what I will be)
              S416 — la-go-ne-mi (the self-originating-I, used as sender-name)
Notes:        IDENTITY COPULA GAP: go-ne lo-mi is a RELATION claim, not an
              IDENTITY claim. The divine tetragrammaton expresses constitutional
              self-identity — X is constitutionally identical with X — which
              Tonesu's current grammar cannot encode. go-ne  lo-mi encodes: "I
              stand in a causal-relational bond directed at myself" = aseity
              (self-grounded existence) + reflexive structure. This captures the
              philosophical content of necessary being but misses the grammatical
              self-identity. Whether go-ne develops a strong conventional identity
              reading through corpus frequency is an empirical question. See
              open-questions.md (THO-001 identity copula question).
              Do not resolve this gap by inventing a new particle.
Related:      go (primitive: cause/origin), ne (primitive: relation/connection),
              go-no-fe (necessary being, THO-001), be-go-li (creator-agent)
```

---

**W160**
```
Form:         ka-pa-ki
Type:         compound
Class:        action
Definition:   liberation act; deliberate production of departure from a place.
              The intentional act of creating movement out of a confining
              location. The verbal form of pa-ki (W156) — the deliberate,
              willed version of place-motion.
Composition:  ka (deliberate action) + pa (place/space) + ki (motion/process)
              = deliberate-place-motion = to liberate / to bring out / to cause
              departure. ka prefixes the pa-ki place-motion concept: the movement
              is not incidental but willed.
Register:     general / theological
Domain:       general / social / theology
Status:       pending
First use:    S410 — ka-pa-ki  lo-zo-li-mi  pa-na-Egypt (liberate my people
              from Egypt)
Notes:        Two attestations in the same passage (S410, S411) under translation
              pressure rather than synthetic construction — confirms the concept
              is productively needed. The Exodus is the paradigm case of
              ka-pa-ki: a specific, willed act of producing departure from a
              place of containment. ka-pa-ki-li = liberator (agent form, not
              yet attested but fully predictable).
Related:      ka (primitive: deliberate action), pa (primitive: place),
              ki (primitive: motion), pa-ki (W156: liberation/place-motion concept),
              pa-ki-li (liberator, agent form — predictable, unregistered)
```

---

## Last Supper / Eucharist Intake (W161–W168)

*Batch: LSP-001. First-pass translation of Luke 22:7–20 + Matthew 26:26–28 (Last Supper, institution of the Eucharist). All entries proposed; corpus basis S418–S438. Full analysis in `corpus/translations/Bible/last-supper.md`.*

---

**W161**
```
Form:         ka-du-zo-su
Type:         compound
Class:        entity (food)
Definition:   bread; the deliberately crafted plant-product. Grain food
              produced through intentional processing (grinding, forming,
              baking) of plant matter. The `ka-` prefix distinguishes it
              from du-zo-su (W142, fruit = naturally produced plant-result):
              bread is the deliberate artifact of plant production.
Composition:  ka (deliberate action) + du (result/product) + zo-su
              (structured plant, base from W143 seed context)
              = the deliberately produced result of structured plant matter
              = grain-product = bread/grain food.
              Right-branch parse: ka modifies [du-zo-su] = deliberate [plant-
              result] = deliberately crafted plant-product.
Register:     general / liturgical
Domain:       general / food / theology / liturgy
Status:       pending
First use:    S429 — la-na-Jesus  ka-ne  lo-ka-du-zo-su (Jesus took bread)
Notes:        The Eucharistic bread uses this compound. Leavened vs unleavened
              distinction not currently encoded (GAP-LSP-004). `ka-du-zo-su`
              covers all intentionally crafted grain foods; context distinguishes
              leavened/unleavened when needed.
              Contrast: du-zo-su (W142, fruit = natural plant-product, no ka-).
Related:      ka (primitive: deliberate action), du (primitive: result/product),
              zo-su (structured plant substrate), du-zo-su (W142: fruit/plant-result),
              zo-ra-ma (W144: food generally)
```

---

**W162**
```
Form:         de-ki'ma
Type:         compound
Class:        substance
Definition:   wine; fermented liquid. Any liquid that has undergone the
              decay/fermentation process: primarily wine (fermented grape-
              liquid), but also covers other fermented drinks. Fermentation
              is compositionally encoded as de (decay/diminishment) applied
              to ki'ma (liquid, W114): the liquid whose nature includes
              a decay process = fermented liquid = wine.
Composition:  de (decay/decrease/diminishment) + ki'ma (liquid, W114)
              = the liquid that has undergone decrease/transformation through
              decay = fermented liquid = wine.
              Note: ki'ma already carries the apostrophe internally; the full
              compound written form is `deki'ma`.
Register:     general / liturgical
Domain:       general / food / theology / liturgy
Status:       pending
First use:    S437 — ka-zo-ra-ma  lo-de-ki'ma  pu-yu (drink the wine, all of you)
Notes:        Eucharistic wine. Contrasts with du-zo-su (W142 = fruit, the raw
              origin material Jesus names in S428: "fruit of the vine"). The shift
              from du-zo-su to de-ki'ma is the institution act: what was named by
              origin is now named by transformation.
              Where Jesus says "fruit of the vine" (S428), he uses du-zo-su
              (the natural-produce designation). The cup that IS the covenant
              (S434–S437) uses zo-ki'ma-mi (my blood), not de-ki'ma — the
              covenant-sign is named by what it signifies, not by its chemical
              composition.
Related:      de (primitive: decay/decrease), ki'ma (W114: liquid),
              du-zo-su (W142: fruit/plant-result — the origin material),
              zo-ki'ma (W164: blood — what the Eucharistic cup signifies)
```

---

**W163**
```
Form:         zo-ma
Type:         compound
Class:        entity (body)
Definition:   body; the physical matter constituting a living organism.
              The corporeal substrate of life — flesh, the material form
              of a living being. Distinct from zo-ra (W117, life-energy/
              animating vitality) which is the energetic dimension; zo-ma
              is the material dimension.
Composition:  zo (living thing) + ma (matter/substance) = living-matter
              = the material substrate of an organism = body/flesh.
              Two-root compound; maximum compositional transparency.
Register:     general / liturgical / theological
Domain:       general / biology / theology / liturgy
Status:       pending
First use:    S431 — zo-ma-mi  ne  ze (This is my body)
              Also S436 — zo-ma-mi  ne  ze (Matthew parallel)
Notes:        The Eucharistic body formula: zo-ma-mi  ne  ze = "my body
              is this." The ne copula attributes the predicate "my body"
              to the bread. This is a property-attribution, not constitutional
              identity (GAP-LSP-001; see also THO-001/S356 identity copula gap).
              The metaphysical question of whether bread BECOMES body, or IS
              body, or symbolizes body — these distinctions fall in the gap
              Tonesu's ne cannot resolve without new grammar.
              Contrast: zo-ra (W117, animating vitality) = the energy-side
              of life; zo-ma is the matter-side.
Related:      zo (primitive: living thing), ma (primitive: matter/substance),
              zo-ra (W117: life-energy — energetic aspect, not material),
              zo-ki'ma (W164: blood — the liquid aspect of living matter)
```

---

**W164**
```
Form:         zo-ki'ma
Type:         compound
Class:        substance
Definition:   blood; the living liquid. The fluid that carries life within
              an organism — the liquid medium of biological vitality. The
              most direct Tonesu encoding: blood IS the living liquid, the
              zo (living) qualified ki'ma (liquid).
Composition:  zo (living thing) + ki'ma (liquid, W114) = living-liquid
              = the fluid of life = blood. Two roots plus the internally
              bound ki'ma apostrophe. Written: `zoki'ma`.
Register:     general / liturgical / theological
Domain:       general / biology / theology / liturgy
Status:       pending
First use:    S434 — ro-zo-ki'ma-mi (through my blood — instrumental)
Notes:        Eucharistic blood formula: zo-ki'ma-mi  ne  ze  go-ne-to-fe
              = "my blood is this, [being the] cause-of-the-covenant-
              relation." The shedding of blood uses de-zo-ki'ma-mi =
              "the decreasing of my living-liquid" = my blood being poured
              out (S435, S437).
              zo-ki'ma is the general biologically-occurring blood; its
              theological significance as covenant-medium comes from context
              and from the `go-ne-to-fe` clause (the causal-genitive of
              the covenant relationship).
Related:      zo (primitive: living thing), ki'ma (W114: liquid),
              de-ki'ma (W162: wine/fermented liquid — transformation parallel),
              zo-ma (W163: body — the material counterpart)
```

---

**W165**
```
Form:         ne-to-fe
Type:         compound
Class:        relation / legal
Definition:   covenant; a formally bounded agreement. A relationship with
              explicitly stated, permanently sealed terms — more than mutual
              acknowledgment (ne-to, W084: transient agreement) and more
              than a bond (ne: static relation). The fe (boundary/limit)
              seals the terms, making the agreement binding and formally
              delimited. Covers covenant, treaty, contract, any formally
              instituted bound-agreement.
Composition:  ne (relation/bond) + to-fe (epistemic boundary, W028)
              = relation-at-the-epistemic-boundary = a relationship with
              formally defined stated conditions.
              Right-branch parse: ne modifies [to-fe] = relation-of-the-
              epistemic-limit = a relationship whose terms are explicitly
              bounded/stated. Extension of ne-to (W084); fe seals it.
Qualified form: ti-be-ne-to-fe = new/fresh covenant: ti-be (W040)
              modifies ne-to-fe = the covenant that is freshly entering
              force = the new covenant. First attested S434.
Register:     theological / legal / formal
Domain:       theology / law / social
Status:       pending
First use:    S434 — ko-mu-ze  ne  ti-be-ne-to-fe  ro-zo-ki'ma-mi
              (this cup is the new covenant through my blood)
Notes:        The new covenant formula: ti-be-ne-to-fe = fresh/renewed
              formally bounded agreement. GAP-LSP-002: ti-be captures
              temporal freshness (the covenant entering force) but not
              qualitative surpassing (kainē vs neos distinction in Greek
              New Testament). The qualitative "better covenant" reading
              (Hebrews) may need a separate elaboration.
Related:      ne (primitive: relation/bond), to-fe (W028: epistemic boundary),
              ne-to (W084: mutual acknowledgment/agreement — base form),
              ti-be (W040: upcoming/fresh — qualifier for "new"),
              zo-ki'ma (W164: blood — the material sealing the covenant)
```

---

**W166**
```
Form:         to-ko-re
Type:         compound
Class:        action / concept
Definition:   remembrance; commemorative memory-return. The deliberate or
              ritual act of returning to stored knowledge of a person or
              event. Specifically: the Eucharistic anamnesis (ἀνάμνησις) —
              not merely recalling, but actively re-presenting the founding
              event. The `re` (return/cycle) element captures the recurring
              re-enactment dimension: each performance is a return to the
              founding event.
Composition:  to-ko (memory/stored knowledge, W027) + re (return/cycle,
              primitive) = memory-return = the act of returning to what
              is stored in memory = remembrance/anamnesis.
Verbal form:  ka-to-ko-re = to deliberately remember/commemorate (with ka-
              prefix). Used in the imperative: ka  lo-ze  to-ko-re-mi =
              "do this [as] my remembrance" (S432).
Register:     general / liturgical / theological
Domain:       theology / liturgy / memory
Status:       pending
First use:    S432 — ka  lo-ze  to-ko-re-mi (do this [as] my remembrance)
Notes:        The founding command of the Eucharist runs on one new compound
              carrying an ancient theological weight. to-ko-re encodes the
              Eucharistic structure: a deliberate act performed for the
              purpose of epistemic return (to-ko-re) to the founding speaker.
              The suffix -mi (my/mine) on to-ko-re gives "my remembrance" =
              the remembrance directed at/belonging to the speaker. Not
              "remember generally" but "remember me" = to-ko-re-mi.
              CLQ-EXT candidate: ka-to-ko-re-mi (deliberate-remember-me) as
              a compressed liturgical token; gated on 3 independent natural
              corpus attestations.
Related:      to-ko (W027: memory/stored knowledge), re (primitive: return/cycle),
              ka (primitive: deliberate action — ka-to-ko-re = to remember [verb])
```

---

**W167**
```
Form:         ka-pa-ki'ti-re
Type:         compound
Class:        event / festival
Definition:   Passover; the annual liberation festival. The historically
              recurring deliberate liberation event. `ka-pa-ki` (W160,
              liberation act = deliberate place-motion) + `'ti-re` (W103,
              recurring cycle). The juncture mark is required: `ka-pa-ki`
              is the pre-bound liberation-act unit; `ti-re` adds the annual
              recurrence. Written: `kapaki'tire`.
Composition:  ka-pa-ki (W160: liberation act, deliberate place-motion)
              + ' (juncture mark: left-bind ka-pa-ki as subcompound)
              + ti-re (W103: recurring temporal cycle)
              = [liberation-act] recurring annually = the Passover festival.
              Parse: `ka-pa-ki'ti-re` = [ka-pa-ki] modified by [ti-re]
              = the recurring liberation event = Passover.
              Without juncture, ka-pa-ki-ti-re (5 morphemes) would parse
              right-branching: ka modifies [pa-ki-ti-re], which loses the
              liberation-act base. Juncture is mandatory here.
Register:     theological / liturgical / cultural
Domain:       theology / Jewish tradition / liturgy
Status:       pending
First use:    S418 — ti-mi  ne  ka-pa-ki'ti-re (Now is the Passover)
Notes:        Passover encoded as the recurring liberation act: each year's
              festival is a re-enactment of ka-pa-ki (the Exodus liberation,
              W160). This grounds the Last Supper's Passover context: Jesus'
              last supper IS the Passover meal — ka-pa-ki'ti-re is both the
              events-of-the-night category and the founding liberation it
              commemorates.
              Connection to EXO-001: ka-pa-ki (W160) was the Exodus liberation
              act. ka-pa-ki'ti-re adds the liturgical recurrence dimension at
              Sinai.
Related:      ka-pa-ki (W160: liberation act — the base compound),
              ti-re (W103: recurring cycle — the festival dimension),
              ka (primitive: deliberate action), pa (primitive: place),
              ki (primitive: motion)
```

---

**W168**
```
Form:         ka-vo-si
Type:         compound
Class:        action
Definition:   thanksgiving; deliberate expression of value. Giving thanks;
              a blessing. The intentional act of signaling the worth/quality
              of something or someone — specifically as a performative speech
              act (a blessing said aloud, a prayer of thanks). Greek
              εὐχαριστία (eucharistia = well-graced thanksgiving) maps
              precisely: ka (deliberate) + vo (value/worth) + si (signal/
              expression) = deliberately expressing gratitude for worth.
Composition:  ka (deliberate action) + vo (value/quality) + si (signal/
              representation) = deliberate-value-signal = intentional
              expression of worth = thanksgiving/blessing.
              Three-root; right-branch: ka modifies [vo-si] = deliberate
              [value-signal] = deliberate expression of value.
Register:     general / liturgical / theological
Domain:       theology / liturgy / prayer / gratitude
Status:       pending
First use:    S426 — la-ze  ka-vo-si (he gave thanks / he blessed)
              Also S429 — la-ze  ka-vo-si (parallel thanksgiving over bread)
Notes:        ka-vo-si is used twice in the institution sequence: once over
              the cup (S426) and once over the bread (S429). The compound
              gives the Eucharist its name in Tonesu: the institution formula
              is a ka-vo-si event — a deliberate act of value-signaling over
              the elements before distributing them. The compound is not
              theology-specific: it covers any deliberate expression of
              gratitude or worth-acknowledgment.
Related:      ka (primitive: deliberate action), vo (primitive: value/quality),
              si (primitive: signal/representation),
              wi-si (W063: prayer = will-signal — a related but distinct form:
              prayer is a will-directed signal; thanksgiving is a value-signal)
```

---

- [ ] Review W002 (su-mu-li) — does it conflict with the derivational marker stack order?
- [ ] Develop domain-specific sub-lists once domains are finalized (see ontology/domains.md)
- [ ] Resolve W087/W156 collision: pa-ki appears twice with different glosses (adrift W087 vs liberation W156). Proposed resolution: unify under W087 as generic place-motion; deprecate W156; ka-pa-ki (W160) is the canonical deliberate-liberation form.
