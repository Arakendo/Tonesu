# Domain System

A **domain** is a conceptual namespace that groups related vocabulary under a shared substrate and organizing principle. Domains are first-class linguistic objects in Tonesu — they act as productive roots from which specialized terminology grows through compounding, rather than requiring new primitives.

---

## What a Domain Is

Domains solve a core language-design problem: *How do you expand vocabulary into specialized fields without fragmenting the primitive set?*

Instead of adding dozens of new primitive roots for, say, computing or genetics, Tonesu declares a single domain root (`da-to-ki` = computation) and derives all related terms by compounding that root with existing concepts.

**A domain is:** substrate + organizing principle.

```
        Computing domain
              ↓
    substrate (to)   +   principle (ki)
    information         transformation/process
              ↓
  da-to-ki  =  computation
```

Once declared, a domain is productive:

```
da-to-ki  +  -mu  →  computing device  (computer)
da-to-ki  +  -su  →  computing structure  (algorithm)
da-to-ki  +  -li  →  computing agent  (programmer)
```

---

## Structure: Substrate + Principle

Every domain is defined by exactly two primitive roots:

| Component | Role | Example |
|-----------|------|---------|
| **Substrate** | The conceptual material the domain operates on | `to` (information/pattern) |
| **Principle** | How that material is organized or transformed | `ki` (change/process) |

The domain label itself is a compound: `da-{substrate}-{principle}`.

```
da-zo-to    =   life-domain + information-principle
               (genetics / bioinformatics)

da-ra-ki    =   energy-domain + process-principle
               (mechanics / motion)

da-to-fe    =   information-domain + formal-reasoning-principle
               (mathematics / logic)
```

This compositional structure means domain labels are inherently semantic — you can parse them and understand what conceptual intersection they represent.

---

## The Five Domain Rules

### 1. Declaration Rule
A domain must be justified from meta-concept primitives, not surface objects. It must be broad enough to support **multiple derived concepts** — a term for a single object is not a domain.

*Why:* Prevents fragmentation and arbitrary proliferation.

### 2. Inheritance Rule
New domains can extend an existing domain by adding exactly one modifier.

```
da-to-ki              base domain: computation
  ↓
da-fe-to-ki           child domain: formal reasoning + computation (logic)
da-ne-to-ki           child domain: networked computation (distributed systems)
```

Inheritance chains should not exceed 3 levels without strong justification.

### 3. Composability Rule
Domains can intersect to yield a new domain when a concept genuinely lies at the boundary of two fields.

```
da-zo         +   da-to      →   da-zo-to
life-domain       knowledge-domain   life-information domain
(biology)         (epistemology)     (genetics / bioinformatics)
```

Both parent domains must already be registered.

### 4. Stability Rule
Once a domain root is registered, it is stable. New vocabulary within the domain grows through compounding — not by renaming or redefining the domain.

*Why:* This is the core lesson from John Wilkins' Real Character (1668). When roots are fixed and vocabulary grows forward, you avoid churn.

### 5. Scope Rule
Domain names condense over time through three stages:

| Stage | Form | Example |
|-------|------|---------|
| 1 | Explicit compound | `information-transformation domain` |
| 2 | Stable label | `computation domain` |
| 3 | Lexicalized shortform | `da-compu` |

---

## Deriving Vocabulary from a Domain

Once a domain is registered, its label is a productive root. New concepts inside the domain combine the domain root with other primitives or derivational suffixes.

### Pattern

```
{domain root}  +  {concept marker}
```

### Example: Computing Domain (`da-to-ki`)

```
da-to-ki + -mu    →  computing device          (computer)
da-to-ki + -su    →  computing structure       (algorithm, architecture)
da-to-ki + -ne    →  computing relation        (network)
da-to-ki + -li    →  computing agent           (programmer)
da-to-ki + -pa    →  computing location        (server, data center)
da-to-ki + -ka    →  computing action          (to process, to compute)
```

Each derived term is compositional — the meaning is transparent from its parts.

---

## Domain Registry

### Cross-Domain Foundation

These provide meta-structure; other domains inherit from or compose with them.

| Domain | Name | Substrate | Principle | Notes |
|--------|------|-----------|-----------|-------|
| `da-su` | Structure | `su` order | `su` arrangement | meta-structure domain |
| `da-ki` | Process | `ki` change | `ki` sequence | transformation domain |
| `da-to` | Knowledge | `to` pattern | `to` organization | epistemology domain |
| `da-li` | Agency | `li` person | `wi` intention | action / social actor domain |

### Physical Sciences

