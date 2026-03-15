# Translation Test: Genesis 1

## Source: Hebrew Bible / Old Testament, Genesis, Chapter 1
## Reference translation: NIV (New International Version)
## Status: Draft — verses 1–31 attempted (complete first pass; see open questions)

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
| God | ✅ Compositional path verified | `be-go-li` (creator-agent) + `[X]-no-fe` attribute compounds; see GOD-001 |
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

Tonesu treats religious constructs as organized social and epistemic structures, not supernatural ontological primitives (see `registry/domains.md`). However, the classical divine *attributes* (omniscience, omnipotence, omnipresence, omnibenevolence, necessary being) are all expressible compositionally via the `[X]-no-fe` suffix pattern. The gap is not a primitive gap — it is a naming gap.

### Attribute Compound Analysis (THO-001)

The `[X]-no-fe` pattern = X + `no` (negation/absence) + `fe` (boundary/limit) = X without limit. All five classical omni-attributes form cleanly:

| Attribute | Compound | Reading |
|-----------|----------|---------|
| Omniscience | `to-no-fe` | knowledge without boundary |
| Omnipotence | `ra-no-fe` | force without boundary |
| Omnibenevolence | `vo-no-fe` | value/goodness without boundary |
| Omnipresence | `pa-no-fe` | space without boundary |
| Necessary being | `go-no-fe` | causal primacy without boundary |
| Creator | `be-go-li` | agent of generative origin |
| Eternal (in time) | `ti-no-fe` | time without boundary |
| Atemporal | `no-ti` | outside time entirely |

**Collision resolved:** The natural form for "uncaused cause" would use `go-no-go` (cause without origin). But `go-no-go` is the concessive grammar particle (G009). `go-no-fe` = cause-without-boundary = **necessary being** avoids the collision and captures the same philosophical content: a cause whose causal primacy has no limiting prior condition.

**Full attribute stacking:**
```
la-be-go-li  go-no-fe  to-no-fe  ra-no-fe  vo-no-fe  pa-no-fe
```
*The creator-agent: necessary-being, omniscient, omnipotent, omnibenevolent, omnipresent.*

Multi-predicate stacking is grammatically valid in Tonesu; each compound is a successive predicate of the same agent. The full chain is available for formal/philosophical register. Too long for everyday use — colloquial compression candidate `bel` (for `be-go-li`) proposed; distinctiveness check pending.

**Image of God (Genesis 1:26):**
```
la-be-go-li  lo-zo-li  ka-be-past  lo-be-go-li-si
```
`be-go-li-si` = `be-go-li` (creator) + `si` (signal/representation/encoding) = creator-representation = *tselem* (image/likeness). `lo-be-go-li-si` as result-patient: persons were generated *as* a creator-representation. Minor gap: "in the image of" is technically a template/manner frame, not a standard result-patient — the result-patient reading is the closest available construction.

**Property-vs-essence copula gap:** "God is love" is an essence claim, not a property claim. `la-be-go-li  fa-vo-no-fe` (the creator-agent: affect-value-without-limit) is the property reading. The essence reading ("love is what God *is*, not merely what God *has*") requires a dedicated identity copula that Tonesu does not have. `la-X  Q` = property attribution; `lo-X  ne  lo-Y` = relational connection; neither cleanly encodes constitutional identity. Logged as a new open question.

### Translation Strategy for This Draft

**Two paths now exist:**

| Path | Form | Tradeoff |
|------|------|---------|
| Proper noun | `la-Elohim` | Borrows the tradition's name; honest about theological identity; grammar handles agency |
| Compositional | `la-be-go-li` | Makes philosophical structure explicit; loses the specific theistic identity of the Hebrew text |

**Decision for this draft:** Use `la-Elohim` as the agent throughout. The proper-noun strategy remains for translation fidelity — the Hebrew text is about *Elohim*, not a generic creator-agent. Tonesu's compositional path for creator-agent semantics is now verified and available for systematic theological writing; the translation draft adopts the name.

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

*All verses now have a first-pass attempt. Remaining gaps and open questions listed below.*

---

## Genesis 1:6–8 — The Vault (Firmament / Sky)

> *"And God said, 'Let there be a vault between the waters to separate water from water.' So God made the vault and separated the water under the vault from the water above it. And it was so. God called the vault 'sky.' And there was evening, and there was morning — the second day."*

**New vocabulary needed:**
- `pa-fe` = space-boundary = vault/firmament (sky dome). New compound; proposed for derived registry.
- `be-ma-ki` = ascending/above water = water above (directional `be` modifying fluid)
- `de-ma-ki` = descending/below water = water below

