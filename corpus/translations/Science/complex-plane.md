---
title: "Complex Plane / Imaginary Axis Probe"
batch_codes: [CPX]
source: "Synthetic mathematics stress test: complex unit and axis language"
sentences: S1244–S1273
w_entries: none
status: active
---

# Complex Plane / Imaginary Axis Probe

## Purpose

This batch is not full complex analysis. It is the narrower stress test that the current repo actually needs first: can Tonesu say anything disciplined about the imaginary unit and an imaginary axis without pretending that the whole complex-number system is already naturalized?

The batch therefore stays local and conservative.

It tests:

- whether the admitted anchor `walf` can function as a sentence-level mathematical constant
- whether `nu-to` is good enough for an axis / parameter reading in formal mathematics
- whether `walf nu-to` cleanly distinguishes an imaginary axis from physical `pa-di` dimensions
- whether a two-axis complex model can be stated without inventing a dedicated plane lexeme

It does **not** try to solve complex arithmetic, coordinate-pair notation, or full analytic geometry.

Corpus sentences from this batch: **S1244–S1248**.

---

## Vocabulary Framework

No new W-entries are introduced.

This batch reuses one admitted anchor and two existing compositional resources:

| Form | Reading | Status |
|------|---------|--------|
| `walf` | imaginary unit `i` | admitted anchor inventory constant |
| `nu-to` | axis / parameter / quantitative concept | existing compositional candidate |
| `pa-di` | spatial dimension | W229 |

Compositional first use in this batch:

| Form | Reading | Notes |
|------|---------|-------|
| `walf nu-to` | imaginary axis | `walf` specifies the axis by the imaginary unit rather than by physical space |

---

## Clause-by-Clause Analysis

### S1244 — CPX-001-A — The imaginary unit is a quarter-turn relation

```
walf  helms  fe-di-ne  ru-pu
```

**Written:** `walf helms fedine rupu`

**Natural reading:** The imaginary unit is by definition a quarter-turn relation.

**Notes:** This is the smallest usable sentence for `walf`. The anchor inventory already glosses it as a 90° rotation in the complex plane, and GEO-001 already established `fe-di-ne ru-pu` as the quarter-turn / right-angle relation. `helms` is correct because the sentence is definitional, not merely analogical.

### S1245 — CPX-001-B — Axis I is an imaginary axis

```
lo-[nu-to  na I]  ne  walf  nu-to
```

**Written:** `lonuto na I ne walf nuto`

**Natural reading:** Axis I is the imaginary axis.

**Notes:** First corpus use of `walf nu-to`. `nu-to` is doing the axis / parameter work; `walf` marks which axis it is. This is the key compositional move of the batch.

### S1246 — CPX-001-C — Axis I is not a spatial dimension

```
lo-[nu-to  na I]  no  ne  pa-di
```

**Written:** `lonuto na I no ne padi`

**Natural reading:** Axis I is not a spatial dimension.

**Notes:** This is the important contrast sentence. The batch does not want the imaginary axis to silently collapse into STR-001's `pa-di` spatial-dimension vocabulary. It is an axis of calculation, not a physical direction through space.

### S1247 — CPX-001-D — The complex model has two axes

```
la-[to-su  na Complex]  ne  bun  nu-to
```

**Written:** `latosu na Complex ne bun nuto`

**Natural reading:** The complex model has two axes.

**Notes:** This reuses the STR-001 pattern `la-pa ne bol bol nu pa-di`, but changes the counted object from physical dimensions to formal axes. No dedicated "complex plane" lexeme is introduced; the model itself is enough for this first probe.

### S1248 — CPX-001-E — The R-axis is a quantity axis, and the I-axis is a walf-axis

```
lo-[nu-to  na R]  ne  nu-to  /  lo-[nu-to  na I]  ne  walf  nu-to
```

**Written:** `lonuto na R ne nuto / lonuto na I ne walf nuto`

**Natural reading:** The R-axis is the ordinary quantity axis, and the I-axis is the walf-axis.

**Notes:** This is the batch payoff. It shows that Tonesu can keep the two axes distinct without inventing a new primitive for "real." The unmarked `nu-to` serves as the default quantity axis; `walf nu-to` marks the imaginary one.

---

## CPX-001 Batch Summary

