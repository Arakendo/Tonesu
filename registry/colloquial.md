# Colloquial Forms

Registered contractions and stub-forms used in the casual/spoken register. All entries must trace back to a canonical formal compound with a corpus attestation sentence. Formal compounds remain the canonical lexical entries; colloquial forms are spoken shortcuts, never the normative phonological form.

**Contraction rule (from spec/word-formation.md § Contraction and Compression):** A formal compound of 3+ morphemes may contract to a shorter spoken form when: (1) the formal compound is at least 3 morphemes long; (2) the short form is unambiguous within its discourse domain; (3) the formal compound remains the canonical registered entry.

**Compression mechanism for kind-term stubs:** When a kind-term base compound shares a productively distinguishable terminal root that uniquely identifies the class across all expected discourse contexts, the middle qualifier morphemes may be stripped. The terminal root is retained as the stub coda; the organism anchor `zo` is retained as the stub head. Pattern: `zo` + `{middle morphemes dropped}` + `{class root}` → `zo{class root}`.

**Ambiguity policy:** Colloquial stubs are CVC at maximum (the phonological ceiling is (C)V(C) — no clusters). The CVC namespace is large enough that inter-stub collisions are rare, but are not prevented by design. When two stubs collide, context disambiguates; the formal compound is always the unambiguous fallback. The registry does not police the CVC namespace — it documents what stubs exist and traces them to formal sources. A general-class stub coexists with species-level stubs in the same class; the formal compound is the species-precision fallback.

**Open design question — longer colloquial forms:** The CVC ceiling was defined for root-compression stubs (organism kind-terms, matter class stubs). It may not be the right ceiling for *prosodic shortening* of high-frequency juncture compounds — long `'`-bounded forms that have become pragmatically chunked through repeated use, where collapsing to a single CVC removes too much structural information. Whether a distinct rule for juncture-preserving colloquial shortening is warranted, and what its admission criteria would be, is an open question. See `notes/open-questions.md` (CLQ-EXT). Do not apply this registry's CVC ceiling to that case until the question is resolved.

**ID prefix:** colloquial entries use the `CLQ-` prefix (not `COL-`, which is reserved for the closed color-system question, COL-001 in notes/open-questions.md).

---

## CLQ-001 — Kind-term stubs: `zol` and `zof`

*First-attested: S269, S269.*

---

**CLQ-001a**
```
Form:         zol
Formal source: zo-se-so-li
Type:         contraction / colloquial stub
Class:        entity (organism kind)
Compression:  zo + [se-so dropped] + li → zol
Register:     colloquial / casual spoken
Domain:       general
Status:       active
First use:    S269
Notes:        Base-class stub, not a standalone species label. Plain zol = canid class as a whole; species reference requires a retained discriminator (li-ne'zol = dog, wi-pu'zol = wolf). Discriminator prefixes are NOT dropped in contraction.
Related:      CLQ-001b
```

---

**CLQ-001b**
```
Form:         zof
Formal source: zo-se-so-fe
Type:         contraction / colloquial stub
Class:        entity (organism kind)
Compression:  zo + [se-so dropped] + fe → zof
Register:     colloquial / casual spoken
Domain:       general
Status:       active
First use:    S269
Notes:        Symmetric pair with zol. Plain zof = felid/fox class as a whole; species reference requires a retained discriminator (li-ne'zof = house cat, pu-zo'zof = lion, ko-pa'zof = fox). Registered simultaneously with zol on analogical grounds; first direct corpus use originally pending.
Related:      CLQ-001a
```

---

## CLQ-002 — Kind-term stub: `zod`

*First-attested: S284.*

---

**CLQ-002a**
```
Form:         zod
Formal source: zo-se-so-di
Type:         contraction / colloquial stub
Class:        entity (organism kind)
Compression:  zo + [se-so dropped] + di → zod
Register:     colloquial / casual spoken
Domain:       general
Status:       active
First use:    S284
Notes:        Base-class stub, not a species label. Plain zod = bird class as a whole; species reference requires a retained discriminator (wi-di'zod = eagle, si-so'zod = parrot, ma-ki'zod = penguin).
```

---

## CLQ-003 — Kind-term stub: `zos`

*First-attested: S292.*

---

**CLQ-003a**
```
Form:         zos
Formal source: zo-su
Type:         contraction / colloquial stub
Class:        entity (organism kind)
Compression:  zo + su → zos (two-root base; solid written form = stub)
Register:     colloquial / casual spoken
Domain:       general
Status:       active
First use:    S292
Notes:        Two-root base; no middle acoustic-organism layer to drop. Different compression depth from zol/zof/zod (which drop se-so) but satisfies the same rule: unambiguous in discourse domain; formal compound canonical. Plain zos = plant class; discriminated forms retain prefix (be-di'zos = tree, lu-be'zos = flower, pa-be'zos = grass).
```

---

## CLQ-004 — Kind-term stub: `mas`

