# Word Formation

## Status: Draft

---

## Core Principle

Words are not looked up — they are built. The system is generative: a speaker who knows the primitives and rules can construct and interpret unfamiliar words without a dictionary.

---

## Compound Order Rule

**Head-final: modifier precedes core concept.**

```
[modifier] + [core concept]
```

For multi-part compounds:
```
[domain/class] + [function] + [head concept]
```

Examples:
```
knowledge + store + object   →  "memory device / database"
person + build + maintain    →  "engineer"
energy + change + process    →  "propulsion"
```

The last element is the semantic head. Listeners parse left-to-right, narrowing the concept at each step.

---

## Derivational Markers

Short suffix syllables that shift a root into a different lexical role. Regular, no exceptions.

| Suffix | Role | Example |
|--------|------|---------|
| `-li` | agent (one who does) | build-li → builder |
| `-mu` | device/instrument | build-mu → building tool |
| `-pa` | location | build-pa → construction site |
| `-su` | result/state | build-su → structure / what was built |
| `-to` | abstract concept | build-to → the concept of construction |
| `-ge` | quality/property | energy-ge → energetic |
| `-ki` | ongoing process | build-ki → the act of building (verbal noun) |

Derivational suffixes attach directly to the root without a separator.

---

## Word Formation Pathways

Every lexical item enters the language through one of five pathways:

**Path 1 — Primitive root**
Reserved for foundational meanings. Closed set. New primitives require strong justification.

**Path 2 — Regular derivation**
Known root + derivational suffix. Fully predictable.
```
su (structure) + -li  →  suli  (architect / one who organizes structure)
```

**Path 3 — Semantic compounding**
Two or more roots combined by the compound order rule.
```
to (knowledge) + su (structure) + -mu  →  tosu-mu  (knowledge system / organized information device)
```

**Path 4 — Domain registration**
A conceptual namespace declared using the domain creation rule (see ontology/domains.md).
Compounds inside a domain may reference the domain root implicitly.

**Path 5 — Exceptional adoption**
Borrowed proper terms, culturally anchored words. Explicitly marked as non-compositional.
Rare. Must still fit phonology.

---

## Ambiguity Resolution Rules

When multiple valid constructions exist for a concept, prefer in this order:

1. Function over appearance
2. Ontological category over metaphor (in formal register)
3. Existing domain compound before new root
4. Shortest valid unambiguous form

Example: "computer" could be built as `thought-device`, `logic-device`, `information-process-device`.
The preferred canonical form is registered in lexicon/roots.md. Alternates may be listed.

---

## Compound Grouping Marker

**Default parse: right-branching.**

In a plain hyphenated chain, each element modifies the accumulating chain from left to right. The last element is always the semantic head.

```
A-B-C-D   →   A modifies [B modifies [C modifies D]]
```

**Grouping marker: `'` (apostrophe)**

When a compound's default right-branching parse is ambiguous or when a subunit must be understood as a whole before being modified, `'` marks the left boundary of that subcompound.

```
A'B-C-D   →   A modifies [B-C-D as a pre-bound unit]
A-B'C-D   →   [A-B as a plain chain] modifies [C-D as a pre-bound unit]
```

The elements from `'` to the end of the compound (or the next `'` if present) form the subcompound. Everything to the left then attaches to that subcompound as a modifier.

**Usage policy:**

- Omit for compounds of 2–3 roots where the parse is unambiguous.
- Optional at depth-4 where structure is still clear from primitive meanings alone.
- Expected when X-X repetition appears inside a longer compound (X-X creates genuine parse ambiguity at depth ≥ 4 because the repeated roots can be read as either a meta-level unit or the start of a plain chain).
- **Re-scoping function:** `'` is not solely a depth-management device. When a modifier's default right-branching parse would produce a wrong reading, `'` actively re-scopes the modifier over the pre-bound subunit. Example: `ker-zo-se-so` (no apostrophe) right-branches as *ker modifies [zo-[se-[so]]]*, attaching the color to the terminal root rather than to the organism as a whole. `ker'zo-se-so` binds `zo-se-so` first, then attaches `ker` correctly over the whole kind-term. In such cases `'` is required for correctness, not merely for clarity at depth. The mechanism works identically over 3-root and 4-root units.
- Multiple `'` markers are permitted. Each additional apostrophe increases cognitive parse load; casual and spoken registers will naturally avoid deep nesting. Technical, alchemical, and formal registers may use as many as the compound structure requires.
- Phrase restructuring using connective particles (e.g. `ne`) remains available and is preferred in speech when depth makes the compound unwieldy.

