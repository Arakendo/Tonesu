# Compounds

Compound words are the engine of Tonesu vocabulary. Almost every word in the language is a compound — a sequence of primitive roots that together name a concept.

---

## The basic rule: right-branching

In a compound, the **rightmost root is the head** — it determines the grammatical class and general meaning. Everything to its left modifies it.

```
to-li     =  to (knowledge) + li (person)     →  knower, scholar
to-su-mu  =  to-su (organised knowledge) + mu (device)  →  library, database
```

The parse is **right-branching by default**: in a chain `A-B-C`, the structure is A modifying [B-C].

```
to-su-mu          →  [to + [su + mu]]
                      knowledge + [structure + device]
                  =   knowledge-organisation device
```

---

## Reading a new compound

Because Tonesu compounds are compositional, you can decode them left to right:

1. Identify each root (see [Primitives](../reference/primitives.md))
2. Find the head (rightmost root)
3. Let the left roots narrow the meaning

**Practice:**
```
ra-ki-mu   =  ra (energy) + ki (motion/change) + mu (device)
           →  energy-change device  =  engine, motor, generator
```

```
ne-ra      =  ne (relation) + ra (energy)
           →  energetic relation  =  resonance, energetic coupling
```

---

## The juncture marker `'`

Long compounds are still right-branching by default. When a left subgroup should be read as a unit before combining with the rest, use `'` to mark its right boundary:

```
pa-wi'ka-su   =  [pa-wi] + [ka-su]
              →  [destination-place] + [structured-action]
              =  shrine, temple (a place of structured intentional action)
```

Without the `'`, the parse would be `pa + [wi + [ka + su]]` — which reads differently. The apostrophe makes the intended grouping visible.

---

## Derivational suffixes

Some roots act as productive suffixes that specify the grammatical role of a compound:

| Suffix | Role | Example |
|--------|------|---------|
| `-li` | agent (person who does X) | `to-li` = knower, scholar |
| `-mu` | device (thing that does X) | `ra-ki-mu` = engine |
| `-pa` | place (where X happens) | `wi-ka-pa` = place of ritual |
| `-ki` | entering a state (inchoative) | `ne-ra-ki` = to enter resonance |
| `-su` | structural result | `wi-ka-su` = ritual (organised practice) |

**Stacking order:** root → semantic modifier → role suffix.

```
to-ki-mu   =  to-ki (knowledge-change) + -mu (device)  →  computer
to-ki-li   =  to-ki (knowledge-change) + -li (agent)   →  learner
```

---

## Negation prefix `no-`

Prefixing `no-` to a root or compound negates or reverses it:

```
no-         =  absence, negation, lack of
no-de-ma    =  no + decay + matter  →  salt, preservative matter
no-ne-fe    =  no + relation + boundary  →  no dependency, free-standing
```

---

## Depth and complexity

Most compounds are 2–4 roots. Longer compounds are valid but should use `'` grouping to keep the parse clear at depth 5 or more. If a compound feels unwieldy, it is usually better expressed as a multi-word phrase.

---

## Three stages of a compound's life

1. **Compositional** — you read it and the meaning falls out directly
2. **Algebraic default** — the most useful reading becomes the expected one in context
3. **Registry-stabilised** — the compound has a canonical definition in the word list

Most of the words in [the word list](../reference/words.md) are at stage 3. Some are still compositional and do not need a registry entry.
