# Corpus YAML Schema

*Status: Normative. Decisions locked in March 2026 (see revision notes at bottom).*

---

## Why this matters

With `registry/entries.yaml` as the word source, the one structural gap is the reverse
direction: given a word, which sentences attest it? A corpus YAML adds `words_attested`
per sentence and `first_attests` for new-word debuts — enabling `build_registry.py` to
render "attested in: S012, S047, S103" on each registry page.

---

## Decided: Tier 1 now, Tier 2 deferred

**Tier 1** — structured fields only; prose Notes stay in `.md` files. The payoff
(registry cross-references) is available immediately; sentence editing stays easy.

**Tier 2** (Markdown replacement) is deferred. Do not migrate until Tier 1 is settled
and the `words_attested` annotation pass is complete.

---

## Finalized field set

```yaml
# ── required fields ──────────────────────────────────────────────────────────

snum:         S001             # Stable S-number. Never reassigned.
gloss:        "Simple action"  # English title from bold header (after the dash).
batch:        null             # Batch code, e.g. GRM-001, EXO-001. null if unbatched.
batch_sub:    null             # Single-letter sub-label (A/B/C) within batch. null if none.

status: normative              # Enum: normative | draft | legacy
                               # legacy = S001–S039 (English placeholders, pre-development)
                               # draft  = any newer sentence not yet considered normative
                               # normative = accepted; default for post-S039 sentences

tonesu: |-                     # Tonesu sentence in notation form (hyphens preserved).
  la-engineer  lo-machine  ka-build  ta-now
                               # Source: the `Gloss:` field in old/middle format,
                               # or the entire fenced block in flat format (S398+).

# ── structured parse fields ───────────────────────────────────────────────────

gloss_line: null               # Morpheme-by-morpheme breakdown with English meanings.
                               # e.g. "agent:engineer  patient:machine  action:build"
                               # Source: the `Literal:` field in old/middle format.
                               # null in flat format (S398+) — not recorded there.

natural: null                  # Fluent English reading.
                               # Source: the `Natural:` field in old/middle format.
                               # null in flat format.

# ── cross-reference fields ────────────────────────────────────────────────────

words_attested: []             # W-numbers used in this sentence. Human-maintained.
                               # Empty list on first migration pass; populated later.

first_attests: []              # DERIVED — never hand-edit.
                               # Computed from attestation order across words_attested.
                               # Feeds registry entries.first_use automatically.

gap_refs: []                   # GAP-xxx / OQ-xxx identifiers referenced in notes.
                               # Extracted by migration script; review as needed.

# ── provenance ────────────────────────────────────────────────────────────────

source_file:   "sentences/s001-s039.md"   # Relative path to source .md file.
source_anchor: "S001"                      # S-number anchor (= snum).

# ── prose linkage (Tier 1 — notes stay in .md) ───────────────────────────────

notes: null                    # Always null in Tier 1. Notes prose stays in .md files.
                               # Tier 2 would populate this as a YAML literal block.
```

### Null discipline

- Singular optional fields: `null` when absent  
- List fields: `[]` when empty (never `null`)  
- Required keys always present (no omission)

This keeps downstream tooling simple and avoids special-case soup.

---

## Full Tier-1 example

```yaml
- snum: S335
  gloss: "Tense: past. The tall tree fell to the ground last season."
  batch: GRM-001
  batch_sub: A
  status: normative
  tonesu: la-be-di'zo-su  ki  lo-ma-pa  ta-ti-de
  gloss_line: agent:growing-directional-plant  moved  patient:soil  at-past-time
  natural: The tall tree fell to the ground last season.
  words_attested: []
  first_attests: []
  gap_refs: []
  source_file: sentences/s335-s397.md
  source_anchor: S335
  notes: null

- snum: S398
  gloss: "Moses shepherded Jethro's flock."
  batch: EXO-001
  batch_sub: A
  status: normative
  tonesu: la-na-Moses  lo-zon  ka-zo-su-ka  ne-na-Yitro
  gloss_line: null
  natural: null
  words_attested: []
  first_attests: []
  gap_refs: []
  source_file: sentences/s398-plus.md
  source_anchor: S398
  notes: null

- snum: S001
  gloss: Simple action
  batch: null
  batch_sub: null
  status: legacy
  tonesu: la-engineer  lo-machine  ka-build  ta-now
  gloss_line: agent:engineer  patient:machine  action:build  time:present
  natural: The engineer builds the machine.
  words_attested: []
  first_attests: []
  gap_refs: []
  source_file: sentences/s001-s039.md
  source_anchor: S001
  notes: null
```

---

## Conversation entries

Conversations (C-series) use a separate `corpus/conversations.yaml` with a turn-list
schema. **Schema is defined here; migration is a later milestone (after S-series Tier 1
is working).**

