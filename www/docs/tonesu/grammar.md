# Grammar

Tonesu sentences are built from **role-marked phrases** rather than strict word order. Each participant in a sentence wears a particle prefix that tells you its role.

> **Notation in this page:** Written Tonesu has no hyphens. `latoli` is the written form; `la-toli` is the analytic breakdown showing particle + word. Analytic forms appear in parse labels to make structure visible.

---

## The core sentence frame

```
la-{agent}   {verb}   lo-{patient}
```

| Slot | Particle | Role |
|------|----------|------|
| `la-` | agent | who acts, or whose perspective the sentence is from |
| `lo-` | patient | who or what is acted upon |
| `ka` | action marker | marks the verb phrase |

**Example:**
```
latoli  kaseka  lotosu
```
*The scholar examines the theory.*
*(parse: la-toli  ka-seka  lo-tosu)*

---

## All particles

| Particle | Role | Notes |
|----------|------|-------|
| `la-` | agent / perspective anchor | initiator, stance-holder, relational anchor |
| `lo-` | patient | the affected entity |
| `ka` | action marker | marks the verb/action |
| `ne` | relation / recipient | who receives; also the copula for relational states |
| `go` | cause / origin | "because of", "from" |
| `du` | result / effect | "resulting in", "so that" |
| `ro` | instrument | the tool or means |
| `pa` | location | where the action occurs |
| `ta` | time | temporal anchor |
| `na` | proper name marker | signals a name, not a compound noun |

---

## Copula

There is no "is". Instead, Tonesu uses **`ne`** to connect a subject to a property or relation:

```
lalibe  ne  zode
```
*The child is tired.* (lit. the-child [relation] organism-decay)
*(parse: la-libe  ne  zo-de)*

---

## Modifiers precede their head

A modifier always comes **before** the thing it modifies — no exceptions.

```
nuno toli         →  many scholars        (quantity modifier precedes noun)
kaseka-past       →  examined             (tense marker precedes verb root)
```

---

## Causal frame

Use `go` and `du` to state causes and results:

```
go {lami  kasikipast}  du {layu  to  lofesi}
```
*Because I sent the signal, they know the warning.*

---

## Pronouns

| Form | Meaning |
|------|---------|
| `mi` | I / me (speaker) |
| `tu` | you (addressee) |
| `ze` | he / she / they (third person, singular) |
| `yu` | they (third person, plural) |

---

## Tense and aspect

Tense is optional and marked on the verb with a suffix:

| Suffix | Meaning |
|--------|---------|
| `-past` | completed / past |
| `-now` | ongoing / present |
| (none) | context-determined or timeless |

---

## Predication: `la-X` vs `lo-X`

This is one of the most important distinctions in Tonesu. There are two ways to predicate a quality of an entity, and they mean different things.

**`loli  Q` — contingent state** (X is currently in state Q; this can change)

```
loli   vo    →  The person is valued.    (social esteem — contingent)
lopa   havo  →  The room is warm.        (current thermal state)
```

**`lali  Q` — intrinsic property** (X constitutively has quality Q)

```
lali         vo    →  A person has worth.      (inherent; cannot be revoked)
larakimu     hafe  →  The engine is at a thermal limit.  (structural property)
```

The minimal pair: same noun, same quality, different claim.

```
lali  vo   →  a person has worth          (inherent, intrinsic)
loli  vo   →  the person is valued        (contingent social esteem)
```

Decision rule: can X *exit* this state? → use `lo`. Is Q part of X's constitution? → use `la`.

---

## Negation

Negation uses the single root `no` (negation/absence) as a prefix:

```
node      (no-de)     →  non-decay  =  preservation
nofe      (no-fe)     →  below threshold
noru      (no-ru)     →  lacking unity, incoherent
nonefe    (no-ne-fe)  →  no dependency, free-standing
```

`no-` scopes over the entire following base, including multi-root compounds.

---

## Purpose frame

Use `wi` to attach a purpose or goal clause:

```
layu  katoki  wi [katosuki]
```
*They study in order to comprehend.*

---

## A fuller example

```
laze  losi  kasikipast  wi [kafesi  neyu]
```
*She sent the message to warn them.*

Breaking it down:

- `laze` — she (agent)  *(parse: la-ze)*
- `losi` — the message (patient)  *(parse: lo-si)*
- `kasikipast` — sent (action, past)  *(parse: ka-sika-past)*
- `wi [...]` — with purpose: to warn them
  - `kafesi` — to warn  *(parse: ka-fesi)*
  - `neyu` — them (recipient)  *(parse: ne-yu)*

---

## A note on word order

Because every participant is role-marked, word order in Tonesu is flexible — the role markers carry the meaning, not the position. The default order is **agent – verb – patient**, but emphasis or topic-fronting can rearrange this freely without ambiguity.
