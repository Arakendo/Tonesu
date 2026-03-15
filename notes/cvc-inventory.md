# CVC / CVCC Descriptor Inventory: Digits, Colors, Scale Prefixes, Exceptional Anchors

## Status: Normative — March 2026

Working document. Forms here are candidates. None are formally registered until registry entries are created.

---

## Purpose

Four closed-class descriptor categories are assigned to two phonological strata. This follows the design rationale in `notes/numbers-colors-others.md`:

| Pattern | Stratum | Contents |
|---------|---------|----------|
| CV | primitives | closed ontological root set |
| CV-CV+ | compounds | open, compositional |
| CVC | lexical descriptors | digits, colors — closed class; scale prefixes — ergonomic shortforms, CVC phonology by pragmatic choice not admission criteria |
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

Core set covers the six typologically primary/neutral points. Secondary colors are documented as canonical compositional blends (`A zi B`) rather than CVC atoms; they satisfy the Assemblage-First Rule by composing cleanly from core hues.

### Core

| Color  | Form  | CV stem | Coda | Notes |
|--------|-------|---------|------|-------|
| black  | `yel` | `ye`    | l    | |
| white  | `yim` | `yi`    | m    | |
| red    | `ker` | `ke`    | r    | |
| green  | `gim` | `gi`    | m    | |
| blue   | `pom` | `po`    | m    | |
| yellow | `sam` | `sa`    | m    | |

### Extended (CVC atom retained)

| Color  | Form  | CV stem | Coda | Notes |
|--------|-------|---------|------|-------|
| brown  | `kus` | `ku`    | s    | no clean compositional form |

### Canonical secondary blends

These colors all compose cleanly from core hues via `zi` (mutual/coupling) and therefore do not satisfy criterion 1 of the Assemblage-First Rule. Canonical forms are listed here so usage is consistent across the corpus.

| Color  | Form          | Composition          |
|--------|---------------|----------------------|
| gray   | `yel zi yim`  | black + white        |
| pink   | `ker zi yim`  | red + white          |
| cyan   | `gim zi pom`  | green + blue         |
| lime   | `sam zi gim`  | yellow + green       |
| orange | `ker zi sam`  | red + yellow         |
| purple | `ker zi pom`  | red + blue           |

**Note on prior colloquial anchors:** `lu-ra` (≈red), `lu-zo` (≈green), `lu-pa` (≈blue) were logged as informal hue expressions (COL-001, open-questions.md). With this CVC set now normative, those compounds are poetic/informal register only; the CVC forms above are canonical.

---

## Visual-Pattern Compounds

*These are compositional compounds from existing primitives — not CVC atoms. They form a distinct vocabulary sub-class: named patterns of light distribution on surfaces. They function as pre-nominal modifiers by the same head-final rule as CVC color forms, and require `'` when scoping over multi-root kind-terms. Status: corpus-attested (KNM-003, March 2026) except where noted.*

### Core light-pattern modifiers

| Compound | Composition | Pattern type | Notes |
|----------|-------------|--------------|-------|
| `lu-di`  | `lu` (light) + `di` (direction) | stripe / linear | directional light = linear markings; first attested S255 (tiger, KNM-003) |
| `lu-pe`  | `lu` (light) + `pe` (part/component) | spot / dappled | partial light = distributed patches; first attested S256 (leopard), S257 (jaguar) |
| `lu-fe`  | `lu` (light) + `fe` (boundary/limit) | solid / uniform coat | bounded light = single enclosed color area; default when no pattern is present; not yet corpus-attested |

**Written forms:** `ludi`, `lupe`, `lufe`.

### `no-lu` vs `yel` — dark and black

Two expressions exist for darkness. They are related but non-identical:

| Form | Type | Reading | Use |
|------|------|---------|-----|
| `yel` | CVC atom | black (named hue point) | Color description, hue register: `yel mu` = a black object |
| `no-lu` | Compositional compound | dark / absence of light | Property modifier: coat or surface darkness; `no-lu'zo-se-so-fe` = dark-coated cat |