**Verse 6:**
```
la-Elohim  ka-si-past  [lo-pa-fe  be  du  lo-ma-ki  ka-fe]
```
*God said: let the vault come into being, resulting in the waters being separated.*

**Verse 7:**
```
la-Elohim  lo-pa-fe  ka-be-past
la-Elohim  lo-de-ma-ki  lo-be-ma-ki  ka-fe-past
du  be-past
```
*God made the vault. God separated below-water from above-water. And it was so.*

**Verse 8:**
```
la-Elohim  lo-pa-fe  na-Sky  ka-si-past
ti-de  fe-ki-past
ti-be  fe-ki-past
bun ti  ti-re
```
*God named the vault 'Sky.' Evening was bounded. Morning was bounded. Second day.*

⚠️ **Applying GOD-004 resolution:** `fe-ki` (boundary-motion = a phase being bounded/distinguished) rather than `be` (generation) for evening/morning from this verse onward. The temporal phases are not created — they are established as recurring distinctions.

**Difficulty:** LOW–MEDIUM. `pa-fe` is the one genuinely new compound; the rest composes cleanly.

---

## Genesis 1:9–10 — Dry Land and Seas

> *"And God said, 'Let the water under the sky be gathered to one place, and let dry ground appear.' And it was so. God called the dry ground 'Land,' and the gathered waters he called 'Seas.' And God saw that it was good."*

**New vocabulary:**
- `su-ma-ki` = structured/organized fluid = gathered/collected waters = seas
- "dry ground" = `pa-ma` (material-place = land/earth, already in use) — dryness is implied by contrast with `ma-ki`

**Verse 9:**
```
la-Elohim  ka-si-past  [lo-ma-ki  bol-pa  ki  du  lo-pa-ma  be]
du  be-past
```
*God said: let the waters move to one place, resulting in the material-ground appearing. And it was so.*

**Verse 10:**
```
la-Elohim  lo-pa-ma  na-Land  ka-si-past
la-Elohim  lo-su-ma-ki  na-Seas  ka-si-past
la-Elohim  ka-se-past  ,  lo-su-be-past  vo
```
*God named the ground 'Land.' God named the gathered waters 'Seas.' God examined — the result [was] good.*

**Notes:**
- `bol-pa` = one-place = a single location (ordinal digit + location root). Clean.
- `su-ma-ki` = structured-fluid. `su` (organization/structure) modifying `ma-ki` (fluid in motion) = organized/gathered water = what seas are.
- The "God saw that it was good" formula is established from verse 4; it recurs unchanged through the chapter. `la-Elohim  ka-se-past  ,  lo-su-be-past  vo` = God examined; the generated-result [is] good.

**Difficulty:** LOW.

---

## Genesis 1:11–13 — Vegetation

> *"Then God said, 'Let the land produce vegetation: seed-bearing plants and trees on the land that bear fruit with seed in it, according to their various kinds.' And it was so. The land produced vegetation... And God saw that it was good. And there was evening, and there was morning — the third day."*

**New vocabulary:**
- `zo-su-be` = plant-growth-product = seed (narrower than `zo-be` which covers all organism-growth-products including eggs)
- `du-zo-su` = plant-result = fruit (the product of the plant organism)
- `be-zo-su` = upward-growing organism = tree (growth-plant as opposed to ground-covering plants)

**Verse 11:**
```
la-Elohim  ka-si-past  [lo-pa-ma  lo-zo-su  ka-be  ,  lo-zo-su  lo-zo-su-be  lo-du-zo-su  be]
du  be-past
```
*God said: let the land generate plants; let plants [have] seeds and let fruit come into being. And it was so.*

**Verse 12:**
```
lo-pa-ma  lo-zo-su  ka-be-past
lo-zo-su  lo-zo-su-be  lo-du-zo-su  be-past
la-Elohim  ka-se-past  ,  lo-su-be-past  vo
```

**Verse 13:**
```
ti-de  fe-ki-past
ti-be  fe-ki-past
gal ti  ti-re
```

**Notes:**
- "According to their kinds" (*lemino*) is not explicitly translated — in Tonesu the kind-term system (`zo-su`, `zo-su-be`) already encodes class membership. The Hebrew phrase is redundant in Tonesu's compositional framework.
- `be-zo-su` (tree) is proposed but left out of the main translation here for brevity; the text uses `zo-su` as the general vegetation class with `du-zo-su` for fruit-bearing specimens.

