# CVC / CVCC Descriptor Inventory: Digits, Colors, Scale Prefixes, Exceptional Anchors

## Status: Proposed — March 2026

Working document. Forms here are candidates. None are formally registered until registry entries are created.

---

## Purpose

Four closed-class descriptor categories are assigned to two phonological strata. This follows the design rationale in `notes/numbers-colors-others.md`:

| Pattern | Stratum | Contents |
|---------|---------|----------|
| CV | primitives | closed ontological root set |
| CV-CV+ | compounds | open, compositional |
| CVC | lexical descriptors | digits, colors, scale prefixes, observational anchors |
| CVCC | exceptional anchors | mathematical/physical constants that are irrational, transcendental, or defined by convention with no compositional expression |

CVC and CVCC forms are phonologically stratified from primitives and compounds, giving instant category recognition. The coda cluster in CVCC is itself the tier signal — no CV stem restriction applies.

---

## Design Constraints

All forms must satisfy:

1. **CV stem must be free** — first two characters must not form any taken primitive, particle, pronoun, or derivational marker. The audit table is in `spec/phonology.md §CV Space Audit`. Note: that audit counts 33 roots; `zi` (R034) was added afterward and its CV stem is now taken.
2. **Coda from the safe set** — preferred: `n l r m s`. Marked but allowed: `z f h`. Stops (`k p t b d g`) are legal per syllable rules but ranked lower for cross-linguistic ease and spec preference.
3. **No consonant clusters** — CVC only. Forms like `blu`, `grn`, `blk` are English abbreviations that violate the no-CC-cluster rule and are not valid Tonesu syllables.
4. **Cross-set distinctiveness** — no two forms across all three inventories should be near-homophones (differ by only one phoneme with the same CV stem).

---

## Structural Rules

These govern how CVC descriptors integrate with existing grammar. No new primitives are required.

### Counting

```
[digit] nu [noun]
```

```
bol nu mu         → one object
bun nu zo         → two organisms
bun gal nu li     → twenty-three agents   (positional chain, most-significant first)
```

### Ordinals

```
[digit] ti        → [nth] in sequence
```

```
bol ti            → first
bun ti            → second
gal ti            → third
```

### Large number chaining

Digits chain positionally before `nu`, most significant first:

```
wes nil nil nu mu  → six hundred objects
```

*No explicit hundred/thousand words yet — positional chaining handles it. See FLAG-CVC-003.*

### Base units as compounds

Base SI units do not need CVC forms. The domain primitive **is** the unit label — `nu [domain]` means "a quantity of [domain]", which is exactly what a base unit expresses. No new vocabulary is required.

| Tonesu compound | Reading | SI equivalent |
|-----------------|---------|---------------|
| `nu pa`  | quantity of space    | meter (distance) |
| `nu ti`  | quantity of time     | second (duration) |
| `nu ma`  | quantity of matter   | kilogram (mass) |
| `nu ha`  | quantity of heat     | kelvin (temperature) |
| `nu lu`  | quantity of light    | candela (luminous intensity) |
| `nu ra`  | quantity of force    | newton / joule family |
| `nu so`  | quantity of sound    | decibel register |
| `nu si`  | quantity of signal   | bit / information unit |

The full measurement expression stacks cleanly:

```
[digit] [scale] nu [domain]
```

```
bol nu pa              → 1 meter
pir nu pa              → 1 kilometer
bun gal nu ti          → 23 seconds
gal nu ma              → 3 kilograms      (gal pir nu ma for 3 kg precisely)
mes nu pa              → 1 micrometer
```

**Derived units** (those defined as combinations of base units — newton, joule, pascal, watt) are expressed as multi-domain compounds. They do not receive separate names unless corpus pressure demands a shortform. Examples:

```
ra ne ma-ki            → force in relation to matter-in-motion    (≈ newton)
ra ne pa               → force in relation to space               (≈ joule)
```

**The only units that require CVC forms** are observational/conventional anchors — distances or quantities defined by physical measurement rather than derived from conceptual primitives (AU, light-year, mole, ampere-equivalent). Those use the CVC anchor forms in the Astronomical Distance Anchors section below.

---

### Scale-prefixed measurement

```
[scale] nu [domain]
```

```
pir nu ma         → kilo-scale quantity of matter      (≈ kilogram)
mes nu ti         → micro-scale time                   (≈ microsecond)
baf nu ra         → mega-scale energy                  (≈ megajoule)
bim nu si         → pico-scale signal quantity         (≈ picofarad register)
```

