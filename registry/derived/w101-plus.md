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

- [ ] Review W002 (su-mu-li) — does it conflict with the derivational marker stack order?
- [ ] Develop domain-specific sub-lists once domains are finalized (see ontology/domains.md)
