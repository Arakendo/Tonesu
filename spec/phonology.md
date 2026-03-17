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
- V: **word-initial position only — admitted as the V-prefix class (VPC-001, March 2026).** A bare vowel syllable may open a word or compound; it must not appear mid-compound (invariant 1). Only 5 V forms exist (`a e i o u`). All 5 are admitted as **compound-initial scope-modifier prefixes**: a V-prefix adjusts the register or scope of the following root without adding independent lexical content. Because no V syllable can appear mid-compound, V-prefixes are always unambiguously word-initial, making their morphological role structurally guaranteed.

  **V-Prefix Scope Semantics (admitted):**

  | Prefix | Sound symbolism | Scope effect |
  |--------|----------------|-------------|
  | `a-` | broad, open, general | **abstract/universal** — root at its broadest conceptual category (`a-to` = knowing-in-general; `a-su` = form-as-such) |
  | `i-` | small, sharp, precise | **particular/precise** — root applied to a specific instance (`i-to-ze` = this particular fact) |
  | `u-` | deep, heavy, closed | **interior/foundational** — the tacit or underlying mode of root (`u-to` = interior knowing; `u-su` = deep structure) |
  | `o-` | outward, collective | **collective/distributed** — root as applying to a group as a unit (`o-li` = community-as-unit ≠ `pu-li` count) |
  | `e-` | shifting, emergent | **transitional/in-process** — root in an unsettled, forming state (`e-ki` = emergent/progressive change) |

  **Parse behavior:** Right-branching default applies — `a-to-li` = `a` scopes over `[to-li]` = universal-(knowledge-agent). Written form: solid, no hyphen in ordinary prose (`ato`, `isu`, `oli`, `eki`, `usu`). Morpheme-boundary notation: `a-to`, `i-to`, etc.

  **V-prefix `a-` phonological constraint:** `la-` ends in `a`; placing `a-X` in agent position produces `la-a-X`, which merges with `la-X` in fast speech. The other four prefixes (`i- u- o- e-`) are safe after `la-`. **Rule: `a-` forms should be used in predicate or patient position, not agent position after `la-`.**

  **Corpus basis:** VPC-001 (S504–S513). All 5 prefixes attested and productive.

- VC: **admitted — word-initial only** — a vowel-initial syllable with a closing consonant. Shares the word-initial constraint with bare V; mid-compound VC violates invariant 1 and creates lookahead. Word-initial VC parses cleanly because the word boundary precedes it: `el-X`, `an-be`, `im-ra` are unambiguous. **One form currently occupied:** `el` (G028) — the spoken/written form of `—` (prosodic-suspension mark; admitted EMD-002, March 2026). Remaining ~39 VC slots reserved; no second assignment pending. Condition for further expansion: CV near-exhaustion, or need for a phonologically distinct particle/pronoun class. See § Open Questions.
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

**Spoken form: `peld`** (G021) — CVCC; from `pe` (primitive root). In dictation and formal document reading, `peld` is inserted at each `'` position to explicitly signal the subcompound boundary. **`peld` is a valid written substitute for `'`** wherever the apostrophe symbol is unavailable or a word-form is preferred.

---

## Punctuation and Notation Marks

Thirteen marks supplement `'`. Unlike `'`, these operate **outside** compound boundaries — at clause, sentence, or metalanguage level. Each mark carries a **use** classification: **spoken + written** marks are live in spontaneous discourse and writing alike; **written** marks are primary to written and formal-analytic contexts, with spoken forms available for dictation and pedagogy. Sentence and phrase marks have no phoneme equivalents; speech realizes them through pitch, stress, and prosodic phrasing. The marks `:` and `::` serve primarily as metalanguage notation and appear in Tonesu sentences only in the role specified for each. The marks `-` and `{}` are normative in metalinguistic, pedagogical, and technical contexts; conventional compound writing remains solid.

