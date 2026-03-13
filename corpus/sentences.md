# Example Sentences

## Status: Draft

This file is where the system gets tested. If a concept is hard to express, that signals a gap in the primitives, grammar, or word-formation rules — not a problem with the sentence.

---

## How to Use This File

Each sentence should include:
- **Gloss line:** morpheme-by-morpheme breakdown
- **Literal reading:** what the structure actually says
- **Natural reading:** intended meaning in English
- **Notes:** anything that felt awkward or required a workaround

---

## Sentence Structure Reminder

```
[agent marker] [agent]  [patient marker] [patient]  [action marker] [verb]  [time marker] [tense]
```

---

## Basic Sentences

---

**S001 — Simple action**

```
Gloss:    la-engineer  lo-machine  ka-build  ta-now
Literal:  agent:engineer  patient:machine  action:build  time:present
Natural:  The engineer builds the machine.
Notes:    Clean. No issues.
```

---

**S002 — Future action**

```
Gloss:    la-researcher  lo-knowledge-system  ka-improve  ta-future
Literal:  agent:researcher  patient:knowledge-system  action:improve  time:future
Natural:  The researcher will improve the knowledge system.
Notes:    "knowledge-system" = to-su (W030). Compound slots cleanly as patient NP.
```

---

**S003 — With instrument**

```
Gloss:    la-engineer  lo-machine  ro-tool  ka-build-now
Literal:  agent:engineer  patient:machine  instrument:tool  action:build-present
Natural:  The engineer builds the machine with a tool.
Notes:    Instrument particle is `ro` (no root `ro` exists — clean).
          Former `ra` instrument particle was renamed to `ro` because `ra` = energy/force root
          and the collision was non-transparent. Resolved. See spec/grammar.md particle policy.
```

---

**S004 — Negation**

```
Gloss:    la-engineer  lo-machine  ka-no-build  ta-past
Literal:  agent:engineer  patient:machine  action:NOT-build  time:past
Natural:  The engineer did not build the machine.
Notes:    Negation prefix on verb feels natural and compositional.
```

---

**S005 — Question**

```
Gloss:    la-engineer  lo-machine  ka-build-now  ?
Literal:  agent:engineer  patient:machine  action:build-present  [question]
Natural:  Is the engineer building the machine?
Notes:    Question particle at end feels readable. Distinguish from statement by particle alone.
```

---

**S006 — Location**

```
Gloss:    la-engineer  pa-workshop  ka-work  ta-now
Literal:  agent:engineer  location:workshop  action:work  time:present
Natural:  The engineer works in the workshop.
Notes:    "workshop" = build-pa (derivational form using D003). Satisfying derivation.
```

---

## More Complex Sentences

---

**S010 — Nested concept as object**

```
Gloss:    la-to-li  lo-[to-su-mu]  ka-design  ta-past
Literal:  agent:knower/scholar  patient:[knowledge-structure-device]  action:design  time:past
Natural:  The scholar designed the database.
Notes:    [to-su-mu] functions as a single NP. Nesting may need grouping markers in spoken form 
          to avoid ambiguity with the derivational suffix on to-su-mu.
```

---

**S011 — Causal relation**

```
Gloss:    go-ra-excess  du-machine-fail
Literal:  cause:energy-excess  result:machine-fail
Natural:  The machine failed because of excess energy.
Notes:    go/du as causal frame works conceptually. Sentence lacks explicit agent — acceptable?
          How does this interact with standard SOV order? Needs a grammar rule.
```

---

**S012 — Relational sentence**

```
Gloss:    la-na-Derik  ne-li-na-Mira  vo-close
Literal:  agent:person:Derik  relation:person:Mira  quality:close
Natural:  Derek and Mira have a close relationship.
Notes:    `ne` as relation marker here doubles as a grammatical particle. Needs review.
          "close" as a quality — is vo-close the right structure?
```

---

## Sentences to Attempt Next

*(Harder cases that will stress-test the system)*

- [ ] "The network failed to transmit the signal before the deadline." (time constraint + failure)
- [ ] "A scientist who studies living information patterns works at the institute." (relative clause)
- [ ] "Build me a system that remembers past queries." (imperative + relative clause + memory semantics)
- [ ] "This concept has no equivalent in the old language." (negation + abstract comparison)
- [ ] A full 3–4 sentence paragraph on a coherent topic

**Purpose-clause stress tests** *(require purpose-frame formalization — see spec/grammar.md)*
- [x] **P001** → attempted as **S018**. Same-agent confirmation; agent inheritance rule confirmed (4th data point). `to-su-ki` = comprehend. No surprises. See S018 notes.
- [x] **P002** → attempted as **S016**. Different-agent constraint confirmed; same-patient reduction provisionally valid. See S016 notes.
- [x] **P003** → attempted as **S017**. Default reading is same-agent; agent inheritance rule confirmed (3rd data point). See S017 notes.

**Relative-clause pressure test**
- [x] **P004** → attempted as **S019**. Compounding covers noun-naming but breaks for capability expression. Relativizer gap exposed. Imperative gap also exposed. See S019 notes.

---

## Stress-Test Translation

---

**S013 — Abstract causation / conditional**

*Target: "Knowledge grows when information connects."*

**Attempt 1 — Using `ta` as temporal subordinator:**

```
Gloss:    la-to  ka-be  ta [la-si  ka-ne-ki]
Literal:  agent:knowledge  action:grow  time [agent:signal  action:relate-motion]
Natural:  Knowledge grows at the time that information connects.
```

**Attempt 2 — Using `go` (cause) to frame the relationship — canonical form:**

```
Gloss:    go [la-si  ka-ne-ki]  la-to  ka-be
Literal:  cause [agent:signal  action:connect]  agent:knowledge  action:grow
Natural:  Because-of [signal connecting], knowledge grows.
```

