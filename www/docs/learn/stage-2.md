# Stage 2 — Compound construction

Every Tonesu word with more than one root is a compound.
`no-de` (intact), `ka-se` (examine), `ti-fe` (deadline), `si-su-mu` (antenna array) —
all compounds. You've been reading them since Stage 0. Now you get the rules they follow.

---

## The one rule: modifier first, head last

Every Tonesu compound puts the **head** at the right edge.

The head is what the compound *is*. Everything to its left *characterizes* it.

```
to  +  li  =  to-li

↑       ↑
mod    head
        "person"

to-li = knowledge-person = scholar
```

This is the **head-final rule**. There are no exceptions.

---

## Cluster 1 — Two-root compounds

All of these appeared in Stage 0 or 1. The table makes the structure explicit.

```
(1)  to-li      knowledge + person       =  scholar
(2)  ki-li      motion + person          =  traveler
(3)  ne-mu      relation + artifact      =  connector
(4)  ki-mu      motion + artifact        =  vehicle
(5)  no-de      absence + decay          =  intact
(6)  ti-fe      time + boundary          =  deadline
```

In every case: the rightmost root tells you *what category* the compound belongs to
(person, artifact, state). The left root tells you *which kind*.

Look at (3): you encountered `lo-ne-mu` in C001 — *the connector*. `ne` (relation) says
this artifact's job is to form connections. `mu` (artifact) is the head.

Look at (5): `no-de` from Stage 1. `no` (negation/absence) + `de` (decay) = not-decayed
= intact. `de` is the head (the state), `no` is the modifier (absent/negated).

**New root: `ne`** — relation, connection, coupling. Appeared in `ne-mu` since Stage 1
but wasn't first-class. As a root it names the property of *being relational* — linking,
joining, coupling. `ne-ki` = relational process = networking. `ne-li` = one who forms
connections.

**New root: `su`** — structure, organized form. Appeared in `si-su-mu` (signal-structure-
artifact = antenna array) and `ka-to-su-ki` (acknowledged). As a modifier: `su-X` = the
structured form of X. As a head: `X-su` = the organized system that X produces. `su-li`
= architect (person whose domain is structure).

---

!!! question "Exercise 1 — Build `to-li`"
    A scholar is a *knowledge-person*. Pick the roots in order: modifier first, head last.

    <div class="tn-learn-picker"
         data-template="___-___"
         data-answers='["to","li"]'
         data-mode="both"
         data-ok="to-li — knowledge-person — scholar ✓"
         data-items='[{"form":"to","gloss":"knowledge"},{"form":"li","gloss":"person"},{"form":"ki","gloss":"motion"},{"form":"ne","gloss":"relation"},{"form":"mu","gloss":"artifact"},{"form":"su","gloss":"structure"}]'>
    </div>

??? success "Explanation"
    `to` (knowledge) + `li` (person). `li` is the head — this is a *person*. `to` tells
    you which kind: a *knowledge*-person.

    The `-li` pattern extends to every domain root. You can now build `ki-li` (traveler),
    `ne-li` (connector-of-people), `su-li` (architect) without a dictionary.

---

## Cluster 2 — Operator heads

Certain roots are especially productive as **heads** because they consistently transform
the modifier's meaning in the same way, regardless of what the modifier is.

| Head | What it produces | Example | Meaning |
|------|-----------------|---------|---------|
| `-li` | agent in domain X | `to-li` | scholar |
| `-mu` | artifact / instrument of X | `to-mu` | document / data store |
| `-ki` | process / change involving X | `to-ki` | learning |
| `-su` | organized system of X | `to-su` | knowledge system |
| `-ne` | relational coupling of X | `si-ne` | communication (signal-relation) |

**These are patterns, not a word list.** Learn the operators; derive the words.

The `-mu` pattern:

```
to-mu      knowledge artifact   =   document / data store
ki-mu      motion artifact      =   vehicle
ne-mu      relation artifact    =   connector
ra-mu      power artifact       =   engine
```

The `-su` pattern:

```
to-su      knowledge system     =   organized knowledge / canon
si-su      signal structure     =   communication framework
ne-su      relation structure   =   network (as a framework)
```

Once you know a pattern, any root can fill the modifier slot. `ra-li` (power-person),
`fe-li` (one who sets limits), `wi-li` (agent of intention) — all predictable.

---

!!! question "Exercise 2 — Build `to-su`"
    An organized knowledge system. Which two roots, in which order?

    <div class="tn-learn-picker"
         data-template="___-___"
         data-answers='["to","su"]'
         data-mode="both"
         data-ok="to-su — knowledge-structure — organized knowledge system ✓"
         data-items='[{"form":"to","gloss":"knowledge"},{"form":"su","gloss":"structure / organized form"},{"form":"ki","gloss":"motion"},{"form":"ne","gloss":"relation"},{"form":"mu","gloss":"artifact"},{"form":"li","gloss":"person"}]'>
    </div>

??? success "Explanation"
    `to` (knowledge) + `su` (structure). The `su` head says: "this is the organized
    instantiation." `to-su` = knowledge as an organized system — a canon, a curriculum,
    a doctrine.

    Compare: `to-su` (the knowledge as framework) vs `to-mu` (a knowledge artifact —
    a document, a record) vs `to-li` (the person in the knowledge domain — a scholar).
    Same modifier, different operator head, systematically different meaning.

---

## Cluster 3 — Three-root compounds

Three roots follow the same rule. The last root is the head. The two to its left are
a modifier chain — and that chain is **right-branching by default**.

