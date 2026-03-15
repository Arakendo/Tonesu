# Tonesu

A personal study project designing a phonetic, semantically compositional, domain-extensible language. Tonesu is developed both as a linguistic design exercise and as a **worldbuilding language** — a system for generating culturally coherent names, institutions, technical vocabulary, and in-world text that feels architecturally consistent rather than decorative.

The language is called **Tonesu** — the casual contraction of the formal compound `to-ne-su` (pattern – relation – structure). The name is itself a demonstration of the dual-register design: a compositional root compound that contracts into a natural spoken form.

## Core Goals

- **Phonetically simple:** globally pronounceable, one letter per sound, fixed stress on the first syllable
- **Compositionally transparent:** words are built from audible conceptual parts, not memorized atoms
- **Domain-extensible:** new conceptual fields emerge by combining existing primitives; the language doesn't break when knowledge expands
- **Minimal irregularity:** grammar and morphology are regular by default; exceptions require justification

---

## Sounds

**17 consonants:** `p b t d k g m n s z l r f h y w v`

**5 vowels:** `a e i o u` — one letter, one sound, no exceptions. Stress always falls on the first syllable.

The apostrophe `'` is the only other written character. It is a prosodic juncture marker (see [§ Apostrophe](#apostrophe-grouping-marker) below), not a phoneme.

---

## Phonological Tiers

Every word in Tonesu belongs to one of four tiers. The word shape itself tells you what kind of thing it is:

| Shape | Tier | What lives here | Admission rule |
|-------|------|-----------------|----------------|
| CV | Primitives | The 34 foundational roots (`mu`, `ki`, `go`…) | Passes all primitive validation criteria — closed set |
| CV-CV+ | Compounds | Open vocabulary built from primitives (`zo-se-so`, `to-ne-su`…) | Expressible by assemblage from existing roots |
| CVC | Lexical descriptors | Digits, colors, scale prefixes | Closed-class categories needing fast phonological recognition |
| CVCC | Exceptional anchors | Mathematical/physical constants (`varn`, `werm`…) | Assemblage genuinely impossible; convention-defined with no compositional expression |

**The Assemblage-First Rule:** the default for any concept — however complex — is always compositional assemblage. A long compound is not grounds for a new lexical atom. CVCC is the pressure valve for concepts that literally cannot be composed from primitives: irrational numbers, transcendental constants, SI-convention units.

---

## The 34 Primitives

The primitive set is the closed ontological root vocabulary. Every compound is built from these. A new primitive requires strong justification; the set is near-closed.

### Entities and Substances

| Root | Gloss | Notes |
|------|-------|-------|
| `mu` | object / artifact | physical non-living artifact, tool, device |
| `ma` | matter / substance | raw unformed material, physical substrate |
| `zo` | living thing | any organism: animal, plant, fungus, microbe |
| `li` | social agent / person | conscious intentional actor; `zo+li` = human person; `mu+li` = AI/institution |

### Processes and Change

| Root | Gloss | Notes |
|------|-------|-------|
| `ki` | motion | physical movement, displacement, travel |
| `ka` | intentional action | deliberate act, operation, exertion of will |
| `be` | growth / increase | building up, emergence, gain |
| `de` | decay / decrease | breaking down, entropy, loss |

### Space, Structure, and Pattern

| Root | Gloss | Notes |
|------|-------|-------|
| `pa` | place / space | location, region, physical topology |
| `su` | structure / order | physical arrangement, organization, system |
| `to` | conceptual pattern / thought | idea, plan, model, logic, knowledge |
| `fe` | boundary / limit | edge, category, distinction, threshold |
| `di` | direction | toward, away, path, orientation |
| `ko` | containment / interior | inside, enclosed space, container |

### Relations and Logic

| Root | Gloss | Notes |
|------|-------|-------|
| `ne` | relation / connection | link, bond, membership, network |
| `pe` | part / component | piece, element, member of a whole |
| `go` | cause / origin | reason, source, trigger |
| `du` | result / effect | outcome, product, consequence |
| `zi` | mutual / coupling event | bilateral transformation — both participants changed by their engagement; mating, symbiosis |

### Perception and Signal

| Root | Gloss | Notes |
|------|-------|-------|
| `se` | perception / sense | raw sensory awareness: sight, hearing, touch, detection |
| `so` | sound | acoustic signal, spoken signal, audio |
| `lu` | light / visibility | visual signal, illumination |
| `si` | signal / representation | any encoded information: symbol, sign, data, language, code |

### Energy and Force

| Root | Gloss | Notes |
|------|-------|-------|
| `ra` | energy / force | power, charge, capacity to cause change |
| `ha` | heat / thermal state | temperature, warmth, thermal intensity; distinct from `ra` |

### Quantity and Time

| Root | Gloss | Notes |
|------|-------|-------|
| `nu` | quantity / number | count, measure, amount |
| `ru` | unity / singularity | one, individual, whole |
| `pu` | plurality / collective | many, group, set |
| `re` | repetition / cycle | recurrence, rhythm, iteration |
| `ti` | time / sequence | moment, duration, order of events |

### Mind, Value, and Behavior

| Root | Gloss | Notes |
|------|-------|-------|
| `vo` | value / quality | worth, evaluation, degree, intensity |
| `wi` | will / intention | goal, desire, purpose |
| `no` | negation / absence | not, lack, removal |

### Affective Substrate

| Root | Gloss | Notes |
|------|-------|-------|
| `fa` | affective substrate | inward-facing felt-interior of organism state; `se` is outward detection, `fa` is inward substrate |

---

## Grammar Particles

Short, phonetically distinct syllables that mark grammatical roles. They prefix the element they mark (e.g. `la-mi`, `lo-zo`).

| Particle | Role | Notes |
|----------|------|-------|
| `la` | perspective anchor / agent | initiator in action clauses; stance-holder in epistemic clauses |
| `lo` | patient | the affected object |
| `ro` | instrument | the tool, medium, or cause |
| `pa` | location | where the action occurs — transparent overlap with root `pa` |
| `ne` | recipient / relational | who receives; also marks relational arguments — transparent overlap with root `ne` |
| `ta` | time reference | temporal anchor |
| `ka` | action marker | marks the verb/predicate — transparent overlap with root `ka` |
| `na` | proper name marker | signals an identifier, not a compositional noun |
| `da` | domain marker | always bound prefix; never a free particle; `da-to-ki` not `da [noun]` |

**Default sentence order: Subject–Object–Verb (SOV)**

```
la-mi   lo-mu   ka-be       →  I grow the object.
la-li   lo-to   ka-ko       →  The person stores the knowledge.
```

### Pronouns

| Form | Gloss |
|------|-------|
| `mi` | I / me (1st person singular) |
| `tu` | you (2nd person singular) |
| `ze` | they / them (3rd person singular) |
| `yu` | we / they (group / plural) |

---

## Compounding

**Head-final: modifier precedes core concept.** The last element is always the semantic head. Parse is right-branching by default.

```
zo-se-so    →  [zo [se [so]]]  =  organism that perceives sound  =  acoustic animal
to-ne-su    →  pattern–relation–structure  =  Tonesu (the language)
```

For multi-part compounds:
```
[domain/class] + [function] + [head]
```

---

## Derivational Suffixes

Suffixes that shift a root into a different lexical role. Regular, no exceptions. **Maximum one derivational suffix per lexical unit** — restructure as a compound if more specificity is needed.

| Suffix | Role | Example |
|--------|------|---------|
| `-li` | agent (one who does) | `ka-li` → actor / agent |
| `-mu` | device / instrument | `si-mu` → information device |
| `-pa` | location | `ka-pa` → place of action |
| `-su` | result / product / state | `be-su` → what was grown / the grown thing |
| `-to` | abstract nominalization | `ka-to` → the concept of action |
| `-ge` | quality / property | `ra-ge` → energetic |
| `-ki` | verbal noun / inchoative | `be-ki` → the act of growing; entering a state |

---

## Apostrophe Grouping Marker

The `'` marks the **left boundary of a subcompound**. It is a prosodic juncture — a slight phrasal pause — not a phoneme.

**Default parse is right-branching.** In a plain hyphenated chain, each element modifies the accumulating chain from left to right:

```
A-B-C-D    →   A modifies [B modifies [C modifies D]]
```

**`'` overrides the default parse:**

```
ker-zo-se-so    →  ker modifies [zo-[se-[so]]]   (color attaches to the innermost element — WRONG)
ker'zo-se-so    →  ker modifies [zo-se-so]        (color attaches to the whole kind-term — CORRECT)
```

**Two functions:**

1. **Depth management** — optional at compound depth ≤ 4 where the parse is clear; expected at depth ≥ 5 or when X-X repetition appears inside a longer compound.
2. **Re-scoping** — required when the default right-branching parse produces a wrong reading. In `ker'zo-se-so`, `'` is not stylistic; it changes the meaning.

Multiple `'` markers are permitted. Role-marker particles (`la-`, `lo-`, etc.) attach outside the grouping mechanism: `la-ker'zo-se-so` = agent:[ker modifies [zo-se-so]].

---

## Organism Kind-Term Taxonomy

Kind terms for living things and inorganic matter are built by compounding `zo` or `ma` with perceptual/structural primitives. The tree below shows the established nodes; the `'` rule makes every node a valid base for further discrimination.

### Living Things (`zo`)

```
zo  (living thing)
│
├── zo-se-[x]  Perceptual organism — axis: defining sensory mode
│   │
│   ├── zo-se-so  Acoustic organism (genus term)
│   │   │
│   │   ├── zo-se-so-fe  territorial / cat class (Felidae)
│   │   ├── zo-se-so-li  pack-social / dog class (Canidae)
│   │   ├── zo-se-so-di  directional / bird class (Aves)
│   │   └── zo-se-so-pa  place-acoustic / whale (Cetacea)
│   │
│   ├── zo-se-ma  matter-perceptual / fish & aquatic vertebrates
│   └── zo-se-ne  social-relational / herd ungulates
│
├── zo-su  structural organism / plants
├── zo-pe  component organism / arthropods & invertebrates
└── zo-ne  networked organism / fungi
```

*`zo-li` (human-class organism) is not a corpus test target — humans appear as the pronouns `mi`, `tu`, `ze`, `yu` and the nominal `li` throughout.*

**Depth is unbounded.** Any node is a valid discrimination base. A discriminator subcompound prepends with `'` and scopes over the whole base:

```
[discriminator]'[base-class]
```

Example depth chain:

```
zo-se-so                               acoustic organism (genus)
  [behav]'zo-se-so                     a behavioral subgroup of that genus
    [feature]'[behav]'zo-se-so         a further-specified member
      [variant]'[feature]'[behav]'zo-se-so   individual variant (coat, region…)
```

**Discriminating off intermediate nodes.** Organisms that do not cleanly fit a terminal fourth root (`-li`, `-fe`, `-di`, `-pa`) attach directly to the nearest accurate parent. A fox is neither pack-social (`-li`) nor territorial-feline (`-fe`); the fox discriminator attaches to `zo-se-so` directly (`[fox-discrim]'zo-se-so`), and fox subspecies stack further on top of that.

### Inorganic Matter (`ma`)

```
ma  (matter/substance)
├── ma-su  structured matter / rock & mineral
├── ma-pa  place-matter / soil & sediment
└── ma-ki  flowing matter / water
```

Full corpus provenance with batch codes and sentence ranges: [corpus/sentences/index.md](corpus/sentences/index.md).

---

## Numerals

Digits occupy the CVC tier and are phonologically distinct from all CV primitives. The quantity primitive `nu` anchors all counting expressions.

### Digit Inventory

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| `nil` | `bol` | `bun` | `gal` | `mol` | `hin` | `wes` | `yom` | `fon` | `zan` |

### Cardinals

```
[digit]  nu  [noun]           →  single digit
[digit][digit]  nu  [noun]    →  positional chain, most-significant first

gal nu mu          →  3 objects
hin nu li          →  5 people
bun gal  nu  zo    →  23 organisms
```

### Ordinals

```
[digit]  ti                  →  nth in sequence

bol ti  →  first
bun ti  →  second
gal ti  →  third
```

### Measurement

```
[digit]  [scale]  nu  [domain]

hin  pir  nu  pa   →  5 kilo-space  (= 5 km)
gal  nu  ti        →  3 units-of-time  (≈ 3 seconds)
```

Base SI domains: `nu pa` (meter) · `nu ti` (second) · `nu ma` (kilogram) · `nu ha` (kelvin) · `nu ra` (force) · `nu lu` (luminosity) · `nu so` (sound) · `nu si` (bit)

### Fractions

```
ru-pu  [d]          →  1/d    (one of d)
[n]  ru-pu  [d]     →  n/d    (n of d)

ru-pu bun           →  1/2
bun ru-pu gal       →  2/3
gal ru-pu mol       →  3/4
```

`ru` (unity) + `pu` (plurality) = fractional unit constructor.

### Time Units

| Unit | Form | Construction |
|------|------|--------------|
| hour | `re-ti` | recurring time unit |
| minute | `re-ti-de` | diminished recurring time |
| day | `re-ti-be` | extended recurring time |
| year | `hulm` | CVCC anchor (see below) |

---

## Colors

Color vocabulary was formally admitted in COL-001 (March 2026). All forms are CVC atoms on the same phonological tier as digits.

### Core hues

| Color  | Form  |
|--------|-------|
| black  | `yel` |
| white  | `yim` |
| red    | `ker` |
| green  | `gim` |
| blue   | `pom` |
| yellow | `sam` |

### Extended hues

| Color | Form  | Notes |
|-------|-------|-------|
| brown | `kus` | no clean compositional form |
| orange | — | composes as `ker zi sam` (red + yellow blend) |
| purple | — | composes as `ker zi pom` (red + blue blend) |

### Visual-pattern modifiers

Named patterns of light distribution on surfaces. Compositional compounds, not CVC atoms; follow the same head-final rule and require `'` when scoping over multi-root kind-terms.

| Compound | Pattern     | Basis |
|----------|-------------|-------|
| `lu-di`  | stripe / linear | `lu` (light) + `di` (direction) |
| `lu-pe`  | spot / dappled  | `lu` (light) + `pe` (component) |
| `lu-fe`  | solid / uniform | `lu` (light) + `fe` (boundary) |

### `no-lu` vs `yel`

| Form    | Reading               | Use |
|---------|-----------------------|-----|
| `yel`   | black (named hue)     | Color attribution: `yel mu` = a black object |
| `no-lu` | dark / absence of light | Coat or surface property: `no-lu'zo-se-so-fe` = dark-coated cat |

In formal register the distinction holds; in casual speech they overlap.

---

## CVCC Exceptional Anchors

Forms that pass the Assemblage-First Rule: concepts that have no compositional expression because they are irrational, transcendental, or defined by measurement convention.

### Mathematical Constants

| Form | Constant | Value |
|------|----------|-------|
| `varn` | π | 3.14159… — circle circumference/diameter ratio |
| `worn` | τ (tau) | 6.28318… — full-turn circle constant (2π) |
| `werm` | e (Euler) | 2.71828… — natural logarithm base |
| `vins` | φ (golden ratio) | 1.61803… — (1+√5)/2 |
| `valm` | √2 | 1.41421… — Pythagorean constant |
| `walf` | i (imaginary unit) | √(−1) — complex plane rotation unit |

### Physical Constants

| Form | Constant | Value |
|------|----------|-------|
| `vern` | c (speed of light) | 299,792,458 m/s — exact by SI definition |
| `birm` | ħ (reduced Planck) | 1.055×10⁻³⁴ J·s — quantum of action |
| `velf` | G (gravitational) | 6.674×10⁻¹¹ N·m²/kg² |
| `holm` | k_B (Boltzmann) | 1.381×10⁻²³ J/K — thermal energy per kelvin |
| `vils` | e (elementary charge) | 1.602×10⁻¹⁹ C |
| `yolm` | α (fine structure) | ≈1/137 — electromagnetic coupling |
| `wels` | mole (Avogadro) | 6.022×10²³ — SI counting unit |
| `telf` | ampere | SI base unit for current |

### Astronomical and Physical Anchors

| Form | Constant | Value |
|------|----------|-------|
| `holf` | AU | 1.496×10¹¹ m — Earth-Sun distance |
| `yarm` | parsec | 3.086×10¹⁶ m — parallax-arcsecond unit |
| `hulm` | year (Julian) | 31,557,600 s — Earth orbital period |
| `dolm` | electron mass m_e | 9.109×10⁻³¹ kg |
| `dolf` | proton mass m_p | 1.672×10⁻²⁷ kg |

Usage: `[digit] nu [CVCC]` — e.g. `bun nu yarm` = 2 parsecs.

---

## Key Grammar Patterns

### Causal Frame Family

```
go [cause]  matrix              →  because [cause], [matrix]
to-go [X]  Y                    →  even if X, still Y  (counterfactual)
no-go [X]  Y                    →  although X, Y  (concessive)
```

### Purpose Frame

```
wi [clause]  matrix             →  in order to [clause], [matrix]
```

### Temporal Frame

```
ta  [time-reference]  clause    →  at/in [time], [clause]
```

Time references: `ti-de` (past) · `ti-be` (future) · `ti-re` (cyclic/recurring) · `ti-fe` (deadline)

### Questions

```
to-si  in argument slot         →  content question (who/what/where)
to-si  —  clause                →  polar question (yes/no); fronted
```

### Negation

```
no-[compound]                   →  negated compound
no [ka-clause]                  →  sentence-level negation
[A]  no  [B]                    →  contrastive: A rather than B
```

### Habitual Aspect

```
re-[verb]                       →  habitual/recurring action (prefix)
```

### Epistemic Scale

Three grades of belief, composable with `no-`:

```
se   →  I perceive it (sensory basis)
si   →  I have a signal for it (inferential)
to   →  I model it (cognitive commitment)
```

---

## Punctuation and Notation Marks

Four sentence- and phrase-level marks. None are compound-internal — `'` remains the only mark inside a compound.

| Mark | Name | Function |
|------|------|----------|
| `,` | clause separator | pause between a frame clause and its matrix, or between list items |
| `!` | exclamation | end-of-utterance: heightened affect or emphasis |
| `?` | question mark | end-of-utterance: interrogative; orthographic counterpart to `to-si` |
| `~` | approximation | pre-positional hedge: "approximately / roughly / something like" |

**`,` with frames:** `ta ti-de, la-mi lo-mu ka-be` = In the past, I grew the object.

**`?` usage:** `to-si` is the grammatical question mechanism; `?` is its written-form counterpart. In casual register, `?` alone marks a polar question without requiring the fronted `to-si`.

**`~` with numerals:** `~gal nu li` = about 3 people · `~hin pir nu pa` = roughly 5 km · `~bol nil nil nil nu hulm` = on the order of 1,000 years

**`~` with concepts:** `~zo-li` = something like a person · `~ta ti-be` = roughly "sometime later"

---

## Examples

### Compound Words

Compounds are written solid — no separators. The apostrophe `'` is the only non-letter character that may appear inside a compound.

**Simple compounds**

| Word | Construction | Reading |
|------|-------------|---------|
| `toli` | to · li | knower, scholar |
| `libe` | li · be | child — person in growth phase |
| `rasu` | ra · su | star — structured energy body |
| `zoma` | zo · ma | organic matter, wood |
| `toki` | to · ki | computation, learning, reasoning |
| `rage` | ra · -ge | energetic (quality suffix) |
| `beki` | be · -ki | beginning to grow (inchoative suffix) |

**Longer compounds**

| Word | Construction | Reading |
|------|-------------|---------|
| `tonesu` | to · ne · su | Tonesu — the language |
| `sumuli` | su · mu · -li | engineer — one who structures artifacts |
| `tosumu` | to · su · mu | database, library |
| `rakimu` | ra · ki · mu | engine, motor, generator |
| `tofeli` | to · fe · li | epistemic guardian |
| `sikomu` | si · ko · mu | information-storage device |
| `tokomu` | to · ko · mu | memory device |

### Apostrophe in Action

Default parse is right-branching. `'` pre-binds the subunit to its right before the left-side modifier attaches.

Re-scoping — the same roots, two different meanings:

```
kerzoseso       ker → [zo → [se → so]]   modifier reaches only the deepest root  (wrong)
ker'zoseso      ker → [zoseso]           modifier covers the whole kind-term      (correct)
```

*(ker = future color form, pending COL-001)*

Depth management — naming two subunits explicitly:

```
rasuluvo        ra → [su → [lu → vo]]    one right-branching chain
rasu'luvo       [rasu] → [luvo]          stellar quality-of-light
```

Multiple apostrophes — each binds the subunit to its right in turn:

```
toki'tofe'sumuli   →   [toki] modifies [[tofe] modifies [sumuli]]
                   =   computational-epistemic engineer
```

### Sentences

**Basic sentences**

| Sentence | Meaning |
|----------|---------|
| `lalibe loma kako` | The child drinks water. |
| `larasu lolu be` | The star emits light. (`be` without `ka` = non-intentional process) |
| `lazoli losikumu kabe` | People create information-storage devices. |
| `lami losi kanoko` | I did not store the data. (`kanoko` = action:not-contain) |
| `latu katoki!` | You're computing! |

**Multi-clause sentences**

| Sentence | Meaning |
|----------|---------|
| `go lasi kaneki, lato kabe` | Because information connects, knowledge grows. |
| `ta layu katoki, lato kabe` | When they study, knowledge grows. |
| `lami kabe lomu wi latu kamuka` | I built the machine for you to use. |
| `laze losi kasiki wi kafesi neyu` | She sent the signal to warn them. |
| `togo larasu noki, lato kabe` | Even if the star doesn't move, knowledge grows. |
| `nogo larasu ki, lato kabe` | Although the star moves, knowledge grows. |

**CVC digits and CVCC anchors**

| Expression | Meaning |
|-----------|---------|
| `gal nu li` | 3 people |
| `bun ti` | 2nd (ordinal) |
| `hin pir nu pa` | 5 km (CVC digit + CVC scale prefix + nu + domain) |
| `bun rupu gal` | 2/3 |
| `ta bun ti retibe, larasu lolu be` | On the second day, the star emitted light. |
| `lami katoki lovarn` | I computed π. (`varn` = CVCC anchor) |
| `lazoli ki bun nu holf` | The people traveled 2 AU. (`holf` = CVCC anchor) |

**Questions and approximation**

| Sentence | Meaning |
|----------|---------|
| `latu lotosi katoki?` | What did you compute? (`tosi` in object slot = content question) |
| `tosi latu katoki lovarn?` | Did you compute π? (`tosi` fronted = polar question) |
| `lami katoki lo ~varn` | I computed approximately π. |
| `~gal nu li ki` | About 3 people moved. |

---

## Repository Structure

```
spec/               Normative rules — language changes happen here
  phonology.md      Sound system, syllable structure, tier rules
  grammar.md        Sentence structure, particles, clause syntax
  morphology.md     Derivational suffixes, number, tense/aspect
  word-formation.md Compounding rules, apostrophe, entry schema
  principles.md     Core design commitments and guards
  domain-creation.md  How to declare a domain namespace
  naming.md         Named-entity conventions
registry/           Vocabulary registry
  primitives.md     The 34 primitive roots with full annotations
  roots.md          CVC/CVCC descriptor inventory
  derived.md        Compound entries (W-series)
  domains.md        Registered domain namespaces
corpus/             Test sentences and conversations
notes/              Design rationale, semantic map, open questions, history
  cvc-inventory.md  Digit, scale prefix, and CVCC anchor tables
  semantic-map.md   Conceptual domain organization
  open-questions.md Live design question tracker
  prior-art.md      Relationship to Esperanto, Lojban, Toki Pona, etc.
```

## Where to Go Deeper

| Topic | File |
|-------|------|
| Core design commitments and guards | [spec/principles.md](spec/principles.md) |
| Full sound system and tier rules | [spec/phonology.md](spec/phonology.md) |
| Sentence structure and all grammar patterns | [spec/grammar.md](spec/grammar.md) |
| Derivational suffixes, aspect, number | [spec/morphology.md](spec/morphology.md) |
| Compounding rules and apostrophe detail | [spec/word-formation.md](spec/word-formation.md) |
| All 34 primitives with full annotations | [registry/primitives.md](registry/primitives.md) |
| Digit, scale prefix, and CVCC tables | [notes/cvc-inventory.md](notes/cvc-inventory.md) |
| Domain namespaces | [registry/domains.md](registry/domains.md) |
| Open design questions | [notes/open-questions.md](notes/open-questions.md) |
| Conceptual domain map | [notes/semantic-map.md](notes/semantic-map.md) |
| Design history | [notes/design-history.md](notes/design-history.md) |
| Prior art | [notes/prior-art.md](notes/prior-art.md) |

## Current State (March 2026)

| Area | Status |
|------|--------|
| Spec | Principles, phonology, grammar, morphology, word-formation, domain-creation, naming — all drafted and in active use |
| Primitives | 34 roots admitted; set near-closed |
| Vocabulary | ~100 registered compounds (W-series); active, proposed, and cold entries tracked |
| Corpus | 251 numbered sentences + 7 multi-turn conversations |
| Open questions | ~20 tracked items across phonology, grammar, ontology, and domains |
| CVCC anchors | 19 forms assigned (6 math, 8 physics, 3 astro/time, 2 atomic mass) |
| Colors | 7 CVC atoms admitted (COL-001, March 2026); visual-pattern compounds corpus-attested |

## Prior Art

This project combines ideas from Esperanto (agglutinative phonetic grammar), Lojban (logical grammatical structure), Toki Pona (semantic primitive composition), and formal ontologies (domain namespaces). See [notes/prior-art.md](notes/prior-art.md).
