---
batch_codes: [GQM]
---
# Translation Test: Geometry Quantities in Running Prose

## Source: exact and approximate geometry quantities expressed as sentence-level technical prose
## Reference: circumference quantity via `π`, full-turn quantity via `τ = 2π`, and unit-square diagonal via `√2`
## Status: Draft — first pass

---

## Purpose

This batch is the geometry bridge that the earlier science work intentionally deferred. CVA-001 proved that bare constants can take decimal and scientific-notation identities in prose. GEO-001 already established the compositional shape vocabulary. What remained open was the middle layer: full geometry quantity phrases such as circumference, full-turn angle, and unit-square diagonal.

This batch therefore does not try to solve area formulas or Euclid yet. It tests the narrower question first: can exact and approximate identities apply to full geometry quantity phrases inside ordinary Tonesu sentences?

Corpus sentences from this batch: **S938–S940**.

---

## Vocabulary Framework

No new vocabulary is introduced. The batch reuses existing CVCC constants and geometry-domain phrases:

| Form | Reading | Status |
|------|---------|--------|
| `varn` | π | existing CVCC constant |
| `worn` | τ | existing CVCC constant |
| `valm` | √2 | existing CVCC constant |
| `pa-re` | spatial cycle / circumference-turn domain | existing compositional geometry domain |
| `nu pa` | quantity of space | existing base measurement domain |

The key change is structural, not lexical: these forms are now used as full sentence constituents rather than remaining inventory examples.

---

## Source Values

The batch uses three geometry-reference values:

```text
π ≈ 3.14159
τ = 2π
√2 ≈ 1.41421
```

Two are approximated because the right side is a finite decimal; one is exact because it states an identity among constants.

---

## Clause-by-Clause Analysis

### S938 — GQM-001-A — Approximate circumference quantity

```
~varn  nu  pa-re  helms  3.14159  nu  pa-re
```

**Written:** `~varn nu pare helms 3.14159 nu pare`

**Parse:**
- `~varn nu pa-re` — approximately π as a circumference quantity
- `helms` — strict identity / current-calculation stipulation
- `3.14159 nu pa-re` — finite decimal circumference quantity in the same domain

**Natural reading:** The circumference quantity is taken as approximately 3.14159.

**Notes:**
This is the first running-corpus use of the full phrase `varn nu pa-re`, which the anchor inventory had already proposed for circumference. The important finding is scope: approximation sits on the whole quantity phrase, not just on the naked constant.

---

### S939 — GQM-001-B — Exact full-turn identity

```
worn  nu  pa  helms  bun  varn  nu  pa
```

**Written:** `worn nu pa helms bun varn nu pa`

**Parse:**
- `worn nu pa` — full-turn / tau quantity of space
- `helms` — exact identity
- `bun varn nu pa` — two pi-quantities of space

**Natural reading:** A full-turn quantity is exactly two pi-quantities of space.

**Notes:**
This sentence gives the `τ = 2π` relation directly in running prose. Because both sides are exact constants in the same geometry domain, approximation would be wrong. The batch therefore gets one exact relation and two approximate finite-decimal realizations.

---

### S940 — GQM-001-C — Approximate unit-square diagonal quantity

```
~valm  nu  pa  helms  1.41421  nu  pa
```

**Written:** `~valm nu pa helms 1.41421 nu pa`

**Parse:**
- `~valm nu pa` — approximately √2 as a spatial quantity
- `helms` — strict identity / current-calculation stipulation
- `1.41421 nu pa` — finite decimal quantity of space

**Natural reading:** The unit-square diagonal quantity is taken as approximately 1.41421.

**Notes:**
This is the first running-corpus use of `valm nu pa`, the anchor-inventory form for the diagonal of a unit square. Like S938, it confirms that irrational geometry values take `~` honestly when represented by finite decimals.

---

## GQM-001 Batch Summary

| Entry | Form | Key test |
|-------|------|----------|
| S938 (GQM-001-A) | `~varn nu pa-re helms 3.14159 nu pa-re` | approximation on full circumference quantity |
| S939 (GQM-001-B) | `worn nu pa helms bun varn nu pa` | exact full-turn quantity identity |
| S940 (GQM-001-C) | `~valm nu pa helms 1.41421 nu pa` | approximation on full diagonal quantity |

**Key findings:**

1. **Approximation scopes over the whole geometry quantity phrase.** This is the geometry-level extension of the CVA-001 result.
2. **Exact geometry identities can remain sentence prose.** `τ = 2π` does not have to be relegated to a display-only formula.
3. **The anchor inventory's geometry examples now have live corpus status.** `varn nu pa-re`, `worn nu pa`, and `valm nu pa` are no longer inventory-only.
4. **This is the right precursor to a fuller geometry batch.** The quantity layer is now grounded without forcing an unsupported area term.

**What remains open:**

- a stable area expression for circle formulas
- fuller use of GEO-001 shape compounds in current technical prose
- a Euclid-style proof or construction batch built on top of these quantity forms

---

## Colloquial Register Analysis

| Form used | CLQ entry | Colloquial form | Notes |
|-----------|-----------|-----------------|-------|
| `~varn nu pa-re` | none | — | geometry quantity phrase with approximation; technical minimum |
| `worn nu pa` | none | — | exact geometry quantity phrase; technical minimum |
| `~valm nu pa` | none | — | geometry quantity phrase with approximation; technical minimum |
| `pa-re` | none | — | compositional geometry domain; technical load-bearing |

**Verdict:** irreducibly formal — the batch exists to preserve exact and approximate geometry quantities, and the current forms are already the shortest legitimate ones.

*CLQ entries registered from this batch: none.*