| Mark | Name | Use | Function |
|------|------|-----|----------|
| `,` | clause separator | spoken + written | prosodic pause between a frame clause and its matrix, or between list items; spoken form `wald` (G024) |
| `!` | exclamation mark | spoken + written | end-of-utterance: heightened affective or emphatic force; spoken form `bold` (G025) |
| `?` | question mark | spoken + written | end-of-utterance: interrogative; orthographic counterpart to grammatical `to-si`; spoken form `geld` (G026) |
| `~` | approximation mark | spoken + written | pre-positional hedge: "approximately / roughly / on the order of / something like"; spoken form `ven` (G010) |
| `()` | evidential frame | spoken + written | clause-level epistemic bracket: content is reported, inferred, or unattributed — not directly asserted; spoken forms `vund` (G014, open) / `vunds` (G015, close) |
| `[]` | aside / commentary frame | written | non-semantic editorial or analytic annotation — does not alter truth conditions of surrounding text; removable without semantic change; spoken forms `zeld` (G022, open) / `zelds` (G023, close) serve dictation and pedagogy |
| `:` | topic frame / definition mark | spoken + written | sentence-initial: "as for {topic}, ..." (topic frame); metalanguage: explanatory gloss (`term : reading`) |
| `::` | canonical definition mark | spoken + written | structural decomposition (`term :: roots`); appears in written and verbal discourse; spoken form `helms` (G012) |
| `/` | parallel partition | spoken + written | structural midpoint of a bi-clausal parallel or antithetical construction; marks two clauses as formally paired; spoken form `vel` (G013) |
| `""` | quotation / mention frame | spoken + written | verbatim quotation of direct speech, linguistic mention (use/mention distinction), and titles/labels; spoken forms `sild` (G016, open) / `silds` (G017, close) |
| `-` | morpheme boundary mark | written | marks root boundaries in a compound; normative in metalinguistic, pedagogical, and math/science contexts; spoken form `feld` (G018) |
| `{}` | structural slot / scope bracket | written | marks a structural slot placeholder or formal scope group; normative in metalinguistic, mathematical, and formal-reasoning contexts; spoken forms `suld` (G019, open) / `sulds` (G020, close) |
| `;` | sequential connector | written | directed A-then-B link: A ; B = A, and then B (connection type not asserted — may be causal, incidental, adversative, or temporal); single-clause premise only; left-to-right only; spoken form `teld` (G027) |
| `—` | prosodic suspension | spoken + written | holds a phrase, clause, or fragment in incompletion — suspended, not closed; no assertion about what follows; may appear post-clause, mid-NP-list, after fragments, or terminally; spoken/written-substitute form `el` (G028, VC tier) |

---

### `,` — Clause Separator

A **prosodic pause** between clausal units. Recommended when a frame clause (`go`, `wi`, `ta`) precedes the matrix and the boundary benefits from an explicit mark. Also separates items in a coordinated list.

```
ta ti-de, la-mi lo-mu ka-be         →  In the past, I grew the object.
go {la-lu ki}, la-mi fa-be          →  Because the light moved, my affect rose.
la-mi lo-mu, lo-ma, lo-ra ka-ko    →  I stored the object, the material, and the energy.
```

Omit when the boundary is unambiguous without it.

**Spoken form: `wald`** (G024) — from `wa` (free CV; `w` = flowing): the pause mark. CVCC. In dictation and formal document reading, `wald` is inserted at each `,` position. **`wald` is a valid written substitute for `,`** wherever the symbol is unavailable or a word-form is preferred.

---

### `!` — Exclamation Mark

End-of-utterance marker signaling **heightened affective or emphatic force**. The sentence is grammatically complete without `!`; the mark signals what speech realizes as elevated pitch, stress, or intensity.

```
la-mi fa-be!                        →  My affect is rising! (elation, alarm)
la-tu ka!                           →  Act! (imperative with force)
```

Compatible with any sentence type including questions: `to-si  la-tu  ki!` = Where did you go?! (emphatic).