| Domain | Name | Substrate | Principle | Parent | Notes |
|--------|------|-----------|-----------|--------|-------|
| `da-ra` | Energy | `ra` energy | `ki` transfer | — | thermodynamics, physics |
| `da-ki-ra` | Motion | `ki` motion | `ra` force | `da-ra` | mechanics |
| `da-ma` | Matter | `ma` substance | `su` composition | — | chemistry, materials |
| `da-pa` | Space | `pa` space | `su` topology | — | geometry, topology |

### Life Sciences

| Domain | Name | Substrate | Principle | Parent | Notes |
|--------|------|-----------|-----------|--------|-------|
| `da-zo` | Life | `zo` living thing | `be` growth | — | biology broadly |
| `da-zo-su` | Life-Structure | `zo` organism | `su` organization | `da-zo` | anatomy, cell biology |
| `da-zo-to` | Life-Information | `zo` organism | `to` pattern/encoding | `da-zo` | genetics, bioinformatics |

### Information & Computation

| Domain | Name | Substrate | Principle | Parent | Notes |
|--------|------|-----------|-----------|--------|-------|
| `da-to-ki` | Computation | `to` information | `ki` transformation | `da-to` | computing broadly |
| `da-to-su` | Memory | `to` information | `su` storage | `da-to` | databases, data storage |
| `da-si-ne` | Communication | `si` signal | `ne` transfer | — | networks, language |
| `da-to-fe` | Logic | `to` pattern | `fe` formal reasoning | `da-to` | mathematics, formal systems |

### Social & Human

| Domain | Name | Substrate | Principle | Parent | Notes |
|--------|------|-----------|-----------|--------|-------|
| `da-li-ne` | Social | `li` person | `ne` relation | `da-li` | society, governance, kinship |
| `da-to-ki-li` | Education | `to` knowledge | `ki-li` learning/transfer | `da-to` | teaching, learning |
| `da-vo` | Value | `vo` value | `vo` judgment | — | ethics, aesthetics, beauty |

### Religion & Doctrine

Religious authority and knowledge authority are structurally identical in Tonesu: the priest is an archivist of doctrine (`to-su-li`).

| Domain | Name | Substrate | Principle | Parent | Notes |
|--------|------|-----------|-----------|--------|-------|
| `da-to-re` | Doctrinal | `to` knowledge | `re` recurrence/tradition | `da-to` | religion, canon, tradition |

Key compounds from religious contexts:

```
wi-si          prayer / will-signal
to-re-su       canonical doctrine / scripture
fe-vo          sacredness (set-apart value)
zo-to          soul / identity-pattern
zo-si          spirit / disembodied agent
```

### Mystic & Resonance

Covers mystic phenomena: resonance between will and physical systems, intentional practice, anomalous signal patterns, and non-ordinary perception. All core mystic concepts already derive from existing primitives.

| Domain | Name | Substrate | Principle | Notes |
|--------|------|-----------|-----------|-------|
| `da-wi-ra` | Resonance | `wi` will/intention | `ra` force/energy | mystic practices, ritual, perceptual states |

Key compounds:

```
pa-ra          field (spatial energy distribution)
wi-ka-su       ritual (organized intentional-action structure)
fe-su          ward / protective barrier
zo-se-ki       trance (organism-perception state transition)
ne-ra          resonance / energetic coupling
```

---

## When to Use Domains

Domains are used:
- **In specialized vocabulary** — Writing about computing, biology, or mathematics? Use domain compounds.
- **In teaching** — Show learners how related concepts nest under a single domain root.
- **In compounding** — When you need to create a new term, check if it belongs to an existing domain.

Domains do **not** appear in basic narrative or everyday speech unless the specialized terminology itself is the topic.

---

## Proposing a New Domain

To propose a new domain:

1. **Identify substrate and principle** using existing primitives
2. **Confirm no existing domain** already covers the space
3. **Show at least 3 child concepts** would be expressible under the domain
4. **Document with:** substrate, principle, rationale, and 2–3 example derived terms

Example:

```
Proposed domain: da-no-ma (scarcity domain)
  Substrate: no (negation/absence)
  Principle: ma (matter/stuff)
  Rationale: Economics, resource allocation, scarcity reasoning
  
  Example derived terms:
    - da-no-ma-li  :  economic agent (merchant, trader)
    - da-no-ma-pa  :  market (place of scarcity negotiation)
```

The domain advances to "accepted" status once 3 derived child terms are registered in the word registry.

---

## Design Philosophy

Domains embody a core Tonesu principle: **compositionality and stability over vocabulary inflation**. Instead of adding new roots whenever specialized vocabulary is needed, Tonesu fixes domain roots and allows vocabulary to grow naturally through compounding.

This design:
- **Reduces primitives** — The base set stays small and manageable
- **Makes terminology transparent** — You can parse `da-to-ki-mu` and know it means "computer" (`computation-device`)
- **Supports growth** — New fields and concepts integrate without redefining core roots
- **Enables translation** — Specialized terminology maps clearly to source-language structure

