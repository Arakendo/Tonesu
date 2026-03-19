# Morphology

Morphology covers how words are internally structured: affixes, derivation, and the marking of grammatical categories.

**Related pages:** See [Grammar](grammar.md) for syntax and particles. See [Building words](words.md) for compounding and word-formation rules.

---

## Core Principles

- All morphological marking is **agglutinative**: each marker retains its identity and meaning when combined
- **No root mutation**: adding markers never changes the phonetic form of the root
- All categories are optional by default; obligations arise only from what must be distinguished, not from grammatical tradition
- Markers stack rather than fuse

---

## Tense, Aspect, and Modality

Tonesu does **not** use verbal suffixes for tense, aspect, or modality.

### Tense — Temporal Frame Particles

Tense is expressed by the temporal particle `ta` and the time-reference compound family, which appear as pre-posed frame markers or post-predicate sentence markers.

| Form | Meaning |
|------|---------|
| `ta-now` | at the present moment |
| `ti-de` | past time; previously |
| `ti-be` | proximate future; next |
| `ti-re` | next scheduled occurrence |
| `ti-fe` | deadline; the limiting moment |

### Aspect — Prefix and Compound

Two mechanisms:

1. **`re-` prefix** — habitual/dispositional aspect: `re-{verb}` = the agent characteristically performs {verb}
2. **Inchoative `-ki` compound** — state entry: `{state-root}-ki` = enter the state (see below)

All other aspect readings are inferred from context or made explicit by temporal frame markers.

### Modality — Clause-Level Constructions

Modality lives entirely in clause-level constructions, not on verbs:

| Modality | Construction |
|----------|-------------|
| Capability | `{noun}  be-vo` — has the quality of "can-do" |
| Intention / plan | `{agent}  wi  {clause}` — purpose frame |
| Non-actual / hypothetical | `to-go  {proposition}` — causal frame with conditional sense |
| Epistemic possibility | `{agent}  si  {proposition}` — epistemic frame |
| Epistemic impossibility | `{agent}  no-to  {proposition}` — negated epistemic frame |

---

## Derivational Suffixes

Convert roots from one lexical role to another. Attach directly to the root.

| Suffix | Role | Example |
|--------|------|---------|
| `-li` | **agent** — one who does | `ka-li` → doer / actor |
| `-mu` | **device** / instrument | `ka-mu` → tool for the action |
| `-pa` | **location** | `ka-pa` → site of the action |
| `-su` | **result** / product | `ka-su` → what was produced |
| `-to` | **concept** (abstract nominalization) | `ka-to` → the idea of the action |
| `-ge` | **quality** / property | `ra-ge` → energetic |
| `-ki` | **verbal noun** (ongoing process) | `be-ki` → the act of creating |

**Stacking limit:** maximum **1 derivational suffix per lexical unit**. Any concept requiring two transformations should be restructured as a compound (the design default).

**Historical note:** The quality suffix was renamed from `-se` to `-ge` because the form `se` means "perception," creating semantic ambiguity between the suffix and root in nominal position. Rule formalized: **a suffix must not share form with a root whose semantic domain overlaps with the suffix's role.**

---

## Inchoative Derivation

`{state-root} + ki` produces an **inchoative verb**: the event of entering the state named by the root.

| Compound | Meaning |
|----------|---------|
| `ne-ki` | become related / connect |
| `su-ki` | become organized / take form |
| `zo-ki` | become animate / come to life |
| `ko-ki` | enter / move inside |
| `be-ki` | begin to grow / come into being |

The result is always an **intransitive verb** — the subject transitions from not-ROOT to ROOT. No patient is marked.

**Note:** This is distinct from the derivational suffix `-ki` (verbal noun on action roots). The inchoative applies to **state roots** to express state transition.

---

## Number

Grammatically unmarked by default.

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

## Definiteness

No articles. Definiteness is inferred from context. Optional definiteness markers available when disambiguation is required:

| Marker | Meaning |
|--------|---------|
| `ko-{noun}` | known / definite reference |
| `ne-{noun}` | new / indefinite reference |

These are modifiers, not obligatory determiners.

---

## Possession

Expressed by a relational particle between possessor and possessed. No morphological mutation.

```
{possessor}  poss  {possessed}
```

Personal pronouns combine with the same particle:

```
mi  poss  device           →  my device
wi  poss  system           →  our system
na-Derik  poss  tool       →  Derik's tool
```

---

## Productive Prefixes

### `no-`: Negation / Absence

**Rule:** `no-` + X = the absence, non-attainment, reversal, or prevention of X.

`no-` is a **high-scope operator**: it applies to the entire content of whatever it prefixes — whether that is a primitive root or a compound predicate.

| Form | Base | Meaning |
|------|------|---------|
| `no-de` | `de` (decay) | preservation; non-decay |
| `no-ru` | `ru` (coherence) | unstable; non-coherent |
| `no-fe` | `fe` (boundary) | below threshold; within range |
| `no-ha` | `ha` (thermal) | cold; low-thermal |
| `no-ne-fe` | `ne-fe` (dependency) | non-dependency; does not require |

The `no-ne-fe` case is structurally decisive: `ne-fe` is a two-root compound; `no-` prefixes it as a unit. This confirms that **`no-` scope is the entire predicate**, not only a final root.

**Contrast with lexical antonyms:** `no-de` is not simply "the opposite of decay." It is specifically the condition of *decay not occurring* = preservation.

---

## Casual Register: Colloquial Compression

Formal compounds in Tonesu can be long. Casual speech compresses them by stripping contextually recoverable qualifiers. Example: `ti-past-to-si-ko-mu` (formal) → `to-ko` (casual, meaning "past-communication-device" understood as "that old phone").

