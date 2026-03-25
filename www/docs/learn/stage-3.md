# Stage 3 — Grammar and notation

Particles and notation marks are introduced together because you encounter them
together in every real Tonesu sentence. `la-mi  pa-re-mu  lo-de  ka-se  ta-ti-de`
has five particles and encodes agent, location, patient, action, and time — all in
one line. You've been reading sentences like this since Stage 0. Now the grammar
behind them becomes explicit.

---

## Cluster 1 — The particle system

Every participant in a Tonesu sentence carries a particle that declares its role.
Word order carries no grammatical weight — the particle does the work.

| Particle | Role |
|----------|------|
| `la-` | perspective anchor — agent in action clauses; stance-holder in epistemic clauses |
| `lo-` | patient — the entity acted on, or in a state |
| `ro-` | instrument — the means or tool |
| `pa-` | location — where the action takes place |
| `ta-` | time reference — when |
| `ka-` | action marker — the action or process |
| `ne-` | relation / recipient — who receives, or the relational partner |
| `na-` | proper name marker — signals an identifier, not a compositional noun |

Particles prefix directly to what they mark. A full corpus sentence, role by role:

```
la-mi    pa-re-mu    lo-de    ka-se    ta-ti-de
  I      gen-room    decay    examine  past
```

*I examined the decay in the generator room — past.*  (C001 A1)

The order above is: agent — location — patient — action — time. Any order is valid.
`lo-de  la-mi  ta-ti-de  ka-se  pa-re-mu` says exactly the same thing.

**Most particles are transparent.** `pa-` (location) derives from `pa` (space/place).
`ka-` (action) derives from `ka` (intentional action). `ne-` (recipient) derives from
`ne` (relation). You already know these roots from Stage 1 — particles are the same
semantic atoms pressed into grammatical service.

---

!!! question "Exercise 1 — Which particle marks the patient?"
    In `la-mi  pa-re-mu  ___-de  ka-se  ta-ti-de`, which particle marks the decay —
    the thing being examined?

    <div class="tn-learn-picker"
         data-template="la-mi  pa-re-mu  ___-de  ka-se  ta-ti-de"
         data-answer="lo"
         data-mode="form"
         data-ok="lo — the patient marker. lo-de = the decay, the entity acted on ✓"
         data-nok="That particle has a different role. lo- marks the entity acted on."
         data-items='[{"form":"la","gloss":"agent / perspective"},{"form":"lo","gloss":"patient / acted-on"},{"form":"pa","gloss":"location"},{"form":"ta","gloss":"time"},{"form":"ka","gloss":"action"}]'>
    </div>

??? success "Explanation"
    `lo-` marks the patient — what the action is directed at. `lo-de` = the decay, as
    the entity being examined. `la-mi` = I (as agent). `pa-re-mu` = at the generator
    (location). `ka-se` = examine (action). `ta-ti-de` = past time.

    Five particles. One sentence. Unambiguous parse regardless of which order they
    appear in.

---

## Cluster 2 — Predication types

Three distinct ways to attribute a quality to an entity. They are not interchangeable.

### Type 1 — `lo-X  Q` — contingent state

`lo-{entity}  {quality}` = "X is in state Q"

The entity is the patient — it holds or enters a state. The claim is contingent:
the state can change.

```
lo-si-mu  ru         →  The relay is stable.                   (C002 A3)
lo-pa     ha-vo      →  The room is warm.                      (S033)
lo-li     vo         →  The person is (socially) valued.       (S163)
```

### Type 2 — `la-X  Q` — structural property

`la-{entity}  {quality}` = "X has quality Q"

The entity is the agent/anchor — the structural bearer of the quality. The claim is
intrinsic.

```
la-to-su-mu  vo      →  The archive has value.                 (S030)
la-li        vo      →  A person has worth.                    (S162)
```

### Type 3 — `ka  Q` — manner adverbial

`ka  {quality}` = "the action is performed with Q"

```
la-li-pu   ka  ru    →  The collective acts with unity.        (S031)
```

### The critical minimal pair

Same noun, same quality, different particle, different ontological claim:

```
la-li  vo     →  A person has worth.       (S162) — intrinsic; cannot be revoked
lo-li  vo     →  The person is valued.     (S163) — contingent social esteem; can reverse
```

`la-li vo` makes worth structural — a property of personhood. `lo-li vo` makes it a
current social state. The language requires you to decide which claim you are making.

---

!!! question "Exercise 2 — Intrinsic or contingent?"
    The claim: *a person has worth — structurally, not revocably by social consensus.*
    Fill in the blank: `___-li  vo`

    <div class="tn-learn-picker"
         data-template="___-li  vo"
         data-answer="la"
         data-mode="form"
         data-ok="la — structural bearer. la-li vo: worth is a structural property of personhood ✓"
         data-nok="lo- makes it contingent: lo-li vo = the person is currently socially valued. For the intrinsic claim, use la-."
         data-items='[{"form":"la","gloss":"structural bearer — intrinsic property"},{"form":"lo","gloss":"patient — contingent state"}]'>
    </div>

