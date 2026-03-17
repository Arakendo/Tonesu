# Phonology

## Status: Draft

> **Notation convention:** Hyphens in all examples throughout this document are **analytic notation** — they mark morpheme boundaries for analysis and teaching, and are not written in Tonesu. Written Tonesu is solid: `tofesuki`, not `to-fe-su-ki`. The apostrophe `'` is the only normative non-alphabetic character within a compound. See spec/word-formation.md § Written Form.

---

## Consonant Inventory

| Symbol | Approx. Sound | Notes |
|--------|--------------|-------|
| p | p (spin) | |
| b | b (ban) | |
| t | t (stop) | |
| d | d (dog) | |
| k | k (skip) | |
| g | g (go) | |
| m | m (man) | |
| n | n (no) | |
| s | s (sun) | |
| z | z (zoo) | |
| l | l (let) | |
| r | r (run) | flap or trill, not retroflex |
| f | f (fan) | |
| h | h (hat) | |
| y | y (yes) | |
| w | w (win) | |
| v | v (vine) | labiodental fricative; added March 2026 — already in use in `vo` (R024); see FLAG-CVC-001 |

**Total: 17 consonants**

Excluded by design: th, x, q, c (redundant with k/s), uvulars, retroflexes, ejectives, clicks.
Goal: globally pronounceable for speakers of major world language families.

---

## Vowel Inventory

| Symbol | Approx. Sound |
|--------|--------------|
| a | a (father) |
| e | e (bed) |
| i | i (feet) |
| o | o (go) |
| u | u (food) |

**Total: 5 vowels**

### Optional: Vowel Length
Long vowels (aa, ee, ii, oo, uu) may function as a morphological modifier.
- Short vowel: base concept
- Long vowel: intensified or abstracted form
*Decision pending — see open questions.*

---

## Syllable Structure

**Primary rule: (C)V(C)**

### Parse Invariants

These three invariants are the structural foundation of the phonological system. Violating any one of them degrades or destroys the parser's ability to segment compounds without lookahead:

1. **Internal syllables begin with a consonant** — every syllable inside a compound must have a C onset. Bare-vowel and VC syllables are legal only at word start, never mid-compound.
2. **Compound boundaries are phonologically visible** — because every internal syllable starts with a consonant, the parser can walk a compound left-to-right, finding boundaries at each consonant onset without ambiguity or backtracking.
3. **Root tiers are structurally distinct** — CV (primitives), CVC (lexical atoms), CVCC (exceptional anchors), and V/VC (particles, if used) occupy separate structural slots. A form's phonological shape identifies its tier.

Breaking invariant 1 forces lookahead. Breaking invariant 2 produces parse ambiguity. Breaking invariant 3 collapses the tier signal.

---

- CV: most common (ka, li, mu, se)
- V: **word-initial position only** — a bare vowel syllable may open a word or compound. It must not appear mid-compound: invariant 1 above requires every internal syllable to have a consonant onset. Only 5 V forms exist (a e i o u); none are currently assigned. Reserved as a future closed class (discourse particles, affective interjections, or similar). No form from this space may be assigned without an explicit registry decision.

  Anticipated usage hints (unassigned; for orientation only):

  | Form | Typical discourse particle role |
  |------|--------------------------------|
  | `a`  | affirmation |
  | `e`  | surprise / attention shift |
  | `i`  | hesitation / filler |
  | `o`  | address / calling attention |
  | `u`  | disapproval / mild negation |

- VC: **deferred — word-initial only if ever admitted** — a vowel-initial syllable with a closing consonant (e.g. `an`, `el`, `im`). Shares the same word-initial constraint as bare V; mid-compound VC violates invariant 1 and creates lookahead (is `beanto` parsed `be|an|to` or `bea|nto`?). Word-initial VC parses cleanly because the word boundary precedes it: `an-be`, `im-ra`, `us-lo` are all unambiguous. Up to ~40 clean forms available. No current assignment; no current pressure (37 CV slots remain free). Condition for opening this tier: CV near-exhaustion, or need for a phonologically distinct particle/pronoun class. See § Open Questions.
- CVC: allowed (kel, sun, mar)
- No clusters (CC) in core roots
- Clusters may appear at compound boundaries but should be avoidable via vowel-final roots

---

## Stress

**Fixed rule: stress always falls on the first syllable.**

