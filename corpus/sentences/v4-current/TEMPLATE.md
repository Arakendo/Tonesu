# Batch Template — v4-current format

New corpus batches go in `s398-plus.md` (or the current active intake file)
following this exact format. Do not invent variant layouts.

---

## Template

```markdown
## [Title] ([Sfirst]–[Slast]) — Batch: [CODE]

*Batch purpose ([CODE]): [one-sentence description of what this batch tests].*

*New compounds attested this batch: [W-numbers or "none"].*

---

**[Sfirst] — [English gloss]** *([CODE]-A)*

\```
[Tonesu notation, one line]
\```

**Notes:** [optional — parse notes, design decisions, references]

---

**[Sfirst+1] — [English gloss]** *([CODE]-B)*

\```
[Tonesu notation, one line]
\```

**Notes:** [optional]

---

[...repeat for each sentence...]

---

## [CODE] Batch Summary

| # | English | Tonesu | New |
|---|---------|--------|-----|
| [Sfirst] | [gloss] | `[tonesu]` | [new compounds or —] |
| [Sfirst+1] | [gloss] | `[tonesu]` | — |
| ... | ... | ... | ... |

**Coverage:** [what grammar/domain features this batch exercised]

**Gaps:** [any unresolved issues → reference notes/open-questions.md]
```

---

## Field reference

| Field | Required | Description |
|-------|----------|-------------|
| Title | yes | Human-readable batch topic (e.g. "Exodus 3:1–15") |
| Srange | yes | S-number range (e.g. S398–S417) |
| CODE | yes | Batch code: `[DOMAIN]-[NNN]` (e.g. EXO-001, GRM-003) |
| Batch purpose | yes | One sentence: what this batch stress-tests |
| New compounds | yes | W-numbers of compounds first attested here, or "none" |
| Sentence heading | yes | `**S### — English gloss** *(CODE-LETTER)*` |
| Code block | yes | One line of Tonesu notation per sentence |
| Notes | optional | Parse breakdown, design choices, cross-references |
| Batch Summary table | yes | Quick-reference table at end of batch |
| Coverage | yes | What features this batch exercised |
| Gaps | optional | Unresolved issues |

---

## Batch code conventions

- Use uppercase domain prefix: `EXO`, `GRM`, `THO`, `FAL`, `KNM`, etc.
- Three-digit sequence: `-001`, `-002`, etc.
- Sub-batches use the same code with letter suffixes in sentence tags: `EXO-001-A`, `EXO-001-B`
- New domain prefixes should be registered in `registry/domains.md`

---

## After writing the batch

1. Add sentence entries to `corpus/sentences.yaml`
2. Add batch entry to `corpus/batches.yaml` (code, title, theme, purpose)
3. Run `python scripts/build.py` to regenerate site pages
4. Verify the batch page renders at `tonesu/corpus/batches/[CODE]/`

If this batch has a corresponding translation analysis file in `corpus/translations/`:

5. Add a `## Colloquial Register Analysis` section at the **end** of that file.
   See `corpus/translations/TEMPLATE.md` for the row rules, verdict criteria,
   and CLQ registration steps.
