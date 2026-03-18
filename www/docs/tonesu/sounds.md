# Sounds

Tonesu uses a small, globally pronounceable sound inventory. No special training is required — every sound approximates something in a major world language.

**One letter = one sound. No silent letters, no digraphs, no exceptions.**

---

## Consonants

17 consonants. Excluded by design: `th`, `x`, `q`, `c` (redundant with k/s), uvulars, retroflexes, ejectives, clicks.

| Symbol | Sounds like | Primitive root |
|--------|-------------|---------------|
| `p` | **p** in *spin* | `pa` — place |
| `b` | **b** in *ban* | `be` — growth |
| `t` | **t** in *stop* | `to` — thought/pattern |
| `d` | **d** in *dog* | `di` — direction |
| `k` | **k** in *skip* | `ka` — action |
| `g` | **g** in *go* | `go` — cause |
| `m` | **m** in *man* | `mu` — object |
| `n` | **n** in *no* | `ne` — relation |
| `s` | **s** in *sun* | `su` — structure |
| `z` | **z** in *zoo* | `zo` — living thing |
| `l` | **l** in *let* | `li` — person |
| `r` | flap or trill, not retroflex | `re` — repetition |
| `f` | **f** in *fan* | `fe` — boundary |
| `h` | **h** in *hat* | `ha` — heat |
| `y` | **y** in *yes* | — |
| `w` | **w** in *win* | `wi` — will |
| `v` | **v** in *vine* | `vo` — value |

---

## Vowels

5 vowels — pure, consistent, no context-dependent shifts.

| Symbol | Sounds like | Primitive root |
|--------|-------------|---------------|
| `a` | *father* | `ma` — matter |
| `e` | *bed* | `se` — perception |
| `i` | *feet* | `si` — signal |
| `o` | *go* | `so` — sound |
| `u` | *food* | `mu` — object |

---

## Syllable shapes and tiers

Every word's shape tells you what kind of thing it is. There are four structural tiers:

| Shape | Tier | What lives here | Example |
|-------|------|-----------------|---------|
| CV | Primitive root | The 34 foundational roots | `to`, `li`, `go` |
| CV-CV+ | Compound | Open vocabulary assembled from roots | `toli` (scholar), `rakimu` (engine) |
| CVC | Lexical atom | Digits, colors, scale prefixes — closed classes | `kel`, `sun` |
| CVCC | Exceptional anchor | Mathematical/physical constants only | `varn` |

**Every internal syllable in a compound begins with a consonant.** This means you can always segment a compound left-to-right without backtracking. The parser never needs to guess.

---

## Stress

**Stress always falls on the first syllable.** No exceptions, no marking needed.

- `KA-ru` · `LI-na-se` · `SU-mu-to` · `TO-li` · `RA-ki-mu`

---

## Writing

Written Tonesu is **solid** — compounds are written without spaces or hyphens between roots. The word for *scholar* is `toli`, not `to-li`.

The apostrophe `'` is the only normative non-alphabetic character in a word. It marks a structural grouping boundary inside a long compound. See [Notation](notation.md).

Analytic forms like `to-li` (hyphenated) appear in guides and parse breakdowns to show structure — but they are metalinguistic notation, not the written word itself.

---

## Scope-modifier prefixes

A bare vowel at the start of a compound adjusts its register or scope without adding lexical content:

| Prefix | Effect | Example |
|--------|--------|---------|
| `a-` | abstract / universal | `ato` — knowing-in-general |
| `i-` | precise / particular | `itoli` — this specific scholar |
| `u-` | interior / foundational | `uto` — tacit knowledge |
| `o-` | collective | `oli` — community as a unit |
| `e-` | emergent / in-process | `eki` — change in progress |

When roots are shown with hyphens in these pages — like `to-li` — that is an *analytic notation* to help you see the structure. Those hyphens are not part of the word.
