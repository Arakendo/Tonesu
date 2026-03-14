# Grammar

## Status: Draft

Covers sentence structure, particles, and clause-level syntax. For affixes, tense/aspect, derivation, and morphological categories (number, gender, possession), see spec/morphology.md.

---

## Core Principles

- Explicit role marking: relationships stated, not implied by word order alone
- Consistent constituent order: modifiers always pre-pose what they modify
- Minimal obligatory structures: particles appear only when needed for clarity

---

## Sentence Order

**Default: Agent – Object – Action (SOV)**

```
la-engineer  lo-machine  ka-build
```
*The engineer builds the machine.*

Word order is consistent to aid parsing. Modifiers attach before the element they modify.

---

## Grammatical Particles

Short, phonetically distinct syllables. Never merge with roots ambiguously.

| Particle | Role | Usage |
|----------|------|-------|
| `la` | perspective anchor | marks the perspective-privileged participant: initiator in action clauses, stance-holder in epistemic clauses, relational anchor in stative predicates; commonly glossed "agent" in action contexts |
| `lo` | patient marker | marks the affected object |
| `ro` | instrument marker | marks the tool or cause |
| `pa` | location marker | where the action occurs |
| `ne` | recipient/relation | who receives or to whom |
| `ta` | time reference | temporal anchor |
| `ka` | action marker | marks the verb/action |
| `na` | proper name marker | signals identifier, not compositional noun |
| `da` | domain marker | signals a conceptual domain reference |

*Particles are pre-posed (come before the element they mark).*

---

## Particle–Root Overlap Policy

Any grammatical function word (particle, frame word, negation prefix, pronoun, derivational suffix, or quantity prefix) **may share phonetic form with a primitive root only if its grammatical function is semantically derived from that root's meaning.** Such overlaps are intentional and transparent — a speaker who knows the root can infer the function word's role.

Non-transparent collisions are **not permitted**: if the function word's meaning is unrelated to the root, one must be renamed.

### Full Function-Word Audit

**Core particles**

| Form | Function | Root overlap | Relationship | Status |
|------|----------|-------------|--------------|--------|
| `la` | agent marker | — | no root `la` | Clean |
| `lo` | patient marker | — | no root `lo` | Clean |
| `ro` | instrument marker | — | no root `ro` | Clean |
| `pa` | location marker | `pa` (place/space) | location from place root | Transparent ✓ |
| `ne` | relation/recipient marker | `ne` (relation) | relation marker from relation root | Transparent ✓ |
| `ta` | time reference | — | no root `ta` | Clean |
| `ka` | action marker | `ka` (action) | action marker from action root | Transparent ✓ |
| `na` | proper name marker | — | no root `na` | Clean |
| `da` | domain marker | — | no root `da` | Clean |

**Frame words and negation**

| Form | Function | Root overlap | Relationship | Status |
|------|----------|-------------|--------------|--------|
| `go` | causal frame | `go` (cause/origin) | causal marker from cause root | Transparent ✓ |
| `du` | result frame | `du` (result/effect) | result marker from result root | Transparent ✓ |
| `no` | negation prefix | `no` (negation/absence) | negation function from negation root | Transparent ✓ |

**Quantity prefixes** (see spec/morphology.md)

| Form | Function | Root overlap | Relationship | Status |
|------|----------|-------------|--------------|--------|
| `nu-` | indefinite quantity | `nu` (quantity/number) | quantity prefix from quantity root | Transparent ✓ |
| `ru-` | singular | `ru` (unity/singularity) | singular from unity root | Transparent ✓ |
| `pu-` | plural | `pu` (plurality) | plural from plurality root | Transparent ✓ |

**Derivational suffixes** (see spec/morphology.md)

| Form | Function | Root overlap | Relationship | Status |
|------|----------|-------------|--------------|--------|
| `-li` | agent suffix | `li` (social agent) | agent function from agent root | Transparent ✓ |
| `-mu` | device suffix | `mu` (artifact) | device from artifact root | Transparent ✓ |
| `-pa` | location suffix | `pa` (place) | location from place root | Transparent ✓ |
| `-su` | result/product suffix | `su` (structure) | result = the structure produced | Transparent ✓ |
| `-to` | abstract nominalizer | `to` (concept/pattern) | abstraction from concept root | Transparent ✓ |
| `-ge` | quality/property suffix | none | no root `ge` exists — collision-free | **Resolved** (renamed from `-se`, S049C) |
| `-ki` | inchoative / verbal noun | `ki` (motion) | entering-state from motion root | Transparent ✓ |

**Pronouns**

| Form | Function | Root overlap | Relationship | Status |
|------|----------|-------------|--------------|--------|
| `mi` | 1st person (I) | — | no root `mi` | Clean |
| `tu` | 2nd person (you) | — | no root `tu` | Clean |
| `ze` | 3rd person (other/they) | — | no root `ze` | Clean |
| `yu` | group (we/they) | — | no root `yu` | Clean |

The full pronoun set is collision-free. Former forms `se` (3rd person) and `wi` (group) were renamed: `se` collided non-transparently with root `se` (perception); `wi` collided non-transparently with root `wi` (will/intention) and also blocked adoption of `wi` as a purpose-frame particle.

---

Example:
```
la researcher  lo knowledge-system  ka improve  ta future
```
*The researcher will improve the knowledge system.*

---

## Modifiers

Qualifiers (adjective/adverb equivalent) always pre-pose the modified element.

```
fast-run
heavy-machine
efficient-computation
```

Same rule applies whether modifying a noun or a verb. No separate adjective/adverb class.

---

## Concept Nesting

No dedicated grouping particle is needed. NP scope and structure are handled by four existing tools:

1. **Role-marker scoping** — role-markers (`la-`, `lo-`, `ro-`, `ne-`) scope over the complete following NP as a unit.
2. **Apostrophe `'`** — marks the left boundary of a subcompound within a compound word. See spec/word-formation.md § Compound Grouping Marker.
3. **`na` particle** — partitions kind-term from identifier in named NPs: `[kind  na  identifier]`. See spec/naming.md.
4. **Clause-frame markers** (`go`, `wi`, `ta`, `no-go`, `to-go`) — establish clause-level boundaries; the outer predicate closes the frame.

Bracket notation `[...]` in corpus glosses is analytic notation only; it has no spoken or written equivalent.

---

## Predication Strategies

There are three ways to predicate a quality or state of an entity. They are grammatically
distinct and semantically non-equivalent.

### Type 1 — Patientive state: `lo-X  Q`

`lo-[entity]  [quality]` = "X is in state Q"

The entity occupies the patient slot (`lo`) and is in the named state as a current
condition. The claim is contingent — the state can change.

```
lo-si-mu  ru        →  The relay is stable.            (C002 A3)
lo-pa     ha-vo     →  The room is warm.               (S033)
lo-li     vo        →  The person is socially valued.  (S163)
```

### Type 2 — Attributive property: `la-X  Q`

`la-[entity]  [quality]` = "X has quality Q"

The entity occupies the agent slot (`la`) and is the structural bearer of the quality.
The claim is intrinsic or structural — a property of the entity's constitution.