Base unit takes no scale prefix — bare `nu` is the base form:

```
bun nu ra         → two units of force (base scale)
```

### Color as modifier

Head-final rule applies; color word precedes the noun it modifies:

```
[color] [noun]
```

```
ker mu            → red object
gim zo            → green organism
pom su            → blue structure
```

Color intensity via existing `vo-be` / `vo-de`:

```
ker vo-be         → bright red
pom vo-de         → dark blue
```

Color blending via `zi` (mutual/coupling):

```
ker zi pom        → red interacting with blue    (purple register)
gim zi sam        → green-yellow blend           (lime register)
```

Color gradient via `ki` (motion/change):

```
ker ki pom        → transitioning red-to-blue    (spectral gradient)
```

### Atomic and molecular compounds

Subatomic and chemical-structure concepts compose from existing primitives — no CVC forms needed.

| Concept    | Compound    | Reading |
|------------|-------------|-------------------------------------------------------------------|
| particle   | `pe-ma`     | component of matter |
| atom       | `ru-pe-ma`  | singular / irreducible component of matter |
| molecule   | `su-ma`     | structured matter |
| element    | `fe-ma`     | bounded / categorically distinct matter |
| ion        | `ma-ra`     | matter in an energy / force state |
| compound   | `su-fe-ma`  | structured, categorically distinct matter |

These use the standard compound slot before `nu` where counting is needed: `bun nu ru-pe-ma` = two atoms.

**Conventional anchor exception:** The mole (6.022×10²³ particles) is a defined-by-convention counting unit, not derivable from primitives. It requires a CVC anchor form — see FLAG-CVC-007.

### Probability with digits

From the probability stress test (notes/open-questions.md):

```
wes nu-to         → 60% confidence
zan zan nu-to     → 99% confidence
```

---

## Digit Inventory

All 8 forms from `spec/phonology.md §CVC Root Reserve shortlist` are used here for digits 1–8. The spec shortlist note ("No form assigned yet, March 2026") should be updated when these are committed.

| Digit | Form  | CV stem | Coda | Notes |
|-------|-------|---------|------|-------|
| 0     | `nil` | `ni`    | l    | minor echo of Latin *nil* = nothing; acceptable |
| 1     | `bol` | `bo`    | l    | spec shortlist |
| 2     | `bun` | `bu`    | n    | spec shortlist |
| 3     | `gal` | `ga`    | l    | spec shortlist |
| 4     | `mol` | `mo`    | l    | spec shortlist — fast-speech blur risk with `bol` (1); fallback `mor` reserved if confusion emerges in practice |
| 5     | `hin` | `hi`    | n    | spec shortlist |
| 6     | `wes` | `we`    | s    | spec shortlist |
| 7     | `yom` | `yo`    | m    | spec shortlist |
| 8     | `fon` | `fo`    | n    | spec shortlist |
| 9     | `zan` | `za`    | n    | free CV, not in shortlist |

**Spoken sequence:** nil · bol · bun · gal · mol · hin · wes · yom · fon · zan

---

## Color Inventory

Core set covers the six typologically primary/neutral points. Extended set covers secondary colors; all three can be deferred since they compose from core colors via `zi`.

### Core

| Color  | Form  | CV stem | Coda | Notes |
|--------|-------|---------|------|-------|
| black  | `yel` | `ye`    | l    | |
| white  | `yim` | `yi`    | m    | |
| red    | `ker` | `ke`    | r    | |
| green  | `gim` | `gi`    | m    | |
| blue   | `pom` | `po`    | m    | |
| yellow | `sam` | `sa`    | m    | |

### Extended (can be deferred)

| Color  | Form  | CV stem | Coda | Notes |
|--------|-------|---------|------|-------|
| orange | `tem` | `te`    | m    | compositional alt: `ker zi sam` |
| purple | `dol` | `do`    | l    | compositional alt: `ker zi pom` |
| brown  | `kus` | `ku`    | s    | |

**Note on prior colloquial anchors:** `lu-ra` (≈red), `lu-zo` (≈green), `lu-pa` (≈blue) were logged as informal hue expressions (COL-001, open-questions.md). If this CVC set is adopted, those compounds become poetic/informal register only; the CVC forms above are canonical.

---

## Scale Prefix Inventory

SI-style magnitude scale words. Structure: `[scale] nu [domain]`. Base unit (×1) requires no prefix — bare `nu` with the domain is the base form.

### Core (nano through giga)