```yaml
- cnum: C001
  gloss: "First conversation: backup unit failure"
  scene: "The relay platform, shortly after S027."
  tests:
    - content question
    - copula gap
    - W037 ti-fe
    - agent-drop ellipsis
  status: normative
  source_file: conversations/c001-c004.md
  turns:
    - turn: A1
      tonesu: "la-mi  pa-re-mu  lo-de  ka-se-past"
      gloss_line: "agent:I  location:backup-unit  patient:decay  action:perceive-PAST"
      natural: "I found damage in the backup unit."
      words_attested: []
      first_attests: []
      notes: null
    - turn: B1
      tonesu: "de  vo  to-si?"
      gloss_line: "decay  quality  QUERY"
      natural: "What kind of damage?"
      words_attested: []
      first_attests: []
      notes: null
```

The turn `notes` field is null in Tier 1 (same rule as sentences: prose stays in .md).
Conversations have a `tests` list (string tags, not W-numbers) since they test
grammatical constructions rather than vocabulary items.

---

## Translation files

**Do not YAML-ify the translation files.** They are design essays — vocabulary tables,
verse-by-verse analysis, gap documentation, structural rationale. YAML would destroy
their readability and add no structural benefit. They stay as `.md` prose files.

The translation files are already catalogued in `corpus/index.md`.

---

## Proposed folder arrangement

```
corpus/
  sentences.yaml          ← NEW: Tier 1 thin index (S-series)
  conversations.yaml      ← NEW: Tier 1 thin index (C-series)
  sentences/              ← unchanged: human-readable .md files (notes stay here)
    index.md              ← could be generated from sentences.yaml in future
    s001-s039.md
    ...
  conversations/          ← unchanged
    c001-c004.md
    c005-c007.md
  translations/           ← unchanged (design essays, never YAML)
    Bible/
    Science/
    Literature/
    Philosophy/
  index.md                ← could be generated from sentences.yaml in future
```

If Tier 2 (full migration) is chosen later, sentences/ becomes a generated artifact
folder — same pattern as registry/derived/. But that is not required for Tier 1.

---

## Implementation phases

### Phase 1 — Build the skeleton (NOW)

Run `migrate_to_sentences_yaml.py` to produce `corpus/sentences.yaml` with:
- All required fields: `snum`, `gloss`, `batch`, `batch_sub`, `status`
- All parse fields extractable by script: `tonesu`, `gloss_line`, `natural`
- Empty cross-reference lists: `words_attested: []`, `first_attests: []`
- Auto-extracted `gap_refs` (GAP-/OQ- regex from notes)
- Provenance: `source_file`, `source_anchor`

The file is useful immediately even with empty `words_attested`.

### Phase 2 — Wire registry integration

Update `build_registry.py` to consume `sentences.yaml`. Registry pages can show
"attested in: …" once `words_attested` is populated, but the code should tolerate
`words_attested: []` from day one. Partial annotation is not an error.

### Phase 3 — Annotate `words_attested`

Dedicated annotation pass, separate from migration. Not mixed in.
Target: each sentence lists all W-numbers used in that Tonesu form.

### Phase 4 — Derive `first_attests`

Run a script over the sorted `sentences.yaml`: for each W-number, find the lowest
S-number in `words_attested` that contains it. That entry's `first_attests` gets
that W-number. Then feed into `registry/entries.yaml` `first_use` fields.

`first_attests` is **generated, never hand-edited**. Human maintains `words_attested`;
machine derives `first_attests` and `registry entries.first_use`.

### Phase 5 — Migrate conversations

After the S-series pipeline is settled. Separate file (`corpus/conversations.yaml`),
separate migration script.

---

## Source format variants (for the migration script)

Three variants exist across the sentence files:

| Variant | Files | Fenced block | Notes location |
|---------|-------|--------------|----------------|
| Old | s001-s039.md | `Gloss:` + `Literal:` + `Natural:` + `Notes:` all inside | inside block |
| Middle | s040-s397.md | `Gloss:` + `Literal:` + `Natural:` inside | outside as `**Notes:**` |
| Flat | s398-plus.md | raw Tonesu only | outside as `**Notes:**` |

Field mapping from .md to YAML:
- `Gloss:` → `tonesu`
- `Literal:` → `gloss_line`
- `Natural:` → `natural`

The `Literal:` field in .md is the morpheme-meaning breakdown (e.g. `agent:engineer
patient:machine`), NOT a word-order-preserving translation. There is no separate
`literal` field in the YAML schema.

---

## Revision notes

**March 2026** — Schema finalized from draft based on the following decisions:
- Tier 1 confirmed; Tier 2 deferred
- `words_attested` skipped on first migration pass (empty lists are valid)
- `first_attests` is derived/generated, not hand-maintained
- `status: legacy | draft | normative` enum (not `legacy: true` boolean)
- Provenance fields (`source_file`, `source_anchor`) added
- Conversations: schema defined here; migration deferred to Phase 5
- `literal` field removed (was duplicate of `gloss_line` / Literal: in .md)
- Null discipline: `null` for singular optionals, `[]` for list fields