```
la-to-su-mu  vo     →  The archive has value.              (S030)
la-ra-ki-mu  ha-fe  →  The engine is at a thermal limit.   (S034)
la-li        vo     →  A person has worth.                 (S162)
```

### Type 3 — Manner adverbial: `ka  Q`

`ka  [quality]` = "the action is performed with Q"

The quality follows the action marker `ka` and characterizes *how* the action is
performed. Q modifies the action, not the agent.

```
la-li-pu     ka  ru  →  The collective acts with unity.  (S031)
la-su-mu-li  ka  vo  →  The engineer acts with care.     (S164)
```

### Distinguishing `lo-X  Q` from `la-X  Q`

Both forms predicate a quality of an entity but make different claims. They cannot
substitute freely.

| | `lo-X  Q` | `la-X  Q` |
|---|---|---|
| Slot | patient — X occupies or receives Q | agent — X holds or possesses Q |
| Claim type | contingent state (can change) | structural / intrinsic property |
| Decision rule | can X exit this state? → use `lo` | is Q part of X's constitution? → use `la` |

**Minimal pair (S162 vs S163):** Same noun (`li` = person), same quality (`vo` = value):
- `la-li  vo` = "a person has worth" — intrinsic; cannot be revoked by social consensus
- `lo-li  vo` = "the person is valued" — contingent social esteem; can change

### Compound quality predicates

Compound predicates (`ha-vo`, `ha-fe`, `no-ru`, etc.) work in all three positions
without modification.

```
lo-pa        ha-vo   →  The room is warm.                  (Type 1, S033)
la-ra-ki-mu  ha-fe   →  The engine has a thermal limit.    (Type 2, S034)
la-si-mu     no-ru   →  The document lacks coherence.      (Type 2 negated, S165)
```

`no-` applied to a quality root negates the predicate within whichever frame it appears in.

### Summary

| Pattern | Example | Reading |
|---------|---------|---------|
| `lo-X  Q` | `lo-li  vo` | X is in state Q — patient slot, contingent |
| `la-X  Q` | `la-li  vo` | X has quality Q — agent slot, structural/intrinsic |
| `ka  Q` | `la-su-mu-li  ka  vo` | action performed with Q — manner |

---

## Negation

Negation in Tonesu uses a single root `no` (negation/absence) operating at three scope levels. For derivational detail on the prefix, see spec/morphology.md § Productive Prefixes.

### Level 1 — Root and compound prefix

`no-` prefixes a root or compound predicate to produce its absence or non-attainment. Scope is the **entire base form**, including multi-root compounds.

```
no-de        →  preservation (non-decay)
no-fe        →  below threshold (non-boundary)
no-ha        →  cold (non-thermal)
no-ne-fe     →  non-dependency (does not require)
```

### Level 2 — Action negation

`no-` prefixes a `ka`-compound in the predicate slot to negate a directed action. Standard form for imperative negation:

```
no-ka-ki  lo-mu    →  Don't move the machine.
```

### Level 3 — Clause negation

`no [ka-clause]` fronts an entire action clause, negating the action frame as a whole.
Attested: S036 (`no [ka-se]` = "cannot be consumed"), S172 (`lo-si-de  no [ka-be]`
= "the signal record cannot be altered").

### Level 4 — Intra-clause contrast coordinator

`no` appears between two grammatically parallel constituents in the same clause — both patients, both agents, or both predicate forms — to mark the first as the actual case and the second as the rejected alternative. The predicate is unaffected; only the second constituent is negated.

```
lo-to-re-su  be  no  lo-wi-to    →  followed the doctrine, not the plan  (S090)
la-mu  lo-si  se  no  lo-to      →  machine perceived the signal, not the pattern  (S190)
```

Structure: `[established constituent]  no  [rejected alternative]`. Both constituents must be of the same grammatical type. The `no` is not prefixed to the following constituent — it floats between the two, readable as the `no`-root in its absence/negation meaning: "the second item is absent from this event."

**Sentence-initial `no`** as a minimal negative response to a polar question (`no` / `no — [elaboration]`, C006 B3) is a related discourse-level use with the same root semantics. Documented in § Questions.

### Summary

| Level | Form | Status |
|-------|------|--------|
| Root prefix | `no-X` | confirmed |
| Compound prefix | `no-[compound]` | confirmed (S063) |
| Action negation | `no-ka-X` | confirmed |
| Clause negation | `no [ka-clause]` | confirmed (S036, S172) |
| Contrast coordinator | `A  no  B` | confirmed (S090, S190) |
| Sentence-initial minimal negative | `no` / `no — [prop]` | confirmed (C006 B3); see § Questions |

---

## Questions

Tonesu encodes all questions using `to-si` (W026, knowledge-seeking signal). The same
particle serves both **content questions** (WH-questions) and **polar questions**
(yes/no questions). The type is determined by the position of `to-si` relative to the
proposition.

### Content Questions

`to-si` occupies the **argument slot** of the unknown constituent, inside the proposition.
The proposition has a syntactic gap; `to-si` fills it.

```
de  vo  to-si?
```
*What kind / quality of damage?*  (`to-si` in the quality-qualifier slot, C001 B1)

```
lo-pa-ra  ne-ra  vo  to-si?
```
*What is the character of the field's resonance?*  (`to-si` in the qualifier slot; C006 A2)

General pattern:

```
[entity]  [relation]  [dimension]  to-si?
```

`to-si?` carries a terminal rise marker (`?`) in written gloss, matching its
function as the end of an incomplete proposition seeking the missing argument.

### Polar Questions

`to-si` is **fronted** before the proposition, separated by a dash as an inquiry-frame
boundary. The proposition is structurally complete (missing arguments are recovered by
discourse context, not unknown). The unknown is the **truth value** of the proposition.

```
to-si — lo-pa-ra  be-now
```
*Is the field active?*  (C006 A1)

```
to-si — la-tu  ki  pa-li-pu  ta-ti-be
```
*Are you approaching the congregation?*  (C003 A1)

General pattern:

```
to-si — [complete proposition]
```

The dash (`—`) marks the boundary between the inquiry frame and the proposition whose
truth value is sought. It may be absent in rapid speech register, but is preserved in
formal gloss.

### Summary Table

| Question type | `to-si` position | What is unknown |
|---------------|-----------------|-----------------|
| Content | **Inside** proposition, in argument slot | The argument in that slot |
| Polar | **Outside** proposition (fronted, pre-dash) | The truth value |

### The Ambiguous Case

When `to-si` is fronted before a proposition whose patient is **absent** (dropped by
context), two readings are available: polar (truth-value unknown) and content (patient
argument unknown). The positional rule resolves this: **fronted = polar**. A content
reading requires `to-si` in argument position (`to-si?` at the end).

```
to-si — la-mi  ne-ra-ki
```
*Am I attuning?*  — fronted `to-si` = polar. The patient (what A would attune to)
is absent but contextually recoverable; the question is whether attuning is occurring.
Content reading (`what do I attune to?`) would require: `la-mi  ne-ra-ki  to-si?`

