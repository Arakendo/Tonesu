---
title: "CUA"
---

# CUA

*Theme: [Foundations](../../foundations/overview.md)* · 3 sentences.

:material-book-open-variant: [Full translation analysis](../../translations/science/conventional-unit-anchors/index.md)

[← Foundations](../../foundations/overview.md) · [← Corpus](../../overview.md)

---

## CUA-001 · 

<span id="S935"></span>
**S935**
`wels  nu  ru-pe-ma  helms  6.02214076 × 10^23  nu  ru-pe-ma`
Written: `wels nu rupema helms 6.02214076 × 10^23 nu rupema`
*Exact mole definition in counting register.*

!!! annotation "Notes"
    First running-corpus use of `wels` (mole). The subject is the full measurement NP `wels nu ru-pe-ma`: one mole in the atomic counting domain. This is exact, not approximate, because the modern SI definition fixes the mole by exact entity count. The sentence confirms that a CVCC unit anchor can sit on the left side of `helms` just as cleanly as a physical constant.

<span id="S936"></span>
**S936**
`holf  nu  pa  helms  149597870700  nu  pa`
Written: `holf nu pa helms 149597870700 nu pa`
*Exact astronomical-unit definition.*

!!! annotation "Notes"
    First running-corpus use of `holf` (astronomical unit). `nu pa` supplies the distance domain on both sides of the identity, making the clause explicitly dimensional rather than treating `holf` as a bare symbol. Like S935, this is exact by definition rather than estimated observation, so `helms` is the right operator and `~` would misstate the status of the value.

<span id="S937"></span>
**S937**
`hulm  nu  ti  helms  31557600  nu  ti`
Written: `hulm nu ti helms 31557600 nu ti`
*Exact Julian-year calibration.*

!!! annotation "Notes"
    First running-corpus use of `hulm` (Julian year). This sentence distinguishes the calibrated astronomical time anchor from the ordinary compositional cycle notion `ti-re`. The batch therefore confirms that the same identity pattern works across counting (`wels`), distance (`holf`), and time (`hulm`) without any new grammar.

### Batch Summary

| Entry | Form | Test |
|-------|------|------|
| S935 (CUA-001-A) | `wels nu ru-pe-ma helms 6.02214076 × 10^23 nu ru-pe-ma` | exact counting-unit anchor in prose |
| S936 (CUA-001-B) | `holf nu pa helms 149597870700 nu pa` | exact observational distance anchor in prose |
| S937 (CUA-001-C) | `hulm nu ti helms 31557600 nu ti` | exact calibrated time anchor in prose |

**Key findings:**

1. **CVCC unit anchors integrate cleanly with `nu` phrases.** `wels`, `holf`, and `hulm` work as the heads of full measurement NPs in ordinary clause position.
2. **`helms` remains the correct operator for definition-level unit statements.** All three values are conventionally fixed, so approximation would be structurally false.
3. **The same identity template scales across distinct domains.** Counting, distance, and time all use the same clause pattern without extra machinery.
4. **The CVCC tier now has live corpus evidence on both sides of its design brief.** CVA-001 covered constants; CUA-001 covers conventional/observational units.

**New W-entries:** none

**Compositional first uses:** `ru-pe-ma` as an explicit right-side counting domain in a `helms` identity sentence.

---

*Generated from [`registry/entries.yaml`](https://github.com/Arakendo/Tonesu/blob/main/registry/entries.yaml).*