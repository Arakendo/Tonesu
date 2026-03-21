---
batch_codes: [LOJ-001]
---
# Translation Test: Lojban Type Contrasts

## Source
Canonical examples from:
- John Woldemar Cowan, *The Complete Lojban Language* (CLL), 1997. Definitive grammar reference.
- lojban.org canonical teaching examples; la lojban mailing-list examples.
Selected and adapted to target the six features of Lojban that put maximum structural pressure on Tonesu's type system.

## Status
Draft — first pass

---

## Purpose

This batch does not translate a named text. It uses Lojban as a **structural pressure tool** — a precisely engineered natural-language alternative with explicit type distinctions that many natural languages blur. Lojban's design reveals gaps and choices in any target language.

The six Lojban features tested here are:

| # | Lojban feature | What it tests in Tonesu |
|---|-------------|----------------------|
| 1 | `su'o` existential quantifier | `i-` vs `a-` scope prefix pair |
| 2 | `lo nu X` event nominalization | Causal frame vs first-class event nominal |
| 3 | `na'e` scalar/predicate negation | Level 1 (`no-X`) vs Level 5 (`no proposition`) scope discrimination |
| 4 | `na` claim negation | Whether claim negation is structurally distinguished from predicate negation |
| 5 | `jinvi` + `du'u` (believe that) | `to` primitive as propositional belief frame |
| 6 | `djuno` + `du'u` (know that) | `to-su` as established propositional knowledge frame |

Secondary test (not a separate Lojban feature but exposed by this batch): the **`tanru` underspecification** principle — Lojban's ability to form compounds with deliberately underdetermined relationships. Tonesu cannot form tanru. This is documented as a design-choice contrast.

Corpus sentences: **S690–S695**

---

## Vocabulary Framework

No new entries. All forms are existing derived compounds, primitives, or spec-level operators.

| Form | W# | Reading | Context |
|------|----|---------|---------|
| `i-` | — | precise/particular scope prefix | Spec-level. First use as existential-scope in deductive frame. |
| `a-` | — | abstract/universal scope prefix | Spec-level. From S684 (PRF-001). |
| `ki` | — | motion/change (primitive) | S691 event clause. |
| `fa-vo` | W197 | happiness; positive-valence affect state | S691 result clause. |
| `su-mu` | — | structural artifact; building | Compositional: `su` (structure) + `mu` (artifact). No W-entry needed. |
| `pom` | — | blue (CVC color anchor) | S692/S693. |
| `no-pom` | — | not-blue (predicate negation) | Level 1 `no-` prefix on `pom`. |
| `to` | — | thought/concept/pattern (primitive) | S694: belief-frame marker. |
| `to-su` | W030 | organized knowledge; framework | S695: knowledge-frame predicate. |
| `Sokrates` | — | Socrates (proper name) | From PRF-001 (S685–S686). |
| `de-zo` | W178 | dying / mortality | From PRF-001 (S684–S686). |
| `zo-li` | W049 | person / individual agent | S690. |

---

## The Six Lojban Distinctions

### 1. `su'o` vs `ro` — Existential vs universal quantification

Lojban uses independent pre-predicate quantifiers:
- `ro prenu cu morsi` = "All persons are mortal" (`ro` = every/all)
- `su'o prenu cu morsi` = "At least one person is mortal" (`su'o` = there-exists-at-least-one)

Both are full, syntactically separated quantifier words. The predicate is unchanged; only the quantifier shifts.

Tonesu uses the scope-prefix system on the argument itself:
- `a-zo-li ne de-zo` = "abstract/universal persons have the mortality property" (S684)
- `i-zo-li ne de-zo` = "particular/concrete persons have the mortality property" (S690)

The `a-` / `i-` distinction maps cleanly to the universal / existential-particular split. Differences: (1) in Tonesu the quantifying prefix is bound to the argument form, not syntactically separate; (2) `i-` has a richer semantics than bare existential — it is "precise/particular," meaning the entities in question are determinate instances, not just an abstract existence claim.

### 2. `lo nu X` — Event nominalization

Lojban has a dedicated abstraction particle `nu` for event nominalization:
- `lo nu mi klama` = "the-event-of my-going" — a first-class nominal; can be agent, patient, or topic.
- `lo nu mi klama cu pluka mi` = "The event of my going pleases me"

Tonesu has no `nu`-equivalent. Events can be expressed through compounds (W-entries) or through clause framing. The canonical path is the causal frame:
- `go {la-li ki},  la-li ne fa-vo` = "Because I move: I have happiness"