**Notes:**
- **`la-to` is now clean.** With the agent particle renamed to `la`, abstract agents no longer collide with the person/agent root `li`. `la-to` = "agent: conceptual-pattern" unambiguously.
- **Attempt 2 is canonical.** The causal frame (`go`/`du`) naturally handles "when X, Y follows" without a dedicated conditional particle. Formalized in spec/grammar.md as the Causal Conditional structure.
- **`ne-ki` = connect** (relation + motion → become-related) is the first attested use of the inchoative pattern `ROOT + ki`, now formalized in spec/morphology.md.
- The original attempts were written before the `li`/`la` split — the old forms `li-to`/`li-si` are replaced above with canonical `la-to`/`la-si`.

**Verdict:** Primitives held. Both grammar gaps identified here are resolved:
1. ~~Particle/root collision for `li`~~ → resolved: agent particle renamed to `la`
2. ~~Inchoative derivation undefined~~ → resolved: `ROOT + ki` = enter state ROOT (spec/morphology.md)

---

**S014 — Agency, artifact, and purpose**

*Target: "People create tools to store information."*

```
Gloss:    la zo-li  lo si-ko-mu  ka-be
Literal:  agent:living-person  patient:signal-contain-artifact  action:generate
Natural:  People create information-storage artifacts.
```

**Notes:**
- `zo-li` = living-person: the natural compound for "people." With `la` as the unambiguous agent particle, `la zo-li` is clean — particle followed by root compound, no collision.
- `si-ko-mu` = signal + containment + artifact. Head-final rule: `mu` (artifact) is the head; characterized by containing (`ko`) signals (`si`). The purpose clause "to store information" is absorbed into the compound — the artifact's nature encodes its purpose.
- `ka-be` = action:generate/create. `be` (growth/creation) covers intentional fabrication at this stage.
- **Purpose clause absorbed by compounding:** Works here because purpose IS the artifact's nature. For external purpose — "She studies *to understand*", "He runs *to escape*" — a general purpose-clause structure is now formalized in spec/grammar.md: `wi [clause]` introduces the intended outcome. `wi` is a transparent overlap with root `wi` (will/intention).

**Gaps exposed:**
1. ~~**Purpose clauses**~~ → resolved: `wi [clause]` formalized in spec/grammar.md.
2. `si` (signal/representation) is carrying "information" in both S013 and S014. Confirm this is the right root vs. `to` (conceptual pattern) or `to+si` (encoded knowledge).

---

**S015 — Temporal frame**

*Target: "When they study, knowledge grows."*

```
Gloss:    ta [la-yu  ka-to-ki]  la-to  ka-be
Literal:  temporal [agent:group  action:learn-process]  agent:knowledge  action:grow
Natural:  When they study, knowledge grows.
```

**Notes:**
- **Boundary rule test (pass):** `ta` opens the subordinate clause `la-yu  ka-to-ki`. The matrix clause begins at `la-to` — the next matrix-level argument marker. The subordinate agent `la-yu` is already consumed, so `la-to` is unambiguously matrix-level. Boundary recovered without explicit delimiters. No new machinery needed for this case. ✓
- **`ta` vs `go` doing real work:** S013 used `go` to *assert causation* — "because information connects, knowledge grows." This sentence uses `ta` for temporal correlation only — "when studying happens, knowledge grows" — without claiming studying is the cause. The `ta`/`go` distinction is not cosmetic; the two frames make genuinely different claims.
- **`yu` first corpus appearance:** `la-yu` is the first gloss use of the renamed group pronoun. No collision with root `wi` (will/intention). Clean.
- **`to-ki`** = W020 (learning/computation/reasoning). "Study" is the deliberate human variant; `to-ki` covers it at this stage.

---

**S016 — Purpose frame, different agent** *(P002)*

*Target: "I built the machine for you to use."*

```
Gloss:    la-mi  ka-be-past  lo-mu  wi [la-tu  ka-mu-ka  lo-mu]
Literal:  agent:I  action:create-PAST  patient:machine  intention [agent:you  action:operate  patient:machine]
Natural:  I built the machine for you to use.
```

**Reduced form (same-patient candidate):**
```
la-mi  ka-be-past  lo-mu  wi [la-tu  ka-mu-ka]
```
*Purpose-clause patient omitted — recoverable from main-clause patient immediately preceding `wi`.*

**Notes:**
- **Boundary rule test (pass):** `wi` opens the purpose clause at `la-tu`. The clause extends to sentence end — no matrix-level marker follows; right edge is sentence termination. Boundary rule holds. ✓
- **Different-agent confirmed:** Main-clause agent is `mi` (I); purpose-clause agent is `tu` (you). `la-tu` must be explicit. Same-agent reduction does not apply. Spec constraint correct.
- **Same-patient reduction: provisionally valid.** `lo-mu` (patient:machine) appears in both clauses. The reduced form recovers the patient from the immediately preceding main-clause patient. Recovery is unambiguous in this configuration. First corpus evidence bearing on the open question from spec/grammar.md § Purpose Frame. Provisional verdict: same-patient reduction is valid when the shared patient is explicitly present in the main clause; update grammar spec accordingly.
- **`mu-ka`** (W022) = operate/use an artifact. Head-final: artifact (`mu`) specifies the action (`ka`). Registered in registry/derived.md. Placeholder `ka-use` retired.
- **`ka-be-past`:** tense marker is a placeholder gloss, consistent with current corpus convention.

---

**S017 — Purpose frame, same agent; warning semantics** *(P003)*

*Target: "She sent the message to warn them."*

**Reduced form (same-agent; canonical in practice):**
```
Gloss:    la-ze  lo-si  ka-si-ki-past  wi [ka-fe-si  ne-yu]
Literal:  agent:she  patient:signal  action:transmit-PAST  intention [action:warn  recipient:them]
Natural:  She sent the message to warn them.
```

**Canonical form (full agent explicit):**
```
la-ze  lo-si  ka-si-ki-past  wi [la-ze  ka-fe-si  ne-yu]
```
*Same as above; `la-ze` retained in purpose clause.*

