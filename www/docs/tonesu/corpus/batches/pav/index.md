---
title: "Agentless and Passive Clause Test"
---

# Agentless and Passive Clause Test

*Theme: [Domains](../../domains/)* · 10 sentences.

[← Domains](../../domains/) · [← Corpus](../../index.md)

---

## PAV-001 · Agentless and Passive Clause Test

**Purpose:** To establish the formal typology for agentless, passive, and emergence clauses in Tonesu. The grammar TODO at spec/grammar.md §Open Questions ("Define passive / agentless clause structure (no agent present)") is the explicit target. An early corpus pattern (`lo-ze  de` with no agent) exists in s001–s039 but used the now-retired `-past` suffix system. This batch confirms and extends the pattern under current grammar (`ti-de`), and maps the full typology.

**Design hypothesis:** The diagnostic variable is whether `ka` (intentional-action marker) appears in the predicate alongside an absent `la-`. Claim: `ka` present + `la-` absent = **intentional passive** (an agent acted; agent unspecified). `ka` absent + bare `lo-X` = **non-intentional process** (entity underwent a state change; no agent implied). A third type — **pure emergence** — uses `be` without `ka` and without tense marking.

**Reference compounds used in batch (transparent; not new registry entries):**
- `ra-su` = force-structure = physical structure (building, bridge)
- `su-mu-li` = structure-device-person = engineer (attested S164)
- `ra-ki-mu` = force-change-device = engine / machine (attested S034)
- `to-si` = knowledge-signal = transmitted teaching / doctrine
- `si-su` = signal-structure = written record / text

<span id="S559"></span>
**S559**
`la-su-mu-li  ka-be  lo-ra-su  ti-de`
*Active baseline: "The engineer built the structure.*

!!! annotation "Notes"
    Standard active clause. All slots filled: `la-su-mu-li` = agent (engineer); `ka-be` = intentional creation/growth; `lo-ra-su` = patient (structure); `ti-de` = past. This is the fully specified active reference form against which passive variants are measured in S560–S562.

<span id="S560"></span>
**S560**
`lo-ra-su  de  ti-de`
*Non-intentional process: "The structure collapsed.*

!!! annotation "Notes"
    No agent, no `ka`. Patient `lo-ra-su` + bare predicate `de` (decay/dissolution) + `ti-de` (past). This is a Type 1 patientive state applied as event: the structure entered a state of decay. The absence of `ka` is semantically significant — no intentional agent is encoded, and none is implied. Recovers the early agentless pattern (`lo-ze de`) from s001–s039 under current grammar. **ADMISSIBLE: canonical non-intentional process form.** Note: `de` here is not a catch-all agentless event verb — it specifically encodes decay/dissolution. The non-intentional process pattern is `lo-{patient} [non-ka predicate] ti-de`; the lexical predicate supplies its own semantics (`de` = decay, `ki` = movement, `be` = growth, etc.).

<span id="S561"></span>
**S561**
`lo-ra-su  ka-be  ti-de`
*Intentional passive: "The structure was built.*

!!! annotation "Notes"
    No `la-` (no explicit agent). `ka-be` = intentional creation/growth. The patient `lo-ra-su` is the only argument. Compare to S559: this is S559 with the agent stripped out. The critical question: does `ka` work without an explicit `la-`? **ADMISSIBLE: `ka` does not syntactically require a co-present `la-`.** When `ka` appears with no `la-`, it marks the agentive character of the event — the action was intentional — without specifying the actor. This is the **intentional passive**: `lo-{patient}  ka-{predicate}  ti-de` = X was (intentionally) Q-ed by someone, agent unspecified.
    
    **Core contrast (S560 vs S561):**
    - `lo-ra-su  de  ti-de` = "the structure changed / collapsed" — process, no intentional agent implied
    - `lo-ra-su  ka-be  ti-de` = "the structure was built" — passive, intentional agent implied but absent
    
    The distinction is carried by the presence or absence of `ka`. This is the **passive divide**.

