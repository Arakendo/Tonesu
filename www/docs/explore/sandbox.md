# Sandbox

This is the exploratory space. Compounds built here are **not necessarily registered** — they're constructed to probe what the language can express, find interesting readings, discover what's under-served, and test the generative limits of the root set.

Some of these will get registered. Some will reveal gaps. All are valid constructions.

---

## How to explore

Start with a **concept** or **experience** you want to express. Then:

1. Identify which primitive roots are relevant (see [Primitives](../reference/primitives.md))
2. Apply the [pattern](patterns.md) that fits the conceptual role
3. Check right-branching: the parse is always *rightmost-binding* unless you add `'`
4. Read back what you get — does the compound say what you meant? Does it say something *different* that's also interesting?

---

## Assembled constructs

### Curiosity

Want to say "desire to know"?

```
wi   =  intention / desire
to   =  knowledge / model

wi-to  →  intention toward knowledge
```

Right-branching: `wi` modifies `to` → "knowledge-directed intention" = **curiosity**. Clean and direct.

Now extend it:

```
wi-to-ki   →  entering the state of knowledge-seeking
           →  the moment of becoming curious
```

And the person:

```
wi-to-li   →  person of knowledge-directed intention
           →  the curious one / the seeker
```

---

### Nostalgia

Direct translation isn't the goal — the question is: what does the *structure* of nostalgia look like in Tonesu?

Nostalgia involves:
- a past time (`ti` + temporal direction)
- affective quality (`fa` — felt interior state)
- a sense of value or loss (`vo-de` — value decreasing)

Try:

```
fa-ti  →  affective state anchored in time
        →  felt temporal state: memory mood, nostalgia-region
```

But that's symmetric — it doesn't capture the *backward pull*. Add direction:

```
fa-ti-di  →  affect + time + direction
           →  affect oriented toward time: the pull back
```

Right-branch: `ti-di` = *temporal direction* (a moment oriented backward); `fa-(ti-di)` = felt state of backward temporal orientation. This is closer.

Or go structural: nostalgia includes a *gap* between the current state and the valued past:

```
fa  ne  vo-ti-de  →  affect is: value-of-past decreasing
                  →  the felt awareness of fading past value
```

Neither of these is a clean single compound. Tonesu might need a sentence to say this rather than a word — which is itself information about the language.

---

### Coincidence

A coincidence is two events in the same time and place with no causal connection:

```
go-no-ne  →  origin with no connection
           →  uncaused occurrence, random emergence
```

But coincidence specifically requires *two* things happening together:

```
zi-go-no-ne  →  mutual event (zi), from non-connected origin (go-no-ne)
             →  mutual occurrence without shared cause
             →  coincidence
```

Parse: `zi` modifies `[go-no-ne]` as a whole. The mutual/coupling root applied to an uncaused pair of events. Strong candidate.

---

### Justice

Justice combines:
- intentional action (`ka`)
- value/worth (`vo`)
- structure/system (`su`)
- correctness (alignment with principle — `to-ne`, perhaps)

Try:

```
ka-vo-su  →  action organized by value
           →  value-structured action system
           →  institutional justice
```

Or more precisely, justice as the *alignment* between action and value:

```
ne-vo-ka  →  relation between value and action
           →  the bond of value and act
           →  rightness, justice as a condition (not an institution)
```

These are meaningfully different readings. `ka-vo-su` is a system of justice; `ne-vo-ka` is the property of being just. Both are valid; neither is registered yet.

---

### Grief

Grief has structure: `fa` (affect) + `de` (decay/loss) + `li` (the agent it happens to):

```
fa-de  →  affect in decay
        →  felt loss, the degrading condition
```

The compound is predicate-class: used as `la-X ne fa-de` ("X is in a state of felt loss"). The verbal form:

```
fa-de-ki  →  entering the state of felt loss
           →  to begin grieving, the onset of grief
```

And the noun form (the person mid-grief):

```
fa-de-li  →  person of felt loss
           →  the grieving one
```

---

### Coincidence vs synchrony

These are a minimal pair worth distinguishing:

```
zi-go-no-ne  →  mutual event + uncaused origin = coincidence (unconnected things happening together)
zi-ti-ne     →  mutual event + temporal connection = synchrony (two things whose timing is coupled)
```

`zi-go-no-ne`: the connection is absent (`no-ne`)
`zi-ti-ne`: the connection is temporal (`ti-ne` = time-linked)

---

### Trust

Trust = the disposition to act toward another agent as if their intentions align with yours, without requiring evidence:

```
wi-ne-li  →  intention + relation + person
           →  person who is in intentional relation
           →  relational agent (not strong enough)
```

Try it differently. Trust is acting as if `lo-X wi-ne-mi` (X's intention is connected to mine):

```
no-to-wi  →  action from intention, without requiring knowledge first
           →  acting on intention without verification
           →  faith / trust as a disposition
```

Right-branch: `to-wi` = knowledge-directed intention; `no-(to-wi)` = disposition opposed to knowledge-requiring intention. That's not quite right either — the `no-` reads as negating the whole, producing "lacking knowledge-based intention."

Restructure with `'`:

```
no'to-wi  →  [no] • [to-wi]  = absence of [knowledge → intention] gate
           →  acting without requiring knowledge first
           →  trust
```

This shows how `'` changes meaning. `no-to-wi` (right-branching without juncture) and `no'to-wi` (juncture makes `no` scope over `to-wi` as a unit) produce slightly different readings — one negates a compound, the other negates a causal chain. Worth distinguishing.

---

### Minimal pairs

Small changes produce systematic meaning contrasts. These pairs are good for testing your parse:

| Pair | A | B |
|------|---|---|
| `fa-be` / `fa-de` | affect rising (excitement, hope) | affect falling (grief, despair) |
| `to-ki` / `to-ki-mu` | to grasp a concept | device for constructing concepts |
| `wi-to` / `to-wi` | desire-for-knowledge (curiosity) | knowledge-directed-intention (planning) |
| `ka-vo` / `vo-ka` | action graded by value (ethical action) | value evaluated by action (pragmatic ethics) |
| `no-ki` / `ki-no` | absence of motion (stillness) | motion toward absence (approach to dissolution) |
| `go-be` / `be-go` | caused growth (generation) | growth as origin (fertility, genesis) |
| `ne-fe` / `fe-ne` | relational threshold (dependency condition) | boundary as relation (the edge itself as a connection) |

---

## What these reveal

Some observations from the constructs above:

**The language handles state and event distinctly.** `fa-de` is a state; `fa-de-ki` is the event of entering it. English uses one word ("grief") for both.

**`no-` is precise.** It doesn't produce opposites — it produces absences. Cold is `no-ha`, not the opposite of hot. Stillness is `no-ki`, not the opposite of motion. This forces clear thinking about what the negation actually means.

**`'` is a tool for scope disambiguation, not just readability.** The `no'to-wi` / `no-to-wi` pair shows that without juncture, right-branching may produce a subtly different compound than intended.

**Some English concepts don't compress into single words.** Nostalgia needed a phrase. This is fine — not every concept needs a lexical atom. The language is composable at the sentence level too.

**New compounds are always readable on first encounter** — you don't need to have seen them before if you know the roots and patterns. That's the design guarantee.
