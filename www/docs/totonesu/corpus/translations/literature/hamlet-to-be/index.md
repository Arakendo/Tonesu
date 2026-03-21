---
batch_codes: [HAM]
---
# Translation Test: Hamlet — "To be, or not to be"

## Source: William Shakespeare, *Hamlet*, Act III, Scene I (~1600)
## Status: Draft — first pass

---

## Purpose

The Hamlet soliloquy opening is the **existential deliberative stress test**. Tests:
- **Nominalized bare predicate as topic** — `pa / no-pa` treated as a concept-pair and topicalized without role markers; novel use of the topic frame
- **`/` under parallel load** — both halves of the deliberative are structurally paired; tests whether the parallel partition mark can appear *inside* a topic NP before `:`
- **Agent scope across `/`** — does `la-{agent}` in the first clause of a `/` parallel scope over the second? Universal vs personal readings diverge here
- **Comparative gap exposure** — "Whether 'tis nobler" embeds a degree comparison; Tonesu has `X-fe` (superlative) but no productive comparative particle; **GAP-HAM-001**
- **Existential vs property prediction** — `pa` (presence/existence) vs `ne X` (copula/property); three-way system established at JOH-001 redeployed in secular register

Corpus sentences from this batch: **S462–S464**.

---

## Vocabulary Framework

| Form | Reading | Construction | Notes |
|------|---------|--------------|-------|
| `pa` | to be / to exist | primitive root R021: presence, spatial existence, being-located | used here as abstract concept / infinitive-equivalent, not as predicate with agent |
| `no-pa` | not to be / non-existence | `no` (negation) + `pa` (existence) = absence of existence | parallel partner to `pa` in the deliberative; written `nopa` |
| `to-si` | the question / the inquiry | `to` (knowledge/conceptual-pattern) + `si` (signal/seeking) = knowledge-seeking signal = an inquiry, a question | established; first the grammar marker, here used as a nominalised concept |
| `no-ko-ra` | external force / outrageous fortune | established NEW-001 (S450); external opposition/compulsion that acts on a body or person | here: the compulsion of fortune — what one would "suffer" against |
| `de` | decay / suffer / undergo deterioration | primitive root; used here as predicate: undergo-harm, experience-deterioration | patient `lo-no-ko-ra` = the external force experienced as harm |
| `ka-ra` | act with force / take arms | `ka` (act/do) + `ra` (energy/force) = act-forcefully; compositional, no registration required | the action-alternative to passive endurance |
| `de-no-fe` | unlimited adversity / a sea of troubles | `de` (decay/harm) + `no-fe` (without limit) = harm without limiting bound = unbounded adversity | productive application of `[X]-no-fe` extremal suffix; first attested S464 |

### ~~The comparative gap~~ (GAP-HAM-001 — Resolved)

**Resolved.** `nu-be` / `nu-no` are the established comparative particles (grammar.md §Comparison; corpus S039, S064–S067):

```
lo-A  {quality}  nu-be  lo-B   →  A has more {quality} than B
lo-A  {quality}  nu-no  lo-B   →  A has less {quality} than B
```

"Whether 'tis nobler" = `lo-{X}  vo  nu-be  lo-{Y}` = X has more worth than Y. A comparative rendering of S464 would be: `de lo-no-ko-ra vo nu-be ka-ra lo-de-no-fe : ne to-si` (whether endurance has more worth than taking arms is the question). The gap was logged in error; these particles predate this batch.

S462–S464 chose the deliberative-binary reading (`X / Y : ne to-si` = "is {X or Y} the question?") over the comparative-ranking reading — both are valid translations of the soliloquy opening. The deliberative is arguably more faithful: Hamlet is not computing "which is nobler" but asking whether the question of valuing them is even the right frame. The binary translation stands on its own merits.

### Agent scope across `/` (GAP-HAM-002)

The sentence `la-mi pa / no-pa : ne to-si` is ambiguous: does `la-mi` scope over `no-pa` as well as `pa`?

- **If agent scopes**: `la-mi pa / no-pa` = "[for me,] both existence and non-existence" — one agent governing the full parallel; more economical.
- **If agent does not scope**: `la-mi pa / no-pa` = "me-existing / [generic] non-existence" — the second clause is agentless, shifting to the universal.

S463 resolves this conservatively by repeating `la-mi` on both clauses. **GAP-HAM-002 — Resolved.** Grammar §Ellipsis Pattern 3 (context drop) licenses omission of any argument when it is fully recoverable from discourse context. In a topic-frame construction `{A / B} : {comment}`, the agent is context-recoverable across both branches of `/`; a single `la-mi` on the first clause is grammatically sufficient. The double-agent form in S463 is still the clearer translation; both are valid.

### `pa` as abstract concept-topic

`pa` is a root predicate: `la-X pa` = X is present / X exists. In S462, `pa` stands alone without an agent as a topicalized concept — "existence" as an abstract, as in "to be." This is the stative-to-nominal drift licensed by topic-frame nominalization: the topic frame `:` topicalizes `pa` as *the concept of existing*, not as a predicated state.

Tonesu does not have a formal infinitive marker; the topic frame effectively nominalizes predicates by presenting them as objects of discourse. `pa / no-pa :` = "as for the existence/non-existence binary..." This is first explicitly tested here. **Note:** the topic NP retains its role marker "where it carries one" — `pa` and `no-pa` as abstract concepts carry no role markers, and none is added.

---

## Source Text

