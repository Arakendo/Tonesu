# Tonesu — Copilot Workspace Instructions

This repository is the design record for **Tonesu**, a constructed language.
Every spec, registry entry, and corpus sentence is normative; treat them as
the ground-truth source of record when answering questions or doing work.

---

## Quick orientation

### Folders

| Folder | Contents |
|--------|----------|
| `spec/` | All normative language rules — grammar, phonology, morphology, word-formation, naming, domain-creation, principles. Start here for language design questions. |
| `registry/` | All word inventories — primitives, derived compounds, roots, domains, colloquial forms. The `derived/` subfolder holds the active intake file and full entry files. |
| `registry/derived/` | Derived compound full entries split by W-number range; `index.md` is the quick-reference. New entries always go into `w101-plus.md` first. |
| `corpus/sentences/` | Numbered sentence corpus split into ~40-entry files; `index.md` is the quick-reference. New sentences always go into `s279-plus.md` first. |
| `corpus/translations/` | Translation stress tests by source text. Each source gets its own subfolder (e.g. `Bible/`). |
| `notes/` | Open questions, design notes, semantic map, basics summary, prior-art. Non-normative but important context. |

### File split policy

Files in `registry/derived/` and `corpus/sentences/` are split when they reach ~50 entries. When splitting:
- **Derived compounds**: close the current `w101-plus.md` range, create the next `wNNN-plus.md`, update `registry/derived/index.md` entry counts.
- **Sentence corpus**: close the current range file, create the next `sNNN-plus.md`, update `corpus/sentences/index.md` entry counts.
Never renumber existing W-numbers or S-numbers when splitting.

### Key files within folders

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
| Derived compound quick-reference index | `registry/derived/index.md` |
| Active derived intake (new entries here first) | `registry/derived/w101-plus.md` |
| Domain registry | `registry/domains.md` |
| Root registry (named roots, non-primitive anchors) | `registry/roots.md` |
| Colloquial contracted forms | `registry/colloquial.md` |
| Sentence corpus quick-reference index | `corpus/sentences/index.md` |
| Active sentence intake (new sentences here first) | `corpus/sentences/s279-plus.md` |
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
- Modifier precedes head
- **Default compound parse is right-branching:** `A-B-C` = A modifies [B-C]. The `'` juncture marker overrides this: `A'B-C` = [A] modifies [B-C] as a pre-bound unit.

> **Identity-copula gap:** Tonesu currently has no dedicated identity copula (X ≡ Y). `ne` attributes a property — it does not assert constitutional identity. For identity-like claims use property attribution (`la-X  Q`) or relational construction (`lo-X  ne  lo-Y`) as appropriate. Do not invent an equality particle.

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

### Notation characters

| Character | Status | Meaning |
|-----------|--------|---------|
| `'` | **normative — written** | Prosodic juncture marker. Marks the left boundary of a subcompound inside a longer chain. Right-binding: `A'BC` = A modifies [BC]. Minor phrase break in speech; the only non-alphabetic character written in Tonesu. Spec: `spec/phonology.md §Prosodic Juncture Marker`. |
| `~` | **normative — written** | Approximation mark. Pre-positional hedge: "approximately / roughly / on the order of." Always at the left edge of the unit it qualifies. May appear immediately after `'` to hedge only the subcompound. Spoken form: `ven` (G010). Spec: `spec/phonology.md §~ Approximation Mark`. |
| `-` | **analytic only — not written** | Hyphen. Marks morpheme/root boundaries in examples for readability. Never appears in written Tonesu. `to-fe-su-ki` is the analytic form; `tofesuki` is the written form. |
| `[]` | **analytic only — not written** | Square brackets. Mark slot labels, placeholders, or structural groupings in grammar examples (e.g. `la-[agent]`, `[verb-compound]`). Never appear in written Tonesu. |

### Stable identifiers

- Sentence numbers (`S001`, `S349`, …) — never renumber.
- W-numbers (`W000`, `W116`, …) — never renumber. Retired entries keep their numbers.

### Process conventions

- Corpus tests are tracked under batch labels: THO- (theological), GRAM- (grammar), etc. New batches go in `corpus/sentences/s279-plus.md`.
- Open questions are logged in `notes/open-questions.md`. Mark resolved with `[x]` and a brief resolution note; do not delete old entries.
- New derived entries always go into `registry/derived/w101-plus.md` first, then update `registry/derived/index.md` (sections A, B, and C).
