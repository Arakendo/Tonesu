# v3-transition format — Conversion notes

## Era
S176–S397 (5 files: s176-s227, s228-s251, s252-s278, s279-s334, s335-s397)

## Characteristics
- **Headings:** Named batch sections with descriptive titles
  - Early (s176-s278): `## Observer Paradox & Identity Persistence Stress Test (S176–S181)`
  - Later (s279-s334): `## Sermon on the Mount Stress Test (S293–S299) *(MAT-001)*`
  - Latest (s335-s397): `## Grammar Exercise Batch (S335–S341) *(GRM-001)*` and `## Fallacy-Resistance Corpus — Batch: FAL-001`
- **Batch codes:** Transition from implicit to explicit
  - s176-s278: codes in sentence entries `*(OPX-001-A)*` but not in headings
  - s279-s397: codes appear in heading text
- **Code block fields:** Still `Gloss:`, `Literal:`, `Natural:` (same labeled format)
- **Batch summaries:** Appear consistently from s335-s397 onward
- **Multi-sentence batches:** Batches grow to 7-20 sentences (KNM, ODL, GEO, NUM, FAL series)

## Extraction status
- All sentences migrated to `sentences.yaml`
- Batch codes extracted; some batch titles available from headings
- Batch purposes partially available (s335-s397 has `*Batch purpose:*` lines)

## Known issues
- S335-S397 entries with multi-line tonesu (fallacy demos) have complex structure
- Some entries in the FAL series have no `natural` (now backfilled from gloss)
- Heading format inconsistent: some use `*(CODE)*`, some use `— Batch: CODE`
