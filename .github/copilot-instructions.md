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
| `corpus/sentences/` | Numbered sentence corpus split into ~50-entry files; `index.md` is the quick-reference. New sentences always go into `s398-plus.md` first. |
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
| Kind-term taxonomy tree (living things + matter) | `registry/kinds.md` |
| Active sentence intake (new sentences here first) | `corpus/sentences/s398-plus.md` |
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

### Quick word construction check

**Pattern: modifier precedes head (head-final, right-branching)**

```
to + li       →  to-li   →  toli      scholar (knowledge-person)
to + ki + mu  →  to-ki-mu  →  tokimu  computer (knowledge-change-device)
no + ha       →  no-ha   →  noha      cold (absence of heat)
```

**Smell-test rules — if any of these trip, go read `spec/word-formation.md`:**

- Inventing a new CV root? Stop — the primitive set is closed. Justify or compound instead.
- Using more than one derivational suffix (`-li`, `-mu`, `-pa`, `-ge`, `-ki`) on one base? Restructure as a compound.
- A compound longer than 4 roots with no `'`? Check whether the parse is still unambiguous.
- A CVC form that isn't a digit, color, or SI prefix? It needs to satisfy the ergonomic shortform criteria.
- A CVCC form? Only for universal constants/units (π, c, ℏ …). No vocabulary words.

### Grammar slots (core sentence frame)

```
la-[agent]  [verb-compound]  lo-[patient]
```

- `la-` agent prefix · `lo-` patient prefix · `lu-` result/beneficiary
- `ne` copula (property attribution) · `go` causal/origin particle
- Modifier precedes head
- **Default compound parse is right-branching:** `A-B-C` = A modifies [B-C]. The `'` juncture marker overrides this: `A'B-C` = [A] modifies [B-C] as a pre-bound unit.

> **Identity copula:** `ne` attributes a property — it does not assert constitutional identity. For neutral identity-like claims use property attribution (`la-X  Q`) or relational construction (`lo-X  ne  lo-Y`). Do not invent a new equality particle. `helms` (spoken/written form of `::`, G012) is available as an explicit identity predicate (`X helms Y` = X is by definition Y) in poetic and philosophical register, following the `ven` precedent (spec/phonology.md). This is the strongest identity claim available; reserve for contexts where strict definitional equality is intended. `helm` (spoken/written form of `:`, G011) is the intermediate form: `X helm Y` = X is functionally understood as Y (explanatory reading, softer than `helms`). Three-way distinction: `ne` (property) < `helm` (functional equivalence) < `helms` (strict identity).

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
| `'` | **normative — written** | Prosodic juncture marker. Marks the left boundary of a subcompound inside a longer chain. Right-binding: `A'BC` = A modifies [BC]. Minor phrase break in speech. Spec: `spec/phonology.md §Prosodic Juncture Marker`. |
| `~` | **normative — written** | Approximation mark. Pre-positional hedge: "approximately / roughly / on the order of." Always at the left edge of the unit it qualifies. May appear immediately after `'` to hedge only the subcompound. Spoken form: `ven` (G010). **`ven` is a valid written substitute for `~`** wherever the symbol is unavailable or a word-form is preferred. Spec: `spec/phonology.md §~ Approximation Mark`. |
| `-` | **analytic only — not written** | Hyphen. Marks morpheme/root boundaries in examples for readability. Never appears in written Tonesu. `to-fe-su-ki` is the analytic form; `tofesuki` is the written form. |
| `[]` | **normative — written** | Aside / commentary frame. In written Tonesu: wraps editorial or analytic annotation that does not alter truth conditions of surrounding text. Removal invariance: stripping all `[]` must leave the argument unchanged. Self-policing: may not upgrade evidential status or silently rewrite the core claim. Never appears in spec/grammar *analytic* notation (that role now belongs to `{}`). Legacy spec text may use `[]` analytically; those occurrences are grandfathered. Spec: `spec/phonology.md §[] — Aside / Commentary Frame`; `spec/grammar.md §Aside / Commentary Frame`. |
| `{}` | **analytic only — not written** | Spec/grammar analytic notation. Marks slot placeholders (`la-{agent}`), subordinate clause scope (`go {premise}  result`), and structural groupings in grammar examples and registry entries. Never appears in running Tonesu text. Going-forward convention; legacy `[]` analytic uses in older spec text are grandfathered. |
| `()` | **normative — written** | Evidential frame. Wraps a declarative clause to mark its content as reported, inferred, or unattributed — not directly asserted. Stackable with `~`: `~(clause)` = approximately/reportedly. Spoken forms: `kelm` (G014, open bracket) and `kelms` (G015, close bracket). **`kelm` and `kelms` are valid written substitutes** for `(` and `)` wherever the symbols are unavailable or word-forms are preferred. Spec: `spec/phonology.md §() — Evidential Frame`; `spec/grammar.md §Evidential Frame`. |
| `:` | **normative — written (sentence); metalanguage (definition)** | Sentence-initial topic frame: `[topic-NP] : [comment-clause]` = "as for [topic], ...". Also used as explanatory definition mark in metalanguage (`term : reading`). One per clause; sentence-initial only. Spoken form: `helm` (G011). **`helm` is a valid written substitute for `:`** wherever the symbol is unavailable or a word-form is preferred; also usable as an in-sentence predicate in poetic/philosophical register (`X helm Y` = X is functionally understood as Y). Spec: `spec/phonology.md §: and :: — Definition and Topic Marks`; `spec/grammar.md §Topic Frame`. |
| `::` | **metalanguage (definition)** | Canonical/structural definition mark. Right-hand side gives formal decomposition (`term :: roots`). Appears in written and verbal discourse. Spoken form: `helms` (G012, CVCCS tier). **`helms` is a valid written substitute for `::`** wherever the symbol is unavailable or a word-form is preferred; also usable as an in-sentence identity predicate in poetic/philosophical register (`X helms Y` = X is by definition Y). Spec: `spec/phonology.md §: and :: — Definition and Topic Marks`. |
| `/` | **normative — written** | Parallel partition mark. Marks the structural midpoint of a bi-clausal parallel or antithetical construction — the two flanking clauses are formally paired. Does not specify the relationship type (antithetical, complementary, premise/result); content supplies that. Spoken form: `vel` (G013). **`vel` is a valid written substitute for `/`** wherever the symbol is unavailable or a word-form is preferred. Spec: `spec/phonology.md §/ — Parallel Partition`; `spec/grammar.md §Bi-Clausal Parallel Construction`. |

