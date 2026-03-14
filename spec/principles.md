# Principles

## Status: Normative

This file locks down the foundational design commitments. Every later decision in `spec/`, `registry/`, and `corpus/` should be checked against these. If a proposed rule contradicts a principle, the principle wins — unless the principle itself is being revised, which requires explicit justification here.

---

## 1. Phonetic Transparency

Every written symbol maps to exactly one sound. Every sound maps to exactly one symbol. No silent letters, no digraphs, no context-dependent pronunciation. A speaker who knows the sound inventory can pronounce any word they have never seen before.

*Corollary: the writing system is a transcription of speech, not an independent orthographic tradition.*

---

## 2. Semantic Compositionality

Words are built from a small set of audible conceptual parts. A listener who knows the primitives and formation rules can infer the approximate meaning of an unfamiliar compound without a dictionary. Full transparency is an ideal; partial inferability is the minimum requirement.

*Corollary: new vocabulary is generated, not invented. Roots are reused; arbitrary coinages are exceptions.*

---

## 3. Minimal Irregularity

Grammar and morphology are regular by default. Any irregular form requires explicit justification and documentation. The test: if a learner applies the standard rules to an unfamiliar word, they should not be wrong.

*Corollary: exceptions are expensive. They carry a documentation burden and must be tracked in the registry.*

---

## 4. Optional Rather Than Mandatory Marking

Grammatical categories are marked only when the information must be distinguished. Number, gender, definiteness, and tense are expressed when relevant — not obligatorily on every noun or verb. The language encodes what speakers need to communicate, not what a grammatical tradition requires.

*Corollary: a sentence with all optional markers omitted is still a valid sentence when context is sufficient.*

---

## 5. Generative Domains

New conceptual fields are created by combining existing primitives according to the domain creation rules in `spec/domain-creation.md`. Ad-hoc vocabulary coinages are a last resort. A well-designed domain unlocks many compound words; a well-designed compound unlocks nothing except itself.

*Corollary: if a new concept cannot be expressed as a compound of existing primitives, that is a signal to evaluate whether a new primitive or domain is warranted — not a license to invent an arbitrary root.*

---

## 6. Protected Proper Names

Proper names are a distinct lexical class. They identify; they do not describe. They are phonologically normalized into the language but are not required to be semantically decomposed. The compositional system applies to titles, roles, and institutional names — not to personal identifiers.

*Corollary: the name particle `na` is always honored. A listener encountering `na X` should never try to parse X as a compound noun.*

---

## 7. Dual Register by Design

The language has a formal register (explicit, transparent, compositional) and a colloquial register (contracted, efficient, idiomatic). Both are valid. The formal register is the source of truth; the colloquial register is derived from it and traceable back to it. Formal forms are never deprecated just because colloquial usage overtakes them.

*Corollary: contraction and lexicalization are expected and welcome, but they must be documented.*

---

## 8. Stability Before Extensibility

The primitive root set and domain rules must be stable before the vocabulary registry grows. A large vocabulary built on an unstable foundation requires wholesale revision. Fewer, better-defined primitives are always preferable to more primitives added prematurely.

*Corollary: resist the temptation to add a new primitive root every time a compound feels awkward. Awkward compounds are a diagnostic, not a problem to be solved by root proliferation.*

---

## 9. Emotions Are System States, Not Primitives

Tonesu is a human language spoken by fully human people. Concordians experience the full range of human emotion, **including states that are pre-conceptual, unresolved, or resistant to articulation**. Concordian culture frames emotional states as signal-processing events — internal signals that may or may not resolve into a conceptual model — rather than as fixed, opaque qualia with names. This is not a deficiency; it is a cultural practice that the language reflects and reinforces.

Consequences:

