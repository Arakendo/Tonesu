# Named Roots: Digits, Colors, Scales, and Constants

Named roots are **closed-class lexical anchors** that sit outside the primitive set. They are not compositional — they are assigned fixed meanings by convention or necessity. They are stratified phonologically to distinguish them from primitives and compounds.

---

## Why Named Roots Exist

Tonesu uses three phonological tiers for roots:

| Tier | Pattern | Content | Scope |
|------|---------|---------|-------|
| **Primitive** | CV | Ontological roots; the core concept set | Closed (~34 forms) |
| **Compositional** | CV-CV+ | Combinations of primitives; productive | Open (infinite) |
| **Named Roots** | CVC / CVCC | Descriptors, constants; ergonomic anchors | Closed (dozens) |

**Named roots exist because:**
- Some values are defined by physical convention (AU, the mole), not by ontology
- Some values are irrational or transcendental (π, e, φ) — no compositional expression
- Some categories are closed and frequent enough to warrant shortforms (colors, digits, scales)

They are not failures of composition. They are solutions to practical and mathematical necessity that preserve the integrity of the primitive set.

---

## The Assemblage-First Rule

Before any concept gets a named root, it must **fail compositional expression** in all possible forms. Three criteria must all be met:

1. **No compositional expression exists** — the concept cannot be built from existing primitives no matter how verbose
2. **A single atom is functionally necessary** — it appears frequently enough that spelling it out each time creates genuine communicative friction
3. **A new primitive is explicitly refused** — if the pressure is strong, CVCC is the answer instead

**What does NOT qualify:**
- A long compound (length is not grounds for a shortform)
- A common concept (frequency alone is not grounds)
- Domain vocabulary (use registered compounds or domain shortforms instead)
- Anything expressible from existing roots in any form

---

## Phonological Stratification

Named roots occupy two distinct phonological tiers to make category instantly recognizable:

### CVC Tier (Closed Consonant)

Three consonants with a single vowel. Used for:
- **Digits** (0–9)
- **Colors** (core hues and brown)
- **Scale prefixes** (nano through yotta)

**Coda constraints:** Preferred codas are `n`, `l`, `r`, `m`, `s`. Marked but allowed: `z`, `f`, `h`. Stops and clusters are disallowed.

### CVCC Tier (Closed Consonant Cluster)