| Scale | Exponent | Form  | CV stem | Coda | Notes |
|-------|----------|-------|---------|------|-------|
| nano  | 10⁻⁹     | `zum` | `zu`    | m    | |
| micro | 10⁻⁶     | `mes` | `me`    | s    | |
| milli | 10⁻³     | `rim` | `ri`    | m    | |
| base  | 10⁰      | *(bare `nu`)* | — | — | no prefix |
| kilo  | 10³      | `pir` | `pi`    | r    | |
| mega  | 10⁶      | `baf` | `ba`    | f    | |
| giga  | 10⁹      | `wul` | `wu`    | l    | |

### Extended (optional)

| Scale | Exponent | Form  | CV stem | Coda | Notes |
|-------|----------|-------|---------|------|-------|
| pico  | 10⁻¹²    | `bim` | `bi`    | m    | |
| tera  | 10¹²     | `les` | `le`    | s    | |

### Extended-Extended (astronomical and precision physics)

| Scale  | Exponent | Form  | CV stem | Coda | Notes |
|--------|----------|-------|---------|------|---------|
| peta   | 10¹⁵     | `gul` | `gu`    | l    | light-year territory in SI |
| exa    | 10¹⁸     | `fin` | `fi`    | n    | |
| zetta  | 10²¹     | `fus` | `fu`    | s    | |
| yotta  | 10²⁴     | `hem` | `he`    | m    | observable-universe radius in SI |

**Note:** Sub-pico (femto, atto, etc.) are unassigned. After all current assignments, the free CV stems remaining in the CVC stratum are `wa`, `wo`, `va`, `ve`, `vi` — see FLAG-CVC-006. (`va`/`ve`/`vi` became available when `v` was added to the consonant inventory in March 2026; `vo` was already taken as R024.)

---

## Astronomical Distance Anchors

Named reference distances for astronomical-scale discourse. These are **distance unit anchors**, not scale prefixes — they behave like domain words (`ma`, `ti`, `pa`, `ra`) but carry a pre-calibrated scale. They slot into the standard measurement structure:

```
[digit/scale] nu [anchor]
```

| Unit       | Approx SI     | Form  | CV stem | Coda | Notes |
|------------|---------------|-------|---------|------|---------|
| AU         | 1.5 × 10¹¹ m  | `hon` | `ho`    | n    | solar-system scale; Earth-Sun distance |
| light-year | 9.46 × 10¹⁵ m | `hun` | `hu`    | n    | stellar scale; compositional gloss: `lu-ki-re pa` (light-motion-cycle space) |
| megaparsec | 3.09 × 10²² m | `yam` | `ya`    | m    | cosmological scale; large-structure astronomy |

**Phonetic note:** `hon` and `hun` share the h_n pattern and differ only in vowel (o vs u). In practice they refer to scales five orders of magnitude apart, so context eliminates ambiguity completely. Careful speech makes the vowel distinction clear.

### Structural rules for astronomical expressions

Basic distance:

```
[digit] nu [anchor]
```

```
gal bun nu hun        → 3.2 light-years
bol hin nu hon        → 150 AU            (inner edge of Oort cloud)
bun nu yam            → 2 megaparsecs
```

Scale-prefixed anchor (for very large or very small astronomical distances):

```
[scale] nu [anchor]
```

```
wul nu hun            → giga-light-years  (≈ cosmological survey depth)
```

Digit + scale combined:

```
[digit] [scale] nu [anchor]
```

```
bun wul nu hun        → 2 × 10⁹ light-years    (2 giga-light-years)
```

Mixed: SI precision for physical quantities alongside anchored distances:

```
pir nu ma la ki ne bol hun    → kilo-mass [agent] moves toward one light-year [distance]
```

### Compositional background

`hun` (light-year) has a natural compositional gloss: `lu-ki-re nu pa` (light-motion-cycle quantity of space = distance light travels in one time-cycle). The CVC form is the concise registry name; the compound is the semantically transparent long form. Both are valid; CVC is preferred in measurement expressions.

AU (`hon`) has no clean compositional equivalent — it is the Earth-Sun distance, which is observational rather than derived from primitives. It is therefore a pure named anchor with no compound alternative.

`yam` (megaparsec) is similarly definitional (parsec = parallax second, a measurement-geometry concept). Named anchor only.

---

## CVCC Exceptional Anchor Inventory

### The Assemblage-First Rule

