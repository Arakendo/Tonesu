# Translation Test: Genesis 1

## Source: Hebrew Bible / Old Testament, Genesis, Chapter 1
## Reference translation: NIV (New International Version)
## Status: Draft — verses 1–5 attempted; verses 6–31 pending

---

## Purpose

Genesis 1 is one of the most translated and theologically dense passages in world literature. It combines:

- Cosmological claims (creation, void, light, sky, water, land)
- Theological claims (a creator agent with causal priority)
- Naming events (day, night, sky, earth, sea)
- Evaluation claims ("and it was good")
- Temporal structure (six-day sequence)

For Tonesu this is a Tier 4 edge test. Most content terms compose cleanly from primitives; the primary challenge is the concept of God as a causally prior agent with no Tonesu structural equivalent.

---

## Known Gaps Before Starting

| Concept | Status | Notes |
|---------|--------|-------|
| God | ❌ No compositional expression | Tonesu has no supernatural ontological primitive; see GOD-001 |
| "In the beginning" | ⚠️ Partial | `ta-go-nu` (at the time of origin) — workable but absolute temporal origin claims are unusual |
| "heavens" | ⚠️ Partial | `pa-be` (emerging/upper space) or bare `pa`; no heaven/earth distinction at primitive level |
| "formless" | ✅ `no-su` | absence of structure |
| "void / empty" | ✅ `no-ko` | absence of containment/content |
| "darkness" | ✅ `no-lu` | canon (KNM-003) |
| "waters / the deep" | ⚠️ Partial | `ma-ki` (matter-in-motion) covers fluid; no term for "the deep" as named entity |
| "Spirit / wind" | ❌ Partial | `ra-ki` (energy-in-motion) covers the physical wind reading; theological "Spirit" has no equivalent |
| "hovering" | ⚠️ Partial | `ki-re` (sustained/recurring motion) — possible |
| "light" | ✅ `lu` | primitive — ideal fit |
| "good" | ✅ `vo` | primitive — ideal fit |
| "separated" | ✅ `fe-ki` / `ka-fe` | create/reach a boundary |
| "called X Y" (naming) | ✅ `na` particle | proper-noun naming mechanism — well-established |
| "evening / morning" | ✅ `ti-de` / `ti-be` | W041, W040 |
| "first / second day" | ✅ `bol ti ti-re` | first-ordinal recurring-cycle |

---

## The God Problem (GOD-001)

This is the central challenge. The text presupposes an agent (`la`-position entity) with:

1. **Causal priority** — uncaused first cause; no prior `go`
2. **Creative agency** — `be` (generation) fits the action
3. **Speech acts** — saying, calling, naming
4. **Evaluative capacity** — perceiving and judging (`vo`)
5. **No compositional expression in Tonesu**

Tonesu treats religious constructs as organized social and epistemic structures, not supernatural ontological primitives (see `registry/domains.md`). The concept of an ontologically prior creator agent is not in scope for the primitive set.

**Options evaluated:**

| Option | Form | Problem |
|--------|------|---------|
| Uncaused-causer compound | `go-no-go-li` | Structurally precise but very long; also only captures causal-priority, not divinity |
| Generation-source | `be-go-li` | Covers creative agency; misses omnipotence range |
| Proper noun via `na` | `la-[Elohim na]` | Honest — borrows the name; grammar handles the agency |
| Bare `go-li` | source/origin-agent | Short but too general |

**Decision for this draft:** Use `la-Elohim` as the agent throughout. The proper-noun strategy is the most honest: Tonesu does not claim to express the theological identity of God compositionally. The name is borrowed via the `na` particle (G008); the grammar handles the rest. This is consistent with how Tonesu treats all proper names.

---

## Verse-by-Verse

### Genesis 1:1
> *"In the beginning God created the heavens and the earth."*

**Attempt:**
```
ta-go-nu   la-Elohim   lo-[pa zi pa-ma]   ka-be
```

- `ta-go-nu` — at the time of first origin (temporal: at-cause-quantity = at the point of origination)
- `la-Elohim` — agent: Elohim (proper noun)
- `lo-[pa zi pa-ma]` — patient: [sky coupled-with material-place] (heavens and earth as coupled pair via `zi`)
- `ka-be` — deliberate generation

