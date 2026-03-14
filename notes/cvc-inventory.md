# CVC Descriptor Inventory: Digits, Colors, Scale Prefixes

## Status: Proposed — March 2026

Working document. Forms here are candidates. None are formally registered until registry entries are created.

---

## Purpose

Three closed-class descriptor categories — numerals (digits 0–9), basic colors, and SI-style magnitude scale prefixes — are assigned to the **CVC phonological stratum**. This follows the design rationale in `notes/numbers-colors-others.md`:

- CV = primitives (closed set)
- CV-CV+ = compounds (open, compositional)
- CVC = lexical descriptors (closed-class, fast-recognition)

CVC forms are phonologically stratified from primitives and compounds, giving instant category recognition and avoiding collision with the existing root inventory.

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

**Note:** peta (10¹⁵), exa (10¹⁸) and sub-nano scales are unassigned; extend when corpus pressure arises. Free CV stems available for future scale words include: `fi`, `fo`, `fu`, `ga`, `gu`, `he`, `hi`, `ho`, `hu`, `ya`, `wa`, `wo`, `wu`... (consult spec audit minus any assignments made here).

---

## Cross-inventory Collision Check

### Uniqueness

All 27 proposed forms are distinct:

> nil bol bun gal mol hin wes yom fon zan  
> yel yim ker gim pom sam tem dol kus  
> zum mes rim pir baf wul bim les

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

No dangerous near-homophones across categories. ✓

---

## Flags and Open Questions

### FLAG-CVC-001 — `vo` vs. `v`-exclusion inconsistency ✓ RESOLVED

`spec/phonology.md` previously excluded `v` despite `vo` (R024, value/quality) already using it. **Resolution (March 2026): option A adopted — `v` added to the consonant inventory as the 17th consonant.** `spec/phonology.md §Consonant Inventory` updated; total count corrected from 16 to 17; exclusion note updated.

### FLAG-CVC-002 — Spec CVC shortlist fully consumed by digits

All 8 forms from `spec/phonology.md §CVC Root Reserve` shortlist are assigned to digits 1–8. The spec comment ("No form on this list is assigned yet, March 2026") must be updated once these assignments are committed.

### FLAG-CVC-003 — Large number expression

Digit chaining (`wes nil nil nu mu` = 600) is unambiguous but verbose for large numbers in ordinary speech. Options: (a) accept positional chaining only; (b) add explicit power-of-ten words (`ten`, `hundred`, `thousand` equivalents as additional CVC forms); (c) route large exact values through the scale prefix system (`pir nu mu` ≈ thousand objects). Defer until corpus shows a real pressure; log under NUM-001 in open-questions.md.

### FLAG-CVC-005 — Names and loanwords may collide with CVC layer

Proper names and borrowed vocabulary — personal names, place names, AI system names, titles — have no assigned phonological tier. If ad-hoc CVC forms are used for names, they will be indistinguishable from digit/color/scale descriptors at first glance. **Options:** (a) reserve **CVCC** (CVC + extra coda) or **CV-CVC** (hyphenated compound) as the name/loanword tier; (b) rely on the `na` proper-name particle (G008) to signal context without a separate phonological tier. Option (b) is probably sufficient and lower-complexity. Defer until a corpus sentence requires a proper name; track under `spec/naming.md`.

---

### FLAG-CVC-004 — `nu-to` dual assignment

`nu-to` appears in `registry/primitives.md` stress-test table as both "axis of measurement / dimension" and "probability / confidence level." These are two contextually determined readings of the same compound. **This is intentional and unproblematic** — English does the same thing with *weight* (physical / importance / statistical). Measurement context vs. epistemic context disambiguates reliably. No new primitive, no respelling needed. Document the disambiguation principle in the `nu-to` entry comment for future readers, and cross-reference from NUM-001.
