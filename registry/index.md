# Registry

## Status: Normative

The registry is the authoritative vocabulary ledger. Every word in the language has an entry here (or in the corpus, pending registration).

---

## Entry Counts (March 2026)

| File | Entries | Notes |
|------|---------|-------|
| [primitives.md](primitives.md) | 34 | Closed or near-closed set. Changes are breaking. |
| [roots.md](roots.md) | 34 | One root per primitive; some roots have no registered compound family yet. |
| [domains.md](domains.md) | 8 | Conceptual domain declarations. |
| [derived/](derived/index.md) | 136 W-entries | Active compounds, proposed candidates, and cold entries. |

---

## Files

- **[primitives.md](primitives.md)** — The foundational semantic atoms. Validation rules, entry format, and the full starter set. Changes here are breaking changes to the entire language.
- **[roots.md](roots.md)** — Phonetic root assignments, one per primitive. Includes the root form, gloss, and cross-reference to its primitive entry.
- **[domains.md](domains.md)** — Declared conceptual domains. Each domain unlocks a family of derived compounds.
- **[derived/](derived/index.md)** — All compound vocabulary. Split into range files for manageability.

---

## Status Vocabulary

| Status | Meaning |
|--------|---------|
| `active` | In use; at least two independent corpus attestations |
| `proposed` | Registered but pending corpus validation |
| `cold` | Proposed, zero corpus attestations; held for review |
| `accepted` | Formally ratified beyond active (used for primitives) |