Ambiguous fringe cases are dissolved by **response completeness**: a full answer
(`ru — ne-ra-ki  lo-pa-ra`) satisfies both the polar reading (via `ru`) and the
content reading (via specifying the patient). The language does not require the question
type to be syntactically unambiguous because a complete answer covers both.

### Answers to Polar Questions

Polar questions receive minimal or full responses:

| Answer type | Form | Meaning |
|-------------|------|---------|
| Minimal affirmative | `ru` | "[that] coheres" — yes (C006 B1) |
| Full affirmative | `ru — [proposition]` | yes + elaboration (C006 B1, B4) |
| Minimal negative | `no` | "[that] does not hold" — no (C006 B3) |
| Full negative | `no — [proposition]` | no + elaboration (C006 B3) |
| Echo confirmation | restate proposition from speaker's perspective | yes, with expressed agreement (C003 B1) |
| Action-commit | `ka-[verb]` | I will/am doing it (C001 B3) |

`ru` and `no` are not new particles — they are the primitives for unity/coherence and
negation/absence used sentence-initially as affirmative and negative discourse responses.
Their use here is semantically transparent and does not require special lexical status.

---

## Epistemic Modality

Tonesu encodes speaker-level epistemic commitment through an **utterance-level modal
frame** placed at the beginning of a clause:

```
la-[speaker]  [epistemic-root]  [embedded proposition]
```

The epistemic root appears immediately after the speaker-argument (`la-[speaker]`), before
the embedded proposition. The root modifies the speaker's *relationship to* the
proposition, not the proposition's internal content.

In gloss notation, the embedded proposition is shown in brackets `[...]` — the same
convention used for subordinate clauses.

### Positive Epistemic Scale

Three personal epistemic levels, perceptual floor to established ceiling:

| Level | Root | Meaning | Corpus |
|-------|------|---------|--------|
| Perceptual | `se` | I have signal data / I perceive | (negated form attested C007 B4; positive awaited) |
| Hypothesis | `si` | I hold at assessment level / I hypothesize | C001 A3, C006 A4 |
| Established | `to` | I hold as a conceptual pattern / I know | C005, C007 B1 |

The scale is hierarchical: `to` entails `si`; `si` entails `se`. Marking something as
established implies you have a hypothesis for it and a perceptual basis for it.

Institutional knowledge frameworks (`to-fe-su`, W072) represent a social layer above
personal `to` and are expressed through dedicated compounds, not by extending this
personal modal hierarchy.

### Negated Epistemic Modals

The prefix `no-` applies to any epistemic root in the modal position:

```
la-[speaker]  no-[epistemic-root]  [embedded proposition]
```

| Negated form | Meaning | Corpus |
|--------------|---------|--------|
| `no-to` | I do not hold as established | C005 B3 (first), C007 B2 (confirmed) |
| `no-si` | I do not hypothesize | C007 B3 (first) |
| `no-se` | I have no perceptual basis | C007 B4 (first) |

**Entailment direction is reversed from the positive scale.** The floor denial (`no-se`)
is the strongest claim, subsuming all levels above it. Mid-level and ceiling denials do
not entail the levels below:

```
Positive:   se → si → to         (floor presence entails upper: se required for si, si for to)
Negated:   no-se → no-si → no-to  (floor denial entails all: no-se subsumes no-si and no-to)
```

`no-to` alone is consistent with having `si` or `se` — saying "I don't hold X as
established" leaves open the possibility that you hypothesize it or have a perceptual
signal for it.

### Distinguishing `no-to` from `no-to-fe`

These constructions share the sequence `no-...-to` but are structurally and
semantically different:

- **`no-to` in epistemic position** (`la-[speaker]  no-to  [prop]`): personal epistemic
  disclaimer. The speaker denies holding the proposition at established level. Two
  morphemes: `no-` prefix on the `to` epistemic root.

- **`no-to-fe` as state predicate** (`lo-[thing]  no-to-fe`): institutional status
  descriptor. The proposition or entity has not crossed the certification threshold.
  Three morphemes: `no-` prefix on the compound `to-fe` (knowledge-boundary). Attested
  C005 B2.

`no-to` is about the speaker's epistemic state. `no-to-fe` is about an entity's
certification status. They can co-occur without entailing each other.

### Nested Epistemic Embedding

The embedded proposition slot may itself contain an epistemic modal, since
`la-[speaker]  [modal]  [prop]` is a well-formed proposition that can occupy any
`[prop]` slot:

```
la-mi  to  [la-tu  no-se  lo-ne-ra]
```
*I hold as established: [you have no perceptual basis for the resonance].* (C007 A5)

The outer `la-mi  to` certifies as established; the inner `la-tu  no-se  [prop]` is a
well-formed epistemic claim that serves as the embedded proposition. This is the
institutional form: a knowledge-keeper converts a witness's personal epistemic floor
into a formally certified matter of record.

No additional rule is required — nested embedding is a compositional application of
the standard subordination mechanism. One corpus attestation (C007 A5); treat as
confirmed structure pending a second case.

### Process Epistemic Frame

A non-personal source — an examination process, an institutional doctrine, a measurement system — may occupy the `la`-slot and generate a propositional finding as its output. This is the **process epistemic frame**, structurally parallel to the personal epistemic modal but with an output-production verb rather than an epistemic-stance root:

```
la-[non-personal-source]  [output-verb]  [embedded proposition]
```

Two output verbs are attested:

| Output verb | Meaning | Example | Corpus |
|-------------|---------|---------|--------|
| `be` | produces / generates [prop] as finding | examination generates the finding that X | C004 A2 |
| `si` | signals / asserts [prop] as claim | doctrine emits the claim that X | S084 |

`be` frames the proposition as the *output* of a productive process — the result it generates. `si` frames the proposition as the *assertion* the source emits. Both take a full embedded clause as their complement.

**This is the same `be` as the productive-process root** ("grow, produce, generate output"). When its complement is a proposition rather than a physical patient, the reading shifts naturally to "generates the finding that." No new meaning is required.

**Distinction from the personal epistemic modal:**

| Frame | Structure | Agent type | Verb type |
|-------|-----------|------------|-----------|
| Personal epistemic modal | `la-[person]  [epistemic-root]  [prop]` | person / speaker | epistemic stance root (`se`, `si`, `to`) |
| Process epistemic frame | `la-[source]  [output-verb]  [prop]` | process / institution / doctrine | production verb (`be`, `si`) |

In the personal frame, the root encodes the *speaker's relationship to* the proposition. In the process frame, the verb encodes *how* the source produces or emits the proposition. The two frames may appear in the same discourse with contrasting epistemic weight: personal modal = I hold at some confidence level; process frame = the process produces this as output regardless of my personal confidence. This contrast is exploited in C004 A1–A2, where A first makes a personal bare assertion, then escalates to process-grounded evidence.

---

## Subordinate Clauses

Tonesu has a class of **clause-introducing words** that open a dependent clause modifying or specifying the matrix (main) clause. The three current clause introducers are:

| Introducer | Type | Meaning |
|------------|------|---------|
| `go` | causal | because / since (cause introduces effect) |
| `wi` | purpose | in order that / with the intention that |
| `ta` | temporal | at the time that / when (time reference, no causal implication) |