- Predictable, requires no marking
- Avoids stress-based ambiguity
- Example: **KA**-ru, **LI**-na-se, **SU**-mu-to

---

## Orthography

**One letter = one sound. No exceptions in core vocabulary.**

- No silent letters
- No digraphs for single phonemes
- Diacritics reserved for long vowels only (if adopted): ā ē ī ō ū

*Scope note: the one-symbol/one-sound rule applies to the segmental phonology (consonants and vowels). Prosodic markers are a distinct category and are governed separately below.*

---

## Prosodic Juncture Marker

**Symbol: `'` (apostrophe)**

The apostrophe marks the **left boundary of a subcompound** in a compound chain. It is a prosodic juncture — a slight phrasal pause at a structural boundary — not a segmental phoneme. It does not appear in the consonant or vowel inventory.

**Phonological realization:** a minor phrase break, similar to the IPA `|` juncture feature. In careful speech, a brief silence at the juncture point. In casual speech, may reduce to a perceptible lengthening of the preceding vowel or simply a prosodic grouping boundary without audible pause.

**Orthographic rule:** `'` is written at the point where a speaker would group a subcompound. It acts as a right-binding operator on the elements that follow it:

```
A'B-C-D   →   A modifies {B-C-D}   (single modifier + pre-bound unit)
A-B'C-D   →   {A-B} modifies {C-D} (plain chain + pre-bound unit)
```

Without `'`, the default parse is right-branching: each new element modifies the accumulating chain from left to right.

**Usage policy:**
- Omit for compounds of 2–3 roots where the reading is unambiguous.
- Optional for depth-4 chains where structure is still clear from primitive meanings.
- Expected when X-X repetition appears inside a longer compound, since X-X creates genuine parse ambiguity at depth ≥ 4.
- Multiple `'` markers are permitted; each adds cognitive parse load. Casual and spoken registers naturally avoid nesting depth; technical and formal registers may use as many as structure requires.

**First corpus attestation:** S045 (T-APO-001).

---

## Punctuation and Notation Marks

Eight marks supplement `'`. Unlike `'`, these operate **outside** compound boundaries — at clause, sentence, or metalanguage level. Sentence and phrase marks have no phoneme equivalents; speech realizes them through pitch, stress, and prosodic phrasing. The last two marks (`:`, `::`) serve primarily as metalanguage notation and appear in Tonesu sentences only in the role specified for each.

| Mark | Name | Function |
|------|------|----------|
| `,` | clause separator | prosodic pause between a frame clause and its matrix, or between list items |
| `!` | exclamation mark | end-of-utterance: heightened affective or emphatic force |
| `?` | question mark | end-of-utterance: interrogative; orthographic counterpart to grammatical `to-si` |
| `~` | approximation mark | pre-positional hedge: "approximately / roughly / on the order of / something like"; spoken form `ven` (G010) |
| `()` | evidential frame | clause-level epistemic bracket: content is reported, inferred, or unattributed — not directly asserted; spoken forms `vund` (G014, open) / `vunds` (G015, close) |
| `[]` | aside / commentary frame | non-semantic editorial or analytic annotation — does not alter truth conditions of surrounding text; removable without semantic change |
| `:` | topic frame / definition mark | sentence-initial: "as for {topic}, ..." (topic frame); metalanguage: explanatory gloss (`term : reading`) |
| `::` | canonical definition mark | structural decomposition (`term :: roots`); appears in written and verbal discourse; spoken form `helms` (G012) |
| `/` | parallel partition | structural midpoint of a bi-clausal parallel or antithetical construction; marks two clauses as formally paired; spoken form `vel` (G013) |

---

### `,` — Clause Separator

A **prosodic pause** between clausal units. Recommended when a frame clause (`go`, `wi`, `ta`) precedes the matrix and the boundary benefits from an explicit mark. Also separates items in a coordinated list.

```
ta ti-de, la-mi lo-mu ka-be         →  In the past, I grew the object.
go {la-lu ki}, la-mi fa-be          →  Because the light moved, my affect rose.
la-mi lo-mu, lo-ma, lo-ra ka-ko    →  I stored the object, the material, and the energy.
```

Omit when the boundary is unambiguous without it.

---

### `!` — Exclamation Mark

End-of-utterance marker signaling **heightened affective or emphatic force**. The sentence is grammatically complete without `!`; the mark signals what speech realizes as elevated pitch, stress, or intensity.

