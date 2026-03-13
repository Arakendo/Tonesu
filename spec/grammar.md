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
| `la` | agent marker | marks the doer |
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
| `-se` | quality/property suffix | `se` (perception) | "perceivable property" — indirect link | **Needs justification** |
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

Grouping particles mark compound noun phrases as a single unit when needed.

```
[knowledge-transfer system]-design
```

Open question: use paired particles (e.g. `be...be`) or rely on stress/pause?

---

## Negation

Single negation particle prefixed to the verb or predicate.

```
no-build
no-possible
no-true
```

---

## Questions

Interrogative particle at sentence end (or optionally front for emphasis).

```
la engineer  lo machine  ka build-now  ?
```
*Is the engineer building the machine?*

---

## Subordinate Clauses

Tonesu has a class of **clause-introducing words** that open a dependent clause modifying or specifying the matrix (main) clause. The three current clause introducers are:

| Introducer | Type | Meaning |
|------------|------|---------|
| `go` | causal | because / since (cause introduces effect) |
| `wi` | purpose | in order that / with the intention that |
| `ta` | temporal | at the time that / when (time reference, no causal implication) |

### Boundary Rule

A subordinate clause begins immediately after its clause introducer and extends over the following clause material until parsing returns to the matrix clause, normally signaled by the next matrix-level argument or predicate marker (`la`, `lo`, `ka`, etc.).

In gloss notation, subordinate clauses are shown in brackets `[...]`. These brackets are a **notation convention only** — they are not a defined syntactic device in the language. The mechanism for marking clause boundaries in speech and writing is an open question (see Open Questions).

### Formal and Casual Register

- **Formal register:** all matrix-level argument and predicate markers are present, making clause boundaries unambiguous without additional devices.
- **Casual register:** reduction is permitted when the boundary is recoverable without explicit marking — typically in same-agent contexts or when clause shape makes the boundary obvious from context.

The canonical form is always the formal register. Casual reduction is derived from it and must be traceable back to a fully explicit form.

### Nested Subordination

Embedding a subordinate clause inside another subordinate clause (e.g., a purpose clause inside a causal clause) is **not yet specified**. The boundary rule above handles single-level embedding only. Nested structures should appear in the corpus before a general rule is written. Treat nested subordination as **provisional** until corpus evidence demands a solution.

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

**Distinction from `go`:** `wi` introduces purpose — an intended outcome that has not yet occurred. `go` introduces cause — an origin that already holds or is posited. `wi [understand]` = "in order to understand"; `go [understood]` = "because (they) understood."

For clause boundary rules, register, and nested subordination policy, see **Subordinate Clauses** above.

> **Open:** Same-patient reduction — can the purpose-clause patient be omitted when identical to the main-clause patient? **Provisional verdict (S016):** yes, when the shared patient is explicit in the immediately preceding main clause. Example: `la-mi  ka-be-past  lo-mu  wi [la-tu  ka-use]` recovers `lo-mu` unambiguously. Further corpus evidence (P003) required before this is fully closed.

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

## Open Questions

- [ ] Finalize grouping/nesting particle syntax
- [ ] **Subordinate clause delimiter:** The boundary rule is defined (see Subordinate Clauses): a subordinate clause extends until the next matrix-level argument or predicate marker. What remains open is the **formal-register mechanism**: does Tonesu rely purely on explicit matrix markers (no new device needed), or add optional explicit bracket particles for complex cases? The casual-register reduction rule follows once the formal answer is settled.
- [ ] Decide whether domain marker `da` is pre-posed before the domain root or wraps a phrase
- [ ] Specify behavior when agent and patient are both omitted (topic-drop)
- [ ] Confirm particle set doesn't collide with planned root phonology
- [ ] Define passive / agentless clause structure (no agent present)
- [ ] Causal framing (go/du pair) needs a grammar rule for how it integrates with SOV order