**Spoken form: `bold`** (G025) — from `bo` (free CV; `b` = impact/force): the force mark. CVCC. In dictation and formal document reading, `bold` is pronounced at the `!` position. **`bold` is a valid written substitute for `!`** wherever the symbol is unavailable or a word-form is preferred.

---

### `?` — Question Mark

End-of-utterance marker signaling **interrogative mode**. The grammatical question mechanism (`to-si`) takes priority — `?` is its orthographic counterpart.

- **Formal/careful writing:** `to-si` is required in the clause; `?` appears at the end for clarity.
- **Casual and notes register:** `?` may substitute for the fronted polar `to-si —`, making it a genuine shorthand.

```
to-si  la-tu  lo-to  ka-ko?         →  Who stored the knowledge?
la-tu  lo-mu  ka-be?                →  Did you grow it? (casual: ? replaces fronted to-si)
```

**Spoken form: `geld`** (G026) — from `ge` (property/attribute): the mark that seeks a property. CVCC. In dictation and formal document reading, `geld` is pronounced at the `?` position. **`geld` is a valid written substitute for `?`** wherever the symbol is unavailable or a word-form is preferred.

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

**Register: written.** Aside frames arise in written meta-commentary and formal analysis; they do not occur naturally in spontaneous speech. The spoken forms `zeld`/`zelds` exist for dictation and pedagogical settings where bracket positions must be explicitly named. Discourse use is not yet established — if a natural spoken-aside construction emerges in corpus use (e.g., a teaching or rhetorical register), this note should be revisited.

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

**Spoken forms: `zeld`** (G022, open) / **`zelds`** (G023, close) — CVCC/CVCCS; neutral initial `ze`. `zelds` is produced by the bracket-pair convention (`zeld` + `s`). In ordinary speech `[]` frames are not produced; the spoken forms serve dictation, formal document reading, and pedagogical contexts where bracket positions must be explicitly signaled. **`zeld` and `zelds` are valid written substitutes** for `[` and `]` wherever the bracket symbols are unavailable or word-forms are preferred.

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

### `""` — Quotation / Mention Frame

A **verbatim-content marker** with three licensed uses:

**1. Direct speech.** The enclosed string is the literal utterance of the agent.

```
la-mi li "la-tu zo"          →  I said: "you live."
```

Compare the evidential bracket: `la-mi li (Matthew 5:7)` = I said [citing Matthew 5:7] — source citation, not literal reproduction.

**2. Mention (use/mention distinction).** The enclosed form is being named or discussed as a token, not used as a root or particle.

```
"si" helms si-ge             →  "si" is by definition signal-property.
"tonofe" helms to-no-fe      →  "tonofe" denotes to-no-fe.
```

This is the canonical form for metalinguistic definitions and registry entries where the written token itself is the subject.

**3. Titles and conceptual labels.** Proper names of texts, concepts, or named domains.

```
la-mi to lo-"Laozi"          →  I know [the text] "Laozi".
```

**Framing rule:** Content inside `""` is structurally opaque to the enclosing clause. The parser does not interpret internal compounds or particles as arguments of the outer sentence; the quoted string is an atom from the surrounding clause's perspective.

**Relation to other marks:**
- `()` — *epistemic hedge*: content is reported or unattributed; speaker does not directly assert it.
- `""` — *verbatim claim*: content is reproduced exactly as a string; no epistemic qualification.
- `[]` — *non-semantic annotation*: removed without semantic change.

`""` may appear inside `[]` (metalinguistic annotation) and inside `()` (quoted reported speech). `()` inside `""` is disallowed — evidential wrap may not appear inside a verbatim string.

**Register:** normative in written Tonesu. In speech, `sild` announces the open boundary and `silds` closes it. In casual speech quotation prosody alone (pitch boundary, slight hold) suffices; `sild`/`silds` are required in dictation, formal citation, and wherever nested quotation risks misparse.

