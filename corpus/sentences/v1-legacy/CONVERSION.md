# v1-legacy format — Conversion notes

## Era
S001–S039 (1 file)

## Characteristics
- **Headings:** Topic-based `##` (e.g. `## Basic Sentences`, `## Narrative Scene`)
- **No batch codes** in headings — sentences belong to no named batch
- **Sentence format:** `**S### — English gloss**` followed by fenced code block
- **Code block fields:** `Gloss:`, `Literal:`, `Natural:`, `Notes:` (labeled lines inside ```)
- **Has:** T-prefix codes in some sentence entries (e.g. `(T-PHN-001)`)
- **File preamble:** `## Status: Draft`, `## How to Use This File`, `## Sentence Structure Reminder`

## Extraction status
- All sentences migrated to `sentences.yaml` via `scripts/archive/migrate_to_sentences_yaml.py`
- `Gloss:` → `gloss_line`, `Natural:` → `natural`, `Notes:` → `notes` (partially)
- Batch metadata: none available (no batch headings in source)

## Known issues
- Some sentences have English words in `tonesu` field (pre-vocabulary era)
- Some entries reference compounds that were later renamed or retired
