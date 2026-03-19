# Patterns and Quick Reference

A **pattern** in Tonesu is a productive rule for interpreting or building compounds. Once you learn the patterns, you can understand and construct unfamiliar words from their parts — no dictionary lookup required.

---

## Quick Reference: The Core Rules

These four rules generate almost all Tonesu vocabulary.

### Rule 1: Head-Final Order (Modifier Precedes Head)

The rightmost element is always the **head** — the primary conceptual unit. Everything to its left **modifies** it.

```
{modifier(s)} + {head}
```

**Reading left-to-right narrows the concept:**

```
knowledge + structure        →  to-su      organized knowledge
knowledge + structure + device →  to-su-mu   knowledge system / computer
red + organism               →  ker-zo     red animal
```

### Rule 2: Derivational Suffixes Transform Roles

Short suffixes shift a root into a different grammatical role. They are **stackable, but only one per lexical unit** before compounding.

| Suffix | Transformation | Example |
|--------|---|---|
| `-li` | verb → agent ("one who...") | `build-li` → builder |
| `-mu` | verb → device ("tool for...") | `build-mu` → building tool |
| `-pa` | verb → location ("place of...") | `build-pa` → construction site |
| `-su` | verb → result ("what is...") | `build-su` → structure |
| `-to` | any → abstract concept | `build-to` → the concept of building |
| `-ge` | any → property ("having quality of...") | `energy-ge` → energetic |
| `-ki` | (state root) → entry ("to become...") | `alive-ki` → come to life |

### Rule 3: Semantic Operators Predict Compound Meaning

When a root appears as the **head** (rightmost element), it functions as a **semantic operator** — it transforms the modifier's meaning in a predictable way across all compounds using that head.

| Head | What it means | Example | Gloss |
|------|---|---|---|
| `su` | "structured X" / system of X | `to-su` | knowledge system |
| `ki` | "X in motion/process" / activation of X | `to-ki` | learning (knowledge in process) |
| `fe` | "boundary/limit of X" | `to-fe` | epistemic threshold |
| `li` | "agent of X" / one whose domain is X | `to-li` | scholar |
| `mu` | "device/instrument for X" | `to-mu` | knowledge tool |
| `ne` | "relation/link of X" | `si-ne` | communication (signal-relation) |
| `be` | "growth/emergence of X" | `fa-be` | affect rising |
| `de` | "decay/dissolution of X" | `fa-de` | affect fading |
| `re` | "recurring X" / habitual/cyclic X | `ti-re` | daily cycle |
| `zi` | "mutual/coupled X" / bilateral X | `wi-zi-ka` | negotiation |
| `ge` | "property of X" / characterized by X | `ra-ge` | energetic |
| `pa` | "place/location where X" | `zo-pa` | habitat |

**Algebraic reading:** Once you learn that `-su` means "system of," `X-su` always means a structured framework of X. Apply this rule to **any** root — it works predictably. Same for all other heads.

### Rule 4: The Apostrophe Re-scopes Compounds

**Default:** compounds parse right-branching (the last element is the head, and the parse accumulates left-to-right).

```
A-B-C-D  →  A modifies {B modifies {C modifies D}}
```

**Problem:** at depth ≥3, ambiguity can arise. A modifier that should apply to a whole multi-root unit instead attaches only to the terminal element.

**Solution:** `'` marks the left boundary of a subcompound. The modifier to the left of `'` then applies to the whole subunit.

```
A'B-C-D   →  A modifies {B-C-D as pre-bound unit}
```

**Usage:**
- Omit for 2-3 root compounds where parse is clear
- Required when a CVC color/digit precedes a multi-root noun: `ker'zo-se-so` (red cat, not just the tail)
- Used with visual patterns: `lu-di mu` (striped object) vs. `lu-di'zo-se-so-fe` (striped cat)

```
red + (living-perception-sensory-classification)  →  ker'zo-se-so-fe  (red cat)
no-light + (light-part + living-perception-sensory-classification)  →  no-lu'lu-pe'zo-se-so-fe  (dark-spotted big cat)
```

---

## Semantic Operators: The Generator Table

These tables show how to construct and predict the meaning of any compound using the **head** (rightmost element) as the key.

### State-Modification Heads

These heads take any modifier and produce a verb-like meaning describing what happens to the modified concept.

