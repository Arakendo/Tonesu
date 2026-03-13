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

**C002 — Technical coordination: relay failure**

*Scene: Two engineers on different platforms. A is live at the relay installation; B is directing remotely.*

*Tests: imperative × 2, diagnostic state-change loop (detect → examine → identify → repair → confirm), `lo-X  state` copula × 3, `ru`/`no-ru` as predicate quality on a non-person entity (first device-quality predication).*

---

**Turn A1**

```
Gloss:    lo-si-mu  no-ru
Literal:  patient:relay  not-unified
Natural:  The relay is unstable.
```

**Notes:**
- `si-mu` = signal-artifact = relay device / transceiver. Registered as W039.
- `no-ru` = negate-unity = incoherent / unstable. First use of `no-` on a quality root (previous: `no-de` S030). `no-` is now confirmed as a productive negation prefix on quality and process roots alike.
- `lo-X  quality` with a device in the patient slot — confirms quality predication works on non-person entities. Extends the copula-by-juxtaposition pattern to artifact subjects.

---

**Turn B1**

```
Gloss:    ka-se  lo-si-su-mu
Literal:  action:examine  patient:signal-structure-artifact
Natural:  Examine the antenna array. [Imperative — `la-tu` dropped]
```

**Notes:**
- `si-su-mu` = signal-structure-artifact = antenna array / receiving installation. Transparent compound; not registered separately.
- Third imperative in corpus (`la-tu` drop confirmed pattern): S019 B, C001 A3, C002 B1Imperative now occurs both in formal instruction (S019) and in live technical direction. Register is the same.

---

**Turn A2**

```
Gloss:    lo-ne-mu  de
Literal:  patient:connection-artifact  decayed
Natural:  The connector is broken.
```

**Notes:**
- `ne-mu` = relation-artifact = physical connector / coupling component. Transparent; not registered separately.
- Bare `de` predication on an artifact — the connector has undergone non-intentional deterioration. Consistent with all prior `de` uses.

---

**Turn B2**

```
Gloss:    ka-de-be  lo-ne-mu
Literal:  action:repair  patient:connection-artifact
Natural:  Repair the connector. [Imperative]
```

**Notes:**
- `de-be` (W035) used in imperative for the first time. Previously appeared only in declarative contexts. Works cleanly: the directive is to perform `de-be` on the patient.

---

**Turn A3**

```
Gloss:    lo-si-mu  ru  ta-now
Literal:  patient:relay  unified  time:now
Natural:  The relay is stable now.
```

**Notes:**
- `lo-si-mu  ru  ta-now` closes the loop from A1. State has changed from `no-ru` → `ru`. `ta-now` marks the resolution as present-moment. First time a sentence directly inverts a previous one within the same conversation.
- `ru` as predicate quality on a device: this is the affirmative twin of C002 A1's `no-ru`. Both confirm P-GP-001 territory: quality roots (`ru`, `no-ru`, `vo`) predicated on the patient via juxtaposition.

---

**C002 Gaps and pressures:**

| Gap | Location | Status |
|-----|----------|--------|
| `no-` productivity on quality roots | A1 `no-ru` | Pattern confirmed — `no-de`, `no-ru`, `no-fe` all attested across S030/C002/C004; may be a general negation prefix |
| Device-quality copula | A1, A3 | Extends `lo-X  state` to artifact subjects — no new rule needed, confirms pattern breadth |

---

**C003 — Casual social: travel question**

*Scene: Two non-engineers in everyday context. A asks about travel plans.*

*Tests: FIRST YES/NO QUESTION IN CORPUS (C003 A1 — critical gap), echo-confirmation as first-person restatement (no affirmative particle), `ta-ti-be` first proximate-future time reference, purpose clause in casual register.*

*Grammar pressure: C003 A1 is the first sentence in the corpus that requires distinguishing a question from a statement in writing. This is the trigger for P-QM-001 (polar question marker). C003 B1 is the first conversation response that would normally use "yes" — it avoids it via echo-confirmation, triggering P-AF-001 (minimal affirmative particle).*

---

**Turn A1**

```
Gloss:    to-si  —  la-tu  ki  pa-li-pu  ta-ti-be
Literal:  knowledge-inquiry — agent:you  motion  place:city  time:next-time
Natural:  Are you going to the city soon?
```

**Notes:**
- `to-si` (W026) redeployed as a POLAR question marker. Prior use in C001 B1: content question ("what kind of damage?" — unknown argument). Here: yes/no question (unknown truth-value of complete proposition). Same surface form, different logical scope.
- Structural difference: in content questions, `to-si` fronts a proposition with a gap where the unknown argument sits (`to-si  [damage:___?]`). In polar questions, `to-si` fronts a complete well-formed proposition (`to-si  [la-tu  ki  pa-li-pu]`) with the truth value itself as the unknown. Both are semantically coherent under `to-si` = "seeking information." Whether this fully resolves or just defers the question depends on whether corpus eventually produces an ambiguous case. See P-QM-001.
- `ta-ti-be` = time:next-time = proximate future / tomorrow / soon. `ti` (time) + `be` (grow/come) = an upcoming time interval. Registered as W040. First calendrical / temporal reference compound not using an English placeholder gloss.
- The dash after `to-si` marks a pragmatic boundary: the inquiry frame (`to-si`) sets the mode, then the full proposition follows. This is the same boundary behavior as other clause-framing particles.

---

**Turn B1**

```
Gloss:    la-mi  ki  pa-li-pu  ta-ti-be
Literal:  agent:I  motion  place:city  time:next-time
Natural:  I'm going to the city soon.
```

**Notes:**
- **Echo-confirmation**. B restates the proposition from B's own agent position rather than using a bare affirmative. The question's proposition (`la-tu  ki  pa-li-pu  ta-ti-be`) is answered by replacing `la-tu` (agent:you) with `la-mi` (agent:I) and repeating. "Yes" in Tonesu is currently: "I do the thing you asked about."
- This is the same confirmation strategy as C001 B3 (`ka-to-su-ki` + `ka-ki-now`)  — agreement through action-commitment — but now in its minimal form: restate the claim from oneself. C001 used action-compounds to confirm; C003 B1 uses the proposition's own structure. Two echo-confirmation strategies now in corpus.
- Gap: the echo is unambiguous here because `la-tu` → `la-mi` is a clean substitution. In more complex propositions, full echo may be syntactically heavy. The pressure toward a minimal `[affirm]` particle grows. See P-AF-001.

---

**Turn A2**

```
Gloss:    lo-ma-su  be-now  pa-ze
Literal:  patient:water-structure  present/growing  place:there
Natural:  A new water facility is there now.
```

**Notes:**
- `ma-su` = matter-structure = water facility / material processing system. Transparent compound; not registered separately. `ma` (matter) + `su` (structure/organize) = a system that organizes material. Applicable to water treatment, filtration, reservoir management.
- `be-now` used as presence/existence predicate: the facility is actively there and operational. Consistent with `be` as "grow/exist" in predicate position.
- `pa-ze` = place:there = at that place. First use of `ze` (3rd-person/inanimate) in the location particle frame. `pa-ze` = location of the contextually established place (the city). Economy of reference: the city was established in A1; `ze` stands in without repeating `li-pu`.

---

**Turn B2**

