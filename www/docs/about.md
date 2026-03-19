---
title: About
---

# About Tonesu

Tonesu is a constructed language built on a closed set of **34 two-letter primitive roots**. All vocabulary is assembled from those roots by compounding — the language does not admit improvised atoms. The word shape itself tells you what kind of thing it is: primitive root, compound, digit, or physical constant.

The name **Tonesu** is a contraction of `to-ne-su` (pattern · relation · structure) — itself a demonstration of the dual-register design: a compositional root compound that contracts into a natural spoken form.

> Tonesu does not enforce truth. It enforces clarity about the epistemic status of claims.

---

## Design commitments

| | |
|---|---|
| **Phonetically simple** | Globally pronounceable — one letter, one sound, stress always on the first syllable |
| **Compositionally transparent** | Words are built from audible parts; parsing a word gives you its meaning |
| **Domain-extensible** | New fields emerge by combining existing primitives; the language doesn't break when knowledge expands |
| **Epistemically honest** | The grammar encodes *what kind of claim you are making*, not just what you claim |

---

## Prior art and influences

Tonesu draws on — and departs from — a range of earlier work in constructed languages, philosophy, pedagogy, and formal systems.

### Constructed languages

**Esperanto** (1887) demonstrated that agglutinative morphology with productive affixes works: a small root vocabulary generates many words. But the roots themselves are arbitrary European borrowings, not semantically decomposed. Tonesu requires every root to carry analyzable meaning.

**Lojban** (1987) showed that predicate-argument structure can be encoded directly in grammar, and that explicitly marking epistemic stance is possible. But its roots (gismu) are phonetic blends of world languages, not semantic composites, and the language is notoriously hard to speak naturally.

**Toki Pona** (2001) proved that compositional semantic coverage is possible with a tiny vocabulary — about 130 roots. "Computer" is just "thinking machine." Tonesu takes the same insight but adds formal word-formation rules, a domain system, and mechanisms for precision that Toki Pona intentionally avoids.

**Ithkuil** (2004) demonstrated how much semantic precision can be packed into compact forms — fine-grained encoding of perspective, intentionality, scope, and evidentiality. But the complexity makes it essentially unspeakable. Tonesu aims for a simpler surface that still encodes epistemic structure.

### Philosophy

**Karl Popper's** falsifiability criterion and conjectural epistemology inform Tonesu's epistemic scale directly. The `se → si → to → tosu` pipeline (perception → signal → knowledge → registered theory) tracks what kind of evidence supports a claim. The `()` evidential frame implements Popper's insistence that all knowledge is provisional.

**Wittgenstein's** early picture theory of meaning (propositions mirror the structure of facts) is the philosophical ancestor of Tonesu's compositional semantics. His later work on meaning-as-use is reflected in the three-stage compound lifecycle: compositional reading → algebraic use → registry stabilization. The `tofe` boundary concept makes Wittgenstein's question — where does knowledge end? — grammatical.

**John Wilkins' Real Character** (1668) is the most direct historical ancestor: a universal language where word structure encodes position in a knowledge tree. It failed because the taxonomy was rigid and encoded a 17th-century European worldview. Tonesu's domain-creation protocol and stability rules are a direct response to Wilkins' failure mode.

### Pedagogy

**Hooked on Phonics** (1987) is the direct motivation for Tonesu's phonological design. The one-letter-one-sound rule and the elimination of silent letters, digraphs, and irregular pronunciations come from the insight that a learner should be able to decode any word from first principles, without a teacher present. Tonesu extends this from phonology into semantics: you should be able to decompose any compound into its roots and arrive at an approximate meaning, even for a word you've never seen.

### Formal systems

**RDF / OWL** and the semantic web tradition inform the domain-as-namespace design. Tonesu's domain registry and inheritance rules map closely to how formal ontologies define classes — but in a spoken, human-usable form.

---

## Comparison with other systems

| System | Phonetic | Compositional semantics | Domain system | Scalable | Speakable |
|--------|----------|------------------------|---------------|----------|-----------|
| Esperanto | Yes | Partial | No | Limited | Yes |
| Lojban | Yes | No | No | Limited | Difficult |
| Toki Pona | Yes | Yes (minimal) | No | No | Yes |
| Ithkuil | Yes | Partial | No | No | Very hard |
| Wilkins (1668) | No | Yes | Implicit | No | N/A |
| OWL / RDF | No | Yes | Yes | Yes | No |
| **Tonesu** | **Yes** | **Yes** | **Yes** | **Yes** | **Yes** |

---

## The site

This site is generated from an [open-source repository](https://github.com/Arakendo/Tonesu) by an MkDocs + Python pipeline. It includes:

- **Registry** — searchable word list with etymology, corpus attestations, and domain groupings
- **Word builder** — interactive tool for composing compounds from primitive roots
- **Corpus** — 575+ annotated sentences across grammar, theology, mathematics, and everyday speech
- **To'tonesu** — domain exploration pages (biology, law, physics, theology, mathematics, and more)

Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

---

## Contact

Questions, feedback, or collaboration inquiries:

**arakendo@gmail.com**

---

## License

Tonesu — including the language specification, registry, corpus, and all associated documentation — is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/) license.

You are free to share, remix, transform, and build upon the material for any purpose, even commercially, provided you give appropriate credit and distribute contributions under the same license.
