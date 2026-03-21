# Pipeline Rework Plan

*Created: 2026-03-20*
*Status: Phase 5 complete — Phase 4 remaining (deferred)*

---

## Problem statement

Every time a new batch is filed, 5–7 files must be updated in exact parallel. When any step is missed, the pipeline silently drops content. Recent examples:

- **Law translation category** — `TRANS_CATEGORIES` and `BATCH_TRANSLATION_MAP` in `build_registry.py` were not updated when `corpus/translations/Law/` was created. CDA and ACA translation pages were invisible on the site until manually wired.
- **Open questions** — resolved items left unchecked because the update step was forgotten during a multi-file commit.
- **Sentence/batch dual entry** — every sentence is authored in the `.md` source file and then manually transcribed into `sentences.yaml`. Every batch header is authored in the `.md` and then manually transcribed into `batches.yaml`. This is the most labour-intensive duplication.

---

## Current data flow

| Data type | Source of truth | Generated from it | Direction |
|---|---|---|---|
| Registry entries | `entries.yaml` | → `registry/derived/*.md` (Step 1) | YAML → MD (automated) |
| Sentences | `s398-plus.md` (hand-authored) | → manual copy into `sentences.yaml` | MD → YAML (manual) |
| Batches | `s398-plus.md` batch headers | → manual copy into `batches.yaml` | MD → YAML (manual) |
| Conversations | `c008-plus.md` (hand-authored) | → manual copy into `conversations.yaml` | MD → YAML (manual) |
| Colloquial | `colloquial.md` AND `colloquial.yaml` | both maintained by hand | dual source (manual) |
| Translations | `corpus/translations/{Cat}/*.md` | → copied to site by `copy_translation_files()` | MD → site (automated) |
| Translation wiring | hardcoded `BATCH_TRANSLATION_MAP` + `TRANS_CATEGORIES` in `build_registry.py` | — | must be updated manually per new batch/category |

The two automated paths (registry YAML→MD and translation MD→site) work well. Everything else requires manual parallel updates that are easy to miss.

---

## Current pipeline steps (`scripts/build.py`)

| Step | Script | Reads | Writes |
|---|---|---|---|
| 0 | `extract_sentences.py` | `corpus/sentences/v4-current/*.md`, existing `sentences.yaml` | `sentences.yaml` |
| 0 | `extract_batches.py` | `sentences.yaml`, `corpus/sentences/**/*.md`, existing `batches.yaml` | `batches.yaml` |
| 1 | `generate_registry_md.py` | `entries.yaml` | `registry/derived/*.md`, `registry/derived/index.md` |
| 2 | `annotate_words_attested.py` | `entries.yaml`, `sentences.yaml`, `conversations.yaml` | `sentences.yaml`, `conversations.yaml` (words_attested fields) |
| 3 | `derive_first_attests.py` | `sentences.yaml`, `conversations.yaml`, `entries.yaml` | `sentences.yaml`, `conversations.yaml` (first_attests), `entries.yaml` (first_use backfill) |
| 4 | `build_registry.py` | `entries.yaml`, `primitives.yaml`, `colloquial.yaml`, `sentences.yaml`, `batches.yaml`, `conversations.yaml`, `corpus/translations/` | all `www/docs/` pages |
| 5 | `mkdocs build` | `www/docs/`, `mkdocs.yml` | `site/` |

---

## Proposed phases

### Phase 1 — Eliminate hardcoded lookup tables

**Goal:** Fix the "forgot to register Law" class of bugs.
**Risk:** Near zero — pure improvement, no format changes.

#### 1a. Auto-discover `TRANS_CATEGORIES`

Replace the hardcoded list in `build_registry.py`:

```python
# BEFORE (hardcoded — must be updated when a new category folder is created)
TRANS_CATEGORIES = ["Bible", "Law", "Literature", "Philosophy", "Science"]

# AFTER (auto-discovered from filesystem)
TRANS_CATEGORIES = sorted(
    d.name for d in TRANS_SRC.iterdir()
    if d.is_dir() and not d.name.startswith(".")
)
```

#### 1b. Auto-discover `BATCH_TRANSLATION_MAP`

Each translation `.md` file contains its batch code in the content (e.g., `Batch purpose (EXO-001`). Two options:

**Option A — YAML frontmatter** (preferred): Add a frontmatter block to each translation `.md`:

```yaml
---
batch_prefix: EXO
---
# Translation Test: Exodus 3:1–15
```

Script scans all translation files, reads frontmatter, builds the map automatically.

**Option B — Content scan**: Regex-scan translation files for `Batch purpose ({CODE}-` and extract the prefix. No file changes needed, but more fragile.

#### 1c. Consolidate theme classification

