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
| R032 | `ha` | heat / thermal state | force | general |
| R033 | `fa` | affective substrate | mind | general |
| R034 | `zi` | mutual / coupling event | relation | general |

---

## Grammatical Particles

| ID | Particle | Role | Notes |
|----|----------|------|-------|
| G001 | `la` | perspective anchor | precedes the perspective-privileged participant (agent in action clauses, stance-holder in epistemic clauses, relational anchor in stative predicates) |
| G002 | `lo` | patient marker | precedes the affected NP |
| G003 | `ro` | instrument/cause marker | precedes tool or reason; `ro` has no root assignment — renamed from `ra` to eliminate particle/root collision |
| G004 | `pa` | location marker | precedes place NP |
| G005 | `ne` | recipient / relation | precedes beneficiary or target |
| G006 | `ta` | time reference | precedes temporal expression |
| G007 | `ka` | action marker | precedes verb root |
| G008 | `na` | proper name marker | precedes identifiers |
| G009 | `da` | domain marker | precedes domain label |
| G010 | `ven` | approximation marker (spoken) | spoken realization of `~`; canonical written form is `~`; `ven` is used in speech and phonetic transcription only; pre-positional hedge: "approximately / roughly / something like" |
| G011 | `helm` | topic/definition marker (spoken) | spoken realization of `:` (topic frame / explanatory definition mark); canonical written form is `:`; CVCC; `helm` is used in speech and phonetic transcription only |
| G012 | `helms` | canonical definition marker (spoken) | spoken realization of `::` (structural/canonical definition mark); canonical written form is `::`; CVCCS — produced by the notation-doubling rule (`helm` + `s`); forms the minimal pair `helm` / `helms` with G011. See spec/phonology.md § Phonological Tier Stratification for the CVCCS admission rule. |
| G013 | `vel` | parallel partition marker (spoken) | spoken realization of `/` (parallel partition mark); canonical written form is `/`; CVC; marks the structural midpoint of a formally paired bi-clausal construction. `vel` is a valid written substitute for `/` wherever the symbol is unavailable or a word-form is preferred. |
| G014 | `vund` | evidential frame opener (spoken) | spoken realization of `(` (evidential frame open); canonical written form is `(`; CVCC; forms the minimal pair `vund` / `vunds` with G015. Belongs to the `v`-initial notation family (`ven` ~ · `vel` / · `vund` `(`). The `u` vowel = deep/closed/containing (sound symbolism), fitting for a frame that encloses reported content. `vund` is a valid written substitute for `(` wherever the bracket symbol is unavailable. |
| G015 | `vunds` | evidential frame closer (spoken) | spoken realization of `)` (evidential frame close); canonical written form is `)`; CVCCS — produced by the bracket-pair convention (`vund` + `s`; the `+s` coda marks the secondary/closing element, per the CVCCS admission rule). Forms the minimal pair `vund` / `vunds` with G014. `vunds` is a valid written substitute for `)` wherever the bracket symbol is unavailable. |
| G016 | `sild` | quotation / mention frame opener (spoken) | spoken realization of `"` (open double-quote; quotation/mention frame open); canonical written form is `"`; CVCC; `si` root = signal/communication — the frame that marks literal signal reproduction. Forms the minimal pair `sild` / `silds` with G017. `sild` is a valid written substitute for `"` wherever the symbol is unavailable. Admitted March 2026; probationary status pending 20 corpus attestations. |
| G017 | `silds` | quotation / mention frame closer (spoken) | spoken realization of `"` (close double-quote; quotation/mention frame close); canonical written form is `"`; CVCCS — produced by the bracket-pair convention (`sild` + `s`; the `+s` coda marks the secondary/closing element, per the CVCCS admission rule). Forms the minimal pair `sild` / `silds` with G016. `silds` is a valid written substitute for `"` wherever the symbol is unavailable. |
| G018 | `feld` | morpheme boundary marker (spoken) | spoken realization of `-` (hyphen/morpheme boundary mark); canonical written form is `-`; CVCC; `fe` root = boundary/limit — the mark that renders a root boundary visible. Normative in metalinguistic, pedagogical, and math/science contexts; ordinary compound writing remains solid. `feld` is a valid written substitute for `-` wherever the ASCII hyphen is unavailable or a word-form is preferred. Spec: `spec/phonology.md §- — Morpheme Boundary Mark`. |
| G019 | `suld` | structural slot / scope bracket opener (spoken) | spoken realization of `{` (open brace; structural slot/scope bracket open); canonical written form is `{`; CVCC; `su` root = structure — the bracket that marks structural scope. Forms the minimal pair `suld` / `sulds` with G020. `suld` is a valid written substitute for `{` wherever the symbol is unavailable or a word-form is preferred. Spec: `spec/phonology.md §{} — Structural Slot / Scope Bracket`. |
| G020 | `sulds` | structural slot / scope bracket closer (spoken) | spoken realization of `}` (close brace; structural slot/scope bracket close); canonical written form is `}`; CVCCS — produced by the bracket-pair convention (`suld` + `s`; the `+s` coda marks the secondary/closing element, per the CVCCS admission rule). Forms the minimal pair `suld` / `sulds` with G019. `sulds` is a valid written substitute for `}` wherever the symbol is unavailable or a word-form is preferred. |
| G021 | `peld` | prosodic juncture marker (spoken) | spoken realization of `'` (apostrophe; prosodic juncture marker); canonical written form is `'`; CVCC; from `pe` (primitive root). Used in dictation, formal document reading, and pedagogical contexts to explicitly signal the subcompound boundary. `peld` is a valid written substitute for `'` wherever the apostrophe symbol is unavailable or a word-form is preferred. Spec: `spec/phonology.md §Prosodic Juncture Marker`. |
| G022 | `zeld` | aside / commentary frame opener (spoken) | spoken realization of `[` (open bracket; aside/commentary frame open); canonical written form is `[`; CVCC; neutral initial. Forms the minimal pair `zeld` / `zelds` with G023. Used in dictation and pedagogical contexts where bracket positions must be explicitly signaled. `zeld` is a valid written substitute for `[` wherever the symbol is unavailable or a word-form is preferred. Spec: `spec/phonology.md §[] — Aside / Commentary Frame`. |
| G023 | `zelds` | aside / commentary frame closer (spoken) | spoken realization of `]` (close bracket; aside/commentary frame close); canonical written form is `]`; CVCCS — produced by the bracket-pair convention (`zeld` + `s`; the `+s` coda marks the secondary/closing element, per the CVCCS admission rule). Forms the minimal pair `zeld` / `zelds` with G022. `zelds` is a valid written substitute for `]` wherever the symbol is unavailable or a word-form is preferred. |
| G024 | `wald` | clause separator (spoken) | spoken realization of `,` (comma; clause separator); canonical written form is `,`; CVCC; from `wa` (free CV; `w` = flowing): the pause mark. Used in dictation and formal document reading. `wald` is a valid written substitute for `,` wherever the symbol is unavailable or a word-form is preferred. Spec: `spec/phonology.md §, — Clause Separator`. |
| G025 | `bold` | exclamation mark (spoken) | spoken realization of `!` (exclamation mark); canonical written form is `!`; CVCC; from `bo` (free CV; `b` = impact/force): the force mark. Used in dictation and formal document reading. `bold` is a valid written substitute for `!` wherever the symbol is unavailable or a word-form is preferred. Spec: `spec/phonology.md §! — Exclamation Mark`. |
| G026 | `geld` | question mark (spoken) | spoken realization of `?` (question mark); canonical written form is `?`; CVCC; from `ge` (property/attribute): the mark that seeks a property. Used in dictation and formal document reading. `geld` is a valid written substitute for `?` wherever the symbol is unavailable or a word-form is preferred. Spec: `spec/phonology.md §? — Question Mark`. |
| G027 | `teld` | sequential connector (spoken) | spoken realization of `;` (sequential connector); canonical written form is `;`; CVCC; from `te` (free CV; `t` = sequence/segmentation, sound symbolism): the mark that signals directed A-then-B sequence. Disambiguates from `go` (causal mechanism particle) in dictation: `A teld B` = A, and then B (no mechanism asserted); `A go B` = A caused B. `teld` is a valid written substitute for `;` wherever the symbol is unavailable or a word-form is preferred. Spec: `spec/phonology.md §`;` — Sequential Connector`. |
| G028 | `el` | prosodic suspension (spoken/written-substitute) | spoken realization and written-substitute form of `—` (em-dash; prosodic-suspension mark); canonical written form is `—` (U+2014); **VC tier** — first VC-tier form admitted; `e` = shifting/emergent (V-class sound symbolism); `l` = liquid coda, trailing. Word-initial only (parse invariant 1). Cannot appear mid-compound or combined with role-markers. **Author choice:** `—` and `el` are equally normative; use `el` in verse, in phonetic contexts, or wherever the em-dash glyph is unavailable or a word-form is stylistically preferred. Admitted EMD-002 (March 2026). Spec: `spec/phonology.md §— — Prosodic Suspension`. |
| G029 | `he` | vocative / direct-address particle | standalone direct-address speech act; precedes the name or NP being called (`he na-Moses!`). `h` = breath/aspiration onset — the natural onset of calling; `e` = mid-front, salient. Structurally: `he na-X` is an illocutionary act (a call); `na-X` alone is an NP (not a speech act). Cannot combine with role-markers (`la-he` inadmissible). Interpersonal — directed *at a person*; does not assert speaker affect. Non-interchangeable with `ya` (G030). Admitted CVP-001 (March 2026). |
| G030 | `ya` | attention-signal / content-directing particle | pre-propositional attention marker; directs the interlocutor's attention toward an upcoming claim, event, or revelation (`ya, go-no-fe helms vo`). `y` = smooth/yielding onset, directed at content rather than person; `a` = maximally open vowel, draws attention outward. Asserts nothing about speaker affect; distinguishes from `fa-be!` (affective claim). Propositional — directed *at content*; does not address a named person. Non-interchangeable with `he` (G029). Admitted CVP-001 (March 2026). |