| Head | Pattern | Meaning | Examples |
|------|---------|---------|----------|
| `ki` | X-ki | X enters into motion/process; begins/transitions | `ne-ki` (connect), `be-ki` (begin growing), `zo-ki` (come alive) |
| `be` | X-be | X grows / emerges / increases | `fa-be` (affect grows: happiness), `zo-be` (organism grows) |
| `de` | X-de | X decays / dissolves / decreases | `fa-de` (affect fades: sadness), `zo-de` (organism dies) |
| `re` | X-re | X recurs / repeats / cycles | `ti-re` (time cycles: daily/yearly), `ka-re` (action repeats: habit) |

**Pattern:** State heads + any modifier = inchoative or telic verb.

### Structure-Definition Heads

These heads take any modifier and produce a noun describing what **kind of structure or system** the modifier belongs to.

| Head | Pattern | Meaning | Examples |
|------|---------|---------|----------|
| `su` | X-su | organized system / structured framework of X | `to-su` (knowledge system), `zo-su` (biological structure), `li-su` (social order) |
| `fe` | X-fe | boundary / limit / threshold of X; what separates it from not-X | `to-fe` (epistemic threshold — what counts as knowledge), `no-fe` (no-boundary: infinite), `pa-fe` (territorial boundary) |

**Pattern:** Structure heads + any modifier = noun describing how X is organized or delimited.

### Agent / Role Heads

These heads take any modifier and produce a noun describing a **person or entity whose role or domain is the modifier**.

| Head | Pattern | Meaning | Examples |
|------|---------|---------|----------|
| `li` | X-li | agent / person of X; one whose domain is X | `to-li` (scholar), `ka-li` (actor), `zo-li` (biologist) |
| `mu` | X-mu | device / instrument / artifact that does X or is of X | `to-mu` (knowledge device: computer), `ka-mu` (action tool), `zo-mu` (organism artifact: ?)  |

**Pattern:** Agent/device heads + any modifier = noun describing a person or tool in that domain.

### Relation Heads

| Head | Pattern | Meaning | Examples |
|------|---------|---------|----------|
| `ne` | X-ne | relation / link / connection of X; relational aspect of X | `si-ne` (communication: signal-relation), `zo-ne` (kinship: organism-relation) |
| `zi` | X-zi | mutual / coupled / bilateral X | `wi-zi-ka` (negotiation: will-coupled-action), `zo-zi` (animal family: organism-coupled) |

**Pattern:** Relation heads + any modifier = noun describing how X connects or couples with other things.

### Property Heads

| Head | Pattern | Meaning | Examples |
|------|---------|---------|----------|
| `ge` | X-ge | quality / property of X; the feature or appearance characterized by X | `ra-ge` (energetic property), `zo-ge` (living quality), `fe-ge` (bounded quality: distinctness) |
| `pa` | X-pa | location / place / habitat where X occurs or exists | `zo-pa` (animal habitat), `ka-pa` (action location: theater), `su-pa` (structural place: architecture) |

**Pattern:** Property heads + any modifier = adjective or location noun describing where/how X appears.

---

## Derivational Suffixes: Pattern Reference

One suffix per root; no stacking multiple role-markers. If you need more than one transformation, restructure as a compound.

### Agent Derivation (`-li`)

```
Meaning: one who does {root}

ka-li          → actor / doer / performer
to-li          → scholar / knowledge expert
su-li          → architect / structure expert
zo-li          → biologist / life expert
ne-li          → diplomat / relation expert
```

### Device Derivation (`-mu`)

```
Meaning: device / instrument for {root}

ka-mu          → tool / instrument for action
to-mu          → information device / computer
ka-ki-mu       → processing device
zo-mu          → living organism tool (rare)
```

### Location Derivation (`-pa`)

```
Meaning: location / place / site of {root}

ka-pa          → stage / arena / action location
zo-pa          → habitat / ecosystem
to-pa          → library / knowledge location
ne-pa          → meeting place / diplomatic venue
```

### Result/Product Derivation (`-su`)

```
Meaning: result / product / state resulting from {root}

ka-su          → product / artifact of action
to-su          → system / structured whole
zo-su          → organism / living body
be-su          → creation / what grows
```

### Abstract Nominalization (`-to`)

```
Meaning: the abstract concept / category of {root}

ka-to          → action (as abstract concept)
zo-to          → life (as abstract concept)
ne-to          → relation (schema of how things relate)
su-to          → structure (the abstract principle)
```

