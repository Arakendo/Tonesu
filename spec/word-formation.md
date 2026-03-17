# Word Formation

## Status: Draft

> **Notation convention:** Hyphens in all examples throughout this document are **analytic notation** — they mark morpheme boundaries for analysis and teaching, and are not written in Tonesu. Written Tonesu is solid: `tofesuki`, not `to-fe-su-ki`. The apostrophe `'` is the only normative non-alphabetic character within a compound. See § Written Form below.

---

## Core Principle

Words are not looked up — they are built. The system is generative: a speaker who knows the primitives and rules can construct and interpret unfamiliar words without a dictionary.

---

## Compound Order Rule

**Head-final: modifier precedes core concept.**

```
{modifier} + {core concept}
```

For multi-part compounds:
```
{domain/class} + {function} + {head concept}
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

**Stacking order:** when multiple derivational markers apply, the order is **root → semantic modifier → role marker**. The semantic modifier (`-su`, `-ki`, `-to`, `-ge`) transforms the concept first; the role marker (`-li`, `-mu`, `-pa`) then specifies how that transformed concept is instantiated.

```
to-ki-mu   →   knowledge-change (to-ki) + device (-mu)   =   computing device
to-ki-li   →   knowledge-change (to-ki) + agent (-li)    =   learner
```

Stacking more than one role marker on the same base is disallowed; restructure as a compound instead (`ka-li-su` = governance, not `*ka-li-li-su`). Maximum one derivational suffix per lexical unit before compounding is required — rule is in spec/morphology.md § Derivational Suffix Limit.

---

## V-Prefix Scope Modifiers

Admitted March 2026 (VPC-001). A V-prefix is a **scope-modifier** that precedes a root or compound at word-initial position. It does not add independent lexical content; it shifts the *register, granularity, or mode* of the following root. All 5 bare-vowel forms are admitted.

| Prefix | Scope effect | Example |
|--------|-------------|--------|
| `a-` | abstract/universal — root at broadest conceptual category | `a-to` (knowing-in-general), `a-su` (form-as-such), `a-to-li` (sage) |
| `i-` | particular/precise — root as a discrete, specified instance | `i-to` (this specific fact / particular epistemic object) |
| `u-` | interior/foundational — the tacit or underlying mode of root | `u-to` (interior/tacit knowing), `u-su` (deep structure) |
| `o-` | collective/distributed — root as property of group-as-unit | `o-li` (community-as-unit; ≠ `pu-li` count-of-persons) |
| `e-` | emergent/transitional — root in an unsettled, forming state | `e-ki` (emergent/progressive change; imperfective aspect) |

**Parse rules:**
- Position: word-initial only (parse invariant 1 — mid-compound bare-V violates consonant-onset requirement). V-prefixes cannot appear inside a compound; their position is always structurally unambiguous.
- Right-branching: the V-prefix scopes over everything to its right in the same compound. `a-to-li` = `a-[to-li]` = universal-(knowledge-agent) = sage.
- Written form: solid in ordinary prose — `ato`, `ito`, `uli`, `oki`, `eki`. Morpheme-boundary notation: `a-to`, `i-to`, etc.
- Role-marker interaction: role particles (`la-`, `lo-`) are outside-word and do not interact with V-prefix structure. `lo-a-to` = patient:universal-knowing. `la-a-to` is hazardous — see constraint below.

**Known problem 1 — `a-` merge hazard:** `la-` ends in `a`; `la-a-X` collapses to `la-X` in fast speech (vowel-identity merger). The merged and intended readings are structurally different and not recoverable from context. **Rule: `a-` forms should be used in predicate or patient position, not agent position after `la-`.** The other four prefixes (`i- u- o- e-`) do not share this hazard.

**Known problem 2 — over-generation:** V-prefixes are combinatorially productive across all roots (~5 × 34 minimal compounds, plus all multi-root extensions). This could swamp the lexicon with redundant or speculative forms. **Throttle rule: V-prefixed forms are not vocabulary entries by default.** Any V-prefixed form is readable from context using the scope semantics above; it does not need to be registered to be used. Registry admission requires: (a) the scope-shifted meaning is not paraphraseable by any existing compound without semantic loss, AND (b) the form has ≥ 3 corpus attestations in distinct contexts. Use freely in corpus; register sparingly.

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

## Semantic Operator Patterns

Tonesu compounds are not arbitrary pairings. Many primitives, when used as the **head** of a compound (the rightmost element), function as **semantic operators**: they transform the modifier's meaning in a predictable, domain-general way. These patterns are extracted from registry usage and are normative default readings.

**The default algebraic reading applies unless overridden by a registered specialized meaning.** Registered entries may develop stable specialized readings narrower than the algebraic default (e.g. `ra-su` = "star" rather than the bare algebraic "energy structure") — but the specialized reading *inherits from and does not contradict* the default.

### Productive operator heads

| Head | Operator reading | Example | Gloss |
|------|-----------------|---------|-------|
| `su` | structured system / framework of X | `to-su` | organized knowledge |
| `ki` | process / transition / activation involving X | `to-ki` | learning (knowledge-change) |
| `fe` | boundary / limit / threshold of X | `to-fe` | epistemic threshold |
| `li` | agent whose domain is X | `to-li` | scholar (knowledge-agent) |
| `mu` | artifact / instrument of X | `to-ki-mu` | computing device (process-artifact) |
| `ge` | property characterized by X | `ra-ge` | energetic |
| `ne` | relational link / coupling involving X | `si-ne` | communication (signal-relation) |
| `be` / `de` | growth / decay phase of X | `fa-be` · `fa-de` | affect rising · affect fading |
| `re` | recurring cycle / repeating instance of X | `ti-re` | recurring time, scheduled cycle |
| `zi` | bilateral coupling event of X | `zi-ka` | intentional exchange |
| `no-` | absence / negation of X (prefix) | `no-fe` | no boundary (unbounded) |

**`no-` note:** `no-` is a prefix operator, not a head. It negates the immediately following root or compound. Listed here because it participates in compound algebra as a productive modifier slot.

### Productive operator modifiers (left-slot patterns)

Some primitives in the **modifier position** (left slot) also produce predictable readings:

| Left slot | Effect on head | Example | Gloss |
|-----------|---------------|---------|-------|
| `to` (as modifier) | hypothetical / model-layer version of HEAD | `to-go` | hypothetical causal frame |
| `ka` (as modifier) | deliberate / intentional version of HEAD | `ka-de` | deliberate destruction |
| `no` (as modifier) | negated / absent version of HEAD | `no-ha` | cold (absence of heat) |
| `re` (as modifier) | habitual / repeating version of HEAD | `re-ki` | habitually moves |

### Three stages of compound meaning

Every registered compound passes through up to three interpretive stages:

**1. Compositional** — meaning read directly from primitives by the head rule and operator patterns above. Any speaker who knows the primitives can derive this reading. No registry entry required.

```
se-no-to   →   perception + absence + knowledge   =   signal without model
```

**2. Algebraic default** — meaning follows a recognized operator pattern in the table above. Predictable across the whole class; the pattern itself is what is learned, not each instance.

```
X + fe   →   boundary / limit of X
to + fe  →   epistemic threshold
wi + fe  →   intentional limit / ethical constraint
ti + fe  →   temporal deadline
```

**3. Registry-stabilized** — corpus usage has confirmed a specific reading, which may be narrower than the algebraic default. The specialization is registered; the algebraic reading remains valid in non-registered contexts.

```
ra-su   algebraic: energy structure
        registry:  star (W015) — stable specialized reading in astronomy domain
