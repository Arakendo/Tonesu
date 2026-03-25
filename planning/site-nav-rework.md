# Site Navigation Rework Plan

*Created: 2026-03-24*
*Status: Complete — implemented 2026-03-24*

---

## Problem statement

The current nav has four coherence issues that affect a first-time visitor:

1. **Primitives is at position 8 of 11 in "The language"** — new users stepping through the sidebar hit Grammar before they know any roots. Every example in Grammar becomes opaque.

2. **"Patterns" appears twice** — `Tonesu → Patterns and quick reference` (a use-oriented reference card) and `To'tonesu → Patterns` (a theoretical analysis of why patterns exist). Identical label, opposite purpose.

3. **"Domains" appears twice** — `Tonesu → Domains` (how the domain *system* works abstractly) and the whole `To'tonesu → Domains` subtree (applying vocabulary to specific fields). Same label, different content type.

4. **Vocabulary sub-section is 6-deep-flat** — six entries shown at equal weight (registry, English index, by-domain, by-root, colloquial registry, colloquial lookup). No hierarchy; looks like six different word lists.

Secondary issues:
- `Named roots` and `Exceptional anchors` cover the same topic (non-compositional lexical tiers) split across two pages. Redundant navigation entry.
- `Morphology` is at position 3, before `Building words` — learners hit the most technical reference page before they can form a word.
- Empty domain stubs (10 pages in `To'tonesu`) are full nav entries that deliver nothing.

---

## Current nav skeleton

```
Home
├── Quick start
└── Cheat sheet

Tonesu  (the language)
├── The language
│   ├── Sounds                       [pos 1]
│   ├── Grammar                      [pos 2] ← too early
│   ├── Morphology                   [pos 3] ← too early
│   ├── Building words               [pos 4]
│   ├── Patterns and quick reference [pos 5] ← name collision
│   ├── Notation                     [pos 6]
│   ├── Scope prefixes               [pos 7]
│   ├── Primitives                   [pos 8] ← should be pos 2
│   ├── Named roots                  [pos 9] ┐ partial overlap
│   ├── Exceptional anchors          [pos 10]┘
│   └── Domains                      [pos 11] ← name collision
└── Vocabulary
    ├── Tonesu Registry              ┐
    ├── English index                │
    ├── Tonesu by domain             │ 6-flat
    ├── Tonesu by root               │
    ├── Colloquial registry          │
    ├── Colloquial lookup            ┘
    └── Word Builder

Totonesu  (in use)
├── Practical
│   ├── Worked examples
│   ├── Production pathways
│   ├── Conversations
│   └── Sandbox
├── Analysis
│   ├── Contrast walkthroughs
│   ├── Register & colloquial
│   ├── Failures & edge cases
│   └── Stress tests
└── Sentences
    ├── Corpus
    ├── Foundations
    ├── Grammar & syntax
    ├── Domains
    ├── Theology & philosophy
    ├── Translation
    ├── Conversation corpus
    └── Translation Analyses

To'tonesu  (design)
├── Patterns                 ← name collision
├── Principles
├── Design notes
├── Knowledge & claims
├── Domains                  ← name collision
├── Sciences (3 stubs)
├── Society (5 stubs)
├── Values & ideas (3 stubs)
└── Language & meta (4 stubs)

About
```

---

## Proposed nav skeleton

```
Home
├── Quick start
└── Cheat sheet

Tonesu  (the language)
├── The language
│   ├── Sounds                       [pos 1]  — unchanged
│   ├── Primitives                   [pos 2]  — moved from pos 8
│   ├── Building words               [pos 3]  — moved up
│   ├── Grammar                      [pos 4]  — moved down
│   ├── Scope prefixes               [pos 5]  — now follows Grammar naturally
│   ├── Notation                     [pos 6]  — unchanged relative position
│   ├── Morphology                   [pos 7]  — moved to back half (reference)
│   ├── Quick reference              [pos 8]  — renamed from "Patterns and quick reference"
│   ├── Special forms                [pos 9]  — MERGE of Named roots + Exceptional anchors
│   └── Domain system                [pos 10] — renamed from "Domains"
└── Vocabulary
    ├── Word registry                          — main entry (was "Tonesu Registry")
    │   ├── English lookup                     — was "English index"
    │   ├── By domain                          — unchanged
    │   └── By root                            — unchanged
    ├── Colloquial forms                       — was "Colloquial registry"
    │   └── Colloquial lookup                  — unchanged
    └── Word Builder                           — unchanged

Totonesu  (in use)
└── (unchanged — structure is already coherent)

To'tonesu  (design)
├── Pattern analysis       — renamed from "Patterns" (resolves collision)
├── Principles
├── Design notes
├── Knowledge & claims
└── Domain exploration     — renamed from "Domains" (resolves collision)
    ├── Sciences (3 stubs)
    ├── Society (5 stubs)
    ├── Values & ideas (3 stubs)
    └── Language & meta (4 stubs)
```

