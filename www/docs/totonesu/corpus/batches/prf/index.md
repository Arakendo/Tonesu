---
title: "PRF"
---

# PRF

*Theme: [Foundations](../../foundations/overview/)* · 6 sentences.

:material-book-open-variant: [Full translation analysis](../../translations/philosophy/proof-structure/)

[← Foundations](../../foundations/overview/) · [← Corpus](../../overview.md)

---

## PRF-001 · 

**Purpose:** First test of multi-step deductive chains using `go`. Tests the `a-` universal scope prefix in a major syllogistic premise, stacked double-`go {P}, go {P}, C` conclusion, `;` vs `go` distinction as a minimal contrast pair (Humean constant conjunction vs necessary connection), Descartes' Cogito using `go` as epistemic grounding, and reductio ad absurdum structure. No new vocabulary — pure grammar and connective test. Full analysis in `corpus/translations/Philosophy/proof-structure.md`.

<span id="S684"></span>
**S684**
`a-zo-li  ne  de-zo`
*All persons are mortal.*

<span id="S685"></span>
**S685**
`la-Sokrates  ne  zo-li`
*Socrates is a person.*

<span id="S686"></span>
**S686**
`go  a-zo-li  ne  de-zo ,  go  la-Sokrates  ne  zo-li ,  la-Sokrates  ne  de-zo`
*Because all persons are mortal, and because Socrates is a person: Socrates is mortal.*

<span id="S687"></span>
**S687**
`la-li  to-ki ;  lo-li  su-ti`
*I am reasoning; I am in a current state.*

<span id="S688"></span>
**S688**
`go {la-li  to-ki},  lo-li  su-ti`
*Because I am reasoning: I have a determinate present state.*

<span id="S689"></span>
**S689**
`to-go {no-ki},  no-re ;  re  su-ti ;  go  to ,  ki`
*If there were no motion, there would be no cyclic recurrence. Cyclic recurrence [currently] obtains. By the foregoing principle: motion.*

### Batch Summary

| Entry | Tonesu | Written form | Key feature |
|-------|--------|-------------|-------------|
| S684 (PRF-001-A) | `a-zo-li  ne  de-zo` | `azoli ne dezo` | First `a-` scope prefix in syllogistic major premise |
| S685 (PRF-001-B) | `la-Sokrates  ne  zo-li` | `laSokrates ne zoli` | Minor syllogistic premise with proper name |
| S686 (PRF-001-C) | `go  a-zo-li  ne  de-zo ,  go  la-Sokrates  ne  zo-li ,  la-Sokrates  ne  de-zo` | `go azoli ne dezo, go laSokrates ne zoli, laSokrates ne dezo` | First stacked double-`go {P}, go {P}, C` |
| S687 (PRF-001-D) | `la-li  to-ki ;  lo-li  su-ti` | `lali toki ; loli suti` | Cogito wrong form — `;` constant conjunction |
| S688 (PRF-001-E) | `go {la-li  to-ki},  lo-li  su-ti` | `go lali toki, loli suti` | Cogito correct — `go` epistemic grounding |
| S689 (PRF-001-F) | `to-go {no-ki},  no-re ;  re  su-ti ;  go  to ,  ki` | `togo noki, nore ; re suti ; go to, ki` | First reductio; `go to,` anaphoric conclusion |

**Coverage:** `a-` universal scope prefix in a deductive premise (S684); stacked `go {P}, go {P}, C` (S686); `;` vs `go` minimal pair for the Humean/Cartesian distinction (S687/S688); `to-go` counterfactual + `go to,` anaphoric conclusion in reductio structure (S689). No new vocabulary entries — pure grammar and connective test.

**Key finding:** The `;` / `go` distinction is the sharpest distinction in the corpus. `;` = constant conjunction (Hume): two states recorded in sequence. `go` = necessary connection: the premise constitutively grounds the consequence. S687/S688 are minimal pairs on exactly this axis — same propositional content, different logical structure. The Cogito works in Tonesu only with `go`, not `;`.

---

*Generated from [`registry/entries.yaml`](https://github.com/Arakendo/Tonesu/blob/main/registry/entries.yaml).*