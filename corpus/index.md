# Corpus

## Status: Draft

The corpus is the worked example set for Tonesu. Sentences are the primary tool for testing whether the spec is sufficient: if a sentence requires a construct not covered by the spec, that is a design gap, not a corpus error.

---

## How to Read Entries

Each sentence entry follows this format:

```
**S[number] — [English gloss]** *(batch-code)*

Tonesu:    the Tonesu sentence
Gloss:     word-by-word breakdown
Notes:     construction notes, decisions, cross-references
```

Conversation entries (C-series) use a multi-turn format with `A:` / `B:` turn markers and per-turn analysis blocks.

---

## Files

### Sentences

| File | Range | Contents |
|------|-------|----------|
| [sentences/s001-s039.md](sentences/s001-s039.md) | S001–S039 | Foundational: basic sentences, early stress tests, narrative scene, primitive property tests |
| [sentences/s040-s071.md](sentences/s040-s071.md) | S040–S071 | Compound and suffix tests: X-X repetition, compound grouping, suffix-root collision, ne-fe generality, comparative, containment |
| [sentences/s072-s100.md](sentences/s072-s100.md) | S072–S100 | Domain probes: mystic, religious, kinship + wi-to stress test |
| [sentences/s101-s175.md](sentences/s101-s175.md) | S101–S175 | Grammar validation: head-final clauses, phonology, counterfactuals, affective substrate, model-domain, predication, aspect, bilateral coordination |
| [sentences/s176-plus.md](sentences/s176-plus.md) | S176+ | Advanced: identity persistence, moral/metaphysical, physics, bilateral interaction gaps |

### Conversations

| File | Contents |
|------|----------|
| [conversations/c001-c004.md](conversations/c001-c004.md) | C001–C004: early multi-turn dialogues (engineering, epistemic, resonance) |
| [conversations/c005-c007.md](conversations/c005-c007.md) | C005: Theological Debate · C006: Question Battery · C007: Epistemic Testimony |

### Other

| File | Contents |
|------|----------|
| [translations.md](translations.md) | Known-text translations for external validation |

---

## Sentence Numbering

Sentence numbers (S-series) are assigned sequentially and never reassigned. A gap in numbering means the sentence was removed — the slot stays empty. Retroactive gap records (e.g. S193 Biology Gap) are never given an S-number of their own; they describe what the gap sentence would have needed.