---

## Changes itemised

### 1 — Reorder "The language" (mkdocs.yml only)

Move entries; no file changes needed except possibly updating cross-references on index pages.

| Before | After |
|--------|-------|
| Sounds, Grammar, Morphology, Building words, Patterns+QR, Notation, Scope, **Primitives**, Named roots, Anchors, Domains | Sounds, **Primitives**, Building words, Grammar, Scope, Notation, Morphology, Quick reference, Special forms, Domain system |

**Files affected:** `mkdocs.yml` nav entries only. No content changes.

---

### 2 — Merge "Named roots" + "Exceptional anchors" → "Special forms"

Both pages describe non-compositional lexical tiers (CVC and CVCC). `Named roots` covers the concept and CVC content; `Anchors` covers CVCC detail. They share the Assemblage-First Rule verbatim.

**Proposed merge strategy:**
- Keep `tonesu/named-roots.md` as the merged file (rename in nav to "Special forms")
- Absorb CVCC-specific content from `anchors.md` as a second H2 section
- Redirect `anchors.md` to `named-roots.md` or remove from nav (file can stay for URL stability)

**Files affected:** `www/docs/tonesu/named-roots.md` (expand), `mkdocs.yml` (remove anchors entry).

---

### 3 — Rename "Patterns and quick reference" → "Quick reference"

The current name is accurate but wordy and identical in meaning to `To'tonesu → Patterns` to a scanner. This page is a *use* reference, not a theory page. Calling it "Quick reference" aligns with how cheat sheets are normally labeled and removes the collision.

**Files affected:** `mkdocs.yml` nav label; optionally update the H1 in `www/docs/tonesu/patterns.md`.

---

### 4 — Rename "Patterns" (To'tonesu) → "Pattern analysis"

This page is the *theory* complement to the above. "Pattern analysis" distinguishes it from the reference card and signals that it is explanatory, not lookup.

**Files affected:** `mkdocs.yml` nav label; update H1 in `www/docs/to-tonesu/patterns.md`.

---

### 5 — Rename "Domains" in Tonesu → "Domain system"

Full label: "Domain system" communicates *how the abstraction works*. Removes the collision with To'tonesu's domain exploration tree.

**Files affected:** `mkdocs.yml` nav label; update H1 in `www/docs/tonesu/domains.md`.

---

### 6 — Rename "Domains" in To'tonesu → "Domain exploration"

This is the tree root of the To'tonesu domain pages (biology, law, etc.). "Domain exploration" signals intent and application, not system definition.

**Files affected:** `mkdocs.yml` nav label; update H1 in `www/docs/to-tonesu/domains/index.md`.

---

### 7 — Restructure Vocabulary sub-section

Currently 6 flat items. Proposed: 2 groups (Word registry + Colloquial forms) containing nested items. This makes "Word registry" unmistakably the main entry point and collapses the alternate views into it.

**Files affected:** `mkdocs.yml` nav structure only. No content changes.

---

### 8 — Empty domain stubs in To'tonesu (deferred)

10 pages (biology, theology, law, etc.) are full nav entries containing only a boilerplate placeholder sentence. Options:

- **(A) Deprioritise from nav** — remove from nav; keep files; re-add as content develops. Simplest.
- **(B) Inline under parent** — keep in nav but add a visible admonition at the top of each: `!!! note "In development"` — signals the gap is intentional, not a broken link.

Recommendation: **Option B**. The nav shapes expectations about what the language covers. Empty stubs showing domain intent are more useful than an unexplained absence. Admonition costs one line per file.

**Files affected (Option B):** One `!!! note` block added to each of the 10 stub files.

---

## Proposed implementation phases

| Phase | Scope | Risk | Effort |
|-------|-------|------|--------|
| 1 | `mkdocs.yml` nav reorder (item 1) | None — no content changes | Small |
| 2 | Rename labels in nav + matching H1s (items 3–6) | None | Small |
| 3 | Vocabulary nav restructure (item 7) | None — no content changes | Small |
| 4 | Merge Named roots + Anchors (item 2) | Low — consolidation only | Medium |
| 5 | Domain stub admonitions (item 8) | None | Small |

Phases 1–3 can be done in a single commit. Phase 4 requires reading and merging content. Phase 5 is mechanical and can run alongside any phase.

---

## What is NOT changing

- **The three-section division** (Tonesu / Totonesu / To'tonesu) — the homepage tiles explain it, the header subtitles reinforce it, it works.
- **Totonesu sub-structure** (Practical / Analysis / Under pressure / Sentences) — coherent as-is.
- **Any content files** other than those noted above.
- **URL structure** — unless Named roots + Anchors merge requires redirecting `anchors.md`.
