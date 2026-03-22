---
batch_codes: [JAB]
---
# Translation Test: Jabberwocky

## Source
Lewis Carroll, *Through the Looking-Glass, and What Alice Found There* (1871). Stanzas I, II, VI, VII (selected). Text is public domain.

## Status
Draft — first pass (JAB-001)

---

## Purpose

Carroll's Jabberwocky is the canonical stress test for any language's handling of **nonce vocabulary**: the poem's nouns, verbs, and adjectives lack semantic content yet the deep grammatical structure is fully transparent. Importing Jabberwocky into Tonesu tests:

1. **`""` quotation/mention frame under genuine nonce-vocabulary pressure** — the most extensive multi-sentence workout of the probationary `""` frame yet. Every nonce token (slithy toves, wabe, borogoves, outgrabe, Jabberwock, vorpal, snicker-snack, frabjous, Callooh, Callay) must be imported as-is without semantic translation.

2. **`~` in concept-approximation mode** — the `~` spec allows "approximately / something like," and this batch extends it to *concept approximation* for Carroll terms with partial semantic mappability: brillig ≈ `~ha-lu-ti`, gyre ≈ `~ki-re`, mimsy ≈ `~fa-de`, galumph ≈ `~ki-be-ra`, chortle ≈ `~so-fa-vo`. No new design question needed; the "something like" reading is spec-valid.

3. **Role-particle + quoted token** — `la-"X"` (agent role on quoted noun-phrase), `lo-na-"X"` (patient with kind-term citation), `a-"X"` (universal scope over quoted noun), `fe lo-na-"X"` (guard-from warning with nonce creature).

4. **`na-"X"` for nonce creature proper names** — the `na` kind-term partitioner extended to Carroll-style nonce creatures: `na-"Jabberwock"`, `na-"Jubjub bird"`, `na-"frumious Bandersnatch"`. Parallel to the `la-Yahweh`, `la-Elohim` pattern for proper names, but with `""` frame because these have no semantic content to admit directly.

5. **`so-"X"` onomatopoeia import** — `so` (acoustic-signal primitive) + quoted token = first attestation of importable onomatopoeia: `so-"snicker-snack"`.

6. **`fe` as imperative warning particle** — `fe lo-na-"X"!` = "guard your boundary from X!" = beware. First explicit warning-imperative use of the `fe` primitive.

Primary tests:

- `""` frame under mass nonce-vocabulary load (10+ distinct quoted tokens in one batch)
- `~[compound]` concept-approximation: translating partially-mappable Carroll terms without inventing new primitives
- `la-"X"` / `lo-na-"X"` / `a-"X"` role-particles applied to quoted tokens

Secondary tests:

- `na-li-be-mi` = my child / my son; kind-term + W033 + possessive suffix
- Digit cadence `bol, bun!` = "One, two!" in combat rhythm
- `[de-zo]` secondary result-state predicate in `;`-chained clause
- `go-si fa-vo` = in-the-manner-of happiness = joyfully (extending `go-si` manner function from ISA-001 S757)

Corpus sentences: S759–S764

---

## Vocabulary Framework

Most Carroll terms are imported verbatim inside `""`. New compositional forms:

| Form | Reading | Notes |
|------|---------|-------|
| `~ha-lu-ti` | approximately [warm-daytime] | concept-approx for "brillig" (late-afternoon broiling-hour). `ha` (heat) + `lu-ti` (W140, daytime). Under `~`: "something like warm daytime" |
| `~ki-re` | approximately [cyclic motion] | concept-approx for "gyre." `ki` (motion) + `re` (repetition/cycle) = cyclic/revolving motion. Under `~`: "something like spiralling" |
| `~fa-de` | approximately [affect-decrease] | concept-approx for "mimsy." `fa-de` (W094, affect-fading) used in concept-approx mode: "something like dejected or diminished" |
| `zo-mu` | living-device; organic tool | bodily biological instrument — jaw-like. `zo` (organism) + `mu` (artifact/device). Head-final: `zo-(mu)` = organism [device] = biological tool. First use |
| `ra-mu` | force-device; instrument of force | weapon/claw/blade. `ra` (energy/force) + `mu` (device). Head-final: `ra-(mu)` = force [device] = power-applying tool. First use |
| `ka-ki-fe` | deliberate motion through boundary; cut through | `ka` (intentional action) + `ki` (motion) + `fe` (boundary). Right-branching: `ka-(ki-fe)` = intentional [motion-boundary-crossing] = to cut through. First use |
| `pa-be` | upper-space; above-place | upward/head-region. `pa` (place/space) + `be` (growth/upward direction). Head-final: `pa-(be)` = place [of growth] = upward zone. First use as body-part reference |
| `~ki-be-ra` | approximately [motion-growth-force] | concept-approx for "galumph." `ki` (motion) + `be` (growth/increase) + `ra` (force/energy) = forceful building motion. Under `~`: "something like powerful tromping motion" |
| `~so-fa-vo` | approximately [sound-happiness] | concept-approx for "chortle." `so` (acoustic signal) + `fa-vo` (W197, happiness/positive-affect). Under `~`: "something like a sound of joy." First use of `so` + affect-compound |