*First-attested: S299.*

---

**CLQ-004a**
```
Form:         mas
Formal source: ma-su
Type:         contraction / colloquial stub
Class:        entity (matter kind)
Compression:  ma + su → mas (matter anchor; same mechanism as zos)
Register:     colloquial / casual spoken
Domain:       general
Status:       active
First use:    S299
Notes:        First colloquial stub anchored on ma (matter) rather than zo (organism). Plain mas = rock/stone class as a whole; discriminated forms retain prefix (pu'mas = aggregate rock / gravel / sand casual form).
```

---

## CLQ-005 — Kind-term stubs: `zom` and `zop`

*First-attested: S313, S311.*

---

**CLQ-005a**
```
Form:         zom
Formal source: zo-se-ma
Type:         contraction / colloquial stub
Class:        entity (organism kind)
Compression:  zo + [se dropped] + ma → zom (one-root drop, not two)
Register:     colloquial / casual spoken
Domain:       general
Status:       active
First use:    S313
Notes:        Three-morpheme base (zo-se-ma); shallower than the four-morpheme acoustic-organism bases (zo-se-so-[x]), so only one middle root dropped rather than two. Plain zom = fish class; discriminated forms retain prefix (dipa'zom = salmon casual, wiki'zom = shark casual).
Related:      CLQ-005b
```

---

**CLQ-005b**
```
Form:         zop
Formal source: zo-se-so-pa
Type:         contraction / colloquial stub
Class:        entity (organism kind)
Compression:  zo + [se-so dropped] + pa → zop
Register:     colloquial / casual spoken
Domain:       general
Status:       active
First use:    S311
Notes:        Architectural counterpart to zom. Whales are zo-se-so-pa (acoustic organisms whose signal operates at place scale), not zo-se-ma (matter-perceptual aquatic organisms). The fish/whale split is the central design decision of KNM-006: acoustic primacy, not aquatic habitat, determines the branch.
Related:      CLQ-005a
```

---

## CLQ-006 — Kind-term stub: `zon`

*First-attested: S320.*

---

**CLQ-006a**
```
Form:         zon
Formal source: zo-se-ne
Type:         contraction / colloquial stub
Class:        entity (organism kind)
Compression:  zo + [se dropped] + ne → zon; terminal root ne: initial consonant n retained as coda
Register:     colloquial / casual spoken
Domain:       general
Status:       active
First use:    S320
Notes:        One-root drop (se dropped), same compression depth as zom. Terminal root ne contributes its initial consonant n as the stub coda. Plain zon = herd ungulate class; discriminated forms retain prefix (di'zon = horse casual, pu'zon = cattle casual, re'zon = deer casual).
```

---

## Registration log

| ID | Form | Formal source | First attested | Status |
|----|------|---------------|---------------|--------|
| CLQ-001a | `zol` | `zo-se-so-li` | S269 | active |
| CLQ-001b | `zof` | `zo-se-so-fe` | S269 | active |
| CLQ-002a | `zod` | `zo-se-so-di` | S284 | active |
| CLQ-003a | `zos` | `zo-su` | S292 | active |
| CLQ-004a | `mas` | `ma-su` | S299 | active |
| CLQ-005a | `zom` | `zo-se-ma` | S313 | active |
| CLQ-005b | `zop` | `zo-se-so-pa` | S311 | active |
| CLQ-006a | `zon` | `zo-se-ne` | S320 | active |

---

## KNM-008 namespace note — no CLQ entry for `zo-pe` (arthropod base)

*Documented: S327.*

`zo-pe` (arthropod / invertebrate) cannot produce a CVC stub without collision. `zo-pe` → `zop` is already registered as CLQ-005b.

**Resolution:** the arthropod base class uses the disyllabic casual form `zo-pe`. No CLQ entry registered.

zo-pe → zop collides with whale stub (CLQ-005b). Arthropod base uses disyllabic casual form zo-pe. Discriminated species-level forms (ne'zo-pe, su'zo-pe, so'zo-pe, zi'zo-pe, de'zo-pe) retain their discriminator prefixes and are unaffected.

---

## FNG-001 namespace note — no CLQ entry for `zo-ne` (fungal base)

*Documented: S334.*

`zo-ne` (fungal / mycelial) cannot produce a CVC stub without collision. `zo-ne` → `zon` is already registered as CLQ-006a.

**Resolution:** the fungal base class uses the disyllabic casual form `zo-ne`. No CLQ entry registered.

zo-ne → zon collides with herd-ungulate stub (CLQ-006a). Fungal base uses disyllabic casual form zo-ne. Structural cause: a depth-2 compound zo-{Y} and a depth-3 compound zo-se-{Y} share terminal root Y and therefore produce colliding stubs whenever they end on the same root. Both collisions (KNM-008 and FNG-001) arise from this depth-boundary compression rule.

---

*Generated from `registry/colloquial.yaml`.*