### Stable identifiers

- Sentence numbers (`S001`, `S349`, …) — never renumber.
- W-numbers (`W000`, `W116`, …) — never renumber. Retired entries keep their numbers.

### Process conventions

- Corpus tests are tracked under batch labels: THO- (theological), GRAM- (grammar), etc. New batches go in `corpus/sentences/s398-plus.md`.
- Open questions are logged in `notes/open-questions.md`. Mark resolved with `[x]` and a brief resolution note; do not delete old entries.
- New derived entries always go into `registry/derived/w101-plus.md` first, then update `registry/derived/index.md` (sections A, B, and C).

---

## Website editorial conventions (`www/`)

The website (`www/docs/`) is a public-facing showcase of Tonesu. The following rules apply to all website content:

### Written form is primary; analytic form is the annotation

- **Written Tonesu** has no hyphens. `tofesuki` is the word; `to-fe-su-ki` is the parse breakdown.
- In tables, the primary column shows the written form (e.g. `toli`). A **Parse** column shows the analytic breakdown (e.g. `to-li`).
- In prose, introduce a compound as: `toli (to-li)` — written form first, analytic in parentheses.
- In code blocks showing sentence examples, lead with the written sentence; show the analytic breakdown below labeled as parse.
- Pattern template labels (`X-li`, `X-mu`, `no-X`, etc.) are analytic notation describing the productive pattern — they are always analytic and stay hyphenated.
- Construction-reasoning code blocks (showing step-by-step parse derivation) may use analytic notation throughout; the final named result should show the written form.
- Particles `la-`, `lo-`, `lu-` are prefixes: in written Tonesu they attach without hyphen (`latoli`, `lotosu`). Standalone particles (`ne`, `go`, `du`, `wi`, `ro`, `pa`, `ta`, `na`) are separate words; no hyphen.

### Written-form quick reference

Strip hyphens: `to-li` → `toli` · `ra-ki-mu` → `rakimu` · `to-no-fe` → `tonofe` · `pawi'kasu` (juncture `'` is normative, stays) · `la-toli` → `latoli` · `lo-tosu` → `lotosu`.

---

## Translation file conventions (`corpus/translations/`)

### `Written:` fields are mechanical hyphen-stripping only

The `Written:` line in a translation file entry shows the orthographic form of the Tonesu sentence — the notation form with hyphens removed and apostrophes preserved. **Nothing else changes.**

Rules:
- Remove all hyphens. Every other character is copied verbatim.
- Preserve `'` (prosodic juncture). Preserve spaces between words.
- Do **not** add, remove, or alter any letters.
- Do **not** apply diacritics, accents, or any phonological smoothing.
- Do **not** interpret the token as a natural-language word. It is a formal symbol.

Correct derivation:
```
Notation:   ka-zo-ra-ma  lo-ka-du-zo-su
Written:    kazorama lokaduzosu
```

Wrong (model hallucination pattern to avoid):
```
Written:    kazozarma          ← letters dropped/transposed
Written:    tokoarème          ← diacritics invented, French-style ending hallucinated
Written:    kazozorama         ← morpheme accidentally doubled
Written:    louduzousu         ← vowels inserted mid-token
```

The analytic/notation form (`ka-zo-ra-ma`) is always the source of truth. If the `Written:` field and the notation form disagree, the notation form wins and the `Written:` field must be corrected.
