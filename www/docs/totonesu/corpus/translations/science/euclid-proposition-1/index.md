---
title: "Euclid I.1 — Construct an Equilateral Triangle"
batch_codes: [EUC]
source: "Euclid, Elements, Book I, Proposition 1"
sentences: S1238–S1243
w_entries: none
status: active
---

# Euclid I.1

## Source

> On a given finite straight line, to construct an equilateral triangle.

---

## Purpose

This batch is the first Euclid-style geometry proof in running Tonesu prose. GEO-001 already established the compositional geometry lexicon, and PRF-001 already established nested proof structure with `go`. The open question is narrower: can an actual construction proof be written using the existing geometry system without forcing new primitive vocabulary or collapsing back into pseudo-formula notation?

This first pass chooses Proposition 1 rather than a longer theorem because it keeps the pressure local:

- bounded segment vocabulary (`fe-di-fe`)
- circle construction using point-centered naming conventions
- point-on-circle reasoning as a geometry relation
- equality claims via `su-ne`
- equilateral-triangle conclusion via `su-ne-ru`

No new vocabulary is registered here. The batch instead tests whether the existing geometry layer can be made to carry a classical construction proof with only compositional extensions and explicit notes.

Corpus sentences from this batch: **S1238–S1243**.

---

## Notation Convention For This Batch

To keep the proof legible, the batch uses ordinary Tonesu naming structure with geometry categories attached:

| Form | Reading | Function |
|------|---------|----------|
| `[pa-ru na A]` | point A | named point |
| `[fe-di-fe na A-B]` | segment AB | named bounded segment |
| `[fe-re-ru na A-B]` | circle centered at A through B | center-first circle name |
| `[su-fe-re nu-bol na A-B-C]` | triangle ABC | named triangle |

The name order in a circle matters for the proof notes: `A-B` means center A, through-point B. For the bounded segment itself, `A-B` and `B-A` refer to the same finite segment under opposite orientation.

---

## Clause-by-Clause Analysis

### S1238 — EUC-001-A — Let AB be a bounded segment

```
lo-[fe-di-fe  na A-B]  ne  fe-di-fe
```

**Written:** `lofedife na A-B ne fedife`

**Natural reading:** AB is a bounded segment.

**Notes:** This states the given line in the exact geometric form GEO-001 already licensed: `fe-di-fe` is the bounded line segment, not the unbounded `fe-di` line. The sentence is intentionally spare because the proof depends on this object remaining stable across every later clause.

### S1239 — EUC-001-B — Draw the circles A-B and B-A

```
la-ze  ka  lo-[fe-re-ru  na A-B]  /  la-ze  ka  lo-[fe-re-ru  na B-A]
```

**Written:** `laze ka lofereru na A-B / laze ka lofereru na B-A`

**Natural reading:** One draws the circle centered at A through B, and one draws the circle centered at B through A.

**Notes:** No new circle lexeme is needed. The proof uses naming convention rather than lexical innovation: the first point in the name is the center, the second is the through-point. The `/` holds the paired construction steps together without making one causally prior to the other.

### S1240 — EUC-001-C — Let C be the point where the circles meet

```
lo-[pa-ru  na C]  ne  [fe-re-ru  na A-B]  /  lo-[pa-ru  na C]  ne  [fe-re-ru  na B-A]
```

**Written:** `loparu na C ne [fereru na A-B] / loparu na C ne [fereru na B-A]`

**Natural reading:** C is on the circle A-B, and C is on the circle B-A.

**Notes:** This batch uses bare `ne` as the geometry incidence relation: point C stands in the relevant boundary relation to each circle. That is the smallest plausible extension from GEO-001's existing geometric relation use, and it is enough for the proof.

### S1241 — EUC-001-D — From the first circle, CA equals AB

```
go {lo-[pa-ru  na C]  ne  [fe-re-ru  na A-B]},  lo-[fe-di-fe  na C-A]  su-ne  lo-[fe-di-fe  na A-B]
```

**Written:** `go {loparu na C ne [fereru na A-B]}, lofedife na C-A sune lofedife na A-B`

**Natural reading:** Because C lies on circle A-B, segment CA equals segment AB.

