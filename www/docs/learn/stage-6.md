# Stage 6 — Epistemic discipline

In Stage 3 you saw that `se`, `si`, and `to` form an entailment ladder. This stage
goes deeper: the negated half of that ladder works backwards, there is a structural
move that makes reported evidence look like personal certainty, and three different
identity predicates encode three genuinely different claims. Every point here is load-
bearing — the grammar will not stop you from saying the wrong thing, but it will make
the wrong thing structurally visible.

---

## Cluster 1 — The epistemic ladder, both directions

Stage 3 introduced the positive scale:

| Level | Root | Meaning | Entails |
|-------|------|---------|---------|
| Perceptual floor | `se` | I have signal / I perceive | — |
| Hypothesis | `si` | I am assessing / I hypothesize | entails `se` |
| Established | `to` | I hold as known / I am certain | entails `si`, `se` |

The entailment flows upward: you cannot hold something as established unless you
also hypothesize it and have a perceptual basis for it. `se` is necessary for `si`;
`si` is necessary for `to`.

### The negated half — reversal

Negate each level with `no-` and the entailment direction flips:

| Negated form | Meaning | Entails |
|--------------|---------|---------|
| `no-to` | I do not hold as established | — |
| `no-si` | I do not hypothesize | entails `no-to` |
| `no-se` | I have no perceptual basis | entails `no-si`, `no-to` |

The *floor denial* is the strongest claim. `no-se` forecloses everything: if you have
no perceptual basis at all, you cannot hypothesize and you certainly cannot hold it as
established. `no-to` alone is the weakest denial — it leaves open the possibility
that you hypothesize (`si`) or even perceive (`se`) the thing, just not at established
certainty.

This is non-obvious. Most speakers reach first for `no-to` when they want to express
uncertainty. But `no-to` is compatible with having a strong hypothesis. When you truly
have nothing — no signal whatsoever — `no-se` is the honest form.

### Minimal pair: the corpus case

From C007:

```
la-mi   to   {la-tu  no-se  lo-ne-ra}
```
*I hold as established: that you have no perceptual basis for the resonance.*  (C007 A5)

The outer frame `la-mi to {…}` certifies as established. The inner claim `la-tu
no-se lo-ne-ra` = "you have no perceptual basis for the resonance." The speaker is
not saying "I don't believe the resonance" — they are saying they are *certain* the
other person has *no signal at all* for it. Floor-denial nested inside established
certainty.

### The forbidden upgrade

The epistemic levels are a one-way commitment. You cannot move from `si` to `to`
by assertion alone. A well-formed progression requires new grounding at each step:

```
la-mi  si  {lo-X}                      →  I hypothesize X
go  {la-mi  se  lo-X  ta-ti-mi}  ,     →  because now I perceive X,
du  la-mi  to  {lo-X}                  →  I now hold X as established
```

The fallacious shortcut:
```
la-mi  si  {lo-X}  ,  (du  la-mi  to  {lo-X})
```
*I hypothesize X; (therefore, allegedly: I know X.)*  (S373 modal fallacy)

The `(du …)` wrapper marks the conclusion as reported/ungrounded. A speaker who
drops the `()` is claiming that hypothesis alone yields certainty — making the
forbidden upgrade structurally explicit and therefore challengeable.

---

!!! question "Exercise 1 — *Strongest denial*"
    A colleague asks if you have any basis for a claim — not just uncertainty, but
    truly no signal at all. Which form is correct?

    <div class="tn-learn-mcq"
         data-answer="c"
         data-ok="Correct — no-se: the floor denial. No perceptual basis = no signal at all. This forecloses everything above it ✓"
         data-nok="no-to says only that you don't hold it as established — you might still hypothesize it or perceive it. The floor denial is no-se."
         data-options='[{"id":"a","text":"`no-to` — I do not hold this as established (leaves open: might still hypothesize)"},{"id":"b","text":"`no-si` — I do not hypothesize this (leaves open: might still perceive a signal)"},{"id":"c","text":"`no-se` — I have no perceptual basis at all (forecloses hypothesis and certainty)"}]'>
    </div>