This is truth-conditionally equivalent but type-structurally different. Tonesu commits to the causal relationship; Lojban's `pluka` leaves the relationship type open. As a consequence, Tonesu cannot express "the event pleases me, but I don't know whether the pleasure is caused by the motion itself or by something else." The `go` asserts causation; the Lojban form leaves it pragmatically open.

Whether this is a feature or a limitation depends on what you're encoding. For claims where the causal mechanism IS the point (Cogito, scientific results), Tonesu is more precise. For neutral phenomenological observation ("my going and my happiness co-occur"), Tonesu must either commit to causation or reformulate.

### 3 & 4. `na'e` vs `na` — Predicate vs claim negation

Lojban makes a strong syntactic distinction:
- `lo zdani na'e blanu` = "The house is other-than-blue" — `na'e` negates the predicate; the subject exists and has a determinable property, just not the stated one.
- `lo zdani na blanu` = "It is not the case that the house is blue" — `na` negates the claim; no positive predication is made.

These have different truth conditions in intensional contexts and over presupposition.

Tonesu's five-level negation system captures both:
- `la-su-mu ne no-pom` — Level 1 root negation on the predicate: "the building has the not-blue property." Maps to `na'e`.
- `no  la-su-mu ne pom` — Fronted `no` denies the proposition: "not: [the building is blue]." Maps to `na`.

The S692/S693 minimal pair demonstrates this cleanly. The Tonesu system was not designed with Lojban `na`/`na'e` in mind — these two paths existed independently — but they align precisely.

What Tonesu does NOT have that Lojban has:
- `no'e blanu` = "is at the neutral mid-point on the blue scale" — no equivalent
- `to'e blanu` = "is maximally anti-blue" (polar opposite) — Tonesu would need explicit polar compound specification

### 5 & 6. `jinvi` / `djuno` + `du'u` — Belief vs knowledge

Lojban distinguishes the verb of epistemic attitude (`jinvi` = to opine, `djuno` = to know) from the abstraction type (`du'u` = proposition abstraction). They combine:
- `mi jinvi lo du'u la .sokrates. morsi` = "I believe/think that Socrates is mortal"
- `mi djuno lo du'u la .sokrates. morsi` = "I know that Socrates is mortal"

Tonesu uses the primitive `to` (thought/concept/pattern) vs the compound `to-su` (W030, organized knowledge/framework):
- `la-li to {la-Sokrates ne de-zo}` = "I hold [that Sokrates is mortal] as my conception" = belief
- `la-li to-su {la-Sokrates ne de-zo}` = "I have organized knowledge [that Sokrates is mortal]" = knowledge

The `to` / `to-su` distinction maps to the JTB-style (justified true belief / knowledge) epistemic gradient: `to` is private conceptual commitment; `to-su` is structured, established epistemic state. This distinction was available in the grammar (the counterfactual spec explicitly documents `la-X to {P}` as a belief-attribution frame) but had not been stress-tested with a second-order (`to-su`) version before this batch.

Note: `la-li to-su {P}` is a first corpus extension of `to-su` (normally used as a noun/NP compound = "organized knowledge as a system") into a propositional frame of the form "I have organized knowledge THAT P." This reuses the productive `{...}` content-clause framing from `go`, `wi`, and `la-X to {P}`. The pattern is regular; the specific form is new.

### Tanru underspecification — A structural difference, not a gap

Lojban's `tanru` allows deliberately underdetermined modifier-head compounds:
- `blanu zdani` = "blue-style house" — the relationship between `blanu` (blue) and `zdani` (house) is not specified by the grammar; context determines whether it means "blue-colored house," "house of blue people," "house used for blu-related activities," etc.

Tonesu's head-final composition rule forces specification:
- `pom su-mu` = a blue-colored building-artifact — ONLY. The `pom` (blue) modifies `su-mu` (building) in the single available relationship: color of the artifact. No ambiguity is possible; no alternative reading can be formed with the same two elements in the same order.

This is a design choice with significant consequences:
- **Tonesu advantage:** every compound has exactly one reading without disambiguation. A compound communicates a specific conceptual claim.
- **Lojban advantage:** tanru allows rapid NP assembly in low-commitment contexts where the relationship is contextually obvious and not worth spelling out. `blanu zdani` is faster to say and process when the context makes the blue-ness self-evident.

Whether the forced compositionality of Tonesu is "better" depends on what you're encoding. For technical, legal, and philosophical contexts (where ambiguity failure is high-cost), Tonesu's rule is preferable. For casual speech, it imposes compositional labor that speakers of natural languages have learned to avoid.