??? success "Explanation"
    The choice is an ontological commitment, not a stylistic one.
    `la-li vo` = worth is a structural feature of personhood.
    `lo-li vo` = this person is currently in a valued-state.

    The same distinction applies to any quality: `la-si-mu  no-ru` (the relay
    structurally lacks coherence — by design) vs `lo-si-mu  no-ru` (the relay is
    currently in an incoherent state — it might recover).

---

## Cluster 3 — Questions and negation

### Questions

All questions use `to-si` (W026 — knowledge-seeking signal). Placement determines
the type.

**Content questions** — `to-si` in the argument slot

Put `to-si` where the unknown belongs. The proposition has a gap; `to-si` fills it.

```
de  vo  to-si?              →  What quality of damage?               (C001 B1)
la-ze  ki  pa-to-si?        →  Where did they go?
```

**Polar questions** — `to-si` fronted, before the proposition

```
to-si — lo-pa-ra  be-now        →  Is the field active?              (C006 A1)
to-si — la-tu  ki  pa-li-pu?    →  Are you approaching the gathering?  (C003 A1)
```

**Casual register:** `ku?` clause-final

In informal speech, `ku?` follows the complete proposition instead:

```
la-tu  ki  pa-li-pu  ku?    →  (casual) Are you heading there?
```

**Answers to polar questions:**

| Form | Meaning |
|------|---------|
| `ru` | Yes — that coheres |
| `ru — {proposition}` | Yes + elaboration |
| `no` | No — that does not hold |
| `no — {proposition}` | No + elaboration |

`ru` and `no` are the primitive roots for unity and negation, used sentence-initially
as discourse responses. Their meaning is transparent — `ru` = it coheres; `no` = it
is absent.

### Negation

Four scope levels:

