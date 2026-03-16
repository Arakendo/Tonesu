# Prior Art

## Status: Draft

This file documents existing languages and systems that inform the design. Understanding what each one solved — and where each one broke — prevents repeating the same mistakes.

---

## Engineered Human Languages

---

### Esperanto
**Created:** 1887, L. L. Zamenhof
**Goal:** Universal auxiliary language; easy to learn, phonetically regular

**What it does well:**
- Fully phonetic: one sound per letter, no exceptions
- Agglutinative morphology with productive affixes — small root vocabulary generates many words
- Extremely regular grammar, almost no exceptions
- Large enough speaker community to test real use

**Relevant design patterns:**
- Agent suffix (-ist-), instrument suffix (-il-), place suffix (-ej-), abstract noun suffix (-ec-) — similar to derivational markers in this project
- Root vocabulary is small; most words derived from roots + affixes

**Limitations for this project:**
- Roots are mostly arbitrary (European-derived, not semantically decomposed)
- No formal domain system
- No mechanism for structured concept creation
- Semantic transparency is weak: words are compositional in form, not in meaning

---

### Lojban
**Predecessor:** Loglan (1955, James Cooke Brown); Lojban (1987, Bob LeChevalles)
**Goal:** Unambiguous grammar that maps to predicate logic; test Sapir-Whorf hypothesis

**What it does well:**
- Grammar encodes predicate-argument structure explicitly
- Machine-parseable — no grammatical ambiguity by design
- Explicit markers for epistemic stance (evidentials): speaker's confidence level
- Compounds (lujvo) built from combining form roots (rafsi)

**Relevant design patterns:**
- Predicate logic structure as sentence grammar — close to the "typed semantic graph" concept
- Compound words have documented etymology visible in their structure
- Strict separation of grammar from content words

**Limitations for this project:**
- Root vocabulary (gismu) is not semantically transparent — roots are phonetically engineered blends of world languages, not semantic composites
- Highly complex and difficult to speak naturally
- No domain hierarchy or namespace system
- Very few fluent speakers; untested at scale

---

### Toki Pona
**Created:** 2001, Sonja Lang
**Goal:** A minimal language for clarity of thought; inspired by Taoism

**What it does well:**
- ~120–137 root words total — forces compositional thinking
- New concepts must be constructed from primitives: "computer" = "thinking machine"
- Very low learning curve; speakers productive in weeks
- Demonstrates that compositional semantic coverage is possible with a tiny vocabulary

**Relevant design patterns:**
- Minimal primitive set working in practice
- Natural pressure toward compound construction
- Shows that ambiguity is often contextually resolvable even with a small vocabulary

**Limitations for this project:**
- No formal domain system or word-formation rules
- Intentionally imprecise — unsuitable for technical or scientific use
- No mechanism for expanding precision; the minimalism is a feature, not a bug
- No phonemic self-description

---

### Ithkuil
**Created:** 2004 (and revisions), John Quijada
**Goal:** Maximum semantic and grammatical precision in minimal phonetic space

**What it does well:**
- Encodes very fine-grained semantic distinctions: perspective, intentionality, scope, evidentiality
- Morphology is highly systematic and fully documented
- Demonstrates how much meaning can be packed into a compact form

**Relevant design patterns:**
- Ontological categories baked into grammar (similar to "entity/process/relation" type markers)
- Explicit encoding of conceptual structure in word form

**Limitations for this project:**
- Extraordinarily complex; essentially impossible for casual use
- Not designed for phonetic simplicity or global learnability
- No domain extensibility mechanism

---

### Interlingua
**Created:** 1951, IALA
**Goal:** International auxiliary language based on common scientific vocabulary

**Relevant to this project:**
- Scientific vocabulary built from Latin/Greek morphology (photosynthesis, thermodynamics, bioinformatics)
- Shows that structured morphological derivation works in practice for technical domains
- But: process is cultural and ad-hoc, not formally governed by a designed system

---

## Philosophical / Historical Attempts

---

### Karl Popper — Falsifiability and Conjectural Knowledge
**Works:** *The Logic of Scientific Discovery* (1934/1959), *The Open Society and Its Enemies* (1945), *Conjectures and Refutations* (1963)
**Focus:** Epistemology, philosophy of science, critical rationalism

**What's relevant:**
- **The demarcation criterion:** a claim is scientific only if it is in principle falsifiable. This maps directly to Tonesu's epistemic scale — `se` (perceptual, directly testable), `si` (inferential), `to` (model, testable through implication), `to-su` (registered, held as established). Claims that resist placement on this scale are exhibiting the failure mode Popper named.
- **Conjectural knowledge / fallibilism:** all knowledge is provisional and subject to revision. The `()` evidential frame and the three-grade epistemic scale assume this by default — registered knowledge (`to-su`) is the most committed stance, but it remains revisable.
- **Discourse accountability:** Popper's epistemology is inherently social — claims are advanced into a critical discourse and either survive scrutiny or are revised. The `to-fe-ka` discourse-pattern mechanism (repeated misclassification becomes visible over time) is a direct implementation of this without requiring institutional enforcement.
- **The Open Society:** epistemically open institutions where claims compete on their merits rather than being enforced by authority. Tonesu encodes the tools for tracking epistemic stance; it does not enforce correctness.