**Spoken form: `sild`** (G016, open) / **`silds`** (G017, close) — registered in `registry/roots.md`. `si` root: signal/communication. `sild` is CVCC; `silds` is CVCCS, produced by the bracket-pair convention (`sild` + `s`; the `+s` coda marks the secondary/closing element, per the CVCCS admission rule). Forms the minimal pair `sild`/`silds`. **`sild` and `silds` are valid written substitutes** for `"` and `"` wherever the double-quote symbols are unavailable or word-forms are preferred.

**Probationary status:** admitted March 2026. Principal pressure: the use/mention distinction in metalinguistic registry entries (writing about `"si"` as a token, not using `si` as a root) and direct-speech corpus sentences. `()` does not cover verbatim reproduction. Review after first 20 corpus attestations.

---

### - — Morpheme Boundary Mark

**Register: written.** Appears in metalinguistic, pedagogical, and technical-analytic contexts; not in spontaneous discourse.

**Function:** explicitly marks the boundary between adjacent roots in a compound. Normative in metalinguistic, pedagogical, and formal-analytic contexts; in ordinary written Tonesu, compounds are written solid (e.g., `tofesuki` not `to-fe-su-ki`). The mark appears when the morpheme structure of a compound is itself the subject of discourse, annotation, or instruction.

**Contexts where `-` appears:**
1. **Metalinguistic analysis** — naming compound structure explicitly: `"toli" : to-li` (lit. `"toli"` is `to` modifying `li`)
2. **Pedagogical display** — parse breakdown in examples: `tokimu :: to-ki-mu`
3. **Math and science** — notation that exhibits constituent operators; e.g. the pattern `X-su` where the operator relation itself is the topic
4. **Registry and spec** — analytic notation throughout this document continues to use `-`

**Convention:** ordinary prose and standard compound writing uses the solid form only. `-` is not a general word separator and does not appear between words in running text.

**Spoken form: `feld`** (G018) — from `fe` (boundary/limit): the mark that renders a root boundary visible. CVCC. **`feld` is a valid written substitute for `-`** wherever the ASCII hyphen symbol is unavailable or a word-form is preferred.

---

### {} — Structural Slot / Scope Bracket

**Register: written.** Appears in metalinguistic, mathematical, and formal-reasoning contexts; not in spontaneous discourse.

**Function:** marks a structural slot placeholder or formal scope group. The open brace `{` introduces the scope; the close brace `}` closes it. Normative in metalinguistic, mathematical, and formal-reasoning contexts.

**Contexts where `{}` appears:**
1. **Grammar slot notation** — `la-{agent}`, `go {premise}, result`
2. **Set and group notation** (math and science) — `{X, Y, Z}` denotes the set or group containing X, Y, and Z
3. **Structural grouping in formal reasoning** — marking scope of an operator or quantifier over a defined region
4. **Registry and spec** — slot placeholders and structural groupings in grammar examples and entry formats

**Relation to other brackets:**
- `()` — *epistemic frame*: content is reported or unattributed; speaker does not directly assert it.
- `[]` — *non-semantic aside*: removed without semantic change to the surrounding argument.
- `{}` — *structural scope*: marks a formal slot or set boundary. No epistemic qualification; content type is structural, not propositional.

**Spoken forms: `suld`** (G019, open) / **`sulds`** (G020, close) — from `su` (structure): the bracket that marks structural scope. `suld` is CVCC; `sulds` is CVCCS — produced by the bracket-pair convention (`suld` + `s`; the `+s` coda marks the secondary/closing element, per the CVCCS admission rule). Forms the minimal pair `suld`/`sulds`. **`suld` and `sulds` are valid written substitutes** for `{` and `}` wherever the brace symbols are unavailable or word-forms are preferred.

---

## Admitted Marks (March 2026)

### `;` — Sequential Connector (Admitted March 2026)

**Function:** marks a directed sequential link between two clauses: **A ; B** = A, and then B. The connection type (causal, incidental, adversative, temporal) is **not asserted by the mark** — it is supplied by content and context. This distinguishes `;` from `go`: `go` asserts that a mechanism runs from A to B (necessary connection); `;` notes that B followed A (constant conjunction). The distinction is Hume's.