| Entry | Form | Key test |
|-------|------|----------|
| S1244 (CPX-001-A) | `walf helms fe-di-ne ru-pu` | imaginary unit as quarter-turn definition |
| S1245 (CPX-001-B) | `I = walf nu-to` | first imaginary-axis phrase |
| S1246 (CPX-001-C) | `I no ne pa-di` | axis vs physical dimension split |
| S1247 (CPX-001-D) | `Complex = bun nu-to` | two-axis model statement |
| S1248 (CPX-001-E) | `R = nu-to / I = walf nu-to` | ordinary-axis / imaginary-axis contrast |

**Key findings:**

1. **Tonesu can express an imaginary axis compositionally.** `walf nu-to` is legible enough for a first corpus use.
2. **The language can keep imaginary-axis talk separate from physical dimension talk.** `nu-to` and `pa-di` do not collapse into each other.
3. **A narrow complex-plane model can be described without a special lexeme for plane.** The model is stated as a two-axis system rather than as a newly named object-class.

**What remains open:**

- coordinate-pair notation and point placement, addressed in CPX-002 below
- multiplication/addition rules involving `walf`
- whether a later batch should lexicalize a more specific plane/field term

**Conclusion:** Tonesu can express imaginary-axis language decently at the level of constants, axes, and model structure. Full complex-number prose remains to be pressure-tested separately.

---

## CPX-002 — Coordinate Pairs and Axis Placement

## Purpose

CPX-001 showed that Tonesu can name the imaginary axis without collapsing it into physical dimension language. The next unresolved question is narrower: can the language represent complex-plane points by coordinate pair and use that pair to state axis membership cleanly?

This follow-up keeps the scope tight:

- ordered coordinate-pair notation using `{}` in mathematical register
- named points with existing `pa-ru`
- axis membership from a zero coordinate
- off-axis placement when both coordinates are non-zero

It still does **not** attempt full complex arithmetic.

Corpus sentences from this batch: **S1249–S1253**.

---

## Notation Convention For This Batch

| Form | Reading | Function |
|------|---------|----------|
| `{X, Y}` | ordered coordinate pair | first slot = R-axis, second slot = I-axis |
| `[pa-ru na Z]` | point Z | named point |
| `[nu-to na R]` | R-axis | default quantity axis |
| `[nu-to na I]` | I-axis | `walf`-marked axis established in CPX-001 |

The pair is treated as an ordered mathematical representation, so `helm` is used for point-to-coordinate rendering rather than `helms` strict definitional identity.

---

## Clause-by-Clause Analysis

### S1249 — CPX-002-A — Point Z is represented by the pair {2, 0}

```
lo-[pa-ru  na Z]  helm  {bun,  nil}
```

**Written:** `loparu na Z helm {bun, nil}`

**Natural reading:** Point Z is represented as the coordinate pair {2, 0}.

**Notes:** This is the first direct coordinate-pair sentence in the corpus. `helm` is the right identity strength here: the point is being rendered under a coordinate system, not reduced to pure definition. `bun` and `nil` keep the first test case minimal.

### S1250 — CPX-002-B — Therefore Z lies on the R-axis

```
go {lo-[pa-ru  na Z]  helm  {bun,  nil}},  lo-[pa-ru  na Z]  ne  [nu-to  na R]
```

**Written:** `go {loparu na Z helm {bun, nil}}, loparu na Z ne [nuto na R]`

**Natural reading:** Because Z is {2, 0}, Z lies on the R-axis.

**Notes:** The second coordinate being zero is enough for axis membership. The sentence reuses the same incidence-style `ne` relation that EUC-001 used for point-on-circle reasoning, now extended to point-on-axis reasoning.

### S1251 — CPX-002-C — Point Y is represented by the pair {0, 2}

```
lo-[pa-ru  na Y]  helm  {nil,  bun}
```

**Written:** `loparu na Y helm {nil, bun}`

**Natural reading:** Point Y is represented as the coordinate pair {0, 2}.

**Notes:** This mirrors S1249 with the coordinate order reversed. That reversal is the whole point of the batch: the slot order inside `{}` matters.

### S1252 — CPX-002-D — Therefore Y lies on the I-axis

```
go {lo-[pa-ru  na Y]  helm  {nil,  bun}},  lo-[pa-ru  na Y]  ne  [nu-to  na I]
```

**Written:** `go {loparu na Y helm {nil, bun}}, loparu na Y ne [nuto na I]`

**Natural reading:** Because Y is {0, 2}, Y lies on the I-axis.

**Notes:** This confirms that the ordered-pair notation is doing real structural work rather than decorative bookkeeping. Swapping the zero from the second slot to the first changes the axis claim.

### S1253 — CPX-002-E — A point with two non-zero coordinates lies on neither axis alone

