# v4-current format — Conversion notes

## Era
S398+ (1 active intake file: s398-plus.md)

## Characteristics
- **Headings:** Standardized `## Title (Srange) — Batch: CODE`
- **Batch codes:** Always in heading, always `[DOMAIN]-[NNN]` format
- **Sentence format:** `**S### — English gloss** *(CODE-LETTER)*` followed by fenced code block
- **Code block:** Raw Tonesu notation only (no `Gloss:`, `Literal:`, `Natural:` labels)
- **Notes:** Separate `**Notes:**` section below each sentence
- **Batch summaries:** Consistent `## CODE Batch Summary` tables
- **Batch purpose:** Italicized `*Batch purpose (CODE): ...*` after heading

## Extraction status
- All sentences migrated to `sentences.yaml`
- Batch titles and partial purposes extracted to `batches.yaml`
- `natural` field backfilled from heading gloss text

## Status
This is the **canonical format** for all new work. See `TEMPLATE.md` for the
authoring template. New entries go into `s398-plus.md` first; when it reaches
~50 entries, split per the file-split policy in `.github/copilot-instructions.md`.