**Difficulty:** LOW–MEDIUM.

---

## Genesis 1:14–19 — Lights in the Sky

> *"And God said, 'Let there be lights in the vault of the sky to separate the day from the night, and let them serve as signs to mark sacred times, and days and years.'... God made two great lights — the greater light to govern the day and the lesser light to govern the night. He also made the stars."*

**New vocabulary:**
- `lu-mu` = light-body = any luminous celestial object. `lu` (light) + `mu` (artifact/physical object). Proposed for derived registry.
- `nu-be-lu-mu` = great light-body = sun (large-scale light body)
- `nu-de-lu-mu` = lesser light-body = moon (decreasing/small-scale light body)
- `pu-lu-mu` = collective light-bodies = stars (plural class)
- `lu-ti` = light-time = daytime (as a temporal period, not just the light quality)
- `no-lu-ti` = dark-time = night (as a temporal period)

**Verse 14–15:**
```
la-Elohim  ka-si-past  [lo-pa-fe  lo-lu-mu  be  du  lo-lu-ti  lo-no-lu-ti  ka-fe  du  si-wi-ka-su  be]
```
*God said: let light-bodies come into being in the vault, resulting in day-time and dark-time being separated, and sacred-time signals coming into being.*

- `si-wi-ka-su` = signal-of-ritual = sign for appointed/sacred times. `si` (signal/representation) + `wi-ka-su` (ritual, W054). Composes cleanly.

**Verse 16:**
```
la-Elohim  lo-nu-be-lu-mu  lo-nu-de-lu-mu  ka-be-past
lo-nu-be-lu-mu  lo-lu-ti  wi-re
lo-nu-de-lu-mu  lo-no-lu-ti  wi-re
la-Elohim  lo-pu-lu-mu  ka-be-past
```
*God made the great light-body and the lesser light-body. The great light-body: day-governance. The lesser light-body: night-governance. God made the collective light-bodies [stars].*

- `wi-re` = feedback loop / iterative governance cycle (W099), here used as a predicate: "governs / rules over."

**Verses 17–18:**
```
la-Elohim  lo-lu-mu  pa-pa-fe  ka-past
lo-pa-ma  lo-lu  du
lo-lu-ti  lo-no-lu-ti  wi-re
la-Elohim  ka-se-past  ,  lo-su-be-past  vo
```
*God placed the light-bodies at the vault. The material-ground [received] light as a result. Day and night: governance. God examined — the result [was] good.*

**Verse 19:**
```
ti-de  fe-ki-past
ti-be  fe-ki-past
mol ti  ti-re
```

⚠️ **Collision note for `pa-pa-fe`:** The location particle `pa-` and the compound root `pa` (place) share the same form. `pa-pa-fe` = at/in [the space-boundary] = in the vault. The particle–root overlap is documented as intentional and transparent (grammar.md §Particle–Root Overlap Policy), but three `pa` tokens in sequence (`pa pa fe`) will be unusual in speech. Note for future resolution.

**Difficulty:** LOW–MEDIUM for grammar; MEDIUM for the new celestial vocabulary (`lu-mu`, `lu-ti`, `no-lu-ti`).

---

## Genesis 1:20–23 — Sea Creatures and Birds

> *"And God said, 'Let the water teem with living creatures, and let birds fly above the earth across the vault of the sky.' So God created the great creatures of the sea and every living thing with which the water teems... and every winged bird... And God saw that it was good. God blessed them and said, 'Be fruitful and increase in number...'"*

**New vocabulary:**
- `be-re` = recurring-growth = reproduce/be fruitful (growth + cycle = growth that recurs = reproduction)
- Existing registry terms: `zo-se-ma` (fish/aquatic vertebrates, KNM-006), `zo-se-so-di` (birds, KNM-005)

**Verse 20:**
```
la-Elohim  ka-si-past  [lo-ma-ki  pu-zo-se-ma  be  du  lo-zo-se-so-di  lo-pa-fe  be-ki-di]
```
*God said: let the waters teem with collective-aquatic-organisms; let birds [fly] upward-directed at the vault.*

- `pu-zo-se-ma` = collective sea organisms = teeming fish/sea-life
- `be-ki-di` = upward-directed-motion = flying above (ascending directed movement)

**Verse 21:**
```
la-Elohim  lo-zo-se-ma  lo-zo-se-so-di  ka-be-past
la-Elohim  ka-se-past  ,  lo-su-be-past  vo
```