`yel` names the specific perceptual hue point at zero reflectance — it is a color the way `ker` (red) is a color. `no-lu` = `no` (negation/absence) + `lu` (light/visibility) = absence of light-reflection = darkness as a property. When describing coat color or surface appearance as a feature of a thing, `no-lu` is correct (as in S259, melanistic jaguar). When attributing the named hue black to an object, `yel` is correct. In casual speech they overlap; in formal register the distinction holds.

**Corpus basis:** `no-lu` first attested S259 (KNM-003, melanistic jaguar / "panther"). `yel` not yet corpus-attested; registered here as the canonical black hue atom.

### Scope rule

Same as hue CVC forms: light-pattern compounds pre-pose the noun and require `'` when modifying a multi-root compound:

```
lu-di mu                           →  striped object
lu-pe'zo-se-so-fe                  →  spotted cat-class organism
lu-fe'pa-fe'zo-se-so-fe            →  solid-coated mountain-territory cat
no-lu'lu-pe'ma-ki'zo-se-so-fe      →  dark-coated spotted water-terrain cat (melanistic jaguar)
```

The `'` rules from spec/word-formation.md § CVC Descriptor Modifiers and § Compound Grouping Marker apply without modification.

---

## Scale Prefix Inventory

SI-style magnitude scale words. Structure: `[scale] nu [domain]`. Base unit (×1) requires no prefix — bare `nu` with the domain is the base form.

**Classification note:** Scale prefixes are not closed-class CVC descriptor atoms (see FLAG-CVC-010). They are ergonomic shortforms for positional digit expressions — `pir` = `bol nil nil nil` (10³), `mes` = one-in-a-million scale, etc. Their compositional expressions exist; they were assigned CVC phonology for pragmatic measurement ergonomics, not because they fail the Assemblage-First Rule. They occupy CVC phonological space and block those CV stems, but their admission rationale is separate from digits and colors.

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

**Note:** Sub-pico (femto, atto, etc.) are unassigned. After the Assemblage-First audit (March 2026), the free CV stems in the CVC stratum are `wa`, `wo`, `va`, `ve`, `vi`, `te`, `do`, `ho`, `hu`, `ya` — see FLAG-CVC-006 and FLAG-CVC-008. (`va`/`ve`/`vi` became available when `v` was added to the consonant inventory; `te`/`do`/`ho`/`hu`/`ya` were freed by retiring/promoting five forms.)

---

## Astronomical Distance Anchors

**Assemblage-First audit (March 2026):** All three original CVC astronomical anchors have been reviewed against the Assemblage-First Rule. Two are conventionally/observationally defined with no compositional expression and belong in the CVCC tier. One has a valid compositional expression and receives no special form. CVC slots `ho`, `hu`, and `ya` are freed. See the CVCC section for `holf` and `yarm`.

| Unit | Approx SI | Previous CVC | Outcome | Rationale |
|------|-----------|-------------|---------|----------|
| AU | 1.496×10¹¹ m | `hon` → freed | **→ CVCC `holf`** | IAU-defined constant; no compositional expression; same ontological type as mole (`wels`) |
| light-year | 9.461×10¹⁵ m | `hun` → freed | **RETIRED** | Has compositional expression: `lu-ki ti-re nu pa` (light-motion one-time-cycle quantity of space) |
| parsec | 3.086×10¹⁶ m | `yam` (was megaparsec) → freed | **→ CVCC `yarm`** | Parallax-arcsecond unit; convention-defined; no compositional expression; megaparsec = `baf nu yarm` |

### Compositional form for light-year

```
lu-ki ti-re nu pa     → quantity of space equal to the distance light travels in one time-cycle
```

In stellar-astronomy discourse, the implied time-cycle is a year. When the cycle must be explicit: `lu-ki bol ti-re nu pa` (light-motion one-time-cycle quantity of space). This is the canonical Tonesu expression; no lexical shortform is warranted under the Assemblage-First Rule.

### Structural rules for astronomical expressions (post-audit)

Basic distance with CVCC anchor:

```
[digit] nu [anchor-CVCC]
```

```
bol hin nu holf               → 150 AU                 (inner edge of Oort cloud)
bun nu yarm                   → 2 parsecs              (stellar neighborhood)
baf nu yarm                   → 1 megaparsec           (galaxy-cluster scale)
gal bun nu lu-ki ti-re nu pa  → 3.2 light-years        (compositional form)
```

Scale-prefixed CVCC anchor:

```
[scale] nu [anchor-CVCC]
```

```
pir nu yarm               → 1 kiloparsec           (Milky Way structure)
wul nu yarm               → 1 gigaparsec           (cosmological survey depth)
```

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

**Practical anchor track (second admission class, March 2026):** Some CVCC forms are admitted not because composition fails, but because the referent is a stable, fixed entity with a high-enough frequency in technical registers to justify a short anchor alongside its compositional form. Admission criteria for this track differ from the standard three:

1. **A compositional expression exists and remains canonical** — the CVCC form is a shorthand, not a replacement.
2. **The referent has a stable, externally-assigned identity** (IUPAC atomic number, IAU designation, etc.) making the anchor semantically precise and bounded.
3. **Frequency in technical scientific discourse creates genuine communicative friction** — not stylistic inconvenience.
4. **A new CV primitive is explicitly refused** (same as standard criterion 3).

Chemical element anchors (Tier A) are the founding members of this track. The formal expression `[Z] ti fe-ma` remains canonical; the CVCC anchor names the same referent in fast speech.

### Phonological constraints for CVCC

**The tier signal is phonological, not semantic.** The CC coda tells a listener "stable atomic anchor" — it says nothing about whether a compositional path also exists. Do not reason backwards from "CVCC → must be inexpressible." Both admission tracks produce CVCC forms; the tier signal is identical for both.

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

#### Conventional SI anchors (non-derivable)

| Constant | Value | Form   | CV core | CC coda | Notes |
|----------|-------|--------|---------|---------|-------|
| ampere (A) | 1/(1.602×10⁻¹⁹) e/s | `telf` | `te` | `-lf` | SI base unit for current; defined by elementary charge count per second; no compositional expression beyond `vils`-count-rate |

#### Astronomical and physical anchors (observationally defined)

| Constant | Value | Form   | CV core | CC coda | Notes |
|----------|-------|--------|---------|---------|-------|
| AU (astronomical unit) | 1.496×10¹¹ m | `holf` | `ho` | `-lf` | IAU-defined Earth-Sun distance; observational anchor; formerly CVC `hon` (freed March 2026) |
| parsec | 3.086×10¹⁶ m | `yarm` | `ya` | `-rm` | Parallax-arcsecond unit; convention-defined; no compositional expression; formerly CVC `yam` (freed March 2026). Megaparsec = `baf nu yarm`. |
| year (Julian) | 31,557,600 s | `hulm` | `hu` | `-lm` | One Earth orbital period; temporal analog to `holf` (AU). `ti-re` = a cycle-of-time (compositional); `hulm` = this specific calibrated cycle. Anchors biology (generation times), astronomy (stellar ages), deep history. |

#### Atomic mass anchors

| Constant | Value | Form   | CV core | CC coda | Notes |
|----------|-------|--------|---------|---------|-------|
| electron mass m_e | 9.109×10⁻³¹ kg | `dolm` | `do` | `-lm` | CODATA-defined; no derivation from other constants; atomic physics workhorse |
| proton mass m_p | 1.672×10⁻²⁷ kg | `dolf` | `do` | `-lf` | CODATA-defined; distinct from m_e by factor ≈1836; nuclear physics anchor |

