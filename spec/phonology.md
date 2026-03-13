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

**Total: 16 consonants**

Excluded by design: th, v, x, q, c (redundant with k/s), uvulars, retroflexes, ejectives, clicks.
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
- One `'` per compound is the norm; more than one level of explicit grouping should be restructured as a phrase.

**First corpus attestation:** S045 (T-APO-001).

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

## Open Questions

- [ ] Adopt vowel length as a morphological tool, or avoid complexity?
- [ ] Allow CVC codas freely, or restrict to a subset of consonants?
- [ ] Define phonotactics at compound boundaries explicitly?