```
go {lo-[pa-ru  na W]  helm  {bun,  bun}},  lo-[pa-ru  na W]  no  ne  [nu-to  na R]  /  lo-[pa-ru  na W]  no  ne  [nu-to  na I]
```

**Written:** `go {loparu na W helm {bun, bun}}, loparu na W no ne [nuto na R] / loparu na W no ne [nuto na I]`

**Natural reading:** Because W is {2, 2}, W lies on neither the R-axis nor the I-axis alone.

**Notes:** This is the discriminating check for the whole batch. A non-zero / non-zero pair should not collapse onto either single axis. The `/` is correct because the sentence makes two parallel denials about the same point.

---

## CPX-002 Batch Summary

| Entry | Form | Key test |
|-------|------|----------|
| S1249 (CPX-002-A) | `Z helm {bun, nil}` | first coordinate-pair rendering |
| S1250 (CPX-002-B) | `go {Z = {2,0}}, Z on R` | zero-imaginary coordinate implies R-axis membership |
| S1251 (CPX-002-C) | `Y helm {nil, bun}` | coordinate-order reversal |
| S1252 (CPX-002-D) | `go {Y = {0,2}}, Y on I` | zero-real coordinate implies I-axis membership |
| S1253 (CPX-002-E) | `go {W = {2,2}}, no R / no I` | non-zero pair stays off both single axes |

**Key findings:**

1. **Tonesu can render ordered coordinate pairs without a new primitive.** `{X, Y}` plus explicit slot notes is enough for a first corpus pass.
2. **`helm` cleanly handles mathematical representation.** It is stronger than loose analogy but weaker than strict constitutive identity.
3. **Point-on-axis reasoning composes cleanly with existing geometry relations.** The same `ne` incidence logic used in geometry can extend to formal axes.

**What remains open now:**

- addition rules involving `walf`
- explicit rotation under repeated `walf` application once negative coordinates are grounded
- whether later complex-analysis prose wants a dedicated field/plane lexeme

---

## CPX-003 — First Walf Multiplication

## Purpose

CPX-002 established coordinate-pair notation, but it still stopped short of the actual complex-number pressure point: what does multiplication by `walf` do to a represented point?

This batch takes the narrowest next step that the current repo can support cleanly:

- first operator-application notation in mathematical register
- one explicit `walf` multiplication on an R-axis point
- resulting migration onto the I-axis
- fixed-point behavior at the origin

It deliberately does **not** go further into repeated multiplication, because that would immediately force a negative-coordinate convention that the corpus has not yet grounded.

Corpus sentences from this batch: **S1254–S1258**.

---

## Notation Convention For This Batch

| Form | Reading | Function |
|------|---------|----------|
| `walf [point-term]` | the result of multiplying that point by `walf` | first operator-application notation |
| `[pa-ru na Z]` | point Z | source point |
| `[pa-ru na O]` | origin point | fixed-point test |

The notation is intentionally minimal: the constant is written directly before the point-term, and `helm` still carries the representational claim. This keeps the new pressure local to operator application rather than inventing a separate multiplication symbol system.

---

## Clause-by-Clause Analysis

### S1254 — CPX-003-A — Point Z is represented by the pair {2, 0}

```
lo-[pa-ru  na Z]  helm  {bun,  nil}
```

**Written:** `loparu na Z helm {bun, nil}`

**Natural reading:** Point Z is represented as the coordinate pair {2, 0}.

**Notes:** This restates the starting point because CPX-003 is testing an operation on an explicit input, not merely referring back to CPX-002 elliptically.

### S1255 — CPX-003-B — Multiplying Z by walf yields {0, 2}

```
go {walf  helms  fe-di-ne  ru-pu  ;  lo-[pa-ru  na Z]  helm  {bun,  nil}},  walf  lo-[pa-ru  na Z]  helm  {nil,  bun}
```

**Written:** `go {walf helms fedine rupu ; loparu na Z helm {bun, nil}}, walf loparu na Z helm {nil, bun}`

**Natural reading:** Because `walf` is a quarter-turn and Z is {2, 0}, multiplying Z by `walf` yields {0, 2}.

**Notes:** This is the first actual operator sentence in the complex-plane track. The left side gathers the two premises already established elsewhere in the file; the right side states the rotated result. The batch uses only the first-quarter-turn case so the result stays within already-grounded non-negative digits.

### S1256 — CPX-003-C — Therefore walf·Z lies on the I-axis, not the R-axis