??? success "Explanation"
    The negation scale is the mirror of the positive scale — but reversed. In the
    positive direction, `se` is required for `si`, which is required for `to`:
    claiming certainty without perception is incoherent.

    In the negative direction, `no-se` subsumes everything: no signal means no
    hypothesis and no certainty. `no-to` alone is merely saying "I'm not certain" —
    consistent with having a strong working hypothesis. Reach for `no-se` when you
    genuinely have nothing to report.

---

## Cluster 2 — The evidential frame `()`

The personal epistemic modal (`la-mi  se/si/to`) tells your interlocutor *how you
relate* to a claim — your own calibrated commitment. The evidential frame `()` does
something different: it suspends attribution entirely.

```
(clause)      →   reportedly / allegedly / it is said that {clause}
```

Content inside `()` is presented as received, in circulation, or epistemically
reserved — **not directly asserted by the speaker from their own resources**. No
assertor is named. This is the tool for cited evidence, contested claims, and hearsay.

### Three source types, compared

| Form | Assertor | When to use |
|------|----------|-------------|
| `la-mi  se/si/to  {prop}` | speaker | my own calibrated commitment |
| `la-source  be/si  {prop}` | named non-personal source | process or doctrine output |
| `(prop)` | none | anonymous report, hearsay, epistemic reservation |

### The `(du …)` pattern

`du` is the result/therefore particle. When it appears inside `()`, the result is
a "reportedly-therefore" — an inference presented as ungrounded:

```
(premise)  ,  (du  conclusion)
```
*Reportedly: premise. Reportedly-therefore: conclusion.*

This is the honest form for a cited argument: you neither confirm the premise nor
endorse the inference. Compare:

```
(la-to-li  lo-to-su  no-to)  ,  (du  lo-to-su  no-be)
```
*(The scholar reportedly does not accept the model.)
 (Therefore, reportedly: the model does not hold.)*  (S369)

vs the dishonest form:
```
la-mi  to  lo-to-su  no-be  ,  go  (la-to-li  lo-ze  no-to)
```
*I know the model is false — because (reportedly the scholar did not accept it).*

In the second form, `la-mi  to` claims first-person certainty, then grounds it with a
`go`-link to a `()` premise. The structure makes the move visible: you are claiming
certainty from an anonymous report. The grammar does not block this, but any
interlocutor can challenge it: "why does a reported source yield your personal `to`?"

### `~` stacking with `()`

`~` (ven) is the pre-positional approximation hedge. It can wrap the frame or sit
inside it, and the two positions are semantically distinct:

```
~ (la-Elohim  ra-no-fe)      →   it is reportedly (and I'm uncertain about the report
                                  itself) that God is all-powerful
(~ la-Elohim  ra-no-fe)      →   it is reported: God is approximately all-powerful
```

`~` outside brackets: the speaker hedges the entire act of reporting.
`~` inside brackets: the content of the report is hedged. The report itself is taken
at face value; only its claim is approximate.

---

!!! question "Exercise 2 — *Laundered or honest?*"
    One of these forms makes the epistemic laundering move — asserting certainty from
    a reported premise. Which one?

    *(A = the scholar · B = the speaker)*

    <div class="tn-learn-mcq"
         data-answer="b"
         data-ok="Correct — la-mi to ... go (...): personal certainty (la-mi to) grounded by a go-link to a reported premise (()). The () premise cannot yield la-mi to without independent grounding ✓"
         data-nok="The honest form keeps both premise and conclusion inside () — neither is the speaker's direct assertion. The laundering form uses la-mi to as the matrix predicate."
         data-options='[{"id":"a","text":"`(la-to-li lo-to-su no-to)  ,  (du lo-to-su no-be)` — both premise and conclusion inside (): reportedly the scholar does not accept the model; reportedly therefore it does not hold"},{"id":"b","text":"`la-mi to lo-to-su no-be  ,  go (la-to-li lo-ze no-to)` — I know the model is false, because reportedly the scholar did not accept it"}]'>
    </div>