Quoted tokens imported as-is (no translation): `"slithy toves"`, `"wabe"`, `"borogoves"`, `"gimble"`, `"outgrabe"`, `"mome raths"`, `"Jabberwock"`, `"Jubjub bird"`, `"frumious Bandersnatch"`, `"vorpal"`, `"snicker-snack"`, `"frabjous"`, `"Callooh"`, `"Callay"`.

---

## Source Text

> 'Twas brillig, and the slithy toves
> Did gyre and gimble in the wabe;
> All mimsy were the borogoves,
> And the mome raths outgrabe.
>
> "Beware the Jabberwock, my son!
> The jaws that bite, the claws that catch!
> Beware the Jubjub bird, and shun
> The frumious Bandersnatch!"
>
> *(Stanzas III–V omitted — the hunt.)*
>
> One, two! One, two! And through and through
> The vorpal blade went snicker-snack!
> He left it dead, and with its head
> He came galumphing back.
>
> "And hast thou slain the Jabberwock?
> Come to my arms, my beamish boy!
> O frabjous day! Callooh! Callay!"
> He chortled in his joy.

*(Lewis Carroll, "Jabberwocky," Through the Looking-Glass, 1871 — public domain)*

---

## Verse-by-Verse Analysis

### S759 — JAB-001-A — Stanza I, ll. 1–2

**Source:** "'Twas brillig, and the slithy toves / Did gyre and gimble in the wabe;"

**Tonesu:** `ta {~ha-lu-ti} : la-"slithy toves" ka-~ki-re lo-"wabe" / la-"slithy toves" ka-"gimble" lo-"wabe"`

**Written:** `ta {~haluti} : la"slithy toves" ka~kire lo"wabe" / la"slithy toves" ka"gimble" lo"wabe"`

**Gloss:** at [approximately warm-daytime] : [slithy-toves] cyclically-circled [around-wabe] / [slithy-toves] gimbled [around-wabe]

**Natural reading:** At something like the warm afternoon hour: the slithy toves circled in the wabe / the slithy toves gimbled in the wabe.

**Notes:** `ta {~ha-lu-ti}` = temporal frame: "at the time that is approximately warm-daytime." Carroll's "brillig" = "the time of broiling things for dinner" (4–5pm); `~ha-lu-ti` captures the warm-afternoon character without claiming exact semantic equivalence. `~` reads as "something like" — the spec-valid concept-approximation reading.

`la-"slithy toves"` = agent role marker applied to a quoted noun-phrase. The nonce compound "slithy toves" is imported verbatim inside `""`. The `la-` attaches without hyphen in written form: `la"slithy toves"`. This is the first attestation of role-particles applied directly to quoted tokens — structurally parallel to `la-Yahweh` and `la-Elohim` (proper names used without `""` because they have admitted semantic anchoring), but with `""` frame because the Carrollian tokens carry no Tonesu semantics.

`ka-~ki-re` = deliberate approximately-cyclic motion = to gyre. `~` qualifies `ki-re` (cyclic motion) as the concept-approximate head of the action. Written: `ka~kire`. Note: `ka-` prefix applies to the whole `~ki-re` concept-approximate compound.

`/` = bi-clausal parallel: two actions in the same temporal frame with the same agent. The structural parallelism mirrors Carroll's couplet structure. `ka-"gimble"` = deliberate-gimbling — the nonce verb is quoted as an action-label and prefixed with `ka-` for intentional-action marking.

---

### S760 — JAB-001-B — Stanza I, ll. 3–4

