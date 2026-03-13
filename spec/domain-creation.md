# Domain Creation

## Status: Draft

This file defines the **rules** for creating and managing conceptual domains. It is normative spec — if these rules change, that is a real language change.

The registered domain instances (the actual list of domains) are in registry/domains.md.

---

## What a Domain Is

A domain is a conceptual namespace. It groups related concepts under a shared substrate+principle label, acts as a productive root for that field's vocabulary, and integrates with the language's compounding system through the domain marker `da`.

Domains are first-class linguistic objects. They are not just vocabulary categories — they can be declared, inherited, composed, and compressed.

---

## Domain Structure

Every domain is defined by two required components:

**Substrate** — the conceptual material the domain operates on
**Principle** — how that material is organized or transformed

```
domain = substrate + organizing principle
```

Domains are expressed using the domain marker `da`:

```
da-[substrate root]-[principle root]
```

Example:
```
da-to-ki   =  knowledge (to) + change/process (ki)  =  computation domain
```

---

## The Five Domain Rules

### 1. Declaration Rule
A domain must be declared from meta-concept primitives (see registry/primitives.md), not from surface objects or cultural artifacts. A domain must be broad enough to support **multiple derived concepts**. A term describing only a single object is not a domain.

*Rationale: prevents domain fragmentation and arbitrary proliferation.*

### 2. Inheritance Rule
A new domain may extend an existing domain by adding exactly one modifier.

```
da-to-ki
→ da-fe-to-ki   (formal / logic-based computation)
→ da-ne-to-ki   (networked / distributed computation)
```

Depth limit: avoid inheritance chains longer than 3 levels without strong justification.

### 3. Composability Rule
Domains may intersect to yield a new domain when a concept genuinely lies at the boundary of two fields.

```
da-zo + da-to  →  da-zo-to   (life + knowledge = genetics / bioinformatics)
da-ra + da-si  →  da-ra-si   (energy + signal = signal processing)
```

Composition requires that both parent domains are already registered.

### 4. Stability Rule
Once a domain root is registered, it is stable. New terminology inside the domain grows through compounding — not by redefining or renaming the domain itself.

*Rationale: this is the direct lesson from Wilkins' failure. Fixing the root and growing vocabulary forward prevents vocabulary churn.*

### 5. Scope Rule
Domain names condense over time through three stages:

| Stage | Form | Example |
|-------|------|---------|
| 1 | Explicit compound | `information-process domain` |
| 2 | Stable label | `computation domain` |
| 3 | Lexicalized short form | `da-compu` |

Stage 3 forms are recorded in registry/domains.md alongside the full formal form.

---

## Deriving Vocabulary from a Domain

Once a domain is registered, its label is a productive root. New concepts inside the domain are formed by combining the domain root with other primitives or derivational markers.

Pattern:
```
[domain root] + [concept role]
```

Example using `da-to-ki` (computation domain):
```
da-to-ki + -mu  →  computation device  (computer)
da-to-ki + -su  →  computation structure  (algorithm / architecture)
da-to-ki + -ne  →  computation network  (internet)
da-to-ki + -li  →  computation agent  (programmer)
```

---

## Process for Proposing a New Domain

1. Identify the substrate and principle using existing primitive roots
2. Confirm no existing domain already covers the conceptual space
3. Confirm at least 3 distinct child concepts would be expressible under the proposed domain
4. Add a proposed entry to registry/domains.md with status: proposed
5. Promote to status: accepted once at least 3 child compound words are registered in registry/derived.md

---

## Open Questions

- [ ] Should `da-` be a prefix that fuses with the root phonetically, or always remain a free syntactic particle?
- [ ] Standard procedure for deprecating a domain whose scope was drawn too narrowly
- [ ] Whether intersecting domains always create a new registered domain, or can remain ad-hoc compounds