### Quality/Property (`-ge`)

```
Meaning: having the quality / property of {root}

ra-ge          → energetic (having energy quality)
fe-ge          → bounded / distinct (having boundary quality)
lu-ge          → luminous / bright (having light quality)
no-ge          → absent / null (having absence quality)
```

### Inchoative: Entry into State (`{state} + -ki`)

Attach to **state roots only** — not to action roots. Produces "enter the state" or "become."

```
Meaning: to enter / transition into the state of {root}

ne-ki          → connect / become related
zo-ki          → come alive / become animate
su-ki          → organize / take form
ko-ki          → enter (= enter-interior)
be-ki          → begin to grow
```

---

## Negation and Modification Patterns

### Negation Prefix (`no-`)

`no-` is a compositional prefix meaning "absence / negation of [root]."

```
no-fe          → unbounded / without boundary (infinite)
no-ha          → cold (absence of heat)
no-lu          → dark (absence of light)
no-se          → imperceptible (cannot perceive)
no-zo          → inanimate / not alive
```

### Intensification Pattern (`X-ge`)

Properties can be intensified or modified using `vo` (value/quality) derivatives:

```
{property}-ge           → the base quality
{property}-ge vo-be     → bright / intensified version
{property}-ge vo-de     → dim / faint version
```

```
ker-ge vo-be           → bright red
pom-ge vo-de           → dark blue
```

### Negation of Properties

```
no-{property}          → lacks the property / inverse property

no-ka-ge               → passive (lacks action-quality)
no-to-ge               → irrational (lacks knowledge-quality)
```

---

## Scope Prefixes: Quick Pattern

The five bare-vowel prefixes adjust the **reference mode** of a word. They appear at word-initial position only.

| Prefix | Effect | Examples |
|--------|--------|----------|
| `a-` | abstract / universal | `a-to` (knowing-in-general), `a-toli` (sage — one schooled in abstract knowledge) |
| `i-` | particular / specific | `i-to` (this specific fact), `i-toli` (this scholar) |
| `u-` | interior / foundational | `u-to` (tacit knowing), `u-su` (deep structure / base architecture) |
| `o-` | collective / group-as-unit | `o-li` (community as single entity) |
| `e-` | emergent / transitional | `e-ki` (progressive change), `e-zo` (newly alive) |

**Usage:** Generally **not** registered as separate entries — they are live scope-modifiers readable from context. Registered only if the scope-shifted meaning cannot be paraphrased by existing compounds AND has ≥3 corpus attestations.

**Hazard:** `la-a-X` (agent + abstract scope) collapses to `la-X` in fast speech. Use abstract scope in patient/predicate position instead.

---

## Sentence Patterns

### Basic Transitive Clause

```
la-{agent}  lo-{object}  ka-{verb}
```

```
la-scholar  lo-knowledge  ka-increase
The scholar increases knowledge.
```

### Three-Role Pattern

```
la-{agent}  lo-{patient}  {action}  pa-{location}  ta-{time}
```

Particles appear in order: agent (`la-`), patient (`lo-`), location (`pa-`), time (`ta-`), etc. Omit particles for roles that are not relevant.

### Causal Frame (`go`)

```
{cause}  go  {effect}
```

```
heat  go  water-evaporate           The heat causes water to evaporate.
will  go  action                    Intention leads to action.
```

### Purpose Frame (`wi`)

```
{agent}  wi  {goal}  {action achieved}
```

```
la-architect  wi  su-be-ki  la-architect  ka-design
The architect, with the goal of creating structure, designs.
```

### Negation Clause (`no`)

```
no  {clause}
```

```
no  la-scholar  ka-understand       The scholar does not understand.
```

### Relative Clause

Headless relative: use role-marker scoping.

```
lo-{predicate}  {property}
```

The patient marker (`lo-`) scopes over the following property as a complete relative clause.

---

## Common Compound Types by Domain

### Knowledge / Investigation

```
to-li              scholar / researcher
to-mu              knowledge device / computer
to-ki              learning / thought process
to-su              knowledge system / organized information
to-fe              epistemic threshold / what counts as knowing
a-to-li            sage / one versed in abstract knowing
```

### Action / Agency