- **No named-emotion primitive roots.** A root for "fear" or "joy" fails Validation Rule 1 (irreducibility): both concepts are expressible through existing primitives without circular nonsense. Named emotions are compounds and idiomatic constructions.
- **Unresolved affect is a first-class speech act.** `se-no-to` (W090, signal-without-model) is a complete, honest, culturally valid utterance — not a failed diagnostic. A speaker who cannot name or locate their internal state is using the language correctly. The inability to articulate is itself articulable. Concordian culture does not require emotional clarity before emotional speech is permitted.
- **The diagnostic framing is the primary register.** `la-mi  se  fe-de` (I perceive boundary-decay) is not a clunky workaround for "I'm afraid" — it is the privileged Concordian way to express that state. The process-orientation is intentional.
- **A substrate root is not a named-emotion root.** `fa` (primitive 33, March 2026) names the raw felt-interior substrate of affective experience — inward-facing organism tone before it resolves into any conceptual model. This is categorically different from a named-emotion primitive: `fa` is to affect what `ma` is to matter — the substrate, not any particular instance. **Guard (normative):** `fa` may not be used as an emotion shorthand. `fa-vo-be` is not joy; `fa-vo-de` is not sadness. Process constructions still govern all named emotional states. `fa` appears only where the substrate itself is foregrounded: unresolved affect (`fa-no-to`), numbness (`fa-no`), arousal level, observer-mode separation.
- **Emotional idioms must be documented as corpus develops.** Because the framing is precise but unfamiliar, the standard emotional expressions become vocabulary items in their own right — registered as derived words (W-series) once attested in corpus. The compound is the word; it is not pending a real word.
- **The register gap is productive, not a bug.** When a Concordian says `la-mi  se  fe-de  lo-ne-mi` and a non-Concordian hears "I'm afraid of losing this relationship," that translation gap is a characterization of Concordian culture, not a failure of the language.

*Corollary: do not add sensory or embodied-experience primitives preemptively. Run the 20 ordinary-life sentence test (see notes/open-questions.md) first. If a concept fails to express without genuine distortion — not just verbosity — evaluate it as a primitive candidate. `fa` was justified on this criterion: `se` (outward-facing detection) produces a structurally wrong reading for inward affective substrate states, not merely a verbose one. 20-sentence confirmation batch pending.*

## 10. Religion Is a Subset of Organized Knowledge

Tonesu has no dedicated word for "heresy." This is not an oversight — it is a structural consequence of the language's epistemic architecture.

The theological debate batch (C005) established this result: a doctrinal dispute in Tonesu is epistemically indistinguishable from a scientific or engineering knowledge dispute. The machinery is identical:

- **Inflation** (`to-fe-ka`): claiming a proposition has reached `to-su` status when it has not
- **Deflation** (`to-fe-ka`): suppressing a proposition that has legitimately reached `to-su` status
- **Adjudication** (`to-fe-li`): the qualified arbiter who examines the `to-fe` threshold crossing
- **Institutional authority** (`to-fe-su`): the standards body that formalizes rulings into `to-su`

A charge of heresy, in any other culture, is a claim that someone has mislabeled the epistemic status of a proposition within an organized knowledge domain. In Tonesu, that is simply a `to-fe-ka`/`to-fe-ki` charge. The accuser must establish that the threshold was crossed (or suppressed) deliberately or negligently; the arbiter adjudicates; the institution publishes the result.

**Consequences:**

- **No heresy primitive and no heresy compound.** The concept is already fully expressible through `to-fe-ka` (deliberate boundary violation) with a doctrinal proposition as the content. Adding a separate compound for theological violations would imply religion operates under different epistemic rules — which is precisely the Concordian cultural rejection.
- **Religion does not require a separate domain.** The `to-re-su` (canonical recurring doctrine) / `to-fe-su` (epistemic standards body) / `to-fe-li` (arbiter) machinery serves science, engineering, law, and religion with the same tools. No domain split is needed; the content of the proposition is all that differs.
- **The "no heresy" result generalizes.** Any domain in which humans have developed specialized vocabulary for "epistemic violation within that domain" — academic fraud, perjury, false prophecy — will compress in Tonesu to a `to-fe-ka` charge with contextually specified content. Tonesu makes the epistemic structure visible by refusing to lexicalize the domain distinctions.
- **Guard (normative):** Do not add domain-specific epistemic-violation compounds (`zo-fe-ka` for "biological fraud," `wi-fe-ka` for "doctrinal heresy," etc.). All such concepts route through the unified `to-fe` system. The unification is the point.