The `batch_to_theme()` function and its prefix sets are duplicated between `build_registry.py` and `extract_batches.py`. Consolidate:

- Move the shared logic into a `scripts/shared.py` module, or
- Have `build_registry.py` read `batches.yaml`'s `theme:` field (already present) instead of re-deriving it

---

### Phase 2 — Extract `sentences.yaml` from MD source

**Goal:** Author sentences once in the `.md` file; derive `sentences.yaml` automatically.
**Risk:** Medium — parser must handle formatting variations in v4-current.

#### What the parser extracts

The v4-current sentence format is highly structured:

```markdown
**S398 — Moses shepherded Jethro's flock.** *(EXO-001-A)*

\```
la-na-Moses  lo-zon  ka-zo-su-ka  ne-na-Yitro
\```

**Written:** ...
**Natural reading:** ...
**Notes:** ...
```

Fields to extract per sentence:

| YAML field | Extracted from |
|---|---|
| `snum` | `**S398 — ` header |
| `gloss` | text after `—` in header |
| `batch` | parenthetical batch code `(EXO-001-A)` → `EXO-001` |
| `batch_sub` | sub-label from batch code → `A` |
| `status` | default `normative` for v4 |
| `tonesu` | code block content |
| `gloss_line` | `**Gloss:**` or absent (many v4 sentences omit this) |
| `natural` | `**Natural reading:**` line |
| `notes` | `**Notes:**` content |
| `source_file` | derived from which `.md` file was parsed |
| `source_anchor` | derived from S-number |

Fields NOT extracted (computed by later pipeline steps):
- `words_attested` — Step 2 (`annotate_words_attested.py`)
- `first_attests` — Step 3 (`derive_first_attests.py`)
- `gap_refs` — currently hand-populated where present

#### Legacy sentence handling

Sentences in `v1-legacy/`, `v2-labeled/`, `v3-transition/` have different formats. Strategy: **freeze their YAML entries as-is.** The extraction script only processes `v4-current/*.md`. On each run:

1. Load existing `sentences.yaml`
2. Keep all entries with `source_file` pointing to v1/v2/v3 unchanged
3. Re-extract all entries from v4-current `.md` files
4. Merge and write

#### New pipeline step

Insert as **Step 0** in `build.py`:

| Step | Script | Reads | Writes |
|---|---|---|---|
| 0 | `extract_sentences.py` | `corpus/sentences/v4-current/*.md` | `sentences.yaml`, `batches.yaml` |

Steps 1–5 remain unchanged. The extraction step runs first and produces the YAML that downstream steps consume.

---

### Phase 3 — Extract `batches.yaml` from MD source

**Goal:** Derive batch metadata from the sentence source files instead of maintaining it as a separate manual file.
**Risk:** Low — comes naturally from Phase 2.

`extract_batches.py` already exists and does most of this. Changes needed:

- Wire it into `build.py` as part of Step 0 (or fold its logic into `extract_sentences.py`)
- Remove the duplicated theme-classification logic from `build_registry.py`; read `batches.yaml`'s `theme:` field instead

Batch metadata derivable from the sentence `.md` files:
- `code` — from batch labels on sentences
- `title` — from `##` section headers
- `theme` — from prefix classification (one shared function)
- `range` — from min/max S-numbers in the batch
- `count` — from number of sentences in the batch

---

### Phase 4 — Extract `conversations.yaml` from MD source

**Goal:** Author conversations once in the `.md` file; derive `conversations.yaml` automatically.
**Risk:** Medium — conversations have more complex structure.

Conversation `.md` files have structured format:

```markdown
### C008 — Arbitration hearing: `ze` under competing person and proposition referents

**Scene:** ...
**Tests:** ...

**A1**
\```
la-ze  de  lo-si-de  ta-ti-de
\```
Gloss: ...
Natural: ...
Notes: ...
```

Fields to extract per conversation:
- `cnum`, `gloss`, `scene`, `tests`, `status`, `source_file`
- Per turn: `turn`, `tonesu`, `gloss_line`, `natural`, `notes`

Computed fields (`words_attested`, `first_attests`) remain pipeline-derived.

---

### Phase 5 — Unify colloquial sources

**Goal:** Single source of truth for colloquial entries.
**Risk:** Low.

Currently `colloquial.md` and `colloquial.yaml` must both be updated whenever a CLQ entry changes. Since `colloquial.yaml` is already the pipeline source (`build_registry.py` reads it), the natural fix is:

- Add a `generate_colloquial_md.py` script (or fold it into `generate_registry_md.py`)
- Generate `colloquial.md` from `colloquial.yaml`, same pattern as `registry/derived/*.md`
- `colloquial.yaml` becomes the sole source; `colloquial.md` becomes generated

---

## Effort estimates