### Boundary Rule

A subordinate clause begins immediately after its clause introducer and extends until its predicate marker (`ka-X`) is consumed. This is the **stack rule**: clause introducers push a new clause level onto a parsing stack; each predicate marker (`ka-X`) pops the innermost open level. The stack is empty during the matrix clause.

In gloss notation, subordinate clauses are shown in brackets `[...]`. In formal register, these boundaries are fully recoverable from explicit argument and predicate markers alone — no additional bracket particles are needed.

### Formal and Casual Register

- **Formal register:** all matrix-level argument and predicate markers are present, making clause boundaries unambiguous without additional devices.
- **Casual register:** reduction is permitted when the boundary is recoverable without explicit marking — typically in same-agent contexts or when clause shape makes the boundary obvious from context.

The canonical form is always the formal register. Casual reduction is derived from it and must be traceable back to a fully explicit form. The same-agent reduction rule (documented for `wi` in § Purpose Frame) generalizes to all subordinate clause types: a clause's agent may be omitted when it is identically recoverable from the immediately enclosing clause or from the matrix clause.

### Nested Subordination

Nesting is handled by the stack rule above. The one structural requirement is **linearization**: when a post-posed modifier (`wi`) is embedded inside a pre-posed subordinate clause (`go`, `no-go`, or `ta`), the `wi` clause must precede the outer clause's predicate. This preserves head-final modifier placement at every embedding level and keeps the stack rule unambiguous.

**Example:**

```
go [la-ze  wi [ka-understand]  ka-study]  la-mi  ka-end
```
*Because ze studied (in order to understand), I ended it.*

Stack trace: `go` pushes → `wi` pushes → `ka-understand` pops `wi` → `ka-study` pops `go` → `la-mi  ka-end` is matrix.

Arbitrarily deep nesting is permitted. Same-agent reduction applies at any nesting depth.

---

## Relative Clauses

A noun phrase may be modified by a preceding clause using **head-final clause
modification** — the same left-branching principle that governs word-level modification,
extended to clause scale. No relativizer particle is needed.

### Structure

```
[  modifying clause  ]   role-marker + head
```

The modifying clause precedes the head noun. One participant is absent from the
modifying clause (the **gap**). The head noun, appearing immediately after the
bracket, fills the gap semantically. The role-marker on the head (`la`, `lo`, `ne`,
etc.) encodes the head's role in the **main clause**, not in the modifying clause.

Example:

```
[lo-ne-ra  ka-se]  lo-mu  ne-mi  ka-be
```
*Build me the machine that perceived the resonance.* (S101)

The inner clause `[lo-ne-ra  ka-se]` is missing an agent — the gap is in the `la`
position. The head `lo-mu` (machine) fills that gap: the machine is what perceived
the resonance. In the main clause, `lo-mu` is the patient of `ka-be` (build it for me).

### Gap positions

| Gap | Inner clause structure | Head exits as |
|-----|------------------------|---------------|
| Agent absent | `[ lo-patient  predicate ]  role-head` | any role in main clause |
| Patient absent | `[ la-agent  predicate ]  role-head` | any role in main clause |
| Predication subject absent | `[ stative-predicate ]  lo-head` | `lo` in main clause |

The gap is uniquely identifiable when all other expected participants are present.
Action clauses (`ka`-predicate): absent agent = agent gap; absent patient = patient gap.
Stative predicates (no `ka`): absent `lo`-subject = subject gap.

### Role-particle principle

The role-particle on the head encodes its main-clause role **independently** of its
inner-clause role. The same head noun can exit with different particles depending on
how it is used in the main clause:

```
[lo-ne-ra  ka-se]  lo-mu  ne-mi  ka-be     → lo-mu: machine is patient of main-clause predicate
[lo-ne-ra  ka-se]  ne-mu  ka-[give]        → ne-mu: machine is recipient of main-clause predicate
```

### Stative inner clauses

The inner clause does not need to contain an action particle. Stative predicates —
kinship, epistemic state, property predication — are equally valid inner clauses:

```
[zo-ne-go  la-mi]  ne-li  ka-be
```
*Give [it] to the person who is my parent.* (S104)

The inner clause `[zo-ne-go  la-mi]` is a stative kinship predication. The gap is the
`lo` subject: the entity being described as "my parent" is absent from the inner clause
and filled by `ne-li`. `la-mi` in the inner clause is a relational anchor
(perspective marker), not an action agent.

### Nesting

Relative clauses may be nested — the head of an inner relative clause may itself serve
as the reference entity of an outer relative clause:

```
[zo-ne-ru  [zo-ne-go  la-mi]  lo-li]  ne-li  ka-be
```
*Give [it] to my parent's sibling.* (S105)

The inner NP `[zo-ne-go  la-mi]  lo-li` = "the person who is my parent" appears as
the reference entity inside the outer clause `[zo-ne-ru  inner-NP  ...]`.

Two levels of nesting are attested and parse cleanly (S105). Deeper nesting is
compositionally permitted. Complex paths are typically expressed as multiple declarative
sentences when depth exceeds two levels.

### Distinguishing relative clauses from subordinate clauses

Subordinate clauses have an explicit clause introducer before the bracket:
`go [...]`, `wi [...]`, `ta [...]`.

Relative modifier clauses have **no introducer** — the bracket immediately precedes
the role-marked head. This structural difference disambiguates the two constructions.

---

## Causal Frame (`go`)

The root `go` (cause/origin) functions as a clause introducer for causal and conditional relations. This is a transparent overlap: the causal-frame function is semantically derived from the cause root.

For clause boundary rules and register, see **Subordinate Clauses** above.

```
go [CAUSE-CLAUSE]  MATRIX-CLAUSE
```
*Because / when [cause clause] is true, the matrix clause follows.*

```
go [CAUSE-CLAUSE]  du [RESULT-CLAUSE]
```
*If [cause clause], then [result clause].* (`du` explicit optional; required when the result clause does not follow naturally from word order alone.)

Examples:
```
go [la-si  ka-ne-ki]  la-to  ka-be
```
*When information connects, knowledge grows.* (S013)

```
go [ka-be]  du [la-to  ka-zu]
```
*If something grows, knowledge increases.*

**Distinction from `wi`:** `go` looks backward to a cause that already holds or is posited. `wi` looks forward to an intended outcome. These are not interchangeable.

### `du` as full clause introducer

`du` (result/effect) operates symmetrically with `go` in the result position. When the
result clause is complex enough to require full clause structure, `du [RESULT-CLAUSE]`
expands the compound form:

```
go [CAUSE-CLAUSE]  du [RESULT-CLAUSE]
```

**Boundary rule for `go...du`:**
- The `go`-clause extends until `du` is encountered. `du` is a matrix-level frame word
  and terminates the cause clause immediately.
- The `du`-clause extends from `du` until sentence boundary (or the next matrix-level
  frame word, if embedded).
- **No outer matrix clause is required.** `go [X]  du [Y]` is a complete biclausal
  proposition — the causal relationship itself is the full assertion.