```

### When to apply `'` for algebraic clarity

Because the operator pattern table defines predictable heads, the need for `'` can be stated in algebraic terms:

- **Use `'`** when the intended head is not the terminal root of the compound — i.e., when an operator pattern applies to an internal subunit rather than to the whole remaining chain.
- **Use `'`** when a modifier would otherwise be read as applying to only the terminal element rather than to a multi-root algebraic unit.
- **A compound is a candidate for `'` or for restructuring** when its terminal root is a weak head (a primitive without a strong operator reading) and the semantic weight rests on an internal subunit.

```
ker-zo-se-so     →  ker modifies {so} only (wrong)
ker'zo-se-so     →  ker modifies {zo-se-so as algebraic unit} (correct)
```

The full structural rules for `'` are in § Compound Grouping Marker below.

---

## Compound Grouping Marker

**Default parse: right-branching.**

In a plain compound chain, each element modifies the accumulating chain from left to right (analytic form: `A-B-C-D`). The last element is always the semantic head.

```
A-B-C-D   →   A modifies {B modifies {C modifies D}}
```

**Grouping marker: `'` (apostrophe)**

When a compound's default right-branching parse is ambiguous or when a subunit must be understood as a whole before being modified, `'` marks the left boundary of that subcompound.

```
A'B-C-D   →   A modifies {B-C-D as a pre-bound unit}
A-B'C-D   →   {A-B as a plain chain} modifies {C-D as a pre-bound unit}
```

The elements from `'` to the end of the compound (or the next `'` if present) form the subcompound. Everything to the left then attaches to that subcompound as a modifier.

**Usage policy:**

- Omit for compounds of 2–3 roots where the parse is unambiguous.
- Optional at depth-4 where structure is still clear from primitive meanings alone.
- Expected when X-X repetition appears inside a longer compound (X-X creates genuine parse ambiguity at depth ≥ 4 because the repeated roots can be read as either a meta-level unit or the start of a plain chain).
- **Re-scoping function:** `'` is not solely a depth-management device. When a modifier's default right-branching parse would produce a wrong reading, `'` actively re-scopes the modifier over the pre-bound subunit. Example: `ker-zo-se-so` (no apostrophe) right-branches as *ker modifies {zo-{se-{so}}}*, attaching the color to the terminal root rather than to the organism as a whole. `ker'zo-se-so` binds `zo-se-so` first, then attaches `ker` correctly over the whole kind-term. In such cases `'` is required for correctness, not merely for clarity at depth. The mechanism works identically over 3-root and 4-root units.
- Multiple `'` markers are permitted. Each additional apostrophe increases cognitive parse load; casual and spoken registers will naturally avoid deep nesting. Technical, alchemical, and formal registers may use as many as the compound structure requires.
- Phrase restructuring using connective particles (e.g. `ne`) remains available and is preferred in speech when depth makes the compound unwieldy.
- **Depth guideline:** 2–4 roots are the normal range for a single compound. At depth 5+, prefer `'` grouping if the parse is still unambiguous, or restructure as a multi-word phrase. Depth is not a hard limit — technical and formal registers routinely exceed it — but compounds longer than 4 roots without `'` are a signal to pause and check whether the intent is clear.