| Phase | Description | Effort | Dependencies |
|---|---|---|---|
| **1** | Auto-discover categories + translation map + consolidate themes | Small | None |
| **2** | Extract `sentences.yaml` from MD | Medium | None |
| **3** | Extract `batches.yaml` from MD | Small | Phase 2 |
| **4** | Extract `conversations.yaml` from MD | Medium | None |
| **5** | Generate `colloquial.md` from YAML | Small | None |

**Recommended order:** Phase 1 → Phase 2 → Phase 3 → Phase 5 → Phase 4

Phase 1 has the highest value-to-effort ratio and directly prevents the most recent class of bugs. Phase 2+3 together eliminate the most painful manual duplication (sentences + batches). Phase 5 is a quick win. Phase 4 can wait since conversations are authored less frequently.

---

## Post-rework pipeline

After all phases, the pipeline would be:

| Step | Script | Reads (source of truth) | Writes (derived) |
|---|---|---|---|
| 0 | `extract_corpus.py` | `corpus/sentences/v4-current/*.md`, `corpus/conversations/*.md` | `sentences.yaml`, `conversations.yaml`, `batches.yaml` |
| 1 | `generate_registry_md.py` | `entries.yaml` | `registry/derived/*.md`, `registry/derived/index.md` |
| 1b | `generate_colloquial_md.py` | `colloquial.yaml` | `registry/colloquial.md` |
| 2 | `annotate_words_attested.py` | `entries.yaml`, `sentences.yaml`, `conversations.yaml` | `sentences.yaml`, `conversations.yaml` |
| 3 | `derive_first_attests.py` | `sentences.yaml`, `conversations.yaml`, `entries.yaml` | `sentences.yaml`, `conversations.yaml`, `entries.yaml` |
| 4 | `build_registry.py` | all YAML + `corpus/translations/` (auto-discovered) | all `www/docs/` pages |
| 5 | `mkdocs build` | `www/docs/`, `mkdocs.yml` | `site/` |

**Key change:** The hand-authored `.md` files become the sole source of truth for corpus content. YAML files become intermediate build artifacts (still committed to the repo for tooling and GitHub browsing, but generated rather than hand-maintained). Hardcoded lookup tables in scripts are replaced with filesystem discovery.

---

## Files that would need changes

### Phase 1
- `scripts/build_registry.py` — replace `TRANS_CATEGORIES` and `BATCH_TRANSLATION_MAP` with auto-discovery; optionally read theme from `batches.yaml`
- `corpus/translations/*.md` — add YAML frontmatter with `batch_prefix` (Option A only)
- `scripts/extract_batches.py` — consolidate shared theme logic or remove duplication

### Phase 2
- New: `scripts/extract_sentences.py`
- `scripts/build.py` — add Step 0
- `.github/copilot-instructions.md` — update workflow documentation

### Phase 3
- Fold into `extract_sentences.py` or wire `extract_batches.py` into Step 0
- `scripts/build_registry.py` — read theme from `batches.yaml` instead of re-deriving

### Phase 4
- New: `scripts/extract_conversations.py` (or fold into `extract_corpus.py`)
- `scripts/build.py` — extend Step 0

### Phase 5
- New: `scripts/generate_colloquial_md.py` (or extend `generate_registry_md.py`)
- `scripts/build.py` — add as Step 1b
- `.github/copilot-instructions.md` — remove "update both colloquial.md and colloquial.yaml" instruction

---

## Checklist for implementation

- [x] **Phase 1a** — Auto-discover `TRANS_CATEGORIES` from filesystem *(2026-03-20)*
- [x] **Phase 1b** — Auto-discover `BATCH_TRANSLATION_MAP` from translation file frontmatter *(2026-03-20)*
- [x] **Phase 1c** — Consolidate `batch_to_theme()` logic (single source → `scripts/theme.py`) *(2026-03-20)*
- [x] **Phase 2** — Write `extract_sentences.py` parser for v4-current format *(2026-03-22)*
- [x] **Phase 2** — Wire extraction into `build.py` as Step 0 *(2026-03-22)*
- [x] **Phase 2** — Verify roundtrip: extract → annotate → derive → build produces identical output *(2026-03-22)*
- [x] **Phase 3** — Derive `batches.yaml` from extracted sentence data *(2026-03-21)*
- [ ] **Phase 4** — Write conversation extraction parser
- [x] **Phase 5** — Generate `colloquial.md` from `colloquial.yaml` *(2026-03-21)*
- [x] Update `.github/copilot-instructions.md` to reflect new workflow *(2026-03-21)*
- [x] Update `planning/pipeline-rework.md` status as phases complete *(2026-03-21)*
- [x] Audit and rotate `corpus/conversations/TEMPLATE.md` to v2 *(2026-03-21)*