```
ka-li              actor / agent
ka-su              product / result of action
ka-mu              tool / instrument
ka-pa              stage / site of action
ka-re              habit / recurring action
ka-de              destruction (deliberate)
ka-ki              performance / act in progress
```

### Living Things

```
zo-li              biologist / life expert
zo-su              organism / biological structure
zo-pa              habitat / ecosystem
zo-ki              to come alive
zo-se              sense perception by organism
zo-zo              living collective
o-zo               organism as group; ecosystem
```

### Structure / Organization

```
su-li              organizer / architect
su-mu              structural tool / blueprint
su-ki              organization / taking form
u-su               deep structure / foundation
fe-su              boundary of structure / wall
to-su              knowledge organization / system
```

### Signal / Communication

```
si-ne              communication / signal-relation
si-li              communicator
si-mu              communication device
si-to              signal as model / representation
si-ki              signaling / transmission in process
```

---

## Quick Decision Trees

### "How do I say [concept]?"

**Step 1: Are the parts clear?**
- If yes, compose them left-to-right using head-final rule.
- If no, continue.

**Step 2: Is there a single primitive that expresses the core?**
- If yes, use that root.
- If no, continue.

**Step 3: Can I express it as [modifier] + [operator head]?**
- Look at the Semantic Operators table above.
- Find the operator head that best describes the relationship.
- Compose: `{modifier}-{operator-head}`.
- If yes, use that compound.
- If no, continue.

**Step 4: Do I need to show a relationship or transformation?**
- Negation? Use `no-{root}` prefix.
- Agent? Use `{root}-li` suffix.
- Device? Use `{root}-mu` suffix.
- Result? Use `{root}-su` suffix.
- Location? Use `{root}-pa` suffix.
- Property? Use `{root}-ge` suffix.
- Abstract concept? Use `{root}-to` suffix.
- Entering a state? Use `{state}-ki`.

**Step 5: Multiple modifications?**
- Restructure as a multi-root compound using head-final order.
- Stack modifiers left-of-head, not one after another on the root.

**Example decision path for "burning building":**

```
1. Core parts: ka (action) + de (decay) + su (structure) = ka-de-su? No, that's not it.
2. Better: cause of {structure-decay/destruction} = {cause}-de-su? 
3. Cause is heat: ha-de-su? Not quite — that's heat-decay-structure, missing the agency.
4. Better: structured decay via heat = su-ki-de with heat modifier...
5. Or: fire (which is heat-in-action) destroying structure = ha-ka-de-su? 
6. Built: ha (heat) + ka (action, "heat-action"=fire) + de + su = ha-ka-de-su.
7. Check head-final: de-su is the object (decaying structure), ha-ka modifies it (heat-action = fire modifying decaying-structure). Correct.
```

---

## The Three Reading Stages

Every compound can be read three ways, in priority order:

### Stage 1: Compositional Reading (Always valid)

Construct from the component primitives using head and operator rules.

```
to-fe-su-ki   →   knowledge + boundary + structure + motion
           =   motion of the structural boundary of knowledge
           ≈   paradigm shift / epistemic revolution
```

**Algebraic reading:** read the terminals, then work backward:
- Head: `ki` (motion/transition) 
- Before it: `su` (structure/system) — so `su-ki` = the structure enters motion = transformation
- Before it: `fe` (boundary/limit) — so `fe-su-ki` = the boundary's transformation
- Before it: `to` (knowledge/pattern) — so `to-fe-su-ki` = transformation of the boundary of knowledge

### Stage 2: Algebraic Pattern Reading (Standard)

Apply the operator patterns: recognize how the head transforms the meaning.

```
to-fe-su-ki  →  "fe" in position 2 from right = boundary of X:  X = knowledge-structure-motion-pattern
            →  "boundary of a structure in transition" = paradigm shift
```

### Stage 3: Registry-Stabilized Reading (When registered)

If the compound has a corpus-confirmed specialized meaning, use that narrower reading.

```
ha-ka-de-su   algebraic: heat-action-decay-structure = fire destroying a building
            registry: [if registered as "conflagration"] = large uncontrolled fire
```

---

## The Golden Rule: Compositionality

**If you can build it from existing roots + heads + suffixes, you understand it.**

No dictionary is needed. The system is designed so that a speaker who knows the primitives and patterns can parse and construct any unfamiliar word on the fly. The patterns are the law; the lexicon is just examples.

