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

---

**S058 — Need: `ne-fe` compound test** *(T-PRM-003)*

*Target: "The patient needs water."*

*Testing whether `ne-fe` (relation-boundary = dependency condition) resolves S057's gap without a new primitive.*

```
Gloss:    lo-zo-li  ne-fe  ma
Literal:  patient:person  dependency-condition  substance
Natural:  The person needs substance / the person is in a dependency-condition toward substance.
```

Breakdown:
- `zo-li` = living social agent = person / patient
- `ne-fe` = compound: relation (`ne`) + boundary/limit (`fe`) = a relation that must be maintained; a dependency condition
- `ma` = raw matter / substance (water is the canonical `ma`; no more specific root exists)
- `ne-fe` occupies the predicate slot (after the `lo`-marked patient); `ma` follows as the complement — the substance of the dependency

**Parsing disambiguation:** `ne` is both a root (relation/connection) and a particle (recipient marker). In this sentence, `ne` could theoretically be read as the recipient particle, giving `ne-fe  ma` = "recipient:boundary  substance" — which doesn\'t parse (the particle expects a noun phrase, not a root `fe` fused to it). The compound reading `ne-fe` as a single predicate is unambiguous in the predicate slot.

**Contrast with S057 causal paraphrase:**

| Form | Expression | Type of claim |
|------|------------|---------------|
| S057 | `lo-zo-li  no-ma  go  de` | causal prediction — "if no substance, decay follows" |
| S058 | `lo-zo-li  ne-fe  ma` | state description — "the person is in a dependency-condition toward substance" |

The S058 form describes the **current state** of the person, not a predicted consequence. These are different propositions: S057 says what will happen; S058 says what is true now.

**Verdict S058: `ne-fe` bridges the gap. The compound produces a genuine state predication without causal reframing.** The primitive system survives without a new root. `ne-fe` should be registered as a stable compound for dependency/requirement conditions. No new primitive.

---

## `ne-fe` Generality Stress Test (S059–S063)

*Testing whether `ne-fe` is genuinely general or accidentally lucky. Five sentences across distinct subject types, object types, and negation.*

---

**S059 — Child needs sleep** *(T-PRM-004)*

*Target: "The child needs sleep."*

```
Gloss:    lo-li-be  ne-fe  zo-no-ki
Literal:  patient:child  dependency-condition  living-non-motion
Natural:  The child needs sleep / rest.
```

- `li-be` = person in growth phase = child (W033)
- `zo-no-ki` = living + negation + motion = living-stillness = rest/sleep. Head-final: `ki` (motion) is the head; `no-ki` = non-motion; `zo-no-ki` = the non-motion state of a living body.
- `ne-fe` = dependency-condition (W042)

**Verdict S059: clean.** New compound `zo-no-ki` (sleep/rest) emerges naturally. No ambiguity. `ne-fe` holds in child + biological-state context.

---

**S060 — Machine needs cooling** *(T-PRM-005)*

*Target: "The machine needs cooling."*

```
Gloss:    lo-mu  ne-fe  ha-de
Literal:  patient:artifact  dependency-condition  thermal-decrease
Natural:  The machine needs cooling.
```

- `mu` = artifact/device
- `ha-de` = thermal-state + decrease = the process of heat reduction = cooling. Head-final: `de` (decay/decrease) is the head; `ha` specifies the domain of decrease.
- `ne-fe` = dependency-condition

**Verdict S060: clean.** `ha-de` (cooling) is a natural compound parallel to `ha-be` (heating). `ne-fe` holds for artifact + physical-process context.

---

**S061 — City needs water** *(T-PRM-006)*

*Target: "This city needs water."*

```
Gloss:    lo-li-pu-pa  ne-fe  ma
Literal:  patient:city  dependency-condition  substance
Natural:  The city needs water / substance supply.
```

- `li-pu-pa` = city (W036)
- `ma` = raw matter / substance; water is the canonical `ma` in prior corpus usage
- `ne-fe` = dependency-condition

**Verdict S061: clean.** `ne-fe` scales to collective institutional subjects. `lo-li-pu-pa` is a long patient phrase but parses unambiguously — particle `lo` scopes all the way to the predicate slot.

---

**S062 — Team needs a plan** *(T-PRM-007)*

*Target: "The team needs a plan."*

```
Gloss:    lo-li-pu  ne-fe  wi-to
Literal:  patient:collective  dependency-condition  intentional-pattern
Natural:  The team needs a plan / purposive structure.
```

- `li-pu` = persons-collective = team / group
- `wi-to` = will/intention + conceptual pattern = a pattern governed by intention = plan / strategy. Head-final: `to` (conceptual pattern) is the head; `wi` specifies that the pattern is purposive/goal-directed.
- `ne-fe` = dependency-condition

**Verdict S062: clean.** `wi-to` (plan) is a useful new compound. `ne-fe` holds for collective + abstract-object context. Note: `to-wi` would mean "intention characterized by pattern = deliberate will" — subtly different (more motivation than plan). `wi-to` as "intentional design/plan" is the correct head-final reading.

---

**S063 — Patient no longer needs medicine** *(T-PRM-008)*

*Target: "The patient no longer needs medicine."*

```
Gloss:    lo-zo-li  ta-ti-now  no-ne-fe  ma-no-de
Literal:  patient:person  at-present-time  non-dependency-condition  preserving-substance
Natural:  The person currently does not need medicine.
```

- `zo-li` = living social agent = patient / person
- `ta-ti-now` = temporal particle + present time = currently / at this time (distinguishes present state from prior need)
- `no-ne-fe` = negation-prefix + dependency-condition = non-dependency = does not need. The `no-` prefix operates on `ne-fe` as a unit; `no-ne-fe` = the absence of the dependency-condition.
- `ma-no-de` = substance + no-decay = a preserving/maintaining substance = medicine/treatment. Head-final: `de` (decay) is the head; `no-de` = non-decay; `ma-no-de` = matter characterized by preventing decay.

**"No longer"** (implying prior need that has ended) requires the temporal frame `ta-ti-now` to contrast with implied prior state. The bare `no-ne-fe` merely asserts current non-dependency without implying change. To assert explicitly that the patient *previously* needed medicine: `ta-ti-de  ne-fe  ta-ti-now  no-ne-fe  ma-no-de` (past dependency + present non-dependency) — which is grammatically valid but verbose; context usually supplies the implication.

**Verdict S063: clean.** `no-ne-fe` (negated dependency) is grammatical and compositional. `ma-no-de` (medicine) is a useful new compound. The "no longer" temporal nuance is handled by the time-particle system rather than a dedicated word, consistent with Principle 4 (optional rather than mandatory marking).

---

### `ne-fe` Batch Summary

| Sentence | Subject type | Object type | Verdict |
|----------|-------------|-------------|---------|
| S058 | person (patient) | raw substance | clean — state predication confirmed |
| S059 | child | biological rest state | clean — `zo-no-ki` emerges |
| S060 | machine/artifact | physical process | clean — `ha-de` parallel to `ha-be` |
| S061 | collective institution | raw substance | clean — scales to complex subject |
| S062 | collective agent | abstract structure | clean — `wi-to` (plan) emerges |
| S063 | person | medicine | clean — `no-ne-fe` and `ma-no-de` both compositional |

**`ne-fe` is genuinely general.** It held across six sentences spanning biological, mechanical, institutional, and abstract domains. Three new compounds emerged from the test: `zo-no-ki` (sleep/rest), `wi-to` (plan/intentional pattern), `ma-no-de` (medicine/preserving substance). These should be evaluated for W-registration.

---

## Comparative Test Batch (S064–S067)

**Purpose:** First systematic test of `nu-be` (more-than). S039 confirmed `nu-no` (less-than) in one thermal comparison. This batch confirms `nu-be`, tests generalization across quality types (thermal, spatial, biological, signal), and probes whether the comparison baseline can be a temporal reference rather than an entity.

---

**S064 — Room warmer than the corridor** *(T-CMP-001)*

*Target: "The room is warmer than the corridor."*

```
Gloss:    lo-ko-pa  ha-vo  nu-be  lo-ki-pa
Literal:  patient:contained-place  thermal-quality  more-than  patient:motion-place
Natural:  The room has more thermal quality than the corridor.
```

- `ko-pa` = containment-place = room / enclosed space. Head-final: `pa` (place) is head; `ko` (containment) specifies it is a bounded, enclosed space. First corpus use.
- `ki-pa` = motion-place = corridor / hallway. Head-final: `pa` (place) is head; `ki` (motion) specifies it is a place defined by passage through it. The two compounds form a natural pair: rooms are bounded (`ko`), corridors are transitive (`ki`).
- `ha-vo` = thermal-quality = warmth (S033). `nu-be` follows in the comparative slot.
- `nu-be` = quantity-growth = more / to a greater degree. Head-final: `nu` (quantity) is head; `be` (growth) gives the comparison direction. **First corpus attestation of `nu-be`.**

**Verdict S064: clean.** `nu-be` works as the more-than comparative, symmetric with `nu-no`. The `ko-pa`/`ki-pa` room/corridor compound pair is useful for everyday speech.

---

**S065 — Machine larger than the other one** *(T-CMP-002)*

*Target: "This machine is larger than the other one."*

```
Gloss:    lo-mu  pa-nu  nu-be  lo-mu-ne
Literal:  patient:artifact  space-quantity  more-than  patient:reference-artifact
Natural:  The machine has greater spatial magnitude than the related artifact.
```

- `pa-nu` = space-quantity = spatial magnitude / size / volume. Head-final: `nu` (quantity) is head; `pa` (space/place) specifies the dimension. First use. Analogous to `ha-vo` (thermal-quality) — both use a quantity/quality head with a domain modifier.
- `mu-ne` = artifact-in-relation = the other / comparable artifact. `ne` (relation/connection) marks the second machine as the relational reference entity. Compositionally transparent; no dedicated demonstrative pronoun needed.
- Second attestation of `nu-be`. Different quality type from S064 (spatial magnitude rather than thermal quality), confirming `nu-be` generalizes across quality domains.

**Verdict S065: clean.** `nu-be` generalizes. `pa-nu` (size) and `mu-ne` (reference artifact) are both productive.

---

**S066 — Child less tired than yesterday** *(T-CMP-003)*

*Target: "The child is less tired than yesterday."*

```
Gloss:    lo-li-be  ta-ti-now  zo-de  nu-no  ta-ti-de
Literal:  patient:child  at-present-time  organism-decay  less-than  past-time-interval
Natural:  The child has less fatigue now than at the past time.
```

- `li-be` = person in growth phase = child (W033).
- `zo-de` = organism-decay = fatigue / physical tiredness. Head-final: `de` (decay) is head; `zo` (living organism) specifies biological decay — the wearing-down of a living body. Contrast `ra-de` (energy/power decay = power failure) and `ha-de` (thermal decrease = cooling, W044). `zo-de` is the specifically biological decay of exertion. First use.
- `ta-ti-de` = past time interval = yesterday / a prior period (first used S035; W041 candidate).
- **Structural extension:** the comparison baseline is a **temporal reference** (`ta-ti-de`), not a second entity (`lo-B`). The `[baseline]` slot in the comparative construction accepts either `lo-[entity]` (between two things) or `ta-ti-[time]` (one thing against its own earlier/later state). Both positions are syntactically parallel; neither requires a new grammatical device.

**Verdict S066: clean.** `zo-de` (fatigue) is a useful compound. Temporal comparison (`ta-ti-X` as baseline) is grammatically valid and unambiguous. The self-comparison pattern is logged for the grammar formalization.

---

**S067 — Signal stronger than the threshold** *(T-CMP-004)*

*Target: "The signal is stronger than the threshold."*

```
Gloss:    lo-si  ra-vo  nu-be  lo-si-fe
Literal:  patient:signal  energy-quality  more-than  patient:signal-boundary
Natural:  The signal has greater energy intensity than the signal threshold.
```

- `ra-vo` = energy-quality = signal intensity / force magnitude. Head-final: `vo` (quality) is head; `ra` (energy) specifies the domain. Analogous to `ha-vo` (thermal-quality). The `[domain]-vo` quality pattern is now confirmed across both thermal (`ha-vo`) and energetic (`ra-vo`) domains.
- `si-fe` = signal-boundary = the signal threshold / the point at which a signal becomes actionable or alarm-triggering. Head-final: `fe` (boundary) is head; `si` (signal) specifies the domain. Consistent with prior `fe`-boundary compounds: `ha-fe` (thermal threshold, S034), `to-fe` (epistemic threshold).
- Third attestation of `nu-be`. Abstract/technical domain (signal engineering) confirms the comparative works beyond physical, tactile qualities.

**Verdict S067: clean.** `nu-be` with abstract quality dimensions is clean. The `[domain]-vo` pattern generalizes to signal intensity (`ra-vo`).

---

### Comparative Batch Summary

| Sentence | Direction | Quality | Baseline type | Verdict |
|----------|-----------|---------|---------------|---------|
| S039 | `nu-no` | `ha-vo` (thermal) | entity | clean — first comparative |
| S064 | `nu-be` | `ha-vo` (thermal) | entity | clean — first `nu-be` |
| S065 | `nu-be` | `pa-nu` (size) | entity | clean — generalizes quality type |
| S066 | `nu-no` | `zo-de` (fatigue) | temporal | clean — temporal baseline valid |
| S067 | `nu-be` | `ra-vo` (intensity) | entity | clean — abstract quality |

**Comparative system confirmed.** `nu-no`/`nu-be` are productive across quality types and baseline types. No new grammatical mechanism needed. Rule written into spec/grammar.md § Comparison.

Secondary compounds emerging from this batch: `ko-pa` (room), `ki-pa` (corridor), `pa-nu` (size), `zo-de` (fatigue), `ra-vo` (signal intensity), `si-fe` (signal threshold).

---

## Containment Predicate Test Batch (S068–S071)

**Purpose:** Settle the `ko` (passive containment state) vs `ka-ko` (intentional storing action) distinction. S037 established `la-X  ko  lo-Y` as a valid state predicate (the metal holds thermal energy). The open question: is `ko` in the predicate slot always passive, or can it be agentive? Four sentences: two passive, two intentional, varying subject type and presence of a destination argument.

---

**S068 — Vessel contains water** *(T-KO-001)*

*Target: "The vessel contains water."*

```
Gloss:    la-ko-mu  ko  lo-ma-di
Literal:  agent:containment-artifact  containment-state  patient:liquid-matter
Natural:  The vessel holds water.
```

- `ko-mu` = containment-artifact = vessel / tank / container. Head-final: `mu` (artifact) is head; `ko` (containment) specifies its defining function. First use.
- `ko` in predicate slot = passive containment state. Pattern `la-[container]  ko  lo-[contents]` (established S037).
- `ma-di` = directed-matter = water / liquid (S039).
- No action operator. The vessel is *in the state of* containing — not performing an act of placing.

**Verdict S068: clean.** `ko` as passive state predicate holds for a purpose-built container. The `la-[container]  ko  lo-[contents]` pattern is consistent with S037.

---

**S069 — She stored the document** *(T-KO-002)*

*Target: "She stored the document."*

```
Gloss:    la-ze  lo-si-mu  ka-ko
Literal:  agent:she  patient:encoded-artifact  action:intentional-containment
Natural:  She stored / deliberately placed the document into containment.
```

- `ze` = she (3rd person pronoun).
- `si-mu` = encoded-artifact = a document / individual record. Head-final: `mu` (artifact) is head; `si` (encoded/signal) specifies content type. Distinct from `si-su` (encoded-structure = archive / collection, S056); `si-mu` is a single stored item.
- `ka-ko` = action-containment = intentional storing. Head-final: `ko` (containment) is head; `ka` (deliberate action) specifies intentionality. Contrast with S068: no agent is required for passive containment state; `ka-ko` always requires an agent.

**Verdict S069: clean.** `ka-ko` is unambiguously agentive. Contrast with S068 is sharp: `lo-si-mu  ko` would describe a state (the document is held somewhere); `la-ze  lo-si-mu  ka-ko` describes an action (she performed the storing).

---

**S070 — The archive holds records** *(T-KO-003)*

*Target: "The archive holds records."*

```
Gloss:    la-si-su  ko  lo-si-mu
Literal:  agent:encoded-structure  containment-state  patient:encoded-artifact
Natural:  The archive holds documents / records.
```

- `si-su` = encoded-structure = archive / collection (S056).
- `si-mu` = encoded-artifact = individual document (S069).
- `ko` = passive containment — same pattern as S037, S068. Confirms that `ko` state-predication scales to **institutional and abstract** containing relationships. An archive does not perform the act of holding; it is the structural entity in which records reside.

**Verdict S070: clean.** `ko` predication at institutional scale is grammatically identical to `ko` predication for physical vessels. The `la`-slot requires only the containing entity, not an intentional agent.

---

**S071 — He placed the tool into the container** *(T-KO-004)*

*Target: "He put the tool inside the container."*

```
Gloss:    la-ze  lo-ka-mu  ne-ko-mu  ka-ko
Literal:  agent:he  patient:tool  toward:container  action:intentional-containment
Natural:  He placed the tool into the container.
```

- `ka-mu` = action-artifact = tool.
- `ko-mu` = containment-artifact = the container (S068).
- `ne-ko-mu` = recipient/toward marker + container = the destination. `ne` (relation/recipient particle) marks `ko-mu` as the target of the transfer. This extends `ne` from its established use marking recipients of gift-transfers (S056: `ne-li-pu-su`) to marking physical destinations of placement actions. Both uses are semantically coherent: `ne` = relation-toward.
- `ka-ko` + `ne-[destination]` = full intentional-storage form: agent + item + destination + action.

**Verdict S071: clean.** The `ne` particle extends cleanly to spatial destinations. Full form `la-[agent]  lo-[item]  ne-[container]  ka-ko` = "agent stores item into container" is confirmed.

---

### Containment Predicate Batch Summary

| Sentence | Form used | Agent | Pattern | Verdict |
|----------|-----------|-------|---------|---------|
| S068 | `ko` | vessel (non-intentional) | passive state | clean |
| S069 | `ka-ko` | person (intentional) | agentive storing | clean |
| S070 | `ko` | institutional archive | passive state at scale | clean |
| S071 | `ka-ko` | person + destination | agentive + explicit target | clean |

**`ko` / `ka-ko` distinction confirmed.** `ko` in the predicate slot is always a passive relational state; `ka-ko` always asserts intentional placement. The distinction is load-bearing: institutional archives, material containers, and physical vessels are grammatically identical under `ko`-predication — the intentionality of the containing entity is irrelevant to the form. Intentional placing requires `ka-ko` with an explicit agent. Rule written into spec/grammar.md § Containment Predicates.

---

## Mystic Domain Probe (S072–S078)

**Purpose:** Test Monday's hypothesis that "magic" in a Concordia-style setting (space mecha + loose mystic system) does not require a new primitive — that `ra`, `wi`, `to`, `fe`, `ne`, and `se` already cover the conceptual ground. Seven sentences drawn from the domain. Verdict criterion: does the sentence come out clean, serviceable, or distorted? "Maintenance manual haunted by a ghost" = distorted.

---

**S072 — The pilot sensed the field** *(T-MYS-001)*

*Target: "The pilot sensed the field."*

```
Gloss:    la-ra-ki-li  se  lo-pa-ra
Literal:  agent:pilot  perceive  patient:space-energy
Natural:  The pilot detected the spatial energy field.
```

- `ra-ki-li` = energy-motion-person = pilot (established compound).
- `pa-ra` = space-energy = a field: the spatial distribution of an energetic quantity. Head-final: `ra` (energy) is head; `pa` (space) specifies the domain of distribution. The field is energy organized across space, not a point source. First use. Natural companion to `ha-ra` (thermal energy, S037).
- `se` = raw detection / sensing. No interpretation implied — the pilot registers the field, not yet processes what it means.

**Verdict S072: clean and useful.** `pa-ra` (field) is a productive compound; `ra-ki-li` in agent position with `se` predicate is a standard perception sentence. No strain.

---

**S073 — The ritual strengthened the ward** *(T-MYS-002)*

*Target: "The ritual strengthened the protection."*

```
Gloss:    la-wi-ka-su  lo-fe-su  be-past
Literal:  agent:ritual  patient:boundary-structure  grew
Natural:  The ritual strengthened the ward.
```

- `wi-ka-su` = will-action-structure = a formally structured system of intentional acts = ritual / formal procedure. Head-final: `su` (structure/organization) is head; `wi-ka` (intentional action) specifies the type. Three morphemes, but compositionally transparent: a ritual is specifically an *organized system* of intentional acts, distinguished from `wi-to` (plan, a purposive design object) and `wi-ka` (bare intentional action). First use.
- `fe-su` = boundary-structure = ward / protective barrier. Head-final: `su` (structure) is head; `fe` (boundary) specifies function. Distinct from `ha-fe` (thermal threshold, S034) — `fe-su` is a constructed boundary, not a threshold of a physical quantity.
- `be` = growth/increase. In predicate position with a structural object as patient: the boundary structure grew = was strengthened / expanded.
- Non-sentient agent in `la` slot: `la-wi-ka-su` (the ritual as actor) parallels `la-se-ka` (the process as actor) from C004. Grammatically established.

**Verdict S073: clean.** Two useful compounds: `wi-ka-su` (ritual) and `fe-su` (ward/barrier). The mystical action composes entirely from force-pattern-will primitives.

---

**S074 — She entered the trance state** *(T-MYS-003)*

*Target: "She entered the trance state."*

```
Gloss:    la-ze  zo-se-ki
Literal:  agent:she  [living-perception]-enter
Natural:  She entered the state of heightened bodily perception.
```

- `zo-se-ki` = inchoative of `zo-se`. Head-final: `ki` (motion/entering) as inchoative marker; base compound `zo-se` = organism-perception = the raw perceptual state of a living body. `zo-se-ki` = enter the organism-perception state = go into the state where bodily perception dominates. Same inchoative compounding pattern as `ne-ki` (connect), `zo-ki` (come to life), `ko-ki` (enter containment).
- "Trance" in the Concordian frame is not mystical in origin — it is a perceptual mode transition: the pilot/practitioner shifts from cognitive-processing dominance (`to`-mode) to raw sensory presence (`se`-mode) in the body (`zo`). This is a recognizable concept in the mecha context: pilots who "sink into" machine resonance by releasing cognitive overlay.

**Verdict S074: clean.** `zo-se-ki` (entering trance/heightened perception state) is compositionally valid and produces precisely the right Concordian framing: not "entering a mystical realm" but "entering the organism-perception mode." Which is exactly how this culture would describe it — as a sensory-cognitive state, not a spiritual journey.

---

**S075 — The machine responds to her will** *(T-MYS-004)*

*Target: "The machine responds to her will."*

```
Gloss:    la-wi-ze  ka  lo-mu
Literal:  agent:her-will  acts-upon  patient:machine
Natural:  Her will acts upon the machine.
```

- `wi-ze` = her-will / her-intention = will (`wi`) possessed by her (`ze`). `wi` in the agent slot as the acting entity. Non-sentient/non-physical agents in the `la` slot are established (C004: `la-se-ka` process-as-agent). Will occupying the agent slot is structurally valid.
- This sentence is structurally identical to an ordinary one where "her command" acts on the machine — the `la` slot takes agents of any type. The *mystical* reading (her will, unmediated, acts on the machine without physical command) vs the *mundane* reading (her intention causes her to command the machine) are **not distinguished by the sentence alone**.

**Strain analysis:** `la-wi-ze  ka  lo-mu` is not distorted — it is ambiguous. In an engineering register it describes command; in a mystic register it describes direct will-resonance. Tonesu does not currently distinguish these. The candidate disambiguation:
- Mundane: `la-ze  ro-wi  ka  lo-mu` = "she (by means of will/command) acts on the machine" — will as instrument
- Mystic: `la-wi-ze  ka  lo-mu` — will as direct agent, person absent from agent slot
- The contrast is: person-uses-will (`ro-wi`) vs will-acts-directly (`la-wi-ze`). If this distinction is needed regularly, it is the pressure point, not the whole sentence.

**Verdict S075: serviceable, with one ambiguity seam.** Structurally clean; semantically underdetermined between mundane-command and mystic-resonance. The seam is at whether `wi` occupies the instrument slot (`ro-wi`) or the agent slot (`la-wi-ze`). Log as a watch item.

---

**S076 — The relic emits a strange signal** *(T-MYS-005)*

*Target: "The relic emits a strange signal."*

```
Gloss:    la-ti-mu  si-ki  no-to-ge
Literal:  agent:ancient-artifact  signals-outward  patternless-quality
Natural:  The relic emits an anomalous signal.
```

- `ti-mu` = time-artifact = relic / ancient object. Head-final: `mu` (artifact) is head; `ti` (time) specifies temporal depth — an artifact characterized by significant time. First use. Transparent: "a thing from time."
- `si-ki` = signal-motion = signal going outward / transmission. Established direction: `si` (signal) + `ki` (motion) = signal in motion = emit/transmit. Uses the same motion-as-emission pattern as `ra-ki-mu` (engine: energy + motion + artifact).
- `no-to-ge` = negation + concept + quality-suffix = the quality of being patternless / unclassified / anomalous. `no-to` = pattern-absence; `-ge` = quality of. The signal has no recognized conceptual framework. Distinct from `no-to-su` (absence of organized knowledge) — `no-to-ge` is a predication about the signal's qualitative character.

**Verdict S076: clean and evocative.** `ti-mu` (relic) is immediately useful. `no-to-ge` correctly produces the Concordian framing of "strange": not "weird" in an emotional sense, but "outside the current pattern-recognition schema." A properly creepy ancient artifact in Concordian terms is one that emits signals that no existing `to` framework can classify.

---

**S077 — They crossed the forbidden boundary** *(T-MYS-006)*

*Target: "They crossed the forbidden boundary."*

```
Gloss:    la-yu  fe-ki  lo-fe-no-ka
Literal:  agent:they  boundary-cross  patient:prohibition-boundary
Natural:  They crossed the boundary that action forbids.
```

- `fe-ki` = boundary-motion = boundary crossing. Inchoative frame: `fe` (boundary) + `ki` (motion) = entering-boundary-state = to cross a threshold / transgress. Consistent with the established inchoative pattern.
- `fe-no-ka` = boundary + no-action = the boundary defined by its prohibition. Head-final: `fe` (boundary) is head; `no-ka` (negation-action = prohibition / the no-action state) modifies it. "The border that must not be crossed" formulated as: the boundary whose crossing is prohibited = `fe-no-ka`. Note: built from `no-` (productive negation prefix, now formalized) + `ka` (action) + `fe` head. Clean composition.
- The sentence makes no claim about why the boundary is forbidden — whether by institutional decree, mystic danger, physical necessity, or cultural taboo. The prohibition is encoded in the structure of the referent (`fe-no-ka`), not in any new modal root.

**Verdict S077: clean.** `fe-no-ka` (forbidden boundary / prohibition threshold) is a natural compound. The Concordian framing of "taboo" as a *boundary with a no-action property* is exactly right — prohibition is a structural condition, not a feeling.

---

**S078 — The navigator received a vision** *(T-MYS-007)*

*Target: "The navigator saw a vision."*

```
Gloss:    la-di-ki-li  se  lo-se-to
Literal:  agent:navigator  perceive  patient:perception-concept
Natural:  The navigator received a perceptual insight / vision.
```

- `di-ki-li` = direction-motion-person = navigator: one whose work is directed motion through space. Head-final: `li` (person) is head; `di-ki` (directed motion) specifies the domain. First use. Note: `di` (direction/orientation) + `ki` (motion) = directed movement = navigation as an activity type.
- `se-to` = perception-concept = the conceptual pattern that arises from direct perception. Head-final: `to` (conceptual pattern) is head; `se` (perception) specifies that the concept originates from raw sensory input rather than reasoning (`go`) or signal decoding (`si`). A `se-to` is what you grasp directly by sensing, not by inference. In the mystic context: a vision is literally a perceptual-concept — a conceptual image arriving through the perceptual channel. First use.
- The slight recursion (`se` verb + `se`-inside-`se-to` object) is semantically distinct: the outer `se` is the act of receiving; the `se` inside `se-to` names the epistemic *origin* of the concept. The navigator perceives (`se`) a concept-from-perception (`se-to`).

**Verdict S078: clean but carries tension.** `se-to` (perceptual insight) is semantically precise and useful. The tension: "vision" in a mystic sense implies content from outside the perceiver's ordinary sensory experience — the navigator sees something *beyond* what the eyes physically collect. `se-to` doesn't distinguish ordinary insight from prophetic reception. A mystic vision that seems to originate from an external unseen domain might need `se-ne-to` (perception-relation-concept = a concept received through perceptual connection to something external) or a domain qualifier. Logged as a watch item.