**Notes:** `zi` (mutual/coupling, R034) is the right connective for the heaven-earth pair — they are brought into being together as a coupled creation, not sequentially. The `ta-go-nu` frame is novel: Tonesu normally treats time as relational, not absolute; this is the first absolute-origin time claim in the corpus.

**Difficulty:** LOW for grammar; HIGH for theology (deferred to GOD-001).

---

### Genesis 1:2
> *"Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters."*

Three propositions:

**2a. Earth was formless and empty:**
```
lo-pa-ma   no-su   no-ko
```
*The material-place: without-structure, without-content.*

Clean. `no-su` (unstructured) and `no-ko` (without containment/content) stack as parallel predicates.

**2b. Darkness was over the surface of the deep:**
```
lo-no-lu   pa-de-fe
```
- `no-lu` — darkness (canon)
- `pa-de-fe` — the place of deep-limit / the bounding-depth (spatial compound)

⚠️ "Over the surface of the deep" is complex spatial layering. `pa-de-fe` approximates "the place at the deep boundary" — the surface of the void-water. The spatial relationship "over" is not explicitly marked; positional context carries it. Flag as spatial-preposition gap.

**2c. Spirit of God hovering over the waters:**
```
lo-ra-ki-Elohim   lo-ma-ki   ki-re
```
- `ra-ki-Elohim` — the wind/breath of Elohim (energy-in-motion + proper noun; genitive by compounding)
- `ma-ki` — matter-in-motion (fluid / water)
- `ki-re` — sustained/recurring motion (hovering)

⚠️ **Critical note:** `ra-ki` covers the physical wind/breath reading of Hebrew *ruach*. The theological "Spirit" reading is untranslatable directly — Tonesu has no concept of divine pneuma. This draft takes the physical reading. The theological ambiguity that is productive in the Hebrew is lost. See GOD-002.

**Difficulty:** HIGH. Verse 2 is the hardest clause in the chapter.

---

### Genesis 1:3
> *"And God said, 'Let there be light,' and there was light."*

```
la-Elohim   ka-si-past   [lo-lu   ka-be]
du   lo-lu   be-past
```

- `ka-si` — signal/say (signal as deliberate action)
- `[lo-lu ka-be]` — embedded purpose: light comes into being
- `du` — result frame (consequence)
- `lo-lu be-past` — light came into being

**Notes:** `lu` as primitive makes this nearly trivial. The causal chain `say → result → comes into being` maps exactly onto `ka-si` + `du` + `be`. The `du` result frame is the right connector: the coming-into-being of light is the *result* of the speech act, not the purpose (`wi` would imply intentional design; `du` simply marks consequence).

**Difficulty:** LOW. The most Tonesu-natural verse in the chapter.

---

### Genesis 1:4
> *"God saw that the light was good, and he separated the light from the darkness."*

```
la-Elohim   lo-lu   ka-se-past   ,   lo-lu   vo
la-Elohim   lo-lu   lo-no-lu   ka-fe-past
```

- `ka-se` — deliberate examination/perception (W034)
- `lo-lu vo` — light [is] good/valuable
- `ka-fe` — deliberate bounding/separating (fe as deliberate action = to create a categorical boundary)

**Notes:** The evaluative formula `ka-se` + `vo` is Tonesu-natural — perceive then evaluate. `ka-fe` for separation is precise: separating light from dark is exactly creating a categorical boundary (`fe`), not just a spatial one. The `ka` (deliberate action) marker is appropriate here: this is intentional separation.

**Difficulty:** LOW.

---

### Genesis 1:5
> *"God called the light 'Day,' and the darkness he called 'Night.' And there was evening, and there was morning — the first day."*

```
la-Elohim   lo-lu   na-Day   ka-si-past
la-Elohim   lo-no-lu   na-Night   ka-si-past
ti-de   be-past
ti-be   be-past
bol ti   ti-re
```