This difference is not tested in a sentence (no tanru equivalent exists in Tonesu) but is documented here because the Lojban batch inevitably surfaces it.

---

## Source Text

Selected CLL examples (paraphrased to isolate each target feature):

> *Quantification (CLL Chapter 16):*
> `ro prenu cu morsi` / `su'o prenu cu morsi`
> All persons are mortal. / At least one person is mortal.

> *Event nominalization (CLL Chapter 11):*
> `lo nu mi klama cu pluka mi`
> The event of my going pleases me.

> *Negation (CLL Chapter 15):*
> `lo zdani na blanu` — The house is not blue. (claim negation)
> `lo zdani na'e blanu` — The house is other-than-blue. (predicate negation)

> *Propositional attitude (CLL Chapter 11):*
> `mi jinvi lo du'u la .sokrates. morsi` — I believe Socrates is mortal.
> `mi djuno lo du'u la .sokrates. morsi` — I know Socrates is mortal.

---

## Verse-by-Verse Analysis

### S690 — Existential scope (Lojban `su'o`)

```
i-zo-li  ne  de-zo
```

**Written:** `izoli ne dezo`

**Reading:** A particular person is mortal.

**Notes:** `i-` = precise/particular scope prefix. In the syllogistic universal S684, `a-zo-li` = "persons in the abstract / all persons." Here `i-zo-li` = "the particular/concrete persons [in evidence]" = existential reading: there exist (specific) persons with the mortality property. Lojban: `su'o prenu cu morsi`. The `i-`/`a-` distinction tracks `su'o`/`ro` exactly in their quantificational type, though the implementation differs: Lojban uses pre-predicate quantifier words; Tonesu uses scope prefixes bound to the argument. This is the first explicit existential-scope use of `i-` in the corpus, completing the universal/existential pair with S684.

---

### S691 — Event via causal frame (Lojban `lo nu`)

```
go {la-li  ki},  la-li  ne  fa-vo
```

**Written:** `go lali ki, lali ne favo`

**Reading:** Because I move: I have happiness.

**Notes:** Lojban: `lo nu mi klama cu pluka mi` = "The event of my going pleases me." Tonesu routes the same content through a causal frame — the moving-event is the cause; the happiness is the effect. The `go`-frame imposes a constitutive claim: the moving is not merely correlated with happiness, it grounds it. In Lojban, `pluka` (to please) leaves the relational type open — it may be causal, constitutive, coincidental, or phenomenologically simultaneous. Tonesu's `go` commits to causal grounding. The tradeoff: Tonesu is more precise; Lojban is more flexible. `fa-vo` (W197) = happiness/positive-valence affect state.

---

### S692 — Predicate negation (Lojban `na'e`)

```
la-su-mu  ne  no-pom
```

**Written:** `lasumu ne nopom`

**Reading:** The structure-artifact has the not-blue property.

**Notes:** `su-mu` = compositional: structural artifact / building. `no-pom` = Level 1 negation (`no-` root prefix) on the color anchor `pom` (blue). The sentence attributes a determinable property (non-blue-ness) to a real object. The building exists; it has a color; that color is not blue. This is Lojban's `lo zdani na'e blanu` ("the house is other-than-blue"): the predicate is negated, but the subject IS and HAS a property. Minimal pair with S693.

---

### S693 — Claim negation (Lojban `na`)

```
no  la-su-mu  ne  pom
```

**Written:** `no lasumu ne pom`

**Reading:** Not: [the structure-artifact is blue].

**Notes:** Fronted `no` (Level 5 / sentence-initial denial, established by S550 precedent: `no la-li ne vo`). The entire proposition `la-su-mu ne pom` is denied. No positive color predication is made; no claim about what color the building IS is implied. This is Lojban's `lo zdani na blanu` ("it is not the case that the house is blue"). Minimal pair with S692: same words, different scope hierarchy. The scope distinction in Tonesu is implemented positionally — `no-X` as prefix (predicate-level); fronted `no clause` (claim-level) — without additional particles.

---

### S694 — Propositional belief (Lojban `jinvi` + `du'u`)

```
la-li  to  {la-Sokrates  ne  de-zo}
```

**Written:** `lali to laSokrates ne dezo`

**Reading:** I hold [that Sokrates is mortal] as my conception.

