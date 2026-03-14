# Tonesu

A personal study project designing a phonetic, semantically compositional, domain-extensible language. Tonesu is developed both as a linguistic design exercise and as a **worldbuilding language** — a system for generating culturally coherent names, institutions, technical vocabulary, and in-world text that feels architecturally consistent rather than decorative.

The language is called **Tonesu** — the casual contraction of the formal compound `to-ne-su` (pattern – relation – structure). The name is itself a demonstration of the dual-register design: a compositional root compound that contracts into a natural spoken form.

## Core Goals

- **Phonetically simple:** globally pronounceable, one letter per sound, fixed stress
- **Compositionally transparent:** words are built from audible conceptual parts, not memorized atoms
- **Domain-extensible:** new conceptual fields emerge by combining existing primitives; the language doesn't break when knowledge expands
- **Minimal irregularity:** grammar and morphology are regular by default; exceptions require justification

## Repository Structure

```
mkdocs.yml              Nav stub for the MkDocs build project
spec/                   Normative rules — changes here are real language changes
registry/               Vocabulary registry — primitives, roots, domains, compounds
  derived/              Compound entries split into range files (W001–W050, W051–W100, W101+)
corpus/                 Test sentences and conversations
  sentences/            Single-sentence test batches (S-series)
  conversations/        Multi-turn dialogue tests (C-series)
notes/                  Design rationale, semantic map, open questions, history
```

## Where to Start

| If you want to… | Go to |
|-----------------|-------|
| See the core design commitments | [spec/principles.md](spec/principles.md) |
| Understand the sound system | [spec/phonology.md](spec/phonology.md) |
| Understand sentence structure | [spec/grammar.md](spec/grammar.md) |
| Understand word-level structure | [spec/morphology.md](spec/morphology.md) |
| Understand how words are built | [spec/word-formation.md](spec/word-formation.md) |
| See the primitive roots | [registry/primitives.md](registry/primitives.md) |
| Browse all registered vocabulary | [registry/derived/index.md](registry/derived/index.md) |
| Read test sentences | [corpus/sentences/index.md](corpus/sentences/index.md) |
| Read multi-turn conversations | [corpus/conversations/index.md](corpus/conversations/index.md) |
| See open design questions | [notes/open-questions.md](notes/open-questions.md) |
| See the conceptual domain map | [notes/semantic-map.md](notes/semantic-map.md) |
| Read the original design history | [notes/design-history.md](notes/design-history.md) |

## Key Design Tension

Phonetic simplicity and semantic transparency partially conflict. Natural languages drift away from transparency because short efficient sounds beat fully descriptive forms in daily use. This project resolves that tension with a **dual-register design**: a formal layer (transparent compounds) and a casual layer (contracted everyday forms derived from formal compounds). Think of it as source code versus compiled shorthand.

## Current State (March 2026)

| Area | Status |
|------|--------|
| Spec | Principles, phonology, grammar, morphology, word-formation, domain-creation, naming — all drafted and in active use |
| Primitives | 34 roots admitted; set near-closed |
| Vocabulary | 96 registered compounds (W001–W108); 71 active, 6 proposed, 2 cold |
| Corpus | ~194 numbered sentences + 7 multi-turn conversations |
| Open questions | ~25 tracked items across phonology, grammar, ontology, and domains |

## Prior Art

This project combines ideas from Esperanto (agglutinative phonetic grammar), Lojban (logical grammatical structure), Toki Pona (semantic primitive composition), and formal ontologies (domain namespaces). See [notes/prior-art.md](notes/prior-art.md).