**Default resolution for any concept, however complex, is always compositional assemblage.** A long compound is not a problem. An ungodly concatenation is not a problem. Stress landing on an unexpected primitive in a deep chain is not a problem. None of these are grounds for minting a new lexical atom.

**CVCC is the pressure valve, not the shortcut.** It exists precisely so that when assemblage genuinely fails — not because it is inconvenient, but because the referent has no compositional expression at all — there is a clean place for a phonological atom that does not pollute the primitive set.

**Admission criteria — all three must be satisfied:**

1. **No compositional expression exists.** The concept cannot be expressed by any combination of existing primitives, no matter how verbose. Irrational constants, transcendental numbers, and measurement-convention anchors fail compositional expression by definition.
2. **A single stable atom is functionally necessary.** The form appears frequently enough in technical discourse that spelling it out each time creates genuine communicative friction — not stylistic inconvenience, genuine friction.
3. **A new CV primitive is explicitly refused.** If the pressure is strong enough that someone might argue for a new primitive, CVCC is the answer instead. CV primitives are ontological commitments; CVCC forms are convenience tokens with no ontological weight.

**What does NOT qualify:**
- A compound that is merely long
- A concept that is merely common
- A domain term that speakers will use frequently (use a registered compound or domain-register shortform instead)
- Anything expressible with existing roots in any form

These are the rarest entries in the lexicon. The CVCC tier is not for general vocabulary.

### Phonological constraints for CVCC

1. **No CV stem restriction** — the coda cluster is the tier signal. A speaker hearing a CC coda knows it is not a primitive, compound, or CVC descriptor.
2. **CC coda from the preferred set** — sonorant+sonorant or sonorant+fricative clusters are most cross-linguistically pronounceable: `-lm`, `-ls`, `-ln`, `-rm`, `-rs`, `-rn`, `-lf`, `-rf`, `-ns`, `-ms`.
3. **Cross-tier distinctiveness** — must not be a near-homophone of any existing CVC form (one-phoneme difference in the first three phonemes).
4. **Pool size** — ~400–600 usable forms (17 consonants × 5 vowels × ~10 CC pairs, filtering awkward clusters). Effectively inexhaustible for this purpose.

### Assigned forms

#### Mathematical constants

| Constant | Value | Form   | CV core | CC coda | Notes |
|----------|-------|--------|---------|---------|-------|
| π (pi)          | 3.14159…       | `varn` | `va` | `-rn` | transcendental; circle circumference/diameter ratio |
| τ (tau)         | 6.28318…       | `worn` | `wo` | `-rn` | 2π; full-turn circle constant |
| e (Euler)       | 2.71828…       | `werm` | `we` | `-rm` | natural logarithm base; transcendental |
| φ (golden ratio)| 1.61803…       | `vins` | `vi` | `-ns` | (1+√5)/2; self-similar proportion |
| √2              | 1.41421…       | `valm` | `va` | `-lm` | Pythagorean constant; diagonal of unit square |
| i (imaginary)   | √(−1)          | `walf` | `wa` | `-lf` | complex unit; 90° rotation in complex plane |

#### Physical constants

| Constant | Value | Form   | CV core | CC coda | Notes |
|----------|-------|--------|---------|---------|-------|
| c (speed of light)    | 299,792,458 m/s      | `vern` | `ve` | `-rn` | exact by SI definition since 2019 |
| ħ (reduced Planck)    | 1.055×10⁻³⁴ J·s   | `birm` | `bi` | `-rm` | h/2π; quantum of action; preferred form over full h |
| G (gravitational)     | 6.674×10⁻¹¹ N·m²/kg² | `velf` | `ve` | `-lf` | Newton/Einstein gravitational constant |
| k₂ (Boltzmann)        | 1.381×10⁻²³ J/K     | `holm` | `ho` | `-lm` | thermal energy per kelvin |
| e (elementary charge) | 1.602×10⁻¹⁹ C      | `vils` | `vi` | `-ls` | proton/electron charge magnitude |
| α (fine structure)    | ≈1/137.036          | `yolm` | `yo` | `-lm` | dimensionless; electromagnetic coupling strength |
| mole (N₂)            | 6.022×10²³        | `wels` | `we` | `-ls` | Avogadro's number as counting unit; conventional SI anchor |

**Spoken sequence (mathematical):** varn · worn · werm · vins · valm · walf  
**Spoken sequence (physical):** vern · birm · velf · holm · vils · yolm · wels

### Near-neighbor check (CVCC set)