*Note: `la` (perspective anchor particle) is phonetically distinct from `li` (person/agent root) — resolved. `ro` (instrument particle) has no root assignment — resolved by rename from `ra`. Remaining particles that overlap with roots (`pa`, `ka`, `ne`) are lower priority and still under review.*

---

## Derivational Markers

| ID | Marker | Role | Attaches to | Example |
|----|--------|------|-------------|---------|
| D001 | `-li` | agent (one who does) | action, process root | build-li → builder |
| D002 | `-mu` | device / instrument | action, process root | build-mu → building tool |
| D003 | `-pa` | location | action, state root | build-pa → construction site |
| D004 | `-su` | result / state | action root | build-su → structure |
| D005 | `-to` | abstract concept | any root | build-to → concept of construction |
| D006 | `-ge` | quality / property | entity or state root | `ra-ge` → energetic |
| D007 | `-ki` | ongoing process (verbal noun) | action root | build-ki → the building (activity) |

---

## V-Prefix Class

Admitted March 2026 (VPC-001). Five scope-modifier prefixes; word-initial position only. A V-prefix adjusts the register or scope of the following root without adding independent lexical content. Right-branching default: `a-to-li` = `a-[to-li]`. Written solid in prose: `ato`, `ito`, `oki`, `eki`, `usu`.