**Two registers:**

| Register | Form | Use |
|----------|------|-----|
| Formal | `go [full cause clause]  du [full result clause]` | new context, technical or legal prose |
| Compact | `go-[cause-compound]  du-[result-compound]` | established context, conversational (S011, S028) |

Examples:
```
go [lo-si  be]  du [la-ka-si-mu  ka-si  ru]          (S169)
```
*Because the signal grew, the transmitter transmitted successfully.*

```
go [lo-to-su-mu  de]  du [lo-to-su  de]              (S170)
```
*If the archive decays, organized knowledge decays.*

---

## Counterfactual Frame (`to-go`)

The compound `to-go` (conceptual-causal) extends the causal frame into non-actual space.
Head-final: `go` (cause/conditional frame) is head; `to` (conceptual/pattern) marks the
frame as hypothetical — the premise is non-actual, and so is the result.

```
to-go [NON-ACTUAL-PREMISE]  NON-ACTUAL-RESULT
```
*Counterfactually: if [premise had held], [result would have followed].*

`to-go [X]  Y` is to `go [X]  Y` as a non-actual conditional is to an actuality-neutral
conditional. Both mark the same causal relationship; only the ontological status differs:

| Frame | Premise | Result | Use |
|-------|---------|--------|-----|
| `go [X]  Y` | asserted or unspecified | follows from X | factual, general, or prospective conditional |
| `to-go [X]  Y` | explicitly non-actual | would have followed | counterfactual — past or future hypothetical |

**No stance-holder required.** Unlike `la-X  to  [prop]` (personal epistemic claim),
`to-go [X]  Y` makes a bare non-actual assertion about a causal relationship with no
attributor. Appropriate for investigation reports, narrative history, legal briefs, and
all other impersonal counterfactual discourse.

**Temporal axis is independent of the actuality axis.** `to-go` marks non-actuality;
time-marking inside premise and result clauses marks when the hypothetical is located:

```
to-go [lo-X  de]        result            → future hypothetical ("if X were to fail...")
to-go [lo-X  de  ti-de] result  ti-de     → past counterfactual ("if X had failed...")
```

**Attributed counterfactual:** when epistemic attribution matters (an arbiter ruling,
an on-the-record personal assessment), Path A wraps Path C:

```
la-X  to  [to-go [NON-ACTUAL-PREMISE]  NON-ACTUAL-RESULT]
```
*X holds as their conceptual model: counterfactually, if [premise], [result].*

These two constructions have distinct illocutionary force:
- `to-go [X]  Y` = bare counterfactual conditional (no thinker asserted)
- `la-X  to  [to-go [X]  Y]` = attributed counterfactual (X owns the counterfactual claim)

Examples:
```
to-go [lo-ra-ki-mu  de  ti-de]  lo-ki-pa-mu  pa-ki  ti-de
```
*If the engine had failed, the ship would have drifted.* (S130)

```
to-go [lo-to-re-su  to-fe-su-ki  ti-de]  lo-ne-fe  de  ti-de
```
*If the doctrine had been published, the dispute would have been resolved.* (S131)

---

## Concessive Frame (`no-go`)

The compound `no-go` (negation-of-cause) extends the causal frame to express **causal
independence**: Y holds regardless of X — not because of it, and not despite a
hypothetical (as in `to-go`), but as a real-world independence claim.

```
no-go [CONCURRENT-EVENT]  INDEPENDENT-RESULT
```
*Despite [X], Y holds. / Y is not derived from X.*

`no-go [X]  Y` asserts two things simultaneously:
1. X is a real event or state (unlike `to-go`, not hypothetical).
2. Y's truth does not originate in X. X and Y coexist, but causally independently.

**Three-member causal frame family:**

| Frame | Form | Relationship |
|-------|------|-------------|
| Factual causal | `go [X]  Y` | X causes / grounds Y |
| Counterfactual | `to-go [X]  Y` | non-actual X would cause Y |
| Concessive | `no-go [X]  Y` | Y holds independent of / despite X |

All three mark the same clause boundary structure: the bracketed clause is the dependent
clause; the matrix clause follows. The head is `go`; the prefix specifies the
causal-ontological relation.

**Contrast with `go`:** `go [la-mu  de-be]  lo-mu  ru` would mean the repair *caused*
the unity — the repair made the device one. `no-go [la-mu  de-be]  lo-mu  ru` means the
unity holds independent of the repair: the device was already and still is one.

Examples:
```
no-go [la-mu  de-be]  lo-mu  ru
```
*Despite the device being repaired, the device remains one.* (S180)

```
no-go [la-mu  pe  ki]  lo-mu  ru
```
*Despite the device's parts changing, the device remains one.* (S181, Ship of Theseus)

---

## Model-Domain Frame (`to  lo-[model]  be`)

A **discourse-scope frame** that opens and closes a stretch of sentences as operating in
the model layer (non-actual, analytical, hypothetical), removing the need to mark each
sentence individually with `to-go`. Where `to-go [X]  Y` is a clause-level counterfactual
frame for a single causal assertion, the model-domain frame opens a discourse scope over
multiple sentences.

**Scope-open:**
```
to  lo-[model-reference]  be
```
*The conceptual model [of X] activates. All following sentences operate in model space
until the scope is closed.*

- `to` = conceptual model root (predicate)
- `lo-[model-reference]` = patient: the model being activated (e.g., `lo-go-su` = the causal
  analysis; `lo-to-go-su` = the counterfactual analysis; any model-reference NP)
- `be` = generation/activation: the model activates
- No `la-` required — scope opens impersonally, parallel to `to-go [X]  Y`

**Attributed scope-open:** when the scope belongs to a specific assertor (investigation
body, doctrine, theory):
```
la-X  to  lo-[model-reference]  be
```
*X activates the model scope. All following sentences are attributable to X's model.*

**In-scope sentences:** sentences between the scope-open and scope-close operate in the
model layer. They are stated as in-model facts — not individual counterfactuals. No
`to-go` prefix required per sentence.

- Causal links inside scope use `go [X]  Y` (model-causal assertion within the frame),
  not `to-go [X]  Y` (the outer scope already marks non-actuality).
- Temporal markers (`ti-de`, etc.) inside scope mark time within the model scenario,
  exactly as in individual `to-go [X]  Y` sentences.

**Scope-close:**
```
to  lo-[model-reference]  de           ← explicit close
```
or any actuality-asserted sentence (world-layer assertion implicitly terminates scope).

- `de` = decay/close: the model deactivates. Symmetric with `be` (open).
- Attributed close: `la-X  to  lo-[model-reference]  de` — X closes the scope they opened.
- **Formal register** expects a symmetric explicit close (same attributor opens and closes).
- **Casual register** may rely on implicit close via actuality-return sentence.

**Actuality-return sentence:** any sentence using `la-[agent]  ka  [action]` (agentive
world-layer assertion) or similar world-layer construction with no model-frame marker
terminates model scope implicitly and reasserts the world layer.

**Summary:**

