# Naming

## Status: Draft

---

## Core Principle

Proper names are a **protected lexical class**. They identify; they do not describe. The language's compositional system applies to titles and institutional names, not to personal identifiers by default.

Introduced by the proper-name particle `na`:
```
na Derek
na Tucson
na Atlas
```

This signals to the listener: "what follows is an identifier, not a compositional noun."

---

## Name Categories

### 1. Personal Names
- Chosen by individual, family, or culture
- Phonologically normalized into the language's sound system
- Not semantically decomposed by default
- Stress rule applies (first syllable)

Examples:
```
na Derek  →  na Derik
na Sarah  →  na Sara
```

### 2. Family / House / Clan Names
- Inherited or collectively held
- May be semantically constructed if the culture supports it
- Follow same `na` marking

```
na Alaren   (inherited, opaque)
na Stonepath (descriptive, transparent)
```

### 3. Place Names
- Two official forms allowed:
  - **Endonym-preserving:** keeps original identifier
  - **Descriptive:** constructed in-language if useful
- Both forms valid; context determines which is used

```
na Tucson         (endonym)
na warm-valley    (descriptive equivalent)
```

### 4. Institutional / Organization Names
- Semantic naming strongly preferred
- Constructed as normal compounds, then registered
- Not marked with `na` — treated as ordinary domain-compound nouns

```
knowledge-transfer system
defense-information network
harmony-union project
```

### 5. Project / System / AI / Technical Names
- May use both a semantic compound and a short identifier
- Semantic form is canonical; short form is colloquial

```
Formal:     information-process coordination system
Identifier: na Concordia
```

### 6. The Language's Own Name

The language is named using its own primitives, demonstrating the dual-register design:

```
Formal:   to-ne-su      (pattern – relation – structure)
Casual:   tonesu
```

This is the canonical example of **formal compound → casual contraction**. The name describes what the language does: patterns of meaning built through relational structure. The casual form `tonesu` follows standard phonological contraction and is the name used in ordinary reference.

---

## Name Integrity Rules

Proper names resist normal lexical mutation:

- Names do not compound internally unless intentionally constructed
- Names do not take derivational suffixes directly (use a title instead)
- Names may be phonologically adapted (within phonotactic rules) but not semantically reanalyzed
- Titles and relational markers attach externally, leaving the name intact

**Correct:**
```
title-engineer na Derek
place-in na Tucson
na Derek poss device
```

**Avoid:**
```
Derik-li   (treating the name as a root with agent suffix)
```

---

## Dual-Form Naming

A person (or entity) may carry both forms:

| Form | Purpose |
|------|---------|
| Identifier | everyday reference, legal identity |
| Semantic title | role, domain, function |
| Community/honor name | cultural or symbolic |

Example:
```
Identifier:    na Derik Alaren
Role title:    defense-systems architect
Community name: na Red-Fox
System ID:     derik-alaren-01
```

---

## Relational and Social Forms

Familiarity, respect, rank, and kinship are expressed as external grammar, never built into the name itself.

```
elder-title na Alaren
student-of na Mira
group-member na Derik
```

---

## Gender in Names

Not built into names grammatically. Any sex/gender/social marker is an optional modifier:

```
female na Sara
elder-male na Kerun
```

---

## Open Questions

- [ ] Define phonological adaptation rules precisely (which sounds map to which when borrowing foreign names)
- [ ] Should `na` be required in all contexts or only when ambiguity could occur?
- [ ] Define rules for compound place names that are partly descriptive and partly endonymic
- [ ] Specify format for machine/system identifiers (language vs. external convention)
