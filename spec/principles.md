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

Tonesu is a human language spoken by fully human people. Concordians experience the full range of human emotion. However, **Concordian culture frames emotional states as reportable system diagnostics**, not as opaque private experiences. This is not a deficiency — it is a cultural practice that the language reflects and reinforces.

Consequences:

- **No emotional primitive roots.** Emotional states are expressed as derived compounds or idiomatic constructions using existing process, quality, and boundary roots. A new root for "fear" or "joy" fails Validation Rule 1 (irreducibility): both concepts are expressible through existing primitives without circular nonsense.
- **The diagnostic framing is the native register.** `la-mi  se  fe-de` (I perceive boundary-decay) is not a clunky workaround for "I'm afraid" — it is the privileged Concordian way to express that state. The process-orientation is intentional.
- **Emotional idioms must be documented as corpus develops.** Because the framing is precise but unfamiliar, the standard emotional expressions become vocabulary items in their own right — registered as derived words (W-series) once attested in corpus. The compound is the word; it is not pending a real word.
- **The register gap is productive, not a bug.** When a Concordian says `la-mi  se  fe-de  lo-ne-mi` (I perceive decay-threat at my connection), a non-Concordian might need it translated as "I'm afraid of losing this relationship." That translation gap is a characterization of Concordian culture, not a failure of the language.

*Corollary: do not add sensory or embodied-experience primitives preemptively. Run the 20 ordinary-life sentence test (see notes/open-questions.md) first. If a concept fails to express without genuine distortion — not just verbosity — then and only then evaluate it as a primitive candidate.*