| Form | Layer | Scope |
|------|-------|-------|
| `go [X]  Y` | world | single causal assertion |
| `to-go [X]  Y` | model | single non-actual causal assertion |
| `to  lo-[model]  be ... de` | model | multi-sentence non-actual scope |
| `la-X  to  [to-go [X]  Y]` | epistemic | attributed single counterfactual |
| `la-X  to  lo-[model]  be ... de` | epistemic | attributed multi-sentence scope |

**Relationship to `to-go [X]  Y`:** for single-sentence counterfactuals, `to-go [X]  Y`
remains canonical — it is more compact and grammatically self-contained. The model-domain
frame is warranted when three or more sentences belong to a single analytical scope and
the per-sentence `to-go` prefix creates structural redundancy.

Examples:
```
to  lo-go-su  be
```
*The causal analysis model activates.* (S159)

```
to  lo-go-su  be
lo-si  no  be  ti-de.  la-li-pu  no  se  lo-si  ti-de.  la-li-pu  no  ka  fe-si  ti-de.
to  lo-go-su  de.
```
*[Model open] Signal had not arrived. Crew had not received it. Crew had not warned.
[Model closed.]* (S159)

```
la-to-fe-su  to  lo-go-su  be
```
*The investigation body opens the causal model.* (S160)

---

## Aspect

Repetition/habituality in Tonesu is expressed by two distinct strategies that are not
synonymous. Both are grammatically legal.

### Strategy 1 — Time-adverbial (`ta-re-[cycle]`)

```
la-[agent]  ta-re-[time-unit]  VERB
```

The time slot (`ta`) contains a compound time noun built with `re` (repetition) as a
modifier: `ta-re-ti` (at each recurring cycle), `ta-re-X` (at each recurring X). This
strategy quantifies over **scheduled intervals** — it says when the event recurs.

```
la-wi-re-su  ta-re-ti  ka-ne        (S166)
```
*The committee meets at each recurring interval.* — a fact about the committee's schedule.

### Strategy 2 — Morphological aspect prefix (`re-VERB`)

```
la-[agent]  re-[verb-compound]
```

The prefix `re-` (repetition) attaches to the entire verb compound (before `ka-`). This
strategy marks **dispositional habituality** — a property of the agent's or system's
characteristic behavior.

```
la-ze  re-ka-se                     (S167)
```
*She habitually records observations.* — a claim about her disposition, not her schedule.

### Distinguishing the two

| | Strategy 1 `ta-re-X  VERB` | Strategy 2 `re-VERB` |
|--|--|--|
| What it describes | external frequency / schedule | agent or system disposition |
| Negatable while the other holds | yes — she can have a disposition without a schedule | yes — a schedule can exist without indicating disposition |
| Register | neutral | neutral |

**Minimal contrast:** `la-ze  ta-re-ti  ka-se` = "she records at regular intervals"
(schedule); `la-ze  re-ka-se` = "she is a habitual recorder" (character).

### Aspect with past/future markers

`re-VERB  ta-[time]` — the aspect prefix and the time marker are independent:

```
lo-to-su-mu  re-ka-de-be  ti-de     (S168)
```
*The archive was habitually maintained.* (`re-` = habitual aspect; `ti-de` = past time)

The two modifiers are orthogonal and do not collapse.

---

## Temporal Frame (`ta`)

The particle `ta` (time reference) functions both as a simple time marker before a time expression and as a clause introducer for temporal subordinate clauses.

For clause boundary rules and register, see **Subordinate Clauses** above.

**As a time marker** (before a time expression):
```
ta-future
ta-past
ta [specific time reference]
```

**As a temporal clause introducer:**
```
ta [TIME-CLAUSE]  MATRIX-CLAUSE
```
*At the time that [time clause], the matrix clause holds.*

`ta` expresses temporal coincidence or sequence. It carries no causal implication. For events where the temporal relationship also implies causation, prefer `go` framing.

### Time Reference Compounds

The `ti` (time) root combines with directional primitives to produce a family of temporal reference compounds. All are used in the `ta` frame (`ta-ti-X`):

| Compound | Roots | Meaning | Corpus | Registry |
|----------|-------|---------|--------|----------|
| `ti-de` | time + decay | past time; previous interval; yesterday | S035, S066 | W041 |
| `ta-now` | `ta` + deictic | present moment | throughout | — |
| `ti-be` | time + growth | proximate future; next time; tomorrow | C003, C006 A4 | W040 |
| `ti-re` | time + recurrence | next scheduled occurrence; next cycle | C006 B4 | W103 |
| `ti-fe` | time + boundary | deadline; time-limit; the moment of | throughout | W037 |

**Linear vs. cyclic distinction (`ti-be` / `ti-re`):**

`ti-be` and `ti-re` both reference a future time point, but differ in temporal structure:

- **`ti-be`** = the next interval on the **open linear timeline** — generic "soon," "tomorrow," "in the near future." No recurring structure is implied or required.
- **`ti-re`** = the next occurrence in an **established recurring sequence** — "when it comes around again," "at the next session," "next cycle." A cycle must be contextually established.

**Decision rule:** use `ti-be` when the claim is only that time will pass; use `ti-re` when the event belongs to a known recurrent pattern and the next instance is being referenced.

**Corpus contrastive pair (C006):** A4 uses `ta-ti-be  ne-ra-ki  be` ("the link will develop soon" — open-timeline prediction); B4 replies `ta-ti-re  ki` ("yes, it's coming up in the cycle" — scheduled resonance training). Same event, different temporal frames: A is predicting on the linear timeline; B is announcing the next scheduled occurrence.

### Event-Anchor Construction

A `lo-`-marked event nominal may follow a time compound to set the temporal reference point relative to that event — the **event-anchor** construction:

```
ta  ti-[dir]  lo-[event]   MATRIX-CLAUSE
```

The direction compound (`ti-de` or `ti-be`) specifies the relative position; the `lo-[event]` phrase names the anchor event.

| Form | Meaning | Corpus |
|------|---------|--------|
| `ta-ti-de  lo-[event]` | before [event] | S092 (`ta-ti-de  lo-ka-wi-de` — before the mission departure) |
| `ta-ti-be  lo-[event]` | after [event] | S192 (`ta-ti-be  lo-se-ka` — after the inspection) |

The construction is compositionally transparent: `ti-de` = time-that-has-decayed = prior time; `ti-be` = time-that-is-growing = following time. The `lo-` particle marks the anchor event in its standard patient role. Any event nominal can serve as the anchor.

---

## Purpose Frame

The root `wi` (will/intention) doubles as a purpose-frame particle, introducing a subordinate clause whose content is the intended outcome of the main clause event. This is a transparent overlap: the purpose-frame function is semantically derived from the will/intention root.

```
MAIN-CLAUSE  wi [PURPOSE-CLAUSE]
```

The event in the main clause is performed with the intention that the purpose clause occur.

**Canonical constraint:** `wi` introduces a **full clause**, not a bare verb phrase. The purpose clause may omit its agent when it is identical to the main clause agent (same-agent reduction), but full clause structure — including explicit agent marking — is canonical and always valid.

### Same-agent purpose (agent omitted in purpose clause)