```
go {walf  lo-[pa-ru  na Z]  helm  {nil,  bun}},  walf  lo-[pa-ru  na Z]  ne  [nu-to  na I]  /  walf  lo-[pa-ru  na Z]  no  ne  [nu-to  na R]
```

**Written:** `go {walf loparu na Z helm {nil, bun}}, walf loparu na Z ne [nuto na I] / walf loparu na Z no ne [nuto na R]`

**Natural reading:** Because `walf·Z` is {0, 2}, `walf·Z` lies on the I-axis and not on the R-axis.

**Notes:** This is the behavioral payoff. Multiplication by `walf` is not treated as an abstract algebraic ritual; it visibly relocates the point from one axis to the other.

### S1257 — CPX-003-D — Point O is represented by the pair {0, 0}

```
lo-[pa-ru  na O]  helm  {nil,  nil}
```

**Written:** `loparu na O helm {nil, nil}`

**Natural reading:** Point O is represented as the coordinate pair {0, 0}.

**Notes:** The origin is the cheapest discriminating check for fixed-point behavior under the operation: if `walf` changes the origin, the operator notation is wrong.

### S1258 — CPX-003-E — Multiplying the origin by walf leaves it at the origin

```
go {lo-[pa-ru  na O]  helm  {nil,  nil}},  walf  lo-[pa-ru  na O]  helm  {nil,  nil}
```

**Written:** `go {loparu na O helm {nil, nil}}, walf loparu na O helm {nil, nil}`

**Natural reading:** Because O is {0, 0}, multiplying O by `walf` leaves it at {0, 0}.

**Notes:** This confirms that the operator syntax is not just a relabeling device for one special point. It also identifies the origin as the stable center of the quarter-turn system.

---

## CPX-003 Batch Summary

| Entry | Form | Key test |
|-------|------|----------|
| S1254 (CPX-003-A) | `Z helm {bun, nil}` | explicit input point |
| S1255 (CPX-003-B) | `go {walf = quarter-turn ; Z = {2,0}}, walf Z = {0,2}` | first `walf` multiplication result |
| S1256 (CPX-003-C) | `go {walf Z = {0,2}}, on I / not on R` | operator result changes axis membership |
| S1257 (CPX-003-D) | `O helm {nil, nil}` | origin as fixed-point test input |
| S1258 (CPX-003-E) | `go {O = {0,0}}, walf O = {0,0}` | origin remains fixed |

**Key findings:**

1. **A first-pass multiplication notation is workable.** `walf [point-term]` is readable enough for operator application in mathematical register.
2. **`walf` multiplication can be stated as a geometric action on coordinates.** The batch makes the quarter-turn claim operational rather than merely definitional.
3. **The origin behaves correctly as a fixed point.** That gives the operator notation a cheap internal consistency check before more ambitious arithmetic is attempted.

**What remains open after CPX-003:**

- repeated `walf` multiplication beyond the first quarter-turn, addressed in CPX-004 below
- negative-coordinate notation for second- and third-quadrant results, addressed in CPX-004 below
- addition and multiplication of general complex pairs

---

## CPX-004 — Repeated Walf Rotation and Signed Coordinates

## Purpose

CPX-003 established the first quarter-turn. The next unresolved pressure point is whether Tonesu can continue that rotation into the second and third quadrants without collapsing when negative coordinates appear.

This batch therefore tests two things together:

- repeated operator application by direct `walf walf ...` stacking
- signed-coordinate notation without fusing `no-` onto CVC digits

The goal is still modest. It does not attempt full arithmetic on arbitrary pairs. It only asks whether repeated quarter-turn behavior can remain legible once the coordinates pass below zero.

Corpus sentences from this batch: **S1259–S1263**.

---

## Notation Convention For This Batch

| Form | Reading | Function |
|------|---------|----------|
| `walf walf X` | apply `walf` twice to X | repeated operator application |
| `no [digit]` inside `{}` | negative coordinate value | signed slot notation without digit fusion |

The sign is written as a separate operator, not a fused compound. This matters because the digit anchors are CVC-tier atoms, not ordinary CV roots. `{no bun, nil}` is therefore read as a signed coordinate slot, not as a newly compounded lexical form.

For English-side summary shorthand in this track, repeated application may be written in standard formula style as `walf^n`, but the shorthand should stay visibly paired with the older expanded form when comparison matters. For example, the core corpus form `walf walf walf walf lo-[pa-ru na Z] helm lo-[pa-ru na Z]` can be summarized beside it as `walf^4 Z helm Z`, with display typography `walf⁴ Z helm Z` reserved for contexts where superscript rendering is actually helpful. The actual Tonesu notation lines keep the fully expanded operator chain.