??? success "Explanation"
    The honest form (A) wraps both the premise and the conclusion in `()`. The speaker
    presents both as reported/uncertain — `(du …)` = reportedly-therefore. Neither the
    claim about the scholar nor the inference is directly asserted.

    The laundering form (B) lifts the conclusion out of `()` with `la-mi to` — first-
    person certainty — then grounds it via `go` on a `()` premise. The structure says:
    *I am certain* because *allegedly the scholar said so*. The `go`-link bridges an
    anonymous report to a personal certainty claim. A `to`-level commitment requires a
    `se`-level basis: perception, confirmed source, or demonstrated reasoning — not
    an unverified citation.

---

## Cluster 3 — `~` (ven) as epistemic tool

`~` hedges precision without collapsing a claim. It is not doubt — it is the
acknowledgment that a quantity, value, or category is being given to approximation
resolution.

```
pu-to-su  ne  ven  du-to        →  All models are approximately correct.    (S445)
pu-to-su  ne  ven  no-du-to     →  All models are approximately wrong.      (S446)
```

Both sentences are true of the same referent. This is not a contradiction — it is
Box's point: a model near the precision boundary is simultaneously `ven du-to` and
`ven no-du-to`. `ven` is symmetric: the hedge runs in both directions from the
boundary.

This makes `~` an honest tool. When a model is genuinely near the precision
boundary, asserting `du-to` without `~` overclaims; asserting `no-du-to` without
`~` also overclaims. Only `ven` captures the epistemic situation accurately.

Compare `~` with the evidential frame: `()` suspends attribution; `~` hedges
precision while still asserting. `ven du-to` is still an assertion — just a hedged
one. `(du-to)` is a report — attributed to no one.

### When `~` is wrong

`~` is wrong when you *do* have the precision. Do not hedge to seem modest. If you
measured the temperature as 38°C, `ven nu-ha-be-fe` is evasion, not epistemic care.
The tool is honest to the resolution of your actual knowledge. Applying it where you
have precision is itself a form of miscalibration in the other direction.

---

## Cluster 4 — The identity spectrum: `ne` / `helm` / `helms`

These are three distinct predicates, not stylistic variants. Each makes a different
kind of claim.

### `ne` — property attribution

`ne` attributes a quality or state to an entity. The claim can be contingent or
structural depending on the particle used (Stage 3, Cluster 2), but it does not
assert that the subject *is* the predicate — only that the subject *has* or *holds*
the predicate.

```
lo-li  vo          →   The person is valued.           (contingent state)
la-li  vo          →   A person has worth.              (structural property)
```

`vo` is attributed to `li` — not identified with it.

### `helm` — functional equivalence

`helm` asserts that X is *functionally understood as* Y in some domain or context.
Not a logical identity — a pragmatic or cultural one. The claim can be challenged by
pointing to the domain where it breaks down.

```
to-su  helm  ra        →  Knowledge is power.          (S439, Bacon)
ti     helm  nu-vo     →  Time is money.                (S440, Franklin)
go-no-fe  helm  de     →  God is [culturally] dead.     (S441, Nietzsche)
```

All three are domain-specific pragmatic assertions. None of them would survive as
`helms` — which is why `helm` is the right operator here.

### `helms` — strict definitional identity

`helms` asserts X *is by definition* Y. The right-hand side gives the essential
nature of the left. This is a strong commitment: you are saying the subject cannot
be what it is without being the predicate.

```
go-no-fe  helms  vo     →  God is by definition love.  (S442, 1 John 4:8)
zo-li  helms  to-zo     →  A human is by definition a rational animal.  (S443, Aristotle)
```

Contrast S441 (`helm de`) vs S442 (`helms vo`): same subject `go-no-fe`, different
operators. The cultural claim about the death of God uses `helm` because it is a
functional/cultural observation — contradiction with `helms` is the whole point
of the provocation. The theological claim uses `helms` because it is a constitutional
definition.

### The three-way scale

```
la-li  vo             →  a person has worth                (property)
li  helm  vo-li       →  a person functions as a valued-agent  (functional)
zo-li  helms  to-zo   →  a human is by definition rational  (definitional)
```

| Predicate | Operator | What it claims |
|-----------|----------|---------------|
| `ne` | property | the subject holds or is in this state |
| `helm` | functional | the subject is pragmatically understood as this in context |
| `helms` | definitional | the subject cannot be what it is without being this |

### The Cogito — a useful non-example

```
la-mi  to  go  la-mi  pa        →  I think, therefore I am.  (S444, Descartes)
```