**Source:** "All mimsy were the borogoves, / And the mome raths outgrabe."

**Tonesu:** `a-"borogoves" ne ~fa-de ; la-"mome raths" "outgrabe"`

**Written:** `a"borogoves" ne ~fade ; la"mome raths" "outgrabe"`

**Gloss:** all-[borogoves] have-property approximately-affect-decrease ; [mome-raths] outgrabe

**Natural reading:** All borogoves are something like diminished/miserable; the mome raths outgrabe.

**Notes:** `a-"borogoves"` = V-prefix universal scope (`a-`) applied to a quoted noun: "all instances of whatever borogoves are." Written: `a"borogoves"`. This is the first attestation of the `a-` scope-prefix on a quoted token. The universal scope is clearly the intended Carrollian reading ("all mimsy were the borogoves" = it is a universal property of borogoves).

`ne ~fa-de` = copula + concept-approximate property: "has the property of approximately diminished-affect." Carroll's "mimsy" = "flimsy and miserable." `~fa-de` = something like affect-fading = approximately dejected/diminished-state. `fa-de` (W094) is already registered; `~fa-de` in concept-approximation mode is a new structural use. The `~` applies to the property compound, not to the copula.

`;` connector: the first clause predicts a universal property of borogoves; the second records the mome raths' action. Carroll treats these as parallel observations of the same scene. The `;` = sequential connector (constant conjunction without mechanism) correctly marks this.

`la-"mome raths"` = agent role on quoted plural noun-phrase. `"outgrabe"` = bare quoted verb-token in predicate position: "the mome raths did their outgrabing." No `ka-` prefix because `"outgrabe"` is already past-completed in Carroll (the original verb form is specifically "outgrabe"), and quoting it verbatim preserves that marking. First instance of a quoted form occupying the verbal slot without `ka-` or particle framing.

---

### S761 — JAB-001-C — Stanza II (full warning)

**Source:** "Beware the Jabberwock, my son! / The jaws that bite, the claws that catch! / Beware the Jubjub bird, and shun / The frumious Bandersnatch!"

**Tonesu:** `he na-li-be-mi! fe lo-na-"Jabberwock"! — [ka-ra-de] zo-mu ; [ka-ko] ra-mu — / fe lo-na-"Jubjub bird"! / fe lo-na-"frumious Bandersnatch"!`

**Written:** `he nalibemi! fe lona"Jabberwock"! — [karade] zomu ; [kako] ramu — / fe lona"Jubjub bird"! / fe lona"frumious Bandersnatch"!`

**Gloss:** [vocative my-child]! guard-boundary [Jabberwock]! — [biting] organism-tool ; [catching] force-tool — / guard-boundary [Jubjub-bird]! / guard-boundary [frumious-Bandersnatch]!

**Natural reading:** My son! Beware the Jabberwock! — the biting jaws; the grasping claws — beware the Jubjub bird! Beware the frumious Bandersnatch!

**Notes:** `he na-li-be-mi!` = vocative call: `he` (G029, vocative particle) + `na-li-be-mi` (kind-term-my-child). `li-be` (W033) = child, person in growth. `mi` = first-person possessive suffix. `na-` = kind-term prefix (from naming spec). Full construction: `na-[li-be-mi]` = the kind-of-growing-person-that-is-mine = my son/offspring. ✓

`fe lo-na-"Jabberwock"!` = **imperative warning.** `fe` = boundary/limit (primitive CV root). First use as explicit imperative: "boundary toward the Jabberwock!" = "maintain your boundary from the Jabberwock!" = beware. This is a pragmatic extension of `fe` as a boundary-marking imperative: "fe lo-X" = "apply a boundary toward X" = "guard yourself from X." `na-"Jabberwock"` = kind-term citation for the nonce creature: whatever kind of thing a Jabberwock is. `lo-na-"Jabberwock"` = patient-marked kind-citation: the Jabberwock that is the object of the warning.

`— [ka-ra-de] zo-mu ; [ka-ko] ra-mu —` = prosodic suspension frames enclosing a parenthetical identification of the Jabberwock's instruments. `[ka-ra-de]` = the-striking modifier-clause = biting; `zo-mu` = organism-device = biological tool = jaws. `[ka-ko]` = the-containing modifier-clause = grasping; `ra-mu` = force-device = power-applying instrument = claws. Both `zo-mu` and `ra-mu` are first uses. The `—` marks (G028, el) suspend the parenthetical within the larger sentence. The `;` between the two suspended instruments marks them as parallel fragments.