---

## Clause-by-Clause Analysis

### S1259 — CPX-004-A — `walf·Z` is represented by the pair {0, 2}

```
walf  lo-[pa-ru  na Z]  helm  {nil,  bun}
```

**Written:** `walf loparu na Z helm {nil, bun}`

**Natural reading:** `walf·Z` is represented as the pair {0, 2}.

**Notes:** This restates the CPX-003 output as the explicit input to the next quarter-turn. The batch is testing iteration, so the intermediate state must be made overt.

### S1260 — CPX-004-B — Applying `walf` again yields {−2, 0}

```
go {walf  lo-[pa-ru  na Z]  helm  {nil,  bun}},  walf  walf  lo-[pa-ru  na Z]  helm  {no  bun,  nil}
```

**Written:** `go {walf loparu na Z helm {nil, bun}}, walf walf loparu na Z helm {no bun, nil}`

**Natural reading:** Because `walf·Z` is {0, 2}, applying `walf` again yields {−2, 0}.

**Notes:** This is the core signed-coordinate probe. The negative value is written as `no bun`, with the sign kept separate from the digit anchor. That is the smallest move that respects the CVC digit tier while still letting the batch say something exact about quadrant change.

### S1261 — CPX-004-C — The second-quarter-turn result lies on the R-axis, not the I-axis

```
go {walf  walf  lo-[pa-ru  na Z]  helm  {no  bun,  nil}},  walf  walf  lo-[pa-ru  na Z]  ne  [nu-to  na R]  /  walf  walf  lo-[pa-ru  na Z]  no  ne  [nu-to  na I]
```

**Written:** `go {walf walf loparu na Z helm {no bun, nil}}, walf walf loparu na Z ne [nuto na R] / walf walf loparu na Z no ne [nuto na I]`

**Natural reading:** Because `walf^2·Z` is {−2, 0}, it lies on the R-axis and not on the I-axis.

**Notes:** The important point is structural, not metaphysical: a negative real coordinate is still real-axis placement. Axis membership depends on which slot is zero, not on the sign of the remaining slot.

### S1262 — CPX-004-D — Applying `walf` a third time yields {0, −2}

```
go {walf  walf  lo-[pa-ru  na Z]  helm  {no  bun,  nil}},  walf  walf  walf  lo-[pa-ru  na Z]  helm  {nil,  no  bun}
```

**Written:** `go {walf walf loparu na Z helm {no bun, nil}}, walf walf walf loparu na Z helm {nil, no bun}`

**Natural reading:** Because `walf^2·Z` is {−2, 0}, applying `walf` a third time yields {0, −2}.

**Notes:** This confirms that the sign convention works in either slot position. The repeated-operator notation remains readable even at three applications, which is the real syntactic stress test here.

### S1263 — CPX-004-E — The third-quarter-turn result lies on the I-axis, not the R-axis

```
go {walf  walf  walf  lo-[pa-ru  na Z]  helm  {nil,  no  bun}},  walf  walf  walf  lo-[pa-ru  na Z]  ne  [nu-to  na I]  /  walf  walf  walf  lo-[pa-ru  na Z]  no  ne  [nu-to  na R]
```

**Written:** `go {walf walf walf loparu na Z helm {nil, no bun}}, walf walf walf loparu na Z ne [nuto na I] / walf walf walf loparu na Z no ne [nuto na R]`

**Natural reading:** Because `walf^3·Z` is {0, −2}, it lies on the I-axis and not on the R-axis.

**Notes:** This completes the three-quarter-turn path without requiring a full general theory of signed arithmetic. The same axis-membership logic survives once the sign convention is introduced.

---

## CPX-004 Batch Summary

| Entry | Form | Key test |
|-------|------|----------|
| S1259 (CPX-004-A) | `walf Z = {0,2}` | explicit intermediate input |
| S1260 (CPX-004-B) | `walf walf Z = {no bun, nil}` | first negative real coordinate |
| S1261 (CPX-004-C) | `walf^2 Z on R / not on I` | signed real still counts as R-axis placement |
| S1262 (CPX-004-D) | `walf walf walf Z = {nil, no bun}` | first negative imaginary coordinate |
| S1263 (CPX-004-E) | `walf^3 Z on I / not on R` | signed imaginary still counts as I-axis placement |

**Key findings:**

