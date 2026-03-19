# Building Compounds

The best way to understand Tonesu is to watch a word get built. Each example below starts from a concept, works through the root selection, and arrives at a compound — showing why that particular structure was chosen.

---

## Example 1: scholar

**Concept:** a person whose defining role is knowledge

**Available roots:**
- `to` — conceptual pattern, knowledge, thought
- `li` — social agent, person

**Structure:** `to + li` — a person characterised by knowledge

<div class="tn-derive" markdown>

`to-li` → knower, scholar

</div>

Head-final rule: `li` (person) is the head; `to` narrows it to the knowledge domain.
Nothing wasted, nothing ambiguous.

---

## Example 2: computer

**Concept:** a device that processes knowledge

**Available roots:**
- `to` — knowledge, conceptual pattern
- `ki` — change, process, motion
- `mu` — device, artifact

**Building up:**

<div class="tn-derive" markdown>

`to-ki` = knowledge + change → the process of transforming knowledge

`to-ki-mu` = `to-ki` + device → a device that performs `to-ki` → **computer, calculator**

</div>

Derivational suffix `-mu` (device) attaches after the semantic core. Stacking order: **root → semantic modifier → role suffix**.

---

## Example 3: engine

**Concept:** a device that converts energy into motion

**Available roots:**
- `ra` — energy, force
- `ki` — motion, change
- `mu` — device

<div class="tn-derive" markdown>

`ra-ki-mu` = `ra` (energy) + `ki` (change) + `mu` (device) → energy-change device → **engine, motor, generator**

</div>

The same pattern as `to-ki-mu` — semantic core first, role suffix last. The head tells you what kind of thing it is; the left roots tell you what domain it operates in.

---

## Example 4: shrine / temple

**Concept:** a place defined by structured intentional practice — rituals, acts of will, organized form

**Available roots:**
- `pa` — place, space
- `wi` — will, intention, goal
- `ka` — intentional action
- `su` — structure, organized form

**First pass:**

<div class="tn-derive" markdown>

`pa-wi-ka-su` → right-branching: `pa` modifies {`wi` modifies {`ka-su`}} → place of will modifying structured-action

</div>

That reads as: *a place-of-will organized-action-structure*. Close, but `pa-wi` (destination place) is a unit — we want `[pa-wi]` (the destination) to be the head that `[ka-su]` (structured practice) describes.

**With `'`:**

<div class="tn-derive" markdown>

`pa-wi'ka-su` = `[pa-wi]` + `[ka-su]` → destination-place of structured-intentional-practice → **shrine, temple**

</div>

The apostrophe binds `pa-wi` first, then the full compound combines. This is a case where `'` is required for the intended reading, not merely helpful — without it the parse lands in the wrong place.

---

## Example 5: deliberate removal of fault (forgiveness)

**Concept:** the intentional act of cancelling out a moral failing

**Available roots:**
- `ka` — intentional action
- `no` — negation, removal, absence
- `de` — decay, decrease, breakdown
- `su` — structure, organized system

**Building the fault first:**

<div class="tn-derive" markdown>

`de-su` = decay + structure → fault, moral failing (a degradation of order)

</div>

**Then adding deliberate removal:**

<div class="tn-derive" markdown>

`ka-no-de-su` = `ka` (deliberate) + `no` (removal) + `de-su` (fault) → deliberate un-faulting → **forgiveness**

</div>

Left-to-right: `ka` marks the act as intentional; `no` negates/removes; `de-su` is what gets removed. The full compound is compositionally transparent — a reader who knows the roots can arrive at the meaning without a dictionary.

---

## What makes a good compound?

**Root economy** — use the minimum roots that achieve the target meaning without ambiguity.

**Head clarity** — the rightmost root should be the strongest semantic anchor for the class of thing being named.

**Operator consistency** — if you use `no-`, `ka-`, or `re-` as a left-slot modifier, it applies to everything to its right. Make sure that scope is intentional.

**Stability across contexts** — a good compound reads the same way whether it appears alone or embedded in a longer sentence.

When a compound needs restructuring to be clear, the first tool is `'`. If `'` alone is insufficient, the concept probably wants to be a multi-word phrase rather than a single compound.

For the full rules on right-branching, `'` juncture, and derivational suffixes, see [Building words](../tonesu/words.md).

---

## Sentence walkthroughs

The worked examples above show how individual words are built. The walkthroughs below show the grammar working in full sentences — parse breakdowns that reveal how slots, particles, and compounds interact.

For the complete corpus (575+ sentences), see the [Corpus](../tonesu/corpus/overview.md).

---

### S001 — Basic agent-action-patient

```
la-li  ka-be  lo-mu
```
*The person builds the object.*

| Element | Parse |
|---------|-------|
| `la-li` | agent: person |
| `ka-be` | action: growth/construction |
| `lo-mu` | patient: artifact |

---

### S017 — Purpose clause

```
la-ze  lo-si  ka-sikipast  wi [ka-fesi  ne-yu]
```
*She sent the message to warn them.*

| Element | Parse |
|---------|-------|
| `la-ze` | agent: she / they (3rd person) |
| `lo-si` | patient: the signal / message |
| `ka-sikipast` | action: transmitted (past) — `si-ki` = signal-motion |
| `wi [...]` | purpose frame: in order to... |
| `ka-fesi  ne-yu` | warn (`fe-si` = boundary-signal) them |

The `wi` frame introduces a purpose clause. The `[...]` brackets are an aside — they could be omitted and the core sentence would still be grammatical.

---

### S018 — Studying to comprehend

```
la-yu  ka-to-ki  wi [ka-to-su-ki]
```
*They study in order to comprehend.*

- `to-ki` = knowledge-change = the process of reasoning, studying
- `to-su-ki` = entering a state of organised knowledge = comprehension (the threshold moment)
- The distinction: `to-ki` is the ongoing activity; `to-su-ki` is the moment it crosses into understanding

---

### S033 — Contingent state

```
lo-pa  ha-vo
```
*The room is warm.*

`lo-` places `pa` (room) in the patient slot — a contingent current state. The room *is warm right now*; it could cool down. Compare with the intrinsic property form:

```
la-pa  ha-vo
```
*The room has warmth as a property.* (structural — built to be warm)

Same words, different claim. See [Grammar](../tonesu/grammar.md) for the full `la-X` / `lo-X` distinction.