```
Gloss:    la-mi  wi [ka-se  lo-ze]
Literal:  agent:I  intention [action:examine  patient:it]
Natural:  I intend to go see it.
```

**Notes:**
- Purpose clause (`wi [clause]`) in casual register. C001's purpose clauses were obligation/instruction; this one is personal intention. Confirms `wi` is not register-restricted.
- `ka-se  lo-ze` = examine/perceive it. `se` (perceive) as the verb content of the action. B intends to go look at the new facility. Simple and clean; the purpose clause carries the full meaning without a separate "go" verb because going is implied by the intention-toward.
- Agent of `wi` clause: inherited as `la-mi` per the agent-inheritance rule. 7th corpus confirmation.

---

**C003 Gaps and pressures:**

| Gap | Location | Status |
|-----|----------|--------|
| **Polar question marker (P-QM-001)** | A1 | Critical — `to-si` pressed into service for both content and polar questions. Works semantically but creates ambiguity with complex propositions. A dedicated polar marker (e.g., rising-particle or question-final morpheme) may be needed within 20–30 more sentences. |
| **Minimal affirmative (P-AF-001)** | B1 | Echo-confirmation valid but verbose. Two strategies in corpus (action-commit C001, echo-restate C003); neither is a bare "yes." Pressure toward minimal particle grows with each conversation. |
| `ta-ti-be` future reference | A1 | First real future time reference without English placeholder gloss. `ti-be` (W040) works; related expressions (`ti-de` = past time? `ti-re-be` = next cycle?) not yet tested. |

---

**C004 — Disagreement: disputed damage assessment**

*Scene: Two engineers have both examined the same unit (following C002 pattern). They disagree on its status.*

*Tests: FIRST DIRECT EPISTEMIC CONTRAST between two speakers (different epistemic levels on the same proposition), `la-[process]  be  [embedded-proposition]` as new evidential frame (examination as epistemic agent), `no-fe` first use, institutional routing as dialogue resolution.*

---

**Turn A1**

```
Gloss:    lo-mu  de
Literal:  patient:machine  decayed
Natural:  The unit is damaged.
```

**Notes:**
- Bare unhedged assertion. No epistemic marker. A is asserting at the `to` level implicitly: "this is known, I'm not qualifying it." This is the default unmodified register.
- Short form — the confident claim is also the economical one. Length correlates with uncertainty in Tonesu.

---

**Turn B1**

```
Gloss:    la-mi  si  [lo-mu  be-now]
Literal:  agent:I  [signal-level]  [patient:machine  exists/functions-now]
Natural:  I assess: the machine is still operating.
```

**Notes:**
- **First direct epistemic contrast in corpus.** A1 makes a bare `to`-level (unmarked = assumed certain) assertion. B1 explicitly marks `si`-level (signal/inference level — not direct perception, not certain knowledge). The two speakers are at architecturally different epistemic positions about the same entity.
- This is the first corpus test of Monday's proposed full epistemic ladder (`se` → `si` → `to`). The `si` marker is working exactly as predicted: B has a signal-level assessment, not a to-level certainty. The contrast is immediate and crisp.
- `lo-mu  be-now` = the machine currently functions/exists. `be` as "is present and operational." This is the second corpus use of `be` as an existence predicate (first: C003 A2). Pattern tentatively confirmed: `be` can carry "is still present/operational" meaning in patient-predicate position.
- Second corpus use of utterance-level epistemic modal (`la-[speaker]  [epistemic-root]  [embedded-prop]`). First was C001 A3 (`la-mi  si  [fe-ki-now]`). Pattern appears twice, different speakers, same structure. Ready to formalize in spec/grammar.md.

---

**Turn A2**

```
Gloss:    la-se-ka  be  [lo-mu  de]
Literal:  agent:examination  produces/records  [patient:machine  decayed]
Natural:  The examination produces the finding: the machine has decayed.
```

**Notes:**
- **New evidential frame: process as epistemic agent.** `la-se-ka` = agent:examination. An examination process (`se-ka`, W034) occupies the `la` slot and produces (`be`) an embedded propositionas its output. This extends the epistemic agent pattern beyond persons: not just "I assess" but "the process produces [result]."
- `be` with embedded proposition: `la-X  be  [proposition]` = "X generates/produces [proposition as finding]". First use of `be` with a clausal complement. The embedded `[lo-mu  de]` is the finding.
- This is an important new construction: the examination is not a person, but it occupies the agent-epistemic position fully. This aligns with Concordian institutional epistemology — the validity of a claim comes from the process, not just the person. The process is the agent; its output is the proposition.
- A is now escalating: A1 was personal assertion; A2 is impersonal institutional evidence. The claim hasn't changed but the grounding has shifted from personal to procedural.

---

**Turn B2**

```
Gloss:    lo-de  no-fe  —  lo-mu  be-now
Literal:  patient:decay  not-at-boundary — patient:machine  functions-now
Natural:  The decay has not reached the limit. The machine still functions.
```