1. **Repeated `walf` application remains legible under direct stacking.** The notation survives second and third application without new operator machinery.
2. **Signed coordinates can be written without violating the digit tier.** `no [digit]` works as a slot-level sign notation while preserving the CVC atom itself.
3. **Axis-membership logic survives sign inversion.** What matters is which coordinate is zero, not whether the non-zero coordinate is positive or negative.

**What remains open after CPX-004:**

- the fourth quarter-turn and explicit return to the starting point, addressed in CPX-005 below
- addition and multiplication of general complex pairs
- whether the signed-slot convention should be generalized beyond this batch into formal math guidance

---

## CPX-005 — Fourth Quarter-Turn and Return

## Purpose

CPX-004 carried the rotation through three quarter-turns. The next exact question is whether the system closes cleanly on the fourth turn: does another application of `walf` return the point to its original coordinates, and can Tonesu state that return without confusing coordinate equality, axis membership, and point identity?

This batch keeps those claims separate on purpose:

- explicit third-turn input
- fourth-turn coordinate result
- recovered R-axis placement
- original-point coordinate restatement
- return-to-point equivalence claim

Corpus sentences from this batch: **S1264–S1268**.

---

## Clause-by-Clause Analysis

### S1264 — CPX-005-A — `walf^3·Z` is represented by the pair {0, −2}

```
walf  walf  walf  lo-[pa-ru  na Z]  helm  {nil,  no  bun}
```

**Written:** `walf walf walf loparu na Z helm {nil, no bun}`

**Natural reading:** `walf^3·Z` is represented as the pair {0, −2}.

**Notes:** This restates the CPX-004 result as the explicit input for the final quarter-turn. The closure batch needs the third-turn state overt rather than merely implied.

### S1265 — CPX-005-B — Applying `walf` a fourth time yields {2, 0}

```
go {walf  walf  walf  lo-[pa-ru  na Z]  helm  {nil,  no  bun}},  walf  walf  walf  walf  lo-[pa-ru  na Z]  helm  {bun,  nil}
```

**Written:** `go {walf walf walf loparu na Z helm {nil, no bun}}, walf walf walf walf loparu na Z helm {bun, nil}`

**Natural reading:** Because `walf^3·Z` is {0, −2}, applying `walf` a fourth time yields {2, 0}.

**Notes:** This is the closure claim proper: the fourth quarter-turn returns the coordinates to the original positive-real position.

### S1266 — CPX-005-C — The fourth-turn result lies on the R-axis, not the I-axis

```
go {walf  walf  walf  walf  lo-[pa-ru  na Z]  helm  {bun,  nil}},  walf  walf  walf  walf  lo-[pa-ru  na Z]  ne  [nu-to  na R]  /  walf  walf  walf  walf  lo-[pa-ru  na Z]  no  ne  [nu-to  na I]
```

**Written:** `go {walf walf walf walf loparu na Z helm {bun, nil}}, walf walf walf walf loparu na Z ne [nuto na R] / walf walf walf walf loparu na Z no ne [nuto na I]`

**Natural reading:** Because `walf^4·Z` is {2, 0}, it lies on the R-axis and not on the I-axis.

**Notes:** This confirms that the closure is not merely symbolic recurrence. The point has returned to the same structural axis relation it started from.

### S1267 — CPX-005-D — Point Z is represented by the pair {2, 0}

```
lo-[pa-ru  na Z]  helm  {bun,  nil}
```

**Written:** `loparu na Z helm {bun, nil}`

**Natural reading:** Point Z is represented as the pair {2, 0}.

**Notes:** This repeats the original coordinate claim so the return statement can cite two explicit premises inside the same local proof slice.

### S1268 — CPX-005-E — Therefore four `walf` applications return to point Z

```
go {walf  walf  walf  walf  lo-[pa-ru  na Z]  helm  {bun,  nil}  ;  lo-[pa-ru  na Z]  helm  {bun,  nil}},  walf  walf  walf  walf  lo-[pa-ru  na Z]  helm  lo-[pa-ru  na Z]
```

**Written:** `go {walf walf walf walf loparu na Z helm {bun, nil} ; loparu na Z helm {bun, nil}}, walf walf walf walf loparu na Z helm loparu na Z`

**Natural reading:** Because both the fourth-turn result and Z are represented by {2, 0}, four `walf` applications return to point Z.

**Notes:** `helm` is the right identity strength here. The claim is return-under-the-given coordinate representation, not a new definitional identity for `walf^4` in every possible context. This is enough to close the cycle without overstating the algebra.

