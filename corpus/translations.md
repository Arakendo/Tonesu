# Translations — Directory Index

Translation analysis files live in `corpus/translations/{Category}/`.
This file is a pointer; it is not used by the pipeline.

---

## Active translation files

| Category | File | Batch | Status |
|----------|------|-------|--------|
| Bible | [exodus-3-1-15.md](translations/Bible/exodus-3-1-15.md) | EXO-001 | draft |
| Bible | [genesis-1.md](translations/Bible/genesis-1.md) | — | draft |
| Bible | [john-1-1.md](translations/Bible/john-1-1.md) | JOH-001 | draft |
| Bible | [last-supper.md](translations/Bible/last-supper.md) | LSP-001 | draft |
| Bible | [matthew-16-25.md](translations/Bible/matthew-16-25.md) | MAT-001 | draft |
| Bible | [matthew-5-7.md](translations/Bible/matthew-5-7.md) | — | draft |
| Bible | [romans-7-19.md](translations/Bible/romans-7-19.md) | ROM-001 | draft |
| Literature | [basho-frog.md](translations/Literature/basho-frog.md) | BSH-001 | draft |
| Literature | [dickinson-death.md](translations/Literature/dickinson-death.md) | DEB-001 | draft |
| Literature | [hamlet-to-be.md](translations/Literature/hamlet-to-be.md) | HAM-001 | draft |
| Literature | [tale-of-two-cities.md](translations/Literature/tale-of-two-cities.md) | — | draft |
| Philosophy | [liar-paradox.md](translations/Philosophy/liar-paradox.md) | LPR-001 | draft |
| Philosophy | [tao-te-ching-ch1.md](translations/Philosophy/tao-te-ching-ch1.md) | TAO-001 | draft |
| Philosophy | [tractatus.md](translations/Philosophy/tractatus.md) | — | draft |
| Science | [newton-first-law.md](translations/Science/newton-first-law.md) | NEW-001 | draft |

---

## Template

See [`corpus/translations/TEMPLATE.md`](translations/TEMPLATE.md) for the
canonical format for new translation analysis files, including:

- File structure (H1, sections, verse-by-verse format)
- `**Written:**` field rules (mechanical hyphen-stripping only)
- Colloquial Register Analysis section (required, appears last)
- CLQ row rules and verdict criteria
- Registration checklist

---

## Pipeline integration

`copy_translation_files()` in `scripts/build_registry.py` copies every `*.md`
under `corpus/translations/{Category}/` verbatim to:

```
www/docs/totonesu/corpus/translations/{category.lower()}/{slug}/index.md
```

The pipeline reads only: (1) the first `# …` heading for the page title, and
(2) runs `_strip_empty_table_columns` on all tables. Internal structure is not
parsed — what you write is what renders.

The `generate_translations_index()` function then regenerates
`www/docs/totonesu/corpus/translations/overview.md` from the collected entries.

