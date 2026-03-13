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
| `ra` | instrument marker | marks the tool or cause |
| `pa` | location marker | where the action occurs |
| `ne` | recipient/relation | who receives or to whom |
| `ta` | time reference | temporal anchor |
| `ka` | action marker | marks the verb/action |
| `na` | proper name marker | signals identifier, not compositional noun |
| `da` | domain marker | signals a conceptual domain reference |

*Particles are pre-posed (come before the element they mark).*

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