**Role-marker interaction:** role-prefix particles (`la-`, `lo-`, etc.) attach to the outer NP boundary and do not participate in the `'` grouping mechanism. The role-marker is outside-NP; `'` is NP-internal. The two levels are orthogonal: `la-ker'zo-se-so` = agent:{red-{kind-term}}, with no conflict.

**`~` interaction:** the approximation mark `~` may appear immediately after `'`, scoping over only the introduced subcompound. In written form: `A'~BC` = A modifies {approximately BC}; distinct from `~A'BC` = approximately {A-BC as a whole}. `~` cannot interrupt a solid compound (no `'` boundary present). See spec/phonology.md § Approximation Mark for the full scope semantics and example pair.

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

**The only normative non-alphabetic character in a written *compound* is `'`** (the prosodic juncture marker, § Compound Grouping Marker). `'` is structural: it encodes prosodic grouping that bare letter sequences cannot. Hyphens encode nothing; they are readability aids that a writer may add or omit at will.

This gives Tonesu three layers with distinct functions:

| Layer | Device | Role |
|-------|--------|------|
| Spoken morphology | none | continuous phonological word |
| Structural grouping | `'` | prosodic boundary, left edge of subcompound |
| Analytic clarity | `-` | optional notation in specs, teaching, glosses |