```
la-mi fa-be!                        →  My affect is rising! (elation, alarm)
la-tu ka!                           →  Act! (imperative with force)
```

Compatible with any sentence type including questions: `to-si  la-tu  ki!` = Where did you go?! (emphatic).

---

### `?` — Question Mark

End-of-utterance marker signaling **interrogative mode**. The grammatical question mechanism (`to-si`) takes priority — `?` is its orthographic counterpart.

- **Formal/careful writing:** `to-si` is required in the clause; `?` appears at the end for clarity.
- **Casual and notes register:** `?` may substitute for the fronted polar `to-si —`, making it a genuine shorthand.

```
to-si  la-tu  lo-to  ka-ko?         →  Who stored the knowledge?
la-tu  lo-mu  ka-be?                →  Did you grow it? (casual: ? replaces fronted to-si)
```

---

### `~` — Approximation Mark

Pre-positional hedge meaning **"approximately / roughly / on the order of / something like."** Always at the **left edge of the unit it qualifies**: the start of a sentence-level NP or word, or immediately following `'`. `~` cannot interrupt a solid compound string. In a full measurement expression, `~` pre-poses the entire `{digit} {scale} nu {domain}` block.

**`'` interaction:** because `'` marks the left boundary of a subcompound, `~` may appear immediately after `'`. `~` then hedges only the subcompound, not the full compound. In written form (hyphens are analytic notation only):

```
~A'BC       →  approximately {A modifying BC}; the whole compound is hedged
A'~BC       →  A modifies {approximately BC}; only the subcompound is hedged
```

These are distinct propositions. `~wipu'zosesoli` = approximately {wolf-kind} (uncertain about the whole categorization: "something wolf-like"). `wipu'~zosesoli` = {wolf-discriminator} over {approximately the canid-pack class} (certain about the outer frame; hedging the base kind-term — used for ancestral, mythological, or proto-taxon references). The same distinction is available at any `'` boundary.

**Spoken form: `ven`** — registered as G010 in `registry/roots.md`. In speech, `~` is realized as `ven`. The written form `~` is canonical in formal and technical Tonesu. `ven` may appear in written text where a phonetic or poetic rendering is intended (verse, informal writing, transcribed speech); in all such cases it is understood as a graphical variant of `~`, not a distinct word.

**With numerals and measurement:**
```
~gal nu li                          →  about 3 people
~hin pir nu pa                      →  roughly 5 km
~bol nil nil nil nu hulm            →  on the order of 1,000 years
~varn                               →  approximately π (loose derivation or estimate)
```

**With compounds and concepts (analytic notation; linguistic and notes register):**
```
~zo-li                              →  something like a person / roughly person-class
~ta ti-be                           →  somewhere around the future / roughly "later"
~to-si                              →  something like a question / quasi-interrogative framing
~to-su                              →  working/tentative theory (a provisional knowledge
                                       framework; contrast to-su = established framework)
~tonesu                             →  approximately truth / theory / conjecture
                                       (poetic/philosophical register: tonesu = to-ne-su
                                       = complete structured knowledge; ~tonesu = something
                                       like complete truth = a theory)
```

Multiple `~` marks in a sentence are permitted, each scoping its own following unit independently.

---

### `()` — Evidential Frame

Round brackets wrap a **clause or sub-clause** to mark its epistemic status as **reported, inferred, or unattributed** — not directly asserted by the speaker. The speaker presents the bracketed content as something they have received, derived, or are advancing with explicit epistemic reservation.

**Structure:**
```
(clause)                  →  reportedly / allegedly / it is said that {clause}
~ (clause)                →  approximately / reportedly: {clause}   (stacked hedge + report)
(~ clause)                →  reportedly approximately {clause}      (hedge scoped inside frame)
```

**Spoken form:** **`vund`** (G014) at the `(` position; **`vunds`** (G015) at the `)` position. In speech the evidential frame is announced by `vund` before the reported clause and closed by `vunds` after it. Prosodic bracketing (slight boundary pause, consistent framing intonation) accompanies the spoken forms — the spoken tokens reinforce prosody rather than replacing it. In casual speech prosody alone is sufficient; `vund`/`vunds` are required in formal, legal, and dictation register, and whenever nested evidential frames risk misparse. **`vund` and `vunds` are also valid written substitutes** for `(` and `)` wherever the bracket symbols are unavailable.

