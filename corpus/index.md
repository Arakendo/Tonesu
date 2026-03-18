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
| [sentences/s176-s227.md](sentences/s176-s227.md) | S176–S227 | Observer paradox · identity persistence · moral/metaphysical · physics/math · bilateral gaps · temporal anchor · kind-term naming · daily life |
| [sentences/s228-s251.md](sentences/s228-s251.md) | S228–S251 | Geometric constructs (GEO-001) · cardinal numerals (NUM-001) |
| [sentences/s252-s278.md](sentences/s252-s278.md) | S252–S278 | Cat-family taxonomy (KNM-003) · canid-family (KNM-004) · legal theory epistemics (LGL-001) |
| [sentences/s279-s334.md](sentences/s279-s334.md) | S279–S334 | KNM-005 bird taxonomy · PLT-001 plants · MAT-001/002 rock/soil/water · KNM-006–008 fish/ungulates/arthropods · FNG-001 fungi |
| [sentences/s335-s397.md](sentences/s335-s397.md) | S335–S397 | GRM-001/002 grammar · THO-001 divine attributes · GOD-RES · FAL-001–007 fallacy corpus |
| [sentences/s398-plus.md](sentences/s398-plus.md) | S398+ | EXO-001 · LSP-001 · FMQ-001 · JOH-001 · NEW-001 · ROM-001 · DKN-001 · MTH-001 · WIT-001 · HAM-001 · LPR-001 · BSH-001 · EMD-001/002 · TAO-001 · SCL-001/002 · VPT-001 · VPC-001 · CVP-001 · COR-001 *(ongoing)* |

### Conversations

| File | Contents |
|------|----------|
| [conversations/c001-c004.md](conversations/c001-c004.md) | C001–C004: early multi-turn dialogues (engineering, epistemic, resonance) |
| [conversations/c005-c007.md](conversations/c005-c007.md) | C005: Theological Debate · C006: Question Battery · C007: Epistemic Testimony |

### Bible Translations

| File | Scope |
|------|-------|
| [translations/Bible/genesis-1.md](translations/Bible/genesis-1.md) | Genesis 1:1–31 |
| [translations/Bible/matthew-5-7.md](translations/Bible/matthew-5-7.md) | Matthew 5–7 (Sermon on the Mount) |
| [translations/Bible/exodus-3-1-15.md](translations/Bible/exodus-3-1-15.md) | Exodus 3:1–15 |
| [translations/Bible/last-supper.md](translations/Bible/last-supper.md) | The Last Supper |
| [translations/Bible/john-1-1.md](translations/Bible/john-1-1.md) | John 1:1 |
| [translations/Bible/romans-7-19.md](translations/Bible/romans-7-19.md) | Romans 7:19 |
| [translations/Bible/matthew-16-25.md](translations/Bible/matthew-16-25.md) | Matthew 16:25 |

### Science Translations

| File | Scope |
|------|-------|
| [translations/Science/newton-first-law.md](translations/Science/newton-first-law.md) | Newton's First Law of Motion |

### Literature Translations

| File | Scope |
|------|-------|
| [translations/Literature/tale-of-two-cities.md](translations/Literature/tale-of-two-cities.md) | A Tale of Two Cities — opening |
| [translations/Literature/hamlet-to-be.md](translations/Literature/hamlet-to-be.md) | Hamlet — "To be, or not to be" |
| [translations/Literature/basho-frog.md](translations/Literature/basho-frog.md) | Bashō — The Frog Haiku |
| [translations/Literature/dickinson-death.md](translations/Literature/dickinson-death.md) | Emily Dickinson — "Because I could not stop for Death" |

### Philosophy Translations

| File | Scope |
|------|-------|
| [translations/Philosophy/tractatus.md](translations/Philosophy/tractatus.md) | Wittgenstein, Tractatus §1 |
| [translations/Philosophy/liar-paradox.md](translations/Philosophy/liar-paradox.md) | The Liar Paradox |
| [translations/Philosophy/tao-te-ching-ch1.md](translations/Philosophy/tao-te-ching-ch1.md) | Tao Te Ching, Chapter 1 |

### Other

| File | Contents |
|------|----------|
| [translations.md](translations.md) | Legacy translations index (pre-subfolder era) |

---

## Sentence Numbering

Sentence numbers (S-series) are assigned sequentially and never reassigned. A gap in numbering means the sentence was removed — the slot stays empty. Retroactive gap records (e.g. S193 Biology Gap) are never given an S-number of their own; they describe what the gap sentence would have needed.
