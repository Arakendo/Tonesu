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
- [ ] **Relativizer / noun-modifying clause.** S019 (P004) confirmed compounding cannot express capability sentences where the noun is the agent of an active verb ("a system that remembers"). Decision: (a) define a relativizer particle, (b) define participial noun-modifiers as a formal pattern, or (c) accept that capability clauses will use a paraphrase strategy. Do not design in advance of further corpus evidence.
- [x] ~~**Imperative.**~~ → **Resolved:** drop `la-tu`; all other argument and predicate markers remain. Addressee-as-agent is implied by marker absence in addressed-speech context. Emphatic/polite form retains `la-tu`. See spec/grammar.md § Imperative. First corpus example pending.
- [ ] Causal framing (`go`/`du` pair) — how does it integrate with SOV order?
- [x] ~~**Purpose clauses:** no dedicated structure for "to [infinitive]" when purpose cannot be embedded in a compound.~~ → **Resolved:** `wi [clause]` is the canonical purpose frame. `wi` is a transparent overlap with root `wi` (will/intention). Full clause scope is canonical; same-agent reduction permitted when agents are identical. Defined in spec/grammar.md § Purpose Frame. Stress-test sentences P001–P004 queued in corpus/sentences.md.
- [ ] **Subordinate clause delimiter:** Architecture drafted in spec/grammar.md § Subordinate Clauses. Boundary rule defined: subordinate clause extends from introducer until next matrix-level argument/predicate marker. Remaining open question: does the formal register rely purely on explicit matrix markers (no new device), or are optional explicit bracket particles needed for complex/ambiguous cases? Casual-register reduction rule follows once the formal mechanism is settled. Prerequisite for full gloss of P001–P004.
- [ ] Finalize phonetic forms of tense/aspect/modality markers (current labels are English glosses).
- [ ] Decide stacking limit for derivational suffixes before restructuring as a compound is required.
- [ ] Should modality (might/must/plan) live on the verb or as a sentence-level particle?
- [ ] Should definiteness markers (`ko-` / `ne-`) be drawn from root vocabulary or be dedicated particles? Note: `ko` is now the containment primitive — collision if reused as definiteness marker.

---

## Primitives and Ontology

- [x] ~~Is `li` too broad?~~ → Decided: `li ⊂ zo`. Every `li` is a `zo`. Animals are `zo` only. AI/institutions are `mu + li`. See registry/primitives.md entity model.
- [x] ~~`ki` overloaded?~~ → Narrowed: `ki` = motion only. General transformation uses `be`/`de` compounds. Candidate root `ce` (state change) pending corpus evaluation.
- [ ] Does `to` need to split into `thought` and `knowledge`? Working model: `to` = conceptual pattern/thought; `to+su` = organized knowledge (body of knowledge); `to+si` = encoded information / data. Confirm before corpus work scales — S013 used `to` alone for "knowledge", which may be too loose.
- [ ] **Evidentiality.** The Cultural Precision Domain 1 (epistemic states) raises a natural follow-on: does Tonesu grammatically mark the *source* of knowledge? Many languages with rich epistemic vocabulary develop light evidentiality markers — lexical tools that specify how a speaker came to know something. Candidates using existing roots: `se-ro` (by direct perception), `si-ro` (by received signal / hearsay), `to-ro` (by inference/reasoning). Do not add until corpus shows a need to distinguish these in-sentence — one confirmed ambiguous corpus case first.
- [ ] **Epistemic deflation as a distinct charge.** `to-fe-ka` covers both inflation (se presented as to) and deflation (to-su suppressed as si). The evidentiary burden differs: proving inflation requires showing the claim was mislabeled; proving deflation requires establishing what status a claim had *actually reached*. May need either a qualifier or a separate compound when corpus produces a formal adjudication sentence where the direction (inflation vs deflation) matters legally.
- [ ] **The manufactured-doubt problem.** Deflation `to-fe-ka` is structurally adjacent to legitimate conservative epistemic judgment. A `to-fe-li` panel adjudicating a deflation charge must distinguish three positions that look identical from the outside: (1) genuine conservative judgment — "I don't think this has reached to-su" — not a violation; (2) `to-fe-ki` — honest misjudgment of the threshold; (3) `to-fe-ka` deflation — knowing the threshold was met, suppressing the promotion. This three-way distinction is *only resolvable objectively* if `to-fe-su` (the standards framework) defines promotion thresholds procedurally. Without `to-fe-su`, every deflation charge collapses into a subjective dispute and the `to-fe-li` role cannot adjudicate. This makes `to-fe-su` load-bearing, not optional. Register when a corpus sentence requires formal adjudication.
- [ ] **Publication-state gap.** There is currently no vocabulary distinction between a `to-fe-su` ruling that is internal (adopted by the body) and one that has been published to `to-su` status (openly systematized, challengeable by any `to-fe-li`). An unpublished standard is adoption without certification; institutional capture shows up precisely here — a body that enforces rules it has not published to `to-su` status is exercising unchallengeable authority. The distinction may eventually need a compound or qualifier. Candidate: `to-fe-su-ki` (the inchoative — the moment a standards rule enters published `to-su` status) vs bare `to-fe-su` (the body / the unpublished ruleset). Do not register until corpus demands the distinction.
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
