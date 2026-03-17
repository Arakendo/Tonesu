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

## Tense, Aspect, and Modality

Tonesu does **not** use morphological verb suffixes for tense, aspect, or modality. The English-gloss system (`-past`, `-now`, `-fut`, `-done`, `-ing`, `-rep`, `-might`, `-must`, `-plan`) was an early draft; the corpus implementation went a different direction entirely.

### Tense — Temporal Frame Particles

Tense is expressed by the temporal particle `ta` and the time-reference compound family. These appear as pre-posed frame markers or post-predicate sentence markers.

| Form | Meaning | Corpus |
|------|---------|--------|
| `ta-now` | at the present moment | throughout |
| `ti-de` | past time; previously | S035, S066, S168 |
| `ti-be` | proximate future; next | C003, C006 A4 |
| `ti-re` | next scheduled occurrence | C006 B4 |
| `ti-fe` | deadline; the limiting moment | throughout |

Full documentation in spec/grammar.md § Temporal Frame.

### Aspect — Prefix and Compound

Two mechanisms:

1. **`re-` prefix** — habitual/dispositional aspect: `re-{verb}` = the agent characteristically performs {verb}. Documents a disposition, not a schedule. See spec/grammar.md § Aspect.
2. **Inchoative `-ki` compound** — state entry: `{state-root}-ki` = enter the state. See Inchoative Derivation below.

All other aspect readings (perfective, ongoing) are inferred from context or made explicit by temporal frame markers.

### Modality — Clause-Level Constructions

Modality lives entirely in clause-level semantic constructions, not on verbs:

| Modality | Construction | Where defined |
|----------|-------------|---------------|
| Capability | `lo-X  be-vo` | spec/grammar.md § Predication |
| Intention / plan | `la-X  wi {clause}` | spec/grammar.md § Purpose Frame |
| Non-actual / hypothetical | `to-go {X}  Y` | spec/grammar.md § Causal Frame |
| Epistemic possibility | `la-X  si  {prop}` | spec/grammar.md § Epistemic Modality |
| Epistemic impossibility | `la-X  no-to  {prop}` | spec/grammar.md § Epistemic Modality |

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

**Stacking limit: maximum 1 derivational suffix per lexical unit.** Any concept requiring two derivational transformations should be restructured as a compound. The preference for compounds over suffix chains is the design default; this rule formalizes the limit.

Note: the inchoative `-ki` compound (see § Inchoative Derivation below) is a compounding operation on a state root, not a stacking derivational suffix. It does not count toward this limit.

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
| `{noun}` | number-neutral; singular or plural by context |
| `nu-{noun}` | some quantity of (non-specific) |
| `ru-{noun}` | one / a single |
| `pu-{noun}` | many / multiple |
| `ne-su-{noun}` | a collective / a structured group |

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
| `ko-{noun}` | known / definite reference |
| `ne-{noun}` | new / indefinite reference |

These are modifiers, not obligatory determiners.

---

## Possession

Expressed by a relational particle between possessor and possessed. No morphological mutation.

```
{possessor} poss {possessed}
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

---

## Productive Prefixes

Prefixes that attach to roots or compound predicates to modify meaning without changing lexical class.

---

### `no-`: Negation / Absence

**Rule:** `no-` + X = the absence, non-attainment, reversal, or prevention of X.

`no-` is a **high-scope operator**: it applies to the entire content of whatever it prefixes — whether that is a primitive root or a compound predicate. The result is the condition in which X does not hold.

**Corpus evidence — three depth classes:**

| Form | Base | Meaning | First use |
|------|------|---------|-----------|
| `no-de` | `de` (decay) | preservation; non-decay | S030 |
| `no-ru` | `ru` (coherence) | unstable; non-coherent | C002 |
| `no-fe` | `fe` (boundary) | below threshold; within range | C004 |
| `no-ha` | `ha` (thermal state) | cold; low-thermal | S032 |
| `no-ne-fe` | `ne-fe` (dependency condition, W042) | non-dependency; does not require | S063 |

The `no-ne-fe` case is structurally decisive: `ne-fe` is a two-root compound predicate; `no-` prefixes it as a unit. This confirms that **`no-` scope is the entire predicate**, not only the final morpheme. The prefix is a predicate-level operator, not a root-level one.

**Direction:** `no-` always prefixes. Postfix and infix forms are not used.

**Contrast with lexical antonyms:** `no-de` is not simply "the opposite of decay." It is specifically the condition of *decay not occurring* = preservation. The meaning is the state in which the base process, quality, or boundary is absent — not a semantic antonym generated by arbitrary convention.

**Sentence-level extension (provisional):** `no` can also front a full `{ka-clause}` to negate an action frame at clause scope: `no {ka-se}` = "cannot consume; the action of consuming is negated." Attested once (S036). The same operator appears to extend its scope one level: prefix scope = root/compound; clause scope = action frame. Formalized as a grammar rule once confirmed by a second corpus case. See spec/grammar.md § Negation.

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

### V-Prefix Scope Modifiers

Admitted March 2026 (VPC-001). Five bare-vowel forms, all admitted. A V-prefix is a **scope-modifier**: it precedes a root or compound at word-initial position and shifts the *register, granularity, or mode* of the following root without adding independent lexical content.

| Prefix | Scope effect |
|--------|-------------|
| `a-` | abstract/universal — root at broadest conceptual category |
| `i-` | particular/precise — root as a discrete, specified instance |
| `u-` | interior/foundational — the tacit or underlying mode of root |
| `o-` | collective/distributed — root as property of group-as-unit |
| `e-` | emergent/transitional — root in an unsettled, forming state |

**Position constraint:** word-initial only. Mid-compound bare vowels violate parse invariant 1 (every internal syllable begins with a consonant). Position is always structurally unambiguous.

**Scope:** the V-prefix scopes over everything to its right in the same compound (right-branching). `a-to-li` = `a-[to-li]` = universal-(knowledge-agent) = sage.

**`a-` hazard:** `la-a-X` collapses to `la-X` in fast speech. Rule: use `a-` in predicate or patient position, not agent position after `la-`. The other four prefixes are unaffected.

**Registry throttle:** V-prefixed forms are not vocabulary entries by default — they are readable from scope semantics alone. Registry admission requires the scope-shifted meaning to be unparaphraseable by an existing compound AND ≥ 3 corpus attestations in distinct contexts.

Full specification, parse rules, and examples: `spec/word-formation.md § V-Prefix Scope Modifiers`.

---

## Open Questions

- [ ] Finalize phonetic forms of tense/aspect markers (placeholders like `-past` are English glosses, not real roots)
- [ ] Decide stacking limit — at what point does a suffix chain require restructuring as a compound?
- [ ] Should definiteness markers `ko-` / `ne-` be drawn from root vocabulary or be dedicated particles? Note: `ko` is now a primitive (containment) — `ko-` as definiteness would collide.
- [ ] Does modality (might/must/plan) live on the verb or as a separate sentence-level particle?
- [ ] Formal colloquial compression rule: one documented case (W027). More corpus pairs needed to generalize the pattern into a stable rule.