**Direct connection to current design:**
The `to-fe-ka` / `to-fe-ki` distinction maps to a Popperian distinction: bad science is not simply *falsified* science, it is *unfalsifiable* science — claims engineered to avoid the classification that would expose them. `to-fe-ka` is the grammatical marker for presenting a claim at a higher epistemic tier than its evidence supports. Popper would call this pseudoscience; Tonesu calls it epistemic misrepresentation and makes it visible by design.

**Awareness note:** indirect connection currently; may become more direct as the epistemic classification system matures.

---

### Ludwig Wittgenstein — The Limits of Language and Meaning as Use
**Works:** *Tractatus Logico-Philosophicus* (1921), *Philosophical Investigations* (1953)
**Focus:** Philosophy of language, logic, meaning

**Early Wittgenstein (*Tractatus*) — the founding aspiration:**
- The picture theory of meaning: propositions mirror the structure of facts. This is the philosophical ancestor of compositional semantics — a compound's structure should reflect the structure of what it means. Tonesu is built on exactly this intuition.
- "The limits of my language are the limits of my world" — the founding motivation for building a language that increases expressive precision.
- "Whereof one cannot speak, thereof one must be silent." — *Tractatus* 7. Tonesu's response: if you cannot speak with certainty, mark the uncertainty explicitly (`~`, `()`). If you're at the edge of knowledge, use `to-fe` to name the boundary. Silence is replaced by graduated epistemic marking.

**Late Wittgenstein (*Philosophical Investigations*) — the correction:**
- **Language games:** meaning is use within a practice, not a fixed property of a form. Tonesu's three-stage compound lifecycle (compositional → algebraic → registry-stabilized) acknowledges this — words drift from their structural readings through use, and the registry tracks the drift rather than denying it.
- **Family resemblance:** natural categories don't have sharp essential definitions; they share overlapping features. Tonesu handles this by making the boundary (`fe`) a first-class primitive — the edge of a category is a real concept, not a failure of definition.
- The later Wittgenstein specifically warns against the ambition of a *perfect* logical language. Tonesu is a post-*Philosophical Investigations* project: it does not claim to be a perfect logical language. It claims only to make the *epistemic status* of claims visible — a much more modest and achievable goal.

**Direct connection to current design:**
The `to-fe` boundary concept is Wittgenstein's question made grammatical: where does knowledge end? The `()` evidential frame is a direct implementation of "I carry this without asserting it." The three-stage compound lifecycle is Wittgenstein's meaning-as-use observation built into the registry protocol.

**Awareness note:** indirect connection currently via design philosophy; the epistemic classification system (`se → si → to → to-su`) and the `to-fe-ka` discourse mechanism may justify a direct reference once the corpus is more developed.

---

### John Wilkins — Real Character (1668)
**Goal:** A universal language where word structure encodes taxonomic position in a knowledge tree

**What it did:**
- Organized all of knowledge into a hierarchy
- Word forms encoded the concept's location in the hierarchy
- Concept essentially identical to "self-describing constructs"

**Why it failed:**
- Taxonomy became too rigid — knowledge changed but the word structure could not adapt
- Ontological bias: Wilkins' categories encoded a specific 17th-century European worldview
- No mechanism for revision without breaking the whole system

**Lesson for this project:**
The most direct ancestor of this project. The domain inheritance and stability rules in ontology/domains.md are a direct response to Wilkins' failure mode.

---

## Computational / Formal Systems

---

### RDF / OWL / Formal Ontologies
**Type:** Semantic web standards; knowledge representation languages
**Used for:** Defining concepts, properties, and relationships in machine-readable form

**What it does well:**
- Explicit class hierarchies and domain/range constraints
- Namespace system (URIs) for concepts — directly analogous to the domain system in this project
- Inheritance, composition, and constraint all formally defined

**Relevant design patterns:**
- The domain-as-namespace idea derives most directly from this tradition
- "Domain declaration rule" in ontology/domains.md maps closely to how ontologies define new classes

**Limitations:**
- Not a spoken language; no phonology
- Verbose and not human-friendly for everyday use

---

## Summary Table

| System | Phonetic | Compositional semantics | Domain system | Scalable | Speakable |
|--------|----------|------------------------|---------------|----------|-----------|
| Esperanto | Yes | Partial | No | Limited | Yes |
| Lojban | Yes | No | No | Limited | Difficult |
| Toki Pona | Yes | Yes (minimal) | No | No | Yes |
| Ithkuil | Yes | Partial | No | No | Very hard |
| Wilkins | No | Yes | Implicit | No | N/A |
| OWL/RDF | No | Yes | Yes | Yes | No |
| **This project** | **Yes** | **Yes** | **Yes** | **Yes (goal)** | **Yes (goal)** |

---

## Open Questions

- [ ] Review AUI (1962, W. John Weilgart) — a semantic atomic language using symbols; potentially relevant
- [ ] Review Ceqli and other agglutinative auxlangs for morphological patterns
- [ ] Investigate how constructed languages handle semantic drift over time (Esperanto dialects, Lojban variants)
