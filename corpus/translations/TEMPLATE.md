# Translation File Template — corpus/translations/

Each file under `corpus/translations/{Category}/` is a standalone translation
analysis document. Files are copied verbatim into the site by `copy_translation_files()`
in `scripts/build_registry.py`. No internal structure is parsed by the pipeline
except: (1) YAML frontmatter (`batch_codes` for linking batch pages to analysis
files), (2) the first `# …` heading (used as the page title), and (3) removal of
empty table columns via `_strip_empty_table_columns`.

**Categories are auto-discovered** from subdirectory names under
`corpus/translations/`. To add a new category, create the folder — no script
changes needed.

**Batch linking is auto-discovered** from `batch_codes` in YAML frontmatter.
Each entry can be a full batch code (`DND-001`) or a prefix (`EXO`). The
pipeline tries exact match first, then prefix. To link a batch page to a
translation analysis file, add `batch_codes` to the file's frontmatter — no
script changes needed.

New translation files go directly in the appropriate category folder
(`Bible/`, `Law/`, `Literature/`, `Philosophy/`, `Science/`, or a new one).
Name the file after the source text: `hamlet-to-be.md`, `john-1-1.md`, etc.

---

## Template

```markdown
---
batch_codes: [PREFIX]
---
# Translation Test: [Source Title]

## Source
[Author, work, edition/version — e.g. "Gospel of John 1:1, NIV (2011)"]

## Status
Draft — first pass

---

## Purpose

[One paragraph: what structural problem(s) this text tests in Tonesu.
Be specific about what is at stake — not just "tests grammar" but which
constructions, particles, or word gaps are under pressure.]

Primary tests:

- [bullet: specific linguistic challenge]
- [bullet: specific linguistic challenge]

Secondary tests:

- [bullet]

Corpus sentences: [S-number range, e.g. S474–S476] ← fill in after writing the batch

---

## Vocabulary Framework

[Prose: explain any new compounds coined or existing compounds repurposed.
Group by semantic role if more than ~4 entries.]

| Form | Reading | Notes |
|------|---------|-------|
| `form` | gloss | source compound, new for this batch, etc. |

---

## Source Text

> [Original text block — for verse analyses, quote in original language if
> available and provide a standard English reading.]

---

## Verse-by-Verse Analysis

### [S-number] — [Source reference] — "[English quotation]"

```
[Tonesu notation — one sentence per block]
```

**Written:** `[notation with hyphens stripped, apostrophes preserved]`

**Parse:**

```
[optional: ASCII parse tree or labeled bracket notation when the parse is
non-obvious; omit for simple 3-slot sentences]
```

**Reading:** "[Natural English reading of the Tonesu sentence]"

**Notes:** [Prose: design decisions, gap references, structural choices,
comparisons to alternatives not chosen. Reference open questions as
`notes/open-questions.md (ISSUE-NNN)`.]

---

[...repeat for each sentence in the batch...]

---

## [CODE]-NNN Batch Summary

| # | English | Tonesu | Notes |
|---|---------|--------|-------|
| S### | [gloss] | `[form]` | new: W-number or — |

**Key finding:** [One sentence: the most important structural insight from
this batch.]

**New vocabulary introduced:** [W-numbers with forms, or "none"]

**Open questions logged:** [ISSUE-NNN references, or "none"]

---

## Colloquial Register Analysis

| Form used | CLQ entry | Colloquial form | Notes |
|-----------|-----------|-----------------|-------|
| `form` | CLQ-NNN | `stub` | one-line note |
| `form` | none | — | reason |

**Verdict:** [one sentence — e.g. "irreducibly formal" or "N stubs applicable: ..."]

*CLQ entries registered from this batch: CLQ-NNN · CLQ-NNN / none.*
```

---

## Field reference

| Field | Required | Pipeline use |
|-------|----------|--------------|
| `# Translation Test: …` H1 | yes | Page title (prefix stripped for display) |
| Source | yes | Not parsed; human reference only |
| Status | yes | Not parsed; human tracking only |
| Purpose | yes | Not parsed; contextual framing |
| Vocabulary Framework table | recommended | Not parsed; `_strip_empty_table_columns` removes all-empty columns |
| Source Text | yes | Not parsed; reader context |
| `**Written:**` line | yes | Not parsed by the translation pipeline; present for reader clarity |
| `**Notes:**` block | yes | Not parsed by the translation pipeline (only parsed by `parse_source_notes()` in *sentence batch* files — this is a translation file, not a batch file) |
| Batch Summary table | yes | Not parsed; human quick-reference |
| Colloquial Register Analysis | yes | Copied verbatim; human-authored; see below |

---

## `Written:` field rules

The `**Written:**` line shows the orthographic form of the Tonesu sentence.
**Strip hyphens only.** Everything else is copied verbatim.

- Remove all `-` hyphens.
- Preserve `'` (prosodic juncture), spaces, and all other characters.
- Do not add diacritics, change letters, or reorder morphemes.

```
Notation:   la-to-li  lo-su-ki
Written:    latoli losuki
```

---

## Colloquial Register Analysis — row rules

Include every new compound first-attested in the batch, plus any operators
that might relax under register shift.

| Case | CLQ entry | Notes column |
|------|-----------|--------------|
| Primitive CV root | none | "Primitive CV root — minimum possible" |
| 2-root compound | none | "2-root — below 3-morpheme contraction threshold" |
| `[X]-no-fe` extremal | none | "`[X]-no-fe` extremal — outside CLQ scope; CLQ-EXT unresolved" |
| Semantically load-bearing operator | none | "semantically load-bearing; relaxation changes the claim" |
| CLQ entry applies | CLQ-NNN | stub form + brief note |

**Verdict criteria:**

- **"irreducibly formal"** — all forms are below threshold, extremal, or load-bearing
- **"N stubs applicable: [list]"** — at least one CLQ entry applies

When a new CLQ entry is registered from this batch, update both
`registry/colloquial.md` (human-readable) and `registry/colloquial.yaml`
(pipeline source).

---

## Naming and registration

1. Name the file after the source text slug: `source-title.md`
2. Place it in the correct category folder (`Bible/`, `Literature/`, `Philosophy/`, `Science/`)
3. Add the batch sentences to `corpus/sentences/v4-current/s549-plus.md` (or current active intake)
4. Add the batch entry to `corpus/batches.yaml`
5. Add sentence entries to `corpus/sentences.yaml`
6. Run `python scripts/build.py` — the file will be copied to `www/docs/totonesu/corpus/translations/{category}/{slug}/index.md`
7. The translations index page (`www/docs/totonesu/corpus/translations/overview.md`) is regenerated automatically