Because hyphens carry no grammatical meaning, written forms strip cleanly: `to'semaka` and `to'se-ma-ka` are the same word. Within a compound, the apostrophe is the only mark that matters.

**At sentence and discourse level,** four additional marks operate at or between word boundaries: `,` (clause separator), `!` (exclamation), `?` (question), `~` (approximation). `,`, `!`, and `?` are strictly external to compounds. `~` is external to compounds but may attach immediately after `'` — the only written character that creates an internal left edge — giving `A'~BC` (approximately the subcompound). See spec/phonology.md § Punctuation and Notation Marks and § Approximation Mark.

**Mathematical expressions:** Tonesu uses standard international mathematical notation (Arabic digits 0–9, operators `+  −  ×  ÷  =  <  >  ^`, parentheses, etc.) for standalone expressions and inline formulas. CVC digit and CVCC constant forms are the *spoken* and *prose* representations — for counting, measurement, and embedding quantities in sentences. When a formula needs to appear as a formula, you write `3 + varn = 3 + 3.14159…` not `gal pa ne varn nu pa-re`. The two registers do not conflict: prose Tonesu speaks quantities via CVC; displayed math writes them via universal symbology. This applies to all technical and scientific writing where equations appear as distinct display elements rather than as sentence constituents.

---

## CVC Descriptor Modifiers

CVC-tier forms — colors, digits, and scale prefixes — function as **pre-nominal modifiers** in the compound system. The same head-final rule applies: the descriptor precedes the noun or compound it modifies.

```
{color}  {noun}          →  ker mu      (red object)
{scale}  nu  {domain}    →  pir nu pa   (kilometer)
{digit}  nu  {noun}      →  gal nu zo   (three organisms)
```

CVC forms are phonologically stratified from CV primitives: the coda signals tier membership instantly. A CVC color or digit is never misread as a primitive root in isolation.

**Modifier scope and `'`:** when a CVC color or visual-pattern modifier precedes a multi-root compound, `'` is required to prevent the default right-branching parse from attaching the modifier to only the terminal root rather than to the compound as a whole:

```
ker-zo-se-so   →  wrong: ker modifies only {so}
ker'zo-se-so   →  correct: ker scopes over {zo-se-so} as a unit
```

This is a specific instance of the `'` re-scoping function (§ Compound Grouping Marker). The rule is: **a CVC-tier modifier preceding a compound of two or more roots requires `'` between the modifier and the compound.**

**Visual-pattern compounds** (`lu-di` = stripe, `lu-pe` = spot, `lu-fe` = solid/uniform coat) are compositional compounds built from the `lu` (light/visibility) primitive, not CVC atoms. They function as pre-nominal modifiers under the same rule; `'` applies under the same conditions:

```
lu-di mu               →  striped object
lu-pe'zo-se-so-fe      →  spotted cat-class organism
lu-fe'pa-fe'zo-se-so-fe  →  solid-coated mountain-territory cat
```

**`no-lu` (dark/absence of light) as modifier:** the compositional compound `no-lu` expresses the property of being dark or light-absent. It is not the same as the CVC atom `yel` (black hue). `no-lu` is used when darkness is a feature or coat property of a thing; `yel` is used to name the specific perceptual hue point. Both are pre-nominal modifiers; `'` applies when either precedes a multi-root compound.

**Corpus basis:** S204–S207 (KNM-002) — `ker'zo-se-so`, `ker'zo-se-so-li`, color scoping confirmed in agent and patient positions. S255–S259 (KNM-003) — `lu-di`, `lu-pe`, and `no-lu` as pre-nominal modifiers on multi-discriminator Felidae kind-terms; three-apostrophe compound `nolu'lupe'maki'zosesof` (melanistic jaguar) is the maximum-depth attested example.