<span id="S562"></span>
**S562**
`ro-ra-ki-mu  lo-ra-su  ka-be  ti-de`
*Instrument-present passive: "The structure was built using the engine.*

!!! annotation "Notes"
    `ro-ra-ki-mu` = instrument prefix (`ro-`) + engine (`ra-ki-mu`). No `la-` agent. Instrument is explicit; agent is absent. This tests whether `ro-` is a satellite argument independent of `la-`. **ADMISSIBLE: instrument clauses (`ro-`) do not require a co-present agent clause (`la-`).** Tools are never agents in Tonesu — the grammar explicitly blocks `la-ra-ki-mu` for "the machine did X" (machines are instruments, not volitional actors). When the instrument is named but the agent is not, the correct form is `ro-{tool}  lo-{patient}  ka-{predicate}`. This is the instrument-present passive.

<span id="S563"></span>
**S563**
`ra-su : ka-be  ti-de`
*Topic-frame passive: "As for the structure: [it was] built.*

!!! annotation "Notes"
    Patient extracted to topic position via the `:` frame. `ra-su` = topic NP (no `lo-` prefix — the `:` frame positions it outside the clause-internal argument slots). `:` = topic-comment boundary. `ka-be  ti-de` = predicate only; the patient slot of `ka-be` is filled implicitly by the topic NP. **ADMISSIBLE: topic-frame passivization is available.** The patient is in topic position; the comment clause is the bare passive predicate. No new rule is needed — the existing Pattern 3 ellipsis (argument drop when fully recoverable) licenses the patient drop inside the comment clause when the topic IS the patient. One spelling out: `ra-su : lo-ra-su ka-be ti-de` (topic + full passive) would be redundant; idiomatic Tonesu prefers the topic-drop form shown here.

<span id="S564"></span>
**S564**
`la-li-pu  ka-be  lo-su  ti-de`
*Institutional active: "The council enacted the law.*

!!! annotation "Notes"
    `li-pu` = person-collective = council/assembly; `su` = structure/order = law; `ka-be` = intentional creation. Fully active with an institutional agent. The same event in English would often appear as a passive: "a law was enacted." But in Tonesu, when the institutional agent is known and relevant, the active form with a collective agent (`la-li-pu`) is the natural expression. The intentional passive `lo-su  ka-be  ti-de` remains available but is pragmatically appropriate only when institutional authorship is unknown or deliberately suppressed. **Finding: in law, covenant, and formal institutional discourse, Tonesu prefers the active form with the institution named over the agentless passive.**

<span id="S565"></span>
**S565**
`la-si-su  ko  {la-Elohim  ne  go-no-fe}`
*Archival containment: "it is written that…*

!!! annotation "Notes"
    `si-su` = signal-structure = written record/document. `ko` = containment. `{la-Elohim ne go-no-fe}` = propositional content in structural braces (scope bracket). The record is in `la-` position — it is the container-agent of the containment predicate. **Finding: the Tonesu equivalent of "it is written that X" is structurally active.** The form is `la-{document}  ko  {X}` = "the document contains X." This is not a passive but a containment predicate with the text itself as the `la-` container-agent. There is no agentless equivalent for the archival-passive; the document occupies `la-`. Scripture-to-Tonesu translation always uses this form for "it is written / it is recorded."

<span id="S566"></span>
**S566**
`lo-pa  be`
*Pure emergence: "The world comes into being." (Genesis register)*

!!! annotation "Notes"
    `pa` = space/place/presence = the world (as spatial totality). `be` = growth/expansion/becoming. No `ka`, no `la-`, no `ti-de` (untensed). This is the **emergence form**: patient-slot entity + bare `be`. No intentional cause is encoded; the world grows into existence from no specified cause. The absence of `ti-de` gives a jussive/habitual/present reading alongside the declarative — `lo-pa  be` can mean "the world is coming into being" (present), "let the world be" (fiat), or "the world comes into being" (general/habitual). All three readings are structurally identical; context disambiguates. This is the appropriate form for creation-fiat utterances in Genesis register (Hebrew יְהִי, jussive). **ADMISSIBLE: `lo-X  be` = emergence; no agent, no intentionality marker.**