```
A - B - C   =   A modifies [B-C]
                             ↑
                        B-C parsed first as a unit;
                        then A attaches to that unit.
```

From the corpus:

```
(1)  to - ki - mu   →   to + [ki-mu]
                               ↑
                           motion-artifact = vehicle
                 →   knowledge + vehicle = computing device

(2)  si - su - mu   →   si + [su-mu]
                               ↑
                           structure-artifact = framework/device
                 →   signal + framework = signal-structure device (antenna array)

(3)  ra - ki - li   →   ra + [ki-li]
                               ↑
                           motion-person = traveler / mover
                 →   power + mover = one who operates powered motion (pilot)
```

You've seen (1) and (2) since Stage 1. Sentence (3) appears in C005.

**New root: `ra`** — power, force, energy. As a modifier, `ra` says "this involves
force / is powered." `ra-ki-li` = powered-motion-person = pilot. `ra-mu` = power artifact
= engine. `ra-su` = power structure = star (registered, astronomy domain).

---

!!! question "Exercise 3 — Build `to-ki-mu`"
    A computing device: knowledge + change + artifact. Three roots, in order.
    The outlined slot is active — fill them left to right.

    <div class="tn-learn-picker"
         data-template="___-___-___"
         data-answers='["to","ki","mu"]'
         data-mode="both"
         data-ok="to-ki-mu — knowledge-change-device — computer ✓"
         data-items='[{"form":"to","gloss":"knowledge"},{"form":"ki","gloss":"motion / change"},{"form":"mu","gloss":"artifact / device"},{"form":"ra","gloss":"power / force"},{"form":"su","gloss":"structure"},{"form":"li","gloss":"person"}]'>
    </div>

??? success "Explanation"
    Parse: `to` + `[ki-mu]`. First: `ki-mu` = motion-artifact = device that performs
    change. Then: `to` narrows it — a *knowledge-change* device = computing device.

    The exercise enforces the parse order physically: fill left to right, mirroring
    how the compound is semantically constructed.

---

## Cluster 4 — The `'` juncture (first look)

The default right-branching parse works for most compounds. But sometimes you need
a different grouping. The `'` marker binds a subunit explicitly.

**The rule:** `'` marks the left boundary of a pre-bound subcompound. Everything from
`'` to the end of the compound groups together first; the chain to the left of `'` then
attaches to that bound unit as a modifier.

```
A - B ' C - D     →     [A-B] modifies [C-D]
                                 ↑
                        A-B bind as a modifier unit;
                        C-D bind as the head unit.
```

A solid example, using roots you already know:

```
to-ki-li     (no marker — default right-branch)
   = to + [ki-li]
   = knowledge + [motion-person]
   = knowledge + traveler
   = one who journeys through knowledge

to-ki'li     (' after ki — juncture before li)
   = [to-ki] + li
   = [learning-process] + person
   = agent of the learning process
   = learner
```

In `to-ki'li`, the `'` sits between `ki` and `li`. This marks `li` alone as the
right-side subcompound, forcing `to-ki` to bind together as the modifier. Result:
`[to-ki]`-person = learning-process-person = learner.

In the default `to-ki-li`, `to` attaches to `[ki-li]` — the knowledge-type traveling
person.

Both are valid Tonesu. They mean different things.

`'` is unnecessary for two-root compounds — there is no ambiguity. For three or more
roots, use it when the default right-branching parse gives you the wrong meaning.

---

!!! question "Exercise 4 — Which form means *learner*?"
    The *agent of the learning process* (someone who actively does learning) is
    not the same as *one who journeys through knowledge*. Which written form
    encodes which meaning?

    Select the form that means *learner*:

    <div class="tn-learn-picker"
         data-template="___"
         data-answer="to-ki'li"
         data-mode="form"
         data-ok="Correct — to-ki'li: [to-ki] (learning-process) + li (person) ✓"
         data-nok="Look at where the ' sits — which chain does it force to bind first?"
         data-items='[{"form":"to-ki-li","gloss":"default right-branch"},{"form":"to-ki&#39;li","gloss":"juncture form"}]'>
    </div>

??? success "Explanation"
    `to-ki'li` — the `'` between `ki` and `li` forces `to-ki` to bind as a unit
    (learning-process) and then attach to `li` (person). Learning-process-person =
    learner.

    `to-ki-li` (default) — `to` attaches to `[ki-li]` = knowledge + traveling-person
    = one who travels through knowledge.

    Both valid. The `'` is required in spoken form too — it marks a slight prosodic
    boundary at that position. Stage 3 covers the juncture marker in full, including
    its interaction with longer compounds, `~` approximation, and the spoken form `peld`.

---

## Roots introduced in this stage

| Root | Core meaning | Key compounds |
|------|-------------|--------------|
| `ne` | relation / connection | `ne-mu` (connector), `si-ne` (communication), `ne-li` (one who connects) |
| `su` | structure / organized form | `to-su` (knowledge system), `su-li` (architect), `si-su-mu` (antenna array) |
| `ra` | power / force / energy | `ra-ki-li` (pilot), `ra-mu` (engine), `ra-su` (star) |

---

## Next

[Stage 3 — Grammar and notation](stage-3.md) formally introduces the particle system
(`la-`, `lo-`, `lu-`) and the notation marks together. They're learned together because
they're used together.


!!! note "In development"
    This stage is not yet written. Start with [Stage 0 — First Contact](stage-0.md)
    and return here as the curriculum develops.
