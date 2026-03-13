# Open Questions

Consolidated list of unresolved design decisions from across all spec and registry files. When a question is resolved, move it to docs/decisions/ (or note the resolution inline and delete it here).

---

## Phonology

- [ ] Adopt vowel length as a morphological tool, or avoid complexity? (spec/phonology.md)
- [ ] Allow CVC codas freely, or restrict to a subset of consonants?
- [ ] Define phonotactics at compound boundaries explicitly.
- [x] ~~Replace `plu` (three-letter root) with a CVC-compliant form.~~ → replaced with `pu`.

---

## Grammar and Morphology

- [ ] Finalize grouping/nesting particle syntax for compound NPs.
- [ ] Decide whether domain marker `da` is a prefix that fuses with the root or always a free particle.
- [ ] Specify behavior when agent and patient are both omitted (topic-drop).
- [x] ~~**Resolve `li` particle / `li` root collision.**~~ → **Resolved:** agent particle renamed to `la`. The `li` root (person/agent) is unchanged. See spec/grammar.md particle table and registry/roots.md G001.
- [ ] Define passive / agentless clause structure.
- [ ] **Conditionals:** no dedicated conditional particle exists. S013 shows `go` (causal framing) is a viable substitute — decide whether to add a conditional particle or formalize causal framing as the canonical strategy.
- [x] ~~**Inchoative derivation**~~ → **Resolved:** `ROOT + ki` = enter state ROOT. Full table in spec/morphology.md. First attested: `ne-ki` (connect) in S013.
- [ ] Causal framing (`go`/`du` pair) — how does it integrate with SOV order?
- [ ] **Purpose clauses:** no dedicated structure for "to [infinitive]" when purpose cannot be embedded in a compound. S014 worked around it via compounding; does not generalize. Candidate: `wi [action]` = "intending to [action]" as a purpose frame. Define in spec/grammar.md.
- [ ] Finalize phonetic forms of tense/aspect/modality markers (current labels are English glosses).
- [ ] Decide stacking limit for derivational suffixes before restructuring as a compound is required.
- [ ] Should modality (might/must/plan) live on the verb or as a sentence-level particle?
- [ ] Should definiteness markers (`ko-` / `ne-`) be drawn from root vocabulary or be dedicated particles? Note: `ko` is now the containment primitive — collision if reused as definiteness marker.

---

## Primitives and Ontology

- [x] ~~Is `li` too broad?~~ → Decided: `li ⊂ zo`. Every `li` is a `zo`. Animals are `zo` only. AI/institutions are `mu + li`. See registry/primitives.md entity model.
- [x] ~~`ki` overloaded?~~ → Narrowed: `ki` = motion only. General transformation uses `be`/`de` compounds. Candidate root `ce` (state change) pending corpus evaluation.
- [ ] Does `to` need to split into `thought` and `knowledge`? Working model: `to` = conceptual pattern/thought; `to+su` = organized knowledge (body of knowledge); `to+si` = encoded information / data. Confirm before corpus work scales — S013 used `to` alone for "knowledge", which may be too loose.
- [x] ~~**`ra` particle / `ra` root collision.**~~ → **Resolved:** instrument particle renamed from `ra` to `ro` (`ro` has no root assignment). The collision was non-transparent — instrument-marking and energy/force share no semantic relationship. Policy formalized in spec/grammar.md: **Particle–Root Overlap Policy** (particles may share a root's form only when the particle's function is semantically derived from that root). `ra` now unambiguously means energy/force everywhere it appears.
- [x] ~~**`se` pronoun / `se` root collision.**~~ → **Resolved:** 3rd person pronoun renamed `se` → `ze`. No root `ze` exists. Corpus impact was zero (pronoun had not appeared in any gloss). See spec/grammar.md pronoun table.
- [x] ~~**`wi` pronoun / `wi` root collision.**~~ → **Resolved:** group pronoun renamed `wi` → `yu`. No root `yu` exists. The rename also unblocks `wi` (will/intention root) from future adoption as a purpose-frame particle without pronoun ambiguity. See spec/grammar.md pronoun table.
- [ ] Should `ra` (energy) cover information energy or remain strictly physical?
- [ ] Phonetic cluster `se`/`so`/`si`: evaluate survival at normal speech speed.
- [ ] Evaluate candidate root `ce` (transformation/state change) after first corpus sentences.
- [ ] `zo` subtypes: are plant/animal/fungus distinguishable by compound, or is `zo` intentionally undifferentiated?

---

## Word Formation

- [ ] Decide separator convention at compound boundaries (none, hyphen in writing, pause in speech).
- [ ] Define maximum compound length before compression is required.
- [ ] Confirm suffix order when multiple derivational markers stack.

---

## Domains

- [ ] Several domain entries have substrate == principle (e.g. `da-su`). Review whether this is meaningful.
- [ ] `da-to-ki-li` (knowledge-transfer) is four elements — too long; needs a better construction.
- [ ] Establish Stage 3 short forms for the highest-frequency domains.
- [ ] Standard procedure for deprecating a domain whose scope was drawn too narrowly.
- [ ] Intersecting domains: always create a new registered domain, or allow ad-hoc compounds?

---

## Naming

- [ ] Define phonological adaptation rules for borrowing foreign names precisely.
- [ ] Should `na` always be required or only when ambiguity could occur?
- [ ] Rules for compound place names that are partly descriptive and partly endonymic.
- [ ] Specify format for machine/system identifiers.

---

## Corpus / Testing

- [ ] Does the language need a passive voice construction?
- [ ] How should idiomatic metaphors be handled — preserve, block, or formally encode as analogy?
- [ ] Translation policy for culturally specific concepts with no structural equivalent.