---

## Ergonomic Shortforms

Some CVC-tier forms have valid compositional expressions but are registered as shortforms on ergonomic grounds. These are a **distinct sub-class** within the CVC stratum — not closed-class descriptor atoms, and not CVCC exceptional anchors.

**Admission criteria — all four must be satisfied:**

1. **A compositional expression exists and is canonical.** The concept is expressible by assemblage from existing primitives. That expression remains the formal form — the shortform does not replace it.
2. **CVC phonology is assigned on pragmatic grounds.** The short form is admitted because it appears frequently in technical prose and spelling out the full expression creates genuine communicative friction, not stylistic inconvenience.
3. **The short form does not compete with or displace a closed-class CVC atom.** It must occupy a free CV stem not already blocked by digits, colors, or observational anchors.
4. **A new CV primitive is explicitly refused.** The concept is domain-specific vocabulary, not an ontological commitment warranting a primitive slot.

**Distinction from closed-class CVC atoms (digits, colors):**
Digits and colors are admitted because they define irreducible scale or perceptual anchor points — no compositional expression exists or is possible. Ergonomic shortforms do the opposite: they shorten an expression that already composes cleanly. The shortform is convenient; the compositional form is canonical.

**Distinction from CVCC exceptional anchors:**
CVCC requires that *no compositional expression exists*. Ergonomic shortforms have a canonical compositional expression and fail CVCC criterion 1. Assigning them CVCC would make them longer and send a false phonological signal that assemblage is impossible.

### Founding members: SI scale prefixes

All twelve SI scale prefix forms satisfy the four criteria above. Their compositional expressions are positional digit chains; the shortforms are registered because measurement expressions appear thousands of times per domain and the full chains are acoustically unwieldy.

| Form | Scale | Compositional expression | Tier note |
|------|-------|--------------------------|-----------|
| `zum` | nano (10⁻⁹)  | `nil nil nil nil nil nil nil nil nil bol nu {domain}` (positional chain) | ergonomic shortform |
| `mes` | micro (10⁻⁶) | positional digit chain × 10⁻⁶ | ergonomic shortform |
| `rim` | milli (10⁻³) | positional digit chain × 10⁻³ | ergonomic shortform |
| `pir` | kilo (10³)   | `bol nil nil nil nu {domain}` | ergonomic shortform |
| `baf` | mega (10⁶)   | positional digit chain × 10⁶ | ergonomic shortform |
| `wul` | giga (10⁹)   | positional digit chain × 10⁹ | ergonomic shortform |

Extended forms (`bim` pico, `les` tera) and Extended-Extended (`gul` peta through `hem` yotta) follow the same rule but are optional for most domains. Full inventory and free-stem accounting in `notes/anchor-inventory.md §Scale Prefix Inventory`.

**Future candidates** (femto, atto, sub-pico) and high-frequency time-cycle names may be admitted as ergonomic shortforms when corpus pressure justifies it. Each candidate must demonstrate all four criteria; admission is tracked under FLAG-CVC-010 in `notes/anchor-inventory.md`.

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

Colloquial forms are recorded in registry/colloquial.md and must trace back to their formal source.

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
Domain:       general | {named domain}
Examples:     2–5 sample usages
Related:      synonyms, narrower, broader, contrasts
Status:       proposed | accepted | lexicalized | deprecated
```

---

## Open Questions

- [x] ~~Decide separator convention at compound boundaries (none, hyphen in writing, pause in speech).~~ → **Resolved: solid spelling (no separator).** See § Written Form.
- [ ] Define maximum compound length before compression is required
- [x] ~~Confirm suffix order when multiple derivational markers stack~~ → **Resolved.** Order is root → semantic modifier → role marker. See § Derivational Markers.