**Where `;` is preferred:**
- Multi-link natural-process or narrative chains of ≥3 steps (reduces `go {…},` duplication)
- Chronicle / observational / proverbial register where the sequence is noted but the mechanism is not argued
- Cases where `go` would over-assert a causal mechanism (S484: the clock moved; we departed)
- Adversative sequences where `go` would mis-assert causality (S493: the plan was made; it failed)

**Where `go {…},` is required:**
- Logical deduction / argumentative necessity (Cogito, modus ponens — S482/S444)
- Complex or multi-clause premises (`;` is single-clause only — S487)
- Retrospective causal framing with `ti-de` (`;` is left-to-right only — S486)

**Spoken form:** `teld` (G027) — CVCC; from `te` (free CV; `t` = sequence/segmentation, sound symbolism). Functionally necessary: without a distinct spoken form, dictation of `A ; B` would require `go`, which collides with the causal mechanism particle and erases the precise distinction that `;` was admitted to encode. `teld` is a valid written substitute for `;` wherever the symbol is unavailable or a word-form is preferred.

**Chain parse rule:** chains are **left-chaining** — each step sequences the next:

```
A ; B ; C
=  A, and then B, and then C
```

**Single-clause constraint:** `;` is valid only when the premise (left side) is a single clause. A complex or multi-clause premise requires the full `go {…},` form (confirmed S487).

**Relation to `/`:** `/` marks structural pairing between two co-equal clauses (symmetric, no directionality). `;` marks directed sequence (asymmetric, left-to-right). They are not interchangeable.

**Corpus status:** admitted on the basis of 14 viable sentences across 3 text types (SCL-001: S477–S488; SCL-002: S489–S493). Semantic differentiation confirmed at S482 (Cogito: `;` reads as temporal; `go` reads as logical necessity). Sequential-only characterization confirmed at S493 (adversative sequence: `;` correct, `go` wrong). OQ-GO-001 resolved. See `notes/open-questions.md`.

---

### `—` — Prosodic Suspension (Admitted March 2026)

**Function:** marks a **held incompletion** — a phrase, clause, or fragment that is suspended rather than closed. The idea before `—` has not been resolved; the breath is held before whatever (if anything) follows. `—` makes no assertion about the content, connection, temporal order, or status of what follows; it signals only that the unit before it is left open.

**Distinction from other marks:**

| Mark | What it asserts | `—` contrast |
|------|----------------|--------------|
| `,` | completed boundary; clean handoff to next clause | `—` leaves the preceding unit open; resumption emerges from a held state |
| `;` | A followed B (directed sequence, constant conjunction) | `—` asserts no sequence, no connection, no directionality |
| `/` | two clauses formally paired as a dyad (symmetric) | `—` is successive dwelling, not structural pairing |
| `!` | heightened force at end of utterance | `—` is incompletion, not emphasis |

**Admitted positions (EMD-002):**
- Post-clause: `la-su ki — la-mi se lo-ze` (structure changed — I perceived it)
- Mid-patient-list, creating revelation-arrival: `lo-mi lo-de-zo-li — lo-no-de-zo-li` (us, Death — Immortality)
- Pre-reveal mid-sentence: `de-ki ne-di-ko-pa — ko-pa helm be-ma-pa`
- After bare NP fragment: `na-Moses —` (name spoken and suspended)
- Post-agent NP before predicate: `la-de-zo-li — wi-vo de-ki lu-mi`
- Terminal, after a grammatically complete sentence: sentence closed grammatically, phenomenologically open

**Register:** spoken + written. Cross-register: productive in poetry (Dickinson, EMD-001/EMD-002), investigative prose, and any context where a speaker dwells before resumption or trailing silence.