**Notes:** `to` (primitive: thought/concept/pattern) as the belief-frame marker. `la-X to {P}` = X holds P as their conceptual model — established in the counterfactual attribution spec. Applied here to a factual (non-counterfactual) proposition: the `{P}` is a simple property-attribution clause. The proposition `{la-Sokrates ne de-zo}` is held inside a private epistemic frame; the sentence does not assert Sokrates' mortality as fact, only that the speaker believes it. Lojban: `mi jinvi lo du'u la .sokrates. morsi` — `jinvi` = to opine (uncommitted); `du'u` = proposition abstraction (the abstract fact-that). Tonesu's `to` + `{P}` = the Tonesu analogue of `jinvi lo du'u P`. Minimal pair with S695.

---

### S695 — Propositional knowledge (Lojban `djuno` + `du'u`)

```
la-li  to-su  {la-Sokrates  ne  de-zo}
```

**Written:** `lali tosu laSokrates ne dezo`

**Reading:** I have organized knowledge [that Sokrates is mortal].

**Notes:** `to-su` (W030: organized knowledge / framework) + `{proposition}` as propositional knowledge-attribution frame. First extension of `to-su` into the `{P}` braced-clause pattern. `la-li to-su {P}` = I have established, structured knowledge that P. `to-su` is stronger than `to` (primitive belief): structured knowledge implies the proposition has been organized into a confirmed epistemic framework, not merely held as a private conception. Lojban: `mi djuno lo du'u la .sokrates. morsi` — `djuno` = to know (established). Tonesu: `to` = I believe P (private model); `to-su` = I know P (structured knowledge). The `to`/`to-su` pair maps to Lojban's `jinvi`/`djuno` split. Provisional: this is the first corpus use of `to-su {P}` as a propositional knowledge frame; the `to-su` compound had only appeared as an NP (organized knowledge as a thing). The pattern is regular but requires a second attestation before full confirmation.

---

## LOJ-001 Batch Summary

| # | Lojban feature | English | Tonesu | Notes |
|---|-------------|---------|--------|-------|
| S690 | `su'o` existential | At least one person is mortal | `i-zo-li ne de-zo` | `i-` = particular scope; existential pair with S684 |
| S691 | `lo nu X` event nominal | My going pleases me | `go {la-li ki}, la-li ne fa-vo` | Causal frame instead of free event nominal |
| S692 | `na'e` predicate negation | The building is other-than-blue | `la-su-mu ne no-pom` | Level 1 `no-` prefix = predicate negated |
| S693 | `na` claim negation | Not: the building is blue | `no la-su-mu ne pom` | Fronted `no` = entire claim denied |
| S694 | `jinvi` + `du'u` (believe) | I believe Sokrates is mortal | `la-li to {la-Sokrates ne de-zo}` | `to` = private conception frame |
| S695 | `djuno` + `du'u` (know) | I know Sokrates is mortal | `la-li to-su {la-Sokrates ne de-zo}` | `to-su` = organized knowledge frame (provisional) |

**New vocabulary:** none — pure structural analysis.

**Key finding:** Lojban's six major type distinctions tested here map onto Tonesu through structural redirections rather than direct equivalents. The `su'o`/`ro` quantifier split maps to `i-`/`a-` scope prefixes. The `na`/`na'e` negation split maps to fronted-`no` claim denial vs `no-X` predicate prefix. The `jinvi`/`djuno` belief-knowledge split maps to `to`/`to-su`. Only the `lo nu X` event nominalization requires a genuine structural substitution (causal framing), which introduces a narrower commitment (causal grounding) than Lojban's neutral `pluka`. The one feature Tonesu cannot reproduce: tanru underspecification. This is a design difference — Tonesu demands compositional specificity at construction time.

---

## Colloquial Register Analysis

| Form used | CLQ entry | Colloquial form | Notes |
|-----------|-----------|-----------------|-------|
| `i-zo-li` | none | — | `i-`-prefixed `zo-li` (2-root) — below threshold; scope prefix is spec-level |
| `de-zo` | none | — | 2-root — below threshold |
| `ki` (primitive) | none | — | Primitive root — minimum possible |
| `fa-vo` | none | — | 2-root — below threshold |
| `su-mu` | none | — | 2-root compositional — below threshold |
| `pom` | none | — | CVC color anchor — minimum possible |
| `no-pom` | none | — | 2-root — below threshold |
| `to` (primitive) | none | — | Primitive root — minimum possible |
| `to-su` | none | — | 2-root — below threshold; also semantically load-bearing (`to` vs `to-su` distinction is tested across this whole batch) |

**Verdict:** irreducibly formal — all forms are primitives, 2-root compounds below threshold, or semantically load-bearing operators.

*CLQ entries registered from this batch: none.*