---

### Mystic Domain Batch Summary

| Sentence | Target concept | Form | Verdict |
|----------|---------------|------|---------|
| S072 | field | `pa-ra` | clean — immediate use |
| S073 | ritual / ward | `wi-ka-su`, `fe-su` | clean — ritual as organized-will-structure |
| S074 | trance | `zo-se-ki` | clean — perceptual mode transition |
| S075 | will as cause | `la-wi-ze  ka` | serviceable — ambiguous instrument vs agent |
| S076 | relic / anomalous signal | `ti-mu`, `no-to-ge` | clean — "strange" = patternless quality |
| S077 | forbidden boundary | `fe-no-ka` | clean — prohibition as a boundary property |
| S078 | vision / insight | `se-to` | clean — 1 watch item (mystic vs ordinary insight) |

**Verdict: Monday's hypothesis confirmed.** 6/7 sentences compose cleanly from existing roots with no strain. S075 has one ambiguity seam (`wi` as instrument vs direct agent); S078 has one unresolved nuance (prophetic vs ordinary perceptual insight). Neither requires a new primitive. Both are compound-level issues.

**Emergent compounds from this batch:** `pa-ra` (field), `wi-ka-su` (ritual), `fe-su` (ward/barrier), `zo-se-ki` (trance), `ti-mu` (relic), `fe-no-ka` (forbidden boundary), `di-ki-li` (navigator), `se-to` (perceptual insight/vision). Candidates for W-registration.

**The mystic-primitive question is not closed, just deferred properly.** If corpus sentences keep appearing where the `wi`-as-instrument vs `wi`-as-direct-agent ambiguity (S075) matters — i.e., where Concordian speakers would systematically need to distinguish trained-will-resonance from physical-command — and no compound patch resolves it, that is when a dedicated domain root becomes justified. The threshold: more than three attested sentences where the ambiguity produces genuinely wrong or misleading readings.

---

## Religious Construct Probe (S079–S085)

**Purpose:** Test Monday's extension of the composability hypothesis to religious constructs. Different target than the mystic batch: mystic = mechanism (how things work); religion = interpretation and structure (what it means, who enforces it). Seven sentences covering the core religious vocabulary candidates. Criterion: maintenance manual? Or something better?

---

**S079 — She sent a prayer** *(T-REL-001)*

*Target: "She prayed." / "She sent a prayer."*

```
Gloss:    la-ze  ka-wi-si
Literal:  agent:she  action:will-signal
Natural:  She performed intentional-signaling / she prayed.
```

- `wi-si` = will-signal = a signal constituted by and originating from intention. Head-final: `si` (signal) is head; `wi` (will/intention) specifies origin. Not `ka-si` (transmit, directed point-to-point, W024) — the distinction is that `wi-si` is signal whose content *is* the will itself, rather than a signal carrying information. A prayer is the will-signal; a command is an action-signal.
- `ka-wi-si` = action of performing will-signaling = to pray (as an act). The `ka` marks this as a deliberate activity.
- Recipient optionally marked: `la-ze  ne-[recipient]  ka-wi-si` = she prayed *to* [recipient]. Without `ne`, the recipient is contextual or unspecified — both common uses of prayer.

**Verdict S079: clean.** `wi-si` distinguishes prayer from command (`ka-si`) and from ordinary signal-emission. The Concordian framing — prayer as will-signal, not petition-to-supernatural-authority — is consistent with an analytic epistemic culture.

---

**S080 — The scripture holds the doctrine** *(T-REL-002)*

*Target: "The scripture contains the founding doctrine."*

```
Gloss:    la-si-su  ko  lo-to-re-su
Literal:  agent:encoded-structure  contains  patient:recurring-organized-doctrine
Natural:  The archive holds the canonical doctrine.
```

- `si-su` = encoded-structure = archive / organized recording system (S056, S070). Here used for the scripture as a physical institutional archive.
- `to-re-su` = concept-recurring-structure = organized knowledge that is repeatedly transmitted and maintained. Head-final: `su` (structure/organization) is head; `to-re` (recurring doctrine — a conceptual pattern characterized by `re`, periodicity/preservation) modifies it. A `to-re-su` is not any organized knowledge (`to-su`), but specifically the kind that has been canonized and is reproduced over time: scripture, canon, tradition.
- `ko` = passive containment. `la-si-su  ko  lo-to-re-su` follows the S070 pattern: the archive holds the records.

**Verdict S080: clean.** `to-re-su` (canonical doctrine / scripture as content) is a useful and precise compound — distinct from `to-su` (organized knowledge generally) by the inclusion of `re` (recurring, transmitted over time).

---

**S081 — The relic is sacred** *(T-REL-003)*

*Target: "The relic is holy / set apart."*

```
Gloss:    lo-ti-mu  fe-vo
Literal:  patient:ancient-artifact  boundary-value
Natural:  The relic has the quality of set-apart value.
```

- `ti-mu` = time-artifact = relic (S076).
- `fe-vo` = boundary-value = the quality of carrying value that is defined by a boundary — i.e., value that is protected by a prohibition against casual crossing. Head-final: `vo` (quality/value) is head; `fe` (boundary) specifies that the value is of the boundary-protected kind. Sacred = the quality of having value that prohibits approach or casual use. Contrast `fe-no-ka` (S077, forbidden boundary): that is a boundary classified by its prohibition; `fe-vo` is a value classified by its boundary character.
- The Concordian framing: a relic is sacred not because of divine decree but because it is an entity possessing recognized value that carries a boundary (approaches, uses, states of contact are restricted). This is structurally precise and culturally exactly right for an analytic culture.

**Verdict S081: clean.** `fe-vo` (sacredness / boundary-protected value) correctly frames holiness in structural rather than supernatural terms. Pairs naturally with `fe-no-ka` (S077) and `vo-fe` (value at the boundary = another possible reading: the point at which something attains recognizable value — slightly different). `fe-vo` and `vo-fe` are related but not identical compounds; both are useful.

---

**S082 — The doctrine keeper addressed the gathering** *(T-REL-004)*

*Target: "The priest/scholar addressed the assembly."*

```
Gloss:    la-to-su-li  si-ki  ne-li-pu
Literal:  agent:knowledge-organizer  signal-outward  toward:collective
Natural:  The doctrine keeper transmitted signal to the collective.
```

- `to-su-li` = concept-structure-person = "one who organizes and maintains structured knowledge" (already in registry, W003 related). In the Concordian setting, this is the most natural form for a priest: not a supernatural intermediary, but a person whose social role is management of canonical doctrine. The same compound covers librarian, archivist, and religious authority — because in Concordian culture they are structurally the same role.
- `si-ki` = signal-motion = transmit / direct outward (S076 Verdict: transmit).
- `ne-li-pu` = relation:collective = toward the gathered group.

**Verdict S082: clean.** The Concordian frame makes an importantly non-religious claim: the person who "performs religion" is not a specially endowed spiritual figure but a `to-su-li` — a knowledge organizer. A priest is distinguishable from a librarian only by what body of `to-re-su` they maintain. This is a structural consequence of the primitive set, not an import from outside — and it is the most culturally specific result of the batch.

---

**S083 — The pilot attunes to the machine** *(T-REL-005)*

*Target: "The pilot attunes to / synchronizes with the machine."*

*This is the key test. `ne-ra-ki` candidate for "attune": entering the state of energetic connection.*

```
Gloss:    la-ra-ki-li  ne-ra-ki  lo-mu
Literal:  agent:pilot  enter-energy-relation  patient:machine
Natural:  The pilot enters into energetic resonance with the machine.
```

- `ne-ra` = relation-energy = a relational connection in the energetic domain = resonance / attunement. Head-final: `ra` (energy) is head; `ne` (relation) specifies the character of the energy — not a point-source (`pa-ra`, S072) but a relational binding between two systems. `ne-ra` is the state where two energy systems are coupled.
- `ne-ra-ki` = inchoative of `ne-ra` = entering the state of energetic coupling = attune / synchronize. Inchoative pattern: appending `ki` (motion → state-entering) to a state compound (established from `ne-ki`, `zo-ki`, `ko-ki`, `zo-se-ki`).
- `lo-mu` = the machine as the patient of the attunement — the entity being coupled with.

**Structural comparison with S075:** S075 (`la-wi-ze  ka  lo-mu`) uses *will* as agent acting *on* the machine. S083 uses the pilot as agent entering *into relation with* the machine. These are subtly different: S075 encodes a directive relationship (will → machine); S083 encodes a relational state transition (pilot ↔ machine, mutual coupling). In a mecha context where the resonance is bidirectional, S083 is the more accurate form.

**Verdict S083: clean and structurally important.** `ne-ra` (resonance / energetic coupling) and `ne-ra-ki` (to attune) are productive and precise. The compound resolves S075's ambiguity for the specifically relational case: S075 = will acts on machine (directive); S083 = pilot enters energetic coupling with machine (relational/bidirectional). `ne-ra` is the candidate compound for the Concordian mecha resonance concept. Watch whether it eventually needs to be more than a compound.

---

**S084 — The doctrine holds that the machine has a spirit** *(T-REL-006)*

*Target: "They believe the machine has a soul."*

*Concordian framing: this is an epistemic claim within a doctrine, not an ontological assertion.*

```
Gloss:    la-li-pu  to-re-su  si  lo-mu  zo-to
Literal:  agent:collective  recurring-doctrine  signals  patient:machine  living-pattern
Natural:  The group's canonical doctrine signals that the machine has a living-pattern.
```

- `to-re-su` in the instrument slot: the organized doctrine is the means by which the signal is transmitted. This uses `to-re-su` as a citation frame — the group's scripture/tradition is doing the asserting.
- `zo-to` = living-pattern = the conceptual organization of a living entity = soul / spirit as a functional description. Head-final: `to` (conceptual pattern) is head; `zo` (living) specifies that the pattern is of the living-thing type. `zo-to` makes no commitment about whether the pattern is embodied, supernatural, or emergent — it merely asserts that the machine has a *pattern characteristic of living things*. This is the maximally neutral Concordian framing of "soul."
- `si` = signal (as predicate here, in the "the doctrine emits the claim that..." frame). Parallels `la-se-ka  be  [proposition]` (C004) but with `si` rather than `be` — the signal is the mode of assertion.

**The two candidates for "spirit/soul":**
- `zo-si` = living-signal = a spirit as a non-physical entity whose existence consists of emitting signal (an entity that is a living signal without a body)
- `zo-to` = living-pattern = a soul as the organized conceptual pattern constituting the identity of a living entity

These are not identical. `zo-si` is appropriate when "spirit" means an agent without a physical substrate — a ghost, a disembodied entity. `zo-to` is appropriate when "soul" means the identity-pattern of a being — the organizing principle of a living entity. Two valid uses, two compounds. Neither yet requires a primitive.

**Verdict S084: serviceable.** The sentence works and produces the correct Concordian framing: soul/spirit is a doctrine-level claim, not an uncontested ontological fact. `zo-to` and `zo-si` are both useful but need to be kept distinct. Logged as a watch item.

---

**S085 — The spirits protect the shrine** *(T-REL-007)*

*Target: "The spirits protect the shrine / holy place."*

```
Gloss:    la-zo-si  lo-pa-wi-ka-su  no-de
Literal:  agent:living-signal  patient:ritual-place  preserve
Natural:  The spirits preserve the ritual place.
```

- `zo-si` = living-signal = spirit / disembodied living agent. Here used as the actual agent — the spirits are the grammatical subject performing the preservation, not quoted inside a doctrine claim. This tests whether `zo-si` functions cleanly as a non-physical agent without strain.
- `pa-wi-ka-su` = place-ritual = a place defined by its ritual function = shrine / temple. Head-final: `wi-ka-su` (ritual, S073) is head; `pa` (place) is modifier — a place that is a ritual. Wait, head-final means the last element is the head: `pa-wi-ka-su` has `su` as head (structure), `wi-ka` (intentional action) as second modifier, `pa` as first modifier. Reading: an organized structure for intentional action within a place = a formal ritual institution of the place. That works.
- Alternative: `pa-wi-ka` = place-intentional-action = "the place of intentional practice" = shrine without the `su`. Slightly less formal. For the sentence, `pa-wi-ka-su` is used for a recognized institutional holy site.
- `no-de` = preserve (from S030: no-de = prevent-decay).
- The agent `la-zo-si` in agent slot: grammatically, Tonesu does not restrict the agent slot to physically embodied agents. `la-wi-ka-su` (S073: the ritual as agent) and `la-se-ka` (C004: the examination as agent) established non-physical, non-intentional entities in the agent slot. A spirit (`zo-si`) is a non-physical but *intentional* agent — in some ways a cleaner occupant of the `la` slot than a ritual or an examination.

**Verdict S085: clean.** `zo-si` works as an agent without strain. `pa-wi-ka-su` (shrine) is productive. The sentence is not a maintenance manual. It reads, in Concordian: "a living-signal entity preserves the ritual-structure." That is precisely how an analytic culture would record a religious claim — accurate to the doctrine's content, neutral about its ontological truth.

---

### Religious Construct Batch Summary

| Sentence | Target concept | Form | Verdict |
|----------|---------------|------|---------|
| S079 | prayer | `ka-wi-si` | clean — will-signal as act |
| S080 | scripture / doctrine | `to-re-su` | clean — recurring organized doctrine |
| S081 | sacred / holy | `fe-vo` | clean — boundary-protected value |
| S082 | priest / doctrine keeper | `to-su-li` | clean — same as librarian/archivist (Concordian structural finding) |
| S083 | attunement / resonance | `ne-ra-ki` | clean — **key compound; resolves S075 directive vs relational** |
| S084 | spirit / soul (as claim) | `zo-to` | serviceable — works as epistemic frame; `zo-si` vs `zo-to` distinction needed |
| S085 | spirits as agents | `zo-si` | clean — non-physical agent holds in grammar |

**Verdict: composability holds for religion.** 6/7 clean; S084 is serviceable with a watch item (`zo-si` vs `zo-to` disambiguation). No religious primitive required.

**Most important structural finding: S082.** In Concordian grammar, "priest" comes out as `to-su-li` — the same compound as librarian and archivist. This is not a failure to express religion; it is the language making a structural claim about Concordian culture: religious authority and knowledge authority are the same institution. A culture whose primitives treat doctrine as organized recurring knowledge (`to-re-su`) and religious roles as knowledge management roles (`to-su-li`) is making a specific statement about what religion *is* in their ontology.

**Resonance finding: S083.** `ne-ra` (energy-relation = resonance/coupling) solves the S075 ambiguity for the bidirectional mecha-resonance case. `wi` as agent = directed will acting on a machine; `ne-ra-ki` = entering a mutual coupling with a machine. The distinction is precise and now attested. This is the strongest compound candidate from the entire mystic+religion sequence.

**Emergent compounds from this batch:** `wi-si` (prayer/will-signal), `to-re-su` (canonical doctrine/scripture), `fe-vo` (sacredness), `pa-wi-ka-su` (shrine/temple), `ne-ra` (resonance/energetic coupling), `ne-ra-ki` (to attune), `zo-to` (soul/identity-pattern of living entity), `zo-si` (spirit/disembodied living agent). Candidates for W-registration.

---

## Theological Debate Batch (C005)

---

**C005 — Theological dispute: doctrine epistemic status**

*Scene: A `ra-ki-li` (pilot) and a `to-su-li` (doctrine-keeper/archivist) dispute whether
the community's guardian machine has `zo-to` (soul/identity-pattern). The pilot recently
experienced `ne-ra-ki` (attunement) with the machine (S083-type event). The community's
`to-re-su` makes the doctrinal claim. The dispute will escalate from personal assertion
through doctrinal citation, to `to-fe-ka` charge, to institutional routing.*

*Tests: `to-re-su` citation as epistemic grounding; `ze` pronoun as propositional
back-reference; `la-[doctrine]  ko  [embedded-clause]` — doctrine as containment agent;
`no-to-fe` as status predicate on a knowledge structure; first explicit `to-fe-ka`
accusation in corpus; `no-to` as negated epistemic modal; first corpus use of `to-fe-su`
(unlocking registration); structural treatment of "heresy."*

---

**Turn A1**

```
Gloss:    la-mi  si  [lo-mu  zo-to]
Literal:  agent:I  signal-level  [patient:machine  soul/identity-pattern]
Natural:  I hold as hypothesis: the machine has a soul.
```

**Notes:**
- Fourth use of `la-[speaker]  [epistemic-root]  [embedded-proposition]` (C001 A3, C004 B1,
  C004 A2 process-variant). Pattern is now established, not merely attested.
- A opens at `si` (signal / hypothesis) rather than bare assertion (implicit `to`). The
  correct Concordian behavior for a contested doctrinal claim. A is not committing
  `to-fe-ka` by overclaiming; A is maintaining epistemic transparency.
- `zo-to` (W068: soul/identity-pattern) in its first directly adversarial context.
  S084 used `zo-to` wrapped in a third-party doctrinal citation (`la-li-pu  to-re-su  si`);
  here A is asserting A's own position.

---

**Turn B1**

```
Gloss:    la-mi  to  [lo-ze  se]
Literal:  agent:I  established  [patient:it  raw-perception]
Natural:  I hold as established: what you have (that experience) is raw perception.
```

**Notes:**
- **First use of `ze` pronoun as propositional back-reference.** `ze` (3rd person pronoun)
  is established for personal reference (`la-ze`, `lo-ze` = he/she). Here `lo-ze` refers
  back not to a person but to A1's claim and the `se-to` (W062) that grounded it. If `ze`
  refers to the most recent contextually salient discourse entity — and a proposition counts
  as a discourse entity — this extension is legal. First corpus test of propositional `ze`.
  WATCH: does `lo-ze` always resolve to a convenient referent, or does it produce genuine
  ambiguity in complex discourse? Log for future stress-testing.
- B is not denying A had an experience; B is diagnosing the *epistemic level* of that
  experience as `se` (raw perception/vision), not `si` or `to`. The pilot's `se-to` from
  attunement-type experience (S083) constitutes perception, B argues — not yet an encoded
  hypothesis.
- Asymmetric confidence: A hedged `si`; B counters with `to` (confidence). Concordian
  adversarial structure in action: the challenger asserts more certainty about the
  epistemic classification than the claimant asserts about the claim itself.

---

**Turn A2**

```
Gloss:    la-to-re-su  ko  [lo-mu  zo-to]
Literal:  agent:canonical-doctrine  contains  [patient:machine  soul-pattern]
Natural:  The canonical doctrine holds: the machine has a soul.
```

**Notes:**
- **Doctrine as containment agent.** `la-to-re-su  ko` extends the containment predicate
  (spec/grammar.md § Containment Predicates) from physical vessels and institutional
  archives to knowledge structures. In S070: `la-si-su  ko  lo-si-mu` (the archive holds
  records). Here: the canonical doctrine holds a propositional claim. Same `la-X  ko  Y`
  structure; Y is now an embedded clause `[lo-mu  zo-to]` instead of a nominal patient.
- **First use of `ko` with a clausal object.** In S068–S071 `ko` took nominal patients
  (liquid, document, tool). `[lo-mu  zo-to]` is a propositional clause: "the machine has
  soul-pattern." The square brackets mark embedded content. Whether `ko` can
  systematically take clausal complements, or whether this requires a formal extension,
  is a pending grammar question. Tentatively: yes, by analogy — "the doctrine contains
  that the machine has zo-to" has the same containment logic as "the archive contains the
  record."
- A shifts from personal assertion (`la-mi  si`) to institutional citation
  (`la-to-re-su  ko`). The pilot is no longer claiming personal knowledge; A is citing the
  institutional epistemic record. This is the standard Concordian escalation move when
  pressed: from "I believe" to "the record holds."

---

**Turn B2**

```
Gloss:    la-mi  to  [lo-to-re-su  no-to-fe  ta-ti-now]
Literal:  agent:I  established  [patient:canonical-doctrine  not-epistemic-boundary  time:present]
Natural:  I hold as established: the canonical doctrine has not crossed the epistemic
          threshold — not to this day.
```

**Notes:**
- **`no-to-fe` as status predicate.** `no-` (negation prefix, W001-domain, fully
  formalized in spec/morphology.md) + `to-fe` (epistemic boundary, W028) = "has not
  crossed the epistemic boundary / has not been certified through the `to-fe` process."
  This follows the established `no-[root]` pattern (`no-de`, `no-ru`, `no-fe`); `no-to-fe`
  is its application to the epistemic certification boundary.
- B is not challenging the *content* of the doctrine. B is challenging the *epistemic
  procedural status* of the doctrine itself. The move: the `to-re-su` calls itself
  canonical (i.e., claims `to-su` level) but was never adjudicated by a `to-fe-li` panel,
  and therefore never legitimately crossed the `to-fe` threshold into warranted `to-su`
  status.
- `ta-ti-now` — present-time anchor makes this an ongoing status claim, not a historical
  observation. The doctrine has not been certified as of right now.
- This is the Concordian structural equivalent of: "Your scripture isn't actually
  canonical; it was never validated by the proper epistemic body." The attack is procedural,
  not theological. The language makes no distinction between these.

---

**Turn A3**

```
Gloss:    la-mi  to  [lo-ze  to-fe-ka]
Literal:  agent:I  established  [patient:that-claim  deliberate-epistemic-boundary-violation]
Natural:  I hold as established: what you just said is deliberate epistemic fraud.
```

**Notes:**
- **First explicit `to-fe-ka` accusation in corpus.** `to-fe-ka` (W029: deliberate
  epistemic boundary violation) was defined and registered but never directly leveled as
  a charge in a sentence until now. A3 is a full formal accusation.
- `lo-ze` — propositional back-reference again; this time A is using `ze` to refer to B2's
  claim. The pilot accuses B of *deflation `to-fe-ka`*: B is knowingly suppressing the
  doctrine's `to-su` status by falsely asserting `no-to-fe`. The inflation/deflation
  directionality: B is deflating (claiming a `to-su`-status doctrine is below `to-fe`),
  which is the harder-to-prove and politically more subtle form of `to-fe-ka`.
- A's escalation pattern: A1 = `si`-hedge; A2 = institutional citation at `to-su` level;
  A3 = `to`-level accusation of fraud. Three distinct epistemic escalation steps in three
  turns, each raising the stakes.
- The asymmetry of levels: A is charging B with `to-fe-ka` at full `to`-confidence. To
  level a fraud charge requires exactly this: you must assert `to`-level knowledge that
  the boundary was deliberately violated. A `si`-level fraud charge is incoherent.

---

**Turn B3**

```
Gloss:    la-mi  no-to  [lo-ze  to-fe-ka]  —  la-tu  ka-si  lo-to-fe-su
Literal:  agent:I  not-established  [patient:that  epistemic-fraud]  —  [you]  action:signal
          patient:epistemic-standards-framework
Natural:  I hold as not-established: that is not fraud. — Submit this to the standards body.
```

**Notes:**
- **`la-mi  no-to  [prop]` — new construction.** `la-mi  to  [prop]` = "I hold as
  established." `no-to` by the `no-` prefix rule = "I hold as not-established" or "I do
  not assert [prop] as established." This is the negation of an epistemic stance, not a
  negation of the proposition's content. Productive extension of the epistemic modal
  pattern: the modal itself can be negated. B is not saying "it is established that this
  is NOT fraud"; B is saying "I do not hold the fraud charge as established." A weaker,
  more defensible position — B refuses to certify A's accusation as `to`-level.
- **First corpus use of `to-fe-su`.** `la-tu  ka-si  lo-to-fe-su` — the institutional
  routing pattern from C004 A3 (`la-tu  ka-si  lo-li-su-li`) now applied to the epistemic
  standards framework rather than an operational coordinator. The distinction is load-bearing:
  an engineering dispute routes to `li-su-li` (coordinator); a doctrinal epistemic status
  dispute routes to `to-fe-su` (epistemic standards body). The level of institution matches
  the level of dispute. `to-fe-su` is now in corpus: register as W072.
- B does not concede the fraud charge and does not counter-escalate with a personal
  accusation. B routes to the process. The canonical Concordian response: when two parties
  are at irreconcilable `to-fe` positions, the dispute exits the personal layer and enters
  the institutional layer. Neither party wins by assertion; the body adjudicates.
- **Structural result:** "Heresy" has no dedicated Concordian word. A doctrinal challenge
  is structurally a `to-fe` dispute — epistemically identical to a scientific or engineering
  knowledge dispute. The machinery is the same: `to-fe-ka`/`to-fe-ki` charges, `to-fe-li`
  arbiters, `to-fe-su` adjudication. Religion in Concordia is a subset of the knowledge
  domain, and all knowledge disputes use the same institutional tools.

---

**C005 Gaps and pressures:**

| Gap | Location | Status |
|-----|----------|--------|
| **`ze` as propositional back-reference (P-PR-001)** | B1, A3 | New use: `lo-ze` refers to a prior *proposition*, not a person. Productive if valid; dangerous if it creates resolution ambiguity in complex discourse. Two uses in one conversation. Needs a formal rule: does `ze` refer to the most recent contextually salient discourse entity regardless of type (person/proposition), or are propositional references a distinct pronoun class? |
| **`ko` with clausal object** | A2 | `la-to-re-su  ko  [lo-mu  zo-to]` — first `ko` with a clausal rather than nominal patient. Tentatively clean by analogy. Formal rule needed: can containment predicates take clausal complements systematically, or is this special-cased for knowledge structures? |
| **`no-to` as negated epistemic modal** | B3 | `la-mi  no-to  [prop]` = "I do not hold as established that [prop]." New form: `no-` applied to an epistemic modal stance rather than a root in predicate position. Different from `no-[state-root]` (negating a state); this negates a propositional attitude. Worth noting whether `la-mi  no-si  [prop]`, `la-mi  no-se  [prop]` etc. follow by the same logic. Likely yes — confirms `no-` can scope over any epistemic level marker. |
| **`to-fe-su` registration** | B3 | First corpus use. Register as W072 before next session. Design note: does `to-fe-su` as institution require a separate `to-fe-su-ki` (inchoative = moment a ruling enters published to-su status) vs bare `to-fe-su` (the body / unpublished ruleset)? The publication-state gap from open-questions.md becomes urgent once in corpus. |
| **`to-fe-ka` charge directionality** | A3 | A3's charge is deflation `to-fe-ka` (suppressing an established doctrine's status). No explicit marker for direction (inflation vs deflation) appears in the sentence — the sentence alone is: "that is `to-fe-ka`." A `to-fe-li` adjudicating this charge would need to determine direction from context. See open-questions.md on epistemic deflation as a distinct charge. |

---

### Theological Debate Batch Summary

| Turn | Move | Form | Verdict |
|------|------|------|---------|
| A1 | Doctrinal claim (hedged) | `la-mi  si  [zo-to]` | clean — correct Concordian hedge |
| B1 | Epistemic level challenge | `la-mi  to  [lo-ze  se]` | clean — propositional `ze` works |
| A2 | Doctrinal citation | `la-to-re-su  ko  [lo-mu  zo-to]` | clean — doctrine-as-container extension |
| B2 | Challenge doctrine's own status | `no-to-fe` predicate | clean — `no-` applies to epistemic boundary |
| A3 | `to-fe-ka` accusation | `la-mi  to  [lo-ze  to-fe-ka]` | clean — first formal charge in corpus |
| B3 | Reject charge; route to institution | `la-mi  no-to  […]  —  ka-si  lo-to-fe-su` | **first `to-fe-su` use; unlocks registration** |

**Central structural finding: there is no dedicated Concordian word for heresy.**
A theological dispute is epistemically indistinguishable from a scientific or engineering
dispute. The mechanisms are identical: `to-fe-ka` or `to-fe-ki` charges, `to-fe-li`
arbiters, `to-fe-su` adjudication. Religion in Tonesu is a subset of organized knowledge
(`to-re-su` domain), and all organized knowledge disputes use the same institutional tools.
The language makes a structural claim: there is no special ontological category for
theological disagreement.

**Most important new construction: `no-to` as negated epistemic modal.**
`la-mi  no-to  [prop]` = "I do not hold as established that [prop]." The negation of an
epistemic stance rather than a proposition. By `no-` prefix logic, `no-si` and `no-se`
follow. The full contrast set is now available: `la-mi  se/si/to/to-su/no-to/no-si/no-se
[prop]` = I perceive / I hypothesize / I know / I hold as canonical / I do not hold as
known / I do not hold as hypothesis / I do not perceive. This is a dense and expressive
system.