| Pair | Constants | First 3 phonemes | Coda | Verdict |
|------|-----------|-----------------|------|---------|
| `varn` / `vern` | π / c | var vs ver | both -n (part of cluster) | distinct vowel ✓ |
| `varn` / `valm` | π / √2 | var vs val | -rn vs -lm | distinct coda ✓ |
| `vern` / `velf` | c / G | ver vs vel | -rn vs -lf | distinct coda ✓ |
| `vins` / `vils` | φ / charge e | vin vs vil | -ns vs -ls | distinct coda-initial ✓ |
| `werm` / `wels` | e / mole | wer vs wel | -rm vs -ls | distinct coda ✓ |
| `worn` / `walf` | τ / i | wor vs wal | -rn vs -lf | distinct vowel + coda ✓ |
| `holm` / `yolm` | k₂ / α | hol vs yol | both -m | distinct onset (h vs y) ✓ |
| `valm` / `velf` | √2 / G | val vs vel | both -lm/-lf | different vowel + coda ✓ |
| `birm` / `bim`  | ħ / pico (CVC) | bir vs bi\_ | CVCC vs CVC | different length + tier ✓ |
| `vern` / `vern` | — | — | — | unique ✓ |

All 13 CVCC forms are distinct from each other and from all 38 CVC forms. ✓

### Usage examples

```
varn nu pa-re           → π quantities of spatial-cycle     (circumference)
bun varn nu pa-re       → 2π = τ (but use worn directly)
worn nu pa              → τ radians                         (full circle)
werm be                 → e growing                         (natural exponential growth)
holm nu ha              → Boltzmann-quantity of heat         (thermal energy)
bun wels nu ru-pe-ma    → 2 moles of atoms
vern nu pa-ti           → speed-of-light quantity of distance/time
valm nu pa              → √2 unit of space                   (diagonal of unit square)
```

Approximate form (when digits suffice; exact form when precision required):

```
gal bol mol … nu pa-re      → 3.14… (approximation, verbose)
varn nu pa-re                → π exactly (canonical)
```

### Deferred constants (assign when corpus pressure arrives)

| Constant | Description | Candidate form |
|----------|-------------|----------------|
| h (full Planck)    | 6.626×10⁻³⁴ J·s; ħ = h/2π | `birn` (bi+-rn) if distinction needed |
| ampere             | conventional SI current unit | see FLAG-CVC-007 |
| γ (Euler-Mascheroni) | 0.5772…; limit constant | `galf` or `garm` |
| ∞ (infinity)       | not a number; limit concept | may express as `no-fe nu` (unbounded quantity) rather than CVCC |

---

## Cross-inventory Collision Check

### Uniqueness

All 51 proposed forms are distinct:

> nil bol bun gal mol hin wes yom fon zan  
> yel yim ker gim pom sam tem dol kus  
> zum mes rim pir baf wul bim les  
> gul fin fus hem  
> hon hun yam  
> varn worn werm vins valm walf vern birm velf holm vils yolm wels

No two are identical. ✓

### Near-neighbor analysis (differ by one phoneme within same CV stem)

| Pair | Categories | CV stem | Codas | Verdict |
|------|-----------|---------|-------|---------|
| `bol` / `mol` | digit 1 / digit 4 | bo vs mo | both l | distinct onset ✓ |
| `bun` / `hin` | digit 2 / digit 5 | bu vs hi | both n | distinct onset + vowel ✓ |
| `gal` / `gim` | digit 3 / green | ga vs gi | l vs m | distinct vowel + coda ✓ |
| `mol` / `mes` | digit 4 / micro | mo vs me | l vs s | distinct vowel + coda ✓ |
| `nil` / `rim` | digit 0 / milli | ni vs ri | l vs m | distinct onset + coda ✓ |
| `bun` / `wul` | digit 2 / giga | bu vs wu | n vs l | distinct onset + coda ✓ |
| `bim` / `rim` | pico / milli | bi vs ri | both m | distinct onset + vowel ✓ |
| `mes` / `les` | micro / tera | me vs le | both s | distinct onset + vowel ✓ |
| `yel` / `yim` | black / white | ye vs yi | l vs m | distinct vowel + coda ✓ |
| `hon` / `hun` | AU / light-year | ho vs hu | both n | distinct vowel ✓ — 5 orders of magnitude apart; context always disambiguates |
| `gul` / `wul` | peta / giga | gu vs wu | both l | distinct onset + vowel ✓ |
| `fin` / `hin` | exa / digit 5 | fi vs hi | both n | distinct onset ✓ |
| `fus` / `fon` | zetta / digit 8 | fu vs fo | both f onset | distinct vowel + coda ✓ |
| `hem` / `hin` | yotta / digit 5 | he vs hi | m vs n | distinct vowel + coda ✓ |