**Verse 22 — blessing:**
```
la-Elohim  lo-zo-se-ma  lo-zo-se-so-di  ka-vo-past
la-Elohim  ka-si-past  [be-re  nu-be  lo-ma-ki  pu-be]
```
*God blessed the sea-creatures and birds. God said: be fruitful, multiply, fill the waters collectively.*

- `ka-vo` = deliberate-goodness-act = to bless (bestow goodness upon). `ka` (intentional action) + `vo` (value/quality).
- `be-re` as a command predicate = grow-cyclically = be fruitful / reproduce.
- `nu-be` = quantity-increase = multiply in number.
- `pu-be` = collective-growth = fill/increase collectively (in the seas).

**Verse 23:**
```
ti-de  fe-ki-past
ti-be  fe-ki-past
hin ti  ti-re
```

**Difficulty:** LOW. All key terms already established in registry.

---

## Genesis 1:24–25 — Land Animals

> *"And God said, 'Let the land produce living creatures according to their kinds: the livestock, the creatures that move along the ground, and the wild animals, each according to its kind.' And it was so. God made the wild animals... and God saw that it was good."*

**New vocabulary:**
- `wi-zo` = autonomous organism = wild animal (organism defined by self-directed will; `wi` = will/intention + `zo` = living thing)
- `ma-zo-ki` = matter-organism-motion = ground-moving creature / crawler (matter-level organism-in-motion = creatures that move along the ground)
- Existing: `zo-se-ne` (herd ungulates = livestock, KNM-007)

**Verse 24:**
```
la-Elohim  ka-si-past  [lo-pa-ma  lo-zo-se-ne  lo-wi-zo  lo-ma-zo-ki  be]
du  be-past
```
*God said: let the land produce herd-animals, autonomous organisms, and ground-crawlers. And it was so.*

**Verse 25:**
```
la-Elohim  lo-wi-zo  lo-zo-se-ne  lo-ma-zo-ki  ka-be-past
la-Elohim  ka-se-past  ,  lo-su-be-past  vo
```

**Notes:**
- `wi-zo` distinguishes "wild animal" from `zo-se-ne` (social-relational herd animal = livestock/domesticated herds). The structural contrast is will-governed (`wi-zo`) vs social-relational (`zo-se-ne`).
- "According to their kinds" is again left implicit; see note at verse 11.

**Difficulty:** LOW. Two new compounds both compose cleanly.

---

## Genesis 1:26–28 — Humanity; Image of God; Dominion

> *"Then God said, 'Let us make mankind in our image, in our likeness, so that they may rule over the fish in the sea and the birds in the sky, over the livestock and all the wild animals, and over all the creatures that move along the ground.' So God created mankind in his own image, in the image of God he created them; male and female he created them. God blessed them..."*

**Vocabulary:**
- `zo-li` = human-class organism — living social-intentional being
- `be-go-li-si` = creator-representation = *tselem* / image (established THO-001)
- `go-zo-li` = generative-role-person = male person (from `zi-zo-go` coupling role, W107)
- `du-zo-li` = result-role-person = female person (from `zi-zo-du` coupling role, W108)
- `la-yu` = group-agent = "let us" — see GOD-005 note below

**Verse 26:**
```
la-Elohim  ka-si-past  [la-yu  lo-zo-li  ka-be  go-be-go-li-si  du  lo-zo  ka-li-su]
```
*God said: let us (group-agent) generate human-class-organisms from/after the creator-representation, such that they exercise governance over organisms.*

- `la-yu` = group-agent = "we/us" — `yu` (the established group pronoun) in agent position. See GOD-005.
- `go-be-go-li-si` = from/after the creator-representation = in the image of the creator. `go` as origin-frame marker here: "originating from / modeled on."
- `ka-li-su` = deliberate-lead-coordinate = to exercise dominion/governance.

**Verse 27:**
```
la-Elohim  lo-zo-li  ka-be-past  go-be-go-li-si
lo-go-zo-li  lo-du-zo-li  ka-be-past
```
*God generated human-class-organisms from the creator-representation. The generative-role-persons and the result-role-persons [God] generated.*

**Verse 28:**
```
la-Elohim  lo-zo-li  ka-vo-past
la-Elohim  ka-si-past  [be-re  nu-be  lo-pa-ma  pu-be  lo-zo  ka-li-su]
```
*God bestowed goodness on humanity. God said: be fruitful, multiply, fill the material-ground collectively, exercise governance over organisms.*

