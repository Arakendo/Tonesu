# Compounds

Compound words are the engine of Tonesu vocabulary. Almost every word in the language is a compound — a sequence of primitive roots that together name a concept.

> **Notation in this page:** Written Tonesu has no hyphens — `toli` is the word. The analytic breakdown `to-li` (hyphenated) appears in parentheses or labeled as *parse* to show structure.

---

## The basic rule: right-branching

In a compound, the **rightmost root is the head** — it determines the grammatical class and general meaning. Everything to its left modifies it.

```
toli    (to-li:   to = knowledge, li = person)   →  knower, scholar
tosumu  (to-su-mu: to-su = organised knowledge, mu = device)  →  library, database
```

The parse is **right-branching by default**: in a chain `A-B-C`, the structure is A modifying [B-C].

```
tosumu  (to-su-mu)  →  [to + [su + mu]]
                        knowledge + [structure + device]
                    =   knowledge-organisation device
```

---

## Reading a new compound

Because Tonesu compounds are compositional, you can decode them left to right:

1. Identify each root (see [Primitives](primitives.md))
2. Find the head (rightmost root)
3. Let the left roots narrow the meaning

**Practice:**
```
rakimu  (ra-ki-mu)   ra = energy, ki = motion/change, mu = device
                 →   energy-change device  =  engine, motor, generator
```

```
nera  (ne-ra)   ne = relation, ra = energy
            →   energetic relation  =  resonance, energetic coupling
```

---

## The juncture marker `'`

Long compounds are still right-branching by default. When a left subgroup should be read as a unit before combining with the rest, use `'` to mark its left boundary:

```
pawi'kasu  (pa-wi'ka-su)  =  [pa-wi] + [ka-su]
                          →  [destination-place] + [structured-action]
                          =  shrine, temple (a place of structured intentional action)
```

Without the `'`, the parse would be `pa + [wi + [ka + su]]` — which reads differently. The apostrophe makes the intended grouping visible.

`'` is not just a readability tool — it can be required for correctness. Consider a color modifier attached to a kind-term compound:

```
kerzoseso   →  (wrong) ker modifies only the final root so
ker'zoseso  →  (right) ker modifies {zoseso} as a whole kind-term
```

Without `'`, the color binds to the wrong element. With it, the entire organism class is qualified.

`~` (the approximation mark) can follow `'` immediately to hedge just the subcompound:

```
ker'zoseso   →  the red canid-pack kind
ker'~zoseso  →  the red something-like-canid-pack kind  (uncertain about the base class)
```

---

## Derivational suffixes

Some roots act as productive suffixes that specify the grammatical role of a compound:

| Suffix | Role | Written example | Parse |
|--------|------|-----------------|-------|
| `-li` | agent (person who does X) | `toli` | `to-li` |
| `-mu` | device (thing that does X) | `rakimu` | `ra-ki-mu` |
| `-pa` | place (where X happens) | `wikapa` | `wi-ka-pa` |
| `-ki` | entering a state (inchoative) | `neraki` | `ne-ra-ki` |
| `-su` | structural result | `wikasu` | `wi-ka-su` |

**Stacking order:** root → semantic modifier → role suffix.

```
tokimu  (to-ki-mu)  =  toki (knowledge-change) + -mu (device)  →  computer
tokili  (to-ki-li)  =  toki (knowledge-change) + -li (agent)   →  learner
```

---

## Negation prefix `no-`

Prefixing `no-` to a root or compound negates or reverses it:

```
no-          =  absence, negation, lack of
nodema       (no-de-ma)  =  no + decay + matter  →  salt, preservative matter
nonefe       (no-ne-fe)  =  no + relation + boundary  →  no dependency, free-standing
```

---

## Depth and complexity

Most compounds are 2–4 roots. Longer compounds are valid but should use `'` grouping to keep the parse clear at depth 5 or more. If a compound feels unwieldy, it is usually better expressed as a multi-word phrase.

---

## Three stages of a compound's life

1. **Compositional** — you read it and the meaning falls out directly

```
senoto  (se-no-to)  =  perception + absence + knowledge
                   →  a signal without an interpretive model
```

2. **Algebraic default** — a recognized operator pattern makes the reading predictable across a whole class

```
X-fe  →  boundary / limit of X

tofe  (to-fe)  →  epistemic boundary  (the line between knowledge states)
wife  (wi-fe)  →  intentional limit   (ethical constraint, policy bound)
tife  (ti-fe)  →  temporal deadline
```

3. **Registry-stabilised** — corpus use has confirmed a specific narrower reading

```
rasu  (ra-su)   algebraic reading:  energy structure
                registered reading: star  (stable in astronomy contexts)
```

Most of the words in [the word list](registry.md) are at stage 3. Many useful compounds never need registration — their meaning falls directly out of the structure every time.
