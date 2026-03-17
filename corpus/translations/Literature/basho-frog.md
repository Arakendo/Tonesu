# Translation Test: Bashō — The Frog Haiku

## Source: Matsuo Bashō (松尾芭蕉), 1686
## Original: Japanese (classical; kanji + hiragana)
## Status: Draft — first pass

---

## Purpose

The frog haiku is the **kireji / pure juxtaposition stress test**. It is the most translated poem in East Asian literature and has no consensus English version after 340 years, for a specific linguistic reason: the **kireji** `や` (ya) is structurally untranslatable into any European language. Tonesu has two candidate tools — `/` and `:` — and this batch determines which one applies, with consequences for the interpretation of the entire poem.

Primary tests:
- **Kireji as structural mark** — does `/` (parallel partition) or `:` (topic frame) correctly encode the `ya` cut? The two marks encode different readings; choosing between them forces a decision that Japanese leaves open for 340 years
- **Agent-drop** — the frog is grammatically present in line 2 (`kawazu tobikomu` — frog jumps-in); the perceiver of the sound in line 3 is absent; Tonesu has agent marking for the action but must choose how to handle the soundless final clause
- **Pure noun-phrase sentence** — line 3 `水の音` (mizu no oto = water's sound) is a bare noun phrase, no verb, no predicate; Tonesu requires a predicate form
- **Sound as event** — `so` (acoustic signal) must serve as both a thing and an event; minimal predication needed
- **Frog vocabulary gap** — no registered frog compound; `zo-se-ma` (aquatic-vertebrate class, kinds.md) used by contextual inference; GAP-BSH-001

Corpus sentences from this batch: **S468–S470**.

---

## Source Text

**Japanese (original):**
```
古池や
蛙飛び込む
水の音
```

**Romanization:**
```
furuike ya
kawazu tobikomu
mizu no oto
```

**Morpheme gloss:**
```
furu-ike  ya      — old-pond    [kireji: cut / pause / juxtaposition marker]
kawazu    tobi-komu   — frog     leap-enter
mizu  no  oto         — water GEN sound
```

**Literal (syntactically faithful but not poetic):**
> An old pond — / A frog jumps in / The sound of water

**The contested problem:** every English translator must decide what the dash, comma, line break, or silence *is* doing between "old pond" and "frog jumps in." Bashō left that structural relationship undefined by design. The poem's resonance lives in that gap.

---

## Vocabulary Framework

| Form | Reading | Construction | Notes |
|------|---------|--------------|-------|
| `re-fe-ma-ki` | old pond | `re` (recurrence/persistence) + `fe` (boundary) + `ma-ki` (water, MAT-002) = long-established bounded water = old pond | Compositional; `re` encodes long persistence through cycles; `fe-ma-ki` = bounded water = pond; head-final compound |
| `ma-ki` | water | `ma` (matter) + `ki` (motion) = flowing matter = water | Established MAT-002, S300–S306 |
| `zo-se-ma` | aquatic vertebrate / frog (by context) | kinds.md node: matter-perceptual organism; the branch covering fish and aquatic vertebrates | No specific frog discriminator registered — GAP-BSH-001; context (pond + jumping) disambiguates to frog-class |
| `ma-ki-so` | sound of water / water-sound | `ma-ki` (water) + `so` (sound) = water-sound, head `so` modified by `ma-ki` = the sound that belongs to water | Compositional; `so` is the head (the acoustic signal); `ma-ki` modifies it as the source-domain |
| `pa` | exists / occurs | primitive R021; existential predicate — used here as minimal predicate for the pure-noun-phrase final line | Provides required predicate without adding semantic weight |

### `re-fe-ma-ki`: building "old pond"

The compound builds head-finally:
- `ma-ki` = water (established)
- `fe-ma-ki` = boundary-water = bounded body of water = pond (`fe` = boundary/limit; pond is water with a limiting boundary)
- `re-fe-ma-ki` = recurring-bounded-water = a pond that has persisted through many cycles = old pond

`re` (recurrence/persistence/cycle) encodes oldness as temporal persistence — the pond that has been there through many seasons. This is not merely "a pond modified by time" but "a pond characterised by its having-been-there-across-cycles" — which is precisely the existential weight Bashō gives to `furuike`. An old pond in a haiku is not merely aged; it is a marker of established worldly continuity that the moment of the frog's entry briefly punctuates.

### `ma-ki-so`: "sound of water"

Head-final direction: `so` = sound (primitive, the acoustic signal); `ma-ki` = water. `ma-ki-so` = water's sound, where the head is the acoustic event and water is its source modifier. Contrast `so-ma-ki` (which would have `ma-ki` as head = auditory-water, wrong direction). The form `ma-ki-so` is right: it is a sound, of water.

This is compositional; no W-number required. First attested S468.

### The kireji `や` — `/` or `:` ?

The kireji `ya` has been translated into English as:
- A dash: "old pond — a frog jumps in" (most common)
- Nothing: just a line break (weakest)
- "and": "old pond and a frog jumps" (adds causality that isn't there)
- "where": "old pond, where a frog jumps" (makes it a relative clause — wrong)
- Ellipsis: "old pond..." (trailing off — wrong direction; the poem moves forward)

No English solution is correct because English has no structural mark that means: *I am presenting these two images as formally paired without specifying their relationship; hold both in mind simultaneously and let the resonance arise*.

Tonesu has two candidates:

| Mark | Function | What it does with the haiku |
|------|----------|-----------------------------|
| `/` | parallel partition | Signals co-equal structural pairing between two clauses; does not specify the relationship type; content supplies it | The pond and the event are presented as formally paired, co-equal images; their relationship (the contrast of stillness and motion, age and moment) arises from content |
| `:` | topic frame | Establishes the left-side noun phrase as the thematic anchor of the following clause | The pond is presented as the setting/context within which the event occurs; the event is a comment about the pond |

**These are not the same reading of the haiku.**

The `/` reading says: two co-equal images held in juxtaposition — the pond is not *more* than the event; both are equal partners in the resonance. This is the Bashō-as-Zen reading: the poem presents two equally weighted moments of consciousness.

The `:` reading says: the pond is the thematic anchor; the frog and sound are what happen against it — foreground/background. This is the Bashō-as-painter reading: the pond is the canvas; the frog is the mark on it.

**The finding:** Tonesu forces this choice, exposing the interpretive fork that Japanese `ya` keeps open. Both S468 (using `/`) and S469 (using `:`) are valid Tonesu renderings — they encode different critical readings of the same poem. The language is more precise than the source on this axis. Whether that precision is a gain or a loss depends on whether you think a poem should commit to its interpretation or remain open.

### Agent-drop and the final clause

In Japanese line 3, there is no verb and no subject. `水の音` is three particles: water + genitive + sound. Tonesu requires a predicate. Options:

1. `ma-ki-so pa` = water-sound exists/occurs — minimal; `pa` is the existential predicate; says only that the sound is present
2. `se lo-ma-ki-so` = perceiving water-sound — names an act of perception, but invents a perceiver (even an implicit one)
3. `ma-ki-so` alone — ungrammatical in Tonesu (no predicate); but if haiku as a genre were established as a no-predicate form, the genre itself supplies the implied `pa`

S468 and S469 use `ma-ki-so pa`. The existential `pa` is the lightest predicate available — it says "this sound exists" without attributing it to a perceiver or a cause. This preserves the impersonal quality of the source.

**Gap BSH-002:** Tonesu cannot match Japanese's zero-predicate noun-sentence for this line. The existential `pa` is the minimum; it slightly increases the semantic content of "water's sound" by asserting existence rather than simply naming. This is a real translation loss.

---

## Verse-by-Verse Analysis

### S468 — Full haiku — kireji as `/` parallel partition (BSH-001-A)

```
re-fe-ma-ki  /  la-zo-se-ma  ki  lo-re-fe-ma-ki,  ma-ki-so  pa
```

**Written:** `refemaki / lazosema ki lorefemaki, makiso pa`

**Parse:**
- `re-fe-ma-ki` = old pond — the left image
- `/` = kireji: parallel partition; co-equal structural pairing
- `la-zo-se-ma` = the aquatic-vertebrate / frog (agent)
- `ki` = moves / enters (physical motion, `ki` = displacement)
- `lo-re-fe-ma-ki` = patient: the old pond (into which the frog moves)
- `,` = prosodic pause separating the action from the result
- `ma-ki-so pa` = water-sound exists

**Reading:** The pond and the event are co-equal partners in the poem. The structural pairing (`/`) presents them without subordinating either. The relation between them — stillness punctuated by motion, age punctuated by instantaneous presence — is left for the reader to supply. The poem is a juxtaposition, not a sentence with a subject and a predicate.

**Note on pond repetition:** `re-fe-ma-ki` appears both in line 1 (as left image of the `/` pairing) and as `lo-re-fe-ma-ki` in line 2 (patient of the frog's motion). Japanese avoids this: `furuike` in line 1, then `tobikomu` in line 2 (the pond is implied — the frog jumps *in*; no explicit second mention). Tonesu has no discourse-anaphora for established referents — the full compound must repeat. This is GAP-BSH-003: no pro-form for recently-established discourse referents. The repeated compound is slightly more redundant than the source.

### S469 — Full haiku — kireji as `:` topic frame (BSH-001-B)

```
re-fe-ma-ki  :  la-zo-se-ma  ki  lo-re-fe-ma-ki,  ma-ki-so  pa
```

**Written:** `refemaki : lazosema ki lorefemaki, makiso pa`

Identical except `/` is replaced by `:`. The topic frame makes the old pond the thematic anchor: "as for the old pond — the frog enters, water-sound occurs." The pond is no longer a co-equal image; it is the stage setting. The event is a comment *about* the pond: this is what happens here, in this enduring place.

This reading is more temporal: the old pond persists; the frog's leap is a momentary event against that persistence. The deep/present contrast is foregrounded. Many Zen readings of the haiku favour this structure — the sound is not just a sound; it is what the pond *receives* in this moment.

**Structural note:** `:` requires sentence-initial position. `re-fe-ma-ki :` is sentence-initial, so this is valid. No parse conflict.

### S470 — Compressed form — agent suppressed (BSH-001-C)

```
re-fe-ma-ki  :  ki  lo-ma-ki,  ma-ki-so  pa
```

**Written:** `refemaki : ki lomaki, makiso pa`

The most minimal rendering. Agent (`la-zo-se-ma`) is dropped — the frog disappears as a named entity; only the motion event remains. `lo-ma-ki` substitutes for `lo-re-fe-ma-ki` — the patient is simply "the water" (not the full old-pond compound), dropping the `re` (age) and `fe` (boundary) modifiers. The final line is unchanged.

**What this achieves:** The haiku's spirit without the frog's identity. The motion event `ki lo-ma-ki` = motion into water is pure event, not animal-event. This is closest to Bashō's most radical reading — some commentators say the frog is almost irrelevant; what matters is the sound that follows. The agent-dropped form makes the frog's absence structural.

**What it loses:** The frog is actually *in the poem* — `kawazu` is not grammatically absent in Japanese; the agent who performs `tobikomu` is explicitly named. S470 removes that. This is a compression beyond what the source licenses. S468 or S469 are the primary translations; S470 is an exploratory variant.

**Grammatical note:** `ki lo-ma-ki` without `la-{agent}` — is this licensed? **GAP-BSH-004 — Resolved.** Grammar §Ellipsis Pattern 3 (context drop) licenses omission of any argument when fully recoverable from discourse context. Within the BSH-001 batch, `zo-se-ma` (the frog) is explicitly established as agent in S468 and S469; agent drop in S470 is discourse-licensed. In a standalone reading, the agent is scene-recoverable (pond + motion + sound evoking the frog). S470 remains an exploratory compression beyond what the source licenses (Japanese names the frog explicitly); the grammar is not violated, but the translator's choice to omit it goes further than the original.

---

## BSH-001 Translation Comparison

| S | Kireji | Agent | Old pond | Sound |
|---|--------|-------|----------|-------|
| S468 | `/` (co-equal) | `la-zo-se-ma` explicit | `re-fe-ma-ki` × 2 | `ma-ki-so pa` |
| S469 | `:` (topic anchor) | `la-zo-se-ma` explicit | `re-fe-ma-ki` × 2 | `ma-ki-so pa` |
| S470 | `:` (topic anchor) | dropped | `re-fe-ma-ki` + `lo-ma-ki` | `ma-ki-so pa` |

---

## BSH-001 Batch Summary

| Entry | Form | Test |
|-------|------|------|
| S468 (BSH-001-A) | `refemaki / lazosema ki lorefemaki, makiso pa` | kireji as `/`; co-equal juxtaposition; Bashō-as-Zen reading |
| S469 (BSH-001-B) | `refemaki : lazosema ki lorefemaki, makiso pa` | kireji as `:`; topic anchor; Bashō-as-painter reading |
| S470 (BSH-001-C) | `refemaki : ki lomaki, makiso pa` | agent-dropped maximum compression; event-without-actor |

**Key finding:** Tonesu exposes the 340-year critical debate about `ya` as a structural choice between two available marks. The `/` reading (co-equal juxtaposition) and the `:` reading (topic anchor / foreground-background) encode genuinely different interpretive stances on the poem. Japanese `ya` refuses to make this choice; Tonesu cannot avoid it. This is the clearest case yet where Tonesu's greater structural precision is simultaneously a gain (it clarifies what the interpretive options actually are) and a loss (it commits the translator where the poet chose not to).

**The language comparison:** Japanese's richest poetic tool is the *suppression* of grammatical structure — kireji, zero-particles, unpredicated noun-phrases — creating resonance through what is not said. Tonesu's design philosophy is the *explicit articulation* of structure. The haiku tests whether an analytically-explicit language can express a poem built entirely on structural withholding. The answer: partly. S468 and S469 are good translations; neither is a haiku.

**New vocabulary introduced:**
- `re-fe-ma-ki` (old pond; compound; first attested S468)
- `ma-ki-so` (water-sound; compound; first attested S468)

**Open questions logged:**
- **GAP-BSH-001**: no registered frog compound; `zo-se-ma` (aquatic-vertebrate) used by contextual disambiguation; a proper discriminator sub-node should be established in kinds.md when frog-reference recurs
- **GAP-BSH-002**: Tonesu cannot produce a zero-predicate noun-sentence; `pa` (existential) is the minimum addition; this is a structurally unavoidable translation loss
- **GAP-BSH-003**: no discourse-anaphora pronoun for recently-established referents; `re-fe-ma-ki` must be spelled out twice; this inflates compound length
- **GAP-BSH-004**: ~~agent-drop for pure motion-event clauses — is `ki lo-X` without `la-{agent}` grammatical? S470 tests the limit; not yet resolved~~ **Resolved (March 2026):** Grammar §Ellipsis Pattern 3 licenses agent drop when fully context-recoverable. In the batch `zo-se-ma` is established in S468/S469; S470's drop is discourse-licensed. The compression beyond source is a translator's choice, not a grammar violation.
