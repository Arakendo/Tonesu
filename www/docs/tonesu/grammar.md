# Grammar

Tonesu sentences are built from **role-marked phrases** rather than strict word order. Each participant wears a particle prefix that tells you its role — so word order can vary freely for emphasis without ambiguity.

> **Notation:** Written Tonesu has no hyphens. `latoli` is the word; `la-toli` is the analytic parse showing particle + root. Analytic forms appear in breakdowns only.

---

## Core sentence frame

```
la-{agent}   {verb}   lo-{patient}
```

**Default order: Agent – Verb – Patient (AVP/SOV)**

```
latoli  kaseka  lotosu
```
*The scholar examines the theory.*  
*(parse: la-toli · ka-seka · lo-tosu)*

---

## Particles

Short, phonologically distinct syllables. They never merge with roots ambiguously.

| Particle | Role | Notes |
|----------|------|-------|
| `la-` | agent / perspective anchor | who acts; also the stance-holder in epistemic clauses |
| `lo-` | patient | who or what is acted upon |
| `ro-` | instrument | the tool or means |
| `pa-` | location | where the action occurs |
| `ne` | relation / recipient | who receives; also the copula for relational states |
| `ta` | time reference | temporal anchor |
| `ka` | action marker | marks the verb/predicate |
| `na` | proper name marker | signals an identifier, not a compound noun |
| `da-` | domain marker | marks a conceptual domain reference |
| `go` | causal frame | "because of / from" |
| `du` | result frame | "resulting in / so that" |

Where a particle overlaps with a primitive root (`pa`, `ne`, `ka`, `go`, `du`, `no`) the overlap is always **transparent** — the particle meaning is derived from the root meaning.

---

## Modifiers precede their head

Modifiers always come **before** the thing they modify — no exceptions.

```
nuno toli      →  many scholars        (quantity before noun)
voki           →  act with care        (quality-motion compound)
```

---

## Predication: `la-X Q` vs `lo-X Q`

This is one of the most important distinctions in Tonesu. Both forms predicate a quality of an entity — but they make different claims.

**`lo-X Q` — contingent state** (X is currently in state Q; this can change)

```
loli   vo     →  The person is valued.           (social esteem — contingent)
lopa   havo   →  The room is warm.               (current temperature)
```

**`la-X Q` — intrinsic property** (X constitutively possesses quality Q)

```
lali   vo     →  A person has worth.             (inherent; cannot be revoked)
larakimu  hafe  →  The engine has a thermal limit.  (structural property)
```

**Decision rule:** Can X *exit* this state? → use `lo`. Is Q part of X's constitution? → use `la`.

The minimal pair — same noun, same quality, different claim:

```
lali  vo   →  a person has worth          (intrinsic — la)
loli  vo   →  the person is valued        (contingent — lo)
```

---

## Causal frame: `go` and `du`

Use `go` to state a reason and `du` to state a result:

```
go {lami  kasikipast}  du {layu  to  lofesi}
```
*Because I sent the signal, they know the warning.*

---

## Negation

`no-` prefixes any root or compound to negate it. Scope covers the entire base form.

```
node      →  noha       →  noru       →  nonefe
(no-de)      (no-ha)       (no-ru)       (no-ne-fe)
non-decay    cold          incoherent    free-standing
```

`no` also acts as a **contrast coordinator** between two parallel constituents:

```
lali  vo  no  laze    →  the person has worth, not ze
```

And as a **sentence-initial minimal negative** in response to a polar question.

---

## Pronouns

| Form | Meaning |
|------|---------|
| `mi` | I / me (speaker) |
| `tu` | you (addressee) |
| `ze` | he / she / they / it (third person, any referent) |
| `yu` | they / we (group) |

`ze` is a **unified anaphora** — it refers to the most salient discourse entity regardless of type (person, proposition, machine). The predicate's semantics usually makes the referent type clear.

---

## Questions

`tosi` (knowledge-seeking signal) marks a question. Its position determines the type:

**Polar question** — `tosi` at the end:

```
latoli  kaseka  lotosu  tosi
```
*Does the scholar examine the theory?*

**Content question (WH)** — `tosi` replaces the unknown element:

```
latoli  kaseka  tosi
```
*What does the scholar examine?*

---

## Epistemic framing

Tonesu has explicit grammar for marking the *source and confidence* of a claim.

| Form | Meaning |
|------|---------|
| `lami  to  {prop}` | I know/believe that… (speaker's calibrated confidence) |
| `lasource  si  {prop}` | source signals/outputs that… (attributed claim) |
| `(prop)` | reportedly / inferred — not directly asserted |
| `~(prop)` | approximately reportedly… |

---

## Copula

There is no "to be" in Tonesu. Use predication directly:

```
lalibe  ne  zode
```
*The child is tired.* (lit. the-child [relation] organism-decay)  
*(parse: la-libe · ne · zo-de)*

For strict definitional identity: `helms` (`X helms Y` = X is by definition Y).  
For functional equivalence: `helm` (`X helm Y` = X is understood as Y).

---

## Special sentence particles

| Particle | Use | Notes |
|----------|-----|-------|
| `he` | vocative | `he naX!` — direct address |
| `ya` | attention signal | `ya, [clause]` — attend to this |
| `rufe` | exclusive scope | `rufe, [clause]` — only / solely this |
| `ke` | pivot | `ke, [clause]` — advancing a claim after implicit denial |

---

## Purpose frame

`wi` attaches a purpose or goal clause:

```
layu  katoki  wi [katosuki]
```
*They study in order to understand.*

---

## A complete example

```
laze  losi  kasikipast  wi [kafesi  neyu]
```
*She sent the message to warn them.*

| Token | Parse | Role |
|-------|-------|------|
| `laze` | la-ze | agent: she |
| `losi` | lo-si | patient: the message |
| `kasikipast` | ka-si-ki (past) | action: sent |
| `wi [kafesi neyu]` | wi [ka-fe-si · ne-yu] | purpose: to warn them |

Because every participant is role-marked, word order is flexible — the particles carry the meaning, not the position. Default is Agent – Verb – Patient; topic-fronting is free.