**Notes:** `su-ne` is the right equality predicate here: the claim is not identity but equal relational measure. The geometry reason is Euclid's ordinary one: all segments from the center of a circle to its boundary are equal to the defining radius.

### S1242 — EUC-001-E — From the second circle, CB equals AB

```
go {lo-[pa-ru  na C]  ne  [fe-re-ru  na B-A]},  lo-[fe-di-fe  na C-B]  su-ne  lo-[fe-di-fe  na A-B]
```

**Written:** `go {loparu na C ne [fereru na B-A]}, lofedife na C-B sune lofedife na A-B`

**Natural reading:** Because C lies on circle B-A, segment CB equals segment AB.

**Notes:** The circle name is reversed because its center is B, but the radius is still the same given bounded segment AB read from the opposite endpoint. This keeps the theorem on the original given object rather than introducing a second segment-name into the conclusion.

### S1243 — EUC-001-F — Therefore triangle ABC is equilateral

```
go {lo-[fe-di-fe  na C-A]  su-ne  lo-[fe-di-fe  na A-B]  ;  lo-[fe-di-fe  na C-B]  su-ne  lo-[fe-di-fe  na A-B]},  lo-[su-fe-re  nu-bol  na A-B-C]  ne  su-ne-ru
```

**Written:** `go {lofedife na C-A sune lofedife na A-B ; lofedife na C-B sune lofedife na A-B}, losufere nubol na A-B-C ne suneru`

**Natural reading:** Because CA equals AB and CB equals AB, triangle ABC has equal sides.

**Notes:** This is the theorem payoff. `su-ne-ru` is the formal geometric equal-sides qualifier already introduced in GEO-001; here it is applied to the named triangle rather than to a generic square definition. The batch thereby confirms that the old shape vocabulary and the old proof vocabulary meet cleanly in a real Euclidean construction.

---

## EUC-001 Batch Summary

| Entry | Form | Key test |
|-------|------|----------|
| S1238 (EUC-001-A) | `lo-[fe-di-fe na A-B] ne fe-di-fe` | given bounded segment as proof anchor |
| S1239 (EUC-001-B) | paired circle construction | center-first circle naming convention |
| S1240 (EUC-001-C) | point C on both circles | geometry incidence via `ne` |
| S1241 (EUC-001-D) | `C-A su-ne A-B` | equality from first circle |
| S1242 (EUC-001-E) | `C-B su-ne A-B` | equality from second circle |
| S1243 (EUC-001-F) | triangle ABC `ne su-ne-ru` | equilateral conclusion from equal-segment premises |

**Key findings:**

1. **Euclid-style proof prose is possible without new primitives.** GEO-001 and PRF-001 were sufficient scaffolding.
2. **Named geometry objects can be kept readable with category-first naming.** `[pa-ru na A]`, `[fe-di-fe na A-B]`, and `[fe-re-ru na A-B]` are legible enough for proof work.
3. **`ne` is sufficient for the first incidence relation test.** The proof does not need a dedicated new geometry preposition just to say that a point lies on a circle.
4. **`su-ne` and `su-ne-ru` divide the work cleanly.** `su-ne` handles segment equality; `su-ne-ru` handles equal-sided figure classification.

**What remains open:**

- whether circle-center / radius language should later be lexicalized for longer geometry proofs
- whether line-intersection and angle-bisection proofs can stay equally clean with bare `ne`
- whether a fuller Euclid series should keep this naming convention or move to a more explicit formal header

**Conclusion:** Euclid I.1 works as a genuine Tonesu proof batch, not merely as a glossary exercise. The language can already carry short classical constructions in running prose.

---

## Colloquial Register Analysis

| Form used | CLQ entry | Colloquial form | Notes |
|-----------|-----------|-----------------|-------|
| `fe-di-fe` | none | — | formal geometry object; shortest accurate form |
| `fe-re-ru` | none | — | formal geometry object; shortest accurate form |
| `su-ne` | none | — | equality relation is the point of the batch |
| `su-ne-ru` | none | — | formal equal-sided classifier; load-bearing |

**Verdict:** irreducibly formal.

*CLQ entries registered from this batch: none.*