**P003b — Evil variant (different agent, different recipient):**
```
Gloss:    la-ze  lo-si  ka-si-ki-past  wi [la-yu  ka-fe-si  ne-mi]
Literal:  agent:she  patient:signal  action:transmit-PAST  intention [agent:them  action:warn  recipient:us]
Natural:  She sent the message for them to warn us.
```
*`la-yu` explicit because purpose-clause agent (them) ≠ matrix agent (she). Same-agent reduction does not apply.*

**Notes:**
- **P003 is same-agent by default,** not different-agent. Plain English "warn them" has the sender as the warner; the message is the instrument, not an independent agent. This is a control property of the verb, not of the purpose-frame itself.
- **Agent inheritance rule (3rd confirmation):** purpose clause omits `la-ze` → matrix agent `ze` inherited unambiguously. See spec/grammar.md § Purpose Frame — rule now formally stated.
- **`ne` particle inside purpose clause:** `ne-yu` (recipient:them) appears inside the `wi` subordinate clause without issue. `ne` marks an argument within the clause; it is not a clause introducer and does not affect the boundary rule. Passes cleanly. ✓
- **Boundary rule (pass):** `wi` opens, purpose clause runs to sentence end. Same right-edge pattern as S016. ✓
- **P003b** exposes the genuinely different-agent case: `la-yu` required when purpose-clause agent ≠ matrix agent. Consistent with S016. The absence of an agent marker in a `wi` clause now has a confirmed, unambiguous interpretation: inherit the matrix agent.
- **Two new vocabulary items registered:** `si-ki` (W023) = send/transmit; `fe-si` (W024) = warn/alert. Both proposed-status.
- **`ka-si-ki-past` and `ka-fe-si`:** tense/aspect markers remain placeholder glosses.

---

**S018 — Purpose frame, same agent; comprehension** *(P001)*

*Target: "They study in order to comprehend."*

```
Gloss:    la-yu  ka-to-ki  wi [ka-to-su-ki]
Literal:  agent:group  action:process-knowledge  intention [action:comprehend]
Natural:  They study in order to comprehend.
```

**Notes:**
- **Agent inheritance rule (4th confirmation):** purpose clause omits `la-yu` → matrix agent `yu` inherited without ambiguity. Rule confirmed.
- **`to-su-ki` first corpus attestation:** W025 (to-su + inchoative `ki` = enter state of organized knowledge). The learning process (`to-ki`) + purpose marker (`wi`) + comprehension threshold (`to-su-ki`) encodes the full arc of understanding: ongoing process → arrival at organized grasping. The combination is productive.
- **`wi` same-agent reduction (confirmed):** no agent in purpose clause; matrix agent inherited. Consistent with S016 (different-agent), S017 (same-agent with warning semantics). Fourth confirmation.
- **P001 pass.** No new gaps.

---

**S019 — Compounding vs. relative clause; imperative** *(P004)*

*Target: "Build me a system that remembers past queries."*

**Version A — Noun compounding workaround (canonical form):**

```
Gloss:    lo-to-ko-mu  ne-mi  ka-be
Literal:  patient:memory-device  recipient:me  action:create
Natural:  Build me a memory device. (imperative: la-tu dropped)
```

**Version B — What you'd need to express the original (does not yet work):**

The target requires a noun modified by a verb clause: "[a device] [that] [remembers past queries]." Tonesu has no relativizer particle; the structure `lo-mu [REL:la-mu ka-to-ko-past-si] ne-mi ka-be` is not currently expressible.

**Notes:**
- **Imperative resolved:** `la-tu` drop formalized in spec/grammar.md § Imperatives: drop `la-tu`, all other markers remain. Version A above uses the canonical form. Note the SOV argument order is maintained — the agent slot is simply absent.
- **Relativizer gap confirmed:** "a system that remembers" requires a verbal relative clause; compounding handles this by encoding the capability in the noun itself. `to-ko-mu` (memory-containment-device) works for defining properties (the device IS a memory device) but cannot express incidental predication (a device that happened to already know something specific). Logged in notes/open-questions.md.
- **`to-ko-mu`** = memory device; formal compound of W027 (`to-ko`). Colloquial short form drops `-mu`; documented in spec/morphology.md.
- **P004 pass** (partial): imperative gap closed; relativizer remains open.

---

**S020 — Primitive validation: child drinks water** *(T021)*

*Target: "The child drinks water."*

```
Gloss:    la-li-be  lo-ma  ka-ko
Literal:  agent:young-person  patient:matter/water  action:contain/ingest
Natural:  The child drinks water.
```

**Notes:**
- **`li-be`** = growing-person / child. `li` (social agent) + `be` (growth) = person in their growth phase. Candidate W033; registered in registry/derived.md.
- **`ma` for water:** the primitives table notes "water is `ma`" in context. Here the sentence (a person ingesting substance) makes `ma` unambiguously water. Primitive `ma` validated for substance reference.
- **`ka-ko`** = action of containing = ingest / drink / take in. `ko` (containment) used as verbal root: the act of bringing a substance into containment within the body. First corpus use.
- **T021 pass.** Clean.

---

**S021 — Primitive validation: tool cuts wood** *(T022)*

*Target: "The tool cuts wood."*

```
Gloss:    ro-mu  lo-zo-ma  ka-fe
Literal:  instrument:artifact  patient:organic-matter  action:divide/cut
Natural:  With a tool, one cuts wood. / A tool cuts wood.
```

**Notes:**
- **Instrument-as-agent tension resolved:** English "the tool cuts" treats an artifact as a grammatical subject. Tonesu refuses this: `la` (agent) + `ka` (intentional action) requires a volitional agent. A tool is not volitional; it is an instrument (`ro`). The human user is a dropped/implied agent — see agentless clause open question. The English sentence is ontologically misleading. The Tonesu form is more accurate: the tool mediates the action, it does not perform it.
- **`zo-ma`** = organic-matter = wood / biological substance. `zo` (living organism) + `ma` (matter) = organic substance. Transparent compound; not registered separately.
- **`ka-fe`** = action of dividing / cutting / creating a boundary. `fe` (boundary) used as verbal root. First corpus use.
- **T022 pass** (with intentionality principle confirmed). Agentless-with-instrument construction noted; formal grammar rule pending.