**Spoken sequence (mathematical):** varn · worn · werm · vins · valm · walf  
**Spoken sequence (physical):** vern · birm · velf · holm · vils · yolm · wels  
**Spoken sequence (conventional/observational):** telf · holf · yarm · hulm  
**Spoken sequence (atomic):** dolm · dolf  
**Spoken sequence (elements, batch 1 — universal):** polm · narm · sulm · girn · lorm  
**Spoken sequence (elements, batch 2 — metabolic):** fals · riln · bels · duns · lans  
**Spoken sequence (elements, batch 3 — industrial):** murn · tams · gons · rens · koms

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
| `holf` / `holm` | AU / Boltzmann | hol vs hol | -f vs -m | distinct coda-final ✓ |
| `holf` / `velf` | AU / G | hol vs vel | -f vs -f | distinct vowel + onset ✓ |
| `yarm` / `varn` | parsec / π | yar vs var | -m vs -n | distinct onset + coda ✓ |
| `yarm` / `yolm` | parsec / α | yar vs yol | -m vs -m | distinct vowel ✓ |
| `telf` / `velf` | ampere / G | tel vs vel | -lf vs -lf | distinct onset (t vs v) ✓ |
| `telf` / `holf` | ampere / AU | tel vs hol | -lf vs -lf | distinct onset + vowel ✓ |
| `hulm` / `holm` | year / k_B | hul vs hol | -m vs -m | distinct vowel ✓ |
| `hulm` / `yolm` | year / α | hul vs yol | -m vs -m | distinct onset + vowel ✓ |
| `hulm` / `valm` | year / √2 | hul vs val | -m vs -m | distinct onset + vowel ✓ |
| `dolm` / `dolf` | m_e / m_p | dol vs dol | -m vs -f | distinct coda-final ✓ |
| `dolm` / `hulm` | m_e / year | dol vs hul | -m vs -m | distinct onset + vowel ✓ |
| `dolm` / `holm` | m_e / k_B | dol vs hol | -m vs -m | distinct onset ✓ |
| `dolf` / `holf` | m_p / AU | dol vs hol | -f vs -f | distinct onset ✓ |
| `dolf` / `velf` | m_p / G | dol vs vel | -f vs -f | distinct onset + vowel ✓ |

All 34 CVCC forms are distinct from each other and from all 33 CVC forms. ✓

**Element-set near-neighbor notes (batch 1–3):**

