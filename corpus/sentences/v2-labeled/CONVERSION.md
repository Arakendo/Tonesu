# v2-labeled format — Conversion notes

## Era
S040–S175 (3 files: s040-s071, s072-s100, s101-s175)

## Characteristics
- **Headings:** Named sections, no batch codes in headings
- **Batch codes:** Appear in individual sentence entries as `*(T-XX-NNN)*`
- **Sentence format:** `**S### — English gloss**` followed by fenced code block
- **Code block fields:** `Gloss:`, `Literal:`, `Natural:` (same labeled format as v1)
- **Has:** Batch summary sections begin appearing in s040-s071 and s072-s100
- **T-prefix codes:** `T-XX-NNN` (e.g. T-HA-001, T-MYS-003, T-CMP-002)

## Extraction status
- All sentences migrated to `sentences.yaml`
- Batch codes extracted into per-sentence `batch` field
- No batch-level titles or purposes available from headings

## Known issues
- Some files contain multi-part entries (S112, S113, S153) with English interleaved in tonesu field
- T-prefix batch codes are mostly singletons (1 sentence each)