`/` = bi-clausal parallel partition between the three warning units. `fe lo-na-"Jubjub bird"!` and `fe lo-na-"frumious Bandersnatch"!` extend the same pattern. `na-"frumious Bandersnatch"` includes the Carrollian adjective inside the quoted name: the full nonce-compound "frumious Bandersnatch" is the creature's identifier.

---

### S762 — JAB-001-D — Stanza VI, ll. 1–2

**Source:** "One, two! One, two! And through and through / The vorpal blade went snicker-snack!"

**Tonesu:** `bol, bun! bol, bun! la-"vorpal" ra-mu ka-ki-fe lo-na-"Jabberwock" — so-"snicker-snack"!`

**Written:** `bol, bun! bol, bun! la"vorpal" ramu kakife lona"Jabberwock" — so"snicker-snack"!`

**Gloss:** one, two! one, two! [vorpal force-tool] cut-through [Jabberwock] — sound-[snicker-snack]!

**Natural reading:** One, two! One, two! The vorpal blade cut through the Jabberwock — snicker-snack!

**Notes:** `bol, bun! bol, bun!` = digits as cadence. `bol` = 1, `bun` = 2 (digit inventory, grammar spec). The comma-separated pair with `!` puntuates the combat rhythm: "one, two / strike." Repeated twice for the double-pass of Carroll's blade.

`la-"vorpal" ra-mu` = the vorpal force-tool; the vorpal blade. `"vorpal"` is a quoted modifier pre-positioned before the head noun `ra-mu` (modifier precedes head, right-branching). `la-` = agent role-marker applied to the NP `"vorpal" ra-mu`. `ra-mu` = force-device = first use. Written: `la"vorpal" ramu`. The pre-NP quoted adjective pattern mirrors established modifier-head order; quotes do not disrupt the syntactic structure.

`ka-ki-fe lo-na-"Jabberwock"` = the blade cut through the Jabberwock. `ka-ki-fe` = deliberate-motion-through-boundary = to cut through: `ka` (intentional) + `ki` (motion) + `fe` (boundary) right-branching as `ka-(ki-fe)` = intentional [motion-through-boundary]. First use. Patient: `lo-na-"Jabberwock"` = the Jabberwock.

`— so-"snicker-snack"!` = prosodic suspension marker then the onomatopoeic event. **First attestation of `so-"X"` onomatopoeia import strategy.** `so` (acoustic signal, primitive) + `""` frame = the sound whose name is "snicker-snack." The compound `so-"snicker-snack"` imports the phonetic token verbatim as the name of the sound it represents. Note: the hyphen inside `"snicker-snack"` is English punctuation, not a Tonesu morpheme boundary — it is preserved inside quotes in written form: `so"snicker-snack"`.

---

### S763 — JAB-001-E — Stanza VI, ll. 3–4

**Source:** "He left it dead, and with its head / He came galumphing back."

**Tonesu:** `ta ti-de : la-zo-li ka-ne-de lo-na-"Jabberwock" [de-zo] ; la-zo-li ka-~ki-be-ra [ko lo-pa-be lo-na-"Jabberwock"]`

**Written:** `ta tide : lazoli kanede lona"Jabberwock" [dezo] ; lazoli ka~kibera [ko lopabe lona"Jabberwock"]`

**Gloss:** at past-time : [hero] severed-from [Jabberwock] [in-dead-state] ; [hero] approximately-powerfully-galumphed [while-containing upper-space of-[Jabberwock]]

**Natural reading:** At that past moment: the hero left the Jabberwock (in its dead state) behind; and galumphed back carrying the Jabberwock's head.

**Notes:** `ta ti-de :` = temporal frame: "at past time." `ti-de` = W041, time-decay = past. The `:` topic frame introduces the narrative moment: "as for that past moment, [what happened]."

`ka-ne-de` (W092) = deliberate bond dissolution = to sever, leave behind. The hero cut the connection to the Jabberwock and moved on. Patient: `lo-na-"Jabberwock"`.

`[de-zo]` = result-state secondary predicate: the Jabberwock is in a state of death (`de-zo` W178 = decay + organism = death/dying). The bracketed form marks it as a secondary predicate on the patient, not the primary verb — "he left it [in dead-state]." This extends the PAV-001 secondary predicate pattern to `;`-chained clauses.

