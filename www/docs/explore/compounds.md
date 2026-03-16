# Building Compounds

The best way to understand Tonesu is to watch a word get built. Each example below starts from a concept, works through the root selection, and arrives at a compound — showing why that particular structure was chosen.

---

## Example 1: scholar

**Concept:** a person whose defining role is knowledge

**Available roots:**
- `to` — conceptual pattern, knowledge, thought
- `li` — social agent, person

**Structure:** `to + li` — a person characterised by knowledge

```
to-li  →  knower, scholar
```

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
```
to-ki       =  knowledge + change  →  the process of transforming knowledge
to-ki-mu    =  to-ki + device      →  a device that performs to-ki
            →  computer, calculator
```

Derivational suffix `-mu` (device) attaches after the semantic core. Stacking order: **root → semantic modifier → role suffix**.

---

## Example 3: engine

**Concept:** a device that converts energy into motion

**Available roots:**
- `ra` — energy, force
- `ki` — motion, change
- `mu` — device

```
ra-ki-mu   =  ra (energy) + ki (change) + mu (device)
           →  energy-change device  =  engine, motor, generator
```

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
```
pa-wi-ka-su   →  right-branching: pa modifies {wi modifies {ka-su}}
              →  place of will modifying structured-action
```

That reads as: *a place-of-will organized-action-structure*. Close, but `pa-wi` (destination place) is a unit — we want `[pa-wi]` (the destination) to be the head that `[ka-su]` (structured practice) describes.

**With `'`:**
```
pa-wi'ka-su   =  [pa-wi] + [ka-su]
              →  destination-place  of  structured-intentional-practice
              =  shrine, temple
```

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
```
de-su   =  decay + structure  →  fault, moral failing (a degradation of order)
```

**Then adding deliberate removal:**
```
ka-no-de-su   =  ka (deliberate) + no (removal) + de-su (fault)
              →  deliberate un-faulting  =  forgiveness
```

Left-to-right: `ka` marks the act as intentional; `no` negates/removes; `de-su` is what gets removed. The full compound is compositionally transparent — a reader who knows the roots can arrive at the meaning without a dictionary.

---

## What makes a good compound?

**Root economy** — use the minimum roots that achieve the target meaning without ambiguity.

**Head clarity** — the rightmost root should be the strongest semantic anchor for the class of thing being named.

**Operator consistency** — if you use `no-`, `ka-`, or `re-` as a left-slot modifier, it applies to everything to its right. Make sure that scope is intentional.

**Stability across contexts** — a good compound reads the same way whether it appears alone or embedded in a longer sentence.

When a compound needs restructuring to be clear, the first tool is `'`. If `'` alone is insufficient, the concept probably wants to be a multi-word phrase rather than a single compound.