**Notes:**
- `no-fe` = negate-boundary = has not crossed the threshold. Third `no-` compound: `no-de` (S030), `no-ru` (C002 A1), `no-fe` (C004 B2). Pattern is now robust enough to note: `no-` functions as a productive negation prefix across process roots (`de`), quality roots (`ru`), and boundary terms (`fe`). Likely works on any primitive root.
- B is making a quantitative threshold argument: the decay exists (B doesn't deny it), but hasn't reached `fe` (the limit/boundary). This uses the boundary ontology (`fe`) as a diagnostic threshold — the question isn't whether decay is present but whether it's reached significance.
- Coordinate clauses separated by dash. Third dash-separation in corpus (C001 A2 used mid-sentence dash; S028 attempt used it; C004 B2 uses it in full discourse). Two short propositions that together form B's rebuttal.
- The disagreement is now fully engaged: A says decay (de); B says decay present but below threshold (de + no-fe). Neither is lying or misperceiving — they're at different threshold assessments. This is a `to-fe` (epistemic boundary) dispute in practice.

---

**Turn A3**

```
Gloss:    la-tu  ka-si  lo-li-su-li  lo-ze
Literal:  [you]  action:signal  patient:coordinator  relation:it
Natural:  Signal the coordinator about it. [Imperative]
```

**Notes:**
- A does not concede. A does not double down. A routes the dispute to institutional process: the coordinator (`li-su-li`, W001) will adjudicate.
- `lo-ze` in the `ne`-adjacent (relation) position means "about it" / "regarding it" — the object of the signal is not just the coordinator but the matter at hand. First use of `lo-ze` as a relational argument after a direct object.
- This is the institutional resolution pattern the Concordian design anticipates: when two persons disagree on epistemic status, neither gets to win by assertion — the process decides. A3 enacts this rather than states it.
- **Fifth imperative in corpus** (S019 B, C001 A3, C002 B1, C002 B2, C004 A3). Imperative is now robust enough to be considered a fully verified construction.

---

**C004 Gaps and pressures:**

| Gap | Location | Status |
|-----|----------|--------|
| `la-[process]  be  [proposition]` evidential frame | A2 | New pattern — process as epistemic agent producing a propositional finding. Needs a formal rule. How does the embedded proposition bind? Is the `be` here the same `be` as "grow/produce"? |
| `lo-X  be-now` existence predicate | B1, A2 | `be` used as "is still functioning/present" in predicate position. Pattern appears in C003 A2 and C004 B1 — two corpus instances. Tentatively confirmed; related to copula-by-juxtaposition family. |
| Utterance-level epistemic modal formalization | B1 | Two corpus cases now (`la-mi si [prop]` in C001 A3 and C004 B1). Ready to formalize in spec/grammar.md. |
| `no-` as universal negation prefix | B2 | Three compounds: `no-de`, `no-ru`, `no-fe`. Ready to declare: `no-` + [root] = the negation/absence of that root in any slot. |

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

---

## `ha` Primitive Validation Batch

These nine sentences establish corpus evidence for `ha` (heat / thermal state of matter), added as primitive 32 in March 2026. Each sentence targets a distinct domain where `ha` must operate clearly and without category bleed from `ra` (energy/force). The test criteria: does the sentence produce semantic distortion if `ha` is replaced with `ra` compounds? Distortion = the sentence says something structurally wrong, not merely long.

---

**S032 — Bodily thermal state** *(T-HA-001)*

*Target: "I feel cold."*

```
Gloss:    la-zo-mi  se  no-ha
Literal:  agent:my-organism  perceive  not-thermal
Natural:  My body perceives cold.
```

**Notes:**
- `la-zo-mi` = agent: my-organism. `zo` (organism) rather than `li` (agent) marks the body as the experiencing entity, consistent with Domain 7 (emotional/experiential states use `zo`). The feeling is bodily, not agentive.
- `no-ha` = negate-thermal = cold / low thermal state. First attested use of `no-ha` in corpus. Contrast: `no-ra` would mean "low energy / power off" — which is a different claim entirely. A cold room with the lights on is `no-ha`; a room with no power is `no-ra`. The two expressions are structurally orthogonal, as required.
- `se` (perceive) with a state (`no-ha`) rather than an entity as patient. `la-zo-mi  se  no-ha` = "my body registers the thermal state of not-warm." This parallels `la-mi  se  fe-de` (I perceive boundary-decay, = I feel afraid) from Domain 7 — the perception of a state, not an event.
- **Contrast test:** `la-zo-mi  se  ra-de` = "my body perceives energy-decrease" — plausible as feeling a power drain but not cold. Semantic distortion confirmed; `ha` required.

---

**S033 — Environmental thermal state** *(T-HA-002)*

*Target: "The room is warm."*

```
Gloss:    lo-pa  ha-vo
Literal:  patient:place  thermal-quality
Natural:  The room [is] warm.
```

**Notes:**
- `ha-vo` = thermal-quality = warmth / warm as a property. Quality (`vo`) applied to thermal state (`ha`): the room has a degree of thermal intensity. First attested use of `ha-vo`.
- Pattern: `lo-X  ha-vo` copula-by-juxtaposition with a quality compound as the predicate. Extends the copula pattern (previously used with simple roots: `lo-mu  de`, `lo-si-mu  ru`) to a compound quality predicate. No new grammar needed — the juxtaposition pattern scales to compound predicates.
- **Contrast test:** `lo-pa  ra-vo` = "the room has energy quality" — could mean electrical load, radiation level, or acoustic pressure. Ambiguous across all `ra` dimensions. `ha-vo` is specific. Semantic distortion confirmed.

---

**S034 — Thermal threshold: machinery** *(T-HA-003)*

*Target: "The engine is overheating."*

```
Gloss:    la-ra-ki-mu  ha-fe
Literal:  agent:engine  thermal-boundary
Natural:  The engine [is at] a thermal limit.
```

**Notes:**
- `ha-fe` = thermal-boundary = overheating threshold / the point where thermal state causes harm or failure. First attested use of `ha-fe`.
- `ra-ki-mu` (W012) = energy-motion-artifact = engine. The engine is not the patient here but the agent in a state-predication: `la-X  state` pattern (agent in preceding position, quality predicate following). This is the same `la-X  quality` predication explored in S030–S031 (P-GP-001 territory), now with a compound quality predicate.
- Notably: `ra-fe` would mean "energy boundary / electrical overload." Both are real conditions a machine can exhibit independently. An engine `ra-fe` is an electrical fault; an engine `ha-fe` is a thermal fault. The distinction is diagnostically significant. `ha` supports precise fault taxonomy.

---

**S035 — Thermal change over time** *(T-HA-004)*

*Target: "The temperature dropped overnight."*

```
Gloss:    lo-ha  de-past  ta-ti-de
Literal:  patient:thermal-state  decreased-PAST  time:past-time
Natural:  The thermal state decreased last night.
```

**Notes:**
- `lo-ha` = patient:thermal-state — treating `ha` as an entity/quantity that can undergo change. This is a nominalized use: `ha` as the patient of `de` (decrease). First nominalized use of a primitive root as a bare quantity noun.
- `ti-de` = time-decay = past time interval (derivationally parallel to `ti-be` W040 = proximate future). Not yet registered. First use in corpus; candidate for W041.
- **Contrast test:** `lo-ra  de-past` = "energy decreased" — means power failure, fuel consumption, force dissipation. None of these capture "temperature fell overnight." The distinction between energy loss and thermal state change is exactly the `ra`/`ha` boundary. Semantic distortion confirmed.
- **Grammar note:** `lo-ha` treating a primitive root as a bare nominalized quantity is new. Previously, primitives appeared as parts of compounds or in particle frames. Using `ha` directly as the patient of a state-change verb tests whether the language allows this. It appears grammatically clean — `lo-[root]  verb` is a standard pattern when the root names a quantity or state directly.

---

**S036 — Food and cooking** *(T-HA-005)*

*Target: "The food is too hot to eat."*

```
Gloss:    lo-ma  ha-fe  —  no [ka-se]
Literal:  patient:matter  thermal-boundary — [negates] [action:perceive/consume]
Natural:  The food is at a thermal limit. [It] cannot be consumed.
```

**Notes:**
- Two-clause structure separated by dash (third time this pattern appears: C001 A2, C004 B2, S036). The second clause expresses the consequence: consuming (`ka-se`) is negated (`no`).
- `no [ka-se]` = negate [intentional-perceiving/consuming]. `ka-se` = intentional perception; eating is perceiving-through-consuming. `no` negates the action frame. This is `no` as a sentence-level negation of a `ka` clause, first such use. Previously `no-` appeared as a compound prefix (`no-de`, `no-ru`, `no-fe`, `no-ha`); here it fronts a full `[ka-clause]`. Flags whether `no` can negate a clause or only compounds. Provisional: yes — `no` fronts the action it negates.
- **Contrast test:** `lo-ma  ra-fe` = "the matter is at an energy boundary" — sounds like radioactive material or an electrical hazard. A hot bowl of soup is `ha-fe`, not `ra-fe`. Register distortion confirmed.

---

**S037 — Thermal retention** *(T-HA-006)*

*Target: "The metal holds heat."*

```
Gloss:    la-mu  ko  lo-ha-ra
Literal:  agent:metal/artifact  contains  patient:thermal-energy
Natural:  The metal contains thermal energy.
```

**Notes:**
- `ha-ra` = thermal-energy = heat as energetic phenomenon (distinct from `ha` alone = thermal state). The metal holds `ha-ra` (heat as a form of energy stored in matter) rather than simply being `ha-vo` (being warm as a quality). This is Monday's recommended split: `ha` = state, `ha-ra` = energy-form.
- `la-mu  ko  lo-X` = agent:artifact contains patient:X. `ko` (containment/interior) used as a verb-equivalent: "encloses, retains." This parallels how `de` and `be` appear in similar predicate positions. First use of `ko` as a predicate rather than as part of a compound.
- Note the difference from S033 (`lo-pa  ha-vo` = the room is warm): S033 describes a current state; S037 describes a material property — the metal's capacity to store thermal energy. State vs capacity is now expressible through `ha-vo` (state) vs `ko  lo-ha-ra` (retention capacity).

---

**S038 — Thermal comfort / habitability** *(T-HA-007)*

*Target: "The reactor must remain cool."*

```
Gloss:    la-ra-ki-mu  wi [lo-ha  no-fe]
Literal:  agent:reactor  intention [patient:thermal-state  not-at-boundary]
Natural:  The reactor [must have] the intention [that its thermal state not reach the boundary].
```

**Notes:**
- `wi [lo-ha  no-fe]` = purpose/obligation clause: "the intended state is thermal-below-threshold." `lo-ha  no-fe` is a nominal description of the target state inside the `wi` frame — not a full action clause but a state description. This tests whether `wi [description]` (rather than `wi [ka-clause]`) is grammatical. Tentatively: yes, `wi` can frame a description of a required state as well as an intended action.
- `no-fe` = not-at-boundary = below the limit / within safe range. Previously used in C004 B2 for epistemic thresholds; here applied to thermal boundaries. Confirms `no-fe` generalizes across boundary types, consistent with `fe`'s domain-consolidation role.
- `la-ra-ki-mu` (W012) as the agent of a `wi` clause: formally, the reactor cannot have will or intention. This is institutional shorthand — "the reactor must remain cool" is really "the operators must keep it cool." The agent inherits from surrounding discourse context. Flags whether non-intentional `mu` agents are grammatically licit in `wi` clauses. Likely: yes in prescriptive/institutional register; constraint is social, not grammatical.

---

**S039 — Thermal comparison / gradation** *(T-HA-008)*

*Target: "The water is cooler than the air."*

```
Gloss:    lo-ma-di  ha-vo  nu-no  lo-pa-ma
Literal:  patient:water  thermal-quality  less  patient:air-matter
Natural:  The water [has] less thermal quality than the air.
```

**Notes:**
- `nu-no` = quantity-negation = less / fewer / reduced by comparison. First comparative construction in corpus. `nu` (quantity) + `no` (negation) = less-than. The structure: `lo-A  quality  nu-no  lo-B` = "A has the quality to a lesser degree than B." Clean and compositional.
- `pa-ma` = place-matter = air / atmosphere (the matter of the place/surrounding space). Transparent compound; not registered separately. `ma` (matter/substance) + `pa` (place/space) = the diffuse matter of the surrounding environment = air.
- **`ha-vo` in comparison.** The gradable nature of `ha-vo` is confirmed: it can take a quantitative modifier (`nu-no`). This is consistent with `vo` as "degree/intensity" — `ha-vo` names thermal intensity, and intensity is measurable. The comparison construction likely generalizes: `lo-X  [quality]  nu-no  lo-Y` = "X has less [quality] than Y."
- **Grammar note:** This is the first comparative in corpus. Comparative grammar is now attested even if not formalized. The `nu-no` construction is provisional; other framings possible (e.g., `lo-A  ha-vo-de  ne  lo-B`). Log as a pending formalization item.

---

### `ha` Validation Summary

| Sentence | Domain | `ra` replacement result | Verdict |
|----------|--------|------------------------|---------|
| S032 `la-zo-mi  se  no-ha` | Bodily | `ra-de` = power-down ≠ cold | **ha required** |
| S033 `lo-pa  ha-vo` | Environment | `ra-vo` = ambiguous energy-intensity | **ha required** |
| S034 `la-ra-ki-mu  ha-fe` | Machinery | `ra-fe` = electrical fault (distinct condition) | **ha required** |
| S035 `lo-ha  de-past` | Temporal change | `lo-ra  de` = power failure | **ha required** |
| S036 `lo-ma  ha-fe` | Cooking | `ra-fe` = radioactive/electrical hazard | **ha required** |
| S037 `la-mu  ko  lo-ha-ra` | Material property | `ha-ra` = thermal energy; `ra` alone inadequate | **ha-ra split confirms** |
| S038 `wi [lo-ha  no-fe]` | Institutional requirement | `ra` compounds: no clean path | **ha required** |
| S039 `lo-ma-di  ha-vo  nu-no  lo-pa-ma` | Comparison | `ra-vo` = energy intensity comparison ≠ thermal | **ha required** |

**All eight sentences require `ha`. Zero false positives (no sentence where `ra` would have worked cleanly). `ha` promoted from candidate to confirmed primitive.**

Secondary findings from this batch:
- `ti-de` (past time) confirmed; candidate W041
- `ko` as a verb-equivalent predicate (S037) — first such use
- `no [ka-clause]` as sentence-level negation (S036) — needs formalization
- Comparative `nu-no` construction (S039) — first attested comparative; formalize

---

## X-X Repetition Test Batch (S040–S044)

**Purpose:** Test whether doubling a primitive root (X-X) produces a stable, unambiguous meta-level reading via ordinary head-final compounding alone — with no new grammatical mechanism. Five pairs: `to-to`, `su-su`, `ka-ka`, `se-se`, `ne-ne`. All sentences are intentionally spare to isolate the compound.

---

**S040 — Meta-concept (abstraction)** *(T-XX-001)*

*Target: "The standards framework is a meta-conceptual system."*

```
Gloss:    lo-to-fe-su  to-to-su
Literal:  patient:concept-boundary-arrangement  concept-of-concepts-arrangement
Natural:  The standards framework is a system of meta-concepts.
```

**Notes:**
- `to-to` = "conceptual-pattern of conceptual-patterns." Head-final: `to` (concept) as head, modified by `to` (concept) = the conceptual layer above concepts = meta-concept / abstraction. No new mechanism. This is the ordinary compound rule where modifier and head happen to be the same root.
- `to-fe-su` = concept-boundary-arrangement = the epistemic standards framework (established in epistemic domain registry). It is a formalized structure of rules about how conceptual categories are bounded — i.e., it is literally constructed from meta-concepts. The test subject is load-bearing.
- `to-to-su` = meta-concept-formal-arrangement. The `su` head confirms this is a physical/organizational arrangement per specification (`su` excludes mental models). The arrangement contains meta-conceptual material: epistemic thresholds, promotion criteria, boundary rules. This is a structured formal framework, not airy philosophy.
- **Spec constraint enforced:** `su` is NOT "abstract organized knowledge." It is organizational arrangement. `to-to-su` is a formally structured system; the abstraction lives in `to-to`, not in `su`.
- **T-XX-001 verdict:** Parses cleanly. `to-to` is unambiguous and compositionally inferrable.

---

**S041 — Meta-structure (architecture)** *(T-XX-002)*

*Target: "A network is a structure of structures."*

```
Gloss:    lo-ne-su  su-su
Literal:  patient:connection-arrangement  structure-of-structures
Natural:  A network is a meta-structure / has an architectural form.
```

**Notes:**
- `su-su` = "structure whose elements are themselves structures." Head-final: `su` (structure/arrangement) as head, modified by `su` = the organizational level above individual structures = meta-architecture / architecture / topology of organizational form.
- `ne-su` = connection-arrangement = a network as a physical/organizational system (head `su`, modifier `ne` = connection). A network is a natural test case: it is genuinely composed of structured elements (nodes, links, subnets) arranged into a higher-level structure. `ne-su` is a `su-su` — not metaphorically, factually.
- The copular juxtaposition pattern `lo-X  compound` is consistent with S032–S039 corpus. No new grammar.
- Contrast with `ne-ne` (S044): `ne-su` is the physical network; `su-su` describes its meta-structural character; `ne-ne` is its topological description. Three distinct levels, all derivable from two primitive roots.
- **T-XX-002 verdict:** Parses cleanly. `su-su` gives a precise engineering meaning: architecture-of-architectures, meta-organization.

---

**S042 — Action-governance (procedure, protocol)** *(T-XX-003)*

*Target: "Operations require action-governance."*

```
Gloss:    la-ka-ki  wi  ka-ka
Literal:  agent:action-motion  intends  action-of-actions
Natural:  Operations require procedure / protocol.
```

**Notes:**
- `ka-ka` = "action whose scope is actions." Head-final: `ka` (deliberate action) as head, modified by `ka` = deliberate action directed at the regulative frame of actions = procedure, protocol, governance of action, operational oversight.
- `la-ka-ki` = agent:action-motion = "the entity that is operational movement through its steps." Using a process-compound as the subject, parallel to C004 `la-se-ka` (inanimate process in agent slot). `ka-ki` = deliberate-action + motion = an operation proceeding through stages = ongoing maintenance/operations activity.
- `wi [ka-ka]` = purpose frame (spec/grammar.md § Purpose Frame): the operations activity is oriented toward / requires action-governance. Natural and unforced — a process that must follow a protocol is exactly the use case where `ka-ka` would appear.
- Contrast `ka-ka` with `ka-su` (action-arrangement = an operational system) and `ka-to` (abstract-nominalization of action = "doing" as a concept). `ka-ka` is specifically the regulative layer: the governance of what actions are permissible and how they must sequence.
- **T-XX-003 verdict:** Parses cleanly. `ka-ka` = procedure/protocol is the most socially productive of the five — governance, oversight, safety protocols, maintenance checklists all fall here.

---

**S043 — Sensor self-monitoring (introspection)** *(T-XX-004)*

*Target: "The relay device performs sensor self-monitoring."*

```
Gloss:    la-si-mu  ka  se-se
Literal:  agent:signal-device  does  perception-of-perception
Natural:  The relay device performs sensor self-monitoring.
```

**Notes:**
- `se-se` = "perception whose object is perception." Head-final: `se` (raw sensory awareness / detection) as head, modified by `se` = the detection of one's own detection state = sensor self-monitoring / introspection / calibration check.
- `si-mu` = signal-device (W039). Natural subject — relay units checking their own sensor state is a routine Concordian engineering operation.
- **Critical correction enforced here:** Monday's analysis glossed `se-se` as "methodology / evidence evaluation." That reading violates the primitive specification. `se` excludes processed knowledge (use `to`) and deliberate analytical action (use `ka`). Evidence evaluation requires `to` or `ka` carrying the weight. `se-se` is strictly perception-of-perception: it does not have a lab coat. A device running `se-se` is checking whether its own sensors are detecting accurately. A device running `to-se` is reasoning about what its sensors detected. The distinction is technically meaningful in Concordian engineering contexts.
- The narrowness is a feature: `se-se` is precise because `se` is precise. The spec constraint works as designed.
- **T-XX-004 verdict:** Parses cleanly. Meaning is narrow and correct — *only* after enforcing the primitive specification. This is the sharpest test in the batch: the X-X compound is only useful because the base primitive is well-defined.

---

**S044 — Network topology (relation-of-relations)** *(T-XX-005)*

*Target: "The transit grid is a topology."*

```
Gloss:    lo-ki-ne  ne-ne
Literal:  patient:motion-connection  relation-of-connections
Natural:  The transit grid has a topological structure.
```

**Notes:**
- `ne-ne` = "relation whose scope is relations." Head-final: `ne` (connection/relation) as head, modified by `ne` = the structural pattern of how connections relate to one another = topology.
- `ki-ne` = motion-connection = a transit link / route connection. A transit grid (`lo-ki-ne` = patient:transit-link, used here for the grid as a whole by the established pattern of using a constituent compound to stand for the system). The topological claim is about the grid's higher-order structure: not its individual links, but how the links relate.
- Contrast `ne-su` (connection-arrangement = the network as a physical system) with `ne-ne` (how connections are themselves connected = topological description). In formal register a Concordian might say `lo-ne-su  ne-ne-su` = "the network has a topological structure" using `su` to formalize `ne-ne` as an arrangement. S044 uses the bare copular form to test the compound in isolation.
- `ne-ne` is the most abstract of the five X-X tests. It describes a second-order property: not the connections, but the pattern of how connections are organized relative to each other. Engineering-useful in grid analysis, network design, relay routing.
- **T-XX-005 verdict:** Parses cleanly. `ne-ne` achieves a meaning — topology / relational pattern — that no non-doubled compound reaches as directly.

---

### X-X Repetition Test Summary

| Sentence | X-X compound | Reading | Verdict |
|----------|-------------|---------|---------|
| S040 `lo-to-fe-su  to-to-su` | `to-to` | meta-concept / abstraction | **stable** |
| S041 `lo-ne-su  su-su` | `su-su` | meta-structure / architecture | **stable** |
| S042 `la-ka-ki  wi  ka-ka` | `ka-ka` | action-governance / procedure | **stable** |
| S043 `la-si-mu  ka  se-se` | `se-se` | sensor self-monitoring / introspection | **stable — requires spec precision** |
| S044 `lo-ki-ne  ne-ne` | `ne-ne` | topology / relation-of-relations | **stable** |

**Batch conclusion:** All five X-X compounds parse consistently using ordinary head-final compounding. No new grammatical mechanism is needed. The meta-level reading is a natural consequence of head-final structure when modifier = head. The quality of the X-X reading is entirely dependent on the precision of the base primitive — `se-se` is the sharpest illustration: the narrow spec definition of `se` directly constrains `se-se` to sensor self-monitoring, blocking the "methodology" overreach. The spec precision is load-bearing.

**Not yet formalized.** Two open items must be resolved before X-X is written into word-formation.md: (1) the `-to` suffix / `to-` compound head collision (logged in open-questions); (2) a second corpus round testing contrastive X-X vs X-Y pairs in the same domain to confirm the meta-level reading is stable against compound alternatives.

---

## Compound Grouping Test (S045)

**Purpose:** Verify that the proposed apostrophe grouping marker `'` earns its weight — i.e., that a genuine ambiguity arises from plain hyphenated chains once the X-X meta pattern is established, and that `'` resolves it to two distinct, non-equivalent readings.

---

**S045 — Compound grouping disambiguation** *(T-APO-001)*

*Target: "The standards adjudicator operates through [a formal method / an engineering doctrine]."*
*Purpose: three-way comparison — ungrouped (ambiguous), and two distinct grouped readings.*

**Attempt A — ungrouped:**

```
Gloss:    la-to-fe-li  wi  to-to-se-ma-ka
Literal:  agent:concept-boundary-person  intends  concept-concept-perception-matter-action
Natural:  The standards adjudicator operates through [???].
```

Ambiguous. Default right-branching gives Parse C; X-X recognition gives Parse B. A reader cannot determine which is intended.

---

**Attempt B — `to-to'se-ma-ka` (X-X applied to inspection):**

```
Gloss:    la-to-fe-li  wi  to-to'se-ma-ka
Parse:    [to-to] + [se-ma-ka]
Literal:  agent:concept-boundary-person  intends  [meta-concept][observation-of-material-work]
Natural:  The standards adjudicator operates by applying formal theory to material inspection.
```

`to-to` = meta-concept / abstraction (X-X, attested S040). `se-ma-ka` = observation of material action = inspection of physical work. The `'` marks `se-ma-ka` as a pre-bound unit; the X-X compound modifies it as a whole. Reading: **active and procedural** — abstraction being used as a tool on a specific domain.

---

**Attempt C — `to'to-se-ma-ka` (outer concept wrapping theory of inspection):**

```
Gloss:    la-to-fe-li  wi  to'to-se-ma-ka
Parse:    to + [to-se-ma-ka]
Literal:  agent:concept-boundary-person  intends  [concept-of][theory-of-inspection]
Natural:  The standards adjudicator operates per the engineering verification doctrine.
```

`to-se-ma-ka` = conceptual framework for inspecting material work = engineering verification theory / doctrine. The outer `to` nominalizes it as a conceptual object: a specific established framework being cited. Reading: **referential and doctrinal** — the authority invokes a named body of method.

---

**Notes:**
- **The ambiguity is real.** Without X-X, `to-to-se-ma-ka` reads by pure right-branching as Attempt C. Once X-X = meta-concept is an established pattern (S040–S044), the first two `to`s draw the eye as a unit and Attempt B becomes an equally valid parse. Ungrouped Attempt A is genuinely ambiguous after S040.
- **B ≠ C in Concordian formal register.** B = a procedure being actively performed (a method). C = a doctrine being cited (a named framework). In institutional contexts where `to-fe-li` figures operate, this distinction determines how a claim is classified — method vs. authority.
- **`'` directionality rule used here is consistent:** `'` marks the left boundary of a subcompound. `A-B'C-D` = plain chain `[A-B]` modifies pre-bound unit `[C-D]`. `A'B-C-D` = single modifier `A` attaches to pre-bound unit `[B-C-D]`. Both directions attested in one sentence set.
- **Phonological status of `'` unresolved.** See open-questions.md. Whether the two readings are also phonologically distinct depends on that resolution.
- **T-APO-001 verdict: `'` earns its weight.** The ungrouped form is genuinely ambiguous post-S040. The two grouped forms are unambiguous, non-equivalent in meaning, and compositionally transparent.

---

## Double Apostrophe Test (S046)

**Purpose:** Determine what two apostrophes mean under the current rule (`'` = left boundary of subcompound). Test whether `A'B'C-D` produces (i) a nested tree (current rule → A modifies `[B modifies [C-D]]`) or (ii) flat coordination (`[A] [B] [C-D]` as parallel chunks). Determine whether the nested form is useful or whether multi-apostrophe compounds should always be restructured as phrases.

The concept under test: the abstract study of how embodied persons derive concepts from perception (roughly: philosophy of mind, cognitive theory). Three approaches.

---

**S046 — Two apostrophes: nested vs. phrase restructuring** *(T-APO-002)*

*Target: "Concordian scholars study the theory of how persons derive concepts from perception."*

**Attempt A — two apostrophes (nested, current rule):**

```
Gloss:    la-to-li  ka  to-to'ma-li'ne-se-to
Parse:    to-to modifies [ma-li modifies [ne-se-to]]
Literal:  agent:concept-person  does  meta-concept [embodied-person [perceptual-conceptual-relation]]
Natural:  Concordian scholars engage in the meta-theory of how embodied persons build conceptual relations from perception.
```

Nested reading under the left-boundary rule, working inside-out:
- `ne-se-to` = relation (`ne`) of perceived (`se`) conceptual patterns (`to`) = a conceptual relation grounded in observation
- `ma-li'ne-se-to` = `ma-li` modifies `[ne-se-to]` = the perceptual-conceptual relations *of* an embodied person = how a physical being generates grounded concepts from what they sense
- `to-to'ma-li'ne-se-to` = meta-concept applied to `[ma-li'ne-se-to]` = the abstract theoretical study of that whole process

This is coherent and compositionally traceable, but requires the reader to apply the nesting rule twice in succession — two left-boundary resolutions before arriving at the final meaning.

---

**Attempt B — phrase restructuring (recommended):**

```
Gloss:    la-to-li  ka  to-to  ne  ma-li'ne-se-to
Literal:  agent:concept-person  does  meta-concept  relation  [embodied-person][perceptual-conceptual-relation]
Natural:  Concordian scholars engage in the meta-theory that is connected to how embodied persons build conceptual relations from perception.
```

`ne` (relation/connection) serves as an explicit connective particle between the outer meta-concept and the inner compound. The single-apostrophe subcompound `ma-li'ne-se-to` is well within the established S045 pattern. Reading is unambiguous and requires only one `'` resolution. The `ne` particle does the structural work that the second `'` was trying to do.

---

**Attempt C — two-sentence split (maximum clarity):**

```
Sentence 1:  lo-ma-li  ne-se-to  ka
             Embodied persons construct perceptual-conceptual relations.

Sentence 2:  lo-ne-se-to-su  to-to
             The study of that is a meta-conceptual framework.
```

Two short sentences, no apostrophes needed. Unambiguous. The formal register equivalent of what Attempt A compressed into one word.

---

**Notes:**
- **Attempt A is grammatically legal under the current rule** — two nested `'` markers produce a well-formed tree. But the cognitive load of resolving two left-boundary operations in sequence is high, even for a formal register reader. The nesting is correct; the readability is strained.
- **Attempt B is the recommended form.** `ne` as an explicit connective between two subcompound units costs one extra morpheme and gains full parse transparency. This is consistent with the ambiguity-resolution rule in word-formation.md: "shortest valid *unambiguous* form" — Attempt A is shorter but not unambiguous on first read; Attempt B is the shortest *clearly* unambiguous form.
- **Attempt C confirms the phrase-split option.** The two-sentence form has zero parse complexity and fits the spec's contraction rule: "if a compound requires more than one apostrophe, restructure as a phrase." This is the pattern to recommend in the usage policy.
- **The `ma-li` / `-li` suffix collision appears here.** `ma-li` is parsed as modifier + root (`ma` = matter, `li` = social agent = "embodied person"). But `-li` is also the derivational suffix meaning "one who does" (morphology.md). The forms are identical: `ma-li` (compound) vs `ma-li` (matter + doer-suffix = "one who works with matter / material agent"). The two readings are semantically close enough to be genuinely confusing in some contexts. Logged in open-questions.md.
- **T-APO-002 verdict:** Two apostrophes produce nested structure that is legal but strains readability. Usage policy update: **compounds requiring more than one `'` should be restructured as phrases** (Attempt B or C). Single `'` confirmed as the practical limit. This closes the remaining prerequisite for adopting `'` into word-formation.md.

---

## Suffix–Root Collision Batch (S047–S055)

**Purpose:** Three derivational suffixes share their form with primitive roots: `-to` / `to`, `-li` / `li`, `-se` / `se`. The question is whether context reliably disambiguates the two readings in realistic sentences, or whether structural resolution is required. Each pair gets three sentence slots: (A) suffix reading clearly dominant, (B) compound-head reading clearly dominant, (C) both readings structurally valid — verdict on whether meaning differs.

---

### Pair 1: `-to` (abstract nominalization) vs `to-` (conceptual framework)

**S047A — `-to` suffix reading** *(T-SFX-001)*

*Target: "Maintenance is a difficult concept."*

```
Gloss:    lo-ka-mu-to  fe-ki
Literal:  patient:action-device-[concept-of]  boundary-intense
Natural:  The concept of device-maintenance is complex.
```

`ka-mu-to` = action (`ka`) + device (`mu`) + abstract-nominalization (`-to`) = "the concept of maintaining devices." The `-to` suffix nominalizes `ka-mu` into an abstract concept-thing. The reading is unambiguous: there is nothing here for `to` as a compound head to modify — it sits at the end of a three-part derivation chain with no following root for it to govern.

**Verdict A: `-to` suffix reading is primary and unambiguous in final position with no following root.**

---

**S047B — `to-` compound-head reading** *(T-SFX-002)*

*Target: "The fault theory predicts cascade failure."*

```
Gloss:    lo-to-de-ne  du  lo-ne-de-ki
Literal:  patient:concept-decay-relation  produces  patient:connection-decay-motion
Natural:  The theory of fault propagation produces cascade failure.
```

`to-de-ne` = `to` (conceptual framework) as head, modified by `de-ne` (decay-relation = fault-propagation pattern). This is `to` as compound head: it governs the whole right-branching compound. A `-to` suffix reading would require `to` to follow a root and nominalize it (`de-ne-to`), which would have a different word order. Here `to` is unambiguously the head of the compound, not a suffix, because it comes *first*.

**Verdict B: `to-` compound-head reading is primary and unambiguous when `to` appears at the left (head position). Suffix can only appear at the right edge.**

---

**S047C — structural ambiguity test** *(T-SFX-003)*

*Target: "The relay device concept is stable."*

```
Form:     lo-si-mu-to  ru
```

Two valid parses:

- Suffix: `si-mu` (relay device, W039) + `-to` (abstract nominalization) = "the concept of the relay device" → the thing being evaluated is an abstract idea
- Compound: `si-mu-to` right-branching, `to` as head modified by `si-mu` = "a conceptual framework in the domain of signal-devices" → the thing being evaluated is a body of doctrine about relay devices

Both parse as `lo-[form]  ru` = "the [X] is stable/coherent." The two readings are genuinely non-equivalent: stability of *a concept* vs stability of *a doctrine* are different claims. Context (is this a philosophical statement or an engineering review?) would resolve it in speech, but the written form is ambiguous.

**Verdict C: genuine ambiguity exists at the right edge when `to` follows a two-morpheme compound. The two readings are non-equivalent. Resolution: word-formation convention should specify that `-to` suffix is written without hyphen separation (`simu-to`) while the compound head form retains the hyphen (`si-mu-to`), making the boundary explicit in writing. Log as pending convention decision.**

---

### Pair 2: `-li` (agent suffix) vs `li` (social agent root)

**S048A — `-li` suffix reading** *(T-SFX-004)*

*Target: "The signal analyst identified the fault."*

```
Gloss:    la-si-to-li  ka  lo-de-ne
Literal:  agent:signal-concept-[one-who-does]  does  patient:decay-relation
Natural:  The signal analyst identified the fault.
```

`si-to-li` = signal (`si`) + conceptual-framework (`to`) + agent-suffix (`-li`) = "one who performs conceptual work on signals" = signal analyst. The `-li` suffix is final, nominalizing `si-to` into a person-type. The `li` root reading would require treating this as a three-root compound with `li` (social agent) as head: "a social agent in the domain of signal-concepts." That reading is semantically identical to the suffix reading — both describe a person who works with signal knowledge.

**Verdict A: `-li` suffix and `li`-as-head compound produce the same meaning when `li` is final. No practical ambiguity here — the two analyses converge.**

---

**S048B — `li` root reading (distinct from suffix)** *(T-SFX-005)*

*Target: "Relay operators are social nodes in the network."*

```
Gloss:    lo-si-mu-li  ne  lo-ne-su
Literal:  patient:signal-device-person  relation  patient:connection-arrangement
Natural:  Signal-device operators are relational members of the network.
```

`si-mu-li` = signal (`si`) + device (`mu`) + social-agent (`li`) = "person associated with signal devices" = relay operator. The `li` root carries its full meaning as a social agent — it's not just nominalizing; it's specifying that the entity is a *person-type*, distinct from a device (`si-mu-mu` = device-of-devices) or a process. A `-li` suffix reading would also work here (one who operates signal devices), and again converges to the same referent.

**Verdict B: confirmed from both sides — `-li` suffix and `li` root-as-head consistently converge when the role is "person who does/uses X." The divergence would only appear if `li` carried social-agent meaning that `-li` does not (i.e., if `-li` is purely formal-nominalization and `li` root implies full social standing). Currently no corpus evidence of that distinction mattering.**

---

**S048C — potential divergence test** *(T-SFX-006)*

*Target: "An AI system is not a person."*

```
Form:     lo-to-mu-li  no  lo-mu-li
Gloss:    lo-to-mu-li = concept-device-person   lo-mu-li = device-person
```

- `to-mu-li`: concept (`to`) + device (`mu`) + `li` — head-final compound. `li` as root = "a social agent whose nature is that of a conceptual device" = an entity with person-status in the conceptual-device domain. In Tonesu ontology, an AI fitted with person-status would be `to-mu-li` (a conceptual device acknowledged as a social agent — per primitives.md: "AI/institutions are `mu + li`").
- `to-mu-li` with `-li` suffix nominalization = "one who operates conceptual devices" = a knowledge-worker. Entirely different referent.

The same three-syllable form means either (a) an entity *being* a social agent of a certain type, or (b) a person *doing* something with conceptual devices. In a sentence asserting or denying personhood, this ambiguity is semantically significant.

**Verdict C: genuine ambiguity exists and the two readings are non-equivalent in contexts where personhood or agency status is being asserted. The `-li` suffix (role) vs `li` root (being) distinction should be preserved and made explicit. Same hyphen-boundary convention as `-to` applies: `tomu-li` = suffix (role); `to-mu-li` = compound (being). Log as pending convention decision alongside `to`/`-to`.**

---

### Pair 3: ~~`-se`~~ `-ge` (quality/property suffix) vs `se` (perception root)

> **Rename note (post-test):** the quality/property suffix was `-se` when these sentences were written. S049C confirmed the collision was genuine and non-trivial. The suffix was subsequently renamed to `-ge` (no root conflict). The forms below are preserved verbatim as the test evidence that motivated the rename. In current Tonesu: S049A quality reading = `lo-si ra-ge`; S049C quality reading = `la-ra-ge se lo-de-ne`.

**S049A — ~~`-se`~~ `-ge` suffix reading** *(T-SFX-007)*

*Target: "The signal is energetic."*

```
Gloss:    lo-si  ra-se
Literal:  patient:signal  energy-[quality]
Natural:  The signal is energetic / high-energy.
```

`ra-se` = energy (`ra`) + quality-suffix (`-se`) = energetic, the canonical example from morphology.md. The `-se` suffix derives an adjective from a root. The `se` root reading would give `ra-se` as "perception of energy" — a compound meaning "energy detection / energy sensing." These are genuinely different: "the signal is energetic" vs "the signal is an energy-perception." In a predicate position (`lo-si  ra-se`) context disambiguates: quality predicates describe the subject, so the quality reading is dominant.

**Verdict A: `-se` quality suffix is primary in predicate position. The `se`-as-root perception reading would not function as a predicate quality.**

---

**S049B — `se` root reading (distinct from suffix)** *(T-SFX-008)*

*Target: "Energy detection failed."*

```
Gloss:    lo-ra-se  de-past  ta-ti-de
Literal:  patient:energy-perception  decayed  at-past-time
Natural:  The energy sensor / energy detection failed at some past time.
```

`ra-se` = energy (`ra`) + perception (`se`) = "energy sensing / the act of perceiving energy" = a sensor or detection process. This is `se` as a full root in a compound, not a quality suffix. The entity referred to is a *process* or *device*, not a quality. Used as the subject of `de` (decay/failure), it is clearly nominal — it is a thing that failed, not a quality being predicated.

**Verdict B: `se` root reading is primary in subject/nominal position. A quality suffix cannot be a subject.**

---

**S049C — ambiguity test** *(T-SFX-009)*

*Target: "The energetic sensor detected the fault."*

```
Form:     la-ra-se  se  lo-de-ne
```

Two parses:

- `-se` suffix: `ra-se` = energetic (quality) → `la-ra-se` = "the energetic one / one characterized by energy." Sentence: "the energetic [entity] perceived the fault."
- `se` root: `ra-se` = energy-perception = an energy sensor → `la-ra-se` = "the energy sensor." Sentence: "the energy sensor detected the fault."

Both are syntactically valid. The verb `se` (perception, used here as a predicate) is the same root as the suffix, which makes the sentence unusually dense with `se`. The two readings produce different subjects (a quality-characterized entity vs a specific sensor device) and therefore different sentences.

**Verdict C: genuine ambiguity in agent position. The encoded quality and the perception root produce non-equivalent referents. The `-se` suffix is flagged as unstable in morphology.md for exactly this reason — this sentence confirms that instability experimentally. The hyphen-boundary convention proposed for `-to` and `-li` would help here too: `ra-se` = the sensor (compound); `rase` = energetic (derived quality). However, the morphology.md flag ("justification or rename required before this suffix is considered stable") should be escalated: this pair generates the sharpest collision of the three. Log for targeted resolution.**

---

### Suffix–Root Collision Summary

| Pair | Suffix form | Root form | Converge or diverge? | Action |
|------|------------|-----------|---------------------|--------|
| `-to` / `to` | final nominalizer | left-edge compound head | **diverge** — concept-of vs doctrine-about | hyphen-boundary convention |
| `-li` / `li` | role nominalizer | being/status root | **converge** for role contexts; **diverge** for personhood assertion | hyphen-boundary convention; flag personhood edge case |
| ~~`-se`~~ `-ge` / `se` | quality suffix | perception root | **diverge** — quality-predicate vs sensor-compound | **resolved: suffix renamed to `-ge`** (S049C attested collision) |

**Batch conclusion:** Context disambiguates reliably **when the syntactic position is unambiguous** (suffix only in predicate or derivational position; root only in nominal/agent/subject position). Ambiguity arises specifically at **the right edge of a multi-root compound in nominal position**, where both analyses are structurally valid. The proposed resolution — hyphen-boundary notation distinguishing `X-Y-Z` (compound, root final) from `XY-Z` (root chain + suffix) — would eliminate all three collision cases in writing without changing the spoken forms. Log as a single pending convention decision covering all three pairs.

---

## Primitive Pressure Tests (S056–S057)

*Testing whether transfer/exchange and need/functional-dependency force a new primitive, or compose cleanly from existing roots.*

---

**S056 — Transfer / giving** *(T-PRM-001)*

*Target: "She gave the archive to the council."*

```
Gloss:    la-ze  ne-li-pu-su  lo-si-su  de
Literal:  agent:she  recipient:council  patient:archive  release
Natural:  She released the archive to the council.
```

Breakdown:
- `ze` = 3rd-person pronoun (she)
- `si-su` = structured encoded representation = archive / database / document collection
- `li-pu-su` = organized structure of many social agents = council / body / institution
- `ne` = recipient particle (already in grammar.md particle table)
- `de` = release / relinquish — from the giver's perspective, their possession decreases

The `ne` recipient particle + `de` predicate handles giving-with-release cleanly. No additional root or compound needed for this case.

**However:** this only covers giving where the giver loses possession. "She sent a copy to the council" — where she retains the original — has no clean expression. `de` (release/decrease) implies the giver's possession ends. A pure transfer without loss would need `ki` (motion from) + `ne` (toward), but that reads as "the archive moved toward the council" rather than "she transferred it." The agentive transfer-without-loss case is the actual pressure point, not the simple gift.

**Verdict S056: giving-with-release composes cleanly (`ne-particle` + `de`). The pressure point is transfer-without-loss (copy/share rather than give). Downgrade from gap to compound candidate: `de-ki-be` or a lexicalized `ka-ne` (intentional-toward-recipient) for agentive transfer. Monitor corpus.**

---

**S057 — Need / functional dependency** *(T-PRM-002)*

*Target: "The patient needs water."*

Attempt A — paraphrase via consequence structure:

```
Gloss:    lo-zo-li  no-ma  go  de
Literal:  patient:person  absence-substance  cause  decay
Natural:  For the person, absence of substance causes decay.
```

Attempt B — desire frame (wrong register but testing the fit):

```
Gloss:    la-zo-li  wi  lo-ma
Literal:  agent:person  wants  patient:substance
Natural:  The person wants substance.
```

Attempt A is **semantically precise** but pragmatically reframes the proposition. The speaker has to describe the consequence structure instead of the state. "The patient needs water" is a claim about current dependency; Attempt A is a claim about causal architecture. These are not the same claim — Attempt A is an explanation of why (`no-ma go de`), not a characterization of the patient's current state.

Attempt B is wrong: `wi` = volitional desire. An unconscious patient has no `wi` active.

Neither attempt preserves the target meaning without distortion. There is no clean way to say "X requires Y to maintain integrity" as a **state predication** rather than a **causal prediction**.

**Verdict S057: genuine gap confirmed. Need/functional-dependency is not expressible as a state — only as a consequence chain. This is semantic distortion, not verbosity. The concept is: `X is in a condition where absence of Y → de`. Candidate compound: `ne-fe` (relation-boundary = dependency condition) or a new root. Log as pending primitive evaluation.**