| Form | Scope effect | Key attested compounds | Corpus basis |
|------|-------------|----------------------|--------------|
| `a-` | abstract/universal — root at broadest conceptual category | `a-to` (knowing-in-general), `a-su` (form-as-such), `a-to-li` (sage) | VPC-001 (S504, S505, S510, S511) |
| `i-` | particular/precise — root as discrete specified instance | `i-to` (this specific fact) | VPC-001 (S506) |
| `u-` | interior/foundational — tacit or underlying mode of root | `u-to` (interior/tacit knowing), `u-su` (deep structure) | VPC-001 (S507, S513) |
| `o-` | collective/distributed — root as property of group-as-unit | `o-li` (community-as-unit ≠ `pu-li`) | VPC-001 (S508) |
| `e-` | emergent/transitional — root in unsettled, forming state | `e-ki` (emergent/progressive change) | VPC-001 (S509) |

**Known problem — `a-` merge hazard:** `la-a-X` collapses to `la-X` in fast speech. Use `a-` in predicate/patient positions only, not after `la-`.

**Known problem — over-generation:** 5 × 34+ potential minimal forms. V-prefixed compounds are **not registered by default** — they are live scope-modifiers readable from context. Registry admission requires: (a) meaning not paraphraseable by an existing compound without loss, AND (b) ≥ 3 corpus attestations in distinct contexts.

---

## Open Questions

- [x] ~~Resolve particle/root phonetic collision for agent marker~~ → resolved: agent particle renamed `li` → `la`. Remaining overlaps: `ra`, `pa`, `ka`, `ne`.
- [ ] Add tense/aspect suffix IDs as formal markers
- [x] ~~Replace `plu` with a CV or CVC form to comply with syllable rules~~ → replaced with `pu`. Complete.
- [ ] Assign final phonetic forms — current roots are placeholder assignments