**Role-marker interaction:** role-prefix particles (`la-`, `lo-`, etc.) attach to the outer NP boundary and do not participate in the `'` grouping mechanism. The role-marker is outside-NP; `'` is NP-internal. The two levels are orthogonal: `la-ker'zo-se-so` = agent:[red-[kind-term]], with no conflict.

**Phonological status:** prosodic juncture — a slight phrasal pause at the marked boundary. Not a segmental phoneme; not in the consonant inventory. See spec/phonology.md § Prosodic Juncture Marker.

**Corpus basis:** S045 (T-APO-001) — one apostrophe earns its weight; S046 (T-APO-002) — two apostrophes in one compound (legal; heavier; phrase restructuring preferred in ordinary speech). S204–S207 (KNM-002) — `'` as active re-scoping marker over kind-term compounds; symmetry in agent and patient positions confirmed; maximum NP depth with three coexisting structural devices confirmed.

---

## Written Form

**Default: no separator. Compounds are written solid.**

```
to-fe-su-ki  (analytical notation)  →  tofesuki  (written form)
ra-ge        (analytical notation)  →  rage      (written form)
```

Hyphens may be used in analytic or pedagogical contexts to display compound structure. They do not carry grammatical meaning and may be omitted in normal writing. Their role in this spec and corpus is notation only — the way IPA represents pronunciation without being the word itself.

**The only normative non-alphabetic character in a written compound is `'`** (the prosodic juncture marker, § Compound Grouping Marker). `'` is structural: it encodes prosodic grouping that bare letter sequences cannot. Hyphens encode nothing; they are readability aids that a writer may add or omit at will.

This gives Tonesu three layers with distinct functions:

| Layer | Device | Role |
|-------|--------|------|
| Spoken morphology | none | continuous phonological word |
| Structural grouping | `'` | prosodic boundary, left edge of subcompound |
| Analytic clarity | `-` | optional notation in specs, teaching, glosses |

Because hyphens carry no grammatical meaning, written forms strip cleanly: `to'semaka` and `to'se-ma-ka` are the same word. The apostrophe is the only mark that matters.

---

## Lexical Status Tiers

| Tier | Meaning |
|------|---------|
| Compositional-possible | Constructible by rule, not yet standardized |
| Accepted-standard | Reviewed and recommended |
| Lexicalized | Frequent enough to have a contracted colloquial form |
| Deprecated | Replaced by a better construction |

---

## Contraction and Compression Rules

Formal compounds may contract into shorter spoken forms over time. Compression is allowed when:

- The formal compound is at least 3 morphemes long
- The short form is unambiguous within its domain
- The formal form remains the canonical entry in the lexicon

Compression pattern:
```
Formal:     knowledge-store-device
Standard:   knowstore-device
Colloquial: nosta
```

Colloquial forms are recorded in lexicon/colloquial.md and must trace back to their formal source.

---

## Entry Schema

Every compound registered in the lexicon uses this format:

```
ID:           unique identifier
Form:         canonical phonetic form
Orthography:  written form
Type:         primitive | particle | derivation | compound | domain | borrowed
Class:        entity | process | quality | relation | domain
Definition:   concise core meaning
Composition:  root breakdown (if derived)
Semantic bounds:
  includes:   ...
  excludes:   ...
Grammar:      what it modifies, where it may appear
Register:     formal | standard | colloquial | technical
Domain:       general | [named domain]
Examples:     2–5 sample usages
Related:      synonyms, narrower, broader, contrasts
Status:       proposed | accepted | lexicalized | deprecated
```

---

## Open Questions

- [x] ~~Decide separator convention at compound boundaries (none, hyphen in writing, pause in speech).~~ → **Resolved: solid spelling (no separator).** See § Written Form.
- [ ] Define maximum compound length before compression is required
- [ ] Confirm suffix order when multiple derivational markers stack