- `na-Day` / `na-Night` — borrowed names via `na` proper-noun particle; Tonesu has no isolated words for named day/night periods
- `ka-si` — to signal/name (speech act: assigning a name)
- `ti-de be-past` — the receding-time came into being (evening)
- `ti-be be-past` — the approaching-time came into being (morning)
- `bol ti ti-re` — first-ordinal recurring-cycle (the first day)

**Notes:** Tonesu speakers could substitute the compositional forms (`ti-de` / `ti-be`) for the borrowed names Day/Night — the language has the concepts without the names. The naming event (`ka-si` + `na`) is clean. The ordinal day count (`bol ti ti-re`) is the standard corpus pattern.

⚠️ "Evening and morning" coming into being (`be-past`) is slightly awkward — these are not entities being created but temporal phases being bounded. Alternative reading: `ti-de ti-re` / `ti-be ti-re` (recurring-evening / recurring-morning, i.e. the first instance of the cycle). Needs corpus resolution.

**Difficulty:** LOW–MEDIUM.

---

## Summary Assessment

| Category | Result |
|----------|--------|
| Physical cosmology (light, dark, water, land, sky) | ✅ Composes cleanly from primitives |
| Temporal structure (days, evening, morning, sequence) | ✅ Clean via `ti-be`/`ti-de`/`ti-re` + ordinal digits |
| Evaluative clauses ("and it was good") | ✅ `lo-X vo` is natural and compact |
| Creative agency (generates, separates, names) | ✅ Grammar handles; agent-identity deferred |
| Causal and result frames | ✅ `go` / `du` map well to this narrative style |
| God as agent | ❌ No compositional expression; proper-noun strategy adopted |
| Spirit / *ruach* (theological) | ❌ Physical wind covered; pneumatic/theological reading untranslatable |
| Cosmic void / formlessness | ✅ `no-su no-ko` is precise |
| Spatial layering ("over the surface of") | ⚠️ Partial — positional `pa` compounds approximate; no dedicated spatial-preposition system |

**Overall:** Genesis 1 is ~80% compositionally expressible in Tonesu. The 20% gap is concentrated in the theological/supernatural layer, which Tonesu explicitly does not claim to encode. The physical, temporal, and evaluative structure of the creation narrative composes cleanly and in some cases (light = `lu`, good = `vo`) is more direct than English.

---

## Open Questions

**GOD-001:** What is the proper Tonesu compositional candidate for a being with causal priority and no prior cause? `go-no-go-li` is structurally honest but long. Is the proper-noun borrowing strategy (`la-Elohim`) the permanent design decision for theonyms, or is there a compositional treatment that doesn't commit a theological interpretation?

**GOD-002:** `ruach Elohim` (Spirit of God / wind of God / breath of God) — the Hebrew is deliberately ambiguous across physical and theological readings. Translation policy question: when source-language ambiguity is theologically productive, should Tonesu (a) pick one reading, (b) use `~` to hedge, or (c) note untranslatability and move on?

**GOD-003:** The evaluative formula "God saw that it was good" requires `ka-se` (deliberate perception / examination). This anthropomorphizes divine evaluation — treating divine perception as the same category as organism perception. Is this the right verb, or does it accidentally over-constrain the theology?

**GOD-004:** "Evening and morning came into being" — are these temporal phases being *created* (warranting `be`) or *bounded/distinguished* (warranting `fe-ki`)? The Hebrew suggests the bounded-day structure is being established, not new entities generated. `fe-ki` may be more precise for verses 5, 8, 13, 19, 23, 31.

---

## Verses Pending

- [ ] 1:6–8 (sky / firmament / waters above and below)
- [ ] 1:9–10 (dry land, seas — naming)
- [ ] 1:11–13 (vegetation — `zo-no-ki` class)
- [ ] 1:14–19 (lights in the sky — `lu-ki-mu` candidates?)
- [ ] 1:20–23 (sea creatures and birds)
- [ ] 1:24–25 (land animals)
- [ ] 1:26–28 (humanity — `la-li` in image of God; dominion)
- [ ] 1:29–30 (food assignment)
- [ ] 1:31 (very good; sixth day)
