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
| `se` | 3rd person (other/they) | `se` (perception) | other/they ≠ perception | **COLLISION** |
| `wi` | group (we/they) | `wi` (will/intention) | group ≠ will; also candidate purpose-frame | **COLLISION × 2** |

The `se` and `wi` pronoun collisions are open issues. Candidate replacements: `ze` for 3rd person, `yu` for group — both are available CV forms with no root or function-word assignment. See notes/open-questions.md.

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

## Causal Conditional

The `go`/`du` pair encodes causal relations and serves as the canonical conditional structure. No dedicated "if/when" particle is needed.

```
go [clause A]  [main clause]
```
*Because/when A is true, the main clause follows.*

```
go [clause A]  du [clause B]
```
*If A, then B.* (Explicit `du` optional when the main clause follows naturally.)

Examples:
```
go [la-si  ka-ne-ki]  la-to  ka-be
```
*When information connects, knowledge grows.* (S013)

```
go [ka-be]  du [la-to  ka-zu]
```
*If something grows, knowledge increases.*

The temporal particle `ta` with a subordinated clause (`ta [clause]`) expresses "at the time that" but lacks the causal implication. For conditionals with implied causation, prefer `go` framing.

---

## Minimal Pronoun Set

| Form | Meaning |
|------|---------|
| `mi` | speaker (I) |
| `tu` | listener (you) |
| `se` | other person/entity |
| `wi` | group (we/they) |

Pronouns follow the same case-marking rules as nouns.

---

## Open Questions

- [ ] Finalize grouping/nesting particle syntax
- [ ] Decide whether domain marker `da` is pre-posed before the domain root or wraps a phrase
- [ ] Specify behavior when agent and patient are both omitted (topic-drop)
- [ ] Confirm particle set doesn't collide with planned root phonology
- [ ] Define passive / agentless clause structure (no agent present)
- [ ] Causal framing (go/du pair) needs a grammar rule for how it integrates with SOV order
