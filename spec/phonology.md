# Phonology

## Status: Draft

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

- CV: most common (ka, li, mu, se)
- V: allowed at word start only (a-, e-)
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
A'B-C-D   →   A modifies [B-C-D]   (single modifier + pre-bound unit)
A-B'C-D   →   [A-B] modifies [C-D] (plain chain + pre-bound unit)
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

Four sentence- and phrase-level marks supplement `'`. Unlike `'`, these operate **outside** compound boundaries — at clause, sentence, or phrase level. They have no phoneme equivalents; speech realizes them through pitch, stress, and prosodic phrasing.

| Mark | Name | Function |
|------|------|----------|
| `,` | clause separator | prosodic pause between a frame clause and its matrix, or between list items |
| `!` | exclamation mark | end-of-utterance: heightened affective or emphatic force |
| `?` | question mark | end-of-utterance: interrogative; orthographic counterpart to grammatical `to-si` |
| `~` | approximation mark | pre-positional hedge: "approximately / roughly / on the order of / something like" |

---

### `,` — Clause Separator

A **prosodic pause** between clausal units. Recommended when a frame clause (`go`, `wi`, `ta`) precedes the matrix and the boundary benefits from an explicit mark. Also separates items in a coordinated list.

```
ta ti-de, la-mi lo-mu ka-be         →  In the past, I grew the object.
go [la-lu ki], la-mi fa-be          →  Because the light moved, my affect rose.
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

Pre-positional hedge meaning **"approximately / roughly / on the order of / something like."** Attaches before a numeral, NP, compound, or time reference. Not compound-internal — always at the left edge of the unit it qualifies. In a full measurement expression, `~` pre-poses the entire `[digit] [scale] nu [domain]` block.

**Spoken form: `ven`** — registered as G010 in `registry/roots.md`. In speech, `~` is realized as `ven`. The written form `~` is canonical in formal and technical Tonesu. `ven` may appear in written text where a phonetic or poetic rendering is intended (verse, informal writing, transcribed speech); in all such cases it is understood as a graphical variant of `~`, not a distinct word.

**With numerals and measurement:**
```
~gal nu li                          →  about 3 people
~hin pir nu pa                      →  roughly 5 km
~bol nil nil nil nu hulm            →  on the order of 1,000 years
~varn                               →  approximately π (loose derivation or estimate)
```

**With compounds and concepts (linguistic and notes register):**
```
~zo-li                              →  something like a person / roughly person-class
~ta ti-be                           →  somewhere around the future / roughly "later"
~to-si                              →  something like a question / quasi-interrogative framing
```

Multiple `~` marks in a sentence are permitted, each scoping its own following unit independently.

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

These are prioritised candidates when CVC roots are needed. All 8 forms assigned to digits 1–8 (March 2026); see `notes/cvc-inventory.md`.

---

## Phonological Tier Stratification

The full tier system in order of word-shape complexity:

| Pattern | Tier | Contents | Admission rule |
|---------|------|----------|----------------|
| CV | Primitives | Closed ontological root set | Passes all three primitive validation rules (`registry/primitives.md`) |
| CV-CV+ | Compounds | Open compositional vocabulary | Expressible from existing roots; no new primitive needed |
| CVC | Lexical descriptors | Digits, colors, scale prefixes, observational distance anchors | Closed-class categories needing fast phonological recognition |
| CVCC | Exceptional anchors | Mathematical/physical constants; convention-defined units with no compositional expression | Assemblage-First Rule: see `notes/cvc-inventory.md §The Assemblage-First Rule` |

**Assemblage-First Rule (summary):** The default for any concept — however complex — is compositional assemblage. A long or unwieldy compound is not grounds for a new lexical atom at any tier. CVCC is the pressure valve for the specific case where assemblage is genuinely impossible (irrational/transcendental values, convention-defined constants) AND a stable atomic form is functionally necessary. A new CV primitive is never the answer to an awkward compound.

---

## Open Questions

- [ ] Adopt vowel length as a morphological tool, or avoid complexity?
- [x] ~~Allow CVC codas freely, or restrict to a subset of consonants?~~ **Resolved.** CVC codas are restricted: preferred `n l r m s`, marked `z f h`, stops discouraged. Full rule in §CVC Root Reserve and `notes/cvc-inventory.md §Design Constraints`. CVCC tier is the relaxed alternative — no CV stem restriction; CC coda from sonorant/fricative set.
- [x] ~~Define phonotactics at compound boundaries explicitly?~~ **Resolved.** CV-primitive design makes all internal compound boundaries V.C by construction — no clusters arise. CVC/CVCC forms are particle-surrounded in grammar and never directly chained. See open-questions.md § Phonology.
