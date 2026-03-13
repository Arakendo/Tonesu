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
- **Boundary rule tested (S015–S019):** matrix-level argument marker unambiguously signals return to matrix clause in single-level embedding. `ne` inside subordinate clause confirmed as argument marker, not boundary signal. Nested subordination untested.
- **Agent inheritance rule (wi-clauses, confirmed S016–S018):** omitting the purpose-clause agent unambiguously inherits the matrix agent. Rule formally stated in spec/grammar.md § Purpose Frame.
- **Compounding vs relative clause (S019):** compounding covers taxonomic description adequately; it cannot express capability (noun as agent of its own action). Relativizer gap confirmed. Imperative gap also confirmed. Both logged in open-questions.

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

- [ ] **T021** — The child drinks water. *(basic SVO, animate agent, substance)*
- [ ] **T022** — The tool cuts wood. *(instrument as agent, material object, action)*
- [ ] **T023** — The star emits light. *(natural agent, emission process, no intention)*
- [ ] **T024** — The machine stores information. *(device, abstract object, containment)*
- [ ] **T025** — The river flows to the sea. *(motion, direction, natural destination)*
- [ ] **T026** — Knowledge grows when information connects. *(abstract causation, two abstract NPs, conditional)*