The Cogito deliberately uses `go` (causal deduction), not `helm` or `helms`.
"I think" is not identified with "I exist" — Descartes is *inferring* existence from
the undeniable fact of thought. If he had written `la-mi  to  helms  la-mi  pa`, he
would be claiming that thinking *is by definition* existing — a much stronger and
arguably circular claim. The choice of `go` over `helms` is correct and meaningful.

---

!!! question "Exercise 3 — *Property, functional, or definitional?*"
    `Knowledge is power` — Bacon's pragmatic claim about what knowledge does in
    human affairs. Which operator is correct?

    <div class="tn-learn-mcq"
         data-answer="b"
         data-ok="Correct — helm: to-su helm ra. Knowledge is functionally understood as power in human affairs. Not a structural property (ne), not a logical definition (helms) ✓"
         data-nok="ne would say knowledge merely has the property of power. helms would claim knowledge is power by definition — too strong for Bacon's pragmatic point."
         data-options='[{"id":"a","text":"`ne` — property attribution: knowledge has the property of power"},{"id":"b","text":"`helm` — functional: knowledge is understood as power in human affairs"},{"id":"c","text":"`helms` — definitional: knowledge is by definition power"}]'>
    </div>

??? success "Explanation"
    Bacon's claim is pragmatic: in the domain of human affairs, organized knowledge
    *behaves as* force. This is not a structural property (`ne`) and not a logical
    definition (`helms`). `helm` is precise: the claim applies within a context, can
    be challenged in other contexts, and doesn't collapse into an equation.

    `helms` would say knowledge *cannot be what it is* without being power — true of
    Aristotle's "man is a rational animal" or John's "God is love," but not of Bacon,
    who is observing a domain regularity, not asserting an essence.

    S444 (Descartes) shows the fourth option: `go` for a causal inference. The Cogito
    is not an identity claim; it is a deduction. `helm`/`helms` would misrepresent it.

---

!!! question "Exercise 4 — *Calibrate the claim*"
    Complete: `la-mi  ___  {lo-de  no-ru}` — I am *assessing*, not certain: the
    decay is unstable.

    <div class="tn-learn-picker"
         data-template="la-mi  ___  {lo-de  no-ru}"
         data-answer="si"
         data-mode="form"
         data-ok="si — hypothesis. I am assessing that the decay is unstable. Not yet se (mere perception) nor to (established) ✓"
         data-nok="se = I have signal; si = I am assessing / I hypothesize; to = I hold as established. For an active assessment, use si."
         data-items='[{"form":"se","gloss":"perceptual floor — I have signal"},{"form":"si","gloss":"hypothesis — I am assessing"},{"form":"to","gloss":"established — I hold as known"}]'>
    </div>

??? success "Explanation"
    `si` is the hypothesis level — an active assessment, not yet at certainty.

    `la-mi  si  {lo-de  no-ru}` = "I hypothesize that the decay is unstable"
    (C001 A3). Corpus first attestation of `si` in this sentence context. Moving to
    `to` requires new evidence: perception (`se`) or a confirmed source that grounds
    the upgrade. Asserting `to` from `si` alone is the modal fallacy (S373).

---

## Summary: when to use what

| Situation | Tool | Form |
|-----------|------|------|
| Your own direct perception | Personal modal: `se` | `la-mi se {…}` |
| Your working hypothesis | Personal modal: `si` | `la-mi si {…}` |
| Your established knowledge | Personal modal: `to` | `la-mi to {…}` |
| No evidence whatsoever | Floor denial: `no-se` | `la-mi no-se {…}` |
| Someone else's claim, unverified | Evidential frame | `(claim)` |
| Inference from reported premise | `(du …)` pattern | `(premise) , (du conclusion)` |
| Precision is genuinely approximate | Approximation hedge | `ven X` or `~X` |
| Property / state | Property copula | `ne` |
| Functional / pragmatic equivalence | Functional predicate | `helm` |
| Constitutive definition | Identity predicate | `helms` |

---

## Next

[Stage 7 — Production](stage-7.md) moves from analysis to output: writing original
sentences from prompts, applying colloquial register contractions, navigating the
formal/informal register split, and working through translation challenges.