```
la-ze  ka-study  wi [ka-understand]
agent:they  action:study  intention [action:understand]
```
*They study in order to understand.*

Reduced form: purpose-clause agent is omitted because it is identical to the main clause agent (`ze`). Full form retains `la-ze`.

### Different-agent purpose (agent explicit in purpose clause)

```
la-mi  ka-be  lo-mu  wi [la-tu  ka-use  lo-mu]
agent:I  action:create  patient:artifact  intention [agent:you  action:use  patient:artifact]
```
*I built the machine for you to use.*

Different agents require full clause marking. Same-agent reduction **does not apply**.

### Agent inheritance rule (confirmed S016–S017)

When a `wi` purpose clause omits its agent marker, the matrix clause agent is inherited. This is the unambiguous default interpretation — agent omission is never ambiguous in a `wi` clause.

> **If the agent is absent, the matrix agent is performing the purpose-clause action.**
> **Any other agent must be explicitly marked with `la-[agent]`.**

This rule is confirmed by two corpus examples:
- S016: matrix agent `mi` (I), purpose clause has no agent → `mi` does the operating
- S017: matrix agent `ze` (she), purpose clause has no agent → `ze` does the warning

The rule likely generalizes to `go` and `ta` subordinate clauses, but is only confirmed for `wi` at this stage.

**Distinction from `go`:** `wi` introduces purpose — an intended outcome that has not yet occurred. `go` introduces cause — an origin that already holds or is posited. `wi [understand]` = "in order to understand"; `go [understood]` = "because (they) understood."

For clause boundary rules, register, and nested subordination policy, see **Subordinate Clauses** above.

> **Provisional (S016–S017):** Same-patient reduction — the purpose-clause patient may be omitted when identical to the immediately preceding main-clause patient. Confirmed in S016 (`lo-mu` recovered); S017 has no shared patient (matrix patient `lo-si` is the message; warning target is a recipient `ne-yu`, not a patient). Pending one more case before closing.

---

## Minimal Pronoun Set

| Form | Meaning |
|------|---------|
| `mi` | speaker (I) |
| `tu` | listener (you) |
| `ze` | other person/entity |
| `yu` | group (we/they) |

Pronouns follow the same case-marking rules as nouns.

---

## Imperative

A direct command is a **reduced matrix clause** with the second-person agent marker suppressed.

**Rule:** Omit `la-tu`. All other argument and predicate markers remain in their canonical positions. The addressee-as-agent is implied by the absence of any other agent marker in an addressed-speech context.

```
lo-mu  ne-mi  ka-be
(patient:machine)  (recipient:me)  (action:build)
→  Build me a machine.

ka-be  lo-mu
(action:build)  (patient:machine)
→  Build it.

no-ka-ki  lo-mu
(neg-action:move)  (patient:machine)
→  Don't move the machine.
```

**Interpretation rule:** When no `la-X` is present in an addressed-speech context and the clause is not one of the recognized agentless-process forms, parse as imperative.

**Emphatic and polite forms:** Retaining `la-tu` explicitly shifts the register toward formal request or emphasis. Full form (`la-tu  lo-mu  ka-be`) = strong directive or polite request depending on prosody. Reduced form = standard command. The prosodic distinction is pending phonology decisions.

**Consistency with agent inheritance:** The same agent-omission logic used in `wi` purpose clauses applies here — omission always refers to a contextually established agent, never an unspecified placeholder. In the imperative, context establishes the addressee (`tu`) as that agent.

**Corpus status:** Imperative forms not yet attested in corpus. S019 (P004) identified the gap; this rule closes it as a grammar specification. First corpus example pending.

---

## Comparison

Comparison between two entities on a shared quality dimension uses `nu-no` (less-than) or `nu-be` (more-than).

**Composition:**
- `nu-no` = quantity (`nu`) + negation (`no`) = less / fewer / to a lesser degree
- `nu-be` = quantity (`nu`) + growth (`be`) = more / greater / to a higher degree

Both are compositionally transparent: `nu` carries the measurable dimension; `no`/`be` give the direction.

### Structure

```
lo-A  [quality]  nu-no  [baseline]   →  A has less [quality] than baseline
lo-A  [quality]  nu-be  [baseline]   →  A has more [quality] than baseline
```

The baseline is typically `lo-B` (another entity). For comparison against a past or future state, substitute a temporal reference (`ta-ti-[time]`), giving a self-comparison across time.

### Examples

```
lo-ma-di  ha-vo  nu-no  lo-pa-ma           (S039) →  The water is cooler than the air.
lo-ko-pa  ha-vo  nu-be  lo-ki-pa           (S064) →  The room is warmer than the corridor.
lo-mu  pa-nu  nu-be  lo-mu-ne              (S065) →  The machine is larger than the other one.
lo-li-be  ta-ti-now  zo-de  nu-no  ta-ti-de (S066) →  The child is less tired than yesterday.
lo-si  ra-vo  nu-be  lo-si-fe             (S067) →  The signal is stronger than the threshold.
```

### No degree split

`nu-no`/`nu-be` apply to both count quantity (more soldiers) and quality degree (warmer). The `nu` root covers measurable dimension in both senses.

**Corpus basis:** first attested S039 (`nu-no`); `nu-be` confirmed and generalized in S064–S067.

---

## Numerals

Cardinels, ordinals, fractions, and measurement all build from the **digit inventory** (CVC-tier) and the **quantity primitive** `nu`. No new roots are required.

### Digit inventory

| Digit | Form  | Digit | Form  |
|-------|-------|-------|-------|
| 0 | `nil` | 5 | `hin` |
| 1 | `bol` | 6 | `wes` |
| 2 | `bun` | 7 | `yom` |
| 3 | `gal` | 8 | `fon` |
| 4 | `mol` | 9 | `zan` |

Digits occupy the **CVC descriptor tier** — they cannot be confused with CV-primitive roots or compound elements by a structural parser. This is the key property ensuring positional chaining is unambiguous.

### Cardinals

```
[digit]  nu  [noun]
```

Single digit:
```
gal nu mu          → 3 objects
hin nu li          → 5 people
```

Positional chain — most-significant digit first:
```
bun gal  nu  zo    → 23 organisms
bol nil  nu  ti    → 10 [time-units]
```

All CVC digits before `nu` are read as a single positional numeral. There is no structural ambiguity: CVC forms are tier-marked and cannot parse as CV roots or compound-initial elements.

### Ordinals

```
[digit]  ti
```

`ti` (time/sequence primitive) in compound-suffix position on a digit gives ordinal position.

```
bol ti             → first
bun ti             → second
gal ti             → third
```

Ordinals modify nouns directly or occur as bare predicate complements:
```
la-mi  ka  bun ti                 → I acted for the second time. (S246)
la-[zo-ne  go  bun ti]  ki  lo-mi → My grandparent came to me. (S240)
```

Generation distance uses `[zo-ne go [digit] ti]` — the ancestor-relation at the nth origin-step. This resolves the S097 gap directly (grandparent = `zo-ne go bun ti`).

### Measurement

```
[digit]  [scale]  nu  [domain]
```

