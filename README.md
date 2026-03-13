# Tonesu

A personal study project designing a phonetic, semantically compositional, domain-extensible language.

The language is called **Tonesu** — the casual contraction of the formal compound `to-ne-su` (pattern – relation – structure). The name is itself a demonstration of the dual-register design: a compositional root compound that contracts into a natural spoken form.

## Core Goals

- **Phonetically simple:** globally pronounceable, one letter per sound, fixed stress
- **Compositionally transparent:** words are built from audible conceptual parts, not memorized atoms
- **Domain-extensible:** new conceptual fields emerge by combining existing primitives; the language doesn't break when knowledge expands
- **Minimal irregularity:** grammar and morphology are regular by default; exceptions require justification

## Structure

```
spec/           Normative rules — changes here are real language changes
registry/       Data registries — roots, domains, vocabulary instances
corpus/         Test sentences and translations — the language proves itself here
notes/          Research, prior art, open questions, design rationale
```

## Where to Start

| If you want to... | Go to |
|-------------------|-------|
| See the core design commitments | [spec/principles.md](spec/principles.md) |
| Understand the sound system | [spec/phonology.md](spec/phonology.md) |
| Understand sentence structure | [spec/grammar.md](spec/grammar.md) |
| Understand word-level structure | [spec/morphology.md](spec/morphology.md) |
| Understand how words are built | [spec/word-formation.md](spec/word-formation.md) |
| See the primitive roots | [registry/primitives.md](registry/primitives.md) |
| See the registered vocabulary | [registry/derived.md](registry/derived.md) |
| Test the language in use | [corpus/sentences.md](corpus/sentences.md) |
| See open design questions | [notes/open-questions.md](notes/open-questions.md) |
| See background theory | [notes/basics.md](notes/basics.md) |

## Key Design Tension

Phonetic simplicity and semantic transparency partially conflict. Natural languages drift away from transparency because short efficient sounds beat fully descriptive forms in daily use. This project resolves that tension with a **dual-register design**: a formal layer (transparent compounds) and a casual layer (contracted everyday forms derived from formal compounds). Think of it as source code versus compiled shorthand.

## Development Sequence

The recommended order — each step must be stable before the next is meaningful:

- [x] 0. Structure and scaffolding
- [x] 1. `spec/principles.md` — lock core design commitments
- [ ] 2. `spec/phonology.md` — finalize phoneme inventory, syllable shape, stress, orthography, long vowel decision
- [ ] 3. `spec/grammar.md` — finalize clause structure, role markers, particles, modifier placement, questions, negation
- [ ] 4. `spec/morphology.md` — finalize derivation rules, tense/aspect, plurality, possession, nominalizations
- [ ] 5. `registry/primitives.md` — define first 20–30 roots with strict entry format *(this is the real foundation)*
- [ ] 6. `corpus/sentences.md` — 20–40 smoke-test sentences covering ownership, identity, action, description, time, place, one technical example
- [ ] 7. `registry/roots.md` and `registry/derived.md` — only after primitives and corpus are stable

*Do not fill the registry before step 5 is complete. Vocabulary built on unstable primitives requires wholesale revision.*

## Prior Art

This project combines ideas from Esperanto (agglutinative phonetic grammar), Lojban (logical grammatical structure), Toki Pona (semantic primitive composition), and formal ontologies (domain namespaces). See [notes/prior-art.md](notes/prior-art.md).