**Family note:** `vund`/`vunds` belong to the `v`-initial notation family alongside `ven` (~) and `vel` (/). The `v`-family covers structural/operational marks (approximation, partition, evidential wrapper); the `h`-initial family (`helm`/`helms`) covers definition marks. The `u` vowel is intentional — per the sound-symbolism table, `u` = deep, heavy, closed — the containment vowel, fitting for a frame that encloses content.

**Three-way distinction with epistemic modality:**

| Form | Assertor | What is encoded |
|------|----------|-----------------|
| `la-mi  se/si/to  {prop}` | first-person speaker | speaker's calibrated epistemic level |
| `la-source  be/si  {prop}` | named non-personal source | process or doctrine outputs the claim |
| `(prop)` | none (anonymous) | content is reported or epistemically reserved |

`()` differs from the personal modal in two ways: no assertor is named; and the frame does not encode *how certain* the speaker is — only that they are **not directly asserting the content from their own epistemic resources**. For calibrated commitment, use the personal modal or process frame; for anonymous attribution, contested claims, or formal epistemic reservation, use `()`.

**With `~`:** stacking exposes both approximation and evidential weakness simultaneously:
```
~ (la-ze  si  lo-to-fe-su  de)    →  approximately / reportedly: she claims the institution is failing
```

**Internal grammar is unchanged.** The wrapped clause follows all standard grammar rules. The evidential frame is a clause-level meta-operator; it does not alter the agent/patient/predicate structure of the wrapped content. Imperatives and questions may not be wrapped; `()` is a declarative epistemic frame only.

**Cross-reference:** grammar rules for the evidential frame in sentence context: see spec/grammar.md § Evidential Frame.

---

### `:` and `::` — Definition and Topic Marks

Two marks that operate at the **interface between the metalanguage and Tonesu sentences**.

#### `::` — Canonical Definition Mark

`::` introduces a **structural or canonical definition**: the right-hand side gives the formal account — a phonological decomposition, a compositional breakdown, an operational formula. Used in registry entries, spec notation, grammar examples, and wherever a speaker or writer needs to give a formal structural account. Appears in written and verbal discourse.

```
lu-mu :: lu + mu                  →  canonical decomposition of lu-mu
{X}-no-fe :: X + no + fe          →  structural description of the extremal suffix pattern
```

**Spoken form: `helms`** — registered as G012 in `registry/roots.md`. The **notation-doubling rule**: when a CVCC spoken marker is paired with a doubled written form, it takes a final `s` coda to produce the spoken doublet (CVCCS). `helms` is the CVCCS spoken form of `::`. The minimal pair `helm` / `helms` makes the single/double distinction immediately audible in dictation and spoken register without requiring an independent unrelated form.

#### `:` — Explanatory Definition (metalanguage) and Topic Frame (sentences)

`:` has two roles, distinguished by context.

**Role 1 — Explanatory definition (metalanguage):**

`term : explanation` introduces a natural-language gloss or functional description of what the term means — as opposed to its formal structure.

```
to-si : knowledge-seeking signal         →  plain reading of to-si
{X}-no-fe : X without limiting boundary  →  functional gloss of the extremal pattern
```

Contrast: `to-si :: to + si` (structural decomposition, `::`) vs. `to-si : knowledge-seeking signal` (functional gloss, `:`).

**Role 2 — Topic frame (Tonesu sentences):**

At sentence level, `:` appears **sentence-initially** to separate a leading topic NP from the comment clause: "as for {topic}, the following holds."

```
lo-mu : la-ze  ka-ko  lo-mu           →  As for the machine — she stored it.
la-Yeshua : lo-li-pu  vo              →  As for Yeshua — the people are valued.
lo-ne-ra : la-mi  no-se  lo-ze        →  As for the resonance — I have no perceptual basis for it.
```

**Topic frame constraints:**
1. Sentence-initial position only — `:` cannot appear mid-sentence.
2. One topic frame per clause — nested topic frames are not permitted.
3. The topic NP retains its role-marker (`la-`, `lo-`, `ne-`, etc.) where it carries one.

**Spoken form:** a slight prosodic pause at the `:` boundary; the topic NP may carry slightly higher prominence than the comment clause. **Lexical spoken form: `helm`** — registered as G011 in `registry/roots.md`. In speech, `:` is realized as `helm`. The written form `:` is canonical in formal and technical Tonesu; `helm` appears in speech, phonetic transcription, and wherever the written symbol is not available.