---

**S022 — Primitive validation: star emits light** *(T023)*

*Target: "The star emits light."*

```
Gloss:    la-ra-su  lo-lu  be
Literal:  agent:energy-structure/star  patient:light  [grow/emit]
Natural:  The star emits light.
```

**Notes:**
- **Non-intentional production grammar:** bare `be` (not `ka-be`) marks non-intentional generation. First corpus use of `be` as a transitive verb without the `ka` action particle. The distinction is now doing grammatical work:
  - `ka-be` = deliberate creation (S014: people create tools)
  - `be` alone = natural emergence / non-intentional production (this sentence)
  `ka` is not obligatory on `be`; its presence signals intentionality — its absence signals natural process.
- **`la` with a non-volitional natural agent:** the star holds the agent slot even without intent. `la` marks the causal source of the event; non-volitional sources may occupy `la` when the verb is bare `be`. Contrast with S021: the tool uses `ro` (instrument) because a volitional human act is implied; here no human agent exists — the star IS the generative source, so `la` is correct.
- **`ra-su`** = energy-structure = natural energy mass / star. `ra` (energy) + `su` (structure) = a structured concentration of energy. Distinct from `ra-ki-mu` (W012: engine, which is an artifact). A star is not an artifact; it is a natural energy structure. Registry candidate.
- **Natural object gap flagged:** stars, rivers, geological features — non-artifact, non-living physical objects — have no clean entity class. `ra-su` works for energy-generating natural bodies; a general "natural non-living physical object" category may emerge. Logged in notes/open-questions.md.
- **T023 pass** (with non-intentional production distinction formalized).

---

**S023 — Primitive validation: machine stores information** *(T024)*

*Target: "The machine stores information."*

```
Gloss:    la-to-ki-mu  lo-si  ka-ko
Literal:  agent:computation-device  patient:signal/data  action:contain
Natural:  The machine stores information.
```

**Notes:**
- `to-ki-mu` (W011) = knowledge-processing device = computer. First use without a purpose clause.
- `si` = signal / encoded representation = information / data. Consistent with S013–S014 usage. `si` is validated as the right root for "information."
- `ka-ko` = action of containing = store. Second corpus use (first: S020). `ka-ko` now confirmed as the canonical store / hold / contain verb across substances (water, S020) and abstract data (information, this sentence).
- **T024 pass.** Clean.

---

**S024 — Primitive validation: river flows to the sea** *(T025)*

*Target: "The river flows to the sea."*

```
Gloss:    la-ma-di  pa-pu-ma  ka-ki
Literal:  agent:directed-matter/river  location:collective-water/sea  action:move
Natural:  The river flows to the sea.
```

**Notes:**
- **`ma-di`** = directed-matter = river / stream. `ma` (matter/substance) + `di` (direction) = matter with inherent directedness. Preferred over `ma-ki` (matter-motion) because rivers have stable direction; `ma-ki` generalizes to any flowing substance.
- **`pu-ma`** = collective-water = sea / large water body. `pu` (plurality) + `ma` (matter/water) = accumulated water. In the `pa` particle position: `pa-pu-ma` = at/to the sea.
- **Directional destination gap flagged:** `pa` (location particle) does not distinguish rest-at, move-toward, or move-from. "The river flows to the sea" and "the river is in the sea" both use `pa-pu-ma`. The `di` root exists but is not yet a grammatical particle. Logged as open question: promote `di` to destination particle.
- `ka-ki` = action of moving / flow. The motion's direction is encoded in the agent itself (`ma-di`), not in a separate directional marker.
- **T025 pass** (with destination-particle gap logged).

---

## Narrative Scene: The Engineer

*Target: "The engineer inspected the machine. It was damaged. She repaired it to restore power to the city."*

*Tests: narrative continuity, cross-sentence pronoun tracking, agentless state description, repair verb, purpose clause, compound noun for city.*

---

**S025 — Scene sentence 1: inspection**

```
Gloss:    la-su-mu-li  lo-mu  ka-se-past
Literal:  agent:engineer  patient:machine  action:perceive/inspect-PAST
Natural:  The engineer inspected the machine.
```

**Notes:**
- `su-mu-li` (W002) = engineer / systems-builder. First narrative use of this role compound.
- `ka-se` = action of perceiving = inspect / examine deliberately. `se` (perception) used as verbal root with action particle. The act is intentional (`ka`), the mode is perceptual (`se`). No separate compound word needed; particle + root form is sufficient. Noun form `se-ka` (examination / inspection) registered as W034.
- `-past` tense marker is placeholder gloss.

---

**S026 — Scene sentence 2: damage state**

```
Gloss:    lo-ze  de-past
Literal:  patient:it  decay-PAST
Natural:  It was damaged.
```

**Notes:**
- **Agentless-event construction tested:** `lo-ze  de-past` = the machine (as patient) underwent a decay event; no agent specified. This is distinct from `la-[agent]  lo-ze  ka-de-past` (someone intentionally damaged it). The absence of `la` + bare `lo` = passive / agentless event.
- **Copula gap flagged:** "It was damaged" is a predicative adjective in English (state attribution). Tonesu handles this by treating the state as a past event (`de-past`). A dedicated copula structure for "X is [in state] Y" without implying an event remains undefined. Logged in open-questions.md.
- **`ze` as non-person pronoun:** first use of `ze` for an inanimate artifact. Confirms `ze` covers all non-speaker/non-addressee referents, including objects.
- **T006 parallel:** "The old structure collapsed" (T006) is structurally identical — agentless past event, patient as subject. This sentence gives concrete corpus evidence for that pattern.

---

**S027 — Scene sentence 3: repair and purpose**

```
Gloss:    la-ze  lo-ze  ka-de-be-past  wi [ka-ra-be  pa-li-pu]
Literal:  agent:she  patient:it  action:repair-PAST  intention [action:energy-restore  location:city]
Natural:  She repaired it to restore power to the city.
```