Two consonants flanking a vowel, then one final consonant. Used for:
- **Mathematical constants** (π, e, φ)
- **Physical constants** (speed of light, Planck's constant)
- **Convention-defined units** (the mole, AU, parsec)

The CVCC tier signals: *"This value is fixed by external definition, not internal composition."*

---

## Digits: The CVC Digit Inventory

**Counting structure:** `{digit} nu {noun}`

```
bol nu mu           → one object
bun nu zo           → two organisms
gal bun nu li       → thirty-two agents
```

**Ordinals:** `{digit} ti` = nth in sequence

```
bol ti              → first
bun ti              → second
gal ti              → third
```

### Forms (0–9)

| Digit | Form | Meaning | Sound |
|-------|------|---------|-------|
| 0 | `nil` | zero / nothing | *nil* |
| 1 | `bol` | one | *bohl* |
| 2 | `bun` | two | *bun* |
| 3 | `gal` | three | *gahl* |
| 4 | `mol` | four | *mohl* |
| 5 | `hin` | five | *hin* |
| 6 | `wes` | six | *wes* |
| 7 | `yom` | seven | *yohm* |
| 8 | `fon` | eight | *fohn* |
| 9 | `zan` | nine | *zahn* |

### Positional Counting

Most-significant-digit first, chaining before `nu`:

```
wes nil nil nu mu       → 600 objects (6 × 10²)
bun gal hin nu li       → 235 agents (chained: 2·3·5)
```

---

## Colors: The CVC Color Inventory

**Structure:** `{color} {noun}` — head-final, color precedes the noun.

```
ker mu                  → red object
gim zo                  → green organism
pom su                  → blue structure
```

### Core Colors

| Color | Form | Sound | Notes |
|-------|------|-------|-------|
| black | `yel` | *yel* | zero reflectance hue |
| white | `yim` | *yim* | full reflectance hue |
| red | `ker` | *kehr* | |
| green | `gim` | *gim* | |
| blue | `pom` | *pohm* | |
| yellow | `sam` | *sahm* | |
| brown | `kus` | *kus* | no clean compositional form |

### Secondary Colors: Compositional Blends

Secondary colors are built from core hues using `zi` (mutual/coupling):

```
yel zi yim            → gray (black + white)
ker zi yim            → pink (red + white)
gim zi pom            → cyan (green + blue)
sam zi gim            → lime (yellow + green)
ker zi sam            → orange (red + yellow)
ker zi pom            → purple (red + blue)
```

### Color Intensity

Use existing primitives `vo-be` (brightening, growth in value) and `vo-de` (darkening, decay in value):

```
ker vo-be             → bright red
pom vo-de             → dark blue
```

### Color Gradients

Use `ki` (motion/change) for spectral transitions:

```
ker ki pom            → transitioning from red to blue
```

### Darkness vs. Black

Two distinct expressions:
- **`yel`** = black as a hue (named color point)
- **`no-lu`** = dark as a property (absence of light)

Use `yel` for color attribution; use `no-lu` for surface/coat darkness:

```
yel mu                → a black object (hue)
no-lu'zo-se          → dark-coated animal (property of coat)
```

---

## Scale Prefixes: SI-Style Magnitude Words

**Structure:** `{scale} nu {domain}`

Base unit (×1) needs no prefix — bare `nu` with the domain is the base form.

```
bol nu pa             → 1 meter (base)
pir nu ma             → 1 kilogram (kilo-scale matter)
mes nu ti             → 1 microsecond (micro-scale time)
baf nu ra             → 1 megajoule (mega-scale energy)
```

### Core Scales (nano through giga)

| Scale | Exponent | Form | Sound |
|-------|----------|------|-------|
| nano | 10⁻⁹ | `zum` | *zuhm* |
| micro | 10⁻⁶ | `mes` | *mess* |
| milli | 10⁻³ | `rim` | *rim* |
| *base* | 10⁰ | *(bare `nu`)* | — |
| kilo | 10³ | `pir` | *peer* |
| mega | 10⁶ | `baf` | *bahf* |
| giga | 10⁹ | `wul` | *wool* |

### Extended Scales (optional)

| Scale | Exponent | Form | Sound |
|-------|----------|------|-------|
| pico | 10⁻¹² | `bim` | *bim* |
| tera | 10¹² | `les` | *less* |
| peta | 10¹⁵ | `gul` | *gul* |
| exa | 10¹⁸ | `fin` | *fin* |
| zetta | 10²¹ | `fus` | *fuss* |
| yotta | 10²⁴ | `hem` | *hem* |

### Base Units from Primitives

SI base units do not receive special CVC forms. The domain root **is** the unit:

| Expression | Reading | SI Equivalent |
|------------|---------|---------------|
| `nu pa` | quantity of space | meter |
| `nu ti` | quantity of time | second |
| `nu ma` | quantity of matter | kilogram |
| `nu ha` | quantity of heat | kelvin |
| `nu lu` | quantity of light | candela |
| `nu ra` | quantity of force | newton / joule |
| `nu so` | quantity of sound | decibel |
| `nu si` | quantity of signal | bit |

### Derived Units

Derived units (newton, joule, pascal, watt) use multi-domain expressions:

```
ra ne ma-ki           → force in relation to matter-in-motion (≈ newton)
ra pa ne fu           → force in relation to space (≈ joule)
```

---

## CVCC Tier: Mathematical and Physical Constants

Constants that are irrational, transcendental, or defined by convention receive CVCC forms — phonologically distinct as a signal: *"This is a fixed external value, not a composite."*

### Mathematical Constants

| Constant | Form | Value | Sound |
|----------|------|-------|-------|
| π | `pelf` | 3.141592… | *pehlf* |
| e | `emel` | 2.71828… | *eh-mehl* |
| φ (golden ratio) | `frim` | 1.618… | *frihm* |

**Usage in expressions:**

```
pelf nu pa            → π meters (quantity of space: pi units)
emel fu                → base of e: 10^e
```

### Physical Constants (in SI units)

| Constant | Form | Approx Value | Sound |
|----------|------|--------------|-------|
| speed of light (c) | `cerl` | 3×10⁸ m/s | *serl* |
| Planck constant (ℏ) | `hels` | 1.055×10⁻³⁴ J·s | *helps* |
| Gravitational constant (G) | `geol` | 6.674×10⁻¹¹ m³/kg·s² | *geh-ohl* |

**Usage:**

```
cerl nu pa ti           → distance light travels in 1 second
hels nu ra ti           → Planck constant: energy-time anchor
```

### Convention-Defined Units

| Unit | Form | Value | Rationale | Sound |
|------|------|-------|-----------|-------|
| Mole | `wels` | 6.022×10²³ | counted by convention, not composition | *wels* |
| AU (astronomical unit) | `holf` | 1.496×10¹¹ m | IAU-defined; no compositional expression | *holf* |
| Parsec | `yarm` | 3.086×10¹⁶ m | parallax-arcsecond; convention-defined | *yarm* |

**Usage:**

```
bol hin nu holf         → 150 AU (inner Oort cloud edge)
bun nu yarm             → 2 parsecs (stellar neighborhood)
pir nu yarm             → 1 kiloparsec (galactic structure)
wul nu yarm             → 1 gigaparsec (cosmological survey depth)
```

### Light-Year (Compositional)

The light-year **has** a compositional expression and receives no CVCC form:

```
lu-ki ti-re nu pa       → distance light travels in one time-cycle
                           (one year, in stellar-astronomy context)
gal bun nu lu-ki ti-re nu pa
                        → 3.2 light-years (using compositional form)
```

---

## Visual-Pattern Modifiers

Light-distribution patterns on surfaces use compositional compounds (not named roots), but function as pre-nominal color-like modifiers:

| Pattern | Compound | Shape | Example |
|---------|----------|-------|---------|
| striped | `lu-di` | linear | `lu-di'zo-se-so-fe` = striped cat |
| spotted | `lu-pe` | dappled | `lu-pe'zo-se-so-fe` = spotted cat |
| solid | `lu-fe` | uniform coat | default when no pattern |

Use `'` (juncture marker) when modifying multi-root compounds.

---

## Scope Rule for Named-Root Modifiers

Colors, scales, and visual patterns all use head-final order — modifier before noun:

```
{modifier} {noun}                    → simple noun
{modifier}'{compound-noun}           → multi-root compound
```

**Examples:**

```
ker mu                               → red object
gal bun nu ti                        → order 32 (ordinal)
pir nu ma                            → kilogram
lu-di mu                             → striped object
lu-pe'zo-se-so-fe                    → spotted cat organism
no-lu'lu-pe'ma-ki'zo-se-so-fe       → dark-spotted water-cat (panther)
```

The `'` is required whenever the noun is a multi-root compound to avoid ambiguity in parsing.

---

## Design Philosophy

Named roots embody a key principle: **preserve the purity of the primitive set by using closed-class, well-defined anchors for everything else.**

The result:
- **CV primitives** remain a small, manageable, ontologically pure set
- **CVC descriptors** provide ergonomic shortforms for frequent closed categories (digits, colors, scales)
- **CVCC constants** admit mathematical and physical values without polluting the primitive tier
- **All other vocabulary** grows compositionally from primitives

This three-tier architecture keeps the language both generative (infinite compounding) and practical (fast recognition of categories and constants).