**Cross-reference:** grammar rules for the topic frame in sentence context: see spec/grammar.md § Topic Frame.

---

### `[]` — Aside / Commentary Frame

`[]` marks **editorial or analytic commentary** — content that annotates a passage without participating in its argument or truth-conditional structure. It operates in the *analysis layer*, separate from the argument layer (`()`, `:`, `go`, epistemic markers).

**Defining constraint — removal invariance.** Removing all `[]` frames from a passage must leave the surrounding Tonesu sentences semantically and grammatically unchanged. Any annotation that alters meaning when removed is not a valid `[]` frame — it belongs in the core grammar instead.

**Typical contents:**

| content type | examples |
|---|---|
| analytic notes | `[early agricultural report]` · `[estimate from early data]` |
| fallacy / audit flags | `[laundering: report → certainty]` · `[unsupported cascade]` · `[topic shift: policy → person]` |
| missing-structure labels | `[probable topic: food policy]` · `[missing premise: higher cost reduces wellbeing]` |
| burden-of-proof notes | `[burden: show policy improves food security]` |
| discourse stage labels | `[response to opponent question]` · `[closing argument]` |
| citations and references | `[citation needed]` · `[UN food report 2024]` |

**Self-policing rules for annotators:**

1. **No evidential upgrade.** `[]` may label or flag a claim's evidential status; it may not reassert it at a higher level. `(X)  [established fact]` is invalid unless the core text independently supports that elevation.
2. **Interpretive annotations must be visibly hedged.** When the annotation is the annotator's inference rather than a recovery of explicit structure, use hedged phrasing: `[probable topic: X]`, `[likely sense: X]` — not bare `[topic: X]` or `[definition: X]` unless the structure is explicitly recoverable.
3. **No silent rewriting.** `[]` annotates the argument as written; it may not substitute, correct, or upgrade the core claim while appearing to merely describe it — the analytic crime of laundering by cleanup crew.

**Reconstruction use.** When a speaker has omitted an explicit `:` or `::`, an annotator may use `[]` to propose the likely structure after the fact, subject to rule 2 above. This provides graceful annotation of natural or imperfect speech without altering the original text.

**Spoken form:** none. `[]` frames are not realized in oral Tonesu — they are written, typographic, and editorial. In oral contexts `[]` content is either omitted or delivered by explicit convention agreed by participants (e.g., "bracket note: …" as a meta-verbal cue). `[]` has no spoken phoneme equivalent and does not participate in prosodic parsing.

**Disambiguation — spec notation vs. written Tonesu.** Going forward, spec examples, grammar glosses, and registry entries use `{...}` for *analytic notation*: slot placeholders (`la-{agent}`), subordinate clause scope (`go {premise}  result`), and structural groupings. `{...}` never appears in running Tonesu text. In a Tonesu passage, `[...]` is always an aside/commentary frame. Legacy spec text written before this convention was adopted uses `[...]` for analytic purposes; those occurrences are grandfathered and do not require retroactive correction.

**Cross-reference:** grammar rules for the aside frame: see spec/grammar.md § Aside / Commentary Frame.

---

### `/` — Parallel Partition

A **structural midpoint marker** for bi-clausal parallel or antithetical constructions. When a sentence consists of two formally paired clauses — two sides of a contrast, two halves of a complementary structure, or two rhetorically equivalent units — `/` appears between them to make that pairing explicit.

```
la-mi wi-vo / no la-mi ka-ze         →  I intend the good / I do not do it.
ti helm vo-fe / ti helm no-vo'fe     →  The best time / the worst time.
go {X} / Y                           →  Because X / Y (premise / result)
```

**What `/` signals:** the two clauses are not merely sequential — they are structurally paired. The mark is a claim about form: these clauses belong together as a unit, and the relationship between them (contrast, antithesis, complement, premise/result) is intended to be read in parallel. It does not specify the relationship type; the content supplies that.

**Relation to `,`:** `,` marks a prosodic boundary between a frame clause and its matrix. `/` marks a structural pairing between two co-equal clauses. They are compatible and orthogonal: a `go {premise}` frame may use `,` at the frame boundary and `/` at the premise/result split when a complex clause benefits from both markers. In most cases `/` alone is sufficient for short biclausal structures.

