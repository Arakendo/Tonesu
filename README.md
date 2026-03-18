# Tonesu

> **A constructed language built on generative roots.**  
> Every word is audible as its own definition.

**→ [tonesu.org](https://tonesu.org/)** — live reference site with full registry, corpus, and grammar

---

## What it is

Tonesu is a designed language built on a closed set of 34 two-letter (CV) primitive roots. All vocabulary is assembled from those roots by compounding — the language does not admit improvised atoms. The word shape itself tells you what kind of thing it is: primitive, compound, digit-class, or physical constant.

The language is named **Tonesu** — a contraction of `to-ne-su` (pattern · relation · structure), which is itself a demonstration of the dual-register design: a compositional root compound that contracts into a natural spoken form.

---

## Four design commitments

| | |
|---|---|
| **Phonetically simple** | Globally pronounceable — one letter, one sound, stress always on the first syllable |
| **Compositionally transparent** | Words are built from audible parts; parsing a word gives you its meaning |
| **Domain-extensible** | New fields emerge by combining existing primitives; the language doesn't break when knowledge expands |
| **Epistemically honest** | The grammar encodes *what kind of claim you are making*, not just what you claim |

> Tonesu does not enforce truth. It enforces clarity about the epistemic status of claims.

---

## Quick orientation

### Word shape = word tier

| Shape | Tier | Example | What lives here |
|-------|------|---------|-----------------|
| `CV` | Primitive | `to`, `ne`, `su` | 34 foundational roots — closed set |
| `CV-CV+` | Compound | `tonesu`, `toli` | All open vocabulary |
| `CVC` | Lexical atom | `ker` (red), `bol` (1) | Digits, colors — closed class |
| `CVCC` | Exceptional anchor | `varn` (π), `hulm` (year) | Constants/units only |

### Core sentence frame

```
la-[agent]   [verb-compound]   lo-[patient]
```

- `la-` agent · `lo-` patient · `lu-` result/beneficiary
- `ne` copula (property) · `go` causal particle
- Modifier precedes head — compounds are head-final and right-branching

### A few words

```
toli        to-li        pattern-person           →  scholar
tokimu      to-ki-mu     pattern-change-device    →  computer
noha        no-ha        absence-of-heat          →  cold
zolimu      zo-li-mu     organism-agent-device    →  robot / artificial lifeform
```

---

## Repository layout

| Path | Contents |
|------|----------|
| `spec/` | Normative language rules — grammar, phonology, morphology, word-formation |
| `registry/` | Word inventories — primitives, derived compounds, roots, domains |
| `corpus/` | Sentence corpus and translation stress tests |
| `notes/` | Open questions, design notes, semantic map |
| `www/docs/` | MkDocs source for [tonesu.org](https://tonesu.org/) |
| `scripts/` | Pipeline scripts (YAML → annotated → registry → site) |

---

## Key spec files

| What | File |
|------|------|
| Grammar (particles, word order, scopes) | [`spec/grammar.md`](spec/grammar.md) |
| Phonology (tiers, parse invariants) | [`spec/phonology.md`](spec/phonology.md) |
| Morphology (affixes, slots) | [`spec/morphology.md`](spec/morphology.md) |
| Word-formation rules | [`spec/word-formation.md`](spec/word-formation.md) |
| Guiding principles | [`spec/principles.md`](spec/principles.md) |
| All 34 primitive roots | [`registry/primitives.md`](registry/primitives.md) |
| Derived word registry | [`registry/derived/index.md`](registry/derived/index.md) |

---

## The 34 primitives (quick reference)

| Category | Roots |
|----------|-------|
| Entities & Substances | `mu` object · `ma` matter · `zo` living thing · `li` person/agent |
| Processes & Change | `ki` motion · `ka` action · `be` growth · `de` decay |
| Structure & Pattern | `su` structure · `to` pattern/thought · `fe` boundary |
| Relations & Logic | `ne` relation · `pe` part · `go` cause · `du` result · `zi` mutual |
| Space & Location | `pa` place · `di` direction · `ko` containment |
| Time | `ti` time · `re` recurrence |
| Perception & Signal | `se` sense · `so` sound · `lu` light · `si` signal |
| Energy & Force | `ra` energy · `ha` heat |
| Quantity | `nu` quantity · `ru` unity · `pu` plurality |
| Mind & Value | `vo` value · `wi` will · `no` negation |
| Affective | `fa` felt-interior state |

---

## Live site

The [tonesu.org](https://tonesu.org/) site is generated from this repository by an MkDocs + Python pipeline. It includes:

- **Registry** — searchable word list with etymology, corpus attestations, and domain groupings
- **Word builder** — interactive 3-panel tool for composing compounds from primitive roots
- **Corpus** — 575+ annotated sentences across grammar, theology, mathematics, and everyday speech
- **To'tonesu** — domain exploration pages (biology, law, physics, theology, mathematics, and more)

Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).
| All 34 primitive roots | [`registry/primitives.md`](registry/primitives.md) |
| Derived word registry | [`registry/derived/index.md`](registry/derived/index.md) |

---

## The 34 primitives (quick reference)

| Category | Roots |
|----------|-------|
| Entities & Substances | `mu` object · `ma` matter · `zo` living thing · `li` person/agent |
| Processes & Change | `ki` motion · `ka` action · `be` growth · `de` decay |
| Structure & Pattern | `su` structure · `to` pattern/thought · `fe` boundary |
| Relations & Logic | `ne` relation · `pe` part · `go` cause · `du` result · `zi` mutual |
| Space & Location | `pa` place · `di` direction · `ko` containment |
| Time | `ti` time · `re` recurrence |
| Perception & Signal | `se` sense · `so` sound · `lu` light · `si` signal |
| Energy & Force | `ra` energy · `ha` heat |
| Quantity | `nu` quantity · `ru` unity · `pu` plurality |
| Mind & Value | `vo` value · `wi` will · `no` negation |
| Affective | `fa` felt-interior state |

---

## Live site

The [tonesu.org](https://tonesu.org/) site is generated from this repository by an MkDocs + Python pipeline. It includes:

- **Registry** — searchable word list with etymology, corpus attestations, and domain groupings
- **Word builder** — interactive 3-panel tool for composing compounds from primitive roots
- **Corpus** — 575+ annotated sentences across grammar, theology, mathematics, and everyday speech
- **To'tonesu** — domain exploration pages (biology, law, physics, theology, mathematics, and more)

Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

