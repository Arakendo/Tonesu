# Specification

## Status: Normative

The specification defines the invariant rules of Tonesu. All registry entries and corpus sentences must conform to these documents. Spec changes are breaking changes.

---

## Documents

| File | Contents |
|------|----------|
| [principles.md](principles.md) | Ten foundational design commitments. The spec hierarchy's highest authority. |
| [phonology.md](phonology.md) | Sound inventory, syllable structure, stress, and writing system mapping. |
| [morphology.md](morphology.md) | Affixes, derivation, number, tense/aspect marking, and morphological categories. |
| [word-formation.md](word-formation.md) | Rules for compounding primitives into derived vocabulary. |
| [grammar.md](grammar.md) | Sentence structure, particles, clause syntax, predication strategies, epistemic modality, negation, temporal frames. |
| [domain-creation.md](domain-creation.md) | Protocol for opening new conceptual domains. |
| [naming.md](naming.md) | Proper name conventions and the `na` particle. |

---

## Spec Hierarchy

When a registry entry conflicts with grammar.md, grammar wins.
When grammar conflicts with principles.md, principles win.
Corpus sentences illustrate; they do not override spec.