---

## CPX-005 Batch Summary

| Entry | Form | Key test |
|-------|------|----------|
| S1264 (CPX-005-A) | `walf^3 Z = {nil, no bun}` | explicit third-turn input |
| S1265 (CPX-005-B) | `walf^4 Z = {bun, nil}` | fourth quarter-turn returns original coordinates |
| S1266 (CPX-005-C) | `walf^4 Z on R / not on I` | original axis relation restored |
| S1267 (CPX-005-D) | `Z = {bun, nil}` | original-point coordinate restatement |
| S1268 (CPX-005-E) | `go {walf^4 Z = {2,0} ; Z = {2,0}}, walf^4 Z = Z` | return-to-point equivalence |

**Key findings:**

1. **The operator cycle closes cleanly after four applications.** The quarter-turn sequence returns the point to its original coordinates.
2. **Tonesu can distinguish coordinate recurrence from point recurrence.** The batch states same-coordinate and same-point claims in separate steps rather than conflating them.
3. **`helm` is sufficient for return identity under a chosen model.** The language can say that the fourth-turn result is the same represented point without claiming a stronger definitional identity than the data warrants.

**What remains open after CPX-005:**

- whether the `walf` cycle should be explicitly tied to `worn` / full-turn language in a later batch, addressed in CPX-006 below
- addition and multiplication of general complex pairs
- whether the signed-slot convention should be generalized beyond this local track into formal mathematical guidance

---

## CPX-006 — Walf Cycle as Full Turn

## Purpose

CPX-005 closed the operator cycle, but it still left one explicit bridge unmade: how does that four-turn closure relate to the repo's already admitted full-turn constant `worn`?

This batch makes only that bridge.

It tests:

- exact quarter-turn language using the fully explicit fraction form `ru-pu mol`
- four-application return stated again as the cycle's input fact
- functional equivalence between `walf^4` and a full-turn angle quantity
- first direct use of `fe-di-ne nu worn`
- reconnection of the complex-plane track to the earlier `worn = 2π` geometry quantity work

Corpus sentences from this batch: **S1269–S1273**.

---

## Clause-by-Clause Analysis

### S1269 — CPX-006-A — The imaginary unit is exactly a quarter-turn

```
walf  helms  fe-di-ne  ru-pu  mol
```

**Written:** `walf helms fedine rupu mol`

**Natural reading:** The imaginary unit is by definition a quarter-turn.

**Notes:** CPX-001 already used the context-short form `fe-di-ne ru-pu`. This sentence makes the fraction fully explicit by using the grammar's established `ru-pu mol` = one-quarter form.

### S1270 — CPX-006-B — Four applications of `walf` return Z to Z

```
walf  walf  walf  walf  lo-[pa-ru  na Z]  helm  lo-[pa-ru  na Z]
```

**Written:** `walf walf walf walf loparu na Z helm loparu na Z`

**Natural reading:** Four applications of `walf` return point Z to Z.

**Notes:** This restates the CPX-005 closure in the most compressed form. The batch needs that return relation overt because it is the concrete basis for calling the cycle a full turn rather than merely four unrelated operations.

### S1271 — CPX-006-C — Therefore four applications of `walf` function as one full-turn angle quantity

```
go {walf  helms  fe-di-ne  ru-pu  mol  ;  walf  walf  walf  walf  lo-[pa-ru  na Z]  helm  lo-[pa-ru  na Z]},  walf  walf  walf  walf  helm  fe-di-ne  nu  worn
```

**Written:** `go {walf helms fedine rupu mol ; walf walf walf walf loparu na Z helm loparu na Z}, walf walf walf walf helm fedine nu worn`

**Natural reading:** Because `walf` is a quarter-turn and four applications return Z to Z, four applications of `walf` function as one full-turn angle quantity.

**Notes:** `helm` is the right strength here. The batch is not claiming that the repeated operator string and the angle quantity are the same kind of thing in every context; it is claiming functional equivalence within the current model.

### S1272 — CPX-006-D — A full-turn angle quantity is represented by `worn`

```
fe-di-ne  nu  worn  helm  worn
```

**Written:** `fedine nu worn helm worn`

**Natural reading:** A full-turn angle quantity is represented by `worn`.

**Notes:** This is the first direct use of `fe-di-ne nu worn` in the corpus. The sentence links the general angle-quantity frame from GEO-001 to the CVCC constant inventory without requiring a new lexeme for radians.

### S1273 — CPX-006-E — `worn` is exactly two pi-quantities

