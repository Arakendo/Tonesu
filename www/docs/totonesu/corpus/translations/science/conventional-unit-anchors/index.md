---
batch_codes: [CUA]
---
# Translation Test: Conventional and Observational CVCC Anchors

## Source: SI and astronomical unit definitions used as sentence-level technical prose
## Reference: exact definitions for the mole, astronomical unit, and Julian year
## Status: Draft — first pass

---

## Purpose

This batch is the direct follow-on to CVA-001. The previous batch proved that CVCC mathematical and physical constants can appear in ordinary corpus sentences with decimal and scientific notation. This batch tests the other half of the same tier: conventional and observational unit anchors.

The question is narrower than a full astronomy or chemistry translation. It is simply whether a CVCC unit anchor can head a normal `nu` measurement phrase inside a clause and take an exact `helms` identity reading without extra grammatical scaffolding.

Corpus sentences from this batch: **S935–S937**.

---

## Vocabulary Framework

No new vocabulary is introduced. The batch activates existing CVCC anchors already defined in the anchor inventory:

| Form | Reading | Status |
|------|---------|--------|
| `wels` | mole | existing CVCC conventional unit anchor |
| `holf` | astronomical unit | existing CVCC observational anchor |
| `hulm` | Julian year | existing CVCC calibrated time anchor |

It also reuses existing measurement domains:

| Form | Reading | Role |
|------|---------|------|
| `nu ru-pe-ma` | quantity of atoms / atomic counting domain | right-side count domain for mole definition |
| `nu pa` | quantity of space / distance domain | right-side distance domain for astronomical unit |
| `nu ti` | quantity of time | right-side time domain for Julian year |

---

## Source Values

The batch uses exact conventional values:

```text
1 mol = 6.02214076 × 10^23 entities
1 AU = 149,597,870,700 m
1 Julian year = 31,557,600 s
```

All three are treated as exact-definition values, not measured approximations. That is why every sentence uses `helms` and none uses `~`.

---

## Clause-by-Clause Analysis

### S935 — CUA-001-A — Exact mole definition

```
wels  nu  ru-pe-ma  helms  6.02214076 × 10^23  nu  ru-pe-ma
```

**Written:** `wels nu rupema helms 6.02214076 × 10^23 nu rupema`

**Parse:**
- `wels nu ru-pe-ma` — one mole in the atomic counting domain
- `helms` — strict identity / exact definition operator
- `6.02214076 × 10^23 nu ru-pe-ma` — exact atomic-entity count in standard notation

**Natural reading:** One mole of atoms is exactly $6.02214076 × 10^{23}$ atoms.

**Notes:**
This is the first running-corpus use of `wels`. The clause keeps the measurement domain explicit on both sides, which makes the structure clearer than treating the mole as a bare disconnected symbol. Because the SI definition fixes the value exactly, approximation would be wrong here.

---

### S936 — CUA-001-B — Exact astronomical-unit definition

```
holf  nu  pa  helms  149597870700  nu  pa
```

**Written:** `holf nu pa helms 149597870700 nu pa`

**Parse:**
- `holf nu pa` — one astronomical unit of distance
- `helms` — strict identity / exact definition
- `149597870700 nu pa` — exact distance quantity in standard numeral form

**Natural reading:** One astronomical unit of distance is exactly 149,597,870,700 meters.

**Notes:**
This is the first running-corpus use of `holf`. It matters because `holf` is not merely a large number; it is an observationally inherited calibration anchor. The clause shows that the same `helms` pattern used for pure constants also works for conventionally fixed distance units.

---

### S937 — CUA-001-C — Exact Julian-year calibration

```
hulm  nu  ti  helms  31557600  nu  ti
```

**Written:** `hulm nu ti helms 31557600 nu ti`

**Parse:**
- `hulm nu ti` — one Julian year of time
- `helms` — exact identity / calibration operator
- `31557600 nu ti` — exact time quantity in seconds

**Natural reading:** One Julian year of time is exactly 31,557,600 seconds.

**Notes:**
This is the first running-corpus use of `hulm`. The sentence also keeps a useful distinction alive: `hulm` is a calibrated astronomical anchor, while `ti-re` remains the ordinary compositional notion of a cycle or year-like recurrence. The batch therefore exercises exact calibration, not just everyday time talk.

---

## CUA-001 Batch Summary

| Entry | Form | Key test |
|-------|------|----------|
| S935 (CUA-001-A) | `wels nu ru-pe-ma helms 6.02214076 × 10^23 nu ru-pe-ma` | exact counting-unit anchor |
| S936 (CUA-001-B) | `holf nu pa helms 149597870700 nu pa` | exact observational distance anchor |
| S937 (CUA-001-C) | `hulm nu ti helms 31557600 nu ti` | exact calibrated time anchor |

**Key findings:**

1. **CVCC unit anchors behave like ordinary measurement heads.** They do not need a special equation-only register.
2. **Exact unit anchors use the same `helms` logic as exact constants.** There is no separate operator for conventional definition.
3. **Domain marking stays explicit and stable.** `nu ru-pe-ma`, `nu pa`, and `nu ti` preserve dimensional clarity on both sides of the identity.
4. **The CVCC tier now has corpus evidence for both constants and units.** Together, CVA-001 and CUA-001 cover the tier's two main jobs.

**What remains open:**

- fuller astronomy prose that uses `holf` compositionally inside larger clauses
- chemistry sentences that move from exact mole definition to reagent or stoichiometric use
- deeper contrast between calibrated `hulm` and ordinary cycle language like `ti-re`

---

## Colloquial Register Analysis

| Form used | CLQ entry | Colloquial form | Notes |
|-----------|-----------|-----------------|-------|
| `wels nu ru-pe-ma` | none | — | CVCC unit anchor + counting domain; technical minimum |
| `holf nu pa` | none | — | CVCC unit anchor + distance domain; technical minimum |
| `hulm nu ti` | none | — | CVCC unit anchor + time domain; technical minimum |
| `ru-pe-ma` | none | — | compositional counting domain; technical load-bearing |

**Verdict:** irreducibly formal — the batch exists to preserve calibration-level exactness, and the current forms are already the shortest legitimate ones.

*CLQ entries registered from this batch: none.*