---
batch_codes: [CVA]
---
# Translation Test: CVCC Anchors in Running Prose

## Source: Technical reference values (SI exact definitions + rounded scientific reference values)
## Reference: exact `c` value from the SI definition; approximate decimal or scientific-notation values for `π` and electron mass
## Status: Draft — first pass

---

## Purpose

This batch is the smallest useful science-register test still missing from the corpus: not a big theory translation, but actual sentence-level use of CVCC constants in technical prose.

It tests four things at once:

- whether CVCC anchors can function as ordinary sentence subjects rather than inventory items
- whether standard decimal and scientific notation can be embedded directly in Tonesu clauses
- whether `~` belongs on the constant term when a cited value is approximate
- whether `helms` is the right operator for numeric identity statements in technical register

This is not yet a full geometry or quantum-physics batch. It is the narrower prerequisite: get the constant-and-measurement syntax clean first, then expand outward.

Corpus sentences from this batch: **S932–S934**.

---

## Vocabulary Framework

No new vocabulary is introduced. The batch activates existing CVCC anchors from the anchor inventory:

| Form | Reading | Status |
|------|---------|--------|
| `varn` | π | existing CVCC mathematical constant |
| `vern` | speed of light `c` | existing CVCC physical constant |
| `dolm` | electron mass `m_e` | existing CVCC atomic-mass anchor |

One compositional measurement-domain phrase appears in running corpus prose for the first time:

| Form | Reading | Construction |
|------|---------|--------------|
| `pa-ti` | distance-time quantity / spatial-over-temporal measurement domain | `pa` (space) + `ti` (time) |

The batch also reuses established measurement syntax:

- `{number} nu {domain}` for numeric quantities
- `~` on the left edge of the approximated unit
- standard international math notation for the numeral itself

---

## Source Values

The batch uses the following technical values:

```text
π ≈ 3.14159
c = 299,792,458 m/s
m_e ≈ 9.109 × 10^-31 kg
```

The distinction between exact and approximate values is the whole point of the batch:

- `c` is exact by SI definition, so it appears unhedged.
- `π` and `m_e` are cited in finite decimal form, so the constant term is hedged with `~`.

---

## Clause-by-Clause Analysis

### S932 — CVA-001-A — Approximate pi in calculation prose

```
~varn  helms  3.14159
```

**Written:** `~varn helms 3.14159`

**Parse:**
- `~varn` — approximately π; the approximated value of the pi constant used for this calculation
- `helms` — strict identity / exact stipulation operator
- `3.14159` — standard decimal numeral in technical notation

**Natural reading:** For this calculation, pi is taken as 3.14159.

**Notes:**
This sentence answers a question the anchor inventory explicitly raised: if a speaker is using a finite decimal in place of π, the honest subject is `~varn`, not bare `varn`. Bare `varn` names the exact transcendental constant. `~varn` names the approximated calculation value. `helms` is still correct because the sentence is not philosophically defining π; it is stipulating the identity of the approximated value in the current technical context.

---

### S933 — CVA-001-B — Exact speed-of-light definition

```
vern  helms  299792458  nu  pa-ti
```

**Written:** `vern helms 299792458 nu pati`

**Parse:**
- `vern` — speed of light constant `c`
- `helms` — strict identity / exact definition
- `299792458` — standard decimal integer
- `nu pa-ti` — quantity of distance-time; the measurement domain corresponding to meters per second

**Natural reading:** The speed of light is exactly 299,792,458 meters per second.

**Notes:**
This is the decisive exactness case. `vern` is unhedged because the SI definition of `c` is exact. The sentence also confirms the key prose-format point: a plain numeral can precede a `nu` measurement phrase directly, with no extra connective or formula wrapper needed. The result is ordinary Tonesu technical prose, not a detached display equation.

---

### S934 — CVA-001-C — Approximate electron mass in scientific notation

```
~dolm  helms  9.109 × 10^-31  nu  ma
```

**Written:** `~dolm helms 9.109 × 10^-31 nu ma`

**Parse:**
- `~dolm` — approximately the electron-mass constant
- `helms` — identity / current-value stipulation
- `9.109 × 10^-31` — scientific-notation numeral
- `nu ma` — quantity of matter / mass domain

**Natural reading:** The electron mass is taken as approximately $9.109 × 10^{-31}$ kilograms.

**Notes:**
This is the batch's scientific-notation test. The notation remains standard international math notation, exactly as the spec permits for technical prose. The approximation belongs on the constant term (`~dolm`) rather than being left implicit, because the speaker is citing an approximate measured value of the constant, not the constant in ideal full precision.

---

## CVA-001 Batch Summary

| Entry | Form | Key test |
|-------|------|----------|
| S932 (CVA-001-A) | `~varn helms 3.14159` | approximate CVCC constant with decimal notation |
| S933 (CVA-001-B) | `vern helms 299792458 nu pa-ti` | exact CVCC constant with measurement domain |
| S934 (CVA-001-C) | `~dolm helms 9.109 × 10^-31 nu ma` | scientific notation with approximate atomic-mass anchor |

**Key findings:**

1. **Approximation should scope over the constant, not be hidden in the digits.** `~varn` and `~dolm` make the epistemic status explicit.
2. **`helms` is the right operator for technical numeric identities.** It works both for exact SI definition and for stipulated approximate calculation values.
3. **Standard math notation and Tonesu prose coexist cleanly.** The batch does not need a special equation grammar to embed numbers in sentences.
4. **The `nu` measurement frame scales into technical prose without strain.** `nu pa-ti` and `nu ma` behave like normal sentence constituents.

**What remains open:**

- geometry vocabulary for full circle-area prose
- a fuller treatment of reduced Planck constant and quantum-action phrasing
- broader calculation chains beyond single identity statements

This batch therefore closes the notation-and-embedding question first, while leaving the higher-level science vocabulary for a later pass.

---

## Colloquial Register Analysis

| Form used | CLQ entry | Colloquial form | Notes |
|-----------|-----------|-----------------|-------|
| `~varn` | none | — | CVCC anchor + approximation mark; technical minimum |
| `vern` | none | — | CVCC anchor; already atomic minimum |
| `~dolm` | none | — | CVCC anchor + approximation mark; technical minimum |
| `pa-ti` | none | — | 2-root measurement domain — below threshold |
| `nu ma` | none | — | base measurement phrase — below threshold |

**Verdict:** irreducibly formal — the batch exists to preserve exact technical calibration, and the CVCC anchors are already the shortest legitimate forms.

*CLQ entries registered from this batch: none.*