**Spoken/written-substitute form: `el`** (G028) — **VC tier**; first VC-tier form admitted. `e` = shifting/emergent (consistent with V-class sound symbolism); `l` = liquid coda, trailing — phonosemantically appropriate for a suspension that does not close. `el` is **word-initial only** (parse invariant 1 holds; mid-compound VC violates consonant-onset requirement). It cannot be used inside a compound or combined with role-markers.

**Author choice:** `—` (em-dash, U+2014) and `el` are equally normative and refer to the same mark. The author may choose freely between them in any text. `el` is likely preferred in verse where the suspension is itself a voiced presence, in texts where the em-dash glyph is unavailable, or in deliberate poetic contexts where the word-form is more expressive than the symbol. `—` is likely preferred in prose and running text. Neither form takes precedence over the other.

**Corpus basis:** EMD-002 (S514–S523, March 2026). OQ-VC-001 resolved.

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
| CVCCS | Notation pair closers | Spoken forms marking the secondary element of a two-part notation structure: (a) the doublet of a doubled written mark (`::` from `::`; future doubled marks); or (b) the closing bracket of a bracket-pair mark (`)` from `(`). | One rule only: a CVCC notation-marker spoken form may take `+s` to mark the second/closing element of its paired notation structure. Not a free-standing tier; each CVCCS form is bound to its CVCC base. Current instances: `helms` (G012, `::`, `-lm` coda) · `vunds` (G015, `)`, `-nd` coda) · `silds` (G017, `"`, `-ld` coda) · `sulds` (G020, `}`, `-ld` coda) · `zelds` (G023, `]`, `-ld` coda). |

**CVC sub-categories:**

- *Closed-class CVC atoms* — digits and colors. No compositional expression exists; the form defines an irreducible scale anchor or perceptual hue point. The complete set is fixed unless a new irreducible category is identified.
- *Ergonomic shortforms* — scale prefixes and future candidates. A compositional expression exists and remains canonical; CVC phonology is assigned on frequency and measurement-ergonomics grounds. Criteria and full admission rules: `spec/word-formation.md §Ergonomic Shortforms`. Inventory and flags: `notes/anchor-inventory.md §Scale Prefix Inventory` and FLAG-CVC-010.

**Assemblage-First Rule (summary):** The default for any concept — however complex — is compositional assemblage. A long or unwieldy compound is not grounds for a new lexical atom at any tier. CVCC is the pressure valve for the specific case where assemblage is genuinely impossible (irrational/transcendental values, convention-defined constants) AND a stable atomic form is functionally necessary. A new CV primitive is never the answer to an awkward compound.

---

## Open Questions

- [ ] Adopt vowel length as a morphological tool, or avoid complexity?
- [x] ~~**V and VC syllable shapes — status and admission rule.**~~ **Both resolved (March 2026).** V (bare vowel, word-initial only): admitted as **V-prefix scope-modifier class** (VPC-001) — all 5 forms (`a e i o u`) assigned as compound-initial scope modifiers. Documented in § Syllable Structure and spec/word-formation.md § V-Prefix Scope Modifiers. VC (vowel + coda, word-initial only): **admitted, one form occupied** — `el` (G028) as the spoken/written-substitute form of `—` (prosodic-suspension mark; EMD-002, March 2026). Remaining ~39 VC slots reserved. Documented in § Syllable Structure and `§— — Prosodic Suspension`.
- [x] ~~Allow CVC codas freely, or restrict to a subset of consonants?~~ **Resolved.** CVC codas are restricted: preferred `n l r m s`, marked `z f h`, stops discouraged. Full rule in §CVC Root Reserve and `notes/anchor-inventory.md §Design Constraints`. CVCC tier is the relaxed alternative — no CV stem restriction; CC coda from sonorant/fricative set.
- [x] ~~Define phonotactics at compound boundaries explicitly?~~ **Resolved.** CV-primitive design makes all internal compound boundaries V.C by construction — no clusters arise. CVC/CVCC forms are particle-surrounded in grammar and never directly chained. See open-questions.md § Phonology.