**Emergent compound requiring immediate registration:** `to-fe-su` (epistemic standards
framework). First attested B3. Register as W072.

---

## `wi-to` Semantic Range Stress Test (S086–S092)

*Target: determine whether `wi-to` is overloaded across four candidate senses — plan,
design, program (institutionalized sequence), and intention-model (internal goal state) —
and narrow or bifurcate the entry accordingly.*

*Probe design: each sentence targets one sense. If `wi-to` gives the right reading in all
four, the compound is load-bearing but legitimate. If any sentence forces a structural
wrong reading, `wi-to` has bled.*

---

**S086 — Engineer revised the plan** *(T-WIT-001 / baseline)*

*Target: baseline `wi-to` use in context. Establish clean reference before stress cases.*

```
Gloss:    la-to-li  lo-wi-to  be-past
Literal:  agent:knower/engineer  patient:plan  grew/changed-past
Natural:  The engineer revised the plan.
```

**Notes:**
- `be-past` = grew/changed/improved. A plan being revised is the plan growing into a better
  version of itself. `be` here carries the productive/generative sense (the plan was
  developed), not strictly growth in size. Attested pattern: `la-X  lo-Y  be` = X improved Y.
- This is the intended baseline reading: `wi-to` = a concrete plan artifact that exists
  externally (it can be revised, held, destroyed) and has a specific purposive structure.
- Baseline datum: `wi-to` = **plan as external artifact** = what you write down and can
  change. The head `to` is the pattern/concept; `wi` marks it as purposive.
- `to-li` pressed into service for "engineer" — a knowledge-worker in the technical sense.
  The `to-li` is the person whose work is pattern-making, which generalizes to design
  engineer. Compare `to-su-li` (knowledge-structure person = librarian/archivist/priest)
  and `ra-ki-li` (energy-motion person = pilot/driver).

**Verdict S086: clean.** Baseline holds. `wi-to` = plan-as-concrete-revisable-artifact.

---

**S087 — The engineer designed the machine** *(T-WIT-002 / design)*

*Target: "design" — purposive structure specifying *form* rather than sequence. Does `wi-to`
cover this, or does it need a different head?*

```
Gloss:    la-to-li  lo-mu  wi-to  be-past
Literal:  agent:engineer  patient:machine  plan/design  grew/made-past
Natural:  The engineer designed the machine.
```

**Alternative — `wi-to-su` as formal design document:**

```
Gloss:    la-to-li  lo-wi-to-su  ka-past
Literal:  agent:engineer  patient:design-specification  action-past
Natural:  The engineer produced the design specification.
```

**Notes:**
- **First candidate stress.** "Designed the machine" — the purposive conceptual work that
  preceded building it. The question: does `lo-mu  wi-to  be-past` mean "the engineer
  planned/designed the machine" (wi-to as predicate modifier or loose purposive qualifier),
  or is `wi-to` playing a different role here than it did in S086?
- In S086, `wi-to` was a *patient* (what was revised). In S087 first form, `wi-to` is
  closer to being a predicate modifier or manner qualifier on `be` — "improved [the machine]
  [with will-pattern]." This is a different grammatical slot and a different reading. That
  shift is the signal.
- **The distinction:** "plan" as a standalone artifact (S086, S062) vs "design" as a
  purposive activity or form-specification of another object. When `wi-to` is the *patient*
  of a verb, it reads as a plan-artifact. When it appears adjacent to another patient with
  `be`, it reads as purposive-manner — and this is grammatically strained.
- **Alternative is cleaner:** `wi-to-su` = purposive-concept-structure = a design
  specification document. The `su` head marks it as an organized external artifact
  containing formal specifications, not just a purposive idea. The engineer didn't just
  have a willed-concept; the engineer made a structured specification.
- **Tentative result:** `wi-to` (bare) = plan in the sense of a purposive mental-or-paper
  object. `wi-to-su` = structured design specification — the formalized version. For
  "designed the machine" as an activity rather than a document, a `ka-wi-to` (action of
  will-patterning) construction would be needed (not yet attested).

**Verdict S087: `wi-to` strained in predicate-modifier position.** Clean in patient slot.
The compound does not naturally mean "to design [the machine]" as an activity; it means
"the plan" as an artifact. `wi-to-su` is the right compound for formal design specification.
New compound candidate: **`wi-to-su`** (design specification).

---

**S088 — The maintenance program runs every cycle** *(T-WIT-003 / program)*

*Target: "program" = a sequenced structure that recurs, possibly performed by different
agents on different instances. Does `wi-to` cover this?*

```
Attempt A (wi-to):
Gloss:    lo-wi-to  ta-re-ti  be
Literal:  patient:plan/program  time:recurring-cycle  runs/executes
Natural:  The program executes each cycle.

Attempt B (wi-re-su):
Gloss:    lo-wi-re-su  ta-re-ti  be
Literal:  patient:will-recurring-structure  time:recurring-cycle  runs/executes
Natural:  The recurring protocol executes each cycle.
```

**Notes:**
- **`wi-to` (Attempt A) — analysis:** `ta-re-ti` (recurring time) suggests the thing
  recurs. If this is a `wi-to` (purposive concept), what recurs is the concept itself
  being enacted — but a concept doesn't "run" or "execute"; an agent enacts it. `be` with
  `lo-wi-to` as subject = "the plan grows/runs"? This is semantically odd: a plan isn't
  the kind of thing that runs; it's the kind of thing that is *followed* or *enacted*.
  `wi-to` lacks the autonomy to be the subject of `be` without an agent.
- **`wi-re-su` (Attempt B) — analysis:** `wi` (will) + `re` (recurrence) + `su`
  (structure) = organized recurring willed structure = a protocol / program that repeats
  by design. The `su` head makes it an external structure rather than a mental concept.
  The `re` in the middle marks it as a *recurring* structure. On this reading: the
  recurring-willed-structure executes each cycle. Cleaner — `be` takes it as its natural
  subject because a structure can run (instantiate), whereas a concept cannot.
- **`re` placement:** modifier order puts `wi-re` (will-recurrence) before `su` —
  "an institutionalized, recurring, willed structure." Compare `wi-ka-su` (W054, ritual):
  `wi` + `ka` (deliberate action) + `su`. The difference between `wi-ka-su` (ritual) and
  `wi-re-su` (program/protocol): a ritual is defined by its use of deliberate action;
  a program is defined by its recurrence. Orthogonal heads on a shared `wi` modifier.
- **Result:** `wi-to` cannot serve as program. A program has institutional recurrence
  (`re`) and external structure (`su`); a plan has a specific outcome (`to`). These are
  different heads. New compound: **`wi-re-su`** (operational protocol / recurring
  procedural program).

**Verdict S088: `wi-to` cannot cover "program."** `wi-re-su` is the correct compound for
a recurring institutionalized procedure. The `su` head distinguishes it from `wi-to`
(which has a `to` head, marking the purposive conceptual content, not the structure).

---

**S089 — Her intention guided the work** *(T-WIT-004 / intention-model)*

*Target: "intention" = an internal goal representation, not a concrete artifact. Does this
need `wi-to`, bare `wi`, or something else?*

```
Attempt A (wi-to):
Gloss:    la-wi-to-ze  lo-ka  ki
Literal:  agent:plan-of-her  patient:action  motion/directed
Natural:  Her plan directed the action.

Attempt B (bare wi):
Gloss:    la-wi-ze  lo-ka  ki
Literal:  agent:will/intention-of-her  patient:action  directed
Natural:  Her will/intention directed the action.
```

**Notes:**
- `wi-to-ze` = will-pattern-[possessive ze] = her plan. S075 established `wi-ze` = her
  will as agent in `la` slot. The question is whether `wi-to` (plan) adds anything over
  bare `wi` (will) in this context.
- **Bare `wi` (Attempt B)** reads: "her will guided the action." This is clean — `wi`
  alone is the primitive for will/intention, and Tonesu is established as preferring
  primitives when compounds don't add precision.
- **`wi-to-ze` (Attempt A)** reads: "her plan — as an existing external artifact —
  guided the action." This adds the sense that the intention has been externalized or
  committed to as a specific pattern. If there's a plan document, `wi-to` is correct;
  if the guidance is coming from her internal motivational state, bare `wi` is better.
- **The distinction is real and load-bearing.** Intention = internal motivational state
  (`wi`). Plan = purposive concept externalized as an artifact (`wi-to`). This is not
  a distinction the language collapses — `wi` and `wi-to` are already separate entries,
  and this test confirms the line between them.
- **Conclusion:** "Intention" as an internal goal representation = bare `wi`. No compound
  needed. `wi-to` is not for internal motivational states; it is for externalized purposive
  artifacts. The compound does not bleed into the primitive's territory.

**Verdict S089: `wi-to` does NOT cover bare intention.** `wi` alone = internal
motivational state. `wi-to` = externalized, concrete plan-artifact. The distinction holds.
`wi-to` does not need to narrow on this axis; the compound and its base primitive already
divide the domain correctly.

---

**S090 — The pilot followed a different doctrine from the mission plan** *(T-WIT-005 / stress)*

*Target: sentence that forces both "doctrine/standing instruction" and "mission plan" to appear
in the same context — the decisive disambiguation test.*

```
Gloss:    la-ra-ki-li  lo-to-re-su  be  no  lo-wi-to
Literal:  agent:pilot  patient:canonical-doctrine  grew/followed  negation  patient:plan
Natural:  The pilot followed the standing doctrine, not the mission plan.
```

**Notes:**
- **Decisive result.** In a single sentence, `to-re-su` (canonical recurring doctrine)
  and `wi-to` (specific mission plan) are contrastive. Their separation is immediately
  legible: the pilot operated under the background standing instructions
  (`to-re-su` = recurring canon) rather than the specific purposive plan for this
  mission (`wi-to`).
- This is the sentence the watch item was waiting for: `wi-to` and `to-re-su` *contrast
  cleanly*. Neither bleeds into the other. `wi-to` = this specific plan for this specific
  outcome; `to-re-su` = the established recurring doctrine that persists across missions.
  Time-scope is the differentiator: `wi-to` is particular/single-use; `to-re-su` is
  recurring/institutional.
- `be  no  lo-wi-to` = "grew/followed [negation] the plan" = "followed [X], not the plan."
  The `no` as a coordinator meaning "not [the alternative]" uses the established negation
  pattern. First use of `no` as a contrast coordinator between two patients in the same
  clause (rather than as a prefix). Tentatively clean; worth logging as a new `no` use.
- **Design vs plan:** This sentence also confirms that `to-re-su` covers "standing design/
  doctrine" in the sense of "established working instructions." `wi-to` narrows further:
  it is not just "not doctrine" but specifically "mission-specific, single-use purposive
  structure."

**Verdict S090: clean and decisive.** `wi-to` and `to-re-su` are distinct and
contrastive in a single sentence without strain. `wi-to` narrows to: **particular,
single-instance, externalized purposive structure**. Standing doctrine covering multiple
instances = `to-re-su`. Recurring procedure = `wi-re-su` (S088).

---

**S091 — The coordinator briefed the team on the plan** *(T-WIT-006 / transmission)*

*Target: can `wi-to` be the object of a signal/briefing action? Tests whether a plan can
be transmitted like information.*

```
Gloss:    la-li-su-li  lo-yu  lo-wi-to  ka-si-past
Literal:  agent:coordinator  patient:group  [relation:]plan  action:transmitted-past
Natural:  The coordinator briefed the team on the plan.
```

**Notes:**
- `ka-si` (W024, transmit/signal) used with a double-patient construction: `lo-yu`
  (the group = the recipient) and `lo-wi-to` (the plan = the content transmitted). First
  double-patient with `ka-si`. The structure is: agent transmits [content] to [recipient].
  In prior uses, `ka-si` took one patient (the recipient, or occasionally the content).
  The double-patient form may need a formal grammar rule — or `ne-yu` (relation:group)
  for the recipient and `lo-wi-to` for the content alone.
- **`wi-to` as transmissible information object.** The test: can a plan be transmitted
  the way a signal can? Yes — a plan is an externalized artifact (`to` head = conceptual
  pattern, not merely a mental state), so it can be the content of a `ka-si` transmission
  the way `si-mu` (a document) can. This confirms the "externalized artifact" character
  of `wi-to`: it is a thing that can be held, transmitted, revised, and stored.
- Distinction from `wi` (bare will): bare will cannot be transmitted via `ka-si`.
  `la-li-su-li  lo-yu  lo-wi-ze  ka-si-past` = "the coordinator transmitted her will to
  the group" — possible but reads as a command/order rather than a briefing. The
  `wi-to` form is what makes it a briefing: content is shared, not imposed.

**Verdict S091: clean.** `wi-to` works as a transmissible information object. A plan
can be briefed the way a document can be archived. This confirms the artifact/external
character of `wi-to`: it is a plan *as a thing that exists* in the world, not merely
as an internal cognitive state.

---

**S092 — The team updated its design specification before the mission** *(T-WIT-007 / wi-to-su)*

*Target: first corpus use of `wi-to-su` (design specification) proposed in S087.*

```
Gloss:    la-yu  lo-wi-to-su  be-past  ta-ti-de  lo-ka-wi-de
Literal:  agent:group  patient:design-specification  grew/updated-past
          time:before  patient:mission-departure
Natural:  The team updated the design specification before the mission.
```

**Notes:**
- **First corpus use of `wi-to-su`.** `wi` (will) + `to` (concept/pattern) + `su`
  (structure) = purposive-concept-structure = design specification. The three-level
  compound follows the established productive pattern: `wi-to` (purposive concept) →
  `wi-to-su` (that purposive concept organized into a formal structure).
- Compare `wi-to` (plan, two morphemes, the mental/paper artifact) vs `wi-to-su`
  (design specification, three morphemes, the formally organized version). The `su` head
  signals: this is not just a plan someone has; it is a structure that has been organized
  into a form that can be reviewed, published, and revised by the team collectively.
  Same distinction as `to` (knowledge/pattern) vs `to-su` (organized body of knowledge):
  the `su` upgrade marks systemization.
- `ta-ti-de  lo-ka-wi-de` = "before the departure." `ti-de` = time-decay = past/prior
  time. `ka-wi-de` = action-will-departure = mission-departure (intended departure action).
  This is a temporal prepositional phrase using `ta` (time marker) + `ti-de` (before/
  prior) + `lo-ka-wi-de` (the departure). The structure functions as a before-clause.
  New form: `ta-ti-de  lo-[event]` = "before [event]." Watch: does `ta-ti-de` generalize
  as a "before" construction or is it specific to this context?

**Verdict S092: clean.** `wi-to-su` (design specification) is a productive and
unambiguous extension of `wi-to`. The compound composes cleanly. Register as W073.

---

### `wi-to` Stress Test Summary

| Sentence | Target sense | Form tested | Verdict |
|----------|-------------|-------------|---------|
| S086 | plan (baseline) | `wi-to` | clean — canonical use |
| S087 | design (form specification) | `wi-to` strained; `wi-to-su` proposed | **bifurcate** |
| S088 | program (recurring procedure) | `wi-to` wrong; `wi-re-su` proposed | **separate compound** |
| S089 | intention (internal state) | `wi-to` vs bare `wi` | **primitive wins** — `wi` alone correct |
| S090 | plan vs doctrine (disambiguation) | `wi-to` vs `to-re-su` contrast | clean — no bleed |
| S091 | transmissible plan object | `wi-to` as content of `ka-si` | clean — artifact character confirmed |
| S092 | design specification (document) | `wi-to-su` first use | **new compound; register W073** |

**Central finding: `wi-to` does NOT need to narrow — it already has the right range.**
The watch item flagged four potential bleed directions; none materialized:
1. **Design (form):** `wi-to` stretched in predicate position but is clean as a patient.
   `wi-to-su` is the right form for a *formal* design specification. `wi-to` stays as
   "plan/purposive design concept."
2. **Program (recurrence):** `wi-re-su` is a clean new compound. `wi-to` ≠ program.
3. **Intention (internal):** bare `wi` wins. `wi-to` does not bleed into the primitive.
4. **Standing doctrine:** `to-re-su` covers it. No bleed.

**`wi-to` is confirmed as: particular / single-instance / externalized purposive artifact.**
Not internal state (`wi`). Not recurring procedure (`wi-re-su`). Not formal specification
(`wi-to-su`). Not standing doctrine (`to-re-su`). The four-way contrast is now corpus-
grounded.

**New compounds from this batch:**
- `wi-to-su` — design specification: purposive-concept-structure (first use S092). Register W073.
- `wi-re-su` — operational protocol / recurring procedural program (first use S088). Register W074.
- `ka-wi-de` — mission departure (used in S092, transparent compound — register when second context appears).
- `ta-ti-de  lo-[event]` — before-[event] temporal construction (first use S092). Grammar pattern rather than compound.

---

## Question Battery (C006)

---

**C006 — Pre-jump briefing: polar question, content question, and the ambiguous case**

*Scene: Navigator A (`di-ki-li`) and Pilot B (`ra-ki-li`) in a pre-jump sequence. The
field (`pa-ra`) ahead may carry resonance conditions. Six turns covering all four
question-and-answer pressures from the open-question log.*

*Tests: P-QM-001 (polar vs content question using `to-si`); P-AF-001 (minimal affirmative:
first corpus test of `ru`); the ambiguous `to-si` case; negation of a proposition
(`la-mi  no-se`); direct disagreement without epistemic modal; response-form as question-
type disambiguator.*

---

**Turn A1**

```
Gloss:    to-si — lo-pa-ra  be-now
Literal:  knowledge-inquiry — patient:field  is-active-now
Natural:  Is the field active?
```

**Notes:**
- Third polar question in corpus (B2.C004 was a polar; C003 A1 was first explicit
  polar). Structure: `to-si` fronted (OUTSIDE the proposition), dash as inquiry-frame
  boundary, then the complete well-formed proposition `lo-pa-ra  be-now`.
- The proposition `lo-pa-ra  be-now` is structurally complete: a patient exists, a state
  predicate follows. `to-si` does not fill any argument slot inside it; it sits outside
  the proposition, querying the truth value. This is the defining structural feature of
  the polar question type.
- Contrast with C001 B1: `de  vo  to-si?` — there, `to-si?` fills the *qualifier slot*
  inside the proposition (what quality of decay?). The unknown argument is inside; `to-si`
  is inside. Here: unknown is outside (truth value); `to-si` is outside.
- The positional distinction is now explicit: **content questions** have `to-si` filling
  an argument slot inside the proposition; **polar questions** have `to-si` fronted
  outside the complete proposition.

---

**Turn B1**

```
Gloss:    ru — lo-pa-ra  be-now  ra-vo  nu-be  lo-si-fe
Literal:  [affirm] — patient:field  active-now  energy-quality  exceeds  threshold
Natural:  Yes — the field is active and above threshold.
```

**Notes:**
- **First corpus use of `ru` (W039: unity/coherence) as a minimal affirmative.** `ru` =
  coherence/unity — standing alone as the first element, it functions as "[that coheres]" /
  "yes." This is semantically transparent: `ru` is not a new function word; it is the
  primitive whose meaning ("it holds together," "it is coherent") works as an affirmation
  of the prior question's proposition. `lo-pa-ra  be-now` = the field is active = that
  is coherent with what you asked = `ru`.
- The dash separates the affirmative from the extended answer. B does not stop at `ru`;
  B adds the relevant qualifier (`ra-vo  nu-be  lo-si-fe` = intensity above threshold,
  reusing the S067/B2 pattern). This is the natural Concordian pattern: confirm +
  specify. The minimal affirmative is not used alone when more is known.
- **`ru` as functional "yes":** `ru` satisfies a polar question (the question was binary;
  `ru` picks the affirmative branch). Compare with echo-confirmation (C003 B1: full
  proposition restatement) and action-confirmation (C001 B3: `ka-to-su-ki`). Three
  strategies now attested: (1) `ru` = minimal affirm; (2) echo = restatement from speaker's
  perspective; (3) action-commit = `ka-[verb]` = I will/am doing it. All three are licensed;
  `ru` is the shortest.

---

**Turn A2**

```
Gloss:    lo-pa-ra  ne-ra  vo  to-si?
Literal:  patient:field  resonance  quality  [what]?
Natural:  What is the character of the field's resonance?
```

**Notes:**
- **Content question.** `to-si?` at the END of the proposition, in the qualifier slot.
  The proposition has a gap: `lo-pa-ra  ne-ra  vo  ___?` — the unknown is the qualitative
  character/kind of the resonance. `to-si` fills that slot the way an unknown argument
  would. Compare C001 B1: `de  vo  to-si?` (`to-si` in the quality slot of damage type).
  Same structure: `[entity]  [relation]  [dimension]  to-si?`
- `ne-ra` (W058, resonance/energetic coupling) as a predicate on `lo-pa-ra`: the field
  *has* a resonance character. Second/third attestation of `ne-ra`, which matters for
  status upgrade beyond proposed.
- The positional signature is now visible across two corpus cases:
  - Content question: `to-si` **at the end / in argument position** — `de  vo  to-si?`
    (C001 B1), `lo-pa-ra  ne-ra  vo  to-si?` (C006 A2)
  - Polar question: `to-si` **fronted before a complete proposition** — `to-si — [prop]`
    (C003 A1, C006 A1)

---

**Turn B2**

```
Gloss:    lo-ne-ra  no-to-fe  —  lo-pa-ra  no-ne-fe  lo-mu
Literal:  patient:the-resonance  uncertified/unestablished — patient:field
          not-dependency-condition  patient:machine
Natural:  The resonance character is uncertified. The field has no link to the machine.
```

**Notes:**
- **`lo-ne-ra` as nominal patient.** `ne-ra` (resonance, W058) in patient slot with `lo`
  particle = the resonance [of the field, contextually recoverable]. First use of `ne-ra`
  as a standalone nominal. Distinct from `ne-ra-ki` (the inchoative process) — here the
  resonance itself is the subject of a status predication.
- **`no-to-fe`** reused from C005 B2. Here: the resonance character is `no-to-fe`
  (uncertified / has not crossed the epistemic boundary into established status). The
  pilot does not know the quality of this field's resonance — it is at `si` level at best.
- **Second sentence:** `lo-pa-ra  no-ne-fe  lo-mu` = the field is not in a dependency
  condition toward / linked to the machine. `ne-fe` (W042, dependency/requirement) in
  negative: `no-ne-fe` = no established relational dependency between field and machine.
  The machine is not yet attuned to this field. This is B warning A: the field's resonance
  properties are unknown and the machine has not established a link.
- **New `no-ne-fe` compound.** `no-` (negation) + `ne-fe` (dependency condition, W042)
  = no active dependency / no established link. Third `no-`+ compound compound (prior:
  `no-to-fe` C005 B2, `no-to` C005 B3). The pattern continues to be productive.

---

**Turn A3**

```
Gloss:    to-si — la-mi  ne-ra-ki
Literal:  knowledge-inquiry — agent:I  attune
Natural:  [Am I attuning? / What am I attuning to?]
```

**Notes:**
- **THE AMBIGUOUS CASE.** `to-si` fronted before what appears to be a polar proposition
  (`la-mi  ne-ra-ki` = I [am] attuning). But `ne-ra-ki` is an inchoative process that
  normally takes a `lo`-patient (the thing being attuned to). The patient is absent. Two
  valid readings:
  - **Polar reading:** the patient is dropped by discourse context (the field was just
    discussed); the question is: "Am I attuning [to the field / to it]?" — unknown is
    truth-value of the complete proposition with recovered patient.
  - **Content reading:** the patient is unknown (not omitted); the question is: "What am
    I attuning to?" — unknown is the argument, and `to-si` fronts a proposition with an
    unknown patient slot. But on the content reading, `to-si` should be in argument
    position (`la-mi  ne-ra-ki  to-si?`) rather than fronted.
