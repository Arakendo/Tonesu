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
- [ ] **P001** — "They study in order to understand." *(purpose, same agent — canonical form of `wi` same-agent reduction)*
- [ ] **P002** — "I built the machine for you to use." *(purpose, different agent — full clause marking required)*
- [ ] **P003** — "She sent the message to warn them." *(purpose, different agent; tests whether warning-event agent defaults to sender or must be stated)*

**Relative-clause pressure test** *(do not attempt until purpose-clause structure is stable)*
- [ ] **P004** — "Build me a system that remembers past queries." *(imperative + beneficiary + noun-modifying clause + memory/retrieval semantics + past reference — let compounding fail first before designing a relativizer)*

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
1. **Purpose clauses** ("to [infinitive phrase]") need a formal structure when not collapsible into compounding. Candidate: `wi [action]` = "intending to [action]". Flag for spec/grammar.md.
2. `si` (signal/representation) is carrying "information" in both S013 and S014. Confirm this is the right root vs. `to` (conceptual pattern) or `to+si` (encoded knowledge).

---

## Observations

*(Running notes on what works and what doesn't)*

- The SOV + particle system reads clearly for simple sentences
- Nested concepts (S010) reveal the need for explicit grouping markers
- ~~Particle/root collision (`li`)~~ → resolved by renaming agent particle to `la`. Remaining overlaps (`ra`, `pa`, `ka`, `ne`) are lower priority
- Causal structures (S011, S013) confirm `go`/`du` framing as the canonical conditional strategy — no new particle needed
- ~~Inchoative derivation pattern missing~~ → resolved: `ROOT + ki` = enter state ROOT (spec/morphology.md)
- Abstract agents (`to`, `si` as grammatical subjects) now work cleanly with `la` as the unambiguous agent marker
- Purpose clauses ("to [infinitive]") not yet formalized — S014 absorbs via compounding but this won't generalize

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
