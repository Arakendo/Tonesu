# Tonesu — Copilot Workspace Instructions

This repository is the design record for **Tonesu**, a constructed language.
Every spec, registry entry, and corpus sentence is normative; treat them as
the ground-truth source of record when answering questions or doing work.

---

## Quick orientation

| What you need | Where to look |
|---------------|---------------|
| Grammar rules (particles, slots, word order) | `spec/grammar.md` |
| Phonology rules, parse invariants, tier system | `spec/phonology.md` |
| Morphology (agent/patient/result slots, affixes) | `spec/morphology.md` |
| Word-formation procedure, CVC/CVCC admission rules | `spec/word-formation.md` |
| Naming conventions | `spec/naming.md` |
| Domain-creation protocol | `spec/domain-creation.md` |
| Guiding design principles | `spec/principles.md` |
| All primitive roots (CV closed set, ~34 active) | `registry/primitives.md` |
| Derived compound quick-reference index (W000–W116+) | `registry/derived/index.md` |
| Derived compounds W000–W050 (full entries) | `registry/derived/w001-w050.md` |
| Derived compounds W051–W100 (full entries) | `registry/derived/w051-w100.md` |
| Derived compounds W101+ (full entries, active intake) | `registry/derived/w101-plus.md` |
| Domain registry | `registry/domains.md` |
| Root registry (named roots, non-primitive anchors) | `registry/roots.md` |
| Colloquial contracted forms | `registry/colloquial.md` |
| Sentence corpus index | `corpus/sentences/index.md` |
| Sentence corpus (S001–S039) | `corpus/sentences/s001-s039.md` |
| Sentence corpus (S040–S071) | `corpus/sentences/s040-s071.md` |
| Sentence corpus (S072–S100) | `corpus/sentences/s072-s100.md` |
| Sentence corpus (S101–S175) | `corpus/sentences/s101-s175.md` |
| Sentence corpus (S176–S227) | `corpus/sentences/s176-s227.md` |
| Sentence corpus (S228–S251) | `corpus/sentences/s228-s251.md` |
| Sentence corpus (S252–S278) | `corpus/sentences/s252-s278.md` |
| Sentence corpus (S279+, active intake) | `corpus/sentences/s279-plus.md` |
| Corpus index | `corpus/index.md` |
| Bible translation stress tests | `corpus/translations/Bible/` |
| Open design questions | `notes/open-questions.md` |
| Language basics summary | `notes/basics.md` |
| Prior art / inspiration notes | `notes/prior-art.md` |
| Semantic map | `notes/semantic-map.md` |

---

## Key facts to keep in mind

### Word shape = tier membership

| Shape | Tier | Rule |
|-------|------|------|
| CV | Primitive root | Closed set; passes all three primitive validation rules |
| CV-CV+ | Compound | Compositional; no new primitive needed |
| CVC | Lexical atom | Digits, colors (closed), or ergonomic shortforms |
| CVCC | Exceptional anchor | Constants/convention units only; Assemblage-First Rule applies |
| V | Bare-vowel particle | Word-initial only; 5 slots reserved; none assigned |
| VC | Deferred tier | Word-initial only if admitted; ~40 forms; currently unused |

### Parse invariants (never violate)

1. Every internal syllable begins with a consonant.
2. Compound boundaries are phonologically visible without lookahead.
3. Root tiers are structurally distinct — a form's shape identifies its tier.

### Grammar slots (core sentence frame)

```
la-[agent]  [verb-compound]  lo-[patient]
```

- `la-` agent prefix · `lo-` patient prefix · `lu-` result/beneficiary
- `ne` copula (property attribution) · `go` causal/origin particle
- Modifier precedes head · right-branching compound parse by default

### Derived registry — status codes

- ✅ active / accepted  
- ⚠️ proposed  
- ❄️ cold  
- 🚫 retired  

New entries always go into `registry/derived/w101-plus.md` first.
Always update `registry/derived/index.md` (all three sections: A, B, C) when adding entries.

### `[X]-no-fe` extremal suffix (THO-001, canonical)

`X` + `no` (negation) + `fe` (boundary) = X without limiting boundary.
Productive across all property roots — not God-specific.
Key instances: `to-no-fe` omniscience · `ra-no-fe` omnipotence ·
`vo-no-fe` omnibenevolence · `pa-no-fe` omnipresence · `go-no-fe` necessary being ·
`ti-no-fe` eternal · `nu-no-fe` mathematical infinity.

---

## Working conventions

- Hyphens in Tonesu examples are **analytic notation only** — written Tonesu is solid (`tofesuki`, not `to-fe-su-ki`). The apostrophe `'` is the only normative internal character.
- Sentence numbers (`S001`, `S349`, …) are stable identifiers — never renumber.
- W-numbers (`W000`, `W116`, …) are stable identifiers — never renumber. Retired entries keep their numbers.
- Corpus tests are tracked under THO- (theological), GRAM- (grammar), etc. labels. New batch labels go in `corpus/sentences/s279-plus.md`.
- Open questions are logged in `notes/open-questions.md`. Mark resolved with `[x]` and a brief resolution note; do not delete old entries.
