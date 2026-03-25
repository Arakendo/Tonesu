# Stage 0 — First Contact

Not the formal system — what the language *does*.

---

## Three sentences

Here are three real sentences from the Tonesu corpus. Not invented — actual
sentences from recorded exchanges. Read them over. See what you can work out
before reading on.

```
(1)   lo-mu  de
      The unit is damaged.

(2)   la-mi  ki  pa-li-pu  ta-ti-be
      I'm going to the city.

(3)   to-si  —  la-tu  ki  pa-li-pu  ta-ti-be
      Are you going to the city soon?
```

*What do you notice? What's similar across these sentences? What changed between (2) and (3)?*

---

## What's happening

### `lo-` and `la-`

These two prefixes are the most fundamental signals in Tonesu.

**`lo-`** marks *what is being described or affected* — the patient.

**`la-`** marks *who acts* — the agent.

In sentence (1), only `lo-` appears. The unit (`mu`) is in a state of decay (`de`). No
actor — just a thing and its condition. This is how Tonesu describes states: put the
patient first with `lo-`, then state what's true of it.

Sentence (2) introduces `la-mi`: `la-` (agent marker) + `mi` (I, the speaker). Now there
is an actor. That actor moves — `ki` means motion, going somewhere. The destination is
`pa-li-pu`: `pa-` (place marker) + `li-pu` (city, literally: people-established). When:
`ta-ti-be` — at the upcoming time, soon.

Sentence (3) is identical to (2), except:

- `la-mi` (I) has become `la-tu` (you — `tu` is the second-person root)
- `to-si —` has been placed in front

`to-si` is a knowledge-seeking signal — knowledge (`to`) + signal (`si`). It turns a
statement into a question by marking the whole proposition as "information I'm seeking."
The `—` marks the pause before the proposition follows.

### Word order

The core frame is:

```
la-[agent]   [verb]   lo-[patient]
```

In sentences (2) and (3), there is no `lo-` patient — the motion has a destination
(`pa-li-pu`), not a thing being acted on. Both patterns are normal.

Time and place markers (`ta-`, `pa-`) float freely. They can appear anywhere in the
sentence; their role is always clear from the prefix.

---

## Roots introduced

Eight roots carry most of the meaning in these sentences. These are the building
blocks of Tonesu vocabulary.

| Root | Core meaning | Where it appears |
|------|-------------|-----------------|
| `mu` | artifact, device | `lo-mu` — the unit (a made thing) |
| `de` | decay, damage, break | predicate in (1): "is damaged" |
| `mi` | I, the speaker | `la-mi` — I as the acting agent |
| `tu` | you, the addressee | `la-tu` — you as the acting agent |
| `ki` | motion, movement | verb in (2) and (3): "go" |
| `li` | person, people | in `li-pu` — city (people-established) |
| `be` | grow, approach, emerge | in `ti-be` — the approaching time |
| `to` | knowledge, thought, pattern | in `to-si` — inquiry / question marker |

**Structural markers** — not vocabulary roots, but present in every sentence:

| Marker | Role |
|--------|------|
| `la-` | marks the agent (who acts) |
| `lo-` | marks the patient (what is described or acted on) |
| `pa-` | marks place |
| `ta-` | marks time |

**In ordinary writing**, hyphens are dropped: `lomu`, `lami`, `palipu`. The
hyphenated form you see above is the *analytic notation* — it shows the morpheme
boundaries explicitly. Both forms are used in this section: analytic for learning,
solid for natural reading.

---

## Two exercises

!!! question "Exercise 1 — Fill in the blank"
    What root completes this compound?

    The result should mean: *a signal that seeks knowledge* — a question.

    <div class="tn-learn-picker"
         data-template="___-si"
         data-answer="to"
         data-mode="both"
         data-items='[{"form":"to","gloss":"knowledge"},{"form":"ki","gloss":"motion"},{"form":"mu","gloss":"artifact"},{"form":"de","gloss":"decay"}]'>
    </div>

??? success "Answer"
    `to-si` — knowledge (`to`) + signal (`si`).

    `to` characterizes the signal: it's knowledge-seeking. Head-final rule: `si`
    (signal) is the head; `to` describes what kind. In sentence (3), `to-si —` is
    placed before the full proposition. It marks the whole thing as "information I'm
    seeking." Result: a question.

---

!!! question "Exercise 2 — Fill in the blank"
    Sentence (2) says *I'm going to the city*. Fill in the blank to say *you're going
    to the city*:

    <div class="tn-learn-picker"
         data-template="la-___  ki  pa-li-pu  ta-ti-be"
         data-answer="tu"
         data-mode="both"
         data-items='[{"form":"mi","gloss":"I / speaker"},{"form":"tu","gloss":"you / addressee"},{"form":"ze","gloss":"third person"},{"form":"li","gloss":"person"}]'>
    </div>

??? success "Answer"
    `la-tu` — the second-person root is `tu`.

    ```
    la-tu  ki  pa-li-pu  ta-ti-be
    ```

    Tonesu has no conjugation. Who acts is encoded by swapping the root after `la-`.
    Everything else stays the same.

---

## Reference

When you're ready to go deeper into what you've just seen:

- [Quick start](../quick-start.md) — the full language at a glance
- [Primitives](../tonesu/primitives.md) — all CV roots with meanings and usage
- [Grammar](../tonesu/grammar.md) — the `la-` / `lo-` / `lu-` system in full

---

## Next

[Stage 1 — Roots in context](stage-1.md) introduces more roots through sentences,
in clusters of 3–6. Vocabulary is built through use, not memorization.