```
worn  nu  pa  helms  bun  varn  nu  pa
```

**Written:** `worn nu pa helms bun varn nu pa`

**Natural reading:** `worn` is exactly two pi-quantities.

**Notes:** This reuses the established `τ = 2π` identity from GQM-001, now as the final integration point for the complex-plane track. The result is a clean chain: `walf` = quarter-turn, four `walf` applications = full turn, full-turn angle quantity = `worn`, and `worn` = `2π`.

---

## CPX-006 Batch Summary

| Entry | Form | Key test |
|-------|------|----------|
| S1269 (CPX-006-A) | `walf helms fe-di-ne ru-pu mol` | exact quarter-turn statement |
| S1270 (CPX-006-B) | `walf^4 Z = Z` | compact cycle-closure restatement |
| S1271 (CPX-006-C) | `go {quarter-turn ; return}, walf^4 ~ full-turn` | operator cycle to full-turn bridge |
| S1272 (CPX-006-D) | `fe-di-ne nu worn helm worn` | first direct full-turn angle quantity phrase |
| S1273 (CPX-006-E) | `worn nu pa helms bun varn nu pa` | reconnects to existing tau identity |

**Key findings:**

1. **The complex-plane `walf` cycle can now be stated in the repo's older geometry-constant language.** The four-turn closure is no longer isolated from `worn`.
2. **`fe-di-ne nu worn` is a workable angle-quantity phrase.** That gives the project a direct way to talk about full-turn angle quantity inside the existing angle frame.
3. **The track now closes across three surfaces at once:** operator application, geometric angle relation, and CVCC constant inventory.

**What remains open after CPX-006:**

- addition and multiplication of general complex pairs
- whether the signed-slot convention should be generalized beyond this local track into formal mathematical guidance
- whether later prose should introduce a more compact notation for repeated operator powers beyond `^n` shorthand

---

## Notation Pressure and Resolution

The CPX track exposed a real notation pressure rather than a cosmetic preference.

### Pressure

Three pressures converged:

1. **Repeated operator chains become visually heavy.** By CPX-005 and CPX-006, forms like `walf walf walf walf lo-[pa-ru na Z] ...` remained parseable but stopped being easy to scan in summaries and cross-batch comparisons.
2. **Scientific discourse already expects exponent-style shorthand.** The repo already permits standard mathematical notation in technical writing, and other scientific materials already use forms such as `10^23`, `m_e`, `m_p`, `k₂`, and `H₂O`.
3. **Reference-heavy registers want compact index marks.** Legal, scholarly, and technical documents often need citation pointers, footnote numbering, variable indices, and labeled references that are clearer in superscript/subscript form than in full prose restatement.

### Resolution

The resolution is deliberately narrow.

- **Superscript and subscript are admitted in the international technical-notation register.**
- They are **written-only conventions**, not new native Tonesu notation marks.
- They do **not** receive spoken forms and do not enlarge the punctuation inventory in `spec/phonology.md`.
- **Canonical plain-text form remains `^` and underscore-style indexing.** So `walf^4` is the default typed shorthand; display forms like `walf⁴` are acceptable where typography permits.
- Subscript is allowed for indices, scientific labels, chemical formulas, and reference pointers: `x_1`, `m_e`, `m_p`, `H₂O`, `CO₂`, and footnote/citation numbering in legal or scholarly documents.

### Result for the CPX track

The CPX batch family now uses three distinct layers cleanly, and the same example can be shown side by side so the shorthand never replaces the native form:

| Layer | Example |
|------|---------|
| Core Tonesu notation line | `walf walf walf walf lo-[pa-ru na Z] helm lo-[pa-ru na Z]` |
| Math-register shorthand | `walf^4 Z helm Z` |
| Display-only typography | `walf⁴ Z helm Z` |

That keeps the corpus faithful to native structure while still letting technical writing breathe.

---

## Colloquial Register Analysis

| Form used | CLQ entry | Colloquial form | Notes |
|-----------|-----------|-----------------|-------|
| `walf` | none | — | CVCC constant; technical atom |
| `nu-to` | none | — | compositional formal axis term; load-bearing |
| `walf nu-to` | none | — | first-use formal compound phrase |
| `pa-di` | none | — | physical-dimension term; contrast is the point |
| `pa-ru` | none | — | 2-root geometry atom; already minimal |
| `no [digit]` | none | — | formal signed-slot notation; technical only |

**Verdict:** irreducibly formal.

*CLQ entries registered from this batch: none.*