No dangerous near-homophones across categories. ✓

### CVC stratum capacity

After all assignments in this document, the free CV-stem count is:

| Stage | Free stems remaining |
|-------|---------------------|
| Before CVC work (minus `zi`) | 36 |
| After digits + colors + scales | 9: `gu fi fu he ho hu ya wa wo` |
| After astronomical additions | **5: `wa` `wo` `va` `ve` `vi`** (va/ve/vi opened when v was added to inventory) |

The CVC stratum is **effectively full**. Any future CVC assignments must be treated as exceptional and require displacing something or accepting a longer phonological form. See FLAG-CVC-006.

---

## Flags and Open Questions

### FLAG-CVC-001 — `vo` vs. `v`-exclusion inconsistency ✓ RESOLVED

`spec/phonology.md` previously excluded `v` despite `vo` (R024, value/quality) already using it. **Resolution (March 2026): option A adopted — `v` added to the consonant inventory as the 17th consonant.** `spec/phonology.md §Consonant Inventory` updated; total count corrected from 16 to 17; exclusion note updated.

### FLAG-CVC-002 — Spec CVC shortlist fully consumed by digits

All 8 forms from `spec/phonology.md §CVC Root Reserve` shortlist are assigned to digits 1–8. The spec comment ("No form on this list is assigned yet, March 2026") must be updated once these assignments are committed.

### FLAG-CVC-003 — Large number expression

Digit chaining (`wes nil nil nu mu` = 600) is unambiguous but verbose for large numbers in ordinary speech. Options: (a) accept positional chaining only; (b) add explicit power-of-ten words (`ten`, `hundred`, `thousand` equivalents as additional CVC forms); (c) route large exact values through the scale prefix system (`pir nu mu` ≈ thousand objects). Defer until corpus shows a real pressure; log under NUM-001 in open-questions.md.

### FLAG-CVC-007 — Mole and ampere: conventional anchors ✓ PARTIAL

The **mole** (6.022×10²³ — Avogadro's number of particles) and the **ampere** (defined by elementary charge flow) are SI base units whose values are fixed by measurement convention, not derivable from primitives.

**Mole resolved:** assigned `wels` in the CVCC tier (March 2026). CVCC was preferred over spending a CVC slot — the coda cluster distinguishes it as an exceptional anchor, and the CVCC pool is large enough to absorb all future constants of this type without depleting the CVC reserve.

**Ampere deferred:** no corpus pressure yet. When needed, assign from CVCC tier. Track alongside NUM-001 in `notes/open-questions.md`.

### FLAG-CVC-006 — CVC stratum near-depletion

After committing all forms in this document, **five free CVC-stem slots remain: `wa` `wo` `va` `ve` `vi`** (`va`/`ve`/`vi` became available when `v` was added to the consonant inventory in March 2026; `vo` was already taken as R024). Each stem supports ~5 safe codas, giving roughly **~25 additional strict-CVC forms** before the tier is genuinely exhausted. Practical implication: the CVC tier is **constrained but not closed**. It can absorb a small number of further exceptional assignments (conventional anchors, one-off scientific constants) before a decision about CVCC or another extension tier becomes necessary.

### FLAG-CVC-005 — Names and loanwords may collide with CVC layer

Proper names and borrowed vocabulary — personal names, place names, AI system names, titles — have no assigned phonological tier. If ad-hoc CVC forms are used for names, they will be indistinguishable from digit/color/scale descriptors at first glance. **Options:** (a) use the CVCC tier (now established) for names/loanwords; (b) rely on the `na` proper-name particle (G008) to signal context without a separate phonological tier. Option (b) is probably sufficient and lower-complexity; option (a) is available if names need a distinct phonological signature. Defer until a corpus sentence requires a proper name; track under `spec/naming.md`.

---

### FLAG-CVC-004 — `nu-to` dual assignment

`nu-to` appears in `registry/primitives.md` stress-test table as both "axis of measurement / dimension" and "probability / confidence level." These are two contextually determined readings of the same compound. **This is intentional and unproblematic** — English does the same thing with *weight* (physical / importance / statistical). Measurement context vs. epistemic context disambiguates reliably. No new primitive, no respelling needed. Document the disambiguation principle in the `nu-to` entry comment for future readers, and cross-reference from NUM-001.
