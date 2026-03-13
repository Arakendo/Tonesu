# Morphology

## Status: Draft

Morphology covers how words are internally structured: affixes, derivation, and the marking of grammatical categories. Syntax and particles are in spec/grammar.md. Compounding and word-formation rules are in spec/word-formation.md.

---

## Core Principles

- All morphological marking is agglutinative: each marker retains its identity and meaning when combined
- No root mutation: adding markers never changes the phonetic form of the root
- All categories are optional by default; obligations arise only from what must be distinguished, not from grammatical tradition
- Markers stack rather than fuse

---

## Tense and Aspect

Optional suffix markers that stack after the verb root. If omitted, tense and aspect are inferred from context or from explicit time-reference particles (see grammar.md).

### Tense

| Marker | Meaning |
|--------|---------|
| `-past` | situates the event before reference time |
| `-now` | situates the event at reference time |
| `-fut` | situates the event after reference time |

### Aspect

| Marker | Meaning |
|--------|---------|
| `-done` | completed; the event reached its end state |
| `-ing` | ongoing; the event is in progress |
| `-rep` | repeated or habitual |

### Modality

| Marker | Meaning |
|--------|---------|
| `-might` | possibility |
| `-must` | requirement or necessity |
| `-plan` | intentional / planned |

### Stacking Order

Markers stack in this order: `root + tense + aspect + modality`

```
build-fut-ing-plan
```
*will be building (as planned)*

Only the markers needed should appear. Unneeded dimensions are omitted.

---

## Derivational Suffixes

Convert roots from one lexical role to another. Attach directly to the root. Full list in lexicon/roots.md.

| Suffix | Role | Example |
|--------|------|---------|
| `-li` | agent — one who does | `ka-li` → doer / actor |
| `-mu` | device / instrument | `ka-mu` → tool for the action |
| `-pa` | location | `ka-pa` → site of the action |
| `-su` | result / product | `ka-su` → what was produced |
| `-to` | abstract nominalization | `ka-to` → the concept of the action |
| `-ge` | quality / property | `ra-ge` → energetic |
| `-ki` | verbal noun (ongoing process) | `be-ki` → the act of creating |

> **Design note:** the quality/property suffix was formerly `-se`, sharing form with root `se` (perception). The semantic domains overlap — "a quality is what is perceivable about a thing" — producing genuine ambiguity in nominal position (attested S049C). Renamed to `-ge` (no root collision). Rule formalized: **a suffix must not share form with a root whose semantic domain overlaps with the suffix's derivational role.** `-li`, `-mu`, `-pa`, `-su`, `-to`, `-ki` all satisfy this rule because their root forms and suffix functions are semantically distinct despite formal identity.

Multiple derivational suffixes can stack if semantically required, but prefer compounds over long suffix chains.

---

## Inchoative Derivation

`ROOT + ki` produces an inchoative verb: the event of entering the state named by ROOT.

| Compound | Literal | Meaning |
|----------|---------|--------|
| `ne-ki` | relation + motion | connect / become related |
| `su-ki` | structure + motion | become organized / take form |
| `zo-ki` | living + motion | become animate / come to life |
| `ko-ki` | containment + motion | enter / move inside |
| `be-ki` | creation + motion | begin to grow / come into being |

Rule: the result is always an **intransitive verb** — the subject transitions from not-ROOT to ROOT. No patient is marked.

Contrast with the derivational suffix `-ki` (verbal noun, ongoing process: `build-ki` = "the act of building") — that form attaches to action roots. The inchoative compound applies to **state roots** to express state transition. First attested use: `ne-ki` in S013.

---

## Number

Grammatically unmarked by default. Number is expressed by an optional pre-posed quantifier.

| Pattern | Meaning |
|---------|---------|
| `[noun]` | number-neutral; singular or plural by context |
| `nu-[noun]` | some quantity of (non-specific) |
| `ru-[noun]` | one / a single |
| `pu-[noun]` | many / multiple |
| `ne-su-[noun]` | a collective / a structured group |

No agreement: quantifiers do not change verb, adjective, or article forms.

---

## Gender

Not grammatically encoded. Sex, gender, or social category are expressed only when relevant, using a modifier:

```
female-li   male-li   elder-li   child-li
```

No agreement required across sentence elements.

---

## Articles and Definiteness

No articles. Definiteness inferred from context.

Optional definiteness markers available when disambiguation is required:

| Marker | Meaning |
|--------|---------|
| `ko-[noun]` | known / definite reference |
| `ne-[noun]` | new / indefinite reference |

These are modifiers, not obligatory determiners.

---

## Possession

Expressed by a relational particle between possessor and possessed. No morphological mutation.

```
[possessor] poss [possessed]
```

Personal pronouns combine with the same particle:

```
mi poss device     →  my device
wi poss system     →  our system
na-Derik poss tool →  Derik's tool
```

---

## Casual Register: Colloquial Compression

Formal compounds in Tonesu can be long. Casual speech compresses them by stripping contextually recoverable qualifiers. First documented case: `ti-past-to-si-ko-mu` → `to-ko` (see registry/derived.md W027).

**Observed compression pattern (W027 case study):**

| Step | Mechanism | Element dropped |
|------|-----------|----------------|
| 1 | Qualifier drop | `ti-` — living quality is contextually implied by the device category |
| 2 | Qualifier drop | `past` tense — the device is definitionally historical |
| 3 | Nucleus collapse | `to-si` → `to` — non-expert speakers name by salient function (storage), not mechanism |
| 4 | Metonymic drop | `-mu` — device suffix drops when the category referent is clear |

**Working principle:** casual forms strip qualifiers that are recoverable from context or cultural knowledge, retaining the semantic nucleus that identifies function from the *user's* perspective rather than the engineer's.

**Formal rule:** pending. One documented case is insufficient to generalize. Additional corpus compression pairs needed before full rule is stated. See notes/open-questions.md.

> **Note:** This is the Tonesu casual register equivalent of word-clipping in natural languages (English: "refrigerator" → "fridge"; "television" → "TV"). Unlike phonological erosion, Tonesu casual compression is *morphologically principled* — whole morphemes are dropped, not sounds within them.

---

## Open Questions

- [ ] Finalize phonetic forms of tense/aspect markers (placeholders like `-past` are English glosses, not real roots)
- [ ] Decide stacking limit — at what point does a suffix chain require restructuring as a compound?
- [ ] Should definiteness markers `ko-` / `ne-` be drawn from root vocabulary or be dedicated particles? Note: `ko` is now a primitive (containment) — `ko-` as definiteness would collide.
- [ ] Does modality (might/must/plan) live on the verb or as a separate sentence-level particle?
- [ ] Formal colloquial compression rule: one documented case (W027). More corpus pairs needed to generalize the pattern into a stable rule.