- **The positional rule resolves it: fronted `to-si` = polar.** The content reading would
  require `to-si?` in the patient slot: `la-mi  ne-ra-ki  to-si?` ("what am I attuning
  to?"). A3 as written — `to-si` fronted — is therefore unambiguously polar by position:
  the question is whether A is attuning (or beginning to), not what A is attuning to.
  The dropped patient is recovered by discourse context (the field, established in A1).
- **Key result:** the ambiguous case is resolved by the positional rule, not by context
  alone. This is strong evidence that the fronted vs in-argument distinction is
  grammatically load-bearing and sufficient — no additional polar particle is needed.

---

**Turn B3**

```
Gloss:    no — lo-pa-ra  no-ne-fe  ta-ti-now
Literal:  [negate] — patient:field  no-dependency-state  time:present
Natural:  No — the field has no link right now.
```

**Notes:**
- **First corpus use of bare `no` as minimal negative response.** Parallel to `ru` (B1)
  as minimal affirmative. `no` answers the polar question from A3 in the negative branch.
  Semantically transparent: `no` = absence/negation = the situation does NOT cohere with
  the proposition in A3. B has not yet entered attuned state; the field has no established
  coupling with the pilot's systems.
- `no` + dash + elaboration: same structural pattern as `ru` (B1). The minimal
  response + the informative follow-up. The pair is now established: `ru — [elaboration]`
  = yes + detail; `no — [elaboration]` = no + detail.
- `ta-ti-now` = present-time anchor (from C005 B2 pattern). The dependency state is
  assessed as absent at this moment, not in general.
- `no-ne-fe` reused from B2: the field has no active link to the machine. Consistent
  with the technical situation: the pilot cannot attune to a field that has no established
  coupling with the ship's systems.

---

**Turn A4**

```
Gloss:    la-mi  si  [ta-ti-be  ne-ra-ki  be]
Literal:  agent:I  signal-level  [time:approaching  attune  grows]
Natural:  I assess: the link will develop soon.
```

**Notes:**
- `la-mi  si  [prop]` — fifth use of the utterance-level epistemic modal pattern.
  Fully established.
- `ta-ti-be  ne-ra-ki  be` = "at the upcoming time, attuning grows." `ta-ti-be` (W040,
  future time reference) used as temporal frame for an anticipated process. `ne-ra-ki`
  (W059, to attune / enter resonance) + `be` (grow/develop) = the attuning process is
  developing. First use of `ne-ra-ki` with `be` as a growth/continuation predicate rather
  than as a completed inchoative.
- A asserts confidence that the link will form, but marks it only at `si` level (a
  judgment about a future state, not an established fact). Correct Concordian hedging
  for a future prediction.

---

**Turn B4**

```
Gloss:    ru — ta-ti-re  ki
Literal:  [affirm] — time:cycle-coming  approach
Natural:  Yes — it's coming up in the cycle.
```

**Notes:**
- `ru` second use in the same conversation — second corpus attestation. Confirms it is
  stable as a minimal affirmative, not a one-off. The pattern is now: `ru` is a
  sentence-initial affirmative particle licensed as a standalone clause followed by `—`
  and an elaboration.
- `ta-ti-re` = time-cycle = the next cycle / the recurrent time. `ti` (time) + `re`
  (recurrence). First use of `ti-re` as a time nominal: "the upcoming time in the cycle."
  Related to S092's `ta-ti-de` (before = time-decay) — this is the future-cycle
  complement: `ti-re` = the recurring upcoming moment. Distinct from `ti-be` (W040,
  next/upcoming time in general): `ti-be` is the next temporal interval; `ti-re` is
  specifically the next occurrence in a recurring sequence. The distinction matters for
  scheduled events.
- `ki` alone = approach / comes. Bare predicate with dropped agent (the thing coming is
  the link / the resonance readiness — contextually recoverable). Consistent with the
  argument-drop by context pattern established in C001 A2b.

---

**C006 Gaps and pressures:**

| Gap | Location | Status |
|-----|----------|--------|
| **P-QM-001 RESOLVED** | A1, A2, A3 | Three-sentence battery confirms the distinctions. See summary below. |
| **P-AF-001 RESOLVED** | B1, B4 | `ru` attested twice. See summary below. |
| **`no` as minimal negative** | B3 | Paired with `ru` (B1). First corpus use. Clean. Structural parallel established: `ru — [elaboration]` ↔ `no — [elaboration]`. |
| **`ti-re` vs `ti-be`** | B4 | `ti-re` (recurring time) first use. Distinction from `ti-be` (next time): `ti-re` is the recurring next occurrence; `ti-be` is the next temporal interval generally. Does this distinction hold under corpus pressure? Watch. |
| **`no-ne-fe`** | B2, B3 | `no-` + `ne-fe` (dependency compound W042) = no established link. Second use in same conversation: stable compound, register for next session. |
| **`ne-ra-ki  be`** | A4 | Using `ne-ra-ki` (inchoative) + `be` (grow): "the attuning develops." This uses the inchoative as a nominal/process that can itself grow. Grammatically interesting — the entering-state is itself subject to `be`. |

---

### C006 Summary: P-QM-001 and P-AF-001 resolved

**P-QM-001 — Polar vs content questions: RESOLVED.**

The distinction is **positional**, not lexical. Both question types use `to-si`; the
position of `to-si` relative to the proposition determines the type:

| Type | Structure | `to-si` position | Unknown |
|------|-----------|-----------------|---------|
| Content | `[entity]  [relation]  [dimension]  to-si?` | **inside**, in argument slot | The argument in that slot |
| Polar | `to-si — [complete proposition]` | **outside**, fronting the proposition | The truth value |

The three-sentence test:
- A1 (`to-si — lo-pa-ra  be-now`) = polar: `to-si` outside, proposition complete. ✓
- A2 (`lo-pa-ra  ne-ra  vo  to-si?`) = content: `to-si` inside, in qualifier slot. ✓
- A3 (`to-si — la-mi  ne-ra-ki`) = potentially ambiguous BUT the positional rule
  resolves it as polar. Content reading would require `la-mi  ne-ra-ki  to-si?`
  (in-argument). As written — `to-si` fronted — the question is polar (truth value of A
  attuning), with the patient recovered from discourse context. ✓

**No new polar particle needed.** The positional rule is sufficient. `to-si` carries both
question types; the position disambiguates. Any genuinely persistent ambiguity (fronted
`to-si` before a proposition with an *unknown* argument) is dissolved by the response:
a complete answer satisfies both readings simultaneously.

**P-AF-001 — Minimal affirmative: RESOLVED.**

`ru` (W039, unity/coherence) works as a minimal affirmative. Two corpus attestations
in C006 (B1, B4). Semantically transparent: `ru` = "[that] coheres" = yes.

Pair established:
- Affirmative minimal: `ru` (or `ru — [elaboration]`)
- Negative minimal: `no` (or `no — [elaboration]`)

Both are transparent extensions of the root primitives (`ru` = coherence/unity;
`no` = negation/absence). No new particles invented; the primitives serve as
discourse particles in sentence-initial position.

Three-tier confirmation strategy now fully attested:

| Strategy | Form | First use | When to use |
|----------|------|-----------|-------------|
| Minimal `ru` | bare `ru` or `ru — [detail]` | C006 B1 | fast acknowledgment; clean polar confirmation |
| Echo-confirm | restate proposition from speaker's perspective | C003 B1 | confirms understanding *and* speaker's position |
| Action-commit | `ka-[action]` = I am/will do it | C001 B3 | confirms AND commits to action |

**Emergent compound from this batch:** `no-ne-fe` (no active link / no dependency state).
First used B2, reused B3. Registered as W075 (`3323195`).

---

## Epistemic Testimony (C007)

---

**C007 — Formal testimony: the negated epistemic scale**

*Scene: After the C006 field anomaly, the ship's knowledge-keeper (`to-fe-ki-li`, A)
conducts a formal post-event testimony session with pilot B (`ra-ki-li`) regarding
what the pilot knew — and did not know — during the approach.*

*Tests: bare `la-mi  to  [prop]` (first clean first-person established modal); `no-to`
second attestation (C005 B3 was first); `no-si` first attestation; `no-se` first
attestation; nested epistemic embedding (A5, outer frame certifies inner epistemic
state); bare `ru` with no elaboration (B5, fourth attestation, first completely bare
use).*

---

**Turn A1**

```
Gloss:    to-si — la-tu  to  [lo-pa-ra  nu-be  lo-si-fe]
Literal:  knowledge-inquiry — agent:you  established  [patient:field  exceeds  threshold]
Natural:  Do you hold as established: the field exceeded threshold?
```

**Notes:**
- Polar question (`to-si` fronted). Distinctively, the embedded proposition itself
  contains an epistemic modal: A is not asking about the field event but about B's
  epistemic *status* regarding it. "Is it the case that you hold [X] as established?"
  — the object of inquiry is B's epistemic commitment.
- First polar question in the corpus directed at a speaker's epistemic state rather than
  a physical or social fact. The structure `to-si — la-tu  [modal]  [sub-prop]` is
  the formal interrogative for probing someone's epistemic level.
- This sets the investigator's method: ask about `to` level first, then drill down.

---

**Turn B1**

```
Gloss:    ru — la-mi  to  [lo-pa-ra  nu-be  lo-si-fe]
Literal:  [affirm] — agent:I  established  [patient:field  exceeds  threshold]
Natural:  Yes — I hold as established: the field exceeded threshold.
```

**Notes:**
- `ru` third full attestation (C006 B1, C006 B4, C007 B1). Pattern fully confirmed.
- **First clean `la-mi  to  [prop]` form.** The first-person speaker marking established
  personal knowledge. Prior `to`-level uses: C005 had third-person subjects (`la-yo  to
  [prop]`). Here the pilot makes a first-person claim at established level, with `la-mi`
  in the agent slot. The construction is parallel: `la-[speaker]  to  [prop]` = "I,
  the speaker, hold [prop] as a conceptual pattern / established fact." Full paradigm
  now covers both first-person and third-person subjects.
- Clean split emerging: B knows the event (threshold breach, `to`). B does not know
  the resonance character (upcoming B2, `no-to`). A testimony session can partition
  a speaker's knowledge at the proposition level.

---

**Turn A2**

```
Gloss:    lo-ne-ra  vo  to-si?
Literal:  patient:the-resonance  quality  [what]?
Natural:  What is the resonance character?
```

**Notes:**
- Content question (`to-si?` in qualifier slot). Identical form to C006 A2 (same topic,
  different institutional register: field-check vs formal testimony). The interrogative
  form is register-neutral; the institutional weight of the scene comes from context
  and participants, not syntax.
- Second occurrence of `lo-ne-ra  vo  to-si?` across the corpus: confirms the form
  is stable and repeatable when the referent is the same.

---

**Turn B2**

```
Gloss:    la-mi  no-to  [lo-ne-ra  vo]
Literal:  agent:I  not-established  [patient:the-resonance  quality]
Natural:  I do not hold the resonance character as established.
```

**Notes:**
- **`no-to` second corpus attestation.** First: C005 B3 (`la-mi  no-to` — pilot
  regarding the machine's soul-claim). Same frame (`la-mi  no-to  [embedded prop]`),
  different embedded proposition, different scene. Pattern confirmed: two attestations
  across two distinct conversations.
- DIRECT CONTRAST with B1: same speaker, same session, different propositions. B holds
  `to` (established) for the threshold breach. B holds `no-to` (sub-established) for
  the resonance character. The graduated scale enables exactly this: to report
  differential knowledge precision within a single testimony.
- `no-to` alone does not entail `no-si` or `no-se`. The pilot may still hypothesize
  or perceive the resonance character — the investigator needs to probe further.

---

**Turn A3**

```
Gloss:    to-si — la-tu  si  [lo-ne-ra  vo]
Literal:  knowledge-inquiry — agent:you  hypothesize  [patient:the-resonance  quality]
Natural:  Do you hypothesize a resonance character?
```

**Notes:**
- Polar question targeting the `si` (hypothesis) level. After B2 denied `to`, A probes
  the next level down: does B at least have a working model?
- Second corpus example of a polar question querying an embedded epistemic modal
  (first was A1 of this same batch). The pattern `to-si — la-tu  [modal]  [sub-prop]`
  is stable across levels.
- Systematic drilling: `to` (A1) → `si` (A3) → `se` (A4). Three questions, three
  levels. The investigator works from top down.

---

**Turn B3**

```
Gloss:    la-mi  no-si  [lo-ne-ra  vo]
Literal:  agent:I  not-hypothesize  [patient:the-resonance  quality]
Natural:  I do not hypothesize a resonance character.
```

**Notes:**
- **First corpus use of `no-si`.** `la-mi  no-si  [prop]` = the speaker denies having
  a working hypothesis about [prop]. Not merely sub-established — not even a formed
  working model.
- KEY DISTINCTION from `no-to`:
  - `no-to` (B2): I don't hold it as established. Could still hypothesize or perceive.
  - `no-si` (B3): I don't even hypothesize it. `no-si` entails `no-to` (if you have no
    hypothesis, you necessarily have no established knowledge either) but does NOT entail
    `no-se` (you could have a perceptual signal without forming a hypothesis from it).
- B3 removes the hypothesis possibility that B2 left open. After B2 + B3, the only
  remaining question is whether B has any raw perceptual signal at all.

---

**Turn A4**

```
Gloss:    to-si — la-tu  se  [lo-ne-ra]
Literal:  knowledge-inquiry — agent:you  perceive  [patient:the-resonance]
Natural:  Do you perceive the resonance?
```

**Notes:**
- Floor-level probe. `se` = raw perception / signal basis. The most basic question:
  does B have any signal data for the resonance at all?
- Note: the `vo` qualifier is absent. At the `se` floor, asking about perceptual
  *character* would be premature — A is asking whether any signal exists, not what
  character it has. The qualifier is properly omitted here.
- Third concurrence of polar + embedded epistemic modal in this batch (A1, A3, A4).

---

**Turn B4**

```
Gloss:    la-mi  no-se  [lo-ne-ra]
Literal:  agent:I  not-perceive  [patient:the-resonance]
Natural:  I have no perceptual basis for the resonance.
```

**Notes:**
- **First corpus use of `no-se`.** `la-mi  no-se  [prop]` = the speaker has no
  perceptual / signal basis for the embedded proposition. Epistemic floor: no raw input.
- HIERARCHICAL ENTAILMENT: `no-se` entails `no-si` and `no-to`. If you have no
  perceptual basis, you necessarily have no formed hypothesis and no established
  knowledge. B4 retroactively subsumes B2 and B3 — the floor denial is the maximally
  strong claim that covers the entire scale.
- After B4, the complete epistemic diagram for the resonance character:
  `se: absent / si: absent / to: absent`. Total epistemic blank.
  Contrast with the threshold breach from B1: `se: present / si: present / to: present`
  (established, which entails `si` and `se` were both active). Clean partition: B knows
  the event at every level; B has no epistemic contact with the resonance at any level.

---

**Turn A5**

```
Gloss:    la-mi  to  [la-tu  no-se  lo-ne-ra]
Literal:  agent:I  established  [agent:you  not-perceive  patient:the-resonance]
Natural:  I hold as established: you have no perceptual basis for the resonance.
```

**Notes:**
- **First corpus case of nested / stacked epistemic modals.** The outer frame
  `la-mi  to` (A certifies at established level) takes an embedded proposition that
  itself contains an epistemic disclaimer: `la-tu  no-se  lo-ne-ra` (B has no
  perceptual basis for the resonance). A is converting B's personal epistemic floor
  into a formally certified matter of record.
- This is the institutional function of open testimony: the knowledge-keeper transforms
  a speaker's subjective epistemic state into a certified fact. "It is established that
  you have no signal basis" — the negative epistemic state becomes a positive certified
  claim about that state.
- The `no-se` floor is chosen for the outer certification: since `no-se` entails
  `no-si` and `no-to`, certifying at floor is the maximally strong institutional
  summary without redundancy. "I establish that your epistemic contact is zero" is
  more economical than certifying each level separately.
- Grammatically: the embedding works because `la-tu  no-se  lo-ne-ra` is a well-formed
  proposition (agent + negated epistemic root + embedded patient). It occupies the
  `[prop]` slot of `la-mi  to  [prop]` exactly as any other proposition. No special
  construction is needed; subordination generates nested epistemic embedding freely.

---

**Turn B5**

```
Gloss:    ru
Literal:  [affirm/cohere]
Natural:  Acknowledged.
```

**Notes:**
- **Bare `ru` with no elaboration: fourth total attestation, first completely bare
  use.** Prior three: C006 B1 (`ru — [detail]`), C006 B4 (`ru — [detail]`), C007 B1
  (`ru — [detail]`). All had elaborations following the dash. Here, B ratifies A's
  formal institutional summary with nothing added — no correction, no detail, no
  new information.
- In formal institutional contexts, bare `ru` is the acknowledgment token: pure
  alignment without additional content. The `— [elaboration]` seen in all prior uses
  was a choice to add more, never a syntactic requirement.
- Confirms: `ru` is fully functional as a standalone clause. The minimum affirmative
  in Tonesu is one word.

---

**C007 Gaps and pressures:**

| Gap | Location | Status |
|-----|----------|--------|
| **`la-mi  to  [prop]` first-person** | B1 | Second occurrence across speakers (C005: third-person; C007 B1: first-person). Pattern fully confirmed for all persons. |
| **`no-to` → CONFIRMED** | B2 | Second attestation (C005 B3, C007 B2). Two scenes, two different embedded propositions. Pattern confirmed. |
| **`no-si` first use** | B3 | One attestation. Compositionally expected to work exactly as designed; watch for second. |
| **`no-se` first use** | B4 | One attestation. Same as above; watch for second. |
| **Nested epistemic embedding** | A5 | First instance. Structurally clean and compositionally derived. Watch for second before treating as fully confirmed general rule. |
| **`la-mi  se  [prop]` (positive perceptual floor)** | — | Negated form (`no-se`) now attested; positive has not yet appeared in corpus. Expected by symmetry. Watch. |
| **Bare `ru`** | B5 | Fourth total; first bare, confirming optional elaboration. Fully confirmed. |

---

### C007 Summary: negated epistemic scale

The `la-[speaker]  [modal]  [prop]` frame takes three epistemic roots (`se`, `si`, `to`)
and their negated forms (`no-se`, `no-si`, `no-to`). The six forms confirm a
hierarchically structured subsystem:

| Level | Positive | Negative | Entailments |
|-------|----------|----------|-------------|
| Established | `to` | `no-to` | `to` → `si` + `se`; `no-to` → nothing |
| Hypothesis | `si` | `no-si` | `si` → `se`; `no-si` → `no-to` |
| Perceptual | `se` | `no-se` | (floor); `no-se` → `no-si` + `no-to` |

Positive: floor implies upper levels (`se` is required for `si`, `si` for `to`).
Negated: floor denial implies all upper denials (`no-se` subsumes `no-si` and `no-to`).
Mid-level negations do not imply lower levels: `no-to` alone is consistent with having
`si` or `se`.

The negated forms use `no-` as a prefix on the epistemic root in the standard modal
frame. The mechanism is fully compositional — no special rule needed. Formalized in
spec/grammar.md § Epistemic Modality.

**`no-to` vs `no-to-fe`** remain distinct constructions (noted in spec):
- `no-to` in epistemic position = personal epistemic disclaimer (two morphemes)
- `no-to-fe` as state predicate = institutional status descriptor (three morphemes)

---

## Kinship Probe (S093–S100)

---

**Scene: crew registry — next-of-kin declaration**

*Before a long-range mission, the knowledge-keeper (`to-fe-ki-li`) records formal
kinship declarations from each crew member. Pilot (`ra-ki-li`) and navigator
(`di-ki-li`) are present. Sentences are formal declarations, not natural dialogue:
each one tests a specific kinship composition.*

*Design note: this batch probes whether `zo-ne` (living-kin-relation) as a base
compound plus directional qualifiers (`go` = origin, `du` = result, `ru` = unity,
`re` = iterated) can cover the full kinship vocabulary without new primitives. It
also tests the limits of kinship path composition: when does stringing kin-steps
together require grammatical machinery Tonesu doesn't have yet?*

*No new primitives expected. Predicted gaps: noun modification / relative clause
(for embedding a multi-step kin path as an argument), and numeral/cardinal system
(for specifying generation distance precisely).*

---

**S093 — Parent (one step up)**

```
Gloss:    lo-di-ki-li  zo-ne-go  la-mi
Literal:  patient:navigator  living-kin-origin  agent:I
Natural:  The navigator is my parent.
```

**Notes:**
- **First corpus use of `zo-ne-go` (W077).** `zo-ne` = living kin relation (base);
  `go` = origin/source. Together: the entity that is the living-kin-source of the
  reference person. "The navigator is [my] living-kin-origin" = the navigator is
  my parent.
- No sex distinction. `zo-ne-go` is sex-neutral — it covers what English splits
  into "mother" and "father." Tonesu has no sex or gender primitive, so kinship
  terms are structurally sex-blind. The language cannot say "my mother" vs "my
  father" without additional vocabulary that does not naturally derive from the
  existing primitives. This is a Concordian cultural result, not a gap: the
  kinship system treats the parent-child bond as structurally prior to sex.
- **`la-mi` in the second participant position.** The relational predicate has two
  participants: `lo-di-ki-li` (the entity BEING described as a kin-type) and
  `la-mi` (the reference anchor = the speaker, from whose perspective the
  kin-relation is defined). The speaker uses `la-mi` (not `lo-mi`) — consistent
  with the established pattern where first-person always marks its speaker as `la`
  ("agent" in the broad sense of: perspective-holder, perspective-anchor). This
  is a semantic extension of `la` beyond strict intentional action — `la` serves
  as the relational perspective anchor in stative-relational predicates. Flag as
  new grammatical use pressure.

---

**S094 — Child (one step down)**

```
Gloss:    lo-ra-ki-li  zo-ne-du  la-mi
Literal:  patient:pilot  living-kin-result  agent:I
Natural:  The pilot is my child.
```

**Notes:**
- **First corpus use of `zo-ne-du` (W078).** `zo-ne` base + `du` (result/effect) =
  the entity that is the kin-result of the reference person = child/offspring.
- The structural parallel with S093 is exact: `lo-[described-party]  [kin-type]
  la-[reference-person]`. The kin-type (`zo-ne-go` vs `zo-ne-du`) encodes the
  direction: toward the source (parent) vs away from the source (child). The
  reference person (`la-mi`) is always in the same position.
- **`go`/`du` as relational direction qualifiers.** Already established as origin/
  result for causal relations (`go-du` frame). Here they extend into kinship:
  `go` = the source party in the kin-bond; `du` = the result party. The extension
  is semantically transparent — biological parentage is a special case of the
  origin/result polarity. No new semantic burden on either primitive.

---

**S095 — Sibling**

```
Gloss:    lo-ra-ki-li  zo-ne-ru  la-mi
Literal:  patient:pilot  living-kin-unity  agent:I
Natural:  The pilot is my sibling.
```

**Notes:**
- **First corpus use of `zo-ne-ru` (W079).** `zo-ne` base + `ru` (unity/oneness
  /singularity) = kin-unity = a person who shares one origin with the reference
  person. The `ru` qualifier marks that the kin-bond is one of sameness: pilot and
  speaker have the same source. Semantically: `ru` (unity) applied to the kinship
  relation = "we are one in terms of origin."
- Same structural pattern as S093/S094.
- Tonesu sibling is also sex-neutral: no distinction between brother and sister.
  `zo-ne-ru` covers both. The language has no mechanism for sex-typed kin terms
  without an unregistered sex primitive — and the design pressure for such a
  primitive has not yet appeared.
- The sibling relation is symmetric: `lo-A  zo-ne-ru  lo-B` ↔ `lo-B  zo-ne-ru
  lo-A`. The directionality (`la`/`lo`) signals only WHOSE perspective anchors
  the description, not the direction of the bond itself.

---

**S096 — Parent's sibling ("aunt/uncle" equivalent): two-sentence path**

```
Gloss:    [S096a]  lo-di-ki-li  zo-ne-go  la-mi
Literal:  patient:navigator  living-kin-origin  agent:I
Natural:  The navigator is my parent.

          [S096b]  lo-ra-ki-li  zo-ne-ru  lo-di-ki-li
Literal:  patient:pilot  living-kin-unity  patient:navigator
Natural:  The pilot is the navigator's sibling.
```

**Notes:**
- **First multi-step kinship path in corpus.** English compresses this to "aunt"
  or "uncle." Tonesu does not. The path is TWO SENTENCES because the kin-bond
  is two steps: from speaker → to parent → to parent's sibling.
- S096b uses `lo-di-ki-li` in the reference position rather than `la-mi`. This
  confirms the reference participant is not limited to first-person — any
  patient-marked entity can anchor a kinship predicate.
- KEY FINDING: **Tonesu cannot compress this into a single noun phrase without
  a relative clause.** "My parent's sibling" used as a single noun phrase
  argument (e.g. "I spoke to my parent's sibling" in one sentence) requires
  describing the pilot as "the entity who has kin-unity with the entity who has
  kin-origin status toward me" — which is a relative clause embedding. NO
  relative clause introducer exists in Tonesu grammar yet. This is the first
  corpus moment that definitively requires one. (See NM-001 in open questions.)
- Concordians handle this by stating the path declaratively, in sequence. The
  meaning accumulates across sentences. This is fully coherent as a communicative
  strategy — and from a Concordian perspective, the longer path is actually
  *more informative*, not a workaround. There is no pressure to abbreviate it.

---

**S097 — Ancestor (iterated parent)**

```
Gloss:    lo-di-ki-li  zo-ne-go-re  la-mi
Literal:  patient:navigator  living-kin-origin-recurring  agent:I
Natural:  The navigator is my ancestor.
```

**Notes:**
- **First corpus use of `zo-ne-go-re` (W080).** `zo-ne-go` (parent, W077) +
  `re` (recurrence/cycle) = the recurringly-iterated kin-source = ancestor.
  An ancestor is a parent of a parent of a parent... the `re` marks that the
  origin step recurs up the lineage.
- `zo-ne-go-re` is **non-specific about generation distance**. It says "some
  iterated number of kin-steps back." The navigator could be the speaker's
  grandparent, great-grandparent, or any more distant ancestor. The compound
  captures the property of being IN the ancestral line, not the specific degree.
- **Generation count is not expressible with current vocabulary.** To say
  "two generations back" (grandparent specifically) requires either:
  (a) a numeral system (integers, "two" — not yet in corpus); or
  (b) a two-sentence path (`lo-A  zo-ne-go  la-mi` / `lo-B  zo-ne-go  lo-A`
  — B is A's parent; A is my parent; therefore B is my grandparent).
  The language has `nu` (quantity/number) and `re` (recurrence) but no cardinal
  counting system yet. This is the first sentence that definitively requires one.
  (See NUM-001 in open questions.)

---

**S098 — Descendant (iterated child)**

```
Gloss:    lo-ra-ki-li  zo-ne-du-re  la-mi
Literal:  patient:pilot  living-kin-result-recurring  agent:I
Natural:  The pilot is my descendant.
```

**Notes:**
- **First corpus use of `zo-ne-du-re` (W081).** `zo-ne-du` (child, W078) +
  `re` (recurrence) = iterated kin-result = descendant. Parallel structure to
  W080 (`zo-ne-go-re`); the `re` adds the iteration.
- The compound set is now symmetric at every level:
  - parent / child: `zo-ne-go` / `zo-ne-du`
  - ancestor / descendant: `zo-ne-go-re` / `zo-ne-du-re`
  - sibling: `zo-ne-ru` (no directional pair — the sibling bond is symmetric)

---

**S099 — Grandparent: the generation-count problem**

```
Gloss:    lo-di-ki-li  zo-ne-go  lo-ra-ki-li — lo-to-fe-ki-li  zo-ne-go  lo-di-ki-li
Literal:  patient:navigator  kin-origin  patient:pilot — patient:keeper  kin-origin  patient:navigator
Natural:  The navigator is the pilot's parent. The keeper is the navigator's parent.
          [Therefore: the keeper is the pilot's grandparent — by two-sentence path.]
```

**Notes:**
- **Two-sentence path for "grandparent."** No single-sentence equivalent is
  available without a numeral (to quantify generation distance) or a
  relative clause (to embed a kin-noun phrase). Two declarations, two steps.
- This sentence also shows `zo-ne-go` with non-first-person reference: both
  `lo-ra-ki-li` and `lo-di-ki-li` serve as the reference anchor (the `la`
  slot is replaced by `lo` for third-person parties). Confirms: the reference
  anchor position takes `la` for first/second person and `lo` for third-person —
  consistent with the existing case marking paradigm.
- English compresses "grandparent" into a single word. Tonesu requires TWO
  sentences. This is not awkward — it's structurally honest about the fact that
  "grandparent" IS a two-step path. The compression in English is a convenience
  label, not deeper information. Tonesu makes the path explicit.

---

**S100 — "Cousin" as a three-sentence path**

```
Gloss:    [S100a]  lo-di-ki-li  zo-ne-go  la-mi
Natural:  The navigator is my parent.

          [S100b]  lo-ra-ki-li  zo-ne-ru  lo-di-ki-li
Natural:  The pilot is the navigator's sibling.

          [S100c]  lo-li  zo-ne-du  lo-ra-ki-li
Natural:  Someone is the pilot's child.
```

**Notes:**
- **The "cousin" equivalence — three sentences.** Each step is one sentence.
  English "cousin" = parent's sibling's child = three structural facts.
  Tonesu states all three. No compression is attempted; none is needed.
- S100c uses unspecific `lo-li` (patient: a person, unspecified) in subject
  position. This is the first use of bare `li` (person/social agent) as an
  existential rather than a specific named individual. The sentence asserts
  that SOME person is the pilot's child without naming them.
- **The compression trap.** English speakers encountering this system might
  want to register a compound `zo-ne-ru-du` = kin-unity-result = "child of
  one's sibling" — the Tonesu analogue of "cousin." This would be legitimate
  as a compound. The question is whether Concordians WANT it. Given what
  the language has shown: they probably don't. A compressed label drops the
  path information. "My cousin" in English is ambiguous about *which* parent's
  sibling's child — first cousin vs second cousin, once-removed vs twice-removed
  — precisely because the label compresses away the path. Tonesu deliberately
  does not compress it.
- If Concordian culture ever needs a kinship term for "the child of your
  assigned crew partner" or similar social bond (not biological kin), that would
  be built from `wi-ne` or `ne-li` (intentional-relation or relational-person),
  NOT from `zo-ne`. The `zo-ne` family is strictly biological lineage.

---

**S093–S100 Summary: kinship system**

**All kinship vocabulary composes from two primitives: `zo` (living) and `ne` (relation).**

The base compound `zo-ne` (W076, biological kin bond) functions as the base for
all specific kinship terms. Five compounds are sufficient for the entire biological
kinship vocabulary:

| Compound | W#  | Meaning | Composition |
|----------|-----|---------|-------------|
| `zo-ne` | W076 | biological kinship (base) | living + relation |
| `zo-ne-go` | W077 | parent | kin + origin |
| `zo-ne-du` | W078 | child/offspring | kin + result |
| `zo-ne-ru` | W079 | sibling | kin + unity |
| `zo-ne-go-re` | W080 | ancestor | kin-parent + recurrence |
| `zo-ne-du-re` | W081 | descendant | kin-child + recurrence |

All kin terms are **sex-neutral**. Tonesu has no sex primitive; the parent-child
bond is structurally prior to biological sex. "Mother" and "father" do not exist
as separate terms.

Kinship paths beyond one step are described as **sequences of simple sentences**.
"Cousin" is three sentences. "Grandparent" is two. There is no pressure to
abbreviate — the path carries more information than a compressed label.

**Two grammatical pressures surfaced:**

| Gap | Location | Pressure |
|-----|----------|---------|
| **NM-001: Relative clause / noun modification** | S096 | Cannot embed "parent's sibling" as a single noun-phrase argument. Requires a relative clause introducer not yet defined. |
| **NUM-001: Numerals / cardinal counting** | S097, S099 | Cannot specify generation distance precisely (`zo-ne-go-re` = "some ancestor," not "grandparent" specifically). System needs cardinal numbers. |

**`la` as relational anchor:** `la-mi` appears in the reference position of kinship
predicates (not as a strict intentional agent but as the perspective-holder of the
kin-bond). This is a previously undocumented use of `la`. Related to P-PR-001
(`ze` back-reference); both arise from the same underlying question: how does Tonesu
mark a participant whose role is epistemic/relational reference rather than action
initiation?

---

## NM-001 Probe: Head-Final Clause Modification (S101–S107)

---

**Scene: Knowledge-keeper's review session — post-mission documentation**

*Three days after the C006/C007 field anomaly, the knowledge-keeper (`to-fe-ki-li`)
is working through post-mission records with the navigator (`di-ki-li`). These are
administrative declarative sentences produced in a formal documentation register.*

*Design: test the head-final modification hypothesis across seven distinct cases.*

*Candidate rule under test: a noun phrase can be preceded by a modifying clause
from which the head noun is absent (the "gap"). The head noun appears after the
modifying clause, marked by the particle appropriate to its role in the MAIN CLAUSE.
Notation: `[modifier clause]  role-particle + head`. No relativizer particle is
introduced — the construction extends the existing head-final modification principle
from morpheme scale to clause scale.*

*Seven cases, in order of structural complexity: (S101) agent gap; (S102) patient
gap, head as predication subject; (S103) head as recipient in matrix; (S104) stative
kinship relative; (S105) nested two-level kinship; (S106) the original S019 B
target; (S107) stative inner clause + first `la-mi  se  [prop]`.*

---

**S101 — Agent gap: head as patient of matrix**

```
Gloss:    [lo-ne-ra  ka-se]  lo-mu  ne-mi  ka-be
Literal:  [patient:resonance  perceived]  patient:machine  recipient:me  action:produce
Natural:  Build me the machine that perceived the resonance.
```

**Notes:**
- **First corpus use of head-final clause modification.** The structure:
  `[lo-ne-ra  ka-se]` = a clause meaning "perceived the resonance" — with no `la-[agent]`
  present. The gap is in the `la` position. The head noun `lo-mu` (the machine) follows
  directly, filling that gap semantically: the machine IS the thing that perceived the
  resonance. In the main clause, `lo-mu` functions as patient of `ka-be` (build it
  for me). The `lo` marking on the head is its MAIN-CLAUSE role, not its inner-clause
  role (where it was the agent).
- **This directly satisfies S019 Version B** — the target that was deferred at S019
  because no relativizer existed. "A machine that already perceived the resonance" is
  incidental predication (not "a sensing-device by class"). The relative clause form
  handles it; the compound form `se-mu` (W from corpus) handles the CLASS meaning. The
  distinction is now expressible.
- **Key parsing fact:** `lo-ne-ra  ka-se` without a `la` agent is incomplete as a
  standalone sentence — an agent is expected but absent. This incompleteness is what
  signals to the parser that a gap exists and that the following `lo-mu` fills it.
  Standalone sentences in Tonesu require an agent or a licensed drop (imperative or
  established speaker-drop). Here neither license applies, so the gap is obligatorily
  filled by the following head.

---

**S102 — Patient gap: head as subject of stative predication in matrix**

```
Gloss:    [la-di-ki-li  ka-se]  lo-ne-ra  no-to-fe
Literal:  [agent:navigator  perceived]  patient:resonance  not-certified
Natural:  The resonance that the navigator perceived is uncertified.
```

**Notes:**
- **Patient gap.** The inner clause `la-di-ki-li  ka-se` has an agent (navigator) but
  no patient. The gap is in the `lo` position. Head `lo-ne-ra` fills the patient gap
  semantically: the navigator perceived the resonance. In the matrix, `lo-ne-ra` is
  the subject of the stative predication `no-to-fe` (uncertified). Particle `lo` is
  consistent: the resonance is the patient/subject of both the inner clause (gap) and
  the matrix predication.
- **Contrast with agent gap (S101):** in S101, the gap is `la-[head]` (agent) and the
  head exits with `lo` (patient in matrix). In S102, the gap is `lo-[head]` (patient)
  and the head exits with `lo` (also the role for a stative subject in the matrix). The
  critical difference: in S101 the head's inner role ≠ outer role (agent → patient); in
  S102 the head's inner role = outer role (patient → `lo`-subject). The `lo` marking
  is purely the matrix role; the inner role is whatever it needs to be to fill the gap.
- **Matrix is stative (no `ka`).** `lo-ne-ra  no-to-fe` = "the resonance [is]
  uncertified" — a predication with no action particle. This confirms the matrix
  predicate does not need to be an action clause; any predication form that can take
  a `lo-head` argument is a valid matrix for a head-final relative NP.

---

**S103 — Agent gap: head as recipient of matrix (particle changes from `lo` to `ne`)**

```
Gloss:    la-mi  lo-si-ki  [lo-ne-ra  ka-se]  ne-mu  ka-be
Literal:  agent:I  patient:code  [patient:resonance  perceived]  recipient:machine  action:give
Natural:  I gave the code to the machine that perceived the resonance.
```

**Notes:**
- **Same inner clause as S101** (`[lo-ne-ra  ka-se]`, gap = agent) but the head exits
  with `ne-mu` (recipient) instead of `lo-mu` (patient). The head's MATRIX role is
  recipient, not patient. This demonstrates the key principle: **the particle on the
  head encodes the head's role in the MAIN CLAUSE, independently of its role in the
  inner clause.** The head-final position carries role information for the outer structure;
  the inner structure's role is inferred from the gap.
- **Disambiguation:** a naive reading of `ne-mu` alone would be "to the machine"
  (recipient). In context, `[lo-ne-ra  ka-se]  ne-mu` is unambiguous: the bracket
  precedes and modifies `ne-mu`, so `ne-mu` is the head of that NP. The inner clause
  provides the relative description; `ne-mu` provides the matrix slot.
- **Confirmed: the role-particle on the head is the external role anchor.** The same
  head `mu` (machine) can exit as `lo-mu` (S101, patient), `ne-mu` (S103, recipient),
  or — by analogy not yet tested — `la-mu` (agent of matrix) or `pa-mu` (location).

---

**S104 — Stative kinship relative: `la-mi` as perspective anchor inside inner clause, head as recipient of matrix**

```
Gloss:    la-mi  lo-si-ki  [zo-ne-go  la-mi]  ne-li  ka-be
Literal:  agent:I  patient:code  [kin-origin  anchor:I]  recipient:person  action:give
Natural:  I gave the code to the person who is my parent.
```

**Notes:**
- **Stative inner clause — no `ka`.** `zo-ne-go  la-mi` is a kinship predication without
  an action particle: "kin-origin [from] my perspective." The gap is in the `lo`
  position — the entity BEING described as "my parent" is absent from the clause and
  filled by the head `ne-li`.
- **`la-mi` appears twice in this sentence:** once as the action agent of the matrix
  (`la-mi ... ka-be` = "I give") and once as the relational anchor inside the kinship
  clause (`zo-ne-go  la-mi` = "my kin-origin"). These are structurally distinct: the
  outer `la-mi` anchors the matrix action; the inner `la-mi` anchors the relational
  definition from which the kin-type is determined. The brackets disambiguate which
  level each `la-mi` belongs to.
- **`la` as perspective anchor confirmed in embedded context.** In the inner clause,
  `la-mi` is NOT the agent of any action — it is the reference entity from whose
  standpoint the kin-relationship is defined. This is the clearest corpus case yet that
  `la` marks "the participant from whose perspective the clause is evaluated," rather
  than "the intentional agent of an action." The construction is grammatically well-
  formed by applying the head-final modification rule to a stative kinship predication.

---

**S105 — Nested two-level modification: "my parent's sibling" as embedded argument**

```
Gloss:    la-mi  lo-si-ki  [zo-ne-ru  [zo-ne-go  la-mi]  lo-li]  ne-li  ka-be
Literal:  agent:I  patient:code  [kin-unity  [kin-origin  anchor:I]  patient:person]
          recipient:person  action:give
Natural:  I gave the code to my parent's sibling.
```

**Notes:**
- **This sentence directly resolves the S096 NM-001 trigger.** S096 first exposed that
  "my parent's sibling" could not be embedded as a single argument. This sentence embeds
  it as a recipient argument of a matrix clause.
- **Two-level nesting:**
  - Inner NP: `[zo-ne-go  la-mi]  lo-li` = "the person who is my parent." Gap = `lo-li`
    (patient slot — the entity being described as my parent). Head exits as `lo-li`
    because inside the outer relative clause it serves as the reference entity for the
    sibling relationship (the thing you are sibling TO, which takes `lo` marking per the
    existing kinship predicate structure: `lo-X  zo-ne-ru  lo-Y`). So this is a case where
    the inner head's inner-clause role IS `lo` — not a role change.
  - Outer NP: `[zo-ne-ru  [inner NP]  lo-li]  ne-li` = "the person who is sibling to
    [the person who is my parent]." The outer gap = `lo-[outer-head]` (the entity being
    described as the sibling). Head exits as `ne-li` (recipient in the matrix).
- **Readability check:** the sentence is longer than any prior single-sentence kinship
  expression, but each bracket level is structurally well-formed and the nesting is two
  levels, not three. Two levels of head-final embedding appear to be routinely parseable.
  Three or more levels would approach the limit of working memory; Tonesu Concordians
  likely use the multi-sentence path strategy for anything above two levels.

---

**S106 — S019 Version B: finally satisfied**

```
Gloss:    [lo-si-de  ka-to-ko]  lo-mu  ne-mi  ka-be
Literal:  [patient:past-signal  remembers]  patient:machine  recipient:me  action:build
Natural:  Build me a machine that remembers past signals.
```

**Notes:**
- **Direct satisfaction of S019 Version B** — the target that opened the relativizer
  gap in S019. The full original target was "Build me a system that remembers past
  queries." `lo-si-de` = signal-decay = prior/past signal data. `ka-to-ko` = action of
  containing knowledge = remembering/retaining. The machine is the agent of `ka-to-ko`
  (gap = `la-mu` position). Head exits as `lo-mu` (patient of `ka-be` = build).
- **Comparison with `to-ko-mu` (memory-device compound):** S019 Version A used
  `lo-to-ko-mu  ne-mi  ka-be` = "build me a memory device." That expressed a CLASS
  property — the device is BY DESIGN a memory-keeping device. S106 expresses an
  INCIDENTAL property — build me the specific machine that currently has the record of
  past signals. Both are valid; both are now expressible; they mean different things.
  - `to-ko-mu`: "a memory device" = class membership
  - `[lo-si-de  ka-to-ko]  lo-mu`: "the machine that remembers X" = incidental predication about a specific entity
  This is the distinction the relativizer was always needed for. It is now in the language.
- **`si-de`** (signal + decay = past signal) is its first appearance as a compound.
  Signal = `si`; decay = `de`; signal-that-has-undergone-decay = prior/historical signal
  record. Compositionally clean; not registered as it is an ad hoc compound in this
  context and may have narrower or broader application depending on future uses.

---

**S107 — Stative inner clause (no `ka`); first `la-mi  se  [prop]`**

```
Gloss:    la-mi  se  [lo-mu  ne-ra  no-to-fe]
Literal:  agent:I  perceive  [patient:machine  resonance  uncertified]
Natural:  I have a signal-level reading: the machine's resonance is uncertified.
```

**Notes:**
- **First corpus use of positive perceptual floor `la-mi  se  [prop]`.** C007 B4
  established `la-mi  no-se  [prop]` (perceptual floor negated). This is the positive
  form: "I hold at perceptual / signal level: [prop]." Consistent with the modal scale
  formalized in spec/grammar.md § Epistemic Modality. The positive scale is now fully
  attested: `la-mi  se` (S107), `la-mi  si` (C001 A3, C006 A4), `la-mi  to` (C007 B1).
- **The embedded proposition `[lo-mu  ne-ra  no-to-fe]` is a stative predication** —
  no `ka`. "The machine has uncertified resonance." The machine holds the `lo` patient
  position; `ne-ra` is a compound predicate; `no-to-fe` is the state modifier. The
  entire prop is a stative-predication clause, not an action clause. This confirms that
  the epistemic modal frame takes propositions of any predicate type (action and
  stative alike) — consistent with prior cases but here the first example where the
  prop is purely stative.
- **Stative relative test (companion):** the same inner clause `lo-mu  ne-ra  no-to-fe`
  can be tested as a relative modifier. By the head-final rule: `[ne-ra  no-to-fe]  lo-mu`
  = "the machine with uncertified resonance" — a stative-predicate relative clause with
  no `ka`, gap = `lo-mu` (patient of predication). The head exits as `lo-mu`. This works
  by the same rule as action-predicate relatives (S101–S103): the gap-and-head structure
  is unchanged; only the predicate type differs. Stative modifying clauses are confirmed
  possible. (This secondary form is noted here rather than given its own sentence because
  S107 already tests the stative prop type through the epistemic frame, and the relative
  form is compositionally derived with no additional findings.)

---

**S101–S107 Summary: NM-001 resolved**

**The head-final modification hypothesis holds across all seven test cases.**

### The rule

A noun phrase may be modified by a preceding clause from which the head noun
is absent (the gap). The head noun appears after the modifying clause, marked by the
particle appropriate to its role in the **main clause**. The absence of a participant
from the inner clause identifies the gap; the head fills that position in the inner
clause's semantic structure.

```
[  modifying clause  (gap)  ]   role-marker + head
```

The gap may be in any participant position:

| Gap position | Inner clause structure | Example |
|---|---|---|
| Agent (`la`) | `[lo-X  predicate]  lo-head` | S101, S103, S106 |
| Patient (`lo`) | `[la-X  predicate]  lo-head` | S102 |
| Predication subject (`lo`) | `[stative-predicate]  lo-head` | S107 companion |

### The role-particle principle

**The particle on the head encodes the head's role in the MAIN clause**, not in the inner
clause. A head-noun can exit with a different particle than the role it fills inside the
inner clause:

- S101: head is `la` (agent) inside → exits as `lo-mu` (patient) in matrix
- S103: head is `la` (agent) inside → exits as `ne-mu` (recipient) in matrix

The two-particle reality of the head (inner role inferred from gap; outer role explicit
on the head itself) requires no special machinery — gap inference was already available
from the imperative and speaker-drop constructions.

### No new particles required

The construction uses only existing notation and the existing head-final modification
principle, scaled from morpheme level to clause level. This is exactly the pattern
the language has consistently favored: generalize an existing principle rather than
innovate a new one.

### Disambiguation from subordinate clauses

Subordinate clauses have an explicit clause introducer before the bracket:
`go [...]`, `wi [...]`, `ta [...]`.

Relative modifier clauses have NO such introducer — the bracket
immediately precedes `role-marker + head`. This structural difference makes the two
constructions orthogonally distinguishable in both written gloss and speech.

### Nesting

Two levels of nesting are attested (S105) and parse cleanly. Three or more levels
accumulate complexity consistent with cross-linguistic limits on embedded center-
embedding; no formal restriction is imposed, but Concordians naturally
prefer the multi-sentence path strategy for paths deeper than two levels.

### `la` as perspective anchor: consolidated

S104 provides the clearest corpus evidence for the `la`-as-perspective-anchor
analysis. `la-mi` appears twice:

1. Outer `la-mi`: action agent of `ka-be` — the standard "agent does action" reading.
2. Inner `la-mi`: relational anchor of `zo-ne-go` — no action; the kinship predicate is
   evaluated from the perspective of the entity marked `la-mi`.

Both uses share the property that `la` marks **the participant from whose perspective
the clause is evaluated**. For action clauses, that perspective-holder is also the
initiator. For stative predicates (kinship, epistemic modals), the perspective-holder
is not an initiator but a reference anchor or stance-holder.

Consolidating: **`la` = perspective-privileged participant / evaluation anchor.** The
"agent" gloss is a useful shorthand for action clauses but is too narrow as a general
description. The spec should reflect this.

**P-QM-001, P-AF-001, P-NM-001 are all resolved.** The consistent pattern: grammar
gaps close through structural generalization of existing principles.

### Open items from this batch

| Item | Status |
|------|--------|
| `la-mi  se  [prop]` — first positive perceptual floor | **Attested** (S107). Positive scale complete. |
| NM-001 — relative clause / noun modification | **Resolved** (S101–S107). Rule formalized below. |
| `la` as perspective anchor | **Evidence consolidated** (S104). Spec gloss update needed. |
| Stative relative clauses (no `ka` in inner clause) | **Confirmed** (S107 companion). Same rule, no restriction on predicate type. |
| Three-level nesting | Not yet tested. Predicted: works but pragmatically avoided. |
| `si-de` (past-signal compound) | Ad hoc use (S106). Watch for second attestation before registering. |

---

## Phonological Stress Test: `se` / `so` / `si` Cluster (S108–S113)

**Purpose:** The three perception/signal roots `se` (raw perception), `so` (sound), and
`si` (encoded signal/representation) form a phonetic cluster distinguished only by vowel:
`/se/ /so/ /si/`. The open question in registry/primitives.md asks whether all three
survive at normal speech speed without confusion. This batch tests adjacency, alternation,
and minimal-pair contexts.

**Test strategy:**
- S108: `se` and `si` in the same sentence, different argument positions
- S109: `so` and `si` contrasted (acoustic signal vs. encoded representation)
- S110: all three in one sentence
- S111: `se`-compound and `si`-compound in adjacent predicate/argument positions
- S112: minimal pair — same sentence frame, swapping `se` for `si`
- S113: minimal pair — same sentence frame, swapping `so` for `si`

---

**S108 — `se` and `si` in same clause** *(T-PHN-001)*

*Target: "The pilot perceived the signal."*

```
Gloss:    la-ze  lo-si-mu  ka-se
Literal:  agent:they  patient:signal-artifact  action:perceive
Natural:  They perceived the encoded signal.
```

**Notes:**
- `si-mu` = encoded artifact = a record / document / transmitted data packet. Established
  compound (first used S068 area, discussed S070 notes). `si` = encoded representation;
  `mu` = artifact.
- `ka-se` = intentional perception / detection. `ka` (intentional action) + `se`
  (perception root). The pilot is actively reading/receiving the signal.
- **Phonetic adjacency:** `lo-si-mu` (patient) precedes `ka-se` (predicate). The sequence
  `si ... se` spans an argument boundary with a full NP between them. At normal speech
  rate: `lo-si-mu  ka-se` — the vowels /i/ and /e/ are separated by a morpheme boundary
  (`mu` + `ka`) and are in different prosodic feet. **No confusion risk in this position.**
- The distinction `si` (the signal as an encoded thing) vs `se` (the act of perceiving it)
  is semantically clear and is confirmed by the sentence's coherence: perceiving an encoded
  artifact is the canonical use of `ka-se` with a `si`-compound patient.

---

**S109 — `so` and `si` contrasted: acoustic vs. encoded** *(T-PHN-002)*

*Target: "The warning sound is not the same as the warning signal."*

```
Gloss:    lo-fe-so  lo-fe-si  no-ru
Literal:  patient:warning-sound  patient:warning-signal  not-unified/same
Natural:  The warning sound and the warning signal are not the same thing.
```

**Notes:**
- `fe-so` = boundary-sound = warning sound / alarm tone. The acoustic sensory event.
- `fe-si` = boundary-signal = warning signal / encoded alert. The encoded representation
  (which may be visual, data-based, or otherwise non-acoustic).
- `no-ru` = not-unified / not-the-same. Negated `ru` (unity/coherence) functions as a
  predicate of non-identity: "these two are not one thing."
- **Phonetic adjacency:** `lo-fe-so  lo-fe-si` — the crucial minimal pair appears in
  adjacent argument positions. The only difference: `/so/` vs `/si/`. In the full sequence:
  `fe-so ... fe-si`, the contrast is the final vowel of the compound. At normal speech
  rate this is a genuine discrimination challenge. The prosodic boundary between the two
  NPs provides a pause point, but the vowel distinction `/o/` vs `/i/` is the sole
  differentiator.
- **Verdict for this position:** MARGINAL. `/o/` and `/i/` are maximally distinct vowels
  (low-back vs. high-front) so the phonetic distance is large, but the near-identical
  compound frame `fe-so / fe-si` means a listener mishearing the final vowel gets a
  lexically valid but semantically wrong word. This is the cluster's sharpest exposure.

---

**S110 — All three roots in one sentence** *(T-PHN-003)*

*Target: "I heard the sound and encoded the perception."*

```
Gloss:    la-mi  lo-so  ka-se  wi  [lo-si-mu  ka-be]
Literal:  agent:I  patient:sound  action:perceive  purpose  [patient:signal-artifact  action:generate]
Natural:  I detected the sound, intending to produce a record of it.
```

**Notes:**
- `lo-so` = patient:sound. Bare `so` as a noun-equivalent in patient position: the sound
  (acoustic event) is what is being perceived.
- `ka-se` = action:perceive / detect.
- `wi [lo-si-mu  ka-be]` = purpose clause: "with the intention of producing a signal-
  artifact." `si-mu` = document/record; `ka-be` = generate / produce.
- **Three-root sequence:** `so ... se ... si` across the full sentence. Each root is
  separated by at least one particle or compound boundary. The sequencing at speech rate:
  `lo-SO  ka-SE ... lo-si-MU`. Crucially the three roots are never adjacent — they appear
  in different prosodic feet with particles and compound-modifiers between them.
- **Verdict for this position:** CLEAN. When separated by particle boundaries, the three
  roots are unambiguous. The vowels /o/, /e/, /i/ are all near-maximally distinct, and
  the intervening material provides perceptual reset time.

---

**S111 — `se`-compound and `si`-compound in adjacent positions** *(T-PHN-004)*

*Target: "The sensor's reading does not match the recorded data."*

```
Gloss:    lo-se-su  lo-si-su  no-ne
Literal:  patient:sensor-structure  patient:signal-structure  not-related/not-matching
Natural:  The sensor output and the archived data are not in agreement.
```

**Notes:**
- `se-su` = perception-structure = sensor / detection system. The physical arrangement
  that performs detection.
- `si-su` = encoded-structure = archive / database / document collection. Established
  compound (first attested S056).
- `no-ne` = not-related = mismatched / in disagreement. Negated `ne` (relation/connection)
  as a predicate: "these two do not relate / are not in correspondence."
- **Phonetic adjacency:** `lo-se-su  lo-si-su` — same compound frame, initial vowel is
  the only differentiator: `/se-su/` vs `/si-su/`. This is tighter than S109 because
  the contrastive vowel is in the first (stressed) syllable. At normal speech rate, the
  sequence is `se-su ... si-su` within adjacent NPs. Stress falls on the first syllable of
  each compound, so the distinguishing vowels `/e/` and `/i/` are both stressed.
- **Verdict for this position:** BORDERLINE. Stressed /e/ vs stressed /i/ is phonetically
  distinct (/e/ is mid-front, /i/ is high-front, ~2 semitones apart in F1), but the
  near-identical compound frame means the listener must rely on that single vowel height
  difference. In clear speech: unambiguous. In fast speech or noise: moderate risk.
  The context (sensor output vs. archived data) usually disambiguates semantically, which
  is a mitigating factor.

---

**S112 — Minimal pair: `se` vs `si` in predicate** *(T-PHN-005)*

*A: "The machine perceived the boundary."*
*B: "The machine encoded the boundary."*

```
A:  lo-mu  lo-fe  ka-se
    patient:machine  patient:boundary  action:perceive/detect
    The machine detected the limit.

B:  lo-mu  lo-fe  ka-si-ki
    patient:machine  patient:boundary  action:signal-encode(inchoative)
    The machine began encoding the limit as a signal.
```

**Notes:**
- `ka-se` = detect / sense. `ka-si-ki` = begin encoding / start signal-representation.
  The two predicates are structurally and semantically distinguishable — one is
  a simplex compound, the other is a three-morpheme compound — but both start with
  `ka-s`.
- **Verdict:** The full compounds `ka-se` vs `ka-si-ki` are unambiguous at any speech
  rate: `ka-se` (2 syllables) vs `ka-si-ki` (3 syllables). Length alone prevents
  confusion. The pure `se` / `si` distinction in compound-initial position (i.e. bare
  roots in isolation) would be riskier.

---

**S113 — Minimal pair: `so` vs `si` in compound-initial** *(T-PHN-006)*

*A: "The sound archive is damaged."*
*B: "The signal archive is damaged."*

```
A:  lo-so-su  de
    patient:sound-archive  decay/damage
    The sound archive is degraded.

B:  lo-si-su  de
    patient:signal-archive  decay/damage
    The signal archive is degraded.
```

**Notes:**
- `so-su` = sound-structure = acoustic archive / audio recording collection.
- `si-su` = signal-structure = signal archive / encoded document collection. Established
  compound (S056).
- **This is the definitive minimal pair for `so`/`si`.** The only phonetic difference in
  the sentence is the initial vowel of the first compound: `/so-su/` vs `/si-su/`. In
  isolation these are maximally distinct (/o/ low-back vs /i/ high-front). But the compound
  frames are otherwise identical, and the sentence structure `lo-X-su  de` provides no
  other disambiguation cue.
- **Verdict for this position:** CONTEXT-DEPENDENT. A sound archive and a signal archive
  are semantically adjacent concepts; semantic disambiguation is weaker here than for
  `se`/`si` pairs (where perception and encoding are more functionally distinct). In a
  domain where both types of archives are likely (e.g. a ship's data room), the single-
  vowel distinction carries full disambiguation weight with no semantic backup.

---

**S108–S113 Cluster Analysis: `se` / `so` / `si`**

| Test | Pair | Position | Verdict |
|------|------|----------|---------|
| S108 | `se` / `si` | different feet, argument boundary | **CLEAN** |
| S109 | `so` / `si` | adjacent NPs, compound-final | **MARGINAL** |
| S110 | `so` / `se` / `si` | all three, separated by particles | **CLEAN** |
| S111 | `se` / `si` | adjacent NPs, compound-initial (stressed) | **BORDERLINE** |
| S112 | `se` / `si` | predicate position, length differentiates | **CLEAN** |
| S113 | `so` / `si` | adjacent same-frame minimal pair | **CONTEXT-DEPENDENT** |

**Conclusion:**

The cluster survives in **all normal compound usage** where the roots appear with at
least one partner morpheme between them or where compound frame lengths differ. The
vowel system (/e/ mid-front, /i/ high-front, /o/ low-back) provides sufficient acoustic
distance for clear speech and ordinary noise conditions.

**The one genuine exposure:** same-frame adjacent minimal pairs (`lo-se-su  lo-si-su`,
`lo-so-su  lo-si-su`). In these constructions, a single phoneme carries full semantic
disambiguation with no structural or contextual backup. This is the predicted failure
mode.

**Design verdict:**
No reassignment needed. The cluster holds. One domain-specific risk is noted: Tonesu
should avoid register-appropriate shortening that produces bare `se`, `so`, or `si` in
contexts where adjacent roots are semantically close. In practice, compounds effectively
always provide compound-length disambiguation. The open question in primitives.md is
**resolved: the three roots are phonologically viable as distinct primitives.**

**Remaining watch:** if a future domain requires a specialized lexicon that heavily uses
both `so-[X]` and `si-[X]` compounds in adjacent positions (e.g. an audio engineering
domain), the `so`/`si` boundary should be evaluated again in that domain's sentence
patterns specifically. No action now.

---

## Four Deep Axes: Capability / Similarity / Possession / Counterfactual (S114–S125)

**Purpose:** Stress tests proposed by Monday for probing semantic axes that minimalist
primitive systems sometimes handle poorly. Four batches test: (1) capability vs intention
vs causation, (2) similarity vs identity vs component membership, (3) possession vs
containment, and (4) conditional/counterfactual logic.

**Ad hoc compounds introduced this batch:**
- `ra-ma` = energy-matter = fuel (energy-bearing raw material)
- `ki-pa-mu` = motion-place-artifact = vehicle / spacecraft (a place-artifact defined by movement)
- `to-ru` = pattern-unity = same model / same type / same design
- `ne-to` = relation-pattern = similarity / analogy (a relational pattern between two entities)
- `su-ru` = structure-unity = unified system / single system
- `pa-ki` = place-motion = spatial drift / uncontrolled movement through space
- `ra-be-vo` = energy-generative-quality = capacity for energy generation (three-morpheme compound)

---

### Test 1 — Capability vs intention vs causation (S114–S116)

**Target:** cleave three meanings English collapses into "can" / "designed to" / "because":
(1) dispositional capability, (2) design intention, (3) causal chain.

---

**S114 — Capability: "The reactor is capable of generating greater energy output."** *(T-AX-001)*

```
Gloss:    lo-ra-ki-mu  be-vo
Literal:  patient:engine  generative-quality
Natural:  The engine has generative capacity / is capable of producing output.
```

**Notes:**
- `be-vo` = growth-quality = generative potential. `be` (growth/increase) as the
  property-head modifying the entity; `-vo` suffix (via root `vo` = value/quality)
  marks this as a quality/degree predicate. `lo-ra-ki-mu  be-vo` = "the engine has
  the quality of being generative" = has productive capacity.
- **Comparison with S115 (`wi`-intention):** `be-vo` is a bare stative property —
  it makes no claim about direction, purpose, or agent. The reactor simply has this
  property. `wi [clause]` (S115) asserts a *directed goal state*, which requires an
  agent or design-institution. The two are clearly semantically distinct.
- **"Greater energy" can be appended:** `lo-ra-ki-mu  be-vo  lo-ra  nu-be` — "the
  engine has generative capacity [yielding] energy exceeding [current output]." The
  degree phrase floats after the predicate as a scope modifier, consistent with the
  comparison construction established in S064–S067. Both forms (bare `be-vo` and
  expanded `be-vo  lo-ra  nu-be`) appear to be grammatical.
- **Capability primitive verdict:** `be-vo` covers dispositional capability cleanly.
  The quality is the entity's *property*, not its intent or its causal history. The
  watch item can be updated: compound strategy is viable for this use case.

---

**S115 — Intention/design: "The reactor is designed to generate greater energy output."** *(T-AX-002)*

```
Gloss:    la-ra-ki-mu  wi  [lo-ra  nu-be  ka-be]
Literal:  agent:engine  design-purpose  [patient:energy  more-than  action:generate]
Natural:  The engine is [institutionally] designed for generating greater energy output.
```

**Notes:**
- `wi [clause]` = purpose frame. Established in spec/grammar.md § Purpose Frame.
  `la-ra-ki-mu  wi [...]` = the engine's design intent is [to generate greater energy].
- **Non-intentional agent in `wi` frame:** `ra-ki-mu` (an artifact) cannot have
  literal will. This is design-intent attribution, identical to the pattern in S034
  (`la-ra-ki-mu  wi [lo-ha  no-fe]` = the reactor must stay cool). The machine's `wi`
  is its functional design goal, not its agentive intention. Pattern confirmed: `wi [X]`
  on an artifact = prescriptive / design-goal reading. Social context (the institution
  that designed it) is implicit.
- **Contrast with S114:** S115 asserts a *directed goal state* (purpose); S114 asserts
  a *property* (capacity). A reactor that was designed to generate less power might
  still *be capable* of more (`be-vo`). A reactor designed for more power might
  currently be damaged and lack that capacity (`no-be-vo`). The two are logically
  independent — the language keeps them separate.

---

**S116 — Causation: "The reactor generates more power because of the new fuel."** *(T-AX-003)*

```
Gloss:    go [ra-ma  be]  lo-ra-ki-mu  lo-ra  nu-be  ka-be
Literal:  cause:[fuel  grows/added]  patient:engine  patient:energy  more-than  action:generates
Natural:  Because fuel was added, the engine generates greater energy output.
```

**Notes:**
- `ra-ma` = energy-matter = fuel. Head-final: `ma` (raw material/substance) is head;
  `ra` (energy) modifies it as an energy-bearing material. First use; compound candidate.
- `go [ra-ma  be]` = causal frame: the cause is [fuel growth/addition]. `ra-ma  be` =
  "fuel increases / fuel comes into existence" = fuel is added. The inner clause is a
  stative-change predication: bare `be` (growth) with `ra-ma` as patient, no agent.
- `lo-ra-ki-mu  lo-ra  nu-be  ka-be` = matrix clause: engine [regarding] energy
  more-than action:generates. The `lo-ra  nu-be` phrase is a topic-scope modifier
  ("with respect to energy, more than before") preceding the predicate `ka-be`.
- **Contrast with S114 and S115:** S116 is a factual causal assertion — the engine
  *is* generating more, *because of* X. No capability claim; no design-goal claim.
  The `go [X]  matrix` causal frame handles pure causation cleanly.
- **Three-way verdict (Test 1):** capability = `be-vo`, intention = `wi [clause]`,
  causation = `go [X]  matrix`. All three are formally and semantically distinct.
  No new primitive needed. Capability primitive watch item: `be-vo` is sufficient for
  current corpus pressure.

---

### Test 2 — Similarity / identity / component membership (S117–S119)

---

**S117 — Identity: "These two engines are the same model."** *(T-AX-004)*

```
Gloss:    lo-pu-ra-ki-mu  to-ru
Literal:  patient:plural-engine  pattern-unity
Natural:  The engines share a unified pattern / are the same model/type.
```

**Notes:**
- `to-ru` = pattern-unity. Head-final: `ru` (unity/singularity) is head; `to`
  (conceptual pattern) modifies it. "The unity in question is at the pattern level" =
  same design template = same model.
- `lo-pu-ra-ki-mu` = patient:plural-engine. `pu-` prefix marks plurality on the compound.
- **Contrast with S118:** `to-ru` asserts a single unified pattern — the two things share
  one conceptual template. `ne-to` (S118) asserts a relational pattern — the things are
  connected by pattern similarity, not necessarily identical. Same model (`to-ru`) is
  stronger than similar (`ne-to`).

---

**S118 — Similarity: "These two engines are similar."** *(T-AX-005)*

```
Gloss:    lo-pu-ra-ki-mu  ne-to
Literal:  patient:plural-engine  relation-pattern
Natural:  The engines have a relational pattern / are similar to each other.
```

**Notes:**
- `ne-to` = relation-pattern = similarity / analogy. Head-final: `to` (conceptual
  pattern) is head; `ne` (relation/connection) modifies it. "The pattern is a relational
  one" = there exists a pattern of mutual correspondence = similarity.
- **Strength distinction:** `to-ru` = they ARE one (pattern); `ne-to` = they RELATE
  (pattern). These are genuinely distinct: `to-ru` is identity, `ne-to` is analogy.
  No new primitive needed for similarity — `ne-to` is transparent and well-motivated.
- **Similarity primitive verdict:** `ne-to` is sufficient. Monday's prediction confirmed.

---

**S119 — Component membership: "These two engines are parts of the same system."** *(T-AX-006)*

```
Gloss:    lo-pu-ra-ki-mu  pe  lo-su-ru
Literal:  patient:plural-engine  component  patient:unified-structure
Natural:  The engines are components of one unified system.
```

**Notes:**
- `su-ru` = structure-unity = unified system / single system. Head-final: `ru` (unity)
  is head; `su` (structure/organization) modifies it. "The unity in question is
  structural" = a single organized system.
- `pe` as stative predicate: `lo-X  pe  lo-Y` = X is a component of Y. This extends
  `pe` from its primitive definition (part/component) into the predicate slot. The
  two-`lo` construction (`lo-X  pe  lo-Y`) parallels the comparison structure
  (`lo-X  quality  lo-Y`) established in S064–S067. **First corpus use of `pe` as a
  stative predicate.** The construction is compositionally clean.
- **Three-way verdict (Test 2):** identity = `to-ru`, similarity = `ne-to`, component
  membership = `pe` (predicate) with `su-ru` whole. All three are distinct. No new
  primitive needed.

---

### Test 3 — Possession vs containment (S120–S122)

---

**S120 — Possession: "The pilot has a tool."** *(T-AX-007)*

*Note: This is also the first attempt at the queued T001 — "This device belongs to me."
The test sentence is generalized to 3rd person for structural clarity.*

```
Gloss:    la-zo-li  ne  lo-mu-ka
Literal:  agent:person  relation/possess  patient:tool
Natural:  The person is in relation to (possesses) a tool.
```

**Notes:**
- `ne` as **stative possession predicate**. In particle use, `ne` precedes its NP
  (`ne-X` = recipient:X). In predicate use, `ne` stands alone between argument markers:
  `la-X  ne  lo-Y` = X holds a relational state with respect to Y. The disambiguation is
  structural: `ne` as particle would produce `ne-lo-mu-ka` (ungrammatical run-on) or
  appear before the NP without `lo`. In the predicate slot, `ne  lo-Y` is unambiguous.
- `mu-ka` = artifact-action = tool. Established compound (stress-test table, primitives.md).
- **Possession as relation:** Tonesu does not have a dedicated possession primitive.
  Ownership is a type of relation (`ne`). This is philosophically coherent with the
  setting: in Concordian culture, "having" is a relational state, not an ontological
  category. It can dissolve (`de`), strengthen (`be`), be transferred (`ne-particle`
  + `de`), or be in dispute (`ne-fe`).
- **First corpus test of possession via `ne` predicate.** T001 and T002 remain queued
  as more complex possession tests (pronoun reference, shared possession).

---

**S121 — Physical containment: "The tool is inside the container."** *(T-AX-008)*

```
Gloss:    la-ko-mu  ko  lo-mu-ka
Literal:  agent:container  containment  patient:tool
Natural:  The container holds the tool.
```

**Notes:**
- Applies the established `la-X  ko  lo-Y` rule (spec/grammar.md § Containment
  Predicates). The container is the `la`-agent of the containment state; the tool is
  the `lo`-patient (contents).
- `ko-mu` (W052) = containment-artifact = vessel/container. Used with `la` particle.
- **Contrast with S120:** `la-zo-li  ne  lo-mu-ka` = possession (relational state
  between person and tool, no spatial claim). `la-ko-mu  ko  lo-mu-ka` = containment
  (spatial state: tool is physically inside container, no ownership claim). The two
  predicates are orthogonal:
  - A pilot can possess a tool that is not in a container.
  - A tool can be in a container without being owned by anyone.
  - A pilot can own a tool that is stored in a container they don't own.

---

**S122 — Container perspective: "The container has tools in it."** *(T-AX-009)*

```
Gloss:    la-ko-mu  ko  lo-pu-mu-ka
Literal:  agent:container  containment  patient:plural-tools
Natural:  The container holds multiple tools.
```

**Notes:**
- Same structure as S121 with `pu-` pluralizer on the contents.
- **Possession/containment verdict (Test 3):** `ne` (possession) and `ko` (containment)
  are formally and semantically distinct. The `la`/`lo` argument positions are the same,
  but the predicates `ne` and `ko` carry entirely different meanings. The language
  cleanly separates:
  | Concept | Form | Predicate |
  |---------|------|-----------|
  | possession | `la-X  ne  lo-Y` | `ne` (relation) |
  | containment | `la-X  ko  lo-Y` | `ko` (containment) |
  - No new primitive needed. Monday's prediction confirmed.

---

### Test 4 — Conditional and counterfactual logic (S123–S125)

---

**S123 — Present/future conditional: "If the engine fails, the ship drifts."** *(T-AX-010)*

```
Gloss:    go [lo-ra-ki-mu  de]  lo-ki-pa-mu  pa-ki
Literal:  cause:[patient:engine  decay]  patient:vehicle  place:motion
Natural:  Given engine failure, the vehicle drifts through space.
```

**Notes:**
- `go [X]  matrix` = causal/conditional frame. Established in spec/grammar.md §
  Causal Frame and open-questions.md (Conditionals item). The causal frame functions
  as the conditional when the inner clause describes a trigger condition.
- `ki-pa-mu` = motion-place-artifact = vehicle / spacecraft. Head-final: `mu` (artifact)
  is head; `ki-pa` (motion-place, established as corridor/passage compound, S064) specifies
  a place-artifact defined by movement. A spacecraft is a moving-place-artifact. Ad hoc
  compound; candidate for registration.
- `pa-ki` = place-motion = spatial drifting / uncontrolled movement through space.
  `pa` (place/space particle/root) + `ki` (motion) = motion-through-space. As a compound
  predicate: "there is spatial motion [of the subject]" = drifts.
- **Conditional readings:** `go [X]  Y` can be read as (a) present-factual ("the engine
  is failing; it's drifting now"), (b) general conditional ("whenever the engine fails,
  it drifts"), or (c) future hypothetical ("if it fails, it will drift"). The `go` frame
  is *actuality-neutral* — it asserts the causal relationship without specifying whether
  the premise is actual. This is a deliberate feature: the language marks causal
  structure, not factuality of conditions.

---

**S124 — Future conditional with recurrence: "If the engine fails again, the ship will drift."** *(T-AX-011)*

```
Gloss:    go [lo-ra-ki-mu  re-de]  lo-ki-pa-mu  pa-ki
Literal:  cause:[patient:engine  cycle-decay]  patient:vehicle  place:motion
Natural:  Given a recurrent engine failure, the vehicle will drift.
```

**Notes:**
- `re-de` = repetition-decay = recurrent/repeated failure = "fails again." `re`
  (repetition/cycle) + `de` (decay/failure). First use of `re-de` as a predicate in a
  subordinate causal clause.
- **"Will" (future):** Tonesu has no dedicated future tense marker. The future reading
  arises from the conditional structure: a hypothetical causal premise (`go [...]`)
  with a result clause implies the result is prospective. The causal frame is
  inherently forward-directed when the premise is not currently actual.

---

**S125 — Past counterfactual: "If the engine had failed, the ship would have drifted."** *(T-AX-012)*

*Two attempts: one indicative past, one counterfactual.*

**Attempt A — Indicative past conditional (what the language CAN say):**

```
Gloss:    go [lo-ra-ki-mu  ti-de-de]  lo-ki-pa-mu  pa-ki  ti-de
Literal:  cause:[patient:engine  past-decay]  patient:vehicle  place:motion  time:past
Natural:  When/because the engine had failed, the vehicle drifted.
```

- `ti-de-de` = time-decay-decay = past failure / a decay event in past time. `ti-de`
  (past time, W041) combined with `de` (decay/failure) inside the cause clause.
- `pa-ki  ti-de` = spatial-motion  past-time = "drifted [at past time]."
- **Verdict A:** This is a *factual past conditional* — it asserts that the engine
  actually failed and the ship actually drifted. The causal relationship in past time
  is cleanly expressed.

**Attempt B — Counterfactual (what the language CANNOT cleanly say):**

The target is the *non-actual* reading: the engine did NOT fail, but IF it had,
the ship WOULD have drifted.

For this, the language would need to mark the premise as **non-actual** — a hypothetical
scenario rather than an asserted past event. No grammatical device for this exists.

*Closest available construction:*

```
la-mi  to  [go [lo-ra-ki-mu  ti-de-de]  lo-ki-pa-mu  pa-ki  ti-de]
agent:I  hold-conceptually  [causal-conditional chain in past time]
My conceptual model: [had the engine failed, the vehicle would have drifted.]
```

- Wrapping the causal chain in `la-mi  to  [...]` = "I hold as a conceptual model"
  marks the entire scenario as an epistemic *pattern* rather than a factual claim.
  The counterfactual force comes from the framing, not from any grammatical marker
  on the conditional itself.
- **Limitation:** the counterfactual reading requires an explicit stance-holder
  (`la-mi`). Bare counterfactuals — where no stance-holder is stated and the
  non-actuality of the premise is marked grammatically — are not expressible.

**Gap identified: CF-001 — Counterfactual non-actuality marker.**
Tonesu can express causal chains, past events, and hypothetical-framed scenarios.
It cannot grammatically mark the non-actuality of a conditional premise without
adding an epistemic stance-holder. This is not a *primitive* gap — all the conceptual
components are present. It is a *grammar* gap: no device exists to flag a subordinate
clause as a non-actual premise (the counterfactual mood in traditional grammar).

Design paths: (a) a new clause-level marker for non-actual premises (a small functional
particle); (b) accept that counterfactuals always require `la-X  to  [...]` framing with
an explicit stance-holder; (c) reserve the `to` bare-frame (`to [scenario]`) as a
hypothetical/non-actual scene-setter without a stance-holder. Path (c) is the least
invasive — `to [X]` would mean "in the conceptual scenario / hypothetically: [X]."
This would need corpus pressure and a second use case before formalizing. **Watch.**

---

**S114–S125 Summary: Four Axes**

| Axis | Test | Core construction | Gap? |
|------|------|------------------|------|
| Capability | `be-vo` | stative quality predicate | None — `be-vo` sufficient |
| Intention | `wi [clause]` | purpose frame | None — established |
| Causation | `go [X]  matrix` | causal frame | None — established |
| Identity | `to-ru` | pattern-unity | None — new compound |
| Similarity | `ne-to` | relation-pattern | None — new compound |
| Component | `pe  lo-su-ru` | part + unified-whole | None — `pe` in predicate |
| Possession | `la-X  ne  lo-Y` | relational predicate | None — `ne` extends cleanly |
| Containment | `la-X  ko  lo-Y` | containment predicate | None — established |
| Present conditional | `go [X]  Y` | causal/conditional frame | None — established |
| Counterfactual | requires `la-X  to  [...]` | epistemic wrap | **CF-001 watch** |

**Overall verdict:** The primitive set holds across all four axes. No new primitive is
needed from this battery. One grammar gap identified (CF-001: counterfactual non-actuality
marking). The capability watch item can be partially resolved: `be-vo` handles
dispositional capability cleanly in current corpus use cases.

**New compounds from this batch worth registering:**
- `to-ru` (pattern-unity = same model/type)
- `ne-to` (relation-pattern = similarity/analogy)
- `su-ru` (structure-unity = unified system/single system)
- `ra-ma` (energy-matter = fuel)
- `ki-pa-mu` (motion-place-artifact = vehicle/spacecraft)
- `pa-ki` (place-motion = spatial drift/uncontrolled movement)

---

## CF-001 Diagnostic: Counterfactual Mini-Batch (S126–S131)

**Purpose:** Three design paths were proposed for expressing past counterfactuals (S125,
CF-001). This batch runs each path against three domains — engineering, social, and
institutional — to determine which strategy is grammatically viable, cross-domain stable,
and consistent with Tonesu's existing architecture.

**Three paths under examination:**
- **Path A** — epistemic wrapper: `la-X  to  [go [NON-ACTUAL-PREMISE]  RESULT]`
- **Path B** — bare `to` as impersonal hypothetical frame: `to [go [X]  Y]`
- **Path C** — compound hypothetical-causal frame marker: `to-go [X]  Y`

**New compound introduced this batch:**
- `pa-wi` = place-will = destination (the intended/targeted place)

---

### Path A — Epistemic wrapper across three domains (S126–S128)

---

**S126 — Engineering: "If the engine hadn't failed, the ship would have reached its destination."** *(CF-001-A)*

```
Gloss:    la-mi  to  [go [lo-ra-ki-mu  no-de  ti-de]  la-ki-pa-mu  ki  lo-pa-wi  ti-de]
Literal:  agent:I  hold-model  [cause:[patient:engine  no-decay  past-time]
                                 agent:vehicle  moves  patient:destination  past-time]
Natural:  My conceptual model: given no engine failure, the ship would have reached its
          destination.
```

**Notes:**
- `pa-wi` = place-will = destination. Head-final: `wi` (will/intent) is head; `pa`
  (place) modifies it as an intentional place — the place one is heading toward. First
  use; compound candidate (W088).
- `la-ki-pa-mu  ki  lo-pa-wi` = the vehicle moves [toward] its destination. `lo-pa-wi`
  in the patient slot encodes the goal-state of movement: the motion event terminates at
  the destination. The goal-as-patient construction is not yet explicit in spec; it works
  by analogy with change-of-state constructions where the result of a process is in the
  patient slot.
- `no-de  ti-de` = no-decay at past-time = the decay event did not occur in the past.
  `no-de` as a compound predicate means "failure did not happen." The premise is
  non-actual: in reality the engine DID fail; the hypothetical premise inverts this.
- **Path A — what it achieves:** The counterfactual is comprehensible and complete.
  The `la-mi  to  [...]` framing marks the scenario as a conceptual model held by the
  speaker. The non-actuality of the premise is implied by the framing: if the premise
  were actual, no epistemic wrapper would be needed — a bare factual conditional would
  suffice.
- **Path A — what it costs:**
  1. *Mandatory first-person stance-holder (`la-mi`).* The speaker necessarily claims
     personal ownership of the counterfactual model. For a historian, investigator, or
     narrator writing about someone else's past, the natural form would instead require
     `la-to-fe-li  to  [...]` (the investigators hold...) or `la-[narrator]  to  [...]`
     — always an explicit attributor. This reflects Concordian epistemic culture: every
     claim is attributed. But it converts a non-actual conditional into an attributed
     assertion, which has a different illocutionary weight.
  2. *Epistemic weight mismatch.* `la-mi  to  [prop]` = "I hold [prop] at knowledge
     level" — this asserts claim-strength. Counterfactuals in most discourse contexts
     don't assert anything about the speaker's epistemic state; they assert a causal
     relationship while flagging the premise as non-actual. Path A imports `to`'s
     epistemic force inappropriately.
  3. *No structural separation of non-actuality and causal claim.* The non-actuality of
     the premise is implied only by inference from the epistemic wrapper — not marked
     on the conditional itself. A reader must infer: "why is this inside `to [...]`?
     Because the premise is non-actual." This is indirect.

---

**S127 — Social domain: "If she had received the signal, she would have warned the crew."** *(CF-001-B)*

```
Gloss:    la-mi  to  [go [lo-zo-li  se  lo-si  ti-de]  la-zo-li  ka  fe-si  lo-li-pu  ti-de]
Literal:  agent:I  hold-model  [cause:[patient:person  perceives  patient:signal  past]
                                 agent:person  performs  warning-signal  to:collective  past]
Natural:  My conceptual model: given the person having perceived the signal, she would have
          issued a warning to the crew.
```

**Notes:**
- `li-pu` = plural-person = crew/collective. `lo-li-pu` = patient:collective = directed
  to the crew. The `lo-` particle on the recipient argument of `ka  fe-si` marks the
  crew as both patient and target of the warning action.
- `fe-si` = W024, warning signal — the content of the transmitted signal.
- **Path A — social domain problem exposed:** The counterfactual here is not primarily
  about the speaker's epistemic model — it is an assertion about what would have happened
  in a third-party situation. But `la-mi  to  [...]` makes it a first-person epistemic
  claim: "I believe/model that..." A historian writing this investigation report is not
  inserting their personal model — they are reporting a counterfactual finding. The
  natural Concordian form would attribute this differently: to the investigation body,
  not the speaker. Path A structurally conflates reasoning-about-the-world with claiming-
  about-oneself. The language cannot write an anonymous counterfactual historical
  assertion — every counterfactual carries its thinker.
- **Cultural note:** This may not be a bug. Concordian epistemic culture insists that
  all claims have attributors. An "anonymous" counterfactual assertion — one that makes
  a claim about what would have happened with no stated epistemic owner — is potentially
  a species of decontextualized authority claim. The language may be deliberately
  forcing the question: *who* is asserting this counterfactual? But this implies that
  counterfactuals in Concordian discourse are always testimony, not neutral logic.

---

**S128 — Institutional domain: "If the doctrine had been published, the dispute would have been resolved."** *(CF-001-C)*

```
Gloss:    la-mi  to  [go [lo-to-re-su  to-fe-su-ki  ti-de]  lo-ne-fe  de  ti-de]
Literal:  agent:I  hold-model  [cause:[patient:doctrine  publication-event  past]
                                 patient:relational-tension  dissolves  past]
Natural:  My conceptual model: given [the doctrine having been published], the relational
          tension would have dissolved.
```

**Notes:**
- `to-re-su` = W064 (standing doctrine/policy). `to-fe-su-ki` = the inchoative
  publication event: the doctrine crosses the epistemic threshold to published `to-su`
  status. From semantic-map.md § Domain 6. Not yet in derived.md — compound candidate
  (add alongside `pa-wi` W088).
- `lo-ne-fe  de  ti-de` = patient:relational-tension dissolves at past-time = the
  dispute was resolved. `de` (decay) as predicate on the tension: the tension dissolved.
  Clean and compositionally transparent.
- **Path A — institutional domain: worst case.** The sentence now asserts "I, the
  speaker, hold as my conceptual model that the institutional causal chain would have
  produced this outcome." In formal institutional discourse — an arbitration ruling, a
  post-incident analysis, a legal brief — this personal framing (`la-mi`) is the wrong
  register entirely. The statement belongs to an investigation body, not a private mind.
  The institutional counterfactual assertion needs a third party as attributor, an
  institutional voice, not a personal first-person claim.
- **Path A verdict:** The epistemic wrapper strategy works the best in personal
  reasoning contexts (S126 — the speaker reflecting on a situation they witnessed).
  It degrades in social testimony contexts (S127 — historical claim about third
  parties) and is structurally misaligned with institutional discourse (S128 — an
  arbiter's counterfactual analysis). The problem is not that Path A is wrong; it is
  that it is too strong — it collapses "I hold this as a personal model" with "this
  is an assertion about what would have happened." These should be distinguishable.

---

### Path B — Bare `to` as hypothetical frame-setter (S129)

---

**S129 — Engineering: bare `to [scenario]` without a stance-holder** *(CF-001-D)*

```
Gloss:    to [go [lo-ra-ki-mu  de  ti-de]  lo-ki-pa-mu  pa-ki  ti-de]
Literal:  conceptual  [cause:[patient:engine  decays  past]  patient:ship  drifts  past]
Natural:  In the conceptual/hypothetical domain: if the engine had failed, the ship would
          have drifted.
```

**Notes:**
- **Grammar move attempted:** `to` in the frame-setter role — the entire bracketed
  scenario is marked as non-actual/conceptual. No stance-holder (`la-X`) is named.
  The `to [...]` construction claims: "this is a conceptual scenario, not an asserted
  fact." Parallel to how `go [X]` introduces a causal frame without naming the
  causal agent: `go` sets the frame, and the internal clause fills it. By analogy,
  `to [scenario]` would set a hypothetical frame without naming a thinker.
- **Grammatical question: is `to` licensed as an impersonal frame-setter?** All
  current corpus attestations of `to` require a `la-X` agent: `la-mi  to  [prop]` =
  "I hold [prop] as knowledge." The bare form `to [prop]` with no agent would require
  argument-drop — the "thinker" is left unspecified. Tonesu permits argument-drop
  in established contexts (speaker-drop `la-mi`, topic-drop, imperative-drop `la-tu`).
  This would be a new drop environment: *thinker-drop* in epistemic frame constructions.
- **Does `to [X  Y]` internally disambiguate from predicate `to`?** Yes, structurally.
  When `to` is a predicate, it takes a proposition as argument: `la-X  to  [prop]`.
  Bare `to [full-scenario-with-internal-clause-structure]` is distinguishable from a
  predicate use because (a) there is no `la-X` opening agent, and (b) the bracketed
  argument contains a full causal chain (`go [clause]  result`) — not a noun or simple
  state. A parser would read bare `to [go [...] ...]` as a frame-setter, not as a
  headless predicate. The structure is available.
- **Path B verdict:** Grammatically accessible through argument-drop, but requires
  formalizing a new drop environment (thinker-drop from epistemic frame). The resulting
  construction reads well but has a subtle problem: `to [X]` with no thinker still
  *implies* a thinker (the discourse-domain speaker). It suppresses the thinker without
  eliminating the epistemic weight. The non-actuality of the premise comes from
  inference ("this is in the conceptual domain, therefore it isn't being asserted as
  factual") rather than from explicit marking. This is weaker than desired — it marks
  the *register* as hypothetical but not the *premise* as non-actual. Useful as a
  register device; insufficient as a grammatical counterfactual marker.

---

### Path C — Compound hypothetical-causal frame marker `to-go` (S130–S131)

---

**S130 — Engineering: `to-go [X]  Y` compound frame marker** *(CF-001-E)*

```
Gloss:    to-go [lo-ra-ki-mu  de  ti-de]  lo-ki-pa-mu  pa-ki  ti-de
Literal:  hypothetical-causal  [engine  decays  past]  ship  drifts  past
Natural:  Counterfactually: if the engine had failed, the ship would have drifted.
```

**Notes:**
- `to-go` = conceptual-causal = hypothetical-causal frame marker. Head-final: `go`
  (cause/origin) is the head — this IS a causal/conditional frame; `to` (conceptual
  pattern) modifies it as hypothetical/non-actual. The compound marks the entire
  conditional structure as non-actual: premise is non-actual, result is non-actual,
  the causal link between them is being asserted.
- **The structural operation:** `to-go [X]  Y` is to `go [X]  Y` as a compound
  hypothetical-frame is to an actuality-neutral conditional. The `to-` prefix lifts
  the causal frame out of actuality-assertion and into conceptual/hypothetical space.
  `go [X]  Y` can be read as present, future, or general conditional (actuality-neutral
  but not explicitly non-actual). `to-go [X]  Y` explicitly asserts non-actuality:
  "the causal chain [X → Y] is held in the conceptual domain, not the actual one."
- **Advantages:**
  - *No stance-holder required.* The counterfactual is not attributed to any speaker;
    it is an assertion about a causal relationship in non-actual space. The thinker is
    absent in the same way the causal agent is absent from `go [X]  Y`: the frame sets
    the relation, not the attributor.
  - *Compositionally grounded.* `to-go` uses only existing roots with their established
    meanings. A reader who knows `to` (conceptual/pattern) and `go` (cause/conditional
    frame) can parse `to-go` without a glossary entry.
  - *Extends the existing frame paradigm cleanly.* The frame inventory already includes
    `go`, `du`, `wi` as clause-level frame markers. `to-go` is one new compound in the
    same paradigm, not a new category.
  - *Marks non-actuality on the frame, not on the premise.* The non-actuality is a
    property of the conditional structure itself, not of a time-expression or negation
    inside the premise. This is the right level: a counterfactual is non-actual as a
    whole, not just non-actual in the premise.
- **Disadvantages:**
  - *Introduces a new compound frame marker into the grammar.* This must be explicitly
    registered. It is not a derived word in the usual sense — it functions like `go` as
    a structural particle, not like `ra-ki-mu` (a lexical compound). Its status
    (grammar rule vs. derived form) needs definition.
  - *Does not distinguish counterfactual from future hypothetical.* Both "if the engine
    were to fail, the ship would drift" (future hypothetical) and "if the engine had
    failed, the ship would have drifted" (past counterfactual) would use `to-go [X]  Y`.
    The distinction between them would come from the internal time-marking (`ti-de` vs.
    no time-marker) in the premise and result clauses, not from the frame marker itself.
    This is arguably correct: the `to-go` frame marks non-actuality, and time-marking
    adds the past/future dimension independently. The two-axis system (non-actuality via
    `to-go`; time via `ti` compounds) is cleaner than a single frame that encodes both.

---

**S131 — Institutional domain: `to-go [X]  Y` generalization test** *(CF-001-F)*

"If the doctrine had been published, the dispute would have been resolved."

```
Gloss:    to-go [lo-to-re-su  to-fe-su-ki  ti-de]  lo-ne-fe  de  ti-de
Literal:  hypothetical-causal  [patient:doctrine  publication-event  past]
                                patient:relational-tension  dissolves  past
Natural:  Counterfactually, given that the doctrine had been published, the relational
          tension would have dissolved.
```

**Notes:**
- The `to-go` frame removes all reference to any speaker's epistemic state. The
  sentence makes a bare counterfactual assertion about institutional causation: if
  doctrine-publication had occurred, the dispute would have dissolved. This is the
  register appropriate for an arbitration brief, a post-incident analysis, or a
  narrative history — the exact contexts where Path A (S128) degraded.
- **Contrast with S128 directly:**
  - S128 (Path A): `la-mi  to  [go [...]]` = "I, the speaker, hold as my model that..."
  - S131 (Path C): `to-go [...]` = "In the counterfactual domain: [causal chain]"
  - S131 asserts the causal relationship in the counterfactual domain without any agent
    of assertion. It is structurally analogous to how English "If X had happened, Y
    would have followed" can be written in an investigation report without "I believe."
- **Generalization confirmed:** `to-go [X]  Y` works identically in engineering
  (S130), social (apply mentally — `to-go [lo-zo-li  se  lo-si  ti-de]  la-zo-li
  ka  fe-si  lo-li-pu  ti-de` works), and institutional (S131) domains. No
  domain-specific friction.

---

### CF-001 Verdict

**`to-go [X]  Y` is the canonical counterfactual frame. Recommended for adoption.**

| Path | Mechanism | Problems | Verdict |
|------|-----------|----------|---------|
| A (`la-X  to  [go [...]]`) | epistemic wrapper | mandatory stance-holder; wrong illocutionary weight; conflates personal model with bare counterfactual | Valid for personal reasoning; insufficient as a general counterfactual |
| B (bare `to [go [...]]`) | impersonal register-shift | marks hypothetical register, not non-actuality; new argument-drop environment needed | Available but indirect; not a counterfactual marker |
| C (`to-go [X]  Y`) | compound hypothetical-causal frame | must add to frame-marker paradigm | **Adopted.** Compositional, attributor-free, domain-general |

**Path A survives as a complementary construction:** `la-X  to  [to-go [X]  Y]` = "I
(or institution X) hold that: counterfactually, if [X], [Y]." When the epistemic
attribution matters — an arbiter ruling, a personal assessment on the record — Path A
wraps Path C. Both are now valid, with distinct illocutionary force:

| Construction | Force |
|-------------|-------|
| `to-go [X]  Y` | bare counterfactual conditional |
| `la-X  to  [to-go [X]  Y]` | attributed counterfactual (person/body X asserts the counterfactual) |

**Grammar status of `to-go`:** unlike `ra-ki-mu` (lexical compound), `to-go` is a
**frame-marker compound** — it functions structurally like `go` and `du`, not like a
content word. To the grammar spec (§ Causal Frame), `to-go` is a compound extension
of `go` that marks non-actuality. It should be registered in both derived.md (as a
compound entry for lookup) and spec/grammar.md (as a frame-marker rule).

**Future/present hypothetical vs. past counterfactual:** both use `to-go [X]  Y`. The
distinction is carried by internal time-marking:
- `to-go [lo-X  de]  lo-Y  de-ki` = future hypothetical ("if X were to fail, Y would decay into drift")
- `to-go [lo-X  de  ti-de]  lo-Y  pa-ki  ti-de` = past counterfactual ("if X had failed, Y would have drifted")
`to-go` marks the non-actuality axis; `ti-de` marks the temporal axis. Two-axis separation is clean.

**CF-001 status:** COMPLETE. Grammar spec written: spec/grammar.md § Counterfactual Frame.
W089 `to-go` registered in derived.md. Social domain Path C attested S155; attributed
form attested S156. Future hypothetical (minimal contrast with S130) attested S157.
`to-fe-su-ki` registered as W097 (first attested S128/S131).

---

## fa-VAL Diagnostic: Affective Substrate Batch (S132–S134)

**Purpose:** First corpus attestations of `fa` (affective substrate, primitive 33),
`ne-de` (relation-decay), and `ka-ne-de` (intentional relation-dissolution). Validates
the se/fa distinction across formal, casual, and analytical registers using a breakup
scenario developed in design session March 2026.

**Core oppositions under examination:**
- `ne-mi  de` (agentless dissolution) vs `la-ze  ka-ne-de  lo-ne-mi` (agentive)
- `fa-be` without object (substrate register) vs `se  vo-de  lo-ne-mi` (detection register)
- `fa-no-to` (unresolved substrate affect) as a complete discourse move

**New compounds introduced this batch:**
- `ne-de` = relation + decay = relational dissolution (W091)
- `ka-ne-de` = intentional-action + relation-decay = volitional dissolution (W092)

---

**S132 — Formal register: intentional dissolution + affect-rise + se-detection** *(fa-VAL-A)*

"They ended my relationship. Affect rising; I perceive value-loss."

```
Gloss:    la-ze  ka-ne-de  lo-ne-mi; la-mi  fa-be  se  vo-de  lo-ne-mi
Literal:  agent:they  intentional-relation-decay  patient:my-relation;
          agent:I  affect-rises  perceive  value-decay  patient:my-relation
Natural:  They intentionally ended my relationship. Affect is rising in me;
          I perceive value-decay when I look at it.
```

**Notes:**
- First attestation of `ka-ne-de` (W092): volitional reading; `ka` (intentional action) +
  `ne-de` (relation-decay). The `ka` distinguishes this from bare `ne-mi  de` (S133),
  where dissolution happens without an assigned will.
- `fa-be` (affect-rises) in emotional context: first corpus use in a relational-loss
  frame. No named emotion. Raw substrate signal.
- `se  vo-de  lo-ne-mi` — the se-register form: outward-facing detection needs an object
  (`lo-ne-mi`). Speaker detects quality-decay in the relationship as external object.
  This is the `se` column of Domain 7: detection directed at the relation.
- Clause structure: the first half names the agent and their act; the second half names no
  reason — both clauses are grammatically complete. Formal register licenses both.

---

**S133 — Casual compressed: dual-register demonstration** *(fa-VAL-B)*

"My relationship ended. [Affect rising.]"

```
Gloss:    ne-mi  de; fa-be
Literal:  my-relation  decays; affect-rises
Natural:  My relationship ended. [I feel the affect rising.]
```

**Notes:**
- First direct attestation of `ne-de` (W091) via `ne-mi  de`: `ne` (relation root) + `mi`
  (speaker reference) as head NP; `de` (decay) as predicate. No agent named. The
  dissolving is not attributed to any will — it simply occurred.
- Contrast pair with S132: S132 names the agent (`la-ze  ka-ne-de`); S133 omits agent
  and strips `ka` (intentionality). Same external event; different what-is-predicated.
- `fa-be` stands alone as an utterance complete without object or `lo-` patient. This is
  the `fa` substrate column: affect active without an external target to `se` onto.
- Most directly demonstrates P9 corollary: unresolved affect is not a failed diagnostic.
  `fa-be` with no object is grammatically and pragmatically complete.

---

**S134 — Analytical observer: `fa-no-to  lo-go` construction** *(fa-VAL-C)*

"My relationship ended. My affect has no model of the cause."

```
Gloss:    ne-mi  de.  la-mi  fa-no-to  lo-go.
Literal:  my-relation  decays.  agent:I  affect-no-model  patient:cause.
Natural:  My relationship ended. My affect has not resolved into a model of the cause.
```

**Notes:**
- First corpus use of `fa-no-to` (fa-based unresolved affect). Parallels W090 `se-no-to`
  but uses the affective substrate root: substrate-affect-without-model. Where `se-no-to`
  describes perceptual signal without resolution, `fa-no-to` describes the same stall at
  the substrate level itself.
- `lo-go` = patient: cause/origin. The construction `fa-no-to  lo-go` is precise:
  "affect has not resolved into knowledge of [the cause]." Most accurate Tonesu form for
  "I got dumped and I don't understand why." Speaker names the absence of model and
  specifies exactly where the gap lies: at causal explanation.
- Three-sentence progression (S132 → S133 → S134): formal indictment → compressed
  felt-experience → observer-mode registration of confusion as state.
- `la-mi` in S134 is the observer's anchor. Speaker is modeling their own substrate:
  "I-as-observer: affect-no-model." Not confusion stated from inside confusion — the
  registering of confusion as a named state. Analogous to Domain 7 observer mode:
  `la-mi  to  [la-zo-mi  se  lo-X]`.

---

### fa-VAL Verdict

**`fa` primitive validates across all three registers without grammar extension.**

| Code | Register | Key construction | New compounds |
|------|----------|------------------|---------------|
| fa-VAL-A | Formal | `la-ze  ka-ne-de  lo-ne-mi; la-mi  fa-be  se  vo-de  lo-ne-mi` | W092 first attestation |
| fa-VAL-B | Casual | `ne-mi  de; fa-be` | W091 first attestation |
| fa-VAL-C | Analytical | `ne-mi  de.  la-mi  fa-no-to  lo-go.` | `fa-no-to` first corpus use |

**Finding:** `fa` requires no new grammar rules. The se/fa complementarity holds under
pressure: `fa-be` without object is complete; `se  vo-de  lo-ne-mi` needs the object;
both are available to the same speaker in adjacent clauses (S132). The three-stage
pipeline (`se → fa → to`) can stall at `fa-no-to  lo-go` and remain a well-formed
discourse move (S134). The agentive/agentless contrast (`ka-ne-de` vs bare `ne-mi  de`)
falls out of existing grammar without new machinery (S132 vs S133).

---

## CF-001 Completion: Social Domain Path C + Future Hypothetical (S155–S157)

**Purpose:** Close three remaining gaps from the CF-001 diagnostic:
1. The social-domain Path C sentence was only sketched ("apply mentally") in the CF-001
   verdict — never committed as a proper corpus entry.
2. The attributed counterfactual form (`la-X  to  [to-go [X]  Y]`) was described and
   specified in the verdict but has no corpus attestation.
3. The future hypothetical (`to-go` without `ti-de`) was illustrated in the spec but
   never in corpus — meaning the two-axis independence claim rests solely on examples
   in the grammar spec, not corpus sentences.

All three gaps resolved here. No new grammar or compounds introduced.

---

**S155 — Social domain Path C: bare counterfactual** *(CF-001-G)*

"If she had received the signal, she would have warned the crew."

```
Gloss:    to-go [la-zo-li  se  lo-si  ti-de]  la-zo-li  ka  fe-si  lo-li-pu  ti-de
Literal:  hypothetical-causal  [agent:person  detects  patient:signal  past]
                                 agent:person  performs  warning-signal  to:crew  past
Natural:  Counterfactually: given that the person had received the signal, she would
          have issued the warning to the crew.
```

**Notes:**
- The social-domain Path C sentence sketched in the CF-001 verdict (`to-go [lo-zo-li
  se  lo-si  ti-de]  la-zo-li  ka  fe-si  lo-li-pu  ti-de`) is committed here with one
  correction: premise uses `la-zo-li` (perspective-anchor agent) not `lo-zo-li`
  (patient-marker), consistent with all other `se`-perception clauses in corpus.
- Direct comparison with S127 (Path A version of same event):
  - S127: `la-mi  to  [go [lo-zo-li  se  lo-si  ti-de]  la-zo-li  ka  fe-si  lo-li-pu  ti-de]`
  - S155: `to-go [la-zo-li  se  lo-si  ti-de]  la-zo-li  ka  fe-si  lo-li-pu  ti-de`
  The result clause is identical. The only structural difference is the removal of
  `la-mi  to  [go [...]]` and the substitution of `to-go` as the outer frame. S155
  requires no speaker; S127 requires `la-mi` as the mandatory attributor.
- Cross-domain generalization complete: S130 (engineering), S131 (institutional),
  S155 (social). `to-go [X]  Y` works domain-independently, as the CF-001 verdict
  asserted.
- `li-pu` = crew/collective. `lo-li-pu` = to:the-crew (recipient marked as patient).
  `fe-si` = W024 (warning signal). `zo-li` = organism-person (gender-neutral third party).

---

**S156 — Social domain: attributed counterfactual** *(CF-001-H)*

"The investigation body holds: counterfactually, if she had received the signal, she
would have warned the crew."

```
Gloss:    la-to-fe-su  to  [to-go [la-zo-li  se  lo-si  ti-de]
                             la-zo-li  ka  fe-si  lo-li-pu  ti-de]
Literal:  agent:epistemic-standards-body  holds-model
          [hypothetical-causal  [agent:person  detects  signal  past]
                                  agent:person  performs  warning  to:crew  past]
Natural:  The investigation body asserts as its model: had the person received the
          signal, she would have issued the warning to the crew.
```

**Notes:**
- First corpus attestation of the attributed counterfactual form:
  `la-X  to  [to-go [premise]  result]`. The embedded proposition is S155; the outer
  clause assigns epistemic ownership to `to-fe-su` (the epistemic standards/investigation
  body, W072) rather than the speaker (`la-mi`).
- This resolves the S127 illocutionary-weight problem directly. The CF-001 verdict
  diagnosed S127's defect: in a post-incident investigation report, the counterfactual
  claim belongs to the *inquiry body*, not to a private speaker's personal model. S156
  uses `la-to-fe-su  to  [...]` — the investigation body owns the claim.
- Force distinction, now corpus-attested:
  | Construction | Force |
  |---|---|
  | `to-go [X]  Y` (S155) | bare counterfactual — no thinker asserted |
  | `la-mi  to  [to-go [X]  Y]` (S127 Path A variant) | speaker's personal counterfactual model |
  | `la-to-fe-su  to  [to-go [X]  Y]` (S156) | institutional counterfactual assertion |
- Path A (`la-X  to  [...]`) continues to function, but the wrapper is now wrapping
  `to-go [...]` rather than `go [...]`. The attributed form is Path A wrapping Path C —
  exactly as the CF-001 verdict specified.

---

**S157 — Future hypothetical: minimal contrast with S130** *(CF-001-I)*

"If the engine were to fail, the ship would drift."

```
Gloss:    to-go [lo-ra-ki-mu  de]  lo-ki-pa-mu  pa-ki
Literal:  hypothetical-causal  [patient:engine  decays]  patient:ship  drifts
Natural:  Were the engine to fail, the ship would drift. — Future hypothetical.
```

**Notes:**
- Minimal contrast pair with S130 (past counterfactual):
  - S130: `to-go [lo-ra-ki-mu  de  ti-de]  lo-ki-pa-mu  pa-ki  ti-de` — past; `ti-de` in
    both premise and result
  - S157: `to-go [lo-ra-ki-mu  de]  lo-ki-pa-mu  pa-ki` — future hypothetical; no `ti-de`
  The frame marker `to-go` is identical. The only difference is time-marking inside the
  clauses. The actuality-axis (`to-go`) and the temporal-axis (`ti-de`) are independent.
- This provides the corpus evidence for the two-axis design claim that previously only
  had spec-level illustration. `to-go` is now attested for both the past-counterfactual
  and future-hypothetical readings.
- The untensed/unmarked form is prospective (future-open) by default: `lo-ra-ki-mu  de`
  = engine decays [in the hypothetical scenario, prospectively], with no time-location
  asserted.
- S157 is also the minimal engineering-domain future hypothetical — appropriate for
  safety analysis: "if X were to fail under future operating conditions, Y would follow."

---

### CF-001 Final Status

**All CF-001 corpus work complete.**

| Code | Sentence | Construction | Status |
|------|----------|-------------|--------|
| CF-001-A | S126 | Path A, engineering | ✓ |
| CF-001-B | S127 | Path A, social (problem case) | ✓ |
| CF-001-C | S128 | Path A, institutional (worst case) | ✓ |
| CF-001-D | S129 | Path B, bare `to` (rejected) | ✓ |
| CF-001-E | S130 | Path C, engineering — past counterfactual | ✓ |
| CF-001-F | S131 | Path C, institutional — past counterfactual | ✓ |
| CF-001-G | S155 | Path C, social — past counterfactual | ✓ |
| CF-001-H | S156 | Path A wrapping Path C — attributed counterfactual | ✓ |
| CF-001-I | S157 | Path C, future hypothetical | ✓ |

**Open follow-on:** MG-001 (model-domain frame — multi-sentence counterfactual scope).
See notes/open-questions.md § MG-001.

---

## fa-CON: `fa` Confirmation Batch (S135–S154)

**Purpose:** Systematic confirmation of `fa` across all documented use cases. Where
fa-VAL (S132–S134) used a single scenario to test three registers, fa-CON covers the
full width of the Domain 7 table plus boundary conditions, new compound attestations,
and explicit contrast tests. No new grammar is being proposed — this batch either
confirms existing constructions or flags unexpected friction.

**Coverage plan:**

| Group | Sentences | Tests |
|-------|-----------|-------|
| fa-CON-A | S135–S138 | Substrate column: all four base affect-quality combinations |
| fa-CON-B | S139–S141 | Three-stage pipeline: full, stalled, and skipped (propositional) |
| fa-CON-C | S142–S145 | First corpus attestations: `fa-ki`, `fa-re`, `fa-no`, `fa-de` |
| fa-CON-D | S146–S147 | Observer mode: self and other |
| fa-CON-E | S148–S149 | `se`/`fa` independence and explicit contrast |
| fa-CON-F | S150–S154 | Boundary tests: bodily vs affective; usage guard; clinical register; `se-no-to` vs `fa-no-to` |

---

### fa-CON-A: Substrate Column Survey (S135–S138)

**Goal:** First corpus attestations of the four base `fa`-column constructions from
Domain 7. Each: no object, no external trigger named. Substrate substrate is the full
report.

---

**S135 — Free-floating anxiety** *(fa-CON-A1)*

"Affect is in boundary-approach."

```
Gloss:    la-mi  fa  fe-ki
Literal:  agent:I  substrate  risk-becoming
Natural:  My affective substrate is in a state of approaching-threshold. Free-floating
          anxiety — no object, no identifiable source.
```

**Notes:**
- `fa  fe-ki` = substrate in boundary-approach state. `fe` (risk/boundary) + `ki`
  (motion/becoming) = approaching-threshold. The `fa` root situates this inwardly:
  not "I detect an approaching threat" (`se  fe-ki  lo-[X]`) but "substrate itself is
  in an approach-threshold activation." No named threat. No `lo-` patient.
- Domain 7 canonical form for free-floating anxiety. First corpus attestation.
- Contrast: `la-mi  se  fe-ki  lo-[X]` requires a named threat object; this does not.

---

**S136 — Undirected substrate positive affect** *(fa-CON-A2)*

"Substrate is in positive-rise."

```
Gloss:    la-mi  fa  vo-be
Literal:  agent:I  substrate  value-increasing
Natural:  My affective substrate registers a positive-quality rise. No particular object
          caused it — the substrate is simply in positive activation.
```

**Notes:**
- `fa  vo-be` = substrate registering value-increase. `vo` (value/quality) + `be`
  (generation/increase) = quality-rising. No external target.
- Contrast with `la-mi  se  vo-be  lo-[X]` (I detect value-rise at a specific object —
  directed appreciation). This form requires no direction. Waking up in a good mood;
  positive chemistry without identifiable cause.
- Shows `fa` is pre-evaluative and pre-relational: the substrate state exists before
  the speaker assigns it to anything.

---

**S137 — Persistent low / recurring value-decay** *(fa-CON-A3)*

"Affect registers value-decay. Recurring."

```
Gloss:    la-mi  fa  vo-de  re
Literal:  agent:I  substrate  value-decay  recurring
Natural:  My affective substrate keeps registering value-decay. The pattern returns.
```

**Notes:**
- `fa  vo-de  re` = substrate + value-decay + repetition. `vo-de` (value-decay) +
  `re` (repetition/cycle) = the low recurs as a pattern.
- First corpus attestation of `re` in combination with affective substrate. `re` here
  is not a single-event modifier — it marks the whole state as a pattern that resists
  resolution. The substrate keeps returning to value-decay even after apparent recovery.
- Closest Tonesu single-clause form to sustained depression or persistent low mood.
  The `re` is load-bearing: without it, `la-mi  fa  vo-de` describes a moment of low
  affect; with it, the cycling of that low is itself the named state.
- Distinct from `fa-re` (S143): `fa  vo-de  re` specifies the *content* of the cycle
  (value-decay); `fa-re` names the cycling itself without specifying content.

---

**S138 — Substrate threat-response / free-floating fear** *(fa-CON-A4)*

"Substrate boundary is degrading."

```
Gloss:    la-mi  fa  fe-de
Literal:  agent:I  substrate  risk-decay
Natural:  My affective substrate registers boundary-degradation. Free-floating
          threat-response — no identifiable threat.
```

**Notes:**
- `fa  fe-de` = substrate registering risk-decay. `fe` (risk/boundary) + `de`
  (decay/decrease) = the safety-boundary is eroding as an internal felt state.
  This is structural fear: the affective substrate's sense of protective boundary
  is diminishing, independent of whether any external threat is detected.
- Distinct from `fa  fe-ki` (S135, anxiety = approaching a threshold) vs
  `fa  fe-de` (fear = threshold degrading / already being crossed). The direction
  of `fe` movement differs: toward (`ki`) vs. eroding (`de`).
- Domain 7 canonical form for substrate fear. First corpus attestation.

---

### fa-CON-B: Three-Stage Pipeline (S139–S141)

**Goal:** Commit the `se → fa → to` pipeline to corpus in all three modes: full
resolution, mid-pipeline stall, and propositional skip (no `fa` activated).

---

**S139 — Full pipeline: perception → affect → model** *(fa-CON-B1)*

"I heard a sound. Affect rose. I identified the cause."

```
Gloss:    la-mi  se  so.  la-mi  fa-be.  la-mi  to  lo-go.
Literal:  agent:I  perceive  sound.  agent:I  affect-rises.
          agent:I  form-model  patient:cause.
Natural:  I detected an acoustic signal. My affective substrate rose. I identified
          the source. — All three pipeline stages resolved in sequence.
```

**Notes:**
- The thunder example from primitives.md § Affective Substrate, now committed to
  corpus. Three distinct complete clauses, each a valid standalone utterance, together
  forming the canonical `se → fa → to` three-stage sequence.
- Each stage is separable: `la-mi  se  so` (perception complete); `la-mi  fa-be`
  (substrate activated — independently valid, no object needed); `la-mi  to  lo-go`
  (model formed — cause identified). No stage requires the others; the sequence is
  temporal and causal, not grammatically obligatory.
- Establishes the canonical full-resolution form for corpus reference.

---

**S140 — Pipeline stall: perception → affect → no model** *(fa-CON-B2)*

"I heard a sound. Affect rose. No model of the cause formed."

```
Gloss:    la-mi  se  so.  la-mi  fa-be.  la-mi  fa-no-to  lo-go.
Literal:  agent:I  perceive  sound.  agent:I  affect-rises.
          agent:I  affect-no-model  patient:cause.
Natural:  I detected an acoustic signal. My affect rose. The substrate did not resolve
          into a model of the cause.
```

**Notes:**
- Minimal contrast with S139: identical first two clauses; third clause diverges:
  `la-mi  to  lo-go` (model formed) vs `la-mi  fa-no-to  lo-go` (no model formed).
  This is the pipeline stall at the `fa → to` transition.
- `fa-no-to` here is the fa-based form of unresolved affect: the substrate activated,
  but no cognitive model emerged. Distinct from `se-no-to` (W090), where the stall is
  upstream: the perceptual signal itself didn't resolve. Here, `se` succeeded (sound
  detected); the stall is at `fa → to`.
- `lo-go` = patient: cause/origin. The construction `fa-no-to  lo-go` names exactly
  where the model is absent: at causal explanation. More specific than bare `fa-no-to`.
- This sentence pair (S139 + S140) is the minimal pipeline contrast pair.

---

**S141 — Pipeline skip: propositional event, no fa activated** *(fa-CON-B3)*

"I received the information. I integrated it into my model."

```
Gloss:    la-mi  se  lo-si.  la-mi  to  lo-si.
Literal:  agent:I  perceive  patient:encoded-structure.
          agent:I  form-model  patient:encoded-structure.
Natural:  I received the data. I hold a model of it. — No affective substrate
          activation between perception and cognition.
```

**Notes:**
- `lo-si` = patient-marked encoded structure / information. `se  lo-si` = perceiving
  information (a purely propositional event — incoming data, not a threat or reward
  signal). `to  lo-si` = forming a model of that information.
- Key: the `fa` layer is absent. `se → to` directly, bypassing affect. This confirms
  that `fa` is NOT obligatory for all perception-to-model sequences — it activates for
  organism-relevant signals (threat, loss, reward) but not for neutral data intake.
- Without this sentence, the pipeline looks like a mandatory three-stage sequence.
  S141 establishes that `fa` is a conditional layer: engaged when the signal is
  organism-relevant, dormant for purely informational events.
- Contrast with S139: same `la-mi  se  [X]` opening; different subsequent activation.

---

### fa-CON-C: New Compound First Attestations (S142–S145)

**Goal:** First corpus uses of `fa-ki`, `fa-re`, `fa-no`, and `fa-de` — all compounds
documented in the Domain 7 `fa` compound table but never previously in corpus.

---

**S142 — `fa-ki`: affect shift / change of character** *(fa-CON-C1)*

"My affect shifted. Not rising; not falling — the register changed."

```
Gloss:    la-mi  fa-ki.  no  fa-be;  no  fa-de.
Literal:  agent:I  affect-shifts.  not  affect-rising;  not  affect-falling.
Natural:  My affective substrate shifted character. The state didn't escalate or
          diminish — something in its quality changed register.
```

**Notes:**
- First corpus attestation of `fa-ki` (W-pending). `fa` (substrate) + `ki`
  (motion/change/becoming) = substrate in motion / affect changing character.
  Distinct from `fa-be` (level rising) and `fa-de` (level falling): `fa-ki` is
  qualitative change, not quantitative. The affect shifted *kind*, not *amount*.
- The second clause `no  fa-be;  no  fa-de` is the diagnostic contrast: what happened
  is not covered by either of the level-change compounds, isolating `fa-ki` as the
  correct description. This sentence pair form (state + exclusion clause) is useful
  for introducing a compound that occupies a gap.
- Experiential correlate: the shift from diffuse anxiety to focused dread; from
  grief to numbness; from neutral to unsettled without becoming distressed.

---

**S143 — `fa-re`: recurring affect / cyclical substrate state** *(fa-CON-C2)*

"The affect pattern is recurring. I have encountered this state before."

```
Gloss:    la-mi  fa-re.  la-mi  to-ko  lo-su.
Literal:  agent:I  affect-recurring.
          agent:I  hold-memory  patient:structure.
Natural:  My affective substrate is cycling through a recurring pattern. I recognize
          this — the structure of this state has been stored.
```

**Notes:**
- First corpus attestation of `fa-re` (W-pending). `fa` (substrate) + `re`
  (repetition/cycle) = affective pattern cycling. The substrate state as a whole is
  recurring — not merely that an emotion is felt again, but that the *patterned
  substrate state* is returning.
- `to-ko  lo-su` = holds memory of the structure = recognizes the pattern (W027 +
  `lo-su` as patient: structure). "I have been in this patterned state before; it is
  stored." The second clause makes the `re` diagnosis explicit: not just "affect is up
  again" but "I recognize this specific cycle."
- Distinct from `fa  vo-de  re` (S137): S137 specifies *what* is cycling (value-decay);
  `fa-re` names the cycling of the whole substrate pattern without specifying content.
  `fa-re` is the meta-observation; `fa  vo-de  re` is the object-level description.
- Cultural note: `re` as a primitive (repetition) means Concordian speakers are
  structurally equipped to identify cyclical patterns as first-class facts. `fa-re` is
  the application of that primitive to affective experience — pattern recognition turned
  inward.

---

**S144 — `fa-no`: affective numbness / substrate absent** *(fa-CON-C3)*

"I perceive value-decay in my relationship. The substrate is absent."

```
Gloss:    la-mi  se  vo-de  lo-ne-mi.  la-mi  fa-no.
Literal:  agent:I  perceive  value-decay  patient:my-relation.
          agent:I  affect-absent.
Natural:  I detect value-decay when I look at the relationship. And yet the affective
          substrate is not active. The flat state.
```

**Notes:**
- First corpus attestation of `fa-no` (W-pending). `fa` (substrate) + `no`
  (negation/absence) = substrate inactive / affective flatness.
- The pairing with `se  vo-de  lo-ne-mi` is crucial: the `se` detection is functioning
  (the speaker can *detect* that the relationship is deteriorating), but the `fa`
  substrate is not responding. External perception working; internal affect absent.
- This is the precise SSRI-flatness or depression-related anhedonia construction:
  the cognitive/perceptual apparatus works; the affect layer does not activate. English
  can only gesture at this: "I know I should feel sad but I don't." Tonesu expresses
  it as two clean clauses with a structural contrast.
- Distinct from `se-no` (no external signal) and `fa-no-to` (substrate active but
  unresolved). `fa-no` = the substrate is not active at all.

---

**S145 — `fa-de`: affect fading / substrate diminishing** *(fa-CON-C4)*

"Affect was rising. It is now fading."

```
Gloss:    la-mi  fa-be  ta-ti-de.  la-mi  fa-de.
Literal:  agent:I  affect-rising  at-past-time.  agent:I  affect-fading.
Natural:  My affective substrate was in a rising state [earlier]. It is now diminishing.
          The wave is falling.
```

**Notes:**
- First corpus attestation of `fa-de` (W-pending). `fa` (substrate) + `de`
  (decay/decrease) = affect-level diminishing/fading.
- `ta-ti-de` = at past time (`ta` = time marker; `ti-de` = time-decay = past). Temporal
  anchor for the prior state, establishing the contrast with the current `fa-de`.
- Together with `fa-be` (S133 first attestation) and `fa-ki` (S142), this completes
  the level-and-character compound set: `fa-be` (up), `fa-de` (down), `fa-ki` (shift).
- Not "the emotion ended" — `fa-de` describes the active process of the substrate
  diminishing. The affect is still partially present; what is named is its trajectory.

---

### fa-CON-D: Observer Mode (S146–S147)

**Goal:** Confirm `la-mi  to  [la-zo-mi  fa  X]` (self-observer) and
`la-mi  to  [la-zo-ze  fa  X]` (other-observer) as grammatically stable across
both `la-mi` / `la-ze` and across different affect-quality combinations.

---

**S146 — Self-observer: analytically modeling own affective state** *(fa-CON-D1)*

"I model: my organism's affective substrate is in boundary-approach."

```
Gloss:    la-mi  to  [la-zo-mi  fa  fe-ki]
Literal:  agent:I  form-model  [agent:my-organism  substrate  risk-becoming]
Natural:  I analytically model that my organism's affective substrate is in a
          boundary-approach state. — I am observing my own anxiety, not inhabiting it.
```

**Notes:**
- First corpus attestation of the self-observer mode with `fa`. The matrix clause
  `la-mi  to [...]` situates the speaker as a modeling agent; the embedded clause
  `la-zo-mi  fa  fe-ki` assigns the affective state to the organism (`zo-mi`), not
  the agent (`mi`). The feeling is *in the body*; the speaker is *watching* it.
- Structural contrast with S135 (`la-mi  fa  fe-ki`): same affective content; different
  perspective. S135 = speaker inhabits the anxiety (agent is also its site); S146 =
  speaker observes the anxiety in their organism (agent and organism separated by `li`/`zo`).
- This maps onto clinical dissociation, mindfulness-observer stance, SSRI emotional
  distance: the affect is real and registered, but the experiential stance is analytical.
  The language makes the stance explicit rather than leaving it implicit.
- The embedded `la-zo-mi` triggers the `zo`/`li` split documented in Domain 7: `zo`
  (organism) vs `li` (social agent) are distinct, allowing this perspective-split to be
  grammatically encoded.

---

**S147 — Other-observer: clinical assessment of third party** *(fa-CON-D2)*

"I model: their organism's affective substrate is in persistent low."

```
Gloss:    la-mi  to  [la-zo-ze  fa  vo-de  re]
Literal:  agent:I  form-model  [agent:their-organism  substrate  value-decay  recurring]
Natural:  I analytically model that their organism's affective substrate is in a state
          of recurring value-decay. — Clinical diagnostic, first-person epistemic frame.
```

**Notes:**
- Same observer-mode construction as S146; different referent. `la-zo-ze` = organism
  of ze (third party). The speaker (`la-mi  to`) asserts their model; the affective
  state is attributed to the other person's organism (`la-zo-ze`).
- Register: clinical or analytical. This is the Tonesu form for "I think they're
  depressed" — but with the epistemic frame explicit (`la-mi  to` = I, as a modeling
  agent, hold this as my current model).
- The `la-mi  to [...]` wrapper makes this clearly attributable: the speaker owns
  the model. Compare to S152 (bare clinical assertion without epistemic wrapper):
  `la-zo-ze  fa  vo-de  re` = flat assertion; `la-mi  to  [la-zo-ze  fa  vo-de  re]`
  = speaker attributes the judgment to themselves. The epistemic-accountability
  distinction (Domain 6) is live here.

---

### fa-CON-E: `se`/`fa` Independence and Explicit Contrast (S148–S149)

**Goal:** Corpus evidence for the two key orthogonality claims about `se` and `fa`:
(1) `fa` operates without any `se` signal (depression without external cause);
(2) `se` and `fa` both activate for the same event and produce distinct reports.

---

**S148 — `fa` without `se`: depression/anhedonia case** *(fa-CON-E1)*

"No signal detected. Substrate registers value-decay."

```
Gloss:    la-mi  se-no.  la-mi  fa  vo-de.
Literal:  agent:I  perception-absent.  agent:I  substrate  value-decay.
Natural:  I am detecting nothing from the world. My affective substrate nonetheless
          registers value-decay. — Chemical depression without external cause.
```

**Notes:**
- `se-no` = signal-absence / no external detection. Not emotional numbness (which would
  be `fa-no`, S144) — this is the *perception* channel reporting nothing incoming.
  `la-mi  fa  vo-de` = substrate active, in value-decay, without any external signal
  to explain it.
- This is the structural argument for why `fa` must be a separate primitive from `se`.
  If affect were reducible to perception (`se`), `la-mi  se-no.  la-mi  fa  vo-de.`
  would be contradictory: no signal → no affect. The sentence is grammatically and
  experientially coherent without contradiction. `fa` is not a downstream product of
  `se`; it is a parallel layer.
- Experiential correlates: chemical depression, SSRI baseline change, circadian mood
  variation, endocrine mood shifts. All cases where bodily chemistry produces affective
  substrate state independently of incoming perceptual signal.

---

**S149 — Both registers: single event, two-layer report** *(fa-CON-E2)*

"I detect value-rise at the outcome. [And:] substrate is in positive-rise."

```
Gloss:    la-mi  se  vo-be  lo-du.  la-mi  fa  vo-be.
Literal:  agent:I  perceive  value-increasing  patient:result.
          agent:I  substrate  value-increasing.
Natural:  I detect positive quality in the result [external, directed]. And my
          affective substrate is in positive-rise [internal, undirected]. Two layers
          of the same positive event reported in sequence.
```

**Notes:**
- `se  vo-be  lo-du` = detection of value-increase directed at a specific result
  (`lo-du` = patient-marked outcome). External, object-directed perception. `fa  vo-be`
  = substrate positive-rise without object. Internal, undirected.
- English compresses both into "I feel good about this" — a single evaluation that
  may or may not track two separable phenomena. Tonesu preserves the distinction:
  the cognitive/evaluative report (`se`) and the substrate tone (`fa`) are both present
  and separately nameable in adjacent clauses.
- The two clauses can come apart: an anhedonic speaker might report `se  vo-be  lo-du`
  (I evaluate the outcome positively) while also reporting `fa-no` (substrate absent).
  The cognitive evaluation and the felt affect are separable layers. S149 demonstrates
  the case where they align; S144 demonstrated the case where they don't.

---

### fa-CON-F: Boundary Tests (S150–S154)

**Goal:** Confirm that bodily states stay with `la-zo-mi` (not `fa`); the usage guard
holds (no named-emotion via bare `fa-vo-X`); `fa` works in third-party clinical
assertion register; and `se-no-to` / `fa-no-to` are precisely distinct.

---

**S150 — Bodily depletion: NOT `fa`** *(fa-CON-F1)*

"My organism is depleted."

```
Gloss:    la-zo-mi  de.
Literal:  organism-of-me  decays.
Natural:  My body's resources are depleted. — Physical fatigue, not affective state.
```

**Notes:**
- `la-zo-mi` = organism-of-me as perspective anchor. `de` = decay/depletion. The
  construction locates depletion in the biological substrate, not the affective substrate.
- This is the fatigue construction. Key contrast: `la-zo-mi  de` ≠ `la-mi  fa-de`.
  `fa-de` (S145) = affect-level diminishing. `la-zo-mi  de` = organism's physical
  resources depleting. They may co-occur (exhausted *and* emotionally flat) but are
  different ontological events.
- Confirms that `la-zo-mi` cluster stays separate from `fa` cluster under corpus
  pressure. The boundary between body-state and affect-state is active in the grammar.
- Compare: `la-zo-mi  de  lo-ra` (organism depleted of energy = hunger, S150-alt) —
  same `la-zo-mi` frame, with `lo-ra` (patient: energy) specifying the resource.

---

**S151 — Usage guard: processual happiness, not `fa-vo-be`** *(fa-CON-F2)*

"The outcome emerged. Affect rose. Value-rise detected at the result."

```
Gloss:    lo-du  be.  la-mi  fa-be.  la-mi  se  vo-be  lo-du.
Literal:  patient:result  generates.  agent:I  affect-rises.
          agent:I  perceive  value-increasing  patient:result.
Natural:  The outcome came in. My affect rose. I detect quality-increase when I look
          at the result. — This sequence is what Tonesu says instead of "I'm happy
          about the outcome."
```

**Notes:**
- The usage guard (Principle 9, normative): `fa-vo-be` is not joy; `fa-vo-de` is not
  sadness. Named emotional states are derived via process constructions, not via bare
  `fa + quality` labels.
- This sentence demonstrates the *correct* Tonesu construction for what English encodes
  as "I'm happy about this": three stages —  external event (`lo-du  be`), substrate
  activation (`la-mi  fa-be`), directed evaluation (`la-mi  se  vo-be  lo-du`). No
  single word covers all three; the sequence is the expression.
- The guard is meaningful: `la-mi  fa-be` ≠ "I'm happy" by itself — that's substrate
  rising without an evaluation. `la-mi  se  vo-be  lo-du` ≠ "I'm happy" alone — that's
  a directed evaluation without a substrate report. The full state requires both, and
  a trigger. English conflates all three layers into a single word.

---

**S152 — Third-party clinical assertion without epistemic wrapper** *(fa-CON-F3)*

"Their organism: affective substrate in persistent low. No model of cause."

```
Gloss:    la-zo-ze  fa  vo-de  re.  la-ze  fa-no-to  lo-go.
Literal:  organism-of-ze  substrate  value-decay  recurring.
          agent:ze  affect-no-model  patient:cause.
Natural:  Their organism's affective substrate is in a state of recurring value-decay.
          They have no model of the cause. — Clinical-record register.
```

**Notes:**
- Third-party `fa` assertion in two clauses. No `la-mi  to [...]` wrapper: the speaker
  asserts these as flat clinical facts, not as personal epistemic attributions. This is
  the record-entry register: an objective description.
- Compare to S147 (observer mode with `la-mi  to  [la-zo-ze  fa  vo-de  re]`): S147
  makes the speaker's epistemic stance explicit; S152 omits it. Domain 6 distinction:
  the observation is either attributed to the observer (S147) or asserted as record
  (S152). Both are valid; they differ in epistemic-accountability frame.
- `la-ze  fa-no-to  lo-go` = `la-ze` as `fa-no-to` anchor: ze (not zo-ze) holds the
  unresolved-affect state. The shift from `la-zo-ze` (organism of ze) to `la-ze`
  (ze as agent) for the second clause reflects that `fa-no-to` is an agent-level state
  (about forming a model) rather than a purely organism-level state.

---

**S153 — `se-no-to` vs `fa-no-to`: minimal distinction pair** *(fa-CON-F4)*

"Something arrived; I can't model it. [vs.] Affect is active; I can't model why."

```
Gloss A:  la-mi  se-no-to.
Gloss B:  la-mi  fa-no-to.

Literal A: agent:I  perception-no-model.
Literal B: agent:I  affect-no-model.

Natural A: I detected something; no model formed of what it was.
Natural B: My affective substrate is active; no model of why.
```

**Notes:**
- The W090 `se-no-to` / `fa-no-to` pair: same `no-to` stall, different entry points.
  - `se-no-to` (W090): the stall is *upstream* at the `se → to` transition. The
    perceptual signal arrived but did not resolve into a model. "I perceived something
    I couldn't identify."
  - `fa-no-to`: the substrate is active, but the `fa → to` transition did not occur.
    "I feel something but I don't know why." There may have been no `se` event at all
    — the substrate activated from internal chemistry, and still no model formed.
- These can co-occur: `la-mi  se-no-to.  la-mi  fa-no-to  lo-go.` = "Something arrived
  (couldn't model it) and now affect is up (can't model why either)." The full double-
  stall scenario. S140 demonstrates this combined form.
- English has only "I don't know what I'm feeling" for both. Tonesu separates the
  perceptual-stall from the substrate-stall, which are experientially distinct: one is
  about identifying something external; the other is about naming an internal state.

---

**S154 — `fa-no-to  lo-go` in neutral/professional context** *(fa-CON-F5)*

"The document arrived. Affect rose. No model of the cause formed."

```
Gloss:    lo-si-mu  be.  la-mi  fa-be.  la-mi  fa-no-to  lo-go.
Literal:  patient:document  generates.  agent:I  affect-rises.
          agent:I  affect-no-model  patient:cause.
Natural:  An official document arrived. My affective substrate rose. The substrate
          has not resolved into a model of why this document is affecting me.
```

**Notes:**
- `lo-si-mu` = patient-marked document (`si-mu` = encoded-artifact = individual record
  or document, attested S058/S070). `be` = generation/emergence: the document arrived.
- Tests `fa-no-to  lo-go` outside of an interpersonal/relationship context (S134 used
  it for the breakup scenario) — here it is used for an institutional-signal trigger.
  The construction is context-independent: (a) a signal created an affective response;
  (b) the substrate has not resolved into a model of the causal mechanism. This is the
  generic "I got a result and I don't know how to feel about it" form.
- Experiential range: receiving ambiguous test results; a news event that unsettles
  without explanatory framework; a sudden decision from an institution that arouses
  affect before understanding. `fa-no-to  lo-go` covers all these cases.
- Context independence confirmed: `fa-no-to  lo-go` is not specialized to personal
  loss. It describes any pipeline stall where the cause-model is specifically absent.

---

### fa-CON Verdict

**`fa` confirmed across all 20 use cases. No grammar friction, no new rules required.**

| Group | Constructions confirmed | Status |
|-------|------------------------|--------|
| fa-CON-A (S135–S138) | `fa fe-ki`, `fa vo-be`, `fa vo-de re`, `fa fe-de` | ✓ All four substrate-column base forms |
| fa-CON-B (S139–S141) | Full pipeline, stall, propositional skip | ✓ Pipeline optional at `fa`-layer confirmed |
| fa-CON-C (S142–S145) | `fa-ki`, `fa-re`, `fa-no`, `fa-de` | ✓ All four new compounds first-attested |
| fa-CON-D (S146–S147) | Self-observer, other-observer | ✓ `la-mi to [la-zo-X fa Y]` stable for both |
| fa-CON-E (S148–S149) | `se`/`fa` independence; both-register report | ✓ Orthogonality confirmed; both-layer report clean |
| fa-CON-F (S150–S154) | Bodily boundary, usage guard, clinical register, `se-no-to`/`fa-no-to` distinction, neutral context | ✓ All boundary cases hold |

**Key finding: `fa` is optional at the `fa`-layer.** S141 establishes that purely
propositional signals bypass `fa` entirely. This makes `fa` a conditional-activation
layer, not a mandatory processing stage. The three-stage label is accurate but
incomplete: `se → to` (propositional), `se → fa → to` (organism-relevant), and
`fa → to` (or `fa-no-to` stall, purely internal, no external trigger) are all
grammatically valid pathways.

**Key finding: `fa` and `se` are orthogonal under all test conditions.** S144
(`se`-on, `fa`-off = anhedonia) and S148 (`se`-off, `fa`-on = chemical depression)
both produce well-formed, experientially coherent sentences. The primitive separation
holds under pressure.

**Compounds to register (pending, flagged this batch):**
- `fa-ki` (affect-shift) — first attested S142
- `fa-re` (affect-cycle) — first attested S143
- `fa-no` (affective numbness) — first attested S144
- `fa-de` (affect-fading) — first attested S145

---

## MG-001 Diagnostic: Model-Domain Frame (S158–S161)

**Purpose:** Resolve MG-001. CF-001 established `to-go [X]  Y` for single-sentence
counterfactual assertions. That construct requires `to-go` on every sentence. A
multi-sentence causal chain in a model space currently produces three or more repeated
`to-go` prefixes for what is logically a single analytical scope. This batch proposes,
tests, and adopts a discourse-scope frame construction that opens and closes model space
for a stretch of sentences rather than per-sentence.

**Design candidate from MG-001 note:** `to  lo-[model]  be` as scope-opener, with
`to  lo-[model]  de` as explicit closer and any actuality-assertion as implicit closer.
In-scope sentences operate in model space without per-sentence `to-go`.

**New compound introduced this batch:**
- `go-su` = cause-structure = organized causal analysis model (compositional; not separately
  registered — transparent from `go` (cause) + `su` (structure/organization))

---

**S158 — The per-sentence `to-go` problem** *(MG-001-A)*

Three-step signal-failure chain. Each step requires its own counterfactual frame marker.

```
Gloss:    to-go [lo-si  no  be  ti-de]  la-li-pu  no  se  lo-si  ti-de.
          to-go [la-li-pu  no  se  lo-si  ti-de]  la-li-pu  no  ka  fe-si  ti-de.
          to-go [la-li-pu  no  ka  fe-si  ti-de]  lo-li-pu  de  ti-de.

Literal:  counterfactual-causal [patient:signal not-generates past]
            agent:crew not-perceives patient:signal past.
          counterfactual-causal [agent:crew not-perceives patient:signal past]
            agent:crew not-performs warning past.
          counterfactual-causal [agent:crew not-performs warning past]
            patient:collective decays past.

Natural:  Had the signal not arrived, the crew would not have received it.
          Had the crew not received it, they would not have issued a warning.
          Had they not issued a warning, the collective would have suffered.
```

**Notes:**
- Three propositions that form a single causal chain in a single analytical scope. Each
  requires its own `to-go [X]  Y` because the current grammar has no multi-sentence
  scope frame. The non-actuality marker is repeated three times for what is logically
  one non-actual frame.
- `lo-si  no  be  ti-de` = signal not-generated past = "the signal had not arrived."
  (`be` = generation/emergence; `no  be` = did not generate = did not arrive).
- `la-li-pu  no  se  lo-si` = crew not-detected signal. `li-pu` = collective/crew (established).
- `la-li-pu  no  ka  fe-si` = crew not-performed warning-signal. `fe-si` = W024 (alert).
- `lo-li-pu  de` = collective/patient decays = collective suffered.
- This is the problem statement for MG-001. The solution follows at S159.

---

**S159 — Model-domain frame: scope-open / in-model chain / scope-close** *(MG-001-B)*

Same three-step chain, now under a sustained model-domain scope frame.

```
Gloss:    to  lo-go-su  be.
          lo-si  no  be  ti-de.
          la-li-pu  no  se  lo-si  ti-de.
          la-li-pu  no  ka  fe-si  ti-de.
          to  lo-go-su  de.
          la-to-fe-su  ka  to-fe-su-ki  lo-go-su  ti-de.

Literal:  model  patient:causal-analysis  activates.   [SCOPE OPENS]
          patient:signal  not-generates  past.          [IN MODEL]
          agent:crew  not-perceives  patient:signal  past.  [IN MODEL]
          agent:crew  not-performs  warning  past.     [IN MODEL]
          model  patient:causal-analysis  closes.      [SCOPE CLOSES]
          agent:standards-body  performs  publication-event  patient:causal-analysis  past.
                                                        [ACTUALITY RETURN]

Natural:  [The causal analysis model is now active.]
          The signal had not arrived.
          The crew had not received it.
          The crew had not issued the warning.
          [Causal analysis model closes.]
          The investigation body then published the causal analysis.
```

**Notes:**
- `to  lo-go-su  be` = model (root `to`) + patient: causal-analysis (`lo-go-su`) +
  activation (`be`). No `la-` anchor = impersonal, parallel to `to-go [X]  Y`. The
  scope is opened without asserting a thinker.
- `go-su` = cause (root `go`) + structure (root `su`) = organized causal analysis model.
  Compositionally transparent (parallel to `to-su` = organized knowledge, `ne-su` =
  organizational network). Not separately registered; flagged as a compound candidate.
- **In-scope sentences** (`lo-si  no  be  ti-de` through `la-li-pu  no  ka  fe-si  ti-de`):
  note these are structurally identical to the premises of the `to-go [X]  Y`
  constructions in S158 — minus the outer `to-go [...]  result` frame. In model scope
  these are *assertions* within the model, not per-sentence counterfactuals. The frame
  sustains non-actuality; individual sentences state in-model facts. Causal links are
  sequentially implied by ordering and `go` can be used explicitly if a single causal
  step needs emphasis.
- `to  lo-go-su  de` = model (root `to`) + patient: causal-analysis + decay/close (`de`).
  Explicit scope closer. Symmetric with opener: `be` = activates, `de` = closes.
- `la-to-fe-su  ka  to-fe-su-ki  lo-go-su  ti-de` = actuality-return sentence. World-layer
  assertion: the investigation body (W072) completed publication of the causal analysis
  (W097 `to-fe-su-ki`). Marked `la-[agent]  ka  [action]` with no model-frame = clearly
  world-layer. Implicitly closes any remaining model scope even if the explicit `to  lo-go-su
  de` were omitted.
- **Efficiency gain:** S158 used three `to-go` prefixes for one logical scope. S159 uses
  two scope-markers (`be` and `de`) for three in-model sentences, with one mandatory
  `to-go`-equivalent marker amortized across the scope. For longer chains (five, ten
  sentences) the benefit grows proportionally.

---

**S160 — Attributed model-scope: institutional analysis** *(MG-001-C)*

"The investigation body activates the causal model. [In-model analysis.] The investigation
body closes the model."

```
Gloss:    la-to-fe-su  to  lo-go-su  be.
          lo-si  no  be  ti-de.
          la-li-pu  no  ka  fe-si  ti-de.
          la-to-fe-su  to  lo-go-su  de.

Literal:  agent:standards-body  conceptual-model  patient:causal-analysis  activates.
          patient:signal  not-generates  past.
          agent:crew  not-performs  warning  past.
          agent:standards-body  conceptual-model  patient:causal-analysis  closes.

Natural:  The investigation body opens the causal model.
          [In-model:] The signal had not arrived.
          [In-model:] The crew did not issue the warning.
          The investigation body closes the causal model.
```

**Notes:**
- `la-to-fe-su  to  lo-go-su  be` = attributed scope open. The `la-to-fe-su` (agent:
  investigation/standards body, W072) makes this an attributed model activation: the
  investigation body is asserting this model space, not a private speaker.
- This is the MG-001 complement to the attributed counterfactual form in S156:
  S156 (`la-to-fe-su  to  [to-go [X]  Y]`) = single-sentence attributed counterfactual.
  S160 (`la-to-fe-su  to  lo-go-su  be ... de`) = multi-sentence attributed model scope.
- The `la-to-fe-su` on the close sentence mirrors the opener: the same body that opened
  the scope explicitly closes it. In formal register this symmetry is expected
  (an investigation report's model-space is opened and closed by the same institutional
  voice). Informal register may omit the close or let actuality-return handle it.
- Contrast with S159: S159 opens scope impersonally (no thinker); S160 attributes scope
  to an institution. Both are valid; the choice signals whether the model claims an
  institutional owner.

---

**S161 — "According to [theory]": sustained theory-attributive scope** *(MG-001-D)*

"According to the standing doctrine, the following causal analysis holds."

```
Gloss:    la-to-re-su  to  lo-go-su  be.
          la-to-re-su  to  [la-li-pe  ne-ko  lo-si-su].
          la-to-re-su  to  [lo-si-su  de  go  lo-ne-fe  be].
          la-to-re-su  to  lo-go-su  de.

Literal:  agent:doctrine  conceptual-model  patient:causal-analysis  activates.
          agent:doctrine  holds-model  [agent:licensed-party  holds  patient:archive].
          agent:doctrine  holds-model  [patient:archive  decays  cause  patient:tension  rises].
          agent:doctrine  conceptual-model  patient:causal-analysis  closes.

Natural:  According to the standing doctrine, the following causal model applies:
          The doctrine holds that: the licensed party retains custody of the archive.
          The doctrine holds that: archive decay causes tension to arise.
          According to the doctrine, the analysis closes.
```

**Notes:**
- `la-to-re-su` = agent:standing-doctrine (W064, the standing organized doctrine/policy).
  `to  lo-go-su  be` = activates the causal model under this attributor. This form
  means "the doctrine opens a model scope" — a sustained "according to [doctrine]" frame.
- The inner sentences use `la-to-re-su  to  [proposition]`: single-sentence epistemic
  attribution continuing to cite the doctrine as the source. Within the model scope, the
  doctrine can either (a) use bare in-model assertions as in S160 (no per-sentence
  attributor), or (b) maintain explicit attribution sentence by sentence. S161 shows (b)
  — full attribution retained for legal/formal register.
- `la-li-pe` = agent: licensed-party (`li-pe` = person + threshold crossing = accredited
  party; compositional, unregistered). `ne-ko` = W003 (containment relation / custody).
- `go  lo-ne-fe  be` = cause + patient:tension + generation = "causing tension to arise"
  (causal sub-clause using `go` inside the model sentence).
- **The key design distinction (now corpus-attested):**
  | Scope type | Form | Attribution |
  |---|---|---|
  | Single-sentence attributed counterfactual | `la-X  to  [to-go [X]  Y]` | X owns the sentence |
  | Multi-sentence impersonal model scope | `to  lo-go-su  be ... de` | No thinker asserted |
  | Multi-sentence attributed model scope | `la-X  to  lo-go-su  be ... de` | X owns the scope |
  | Sustained theory-attribution, full | `la-X  to  lo-go-su  be; la-X  to  [prop]; la-X  to  lo-go-su  de` | X cited per sentence |

---

### MG-001 Verdict

**`to  lo-[model]  be` / `to  lo-[model]  de` adopted as the model-domain scope frame.**

| Element | Form | Notes |
|---------|------|-------|
| Scope open (impersonal) | `to  lo-[model]  be` | No stance-holder; parallel to `to-go [X] Y` |
| Scope open (attributed) | `la-X  to  lo-[model]  be` | X opens and owns the scope |
| Scope close (explicit) | `to  lo-[model]  de` | Symmetric: `be`=open, `de`=close |
| Scope close (implicit) | Any actuality-asserted sentence | World-layer assertion terminates model scope |
| In-scope sentences | No `to-go` prefix required | Scope sustains non-actuality |
| Causal links in-scope | `go [X]  Y` (not `to-go [X]  Y`) | Inner causal, model-layer |

**Grammar status:** `to  lo-[model]  be/de` is a **discourse-scope frame** — not a
clause-level introducer like `go [...]` or `to-go [...]`, but a sentence-level marker
that opens and closes a discourse scope. Added to spec/grammar.md § Model-Domain Frame.

**Compound status:** `go-su` (causal analysis structure) is compositionally transparent
and used in S158–S161. Not separately registered at this stage — monitor for whether
it needs its own W-number as usage spreads.

**MG-001 status:** CLOSED.