**Notes — GOD-005:** The "let us make" plural (`la-yu`) is the first use of the group-agent pronoun `yu` in theological context. `yu` is already registered as "we / they (group / plural)" in the grammar. Using `la-yu` in a divine speech act works grammatically but leaves open whether `yu` is first-person-inclusive ("we including the speaker") or third-person-plural ("they"). The Hebrew *naasseh* is clearly first-person-plural. If a strict first/third distinction is needed, Tonesu currently has no mechanism for it. Logged as GOD-005.

**Difficulty:** MEDIUM. `be-go-li-si` and the `go-` origin frame for "in the image of" require some care; the rest is clean.

---

## Genesis 1:29–30 — Food Assignment

> *"Then God said, 'I give you every seed-bearing plant on the face of the whole earth and every tree that has fruit with seed in it. They will be yours for food. And to all the beasts of the earth and all the birds in the sky and all the creatures that move along the ground — everything that has the breath of life in it — I give every green plant for food.'"*

**New vocabulary:**
- `zo-ra-ma` = organism-energy-substrate = food (biological fuel). `zo` (living thing) + `ra` (energy/force) + `ma` (matter/substance) = the matter that provides energy to organisms. Proposed for derived registry.

**Verse 29:**
```
la-Elohim  ka-si-past  [lo-zo-su  lo-be-zo-su  lu-zo-li  ka  ,  go-zo-ra-ma]
```
*God said: vegetation and trees — [I] act for the benefit of humans, as organism-food.*

- `lu-zo-li` = for-the-benefit-of human-class-organisms (beneficiary prefix `lu-` + `zo-li`)
- `go-zo-ra-ma` = with organism-food as purpose/origin = intended as food

**Verse 30:**
```
lo-wi-zo  lo-zo-se-ne  lo-zo-se-so-di  lo-ma-zo-ki  zo-ra-ma  be
```
*For wild animals, herd animals, birds, and crawlers — organism-food exists.*

**Notes:** "The breath of life" (*nefesh hayah*) in verse 30 is a theological marker for animate beings. Tonesu handles this compositionally — `zo` (living thing) already encodes the animate distinction. No separate term needed; "all organisms" subsumes the Hebrew.

**Difficulty:** LOW–MEDIUM. `zo-ra-ma` is the one new compound; the food-assignment structure is grammatically simple.

---

## Genesis 1:31 — Very Good; Sixth Day

> *"God saw all that he had made, and it was very good. And there was evening, and there was morning — the sixth day."*

**Vocabulary:**
- `vo-be` = growing-goodness = very good / exceedingly good. (`vo` = value + `be` = increasing = value at a heightened degree)

```
la-Elohim  lo-su-be-past  ka-se-past  ,  lo-su-be-past  vo-be
ti-de  fe-ki-past
ti-be  fe-ki-past
wes ti  ti-re
```
*God examined the organized-generation [all that had been made]; the organized-generation [was] very good. Evening was bounded. Morning was bounded. Sixth day.*

**Notes:**
- `lo-su-be-past` = the structured/organized generation (what was made) — using `su` (structure/organization) + `be` (growth/generation) + past marker as a nominalized form. This is a compression; a fully explicit reading would use a relative clause. Works for purposes of this translation.
- `vo-be` vs `vo-no-fe`: "very good" (`vo-be`) contrasts with the divine attribute compound `vo-no-fe` (omnibenevolence = goodness without boundary). "Very good" is a degree marker on finitely good creation; `vo-no-fe` is a claim about unconditioned divine goodness.

**Difficulty:** LOW.

---

## Summary Assessment (Updated)

| Category | Result |
|----------|--------|
| Physical cosmology (light, dark, water, land, sky) | ✅ Composes cleanly from primitives |
| Temporal structure (days, evening, morning, sequence) | ✅ Clean via `ti-be`/`ti-de`/`ti-re` + ordinal digits; `fe-ki` for phase-bounding |
| Evaluative clauses ("and it was good") | ✅ `lo-X  vo` is natural and compact |
| Creative agency (generates, separates, names, governs) | ✅ Grammar handles throughout |
| Causal and result frames | ✅ `go` / `du` map well to this narrative style |
| Vegetation, sea life, birds, land animals | ✅ `zo-su`, `zo-se-ma`, `zo-se-so-di`, `zo-se-ne`, `wi-zo` all compose |
| Celestial lights (sun, moon, stars) | ✅ `lu-mu` compounds; one `pa-pa-fe` collision flagged |
| Humanity and image of God | ✅ `zo-li`, `be-go-li-si`, `go-be-go-li-si` frame; male/female from coupling-role W-entries |
| God as agent | ❌ No compositional expression; proper-noun strategy adopted |
| Spirit / *ruach* (theological) | ❌ Physical wind covered; pneumatic/theological reading untranslatable |
| Cosmic void / formlessness | ✅ `no-su  no-ko` is precise |
| Spatial layering ("over the surface of") | ⚠️ Partial — `pa-fe` and positional context approximate; no dedicated spatial-preposition system |
| Food / biological fuel | ✅ `zo-ra-ma` proposed; composes cleanly |