**Register:** normative in written Tonesu. Speech realizes the `/` boundary as a prosodic pause slightly more marked than `,` — the "partner clause" intonation, signalling co-equal pairing rather than frame/matrix subordination. No phoneme equivalent; the spoken form `vel` may be inserted at the `/` position in dictation or oral composition.

**Spoken form: `vel`** — registered as G013 in `registry/roots.md`. In speech, `/` is realized as `vel`. The written form `/` is canonical in formal and technical Tonesu; `vel` appears in speech, phonetic transcription, dictation, and wherever the written symbol is unavailable or a spoken word form is preferred. **`vel` is a valid written substitute for `/`** in all contexts where using the symbol is impractical.

**Corpus pressure:** formalized after S450–S461 (March 2026). Six translation stress tests (JOH-001 through WIT-001) produced formally paired bi-clausal structures that neither `,` nor `du` adequately encoded. S452–S453 (Romans 7:19) and S454–S458 (Dickens) are the clearest cases: the clauses are antithetical, not causal, and the pairing is part of the semantic content. Three distinct clause types requiring the mark — antithetical parallel, will/act gap, and premise/result split — were all attested in the same batch.

---

## Sound Symbolism (Advisory, Not Binding)

These are tendencies, not rules. They inform root design intuitively but do not override compositional meaning.

| Sound | Tendency |
|-------|----------|
| i | small, sharp, precise, near |
| a | broad, open, general |
| u | deep, heavy, closed |
| k | discrete boundary, separation |
| m | substance, continuity |
| s | flow, diffusion |
| t | sequence, segmentation |
| l | animate, social, smooth |
| r | force, rotation, energy |

---

## CV Space Audit

**Audit date: March 2026. Basis: 32 roots + 6 particles + 4 pronouns + 1 derivational suffix.**

Taken forms (43 of 80):

| Category | Forms |
|----------|-------|
| Roots (33) | `mu ma li zo ki ka be de su to fe ne pe go du pa di ti re se so lu si vo wi no nu ru pu ra ko ha fa` |
| Particles (6) | `la lo ro ta na da` |
| Pronouns (4) | `mi tu ze yu` |
| Derivational (1) | `ge` |

Note: `ka`, `ne`, `pa` are counted under roots; not double-counted as particles.

**Free CVs (37 of 80):**

|   | a | e | i | o | u |
|---|---|---|---|---|---|
| **p** | — | — | `pi` | `po` | — |
| **b** | `ba` | — | `bi` | `bo` | `bu` |
| **t** | — | `te` | — | — | — |
| **d** | — | — | — | `do` | — |
| **k** | — | `ke` | — | — | `ku` |
| **g** | `ga` | — | `gi` | — | `gu` |
| **m** | — | `me` | — | `mo` | — |
| **n** | — | — | `ni` | — | — |
| **s** | `sa` | — | — | — | — |
| **z** | `za` | — | `zi` | — | `zu` |
| **l** | — | `le` | — | — | — |
| **r** | — | — | `ri` | — | — |
| **f** | — | — | `fi` | `fo` | `fu` |
| **h** | — | `he` | `hi` | `ho` | `hu` |
| **y** | `ya` | `ye` | `yi` | `yo` | — |
| **w** | `wa` | `we` | — | `wo` | `wu` |

The `f`-initial cluster (`fa fi fo fu`) and the `h`-initial cluster (`he hi ho hu`) are largely intact and serve as the primary reserve banks. Some free slots carry speech-speed risk near taken neighbours (`ke`/`ki`/`ko`, `za`/`ze`/`zo`, `yi`/`yu`) and should be used with care.

---

## CVC Root Reserve

CVC syllables (`sun`, `kel`, `mar`) are legal per the syllable structure rule. When the CV pool is exhausted or a concept needs a phonologically distinct shortform, draw from this tier. Design constraints:

1. **CV stem must be free** — a CVC whose first two letters form a taken CV will visually parse as that root plus a coda, creating ambiguity at first glance.
2. **Final consonant must not be a current or likely derivational suffix** — current derivational suffixes are vowel-final (`-li`, `-mu`, `-pa`, `-su`, `-to`, `-ge`, `-ki`). Safe coda consonants: `n l r m s`. Marked cross-linguistically as codas: `z f h`.
3. **Globally pronounceable** — `k p t` work broadly but not universally; `n l r m s` are the safest.