> **To be, or not to be, that is the question:**
> **Whether 'tis nobler in the mind to suffer**
> **The slings and arrows of outrageous fortune,**
> **Or to take arms against a sea of troubles...**

---

## Verse-by-Verse Analysis

### S462 — "To be, or not to be, that is the question." — universal reading (HAM-001-A)

```
pa / no-pa : ne to-si
```

**Written:** `pa / nopa : ne tosi`

The most philosophically rich rendering: `pa / no-pa` states the binary as an abstract concept-pair — existence and its negation — without anchoring it to any particular agent. This is the universal reading: the question is not merely Hamlet's personal dilemma but the general question of existence vs non-existence as a category.

Topic frame `:` topicalizes the binary: "as for [to-be / not-to-be]..." — and the comment `ne to-si` makes the copula claim: this binary *is* the question / the inquiry. `to-si` = knowledge-seeking signal = a question as a concept; the compound `ne to-si` attributes "question-ness" to the topicalized binary.

**Structural note:** this is the first corpus use of `/` inside a topic NP — the structure is `{A / B} : {comment}` where the topic itself is a parallel pair. The topic frame boundary is unambiguous: `:` closes the topic regardless of the internal structure. No parse conflict.

### S463 — "To be, or not to be, that is the question." — personal reading (HAM-001-B)

```
la-mi pa / la-mi no-pa : ne to-si
```

**Written:** `lami pa / lami nopa : ne tosi`

The first-person reading: Hamlet asks specifically about *his own* existence. `la-mi` is explicitly repeated on both clauses to avoid GAP-HAM-002 ambiguity. This is the conservative parsing: each side of the `/` parallel carries its own agent.

Compare S462: the universal reading needs no agent. S463 is more intimate — the soliloquy register, not the philosophical register. Both are valid translations of the same source line; the difference is register and interpretive emphasis.

**Note on `la-mi pa / no-pa` (with agent on first clause only):** this form is grammatical under Grammar §Ellipsis Pattern 3 — `la-mi` is context-recoverable across `/`. It is not used here because the double-agent form is the clearer translation; both are valid.

### S464 — "Whether 'tis nobler... to suffer the slings and arrows... or to take arms against a sea of troubles" (HAM-001-C)

```
de lo-no-ko-ra / ka-ra lo-de-no-fe : ne to-si
```

**Written:** `de lonokora / kara lodenofe : ne tosi`

The second deliberative parallel: the two options Hamlet weighs.

- `de lo-no-ko-ra` = suffer/experience-deterioration [patient: external force/compulsion] = "to suffer the slings and arrows of outrageous fortune." `de` (decay/undergo-harm) takes `lo-no-ko-ra` as its experiential patient — the external compulsion is the thing suffered. `no-ko-ra` established at NEW-001 (Newtonian external force); redeployed here in the register of fortune's hostile agency.

- `ka-ra lo-de-no-fe` = act-forcefully [patient: unlimited adversity] = "to take arms against a sea of troubles." `ka-ra` = act + force = to take vigorous action. `lo-de-no-fe` = patient: harm-without-limit = unbounded adversity = "a sea of troubles." `de-no-fe` follows the productive `[X]-no-fe` pattern: harm without any limiting boundary = the maximum of adversity — "sea of troubles" is not a quantity claim (so not `X-fe` = extremal) but a boundlessness claim (hence `X-no-fe`).

**The "nobler" frame** is expressible: `lo-{X}  vo  nu-be  lo-{Y}` (X has more worth than Y; `nu-be` established grammar §Comparison, S039–S067). S464 chose the deliberative-binary reading over the comparative-ranking reading — both are valid; the binary is arguably more faithful to the soliloquy's rhetorical form, which poses a question rather than a verdict.

---

## HAM-001 Batch Summary

| Entry | Form | Test |
|-------|------|------|
| S462 (HAM-001-A) | `pa / nopa : ne tosi` | bare-predicate pair topicalized; `/` inside topic NP; universal register |
| S463 (HAM-001-B) | `lami pa / lami nopa : ne tosi` | agent-explicit personal reading; GAP-HAM-002 (agent ellipsis across `/`) |
| S464 (HAM-001-C) | `de lonokora / kara lodenofe : ne tosi` | action/endurance binary; `de-no-fe` new; GAP-HAM-001 (comparative) |

**Key finding:** "To be, or not to be" translates elegantly in two moves: `pa / no-pa` (the primitive root for existence, paralleled with its negation) and `:` (the topic frame, nominalizing the pair). Tonesu is precise where Shakespeare is deliberately ambiguous: the personal vs universal reading must be *chosen* (S462 vs S463), and the comparative judgment "nobler" must wait for a comparative construction. The deliberative *form* (binary parallel + topic assertion) is fully expressible; the evaluative *rank* (which option is worthier) is not yet.

**New vocabulary introduced:**
- `de-no-fe` (unlimited adversity; `de` = harm + `[X]-no-fe` extremal pattern; first attested S464)

**Open questions logged:**
- ~~**GAP-HAM-001**~~ **Resolved (March 2026):** `nu-be` / `nu-no` are the comparative particles (grammar.md §Comparison; S039, S064–S067). "Nobler than" = `lo-{X} vo nu-be lo-{Y}`. Logged in error; construction predates this batch.
- ~~**GAP-HAM-002**~~ **Resolved (March 2026):** Grammar §Ellipsis Pattern 3 (context drop) licenses agent omission when fully recoverable from discourse context. In a topic-frame `{A / B} : {comment}`, agent is recoverable across both branches of `/`.