**Notes:**
- **`de-be`** = decay-growth = process of reversing decay = repair / restoration. Head-final: `be` (growth) is the head; `de` (decay) specifies the starting condition. `de-be` = growth characterized as recovery from decay. `ka-de-be` = the act of repairing. Candidate W035; registered in registry/derived.md.
- **`ra-be`** = energy-growth = energy restoration / power return. `ra` (energy) + `be` (growth/increase) = energy increasing. In the purpose clause: the intended outcome is energy being restored to the city.
- **`li-pu`** = person-collective = city (colloquial short form of `li-pu-pa`). `li` (social agent) + `pu` (plurality) = organized collective of persons. Full compound: `li-pu-pa` (person-collective-place). In the `pa` particle position: `pa-li-pu` = at/to the city. Candidate W036; registered in registry/derived.md.
- **Agent inheritance (5th corpus confirmation):** `wi` clause omits agent → matrix agent `ze` inherited. Canonical.
- **Cross-sentence pronoun tracking:** `mu` (machine, introduced S025) is tracked as `ze` from S026 onward. First multi-sentence pronoun tracking test in the corpus.

*(Running notes on what works and what doesn't)*

- The SOV + particle system reads clearly for simple sentences
- Nested concepts (S010) reveal the need for explicit grouping markers
- ~~Particle/root collision (`li`)~~ → resolved by renaming agent particle to `la`
- ~~Particle/root collision (`ra`)~~ → resolved: instrument particle renamed `ro`
- ~~Pronoun collisions (`se`, `wi`)~~ → resolved: pronouns renamed `ze`, `yu`
- Causal structures (S011, S013) confirm `go`/`du` framing as the canonical conditional strategy — no new particle needed
- ~~Inchoative derivation pattern missing~~ → resolved: `ROOT + ki` = enter state ROOT (spec/morphology.md)
- Abstract agents (`to`, `si` as grammatical subjects) work cleanly with `la` as the unambiguous agent marker
- ~~Purpose clauses not formalized~~ → resolved: `wi [clause]` defined in spec/grammar.md § Purpose Frame
- **Boundary rule tested (S015–S027):** matrix-level argument marker unambiguously signals return to matrix clause in single-level embedding. `ne` inside subordinate clause confirmed as argument marker, not boundary signal. Nested subordination untested.
- **Agent inheritance rule (wi-clauses, 5th confirmation at S027):** omitting the purpose-clause agent unambiguously inherits the matrix agent. Rule formally stated in spec/grammar.md § Purpose Frame.
- ~~**Compounding vs relative clause (S019):** compounding covers noun-naming but breaks for capability expression.~~ Relativizer gap confirmed (S019); imperative gap closed (spec/grammar.md § Imperatives).
- **Intentionality split (S021–S022):** `ka` on a verb marks deliberate action; bare `be` marks non-intentional production. `ro` marks instrument; `la` marks causal source. Tools use `ro`; natural sources use `la` with bare `be`. Split first attested S021–S022.
- **Agentless-event construction (S021, S026):** `lo-[patient]  [verb]` without `la` marks a patientive event with no specified agent. First used for instrument-mediated action (S021) and state description (S026). Formal grammar rule pending; see open-questions.
- **Cross-sentence pronoun tracking (S025–S027):** `ze` successfully tracks a machine referent across three sentences. First multi-sentence pronoun coherence test. `ze` confirmed as covering non-person referents.
- **Directional destination gap (S024):** `pa` does not distinguish rest-at from move-toward. `di` root candidate for destination particle; see open-questions.

---

## Smoke-Test Targets

These sentences must remain expressible under any revision to phonology, grammar, or morphology. They cover the minimum range of structures the language claims to support. Write each one out fully (gloss + literal + natural + notes) as primitives stabilize.

### Ownership and Identity
- [ ] **T001** — This device belongs to me. *(possession, pronoun, basic NP)*
- [ ] **T002** — The two engineers share a tool. *(number, shared possession, plural agent)*
- [ ] **T003** — She is the leader of the group. *(identity, role, collective)*

### Basic Action and Description
- [ ] **T004** — The water flows downward. *(intransitive motion, direction, no agent)*
- [ ] **T005** — He built a small shelter quickly. *(action, quality modifier on object, adverb modifier)*
- [ ] **T006** — The old structure collapsed. *(past event, no intentional agent)*

### Time and Place
- [ ] **T007** — The meeting happened before the storm. *(relative time, two events)*
- [ ] **T008** — She will arrive at the eastern boundary tomorrow. *(future, location, direction)*
- [ ] **T009** — They have been working here for a long time. *(ongoing aspect, location, duration)*

### Abstract and Relational
- [ ] **T010** — Knowledge without structure is not useful. *(negation on quality, abstract NPs)*
- [ ] **T011** — The cause of the failure is unknown. *(causal relation, negated epistemic state)*
- [ ] **T012** — This system connects two separate domains. *(relation, quantity, abstract objects)*

### Technical Domain
- [ ] **T013** — The computation device stores and retrieves patterns. *(compound NP, two actions, abstract object)*
- [ ] **T014** — Signal transmission failed because the network lost power. *(causal, failure state, technical vocabulary)*
- [ ] **T015** — The engineer designed a new domain for biological information. *(domain creation concept expressed in-language)*

### Edge Cases
- [ ] **T016** — No one built this. *(agentless past, negated agent)*
- [ ] **T017** — Is this the same system? *(question, identity, definiteness)*
- [ ] **T018** — Do it again, more carefully. *(imperative, repetition, intensity modifier)*
- [ ] **T019** — The idea spread from one person to many. *(abstract motion, source/destination, quantity shift)*
- [ ] **T020** — What she said cannot be unsaid. *(embedded clause, negated reversibility, speech act)*

### Primitive Validation Sentences

These are the minimal sentences that should work as soon as primitives are defined. If they cannot be expressed cleanly, the primitive set needs revision before anything else proceeds.

- [x] **T021** — The child drinks water. *(basic SVO, animate agent, substance)* → **S020**
- [x] **T022** — The tool cuts wood. *(instrument as agent, material object, action)* → **S021** (instrument takes `ro`, not `la`; intentionality principle)
- [x] **T023** — The star emits light. *(natural agent, emission process, no intention)* → **S022** (bare `be` for non-intentional production)
- [x] **T024** — The machine stores information. *(device, abstract object, containment)* → **S023**
- [x] **T025** — The river flows to the sea. *(motion, direction, natural destination)* → **S024** (destination-particle gap flagged)
- [x] **T026** — Knowledge grows when information connects. *(abstract causation, two abstract NPs, conditional)* → **S013** (already written)

---

## Conversations

Conversations test what isolated sentences cannot: turn-taking, pronoun tracking across speakers, content questions, responsive particles, ellipsis. Each exchange is labeled C-series.

---

**C001 — First conversation: backup unit failure**

*Scene: The relay platform, shortly after S027. Engineer A (ze) has discovered the backup power unit is also failing. Engineer B (a colleague) arrives.*

*Tests: content question, copula gap, agentless state, W037 `ti-fe`, utterance-level epistemic marking, imperative in dialogue, acknowledgment particle, agent drop.*

---

**Turn A1**

```
Gloss:    la-mi  pa-re-mu  lo-de  ka-se-past
Literal:  agent:I  location:backup-unit  patient:decay  action:perceive-PAST
Natural:  I found damage in the backup unit.
```

**Notes:**
- `re-mu` = repeat-artifact = backup / secondary unit. `re` (repetition) + `mu` (artifact) = a second instance of the artifact serving the same function. Transparent compound; not registered separately.
- `lo-de` = patient:decay — the decay is what was perceived. Treating damage as a concrete patient-of-perception rather than a predicate. First use of a process root as a nominal patient.
- Agent `la-mi` is explicit because A is introducing new information; no prior discourse context to rely on.

---

**Turn B1**

```
Gloss:    de  vo  to-si?
Literal:  decay  quality  QUERY
Natural:  What kind of damage?
```

**Notes:**
- **First content question in corpus.** `to-si` (W026, query/knowledge-seeking signal) used as a floating interrogative placeholder at end of utterance. Extends W026 from its registered nominal sense ("a query") to a grammatical interrogative function: "the thing-I-am-seeking-knowledge-of."
- Structure: `de` (the topic: decay) + `vo` (the dimension being questioned: quality/kind) + `to-si?` (interrogative marker: what?). Reads: "Decay — quality — [seeking this information]?" = "What quality is the damage?"
- `to-si` as interrogative placeholder is semantically transparent: it is literally a knowledge-seeking signal, placed where the unknown information would go. No new particle required; W026 function extended.
- Contrast with yes/no questions (`?` at end of full proposition): content questions use `to-si?` in the slot corresponding to the queried element.

---

**Turn A2**

```
Gloss:    lo-re-mu  de-now
          ti-fe  ki-now
Literal:  patient:backup-unit  decay-NOW
          time-limit  approach-NOW
Natural:  The backup unit is decaying.
          [It] approaches the time-limit.
```

**Notes:**
- **Copula gap (2nd confirmation):** `lo-re-mu  de-now` = patient:backup-unit + decay-NOW. No linking verb. The state is attributed to the patient by juxtaposition. Consistent with S026 (`lo-ze  de-past`). Copula-by-juxtaposition is the working pattern; formal rule pending.
- **`ti-fe` first corpus use:** W037 (time + boundary = period-limit, deadline). The time-limit approaches; sense of urgency conveyed without intensifiers or exclamations.
- **`ki-now` with dropped argument:** bare `ki-now` (motion-NOW) without `la` or `lo`. The subject of "approaches" is pragmatically recoverable (the system, the failure event, the time itself — it does not matter). First attested *argument-drop driven by discourse context* rather than imperative agent-drop. Minimal, clean.
- Two separate sentences rather than a compound: A is giving information sequentially, not composing a complex clause. Normal for speech under urgency.

---

**Turn B2**

```
Gloss:    ta-now  fe-ki?
Literal:  time:now/today  limit-cross?
Natural:  Does it cross the limit today?
```

**Notes:**
- Yes/no question with content `?` at end. `ta-now` = at this time-period = today / currently. `fe-ki` = reach/cross a limit (from W024 related entry, first verbal use in a question).
- Clean. No gaps.
- **"Today" resolved:** `ta-now` covers "at this time-period" colloquially; no dedicated word for day-as-unit-of-time yet. The time-period granularity (hour? day? shift?) is context-dependent. Adequately ambiguous; flag for future number/time vocabulary.

---

**Turn A3**

```
Gloss:    la-mi  si  [fe-ki-now]
          ne-li-su-li  ka-fe-si
Literal:  agent:I  signal-level  [limit-cross-NOW]
          recipient:coordinator  action:warn
Natural:  I assess [as signal-level]: it crosses the limit now.
          Warn the coordinator.
```

**Notes:**
- **First utterance-level epistemic marker.** `la-mi  si  [proposition]` = "I, at `si` epistemic level, assert [...]." The speaker marks their confidence explicitly: `si` (signal/hypothesis, not yet `to` = established). This is Domain 1 (Epistemic States) operating at discourse level — a speaker hedging not the content of their claim but its *epistemic status*.
- This construction is productive: `la-[speaker]  [epistemic-root]  [proposition]` = "I hold [proposition] at [level]." The epistemic root (`se`, `si`, `to`, `to-su`) becomes a sentence-level modal operator. First corpus evidence that the epistemic vocabulary functions this way. The pattern should be documented in spec/grammar.md once confirmed by a second case.
- **Note:** this is NOT the same as the evidentiality candidates `se-ro`/`si-ro`/`to-ro` (which mark *how* you came to know). This marks *what status you assign the proposition*. Both mechanisms may coexist; they are orthogonal.
- Second sentence: imperative with recipient. `ne-li-su-li` (W001 in recipient slot) first corpus use of that form. `la-tu` dropped (imperative rule). Clean.

---

**Turn B3**

```
Gloss:    ka-to-su-ki
          ka-ki-now
Literal:  action:comprehend
          action:go-NOW
Natural:  Understood.
          I'm going now. / On my way.
```

**Notes:**
- **`ka-to-su-ki` as responsive:** first standalone use of W025 in conversational acknowledgment. `ka` (action) + `to-su-ki` (enter organized understanding) = "I have grasped this." Compact and precise: not "I heard you" (merely signal-level reception) but "I have understood" (comprehension achieved).
- **Agent drop in B3b:** `ka-ki-now` with `la-mi` omitted. In prior imperative constructions (S019, A3 above), `la-tu` (addressee-as-agent) is dropped. Here the *speaker* drops themselves. First attested case of speaker-drop in conversational context. This is presumably licensed by immediate-context salience: the speaker is the obvious actor. The rule is provisional: *in face-to-face exchange, the current speaker may be dropped from the agent slot when the action described can only be theirs.* Log as a grammar open question.
- **Absence of "yes" / affirmative particle:** The entire acknowledgment arc (Turn B3) manages without a standalone affirmative. English "yes" doesn't appear because Tonesu routes agreement through action-confirmation (`ka-to-su-ki` = I have understood, implicitly affirming) and motion-declaration (`ka-ki-now` = I am acting on it). This gap may be real (Concordia never developed a simple "yes") or the pattern may be that Tonesu *always expresses what kind of affirmation*. Needs more corpus data.

---

**Conversation gaps discovered:**

| Gap | First exposed | Status |
|-----|--------------|--------|
| Content question word | B1: `to-si` as interrogative placeholder (workaround using W026) | Open — workaround documented |
| Copula / predicate-state | A2a: juxtaposition pattern (`lo-X  state-NOW`) | Confirmed pattern; formal rule pending |
| `ti-fe` (time-limit, deadline) | A2b | Resolved — W037 registered |
| Argument drop by discourse context | A2b: bare `ki-now` | Open — related to topic-drop question |
| Utterance-level epistemic modal | A3a: `si [proposition]` pattern | New — needs grammar.md entry once confirmed |
| Agent drop (speaker) in conversation | B3b: `la-mi` omitted | Open — provisional rule noted above |
| Affirmative / negative particles | B3: no "yes" used; routed through action-confirmation | Open — may be intentional absence |

---

## Primitive Property Tests

These sentences directly exercise the four hidden properties identified in notes/semantic-map.md § Hidden Properties. Each one is designed to stress-test a specific structural commitment.

---

**S028 — Bilateral causation: double-entry framing** *(Hidden Property A)*

*Target: "The storm caused the bridge to collapse."*

**Attempt — `go`/`du` two-frame version:**

```
Gloss:    go [la-ra-ki  lo-su-mu  de]  du [de-ki]
Literal:  cause [agent:storm  patient:structure-artifact  decay]  result [enter-decay]
Natural:  Because [the storm decayed the structure], result: [collapse].
```

**Single-frame alternative (canonical from S011):**

```
go-ra-ki  du-de-ki-su-mu
cause:storm  result:structure-collapse
```

**Notes:**
- **`ra-ki`** = energy-motion = violent energetic event = storm. `ra` (energy) + `ki` (motion) = energy in motion; undirected discharge of kinetic force. Natural non-volitional agent, so paired with bare `de` (non-intentional decay). Registered as W038.
- **`su-mu`** = structure-artifact = bridge / structural edifice. From the existing compound logic: `su` (structure) + `mu` (artifact). Not separately registered; transparent.
- **`du` as full clause introducer — first test.** In S011, `du` appeared as a prefix on a noun compound (`du-machine-fail`). The two-frame form above uses `du [clause]` symmetrically with `go [clause]`. This is the first attempt; the construction is grammatically suspicious because the boundary rule should apply: `du [de-ki]` — a result clause after a cause clause. But what returns to matrix level after? There is no matrix clause here at all. This may be a **biclausal coordination structure** rather than a subordinate frame. That is a new grammatical category. See grammar-pressure note P-GP-003 and open-questions.md.
- **Single-frame alternative is the safe canon.** Following S011's established pattern: `go-[cause]  du-[result]` using noun compounds as the minimal biclausal form. This works cleanly. The full two-frame version should be treated as provisional until the biclausal coordination rule is defined.
- `de` as a transitive verb of sorts: `la-ra-ki  lo-su-mu  de` = "the storm decay-ed the structure." Bare `de` (non-intentional) with `la` agent and `lo` patient. First transitive use of `de`. The intentionality is absent: storms don't intend anything. Clean.

---

**S029 — Repetition and habitual aspect** *(Hidden Property B)*

*Target: "The river floods every year."*

**Attempt A — `re` as time modifier:**

```
Gloss:    la-ma-di  ta-re-ti  fe-ki
Literal:  agent:river  time:repeat-cycle  boundary-cross
Natural:  The river, at each recurring time, crosses its limit.
```

**Attempt B — `re` as verbal aspect prefix:**

```
Gloss:    la-ma-di  re-fe-ki
Literal:  agent:river  repeat-boundary-cross
Natural:  The river repeatedly crosses its limit.
```

**Notes:**
- **`re-ti`** = recurring time-period = cycle, year-equivalent. The compound is transparent: `re` (repetition) + `ti` (time) = a time unit defined by recurrence. Tonesu has no registered word for "year"; `re-ti` routes this through the repetition primitive cleanly without borrowing. The unit implied (annually, seasonally?) is context-dependent — a feature, not a bug, given the language's preference for compositional precision.
- **`fe-ki`** = reach or cross a limit = flood. The river exceeding its banks is a `fe-ki` event: it has crossed the boundary of its normal channel. No separate "flood" vocabulary needed.
- **Attempt A vs B expose the aspect grammar pressure (P-GP-002).** Attempt A treats `re-ti` as a time adverbial (in the `ta` slot): safe, uses established grammar. Attempt B uses `re` as a prefix on the verb compound itself: uncharted. Both are compositionally plausible. The difference: Attempt A says "at recurring times, the river crosses its limit" (external frequency); Attempt B says "the river habitually limit-crosses" (internal aspect). These are distinct claims. Attempt A is canonical for now; Attempt B is flagged as pending the aspect grammar decision.
- **Attempt A is S029 canon.** Note: makes `ta-re-ti` the first time-expression that uses a compound time noun (`re-ti`) rather than a bare placeholder gloss. Progress toward real tense/time vocabulary.

---

**S030 — Irreducible value and the `vo` predication problem** *(Hidden Property C)*

*Target: "The archive must be preserved."*

**Part 1 — Value predication:**

```
Gloss:    la-to-su-mu  vo
Literal:  agent:archive  quality/value
Natural:  The archive has value.
```

**Part 2 — Obligatory preservation:**

```
Gloss:    wi [ka-no-de]
Literal:  intention [action:negate-decay]
Natural:  [It] should not decay. (= must be preserved)
```

**Combined reading:**

```
la-to-su-mu  vo  wi [ka-no-de]
```

*The archive has value; the intention is its non-decay.*

**Notes:**
- **`vo` as predicate adjective — first unambiguous case.** `la-to-su-mu  vo` treats `vo` (value/quality) as a predicate in the agent position: "agent:archive  quality." This parallels the copula-by-juxtaposition pattern (`lo-X  state`) but inverts it: here the subject is in the `la` slot, not `lo`. The pattern divergence (agent-slot vs patient-slot for state description) is new and unresolved. Both patterns are now in corpus:
  - `lo-X  state` = patient undergoes state (patientive)
  - `la-X  quality` = agent possesses quality (attributive?)
  These may be two distinct constructions with different implications, not registers of one pattern. Flag.
- **`no-de`** = negate-decay = preserve / prevent degradation. `no` (negation) + `de` (decay). Head-final: the process being negated is `de`; `no` reverses it. Complement to W035 `de-be` (repair after decay). `de-be` = grow-after-decay; `no-de` = prevent-decay-from-occurring. First corpus use of `no` as a productive verbal prefix. Valuable.
- **`wi` as obligation marker.** The purpose frame `wi [clause]` here functions differently from S016–S027. Previously: `wi` introduced an agent's *intended* outcome. Here: `wi` fronts the entire sentence as a prescription — "the intention [holding] is [non-decay]" — outside any specific agent's will. This approaches modal obligation. The polysemy is productive (intention and obligation share semantic space), but the agent of `wi` is now absent entirely. Log: when `wi [clause]` appears without a prior agent, its reading shifts from purpose ("in order to") toward obligation ("it is intended that"). The agent of `wi` is either the speaker, Concordian convention, or normative reality — ambiguous. Needs a ruling.
- **`vo` as irreducible.** The sentence works without defining value in terms of anything else. No "valuable to whom" or "valuable for what purpose" is specified. This is the primitive doing its work: `vo` is the assertion; it stands alone.

---

**S031 — Unity vs plurality: the team acts as one** *(Hidden Property D)*

*Target: "The team acts as one."*

**Attempt A — `ru` as adverbial quality modifier:**

```
Gloss:    la-li-pu  ka  ru
Literal:  agent:collective  action  unity
Natural:  The collective acts with unity.
```

**Attempt B — `ru` incorporated into the agent compound:**

```
Gloss:    la-li-pu-ru  ka
Literal:  agent:unified-collective  action
Natural:  The unified collective acts.
```

**Notes:**
- **`li-pu`** (from W036) = person-collective = team / group. First use as a grammatical subject without the location particle `pa`.
- **Attempt A: `ru` as a floating quality modifier.** `ka  ru` — the action is characterized by unity. Parallel to how `vo` was used predicatively in S030. `ru` in post-verbal position modifies the manner of the action: "they act, and the manner is ru (unified)." This would make `ru` an adverb-of-manner in this position — a new grammatical function for a primitive not previously used this way.
- **Attempt B: `ru` incorporated into the NP compound.** `la-li-pu-ru` = agent:many-persons-unified. The unity is an attribute of the collective, not a description of the action. These make different claims: Attempt A says "they are acting in coordination right now"; Attempt B says "they are a unified team (and they act)."
- **Attempt A is preferred for the target sentence.** "Acts as one" is a manner description, not a permanent attribute. Attempt A captures this; Attempt B implies permanent coherence status. But both constructions need formal rules.
- **`pe` (part) gap exposed.** "Acts as one" might also be expressed using `pe` (part/component): the team acts such that each `pe` moves with the whole. But `pe` has no corpus use yet. Flagged.
- **Number/collective precision in practice.** This sentence confirms the `ru`/`pu`/`nu` distinction is doing real work: "the team acts as one" is a `ru` (unity/coherence) claim, not a `nu = 1` (count) claim. A hundred people can `ka ru` (act with unity). The English expression "as one" conflates `ru` with `nu = 1` in a way Tonesu does not.

---

### Structural Grammar Pressures

The four hidden-property tests above revealed three places where the primitive set will eventually force new grammar, not just new vocabulary. These are logged in notes/open-questions.md (P-GP-001 through P-GP-003).

| Pressure | Trigger sentence | Symptom |
|----------|-----------------|---------|
| **P-GP-001: `vo` and `ru` predication** | S030, S031 | Two competing copula-adjacent constructions: `la-X  quality` vs `lo-X  state`. Quality roots (`vo`, `ru`) used predicatively behave differently from state roots (`de`, `be`). A formal rule is needed. |
| **P-GP-002: `re` aspect vs time adverbial** | S029 | `re-ti` as a time phrase vs `re-VERB` as habitual aspect are both compositionally legal. The language must settle whether aspect is encoded temporally (time-phrase strategy) or morphologically (verb-prefix strategy) before `re` can be used consistently. |
| **P-GP-003: `go`/`du` bilateral clause coordination** | S028 | `go [clause]  du [clause]` is a biclausal coordination frame, not a standard subordinate clause. Current grammar only formalizes subordination (`go [clause]` with the matrix following). The symmetric two-frame case has no boundary rule — what comes after `du [clause]`? |