`ka-~ki-be-ra` = deliberately do approximately-motion-growth-force = galumph. `ki-be-ra` right-branches as `ki-(be-ra)` = motion [of force-growth] = motion with increasing forceful energy = triumphant heavy-footed striding. Under `~`: "something like forceful lumbering motion" = galumph. `ka-` = intentional action. First use.

`[ko lo-pa-be lo-na-"Jabberwock"]` = secondary bracketed clause: "while containing the upper-space of the Jabberwock." `ko` = containment/carrying. `pa-be` = place-growth = upward-direction space = the highest spatial point of a body = the head. First use of `pa-be` as a body-part reference. **`pa-be` as anatomical proxy:** Tonesu has no body-part lexicon; `pa-be` (upward zone of place) maps compositionally to "the top part of a body" = the head. This follows the established pattern of using positional vocabulary for body-part reference (cf. `lo-pa-be lo-na-X` = the upper-space belonging to X = X's head). `lo-na-"Jabberwock"` = genitive: the Jabberwock's. Combined: the upper-space of the Jabberwock = the Jabberwock's head.

---

### S764 — JAB-001-F — Stanza VII, ll. 3–4

**Source:** "'O frabjous day! Callooh! Callay!' / He chortled in his joy."

**Tonesu:** `ya, "frabjous"! "Callooh"! "Callay"! la-zo-li ~so-fa-vo go-si fa-vo ti-de`

**Written:** `ya, "frabjous"! "Callooh"! "Callay"! lazoli ~sofavo gosi favo tide`

**Gloss:** [attention] [frabjous]! [Callooh]! [Callay]! [hero] approximately-joy-sound in-manner-of happiness past-time

**Natural reading:** Frabjous! Callooh! Callay! And the hero made a joyful noise — he chortled in his happiness.

**Notes:** `ya,` = attention-signal (established grammar particle, `ya` + comma for clause-initial position). Opens the exclamatory section: "attend to this: [frabjous]!" Without asserting any emotional state on the speaker — `ya` is a grammatical attention marker, not an affect claim.

`"frabjous"!`, `"Callooh"!`, `"Callay"!` = bare quoted exclamations. These are Carroll's invented sounds of joy, imported verbatim. They occupy an exclamatory-nominal position: not subjects, verbs, or predicates in the Tonesu sense — they are quoted tokens used in utterance-position to register the joyful noises. The `!` applies to each quoted token individually.

`la-zo-li ~so-fa-vo` = the hero made approximately-joy-sound. `~so-fa-vo` = approximately [sound-happiness]: `so` (acoustic signal, primitive) + `fa-vo` (W197, happiness). The concept-approximate: "something like a sound of positive affect" = a laugh, a chuckle, a chortle. Carroll coined "chortle" as a portmanteau of "chuckle" + "snort" — the approximation is intentional. First use of `so` + affect-compound as onomatopoeia strategy.

`go-si fa-vo` = in the manner of happiness = joyfully. Extends `go-si` in manner/comparison function (first attested ISA-001 S757). `fa-vo` (W197) = happiness/positive-affect. The manner phrase describes the mode of the chortling: performed with the character of happiness.

`ti-de` = W041, past time. The chortle occurred at a completed past moment.

---

## JAB-001 Batch Summary

| Entry | Tonesu | Written | Claim | Key feature |
|-------|--------|---------|-------|-------------|
| S759 (JAB-001-A) | `ta {~ha-lu-ti} : la-"slithy toves" ka-~ki-re lo-"wabe" / la-"slithy toves" ka-"gimble" lo-"wabe"` | `ta {~haluti} : la"slithy toves" ka~kire lo"wabe" / la"slithy toves" ka"gimble" lo"wabe"` | At brillig-time, the slithy toves gyred and gimbled in the wabe | Temporal `ta {}` + `~ha-lu-ti` concept-approx for "brillig"; `la-"X"` first attestation; `~ki-re` gyre |
| S760 (JAB-001-B) | `a-"borogoves" ne ~fa-de ; la-"mome raths" "outgrabe"` | `a"borogoves" ne ~fade ; la"mome raths" "outgrabe"` | All borogoves were mimsy; mome raths outgrabe | `a-"X"` universal-on-quoted-noun; `ne ~fa-de` concept-approx copula predicate; bare quoted verb |
| S761 (JAB-001-C) | `he na-li-be-mi! fe lo-na-"Jabberwock"! — [ka-ra-de] zo-mu ; [ka-ko] ra-mu — / fe lo-na-"Jubjub bird"! / fe lo-na-"frumious Bandersnatch"!` | `he nalibemi! fe lona"Jabberwock"! — [karade] zomu ; [kako] ramu — / fe lona"Jubjub bird"! / fe lona"frumious Bandersnatch"!` | Beware the Jabberwock, my son! — jaws; claws — beware the Jubjub bird, beware the Bandersnatch | `fe lo-na-"X"` warning imperative; `zo-mu`, `ra-mu` first uses; `na-"X"` creature citation triple |
| S762 (JAB-001-D) | `bol, bun! bol, bun! la-"vorpal" ra-mu ka-ki-fe lo-na-"Jabberwock" — so-"snicker-snack"!` | `bol, bun! bol, bun! la"vorpal" ramu kakife lona"Jabberwock" — so"snicker-snack"!` | One, two! The vorpal blade cut through the Jabberwock — snicker-snack! | Digit cadence; `ra-mu` first use; `ka-ki-fe` cut-through first use; `so-"X"` onomatopoeia first use |
| S763 (JAB-001-E) | `ta ti-de : la-zo-li ka-ne-de lo-na-"Jabberwock" [de-zo] ; la-zo-li ka-~ki-be-ra [ko lo-pa-be lo-na-"Jabberwock"]` | `ta tide : lazoli kanede lona"Jabberwock" [dezo] ; lazoli ka~kibera [ko lopabe lona"Jabberwock"]` | He left the Jabberwock dead and came galumphing back with its head | `[de-zo]` result-state secondary predicate; `~ki-be-ra` galumph concept-approx; `pa-be` head as upper-space first use |
| S764 (JAB-001-F) | `ya, "frabjous"! "Callooh"! "Callay"! la-zo-li ~so-fa-vo go-si fa-vo ti-de` | `ya, "frabjous"! "Callooh"! "Callay"! lazoli ~sofavo gosi favo tide` | Frabjous! Callooh! Callay! He chortled in his joy | `ya` attention + bare quoted exclamations; `~so-fa-vo` chortle concept-approx; `go-si fa-vo` = joyfully |

**New vocabulary:** none (all forms compositional or quoted imports).

**Compositional first uses:** `zo-mu` (organism-device; jaw/biological tool); `ra-mu` (force-device; claw/blade); `ka-ki-fe` (cut through, deliberate motion through boundary); `pa-be` (upper-space; head-region); `ki-re` (cyclic motion, under `~`); `ki-be-ra` (motion-growth-force, under `~`); `so-fa-vo` (sound-happiness, under `~`).

**Open questions logged:** none (all structural gaps previously logged; `""` frame performance noted as first major stress test).

---

## Structural Findings

### 1. `""` frame under nonce-vocabulary pressure — stress test passed

JAB-001 imports 14 Carroll tokens verbatim inside `""`. The frame holds under mass load. Key structural pattern confirmed: the `""` frame acts as a transparent import sleeve — the enclosed token is syntactically inert from Tonesu's perspective, and role-particles, scope-prefixes, and kind-term markers apply *outside* the quotes, wrapping the quoted NP as a unit:

```
Agent-role on quoted NP:       la-"slithy toves"     →  la"slithy toves"
Kind-term on quoted creature:  lo-na-"Jabberwock"    →  lona"Jabberwock"
Universal scope on quoted N:   a-"borogoves"         →  a"borogoves"
Sound root + quoted sound:     so-"snicker-snack"    →  so"snicker-snack"
Warning + kind-term citation:  fe lo-na-"Jabberwock" →  fe lona"Jabberwock"
```

The parse is never ambiguous: the structural role of the compound is carried by the Tonesu morpheme (the prefix or particle), and the quoted token is the semantic slot-filler. This confirms the `""` frame's composability.

### 2. `~[compound]` in concept-approximation mode

The `~` spec allows "approximately / roughly / on the order of / **something like**." JAB-001 extends `~` to *concept approximation* — approximating an untranslatable concept with the closest available compound:

| Carroll word | Tonesu concept-approx | Rationale |
|---|---|---|
| brillig | `~ha-lu-ti` | approximately [warm-daytime] = late-afternoon warmth |
| gyre | `~ki-re` | approximately [cyclic motion] = spiralling |
| mimsy | `~fa-de` | approximately [affect-decrease] = diminished/miserable |
| galumph | `~ki-be-ra` | approximately [motion-growth-force] = heavy triumphant tromping |
| chortle | `~so-fa-vo` | approximately [sound-happiness] = a joyful noise |

The `~` operator's "something like" reading is clean here: it hedges the translation without falsely asserting semantic identity. No new design question needed.

### 3. `fe` as imperative warning particle

`fe lo-na-"X"!` = "maintain your boundary from X!" = beware X. The `fe` primitive (boundary/limit/category edge) is extended to a pragmatic imperative: "apply boundary toward the following entity." This is compositionally transparent and parallels how the `fe` primitive anchors `ti-fe` (W037, time-limit = eternity), `fe-su` (W055, boundary structure = wall), and `ne-no-fe` (extreme forms). The warning imperative function (`fe lo-X!` = guard yourself from X) is new but derivable without invented particles.

### 4. `na-"X"` creature citation for nonce proper names

`na-"Jabberwock"`, `na-"Jubjub bird"`, `na-"frumious Bandersnatch"` each use `na` (kind-term partitioner, from naming spec) as a classifier for the nonce creature. The whole quoted string — adjective + noun — can be enclosed as a single named-kind identifier. This extends the naming convention naturally: `na-X` = "the kind of thing that is X." For nonce terms, `""` wraps X because it has no Tonesu semantic content. The pattern `na-"frumious Bandersnatch"` with a multi-word quoted identifier shows the `""` frame accepts multi-word tokens including internal adjectives without disambiguation problems.

### 5. `so-"X"` onomatopoeia import

`so-"snicker-snack"` = the sound named "snicker-snack." The `so` primitive (acoustic signal) acts as a classifier: "the sound whose name is X." This is the first attestation of `so` + `""` as an onomatopoeia strategy. The English hyphen inside `"snicker-snack"` is preserved in written form (it is English orthography, not a Tonesu morpheme boundary, and the `Written:` rule strips only Tonesu morpheme hyphens).

### 6. `pa-be` as anatomical proxy for "head"

Tonesu has no body-part lexicon. `pa-be` = place-growth = upward-space = the upper zone of a spatial region. Applied to an organism via `lo-na-"X"` genitive: `lo-pa-be lo-na-"Jabberwock"` = the upper-space of the Jabberwock = the Jabberwock's head. This is the first use of positional vocabulary as an anatomical proxy. The strategy is productive: `pa-de` (downward-place) = lower body; `pa-ko` (interior-space) = the body's inside. Potential for a systematic body-topology vocabulary built from spatial primitives.

---

## Colloquial Register Analysis

| Form used | CLQ entry | Colloquial form | Notes |
|-----------|-----------|-----------------|-------|
| `~ha-lu-ti` | none | — | Concept-approximate under `~` — `ha-lu-ti` is 3-root; below contraction threshold |
| `~ki-re` | none | — | Concept-approximate under `~` — 2-root; below threshold |
| `~fa-de` | none | — | `fa-de` W094 is 2-root; below threshold |
| `zo-mu` | none | — | 2-root — below threshold |
| `ra-mu` | none | — | 2-root — below threshold |
| `ka-ki-fe` | none | — | 3-root — below threshold |
| `pa-be` | none | — | 2-root — below threshold |
| `~ki-be-ra` | none | — | 3-root under `~`; below threshold |
| `~so-fa-vo` | none | — | `so` + `fa-vo`; 3-element under `~`; below threshold |
| `na-li-be-mi` | none | — | `na-` + W033 `li-be` + `-mi`; structural derivation, not a bare compound |
| `fe lo-na-"X"` | none | — | Pragmatic imperative construction — semantically load-bearing; relaxation changes the force |
| `go-si fa-vo` | none | — | `go-si` manner function — below threshold; function already established ISA-001 |
| Digit cadence `bol, bun!` | none | — | Primitive digit atoms — minimum possible |
| `""` quoted tokens (×14) | none | — | Import frame — outside CLQ scope by definition; tokens have no Tonesu semantic depth to compress |

**Verdict:** irreducibly formal — all forms are below threshold, structural load-bearing, or outside CLQ scope.

*CLQ entries registered from this batch: none.*
