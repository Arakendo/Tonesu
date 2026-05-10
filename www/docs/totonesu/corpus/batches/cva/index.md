---
title: "CVA"
---

# CVA

*Theme: [Foundations](../../foundations/overview.md)* · 3 sentences.

:material-book-open-variant: [Full translation analysis](../../translations/science/cvcc-anchors/index.md)

[← Foundations](../../foundations/overview.md) · [← Corpus](../../overview.md)

---

## CVA-001 · 

<span id="S932"></span>
**S932**
`~varn  helms  3.14159`
Written: `~varn helms 3.14159`
*Approximate pi in calculation register.*

!!! annotation "Notes"
    First sentence-level use of a CVCC constant with the canonical `~` approximation mark in technical prose. The subject is not exact `varn` but `~varn`: the calculation is being carried out with a finite decimal approximation of $\pi$, not with the transcendental constant in full precision. `helms` is correct because the sentence is stipulating the value used in this calculation, not merely saying that it behaves like that value. This resolves the practical question raised in the anchor inventory note: the honest scientific form is `~varn`, not bare `varn`, whenever a finite decimal stands in for $\pi$.

<span id="S933"></span>
**S933**
`vern  helms  299792458  nu  pa-ti`
Written: `vern helms 299792458 nu pati`
*Exact SI definition of the speed of light.*

!!! annotation "Notes"
    First running-corpus use of `vern` (speed of light). `nu pa-ti` is the measurement-domain phrase for distance-time quantity, matching the anchor-inventory usage model `vern nu pa-ti`. Unlike S932, this one is unhedged: the SI value of $c$ is exact by definition, so `helms` is the right operator and `~` would be wrong. The sentence confirms that a bare decimal/integer numeral can combine directly with a `nu`-measurement phrase inside ordinary prose without forcing a separate display-equation register.

<span id="S934"></span>
**S934**
`~dolm  helms  9.109 × 10^-31  nu  ma`
Written: `~dolm helms 9.109 × 10^-31 nu ma`
*Approximate electron mass in scientific notation.*

!!! annotation "Notes"
    First running-corpus use of `dolm` (electron mass anchor). `nu ma` supplies the mass domain directly, with no extra unit word required. The scientific-notation block is intentionally written in standard international math notation, which `spec/word-formation.md` explicitly permits for technical prose. The approximation mark belongs on the constant term (`~dolm`), not buried inside the numeric string, because what is being cited is an approximate measured value of the electron mass.

### Batch Summary

| Entry | Form | Test |
|-------|------|------|
| S932 (CVA-001-A) | `~varn helms 3.14159` | approximate CVCC constant with decimal notation |
| S933 (CVA-001-B) | `vern helms 299792458 nu pa-ti` | exact CVCC constant with `nu` measurement phrase |
| S934 (CVA-001-C) | `~dolm helms 9.109 × 10^-31 nu ma` | scientific notation plus approximate atomic-mass anchor |

**Key findings:**

1. **`~` belongs on the constant term, not the digits.** `~varn` and `~dolm` are the honest forms when a finite numeral stands in for an inexact or measured value.
2. **`helms` is right for technical identity statements.** The batch uses it for both exact SI definition (S933) and stipulated approximate-value assignment in a calculation context (S932, S934).
3. **Standard math notation integrates cleanly with prose Tonesu.** Plain decimals and scientific notation can appear directly before `nu` measurement domains without needing a separate grammar device.
4. **CVCC anchors are now usable in real sentence flow.** The constants no longer live only in the anchor inventory; they behave as ordinary technical nouns in the corpus.

**New W-entries:** none

**Compositional first uses:** `pa-ti` (distance-time measurement domain) in running corpus prose.

---

*Generated from [`registry/entries.yaml`](https://github.com/Arakendo/Tonesu/blob/main/registry/entries.yaml).*