**Clean CVC shortlist** (free CV stem, safe coda, minimal confusion risk):

| Form | CV stem | Coda | Notes |
|------|---------|------|-------|
| `bol` | `bo` | l | very clean |
| `bun` | `bu` | n | very clean |
| `gal` | `ga` | l | very clean |
| `hin` | `hi` | n | very clean |
| `mol` | `mo` | l | very clean |
| `wes` | `we` | s | very clean |
| `yom` | `yo` | m | very clean |
| `fon` | `fo` | n | very clean |

These are prioritised candidates when CVC roots are needed. All 8 forms assigned to digits 1–8 (March 2026); see `notes/anchor-inventory.md`.

---

## Phonological Tier Stratification

The full tier system in order of word-shape complexity:

| Pattern | Tier | Contents | Admission rule |
|---------|------|----------|----------------|
| CV | Primitives | Closed ontological root set | Passes all three primitive validation rules (`registry/primitives.md`) |
| CV-CV+ | Compounds | Open compositional vocabulary | Expressible from existing roots; no new primitive needed |
| CVC | Lexical descriptors | Digits, colors (closed class); scale prefixes (ergonomic shortforms) | Two sub-categories — see below |
| CVCC | Exceptional anchors | Mathematical/physical constants; convention-defined units with no compositional expression | Assemblage-First Rule: see `notes/anchor-inventory.md §The Assemblage-First Rule` |
| CVCCS | Notation pair closers | Spoken forms marking the secondary element of a two-part notation structure: (a) the doublet of a doubled written mark (`::` from `::`; future doubled marks); or (b) the closing bracket of a bracket-pair mark (`)` from `(`). | One rule only: a CVCC notation-marker spoken form may take `+s` to mark the second/closing element of its paired notation structure. Not a free-standing tier; each CVCCS form is bound to its CVCC base. Current instances: `helms` (G012, `::`, `-lm` coda) · `vunds` (G015, `)`, `-nd` coda). |

**CVC sub-categories:**

- *Closed-class CVC atoms* — digits and colors. No compositional expression exists; the form defines an irreducible scale anchor or perceptual hue point. The complete set is fixed unless a new irreducible category is identified.
- *Ergonomic shortforms* — scale prefixes and future candidates. A compositional expression exists and remains canonical; CVC phonology is assigned on frequency and measurement-ergonomics grounds. Criteria and full admission rules: `spec/word-formation.md §Ergonomic Shortforms`. Inventory and flags: `notes/anchor-inventory.md §Scale Prefix Inventory` and FLAG-CVC-010.

**Assemblage-First Rule (summary):** The default for any concept — however complex — is compositional assemblage. A long or unwieldy compound is not grounds for a new lexical atom at any tier. CVCC is the pressure valve for the specific case where assemblage is genuinely impossible (irrational/transcendental values, convention-defined constants) AND a stable atomic form is functionally necessary. A new CV primitive is never the answer to an awkward compound.

---

## Open Questions

- [ ] Adopt vowel length as a morphological tool, or avoid complexity?
- [x] ~~**V and VC syllable shapes — status and admission rule.**~~ **Resolved (March 2026).** V (bare vowel, word-initial only): formalized as a 5-slot reserved tier; no forms currently assigned. VC (vowel + coda, word-initial only if ever admitted): logged as a future tier option; ~40 clean forms available; admission condition = CV near-exhaustion OR need for a phonologically distinct class. Both shapes are parseably safe only at word-initial position — mid-compound bare-vowel syllables violate the consonant-onset invariant. No action needed until a forcing case arises. Documented in § Syllable Structure.
- [x] ~~Allow CVC codas freely, or restrict to a subset of consonants?~~ **Resolved.** CVC codas are restricted: preferred `n l r m s`, marked `z f h`, stops discouraged. Full rule in §CVC Root Reserve and `notes/anchor-inventory.md §Design Constraints`. CVCC tier is the relaxed alternative — no CV stem restriction; CC coda from sonorant/fricative set.
- [x] ~~Define phonotactics at compound boundaries explicitly?~~ **Resolved.** CV-primitive design makes all internal compound boundaries V.C by construction — no clusters arise. CVC/CVCC forms are particle-surrounded in grammar and never directly chained. See open-questions.md § Phonology.
