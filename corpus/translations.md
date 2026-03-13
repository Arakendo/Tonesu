# Translations

## Status: Empty — populate after sentence patterns are established

This file tests the language against real passages. Translation stress-tests the system in ways that constructed toy sentences cannot: real texts contain idioms, metaphors, implicit assumptions, and concepts that were never anticipated during design.

---

## Purpose

- Find gaps in the primitive set
- Reveal grammatical structures the language cannot yet express
- Test whether contracted forms emerge naturally
- Discover where the formal/colloquial split is necessary

---

## Recommended Test Passages

Work through these roughly in order of complexity.

### Tier 1 — Simple and concrete
- [ ] A weather report (time, place, physical states)
- [ ] A short recipe (sequence, action, quantity, physical objects)
- [ ] A basic tool manual (steps, imperatives, physical description)

### Tier 2 — Relational and social
- [ ] A short letter or greeting
- [ ] A simple news headline
- [ ] A dialogue between two people exchanging information

### Tier 3 — Abstract and technical
- [ ] A dictionary definition of "algorithm"
- [ ] A short paragraph from a science textbook
- [ ] A legal or contractual statement (obligation, condition, party)

### Tier 4 — Edge cases
- [ ] A metaphor or idiom (e.g. "burning bridges," "the idea caught fire")
- [ ] A sentence with deliberate ambiguity in English
- [ ] A question with no clear agent (passive voice equivalent)
- [ ] A philosophical statement about the nature of knowledge

---

## Entry Format

```
Source language:   English (or other)
Original text:     [text here]
Translation:       [language form here]
Gloss:             [morpheme breakdown]
Notes:             [what was difficult, what was approximated, what failed]
Status:            draft | reviewed | stable
```

---

## Open Questions

- [ ] Does the language need a passive voice construction? (See S011 in sentences.md)
- [ ] How should idiomatic metaphors be handled — preserve them, block them, or formally encode analogy?
- [ ] What is the translation policy for culturally specific concepts with no structural equivalent?