Base (no scale):
```
gal  nu  pa        → 3 [units of] space  (≈ 3 meters)
bun gal  nu  ti    → 23 [units of] time  (≈ 23 seconds)
```

With scale prefix:
```
hin  pir  nu  pa   → 5 kilo-space  (= 5 kilometers)  (S243)
gal  pir  nu  ma   → 3 kilo-matter (≈ 3 kilograms)
```

Domain (`nu [root]`) is the base unit. Scale prefix multiplies. Digit precedes. The three modifiers are independent and freely combinable; order is fixed: **digit → scale → nu → domain**.

Base SI domains: `nu pa` (space/meter), `nu ti` (time/second), `nu ma` (matter/kilogram), `nu ha` (heat/kelvin), `nu ra` (force), `nu lu` (light), `nu so` (sound), `nu si` (signal/bit). See `notes/cvc-inventory.md §Base units as compounds`.

### Fractions

```
ru-pu  [digit]            → 1/n   (one-of-n)
[digit]  ru-pu  [digit]   → m/n   (m-of-n)
```

`ru` (unity/one) + `pu` (plurality/many) = "one of many" = the fractional unit constructor. The divisor follows `ru-pu`; an optional numerator precedes.

```
ru-pu bun          → 1/2
ru-pu gal          → 1/3  (S247)
ru-pu mol          → 1/4  (= right-angle fraction; also S233)
bun ru-pu gal      → 2/3  (S248)
gal ru-pu mol      → 3/4
```

Right angle = `fe-di-ne ru-pu mol` (one-quarter of a full turn) or `fe-di-ne ru-pu` (context-default quarter). First attested S233 (GEO-001).

Fractions in a counting context: `ru-pu gal nu zo-ma` = one-third quantity-of food (S247).

### Time expressions

Time units are compounds on `re` (repetition/cycle) and `ti` (time):

| Unit | Compound | Construction |
|------|----------|--------------|
| hour | `re-ti` | recurring time unit (first attested S249) |
| minute | `re-ti-de` | diminished recurring time |
| day | `re-ti-be` | extended recurring time |
| year | `hulm` | CVCC anchor (conventional) |

Time of day: `ta-ti  [digit] nu re-ti` = at [n] o'clock (S249) 
Ordinal day: `[digit] ti  re-ti-be` = [n]th day (S250)

`ta-ti` introduces the temporal frame (see § Temporal Frame).

### Arithmetic predicates

Quantified NPs function as ordinary grammatical agents or patients. All standard predication strategies apply:

```
la-hin nu li  ne  lo-pa   → Five people are in the space. (S251)
la-gal nu mu  ki           → Three objects moved.
```

Numerically quantified NPs have no special syntax. The digit-chain is pre-nominal; the NP head follows `nu`.

**Corpus basis:** S238–S251 (NUM-001, March 2026). Pressure domains confirmed: object counting, positional chaining, ordinals, generation distance (S240–S241), measurement stack (S242–S244), fractions (S247–S248), time expressions (S249–S250), numeric predicates (S251).

---

## Containment Predicates

The root `ko` (containment/interior) functions as either a **state predicate** or a component of an **intentional action compound** (`ka-ko`). The distinction is grammatically and semantically significant.

### `ko` as state predicate

`la-[container]  ko  lo-[contents]` = X holds / contains Y (no action; current relational state)

The container occupies the `la`-agent slot; the contents occupy the `lo`-patient slot. `ko` alone asserts a holding relationship, not an act of placing. Any entity that structurally contains another — physical vessel, institutional archive, material medium — is grammatically a `la`-agent of a `ko`-predicate.

```
la-mu        ko  lo-ha-ra      (S037) →  The metal holds thermal energy.
la-ko-mu     ko  lo-ma-di     (S068) →  The vessel contains water.
la-si-su     ko  lo-si-mu     (S070) →  The archive holds records.
```

### `ka-ko` as intentional action

`la-[agent]  lo-[item]  [ne-destination]  ka-ko` = X intentionally stores / places Y [into Z]

The `ka` action marker combines with `ko` to produce agentive containment. An agent must be present. The destination container is optionally marked with the `ne` recipient particle.

```
la-ze  lo-si-mu  ka-ko               (S069) →  She stored the document.
la-ze  lo-ka-mu  ne-ko-mu  ka-ko    (S071) →  He placed the tool into the container.
```

### Rule

| Form | Claim | Agent required |
|------|-------|----------------|
| `la-X  ko  lo-Y` | X is in the state of containing Y (nominal) | no — any container entity |
| `la-X  ko  [clause]` | X holds / records the proposition that [clause] | no — any epistemic container |
| `la-X  [lo-Y]  ka-ko` | X intentionally stores Y | yes — agentive |

`ko` alone is never agentive. Intentional placement always uses `ka-ko`.

### Clausal complement

`ko` accepts an embedded clause as its patient when the container is an epistemic structure — an archive, a doctrine, a treaty, a memory system. The container type determines the semantic register; the grammar is unchanged:

```
la-to-re-su  ko  [lo-mu  zo-to]     (C005 A2) →  The doctrine holds: the machine has soul-pattern.
la-si-su     ko  [la-ra-ki-li  se  lo-pa-ra]  (S191) →  The archive holds: the pilot perceived the field.
```

**Decision rule:** When the container is a physical vessel, `lo-Y` names a physical patient. When the container is an institutional or epistemic structure, `lo-Y` may be replaced by an embedded clause naming the propositional content. The same `la-X  ko  Y` structure handles both — no new parser rule is required.

---

## Open Questions

- [x] ~~Finalize grouping/nesting particle syntax~~ — resolved; see § Concept Nesting. Role-marker scoping + `'` + `na` + frame markers cover all NP grouping cases; no dedicated grouping particle needed.
- [x] **Subordinate clause delimiter:** Stack rule — no new particles. Clause introducers push a new clause level; each `ka-X` predicate pops the innermost open level. Formal register relies purely on explicit matrix markers. Nested-subordination linearization constraint: a `wi` clause embedded inside `go`/`no-go`/`ta` must precede the outer clause's predicate. Same-agent reduction generalizes to all clause types. See § Subordinate Clauses.
- [x] ~~Decide whether domain marker `da` is pre-posed before the domain root or wraps a phrase~~ — resolved; `da-` is a bound prefix that always fuses with the root compound (`da-to-ki`, `da-ra`, etc.). Never a free particle. See spec/domain-creation.md and open-questions.md.
- [ ] Specify behavior when agent and patient are both omitted (topic-drop)
- [x] ~~Confirm particle set doesn't collide with planned root phonology~~ — resolved; `ra`→`ro` (instrument particle), `se`→`ze` (3rd-person pronoun), `wi`→`yu` (group pronoun) removed all collisions; Particle–Root Overlap Policy formalized in § Particle–Root Overlap Policy.
- [ ] Define passive / agentless clause structure (no agent present)
- [x] ~~Causal framing (go/du pair) needs a grammar rule~~ — resolved; see § Causal Frame. `go [cause-clause]  matrix-clause` is pre-clausal; SOV governs the matrix. Extended by `du`, `to-go`, `no-go` in the same frame family.
