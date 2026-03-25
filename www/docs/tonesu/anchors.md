# Exceptional Anchors

Some values cannot be built from Tonesu's primitive roots no matter how many you stack. Others are fixed by international convention with no derivational path. For exactly these cases, Tonesu provides two non-compositional lexical tiers: **CVC** (closed-class descriptors) and **CVCC** (exceptional anchors).

This page covers the CVCC tier and explains when and why named roots at any tier are admitted.

---

## The Assemblage-First Rule

**The default resolution for any concept is always compositional assemblage.** A long compound is not a problem. Only when assemblage genuinely fails is a named root warranted.

Three criteria must **all** be met before any CVCC form is admitted:

1. **No compositional expression exists** — the concept cannot be expressed by any combination of existing primitives in any form
2. **A single stable atom is functionally necessary** — it appears frequently enough in technical discourse that spelling it out creates genuine communicative friction, not just stylistic inconvenience
3. **A new CV primitive is explicitly refused** — CVCC is the answer instead of an ontological commitment

**What does NOT qualify:**

- A compound that is merely long
- A concept that is merely common
- Anything expressible with existing roots in any form

### Practical anchor track (second admission class)

Some CVCC forms are admitted where a compositional expression *does* exist but the referent is a stable, externally assigned identity (an IUPAC number, an IAU-defined constant) appearing so frequently in technical registers that a shorthand alongside the compositional form is justified. The compositional expression always remains canonical.

---

## Tier Structure

| Tier | Shape | Admission | Examples |
|------|-------|-----------|---------|
| Primitive | CV | Closed ontological set (~34 roots) | `to`, `ra`, `pa` |
| Compound | CV-CV+ | Compositional, open | `toli`, `zomu` |
| CVC descriptor | CVC | Closed-class: digits, colors, scales | `bol` (1), `ker` (red), `pir` (kilo) |
| Exceptional anchor | CVCC | No compositional expression, or convention-fixed external identity | `varn` (π), `vern` (c), `holf` (AU) |

**The CC coda is the tier signal.** A spoken CVCC form tells the listener immediately: *fixed value, not assembled.* This is phonological information, not semantic — CVCC does not imply the value is inexpressible, only that it is structurally atomic.

---

## Mathematical Constants

| Constant | Form | Written | Value | Notes |
|----------|------|---------|-------|-------|
| π (pi) | `varn` | varn | 3.14159… | Transcendental; circle circumference/diameter ratio |
| τ (tau) | `worn` | worn | 6.28318… | 2π; full-turn circle constant |
| e (Euler) | `werm` | werm | 2.71828… | Natural logarithm base; transcendental |
| φ (golden ratio) | `vins` | vins | 1.61803… | (1+√5)/2; self-similar proportion |
| √2 | `valm` | valm | 1.41421… | Pythagorean constant; diagonal of unit square |
| i (imaginary unit) | `walf` | walf | √(−1) | 90° rotation in the complex plane |

**Usage:**

```
varn nu pa                → π meters (quantity of space: pi units)
bun varn nu pa            → 2π meters (τ-scale distance)
werm fu                   → e^x (exponential base)
```

---

## Physical Constants

| Constant | Form | Written | Approx | Notes |
|----------|------|---------|--------|-------|
| c (speed of light) | `vern` | vern | 2.998×10⁸ m/s | Exact by SI definition since 2019 |
| ħ (reduced Planck) | `birm` | birm | 1.055×10⁻³⁴ J·s | h/2π; quantum of action |
| G (gravitational) | `velf` | velf | 6.674×10⁻¹¹ N·m²/kg² | Newton/Einstein gravitational constant |
| k_B (Boltzmann) | `holm` | holm | 1.381×10⁻²³ J/K | Thermal energy per kelvin |
| e (elementary charge) | `vils` | vils | 1.602×10⁻¹⁹ C | Proton/electron charge magnitude |
| α (fine structure) | `yolm` | yolm | ≈ 1/137 | Dimensionless; electromagnetic coupling |

**Usage:**

```
vern nu pa nu ti          → distance light travels in 1 second (c × 1s)
holm nu ha                → Boltzmann energy at 1 kelvin
```

---

## Convention-Defined Units

Units defined by international convention rather than derived from first principles:

| Unit | Form | Written | Value | Rationale |
|------|------|---------|-------|-----------|
| Mole (N_A) | `wels` | wels | 6.022×10²³ | Avogadro counting unit; defined by convention |
| Ampere | `telf` | telf | 1/(1.602×10⁻¹⁹) e/s | SI base unit for current; no compositional expression beyond `vils`-count-rate |

**Usage:**

```
bun nu wels               → 2 moles
bol nu telf               → 1 ampere
```

---

## Astronomical Anchors

Distances and periods defined by physical observation or IAU convention:

| Unit | Form | Written | Value | Notes |
|------|------|---------|-------|-------|
| AU (astronomical unit) | `holf` | holf | 1.496×10¹¹ m | IAU-defined Earth–Sun mean distance |
| Parsec | `yarm` | yarm | 3.086×10¹⁶ m | Parallax-arcsecond unit; convention-defined |
| Julian year | `hulm` | hulm | 31,557,600 s | One Earth orbital period; temporal scale anchor |

**Usage:**

```
bol hin nu holf           → 150 AU  (inner Oort cloud edge)
bun nu yarm               → 2 parsecs  (stellar neighborhood)
pir nu yarm               → 1 kiloparsec  (galactic structure)
wul nu yarm               → 1 gigaparsec  (cosmological survey depth)
gal bun nu hulm           → 3.2 years
```

Scale prefixes stack with CVCC anchors normally:

```
{scale} nu {anchor}

mes nu hulm               → 1 microsecond-equivalent (very small time ratio)
pir nu holf               → 1000 AU (distant Oort cloud)
```

### Light-year: the compositional exception

The light-year has a clean compositional expression and therefore receives **no** CVCC form:

```
lu-ki ti-re nu pa         → distance light travels in one time-cycle
                             (one year in stellar-astronomy context)

gal bun nu lu-ki ti-re nu pa
                          → 3.2 light-years
```

---

## Atomic Mass Anchors

Fundamental mass values defined by CODATA measurement:

| Constant | Form | Written | Value | Notes |
|----------|------|---------|-------|-------|
| Electron mass (m_e) | `dolm` | dolm | 9.109×10⁻³¹ kg | Atomic physics workhorse |
| Proton mass (m_p) | `dolf` | dolf | 1.672×10⁻²⁷ kg | Factor ~1836 heavier than electron |

```
dolm nu ma                → electron mass in mass units
dolf nu ma                → proton mass in mass units
```

---

## Phonological Constraints

CVCC forms are designed to be immediately distinct from all other tiers:

- **No CV stem restriction** — the CC coda already signals tier
- **Preferred CC codas:** `-lm`, `-ls`, `-ln`, `-rm`, `-rs`, `-rn`, `-lf`, `-rf`, `-ns`, `-ms` (sonorant-heavy clusters for cross-linguistic ease)
- **No near-homophones** across the set — every pair differs by at least vowel, coda, or onset

**Spoken sequence overview:**

| Group | Forms |
|-------|-------|
| Mathematical | varn · worn · werm · vins · valm · walf |
| Physical | vern · birm · velf · holm · vils · yolm |
| Conventional / observational | wels · telf · holf · yarm · hulm |
| Atomic mass | dolm · dolf |

---

## Design Rationale

CVCC exceptional anchors embody three commitments:

1. **The primitive set stays ontologically pure.** CV roots encode concepts with real compositional weight. Admitting π or c as a CV primitive would claim that these values are foundational to Tonesu's conceptual ontology — which they are not. They are facts about physical reality, not components of meaning.

2. **Composition is always tried first.** The CVCC tier exists precisely so that when composition genuinely fails, there is a structurally clean answer that does not bend the rules of any other tier. It is a pressure valve, not a shortcut.

3. **The phonological tier signal is public information.** A CVCC form tells a listener *nothing* about whether a compositional form exists — only that this token is atomic. Two admission tracks (irrational/transcendental vs. practical anchor) produce the same phonological shape. The tier signal is structural, not semantic.

---

*See [Named roots](named-roots.md) for the full CVC inventory (digits, colors, scale prefixes). See the [Assemblage-First Rule](named-roots.md#the-assemblage-first-rule) in Special Forms for the general word-formation context.*