| Pair | Elements | Verdict |
|------|----------|--------|
| `polm` / `pom` | H / blue (CVC) | CVCC vs CVC, different tier+length ✓ |
| `girn` / `gim` | N / green (CVC) | CVCC vs CVC, different tier+length ✓ |
| `riln` / `rim` | Si / milli (CVC) | CVCC vs CVC, different tier+length ✓ |
| `narm` / `yarm` | He / parsec | nar vs yar — distinct onset ✓ |
| `lorm` / `lans` | O / Ca | lor vs lan — distinct vowel+coda ✓ |
| `fals` / `bels` | Na / P | fal vs bel — distinct onset+vowel ✓ |
| `bels` / `wels` | P / mole | bel vs wel — distinct onset ✓ |
| `duns` / `gons` | Cl / Zn | dun vs gon — distinct onset+vowel ✓ |
| `tams` / `koms` | Cu / Pb | tam vs kom — distinct onset+vowel ✓ |
| `murn` / `varn` | Fe / π | mur vs var — distinct onset+vowel ✓ |

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
holf nu pa                   → one AU of distance
baf nu yarm                  → one megaparsec
pir nu yarm                  → one kiloparsec
bun hulm nu ti               → two years of time
telf nu ra-ti                → one ampere  (charge-force per time unit)
dolm nu ma                   → one electron mass
baf baf gal … dolm nu ma     → atomic mass unit (≈ 1836 × m_e, approximation)
```

### Deferred constants (assign when corpus pressure arrives)

| Constant | Description | Candidate form |
|----------|-------------|----------------|
| h (full Planck)    | 6.626×10⁻³⁴ J·s; ħ = h/2π | `birn` (bi+-rn) — but h = `birm worn` so may not qualify |
| γ (Euler-Mascheroni) | 0.5772…; limit constant | `garm` (ga+-rm) |
| Solar mass M☉ | 1.989×10³⁰ kg; IAU gravitational parameter | `telm` (te+-lm) — same class as `holf` |
| μ₀ (vacuum permeability) | now measured post-2019 SI redefinition | `dorn` (do+-rn) — Tier B; wait for corpus |
| ∞ (infinity)       | not a number; limit concept | `no-fe nu` (unbounded quantity) preferred; defer CVCC unless corpus insists |

#### Chemical element anchors (Tier A)

Chemical elements are compositionally identifiable in Tonesu through atomic-number structure: `[Z] ti fe-ma` gives the ordinal element reference — e.g., `wes ti fe-ma` = "the 6th element" = carbon. This compositional form remains canonical. Tier A CVCC forms are admitted as **practical high-frequency anchors for scientific discourse** — not on grounds that no expression exists, but because these elements appear constantly in chemistry, physics, and biology contexts and warrant short spoken forms alongside their compositional reference. The architecture mirrors the dual-register pattern used elsewhere in Tonesu: CVCC anchor for fast reference; compositional structure for formal meaning. CVCC forms consume zero CVC capacity. Forms assigned in three batches; see FLAG-CVC-011.

| Element    | Symbol | Z  | Form | CV core | CC coda | Notes |
|------------|--------|----|------|---------|---------|-------|
| hydrogen   | H  |  1 | `polm` | `po` | `-lm` | `po` shares stem with `pom` (CVC blue); tier distinguishes — same precedent as `birm`/`bim` |
| helium     | He |  2 | `narm` | `na` | `-rm` | |
| carbon     | C  |  6 | `sulm` | `su` | `-lm` | |
| nitrogen   | N  |  7 | `girn` | `gi` | `-rn` | `gi` shares stem with `gim` (CVC green); tier distinguishes |
| oxygen     | O  |  8 | `lorm` | `lo` | `-rm` | `lo-` is patient prefix but only bound; bare `lorm` unambiguous in measurement context |
| sodium     | Na | 11 | `fals` | `fa` | `-ls` | |
| silicon    | Si | 14 | `riln` | `ri` | `-ln` | `ri` shares stem with `rim` (CVC milli); tier distinguishes |
| phosphorus | P  | 15 | `bels` | `be` | `-ls` | |
| chlorine   | Cl | 17 | `duns` | `du` | `-ns` | `du` is result-frame particle, but CVCC tier disambiguates |
| calcium    | Ca | 20 | `lans` | `la` | `-ns` | `la` is agent particle, but CVCC tier disambiguates |
| iron       | Fe | 26 | `murn` | `mu` | `-rn` | |
| copper     | Cu | 29 | `tams` | `ta` | `-ms` | |
| zinc       | Zn | 30 | `gons` | `go` | `-ns` | `go` is causal particle; CVCC tier disambiguates |
| gold       | Au | 79 | `rens` | `re` | `-ns` | |
| lead       | Pb | 82 | `koms` | `ko` | `-ms` | `ko` is containment primitive; CVCC tier disambiguates |

---

## Cross-inventory Collision Check

### Uniqueness

All 66 proposed forms are distinct:

> nil bol bun gal mol hin wes yom fon zan  
> yel yim ker gim pom sam kus  
> zum mes rim pir baf wul bim les  
> gul fin fus hem  
> varn worn werm vins valm walf vern birm velf holm vils yolm wels  
> telf holf yarm hulm dolm dolf  
> polm narm sulm girn lorm  
> fals riln bels duns lans  
> murn tams gons rens koms

No two are identical. ✓

*Retired from CVC (March 2026 Assemblage-First audit): `tem` (orange → `ker zi sam`), `dol` (purple → `ker zi pom`), `hun` (light-year → `lu-ki ti-re nu pa`). Moved to CVCC: `hon` → `holf`, `yam` → `yarm`. Added to CVCC: `telf` (ampere), `hulm` (year), `dolm` (m_e), `dolf` (m_p).*

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
| ~~`hon` / `hun`~~ | AU / light-year | — | — | *both retired from CVC (March 2026 audit); `hon` → CVCC `holf`; `hun` → dropped* |
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
| After astronomical additions (original) | 5: `wa` `wo` `va` `ve` `vi` (va/ve/vi opened when v was added) |
| **After Assemblage-First audit (March 2026)** | **10: `wa` `wo` `va` `ve` `vi` `te` `do` `ho` `hu` `ya`** |

Broken down: 5 slots freed by audit — `te` (orange retired), `do` (purple retired), `hu` (light-year retired), `ho` (AU → CVCC), `ya` (megaparsec → CVCC parsec).

The CVC stratum is **constrained but meaningfully relieved** by the audit. Ten free CV stems remain, supporting ~50 additional strict-CVC forms before genuine depletion. Future CVC candidates should still be held to the same high bar. See FLAG-CVC-006.

---

## Flags and Open Questions

### FLAG-CVC-001 — `vo` vs. `v`-exclusion inconsistency ✓ RESOLVED

`spec/phonology.md` previously excluded `v` despite `vo` (R024, value/quality) already using it. **Resolution (March 2026): option A adopted — `v` added to the consonant inventory as the 17th consonant.** `spec/phonology.md §Consonant Inventory` updated; total count corrected from 16 to 17; exclusion note updated.

### FLAG-CVC-002 — Spec CVC shortlist fully consumed by digits ✓ RESOLVED

All 8 forms from `spec/phonology.md §CVC Root Reserve` shortlist were assigned to digits 1–8. **Resolution (March 2026):** `spec/phonology.md §Clean CVC shortlist` updated — now reads "All 8 forms assigned to digits 1–8 (March 2026); see `notes/cvc-inventory.md`." The placeholder text is removed.

### FLAG-CVC-003 — Large number expression

Digit chaining (`wes nil nil nu mu` = 600) is unambiguous but verbose for large numbers in ordinary speech. Options: (a) accept positional chaining only; (b) add explicit power-of-ten words (`ten`, `hundred`, `thousand` equivalents as additional CVC forms); (c) route large exact values through the scale prefix system (`pir nu mu` ≈ thousand objects). Defer until corpus shows a real pressure; log under NUM-001 in open-questions.md.

### FLAG-CVC-007 — Mole and ampere: conventional anchors ✓ RESOLVED

The **mole** (6.022×10²³) and the **ampere** (SI current unit, defined by elementary charge count per second) are SI base units whose values are fixed by measurement convention.

**Mole resolved:** `wels` (CVCC, March 2026).
**Ampere resolved:** `telf` (CVCC, March 2026). Assigned alongside the other Tier A observational additions (year `hulm`, electron mass `dolm`, proton mass `dolf`).

### FLAG-CVC-006 — CVC stratum near-depletion

After committing all forms in this document, **five free CVC-stem slots remain: `wa` `wo` `va` `ve` `vi`** (`va`/`ve`/`vi` became available when `v` was added to the consonant inventory in March 2026; `vo` was already taken as R024). Each stem supports ~5 safe codas, giving roughly **~25 additional strict-CVC forms** before the tier is genuinely exhausted. Practical implication: the CVC tier is **constrained but not closed**. It can absorb a small number of further exceptional assignments (conventional anchors, one-off scientific constants) before a decision about CVCC or another extension tier becomes necessary.

### FLAG-CVC-005 — Names and loanwords may collide with CVC layer

Proper names and borrowed vocabulary — personal names, place names, AI system names, titles — have no assigned phonological tier. If ad-hoc CVC forms are used for names, they will be indistinguishable from digit/color/scale descriptors at first glance. **Options:** (a) use the CVCC tier (now established) for names/loanwords; (b) rely on the `na` proper-name particle (G008) to signal context without a separate phonological tier. Option (b) is probably sufficient and lower-complexity; option (a) is available if names need a distinct phonological signature. Defer until a corpus sentence requires a proper name; track under `spec/naming.md`.

---

### FLAG-CVC-008 — Assemblage-First audit completed (March 2026)

Five CVC forms were reviewed and found to violate the Assemblage-First Rule:

| Form | Concept | Violation | Resolution |
|------|---------|-----------|------------|
| `tem` | orange | Compositional form exists: `ker zi sam` | RETIRED — use `ker zi sam` |
| `dol` | purple | Compositional form exists: `ker zi pom` | RETIRED — use `ker zi pom` |
| `hun` | light-year | Compositional form exists: `lu-ki ti-re nu pa` | RETIRED — use compositional form |
| `hon` | AU | No compositional form; same type as `wels` (mole) | MOVED to CVCC as `holf` |
| `yam` | megaparsec | Parsec has no compositional form; `mega` is already a scale prefix | MOVED to CVCC as `yarm` (parsec); megaparsec = `baf nu yarm` |

Net effect: 33 CVC forms (was 38), 15 CVCC forms (was 13), 10 free CVC stems (was 5). Full form lists updated in collision check and capacity table.

---

### FLAG-CVC-009 — Taxon-class anchors: a new CVCC admission class? (speculation, March 2026)

**Problem statement:** Common biological taxa — cat, dog, bird, fish, tree, grass — are high-frequency concepts in everyday and worldbuilding discourse. Current kind-term construction follows the compound rule: `zo` (living-thing) + discriminating modifiers → kind-term. This works, and the dog/cat distinction has been resolved (`zo-se-so-li` / `zo-se-so-fe`, KNM-002). But the kind-term forms are already 4 morphemes before any individual or variety modifier is added. "My cat Tony" is `[zo-se-so-fe na Tony]` — the kind-term alone is 8 phonemes solid-written `zosesof`.

The question is whether CVCC could serve as **taxon-class anchors**: stable atomic forms for genus/family-level biological (and possibly other natural-kind) categories, to which CV/CVC/CVCC modifiers are then applied.

**Why this is structurally different from current CVCC admissions:**

The existing CVCC criteria require that *no compositional expression exists* (irrational constants, convention-defined units). Biological taxa DO have compositional expressions — `zo-se-so-fe` composes cleanly from primitives and is semantically transparent. Strict criterion 1 is not satisfied. A taxon-CVCC admission class would require a **new, separate criterion**: not "inexpressible" but "high-frequency natural-kind class requiring a stable root for productive modification."

**Architectural options:**

1. **Strict Assemblage-First (status quo)** — no change. `zosesof` is the cat kind-term; `zosesof na Tony` is the cat named Tony. Compound kind-terms are the correct form. The 8-phoneme kind-term is not a problem — it is composable, transparent, and learnable. Accept the length.

2. **Taxon-CVCC anchor tier** — define a new admission sub-class within CVCC for biological (and potentially geological, meteorological, etc.) natural-kind roots. A CVCC form like `felm` = "feline class" anchors the category; `felm zo-fe` = "territorial feline" = cat; `felm zo-li` = "social feline." The CVCC form is the head; modifiers discriminate. Requires defining where on the taxonomic tree the CVCC anchors live — genus? family? order? — and capping the set.

3. **Domain-register shortforms** — no new tier. Register high-frequency kind-terms as domain-accepted compound shortforms within a biology domain (`da-zo`). The formal compound stays canonical; a contracted colloquial form is the practical solution. This is how `tonesu` contracts from `to-ne-su`. The cat kind-term formally is `zosesof`; colloquially it contracts. No new phonological tier needed.

4. **Hybrid: CVCC at class level, compounds at genus level** — CVCC for the broadest natural-kind categories (mammal-class, bird-class, fish-class, insect-class, plant-class, fungus-class), then discriminating compounds from there. The class-level CVCC is coarser than genus — more like the biological *class* or *order* node. Individual `na`-naming handles the rest.

**The Tony problem as a test case:**

| Approach | "My cat Tony" |
|----------|---------------|
| Status quo | `zosesof na Tony` (kind + identifier) |
| Option 2 (genus CVCC) | `felm na Tony` (cat-class anchor + identifier) |
| Option 3 (contraction) | `zosesof` → colloquial `zof` + `na Tony` |
| Option 4 (class CVCC) | `maml zo-fe na Tony` (mammal-class + territorial-living + identifier) |

Option 3 may be the most consistent with the dual-register design already in the spec: formal compounds contract in colloquial register. This requires no new phonological tier, no new admission criteria, and leverages existing infrastructure.

**Questions before committing to any option:**

- Is the 8-phoneme kind-term actually a problem in practice, or does it feel unwieldy only in analytical notation?
- If CVCC taxon anchors are admitted, where does the taxonomy cut? (genus? family? class? order?) Cutting at a wrong level means either too many anchors or anchors that are too broad to be useful.
- Does option 3 (colloquial contraction) already solve this inside the dual-register design without any spec change?
- What's the right comparison: English "cat" (3 chars) vs Tonesu `zosesof` (8 chars written) vs colloquial `zof` (3 chars)? The contraction path already gets there.
- Are there non-biological natural-kind categories (rock types, cloud types, terrain features, chemical element classes) with the same pressure? If yes, a general taxon-CVCC tier is more motivated. If no, the biology domain may be the only pressure point.

**Status:** Speculation only. Do not design until COL-001 (color system) is resolved and at least one corpus sentence creates concrete pressure for a shorter kind-term. Log under open-questions.md.

---

### FLAG-CVC-010 — Scale prefixes reclassified as free CVC ergonomic shortforms (March 2026)

Scale prefixes (`pir` kilo, `baf` mega, `wul` giga, etc.) were previously listed alongside digits and colors as closed-class CVC descriptor atoms. This is incorrect under the Assemblage-First Rule: every scale prefix has a valid compositional expression (positional digit chaining — `pir nu pa` = `bol nil nil nil nu pa` = 1 kilometer). They satisfy no admission criterion that digits and colors satisfy.

**Resolution:** Scale prefixes are reclassified as **free CVC ergonomic shortforms** — registered measurement vocabulary that happens to have CVC phonology. Their CVC shape is a pragmatic choice (short, phonologically distinct from compounds, easy to chain before `nu`) not a principled closed-class assignment. They still occupy CVC phonological space and those CV stems remain blocked; capacity accounting is unchanged. But their admission rationale is now distinct from the closed-class digit/color tier.

**Practical effect:** No forms change. The Purpose table and Scale Prefix section header are updated to reflect this. Future scale-prefix candidates (femto, atto, etc.) are admitted as ergonomic shortforms, not by closed-class criteria.

**Spec reference:** The ergonomic shortform sub-class is formally defined in `spec/word-formation.md §Ergonomic Shortforms`, with admission criteria and the distinction from closed-class CVC atoms and CVCC exceptional anchors. The phonological tier table in `spec/phonology.md §Phonological Tier Stratification` is updated to reflect the two CVC sub-categories.

### FLAG-CVC-011 — Chemical element CVCC anchors (Tier A, scaffolded March 2026)

Tier A chemical elements are compositionally identifiable via `[Z] ti fe-ma` (e.g., `wes ti fe-ma` = carbon, Z=6). CVCC forms are admitted on the **practical anchor track** (see second admission class note in the Assemblage-First Rule section) — not on grounds of inexpressibility, but as high-frequency short forms for scientific discourse alongside the canonical compositional reference. Cost to CVC stratum: zero.

**Planned batches:**
- Batch 1: H, He, C, N, O — universal chemistry anchors
- Batch 2: Na, Si, P, Cl, Ca — metabolic/biochemical set
- Batch 3: Fe, Cu, Zn, Au, Pb — industrial/materials set

For each batch: assign forms, run near-neighbor check against all existing CVCC, update spoken sequences and collision check table.

**Status:** Complete — all 15 Tier A element forms assigned (March 2026). Batches 1–3 committed. Near-neighbor check passed; all 34 CVCC forms distinct from each other and all 33 CVC forms. See spoken sequences and near-neighbor notes in the CVCC Assigned Forms section.

---

### FLAG-CVC-012 — Common molecule CVCC anchors (watch item)

High-frequency molecules are candidates for the practical anchor track (same rationale as Tier A elements): IUPAC-defined identity, compositional form exists via element anchors, extreme domain frequency.

| Molecule | Compositional form | Domain | Notes |
|----------|--------------------|--------|-------|
| H₂O (water) | `su-ma bun polm bol lorm` | universal | most frequent molecule in any biology/chemistry context |
| CO₂ (carbon dioxide) | `su-ma bol sulm bun lorm` | atmosphere, biology | photosynthesis, respiration, climate |
| O₂ (oxygen gas) | `su-ma bun lorm` | biology, chemistry | respiration anchor |
| N₂ (nitrogen gas) | `su-ma bun girn` | atmosphere, chemistry | 78% of atmosphere |
| NH₃ (ammonia) | `su-ma bol girn gal polm` | biochemistry, industry | nitrogen cycle |
| CH₄ (methane) | `su-ma bol sulm mol polm` | energy, atmosphere | greenhouse gas |

Compositional forms are verbose but unambiguous. The question is whether discourse frequency justifies anchors — H₂O almost certainly does; the others depend on corpus direction (biology-heavy vs. physics-heavy).

**Do not assign forms until at least one corpus sentence creates concrete pressure.** The element anchor track (FLAG-CVC-011) is the prerequisite: molecule anchors reference element forms and those forms must be stable first (✓ complete as of March 2026).

**Status:** Watch item. No forms assigned.

---

### FLAG-CVC-004 — `nu-to` dual assignment

`nu-to` appears in `registry/primitives.md` stress-test table as both "axis of measurement / dimension" and "probability / confidence level." These are two contextually determined readings of the same compound. **This is intentional and unproblematic** — English does the same thing with *weight* (physical / importance / statistical). Measurement context vs. epistemic context disambiguates reliably. No new primitive, no respelling needed. Document the disambiguation principle in the `nu-to` entry comment for future readers, and cross-reference from NUM-001.