**Overall:** Genesis 1 is ~85% compositionally expressible in Tonesu. The remaining gap is concentrated in the theological/supernatural layer and in fine spatial prepositions. The physical, temporal, evaluative, and biological structure of the creation narrative composes cleanly.

---

## Open Questions

**GOD-001:** What is the proper Tonesu compositional candidate for a being with causal priority and no prior cause? `go-no-go-li` is structurally honest but long. Is the proper-noun borrowing strategy (`la-Elohim`) the permanent design decision for theonyms, or is there a compositional treatment that doesn't commit a theological interpretation?

**GOD-002:** `ruach Elohim` (Spirit of God / wind of God / breath of God) — the Hebrew is deliberately ambiguous across physical and theological readings. Translation policy question: when source-language ambiguity is theologically productive, should Tonesu (a) pick one reading, (b) use `~` to hedge, or (c) note untranslatability and move on?

**GOD-003:** "God saw that it was good" uses `ka-se` (deliberate examination). This anthropomorphizes divine evaluation. Is this the right verb, or does it over-constrain the theology?

**GOD-004:** ✅ **Resolved.** "Evening and morning" use `fe-ki` (boundary-motion = boundary established) from verse 8 onward. The temporal phases are not created — they are bounded/distinguished. `be` (generation) reserved for entities coming into existence.

**GOD-005:** "Let us make" (Genesis 1:26) — `la-yu` is used, drawing on the existing group-pronoun `yu` = "we / they (group / plural)." However, `yu` is currently non-deictic: it does not distinguish first-person-inclusive ("we the speakers") from third-person-collective ("they"). Whether the divine plural requires a strict first-person reading is unresolved. For now `la-yu` is the best available form.

**GOD-006:** `pa-pa-fe` (at-the-vault) chains three `pa` tokens (particle + compound root + compound second element). Technically transparent per the particle–root overlap policy, but unusual in speech. Possible mitigation: use `lo-pa-fe` (patient-marker on the vault) to mark location by implication in context, avoiding the triple-pa.

**GOD-007 (new):** "The breath of life" (*nefesh hayah*) in verse 30 is currently absorbed into `zo` (living thing). No separate term for "the animating principle within an organism" exists beyond `zo-to` (soul, W068) and `zo-si` (spirit/disembodied agent, W069). Whether those terms cover the *nefesh* concept or a new compound is needed is unresolved.

---

## New Vocabulary Proposed (from 1:6–31)

The following compounds appeared in this translation and require registry review:

| Form | Reading | Priority | Notes |
|------|---------|----------|-------|
| `pa-fe` | space-boundary / vault / firmament | Register | Needed for sky dome; clean composition |
| `lu-mu` | light-body / celestial luminary | Register | Sun, moon, stars all build on this; high utility |
| `lu-ti` | light-time / daytime | Monitor | Compositional; may not need a registry entry |
| `no-lu-ti` | dark-time / night | Monitor | Compositional; pair with `lu-ti` |
| `du-zo-su` | plant-result / fruit | Register | Needed for botany; clean composition |
| `zo-su-be` | plant-growth-product / seed | Register | Alongside `zo-be` (general org-growth-product); narrower |
| `zo-ra-ma` | organism-energy-substrate / food | Register | High-frequency concept; worth anchoring |
| `wi-zo` | autonomous organism / wild animal | Monitor | Compositional; may be sufficient as-is |
| `ma-zo-ki` | ground-moving organism / crawler | Monitor | Compositional; sufficient as-is |
| `be-re` | recurring growth / reproduce | Monitor | Productive pattern from `be`+`re`; no entry needed |
| `vo-be` | growing goodness / very good | Monitor | Productive `vo`+`be` intensifier; no entry needed |
| `si-wi-ka-su` | sacred-time signal / appointed-time sign | Monitor | One-off in this text; defer registration |