| Level | Form | Example |
|-------|------|---------|
| Root prefix | `no-X` | `no-de` (intact), `no-ha` (cold) |
| Compound prefix | `no-{compound}` | `no-ka-ki` (don't go) |
| Clause negation | `no {ka-clause}` | `no {ka-se}` (cannot be examined) |
| Contrast coordinator | `A  no  B` | `lo-to-re-su be no lo-wi-to` (followed doctrine, not the plan) |

The contrast coordinator marks the first constituent as what actually occurred and the
second as the rejected alternative. Both must be the same grammatical type.

---

!!! question "Exercise 3 — Content or polar?"
    Which form asks "what quality of damage?" — seeking the unknown argument, not
    the truth value?

    <div class="tn-learn-picker"
         data-template="___"
         data-answer="de  vo  to-si?"
         data-mode="form"
         data-ok="Correct — to-si in the argument slot = content question: asking for the unknown value ✓"
         data-nok="That form fronts to-si before the proposition — that asks whether the proposition is true (polar)."
         data-items='[{"form":"de  vo  to-si?","gloss":"to-si in argument slot"},{"form":"to-si — de  vo?","gloss":"to-si fronted"}]'>
    </div>

??? success "Explanation"
    Position is everything. `to-si` *inside* the proposition = content question (unknown
    argument). `to-si` *before* the proposition = polar question (unknown truth value).

    `de vo to-si?` fills the quality slot with `to-si`: "damage of what quality?"
    The fronted form `to-si — de vo?` asks: "is it the case that the damage has this
    quality?" — seeking a yes/no.

---

## Cluster 4 — The epistemic frame and notation

### Personal epistemic modality

The epistemic frame places a confidence level between speaker and embedded proposition:

```
la-{speaker}  {level}  {embedded proposition}
```

| Level | Root | Meaning | Entailment |
|-------|------|---------|------------|
| Perceptual floor | `se` | I have signal / I perceive | — |
| Hypothesis | `si` | I am assessing / I hypothesize | entails `se` |
| Established | `to` | I hold as known / I am certain | entails `si`, `se` |

The floor denial is the strongest claim: `no-se` (no perceptual basis) forecloses
everything above it. Denying only the ceiling (`no-to`) is consistent with still
having a hypothesis or a perceptual signal.

Corpus cluster:

```
la-mi  si  {lo-de  no-ru}               →  I hypothesize the decay is unstable.  (C001 A3)
la-mi  to  {lo-ze  se}                  →  I hold as established: that signal is perceptual.  (C005 B1)
la-mi  to  {la-tu  no-se  lo-ne-ra}     →  I hold as established: you have no perceptual
                                            basis for the resonance.  (C007 A5)
```

The last example is a **nested epistemic frame**: the outer `la-mi to` certifies the
inner `la-tu no-se {…}` as an established proposition. No additional grammar required —
the inner frame is itself a well-formed clause in the embedded slot.

### `go` — causal frame

`go {premise}, result` asserts a *necessary connection* — the premise produces the
result.

```
go {lo-de  no-ru},  la-mi  ka-de-be     →  Because the decay is unstable, I repair it.
```

### `;` — sequential connector

`;` connects two clauses as a sequence without asserting the mechanism. `A ; B` = "A,
and then B" — constant conjunction, not necessary connection. This is Hume's
distinction: `go` = necessary connection; `;` = constant conjunction.

```
la-mi  ka-se  ta-ti-de ;  lo-de  no-ru  →  I examined it yesterday; the decay is unstable.
```

Use `go` when the mechanism is the point. Use `;` when the connection is observed but
the mechanism is not being asserted.

### `/` — parallel partition

`/` marks a formally paired bi-clausal structure. The relationship between the flanking
clauses (antithetical, complementary, causal) is supplied by content, not the mark.

```
la-li  vo  /  lo-li  no-vo     →  A person has worth / the person is treated as worthless.
```

### Notation marks

| Mark | Name | Read as | Spoken form |
|------|------|---------|-------------|
| `(clause)` | evidential frame | reportedly / unattributed | `vund … vunds` |
| `[text]` | aside frame | annotation — removable | `zeld … zelds` |
| `~X` | approximation | approximately X | `ven` |
| `—` | prosodic suspension | held in suspension | `el` |
| `""` | quotation / mention | direct speech; use-mention | `sild … silds` |
| `: (clause)` | topic frame | as for {topic}, — | `helm` |

**Evidential frame `()`:** marks content as reported or unattributed. Use when citing
hearsay, a contested claim, or inference not directly asserted by the speaker.
`(la-Yeshua  ra-no-fe)` = it is reportedly said that Yeshua is all-powerful.

**`~` approximation:** pre-positional hedge. `~to-su` = approximately a knowledge
system. `~tonesu` = approximately truth = working conjecture.

**Aside frame `[]`:** annotation that does not alter truth conditions. Removing every
`[…]` must leave the core argument unchanged — this is a self-policing constraint.

### Discourse markers

| Marker | Position | Function |
|--------|----------|----------|
| `he` | before name | vocative: `he na-re-ka!` = Re'ka! |
| `ya,` | clause-initial | attention: attend to what follows |
| `ke,` | clause-initial | pivot: prior claim denied (contextually), new claim advancing |
| `ke!` | clause-initial | heated pivot |
| `ru-fe,` | clause-initial | exclusive scope: *only / solely:* {clause} |

`ya` and `ke` can stack: `ya, ke, {clause}` = now pay attention — the prior position
was wrong and here is the correction.

---

!!! question "Exercise 4 — Epistemic level"
    Complete: `la-mi  ___  {lo-de  ru}` — I hold it as *established* that the decay
    is stable.

    <div class="tn-learn-picker"
         data-template="la-mi  ___  {lo-de  ru}"
         data-answer="to"
         data-mode="form"
         data-ok="to — established knowledge. la-mi to {lo-de ru}: I hold as certain that the decay is stable ✓"
         data-nok="Check the ladder: se = perceptual floor, si = hypothesis, to = established knowledge."
         data-items='[{"form":"se","gloss":"perceptual floor — I have signal"},{"form":"si","gloss":"hypothesis — I am assessing"},{"form":"to","gloss":"established — I hold as known"}]'>
    </div>

??? success "Explanation"
    `to` is the ceiling: the speaker asserts this as settled knowledge, not perception
    or hypothesis.

    The embedded proposition `{lo-de  ru}` is Type 1 predication: the decay is in a
    stable state. The full sentence `la-mi  to  {lo-de  ru}` = I [as agent], hold-as-
    established, [the-decay is-stable].

---

## Grammar introduced in this stage

| Form | Type | Meaning |
|------|------|---------|
| `la-` | particle | perspective anchor / agent |
| `lo-` | particle | patient |
| `ro-` | particle | instrument |
| `pa-` | particle | location |
| `ta-` | particle | time reference |
| `ka-` | particle | action marker |
| `ne-` | particle | relation / recipient |
| `na-` | particle | proper name marker |
| `go {…}, …` | frame | causal frame — necessary connection |
| `;` | connector | sequential connector — sequence only |
| `/` | marker | parallel partition |
| `he` | particle | vocative |
| `ya,` | marker | attention signal |
| `ke,` / `ke!` | marker | pivot |
| `ru-fe,` | marker | exclusive scope |
| `(…)` | notation | evidential frame — reported / unattributed |
| `[…]` | notation | aside / annotation |
| `~` / `ven` | notation | approximation |
| `—` / `el` | notation | prosodic suspension |

---

## Next

[Stage 4 — Derived vocabulary](stage-4.md) works through the derived registry by
root family. You'll parse 30–40 registered forms from their roots, see the operator
patterns from Stage 2 extended to new domains, and drill longer compounds including
four-root chains.