<span id="S567"></span>
**S567**
`la-Elohim  ka-be  lo-pa`
*Divine active creation: "God creates the world.*

!!! annotation "Notes"
    Explicit divine agent. `la-Elohim` = agent; `ka-be` = intentional creation; `lo-pa` = patient (world/space). No `ti-de` to match the untensed S566 for clean comparison; add `ti-de` for past-tense biblical reading (`la-Elohim ka-be lo-pa ti-de` = Genesis 1:1 past register). The contrast with S566 isolates the effect of agent presence.
    
    **Four-way passive typology (core result of PAV-001):**
    
    | Form | Example | Reading | Type |
    |------|---------|---------|------|
    | Active | `la-Elohim  ka-be  lo-pa` | God creates the world | named agent + intentional action |
    | Intentional passive | `lo-ra-su  ka-be  ti-de` | the structure was built | `ka` without `la-` = agent implied, unspecified |
    | Non-intentional process | `lo-ra-su  de  ti-de` | the structure collapsed | no `ka`, no `la-` = no agent implied |
    | Emergence | `lo-pa  be` | the world comes into being | no agent, no `ka`, untensed = pure becoming |
    
    (`ti-de` = past-tense marker; emergence form is untensed.)

<span id="S568"></span>
**S568**
`lo-to-si  ka-ki  ti-de`
*Sacred-historical passive: "A teaching was transmitted.*

!!! annotation "Notes"
    `to-si` = knowledge-signal = transmitted teaching/doctrine. `ka-ki` = intentional action of moving = intentional transmission/conveyance. `ti-de` = past. No explicit agent. This sentence asserts that the doctrine was transmitted by deliberate human action (not mere natural spread) without specifying who transmitted it. Appropriate for "it was taught that X," "the tradition handed this down," or "this was transmitted through the generations" — the canonical sacred-historical passive of scripture and oral tradition. **ADMISSIBLE: intentional passive in theological documentary register confirmed.**
    
    For propositional content add containment: `la-to-si  ko  {X}` = "the teaching contains X" (structurally active, same pattern as S565).

### Batch Summary

| Entry | Form | Verdict | Finding |
|-------|------|---------|---------|
| S559 (PAV-001-A) | `la-su-mu-li  ka-be  lo-ra-su  ti-de` | baseline | active reference form; all slots filled |
| S560 (PAV-001-B) | `lo-ra-su  de  ti-de` | **admissible** | non-intentional process; no `ka`, no `la-`; recovers early agentless pattern |
| S561 (PAV-001-C) | `lo-ra-su  ka-be  ti-de` | **admissible** | intentional passive; `ka` without `la-` encodes agent-implied-absent; **passive divide** |
| S562 (PAV-001-D) | `ro-ra-ki-mu  lo-ra-su  ka-be  ti-de` | **admissible** | instrument-present passive; `ro-` independent of `la-`; tools never agents |
| S563 (PAV-001-E) | `ra-su : ka-be  ti-de` | **admissible** | topic-frame passive; patient topicalized; `lo-` dropped from comment |
| S564 (PAV-001-F) | `la-li-pu  ka-be  lo-su  ti-de` | active (preferred) | institutional agent named; Tonesu prefers active when institution is known |
| S565 (PAV-001-G) | `la-si-su  ko  {la-Elohim  ne  go-no-fe}` | **active (containment)** | "it is written that" = containment predicate; text is `la-` agent |
| S566 (PAV-001-H) | `lo-pa  be` | **admissible** | emergence form; no agent, no `ka`, untensed; Genesis / creation-fiat register |
| S567 (PAV-001-I) | `la-Elohim  ka-be  lo-pa` | baseline | divine active; contrast to S566; four-way typology table established |
| S568 (PAV-001-J) | `lo-to-si  ka-ki  ti-de` | **admissible** | sacred-historical passive; doctrine transmitted; theological documentary register |

---

*Generated from [`registry/entries.yaml`](https://github.com/Arakendo/Tonesu/blob/main/registry/entries.yaml).*