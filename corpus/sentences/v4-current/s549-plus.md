## Exclusive Particle Test (S549–S558) — Batch: EXC-001

**Purpose (GAP-EMD-004):** Test for "only / alone / exclusively" — the logical exclusivity operator. This construction appears constantly in theological discourse ("God alone is good," the Shema, Deut 4:35), philosophical argument ("only through knowledge can one act rightly"), and narrative ("I alone survived"). The design question: can Tonesu express exclusive scope compositionally, or does it need a new particle?

**Background:** "Only X is Y" is logically: {X is Y} AND {for all Z ≠ X, Z is not Y}. It is a *focus* operator that restricts the predicate to exactly one argument. Most natural languages have a dedicated particle for this (Hebrew רַק, Japanese だけ, Chinese 只). For Tonesu the question is whether this can be composed from existing primitives — specifically whether `ru` (unity/singularity) + `fe` (boundary/limit) = `ru-fe` = "the singular bounding case" = "solely/only/exclusively" — and what syntactic position it occupies.

**Primary candidates:**
| Form | Logic | Predicted role |
|------|-------|----------------|
| `no la-{class} ne Y` | deny the whole class | negative-universal half only; requires separate positive clause |
| `no la-{class} ne Y — la-X ne Y` | two-clause sequence | pragmatic exclusive; works but requires two propositions |
| `la-X ru ne Y` | `ru` as post-agent focus | must test: syntactic position unclear |
| `la-X ne ru` | `ru` as predicate | "X is one/unified" — cardinality, not exclusive |
| `ru-fe, la-X ne Y` | clause-initial scope particle | **primary candidate** — `ru` (unity) + `fe` (boundary) = "at the sole limit" |

---

**S549 — Baseline: "God is good."** *(EXC-001-A)*

```
la-Elohim ne vo
```

**Notes:** Simple property attribution. Establishes the reference form from which exclusive "only God is good" must be derived. `la-Elohim ne vo` = "God has the property of worth/value." `Elohim` used directly in agent position (convention from COR-001 theological batch: divine name without `na-` marker, consistent with S532–S538). No exclusive semantics — this is compatible with "God is good and so are many other things." **Baseline clear. EXC-001 count: 1.**

---

**S550 — Universal class negation: "No person is good."** *(EXC-001-B)*

```
no la-li ne vo
```

**Notes:** The negative-universal half of the exclusive claim. `la-li ne vo` = bare class attribution: "person[s] have worth." Fronted `no` negates the whole proposition: "not: person has worth" = "no person has worth." `li` bare (unquantified) functions as the class, following corpus precedent for class-level claims. This is the negation of the whole human class as a property-bearer — it does not quantify over individuals; it denies the class attribution. For the distributive reading ("each person"), a `pu` or `re` form would be needed; `la-li` is the class-property form. **Negative-universal confirmed. One half of the exclusive available. EXC-001 count: 2.**

---

**S551 — Two-clause pragmatic exclusive: "No person is good — God is good."** *(EXC-001-C)*

```
no la-li ne vo — la-Elohim ne vo
```

**Notes:** Matthew 19:17 structure: "Why do you call me good? No one is good but God alone." The `—` (prosodic suspension, EMD-002) creates an asymmetric juxtaposition: (1) deny the class; (2) suspend; (3) affirm the single exception. This is structurally identical to the correction form `no — Y`, but operating at the class-level: the first clause is a true negative-universal, not a mistaken claim being corrected. The sequence reads as exclusive by conversational implicature: "no-one-in-this-class [has worth] — [and yet] God [does]." **Important limitation:** this is two propositions linked by `—`, not a single exclusive proposition. A Tonesu speaker extracts the exclusive reading by inference. There is no grammatical marker in this construction that encodes "and no one else" — the implicature is carried by the sequence + the denied class. If the class is not denied explicitly, the implicature fails. **Two-clause pragmatic exclusive is available but not tight. EXC-001 count: 3.**

---

**S552 — `ru` as post-agent focus: DIAGNOSTIC — syntactic ambiguity.** *(EXC-001-D)*

Attempt:
```
la-Elohim ru ne vo
```

**Notes:** Testing whether `ru` in the inter-argument position (after agent NP, before predicate) functions as an exclusive focus particle. **Two competing parses:**
1. `la-[Elohim-ru] ne vo` = "the unified/one God has worth" — `ru` compounds with the agent NP to form "unified-God." This yields a description (God as unified) + a property claim (has worth), not an exclusive claim.
2. `la-Elohim [ru-ne-vo]` = "God has unity-connection-worth" — `ru` compounds leftward with the predicate into a three-root complex. `ru-ne-vo` = unity-relation-value = ?. Semantically incoherent.
3. `la-Elohim` + floating-`ru` + `ne vo` — `ru` as an unattached focus adverb. **Tonesu has no established syntax for free-floating focus particles between agent and predicate.** `ya` (G030, attention-signal) is clause-initial before the agent NP, not post-agent. There is no established focus-particle position between agent and predicate.

All three parses are either semantically wrong (reading 1), incoherent (reading 2), or syntactically unadmitted (reading 3). **`ru` in post-agent position does not cleanly convey exclusivity.** The form is ambiguous and should not be used. Parse invariants are not violated but the sentence is syntactically unstable. **DIAGNOSTIC: `la-X ru ne Y` fails for exclusive. EXC-001 count: 4.**

---

**S553 — `ru` as predicate: the Shema form "YHWH is one."** *(EXC-001-E)*

```
la-Elohim ne ru
```

**Notes:** Testing `ru` in its natural predicate position. `la-Elohim ne ru` = "God has the property of unity/singularity" = "God is one." This is the Tonesu form of the Shema (Deut 6:4: שְׁמַע יִשְׂרָאֵל יְהוָה אֱלֹהֵינוּ יְהוָה אֶחָד — "Hear, O Israel: YHWH our God, YHWH is one"). The Shema does not primarily assert exclusive scope ("there is no other God") — it asserts divine *unity* and *non-division* (אֶחָד, echad = one/undivided). `la-Elohim ne ru` captures this: God has the property of being undivided, singular, whole. **Positive finding:** the Shema form is clean and natural in Tonesu. `ne ru` = "is one/unified" is a transparent compositional predicate. **Critical distinction:** `la-Elohim ne ru` (God is one — cardinality/unity property) is distinct from "God alone is good" (exclusive scope over a different predicate). `ru` as predicate asserts a property of God; it does not restrict another predicate to God alone. **DIAGNOSTIC: `la-X ne ru` = "X is one." Not an exclusive. Shema form now established. EXC-001 count: 5.**

---

**S554 — `ru-fe` clause-initial: "ONLY God is good."** *(EXC-001-F)*

```
ru-fe, la-Elohim ne vo
```

**Notes:** Primary candidate. `ru-fe` = unity (singularity, `ru`) + boundary/limit (`fe`) = "the singular bounding case" = "at the one limit" = "solely / exclusively." Clause-initial position followed by `,`, parallel to `ya` (G030), which is also clause-initial + `,` as an attention-signal scope marker. The parallel: `ya, [clause]` = "attend to this: [clause]"; `ru-fe, [clause]` = "at the sole limit: [clause]" = "only [clause] holds."

**Compositional analysis:**
- `no-fe` = no-boundary = without limit (THO-001 extremal suffix: `vo-no-fe` = boundless value)
- `ru-fe` = singular-boundary = at the one limit = the single case that holds
- `ru-fe, la-X ne Y` = "at the sole limiting case: X has Y" → "only X has Y"

**Exclusivity logic:** `ru-fe` marks the proposition as true at a single bounding point — one instance holds, and the boundary is at that instance. Every position outside that boundary is excluded. The exclusive reading is compositionally grounded: not just "X is good" (S549), not "no one is good — X is good" (S551, two clauses), but a single proposition in which the exclusivity is encoded by the scope marker.

**Syntactic position:** `ru-fe` is clause-initial, pre-argument, functions as a scope-restricting prefix to the whole proposition. It does not integrate into the NP or predicate compound; it scopes over the entire clause from clause-initial position. This is the same slot as `ya` and parallel to use of `—` for prosodic scope. The `,` after `ru-fe` marks the scope boundary, as in `ya, [clause]`.

**Does it work here?** `ru-fe, la-Elohim ne vo` = "at the sole bounding point: God has worth" = "only God has worth." Yes — the exclusive reading is direct and compositionally transparent. **Primary candidate confirmed for agent-exclusive position. EXC-001 count: 6.**

---

**S555 — `ru-fe` method scope: "Only through knowledge can one act rightly."** *(EXC-001-G)*

```
ru-fe, go to ; ka-vo
```

**Notes:** Method exclusive — `ru-fe` restricts the *causal means*: the only path to right action is via knowledge. `go to` = "via knowledge" (causal frame); `;` = sequential connector; `ka-vo` = action-with-value = acting rightly. The full clause: "via knowledge; action-with-value." `ru-fe` scopes the entire causal proposition: "at the sole bounding point: [via knowledge, action-with-value]" = "only through knowledge does one act with value."

**Scope test:** can `ru-fe` scope over a `go` causal frame constituent? Here it scopes the whole propositional structure (not just the agent NP or the predicate). The scoped content is a complex causal proposition `go to ; ka-vo`. `ru-fe` as clause-initial marker handles this cleanly — it makes no claims about argument structure inside the clause; it simply asserts the exclusive truth-domain for the whole proposition.

**Compare to two-clause workaround:** the same claim could be made as: `no go-pu-to, ka-vo — go to, ka-vo` = "not via many knowledges [does one] act rightly — [only] via knowledge [does one]." This requires explicitly invoking the negative alternative. `ru-fe` compresses this to a single-clause exclusive. **Method exclusive clean. `ru-fe` productive in non-agent scope. EXC-001 count: 7.**

---

**S556 — `ru-fe` agent-narrative: "I alone survived."** *(EXC-001-H)*

```
ru-fe, la-mi ne zo
```

**Notes:** Narrative exclusive context (catastrophe/battle survivor). `la-mi ne zo` = "I have the property of being a living thing" = "I am alive / I survived." `ne zo` uses the copula + `zo` (living thing/organism) as a stative property predicate: I am in the living-organism class. `ru-fe, la-mi ne zo` = "at the sole bounding point: I am alive" = "I alone am alive" = "I alone survived."

**Compare to `la-mi ne ru`:** "I am one (unified)" — cardinality (S553 pattern), not exclusive. The exclusive is `ru-fe, la-mi ne zo` — `ru-fe` scopes the whole existence claim, not just a unity predicate.

**Register check:** in survivor narrative, the `ru-fe` form is emotionally loaded: it declares solitary survivorship without the verbosity of the two-clause form. The form works at the intensity level of `DEB-001-I` (`ke!`) — a statement with compressed force. **Agent-narrative exclusive clean. EXC-001 count: 8.**

---

**S557 — Theological canonical: "God alone is the necessary being."** *(EXC-001-I)*

```
ru-fe, la-Elohim helms go-no-fe
```

**Notes:** Deut 4:35 type — "YHWH, he is God; there is no other besides him." The Tonesu form uses the full theological vocabulary: `la-Elohim` (agent); `helms` (strict identity predicate, G012 — `X helms Y` = "X is by strict definition Y," the strongest identity claim available); `go-no-fe` (necessary/uncaused being — cause-without-limit, from THO-001).

`la-Elohim helms go-no-fe` = "God is by strict definition the necessary being." `ru-fe` scopes the whole identity claim: "at the sole bounding point: God is by strict definition the necessary being" = "God alone is the necessary being."

This is the densest theological form tested — three high-register elements (`ru-fe`, `helms`, `go-no-fe`) in one sentence. **Parse:** no ambiguity. `ru-fe,` = exclusive scope marker (clause-initial); `la-Elohim` = agent NP; `helms` = strict identity predicate; `go-no-fe` = patient NP (the necessary being, a compound description). The sentence is syntactically linear: scope + agent + predicate + patient.

**Register note:** in theological discourse, `ru-fe, la-X helms Y` is the maximal exclusive identity claim — "uniquely and necessarily, X alone is by definition Y." This is the form for monotheistic confession, for philosophical absolute claims, and for any proposition where the combination of strict identity and exclusive scope is intentional and precise. **Theological canonical established. EXC-001 count: 9.**

---

**S558 — DIAGNOSTIC: `ya` + `ru-fe` stacking test.** *(EXC-001-J)*

```
ya, ru-fe, la-Elohim ne vo
```

**Notes:** Both `ya` (attention-signal) and `ru-fe` (exclusive scope) are clause-initial particles with `,` after each. Can they stack? `ya, ru-fe, la-Elohim ne vo` = "attend to this: [at the sole bounding point: God has worth]" = "attend to this — only God has worth." The `ya` directs the listener's attention to the exclusive claim that follows. The two particles operate at different levels: `ya` is pragmatic (meta-communicative: "register this"); `ru-fe` is semantic (truth-conditional: "at the one limiting case"). They do not interfere.

**Parse:** `ya,` → `ru-fe,` → `la-Elohim ne vo`. Left-to-right scope: pragmatic outer scope (`ya`) wrapping semantic inner scope (`ru-fe`) wrapping proposition. This is consistent with how scope modifiers more generally work in left-branching grammars: outermost operator first. Stacking order: pragmatic > semantic > propositional content.

**Register:** this form would appear in heated theological argument when the speaker both insists the listener attend AND marks the claim as exclusively true. "I need you to register this — and it is exclusively so: God alone has worth." In DEB-001 terms, the `ya` is the attention-signal that precedes an exclusive claim in adversarial discourse. **Stacking is clean. Parse is unambiguous. EXC-001 count: 10.**

---

## EXC-001 Batch Summary

| Entry | Form | Verdict | Finding |
|-------|------|---------|---------|
| S549 (EXC-001-A) | `la-Elohim ne vo` | baseline | property attribution; no exclusive |
| S550 (EXC-001-B) | `no la-li ne vo` | adequate | negative-universal class negation; one half of exclusive |
| S551 (EXC-001-C) | `no la-li ne vo — la-Elohim ne vo` | adequate / verbose | two-clause pragmatic exclusive; implicature-based, not grammatically encoded |
| S552 (EXC-001-D) | `la-Elohim ru ne vo` (attempt) | **fails** | `ru` in post-agent position: syntactically ambiguous; three competing parses, none exclusive |
| S553 (EXC-001-E) | `la-Elohim ne ru` | adequate (different claim) | "God is one/unified" = Shema form; cardinality/unity predicate, not exclusive scope |
| S554 (EXC-001-F) | `ru-fe, la-Elohim ne vo` | **`ru-fe` confirmed** | agent-exclusive clean; compositionally transparent; clause-initial scope particle |
| S555 (EXC-001-G) | `ru-fe, go to ; ka-vo` | **`ru-fe` confirmed** | method-exclusive clean; `ru-fe` scopes over causal frame constituent |
| S556 (EXC-001-H) | `ru-fe, la-mi ne zo` | **`ru-fe` confirmed** | agent-narrative exclusive clean; compressed survivor form |
| S557 (EXC-001-I) | `ru-fe, la-Elohim helms go-no-fe` | **`ru-fe` confirmed** | theological canonical; strict identity + `ru-fe` = maximal exclusive claim |
| S558 (EXC-001-J) | `ya, ru-fe, la-Elohim ne vo` | attested | `ya` + `ru-fe` stacking clean; pragmatic outer / semantic-exclusive inner |

---

### EXC-001 Findings

**Finding 1: `ru-fe` is a compositionally grounded exclusive scope particle.** Confirmed across four syntactic positions: agent-exclusive (S554), method-exclusive (S555), agent-narrative (S556), theological strict-identity (S557). The compositional derivation is transparent: `ru` (unity/singularity) + `fe` (boundary/limit) = "the singular bounding case" = solely/exclusively. This parallels `no-fe` (no-limit = infinite) in structure; `ru-fe` is its complement: "the one limit" = "at exactly this boundary, and nowhere else."

**Finding 2: `ru` in post-agent position fails — it is not a viable focus particle in that slot.** The form `la-X ru ne Y` is syntactically ambiguous between three competing parses (NP-compound, predicate-compound, floating adverb), none of which cleanly yield exclusive semantics. Tonesu has no established syntax for inter-argument focus particles; do not use this form.

**Finding 3: `la-X ne ru` = "X is one/unified" — the Shema form is established.** Distinct from the exclusive: this is a unity/cardinality predicate (God is undivided/singular). `la-Elohim ne ru` = "God is one" captures the Shema (Deut 6:4) cleanly. The theological corpus now has two distinct forms: `la-Elohim ne ru` (the Shema — divine unity) and `ru-fe, la-Elohim helms go-no-fe` (Deut 4:35 — divine exclusivity/necessary being).

**Finding 4: Two-clause `no [class] — [exception]` is available but implicature-based.** The sequence `no la-li ne vo — la-Elohim ne vo` carries the exclusive reading by conversational implicature from the negated-class + suspension + affirmation structure. It is not syntactically marked as exclusive. For contexts where the implicature might not carry (e.g., the class negation and exception are distant in the discourse, or the listener is not co-present), `ru-fe` is required for unambiguous exclusive marking.

**Finding 5: `ya` + `ru-fe` stack cleanly.** Pragmatic (`ya`) scopes over semantic (`ru-fe`) scopes over propositional content. Order rule: outermost operator stated first. `ya, ru-fe, [clause]` = "attend to this exclusive claim: [clause]." No parse ambiguity.

**Recommendation: Admit `ru-fe` (G031) as the canonical exclusive scope particle.** Four attested positions, compositionally transparent, no parse ambiguity, productive stacking with `ya`. Writing convention: `ru-fe,` (clause-initial, followed by comma) = "only / solely / exclusively." Written solid: `rufe,` in Tonesu prose.

---

## Agentless and Passive Clause Test (S559–S568) — Batch: PAV-001

**Purpose:** To establish the formal typology for agentless, passive, and emergence clauses in Tonesu. The grammar TODO at spec/grammar.md §Open Questions ("Define passive / agentless clause structure (no agent present)") is the explicit target. An early corpus pattern (`lo-ze  de` with no agent) exists in s001–s039 but used the now-retired `-past` suffix system. This batch confirms and extends the pattern under current grammar (`ti-de`), and maps the full typology.

**Design hypothesis:** The diagnostic variable is whether `ka` (intentional-action marker) appears in the predicate alongside an absent `la-`. Claim: `ka` present + `la-` absent = **intentional passive** (an agent acted; agent unspecified). `ka` absent + bare `lo-X` = **non-intentional process** (entity underwent a state change; no agent implied). A third type — **pure emergence** — uses `be` without `ka` and without tense marking.

**Reference compounds used in batch (transparent; not new registry entries):**
- `ra-su` = force-structure = physical structure (building, bridge)
- `su-mu-li` = structure-device-person = engineer (attested S164)
- `ra-ki-mu` = force-change-device = engine / machine (attested S034)
- `to-si` = knowledge-signal = transmitted teaching / doctrine
- `si-su` = signal-structure = written record / text

---

**S559 — Active baseline: "The engineer built the structure."** *(PAV-001-A)*

```
la-su-mu-li  ka-be  lo-ra-su  ti-de
```

**Written:** lasumuLi kabe lorasu tide

**Notes:** Standard active clause. All slots filled: `la-su-mu-li` = agent (engineer); `ka-be` = intentional creation/growth; `lo-ra-su` = patient (structure); `ti-de` = past. This is the fully specified active reference form against which passive variants are measured in S560–S562.

---

**S560 — Non-intentional process: "The structure collapsed."** *(PAV-001-B)*

```
lo-ra-su  de  ti-de
```

**Written:** lorasu de tide

**Notes:** No agent, no `ka`. Patient `lo-ra-su` + bare predicate `de` (decay/dissolution) + `ti-de` (past). This is a Type 1 patientive state applied as event: the structure entered a state of decay. The absence of `ka` is semantically significant — no intentional agent is encoded, and none is implied. Recovers the early agentless pattern (`lo-ze de`) from s001–s039 under current grammar. **ADMISSIBLE: canonical non-intentional process form.** Note: `de` here is not a catch-all agentless event verb — it specifically encodes decay/dissolution. The non-intentional process pattern is `lo-{patient} [non-ka predicate] ti-de`; the lexical predicate supplies its own semantics (`de` = decay, `ki` = movement, `be` = growth, etc.).

---

**S561 — Intentional passive: "The structure was built."** *(PAV-001-C)*

```
lo-ra-su  ka-be  ti-de
```

**Written:** lorasu kabe tide

**Notes:** No `la-` (no explicit agent). `ka-be` = intentional creation/growth. The patient `lo-ra-su` is the only argument. Compare to S559: this is S559 with the agent stripped out. The critical question: does `ka` work without an explicit `la-`? **ADMISSIBLE: `ka` does not syntactically require a co-present `la-`.** When `ka` appears with no `la-`, it marks the agentive character of the event — the action was intentional — without specifying the actor. This is the **intentional passive**: `lo-{patient}  ka-{predicate}  ti-de` = X was (intentionally) Q-ed by someone, agent unspecified.

**Core contrast (S560 vs S561):**
- `lo-ra-su  de  ti-de` = "the structure changed / collapsed" — process, no intentional agent implied
- `lo-ra-su  ka-be  ti-de` = "the structure was built" — passive, intentional agent implied but absent

The distinction is carried by the presence or absence of `ka`. This is the **passive divide**.

---

**S562 — Instrument-present passive: "The structure was built using the engine."** *(PAV-001-D)*

```
ro-ra-ki-mu  lo-ra-su  ka-be  ti-de
```

**Written:** rorakimu lorasu kabe tide

**Notes:** `ro-ra-ki-mu` = instrument prefix (`ro-`) + engine (`ra-ki-mu`). No `la-` agent. Instrument is explicit; agent is absent. This tests whether `ro-` is a satellite argument independent of `la-`. **ADMISSIBLE: instrument clauses (`ro-`) do not require a co-present agent clause (`la-`).** Tools are never agents in Tonesu — the grammar explicitly blocks `la-ra-ki-mu` for "the machine did X" (machines are instruments, not volitional actors). When the instrument is named but the agent is not, the correct form is `ro-{tool}  lo-{patient}  ka-{predicate}`. This is the instrument-present passive.

---

**S563 — Topic-frame passive: "As for the structure: [it was] built."** *(PAV-001-E)*

```
ra-su : ka-be  ti-de
```

**Written:** rasu : kabe tide

**Notes:** Patient extracted to topic position via the `:` frame. `ra-su` = topic NP (no `lo-` prefix — the `:` frame positions it outside the clause-internal argument slots). `:` = topic-comment boundary. `ka-be  ti-de` = predicate only; the patient slot of `ka-be` is filled implicitly by the topic NP. **ADMISSIBLE: topic-frame passivization is available.** The patient is in topic position; the comment clause is the bare passive predicate. No new rule is needed — the existing Pattern 3 ellipsis (argument drop when fully recoverable) licenses the patient drop inside the comment clause when the topic IS the patient. One spelling out: `ra-su : lo-ra-su ka-be ti-de` (topic + full passive) would be redundant; idiomatic Tonesu prefers the topic-drop form shown here.

---

**S564 — Institutional active: "The council enacted the law."** *(PAV-001-F)*

```
la-li-pu  ka-be  lo-su  ti-de
```

**Written:** lalipu kabe losu tide

**Notes:** `li-pu` = person-collective = council/assembly; `su` = structure/order = law; `ka-be` = intentional creation. Fully active with an institutional agent. The same event in English would often appear as a passive: "a law was enacted." But in Tonesu, when the institutional agent is known and relevant, the active form with a collective agent (`la-li-pu`) is the natural expression. The intentional passive `lo-su  ka-be  ti-de` remains available but is pragmatically appropriate only when institutional authorship is unknown or deliberately suppressed. **Finding: in law, covenant, and formal institutional discourse, Tonesu prefers the active form with the institution named over the agentless passive.**

---

**S565 — Archival containment: "it is written that…"** *(PAV-001-G)*

```
la-si-su  ko  {la-Elohim  ne  go-no-fe}
```

**Written:** lasiSu ko {laElohim ne gonofe}

**Notes:** `si-su` = signal-structure = written record/document. `ko` = containment. `{la-Elohim ne go-no-fe}` = propositional content in structural braces (scope bracket). The record is in `la-` position — it is the container-agent of the containment predicate. **Finding: the Tonesu equivalent of "it is written that X" is structurally active.** The form is `la-{document}  ko  {X}` = "the document contains X." This is not a passive but a containment predicate with the text itself as the `la-` container-agent. There is no agentless equivalent for the archival-passive; the document occupies `la-`. Scripture-to-Tonesu translation always uses this form for "it is written / it is recorded."

---

**S566 — Pure emergence: "The world comes into being." (Genesis register)** *(PAV-001-H)*

```
lo-pa  be
```

**Written:** lopa be

**Notes:** `pa` = space/place/presence = the world (as spatial totality). `be` = growth/expansion/becoming. No `ka`, no `la-`, no `ti-de` (untensed). This is the **emergence form**: patient-slot entity + bare `be`. No intentional cause is encoded; the world grows into existence from no specified cause. The absence of `ti-de` gives a jussive/habitual/present reading alongside the declarative — `lo-pa  be` can mean "the world is coming into being" (present), "let the world be" (fiat), or "the world comes into being" (general/habitual). All three readings are structurally identical; context disambiguates. This is the appropriate form for creation-fiat utterances in Genesis register (Hebrew יְהִי, jussive). **ADMISSIBLE: `lo-X  be` = emergence; no agent, no intentionality marker.**

---

**S567 — Divine active creation: "God creates the world."** *(PAV-001-I)*

```
la-Elohim  ka-be  lo-pa
```

**Written:** laElohim kabe lopa

**Notes:** Explicit divine agent. `la-Elohim` = agent; `ka-be` = intentional creation; `lo-pa` = patient (world/space). No `ti-de` to match the untensed S566 for clean comparison; add `ti-de` for past-tense biblical reading (`la-Elohim ka-be lo-pa ti-de` = Genesis 1:1 past register). The contrast with S566 isolates the effect of agent presence.

**Four-way passive typology (core result of PAV-001):**

| Form | Example | Reading | Type |
|------|---------|---------|------|
| Active | `la-Elohim  ka-be  lo-pa` | God creates the world | named agent + intentional action |
| Intentional passive | `lo-ra-su  ka-be  ti-de` | the structure was built | `ka` without `la-` = agent implied, unspecified |
| Non-intentional process | `lo-ra-su  de  ti-de` | the structure collapsed | no `ka`, no `la-` = no agent implied |
| Emergence | `lo-pa  be` | the world comes into being | no agent, no `ka`, untensed = pure becoming |

(`ti-de` = past-tense marker; emergence form is untensed.)

---

**S568 — Sacred-historical passive: "A teaching was transmitted."** *(PAV-001-J)*

```
lo-to-si  ka-ki  ti-de
```

**Written:** lotosi kaki tide

**Notes:** `to-si` = knowledge-signal = transmitted teaching/doctrine. `ka-ki` = intentional action of moving = intentional transmission/conveyance. `ti-de` = past. No explicit agent. This sentence asserts that the doctrine was transmitted by deliberate human action (not mere natural spread) without specifying who transmitted it. Appropriate for "it was taught that X," "the tradition handed this down," or "this was transmitted through the generations" — the canonical sacred-historical passive of scripture and oral tradition. **ADMISSIBLE: intentional passive in theological documentary register confirmed.**

For propositional content add containment: `la-to-si  ko  {X}` = "the teaching contains X" (structurally active, same pattern as S565).

---

## PAV-001 Batch Summary

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

### PAV-001 Findings

**Finding 1: The passive divide is `ka` presence / absence.** The `ka` particle marks intentional agency. When `la-` is absent but `ka` is present in the predicate, Tonesu encodes the intentional passive: an agent acted, but is unspecified. When `ka` is absent and `lo-X  Q  ti-de` is a bare patientive state with any non-`ka` predicate, the reading is non-intentional process. This divide maps cleanly onto English "X collapsed" (no `ka`) vs "X was demolished" (`ka`, no `la-`). **Caution on `de`:** the non-intentional process pattern admits any lexically appropriate predicate (`de` = decay, `ki` = movement, `be` = growth, etc.). `de` is not a generic agentless event verb — it specifically encodes decay/dissolution. Do not generalize `de` into all non-volitional intransitive events; use the semantically correct predicate for each event type.

**Finding 2: `ka` does not syntactically require a co-present `la-`.** Confirmed at S561, S562, S568. `ka` is semantically sufficient without an explicit agent. The intentional passive `lo-{patient}  ka-{predicate}  ti-de` is grammatical and unambiguous. This closes the grammar TODO.

**Finding 3: Instrument-present passive is `ro-{tool}  lo-{patient}  ka-{predicate}`.** `ro-` is a satellite argument independent of `la-`. Tools are never agents in Tonesu. When the instrument is named but the agent is not, the `ro-` + passive construction is available without any `la-`. (S562)

**Finding 4: Topic-frame passivization is available.** `{patient-NP} : ka-{predicate}  ti-de` = topicalized patient + passive predicate comment. The `lo-` is not used on the topic NP — the `:` frame hosts it outside clause-internal argument structure. Pattern 3 ellipsis licenses the patient drop from the comment clause. (S563)

**Finding 5: The emergence form `lo-X  be` is the Genesis / creation-fiat register.** No agent, no `ka`, untensed. Jussive / present / habitual readings are structurally identical; context disambiguates. This is the Tonesu counterpart of Hebrew jussive יְהִי ("let there be"). Distinct from both the intentional passive (`lo-X  ka-be  ti-de`) and the active divine creation (`la-X  ka-be  lo-Y`). (S566–S567)

**Finding 6: "It is written that X" is structurally active in Tonesu (containment predicate).** The form `la-{document}  ko  {X}` = "the document contains X" is active, with the text as container-agent occupying `la-`. There is no agentless equivalent for archival-passive constructions; the document is always the `la-` agent of the containment event. Scripture-to-Tonesu translation always uses this form. (S565)

**Recommendation: Formalize the four-form passive typology at spec/grammar.md `§ Agentless and Passive Clauses`.** No new particle is needed — the full typology arises from existing resources (`ka` presence/absence, `ro-`, `lo-X` frame, `be` vs `de`). Close the grammar TODO.

---

## Medical Differential Diagnosis Consultation (S569–S578) — Batch: MED-001

**Purpose (OQ-COR-001):** Second qualifying attestation test for `ke`. The first qualifying attestation was S545 (DEB-001-G) in a sustained philosophical debate, Round 3, when B's denial became informationally stale. The gap: `ke` is claimed to be appropriate whenever re-performing `no —` would pull the conversation backward without adding new information. One qualifying attestation is insufficient for admission (threshold: 3/3). This batch tests a different register — a formal medical differential diagnosis consultation — to confirm that the information-freshness rule generalizes across registers, not just heated philosophical debate.

**Scenario:** Two senior clinicians — A (attending physician, proposes thermal hypothesis) and B (consulting specialist, proposes biological-signal hypothesis) — are reviewing a patient's acute deterioration before a case committee. Both have presented evidence over two rounds. By Round 3, A appeals to the canonical diagnostic record (`to-su`). For B at that point, re-stating `no —` would perform the same denial a third time. The room already knows B rejects the thermal hypothesis. `ke` is the right form.

**Register note:** Medical differential diagnosis is a structurally brutal context for this test because:
1. Both speakers are technically precise — loose language is professionally costly.
2. The committee is listening — conversational waste (re-performing a known position) signals poor argumentation.
3. The causal stakes are high — every word is accountable.

**Vocabulary (all transparent composites; no new registry entries):**
| Form | Composition | Gloss |
|------|-------------|-------|
| `se-ka-li` | perception + action + person | diagnostician / clinician (one who acts through perceptual investigation) |
| `ha-be` | heat + growth | fever / rising temperature |
| `si-zo` | signal + living | biological signal |
| `si-zo-be` | signal + living + growth | escalating biological signal / infection cascade |
| `ko-su` | containment + structure | organ / internal structure |
| `zo-li` | living + person | patient (biological person) |
| `to-su` | knowledge + structure | established knowledge / canonical record / the doctrine |

---

**S569 — A's opening claim: "The fever caused the patient's deterioration."** *(MED-001-A)*

```
go ha-be  lo-zo-li  de  ti-de
```

**Notes:** A's diagnostic hypothesis. Causal frame: `go ha-be` = "caused by heat-increase"; `lo-zo-li de ti-de` = "the patient deteriorated." A asserts a thermal causal chain as the primary mechanism. No epistemic hedge — A is putting forward a direct causal reading from observation. **Round 1 opening.**

---

**S570 — B rejects: Round 1, denial is fresh.** *(MED-001-B)*

```
no — go si-zo  lo-zo-li  de  ti-de
```

**Notes:** `no —` is correct here. B's denial of the thermal hypothesis is new information in this exchange — A has not heard it before, and the committee has not heard it before. B replaces A's causal chain with a competing one: `go si-zo` = "caused by biological signal" rather than thermal cause. This is the correction move: deny + replace. The `—` (prosodic suspension) carries the weight of A's discarded claim before B's replacement; same structure as S535–S568 range. **`no —` adequate: denial is informationally fresh. MED-001 round count: 1.**

---

**S571 — A escalates with perceptual evidence.** *(MED-001-C)*

```
ya, la-mi  se  lo-ha-be ; go ha-be  lo-ko-su  de  ti-de
```

**Notes:** A brings new material: (1) personal observation — `la-mi se lo-ha-be` = "I perceived the fever" — grounding the thermal claim in direct sensory evidence; (2) extends the causal chain from patient-level to organ-level: `go ha-be  lo-ko-su  de  ti-de` = "by the fever, the organ deteriorated." The `ya` marks this as the crux A wants the committee to register. The `;` connects the perceptual grounding to the causal extension: "I saw it, and here is what it caused." **A has raised the evidential bar and extended the scope of the thermal claim. B must respond to new content. Round 2.**

---

**S572 — B counters with perceptual redirect: Round 2, `no —` still adequate.** *(MED-001-D)*

```
no — la-tu  se  lo-si-zo-be ; go si-zo-be  lo-ko-su  de  ti-de
```

**Notes:** B's Round 2 response. `no —` is still adequate here because A introduced new evidence (S571) — B's counter must respond to it. The form: `la-tu se lo-si-zo-be` = "you [A] are perceiving the biological signal escalation [and misattributing it to thermal cause]" — B redirects A's perceptual report: you saw a signal cascade, not a fever effect; `go si-zo-be  lo-ko-su  de  ti-de` = "the organ deteriorated because of the biological signal escalation." B's denial is new at S572 because it specifically addresses A's perceptual evidence and extends B's own causal chain to the organ level. **`no —` adequate: A escalated with new evidence; B's counter is informative. MED-001 round count: 2.**

---

**S573 — A's Round 3 structural appeal: "The canonical record says thermal cause."** *(MED-001-E)*

```
ya, la-to-su  si  {go ha-be  lo-ko-su  de}
```

**Notes:** A's strongest move. Instead of further personal evidence, A appeals to `to-su` (established knowledge / the canonical diagnostic record). `la-to-su si {…}` = "established knowledge signals [the proposition that…]." The embedded clause `{go ha-be  lo-ko-su  de}` = "by thermal cause, the organ deteriorated" — the canonical record is on the thermal side. This is a structural appeal: A is now claiming that the thermal hypothesis does not need new defense — it is already in the record. For B at this point: the thermal hypothesis has been asserted (Round 1), backed by perceptual evidence (Round 2), and is now presented as institutionally established (Round 3). A third denial from B would re-engage a premise that the committee has been through twice. The information to convey is not "I still reject the thermal hypothesis" — the committee knows that. The information is: "here is the alternative evidence, here is the causal chain." **Round 3 trigger condition established.**

---

**S574 — B's stale form: what `no —` would produce.** *(MED-001-F)*

```
no — go si-zo-be  lo-ko-su  de  ti-de
```

**Notes:** DIAGNOSTIC. This is the form B would produce if following the Round 1–2 correction pattern mechanically. The content is identical to B's prior challenges (S570, S572). The denial `no —` re-voices a rejection of the thermal hypothesis that is already encoded in the debate context — A knows B rejects it; the committee knows B rejects it; there is no new informational content in re-performing the denial. The sentence is not *wrong* — it is grammatically correct, and `no —` still blocks the thermal claim — but it is a missed opportunity and a waste of the committee's inference budget. It also risks reading as B having run out of new arguments. **DIAGNOSTIC (stale form): `no —` is informationally redundant at Round 3 when the denial has been performed twice with no new evidence from A's side.**

---

**S575 — B's `ke` form: second qualifying attestation.** *(MED-001-G)*

```
ke, la-mi  se  lo-si-zo-be ; go si-zo-be  lo-ko-su  de  ti-de
```

**Notes:** `ke` is the correct form here. The denial of the thermal hypothesis is implied — the committee already holds it as B's established position. B does not need to re-perform it. Instead `ke` signals: "setting that aside, here is my affirmative position." The content then delivers: `la-mi se lo-si-zo-be` = "I perceive the biological signal escalation" — a new perceptual claim that directly counters A's `la-to-su si {…}` (S573) at the evidence level; `go si-zo-be  lo-ko-su  de  ti-de` = "the organ deteriorated because of signal escalation" — the affirmative causal chain, advanced without re-litigating the prior denial. The shift from `no —` to `ke` encodes a real semantic difference in the discourse: B is no longer correcting A, B is running the argument forward. **OQ-COR-001: second qualifying attestation. `ke` is the precise form at Round 3 when the denial is informationally stale. Corpus pressure: 2/3.**

---

**S576 — `ke!` in the heated version.** *(MED-001-H)*

```
ke! la-mi  se  lo-si-zo-be ; go si-zo-be  lo-ko-su  de  ti-de
```

**Notes:** Same content as S575, added force marker `!`. In a heated committee room where A has just appealed to the canonical record — "the doctrine is on my side" — B's exasperation at the institutional appeal may push the register. `ke!` = forceful implicit denial + advancement, without the re-performance. The `!` here is professional anger (analogous to COR-001 `ke!`, S547 in DEB-001), not theatrical. **`ke!` in clinical-professional register: attested.**

---

**S577 — Contrast: `ya` alone does not substitute for `ke`.** *(MED-001-I)*

```
ya, la-mi  se  lo-si-zo-be ; go si-zo-be  lo-ko-su  de  ti-de
```

**Notes:** Testing whether `ya` (attention-signal) can do the work of `ke` (pivot particle) in this position. `ya, [clause]` = "attend to this claim." It directs the committee's attention to B's evidence but **does not** encode the pivot past A's prior premise. The difference is subtle but real: `ya` says "look here"; `ke` says "setting the prior exchange aside, here is my position." In context, `ya` alone would give B's evidence but would leave the prior denial question open — the committee might hear it as a new supporting argument rather than as a pivot that supersedes the round-3 re-denial. In a high-inference context (medical committee — all technically literate), `ya` alone may carry the pragmatic load through implicature; in a less inferentially rich context (general audience, transcript reading without real-time updating), it would not. `ke` is the precise form; `ya` is pragmatically close but semantically weaker at this function. **`ya` does not substitute for `ke` in the pivot position: distinction confirmed.**

---

**S578 — `ya, ke,` stacking test.** *(MED-001-J)*

```
ya, ke, la-mi  se  lo-si-zo-be ; go si-zo-be  lo-ko-su  de  ti-de
```

**Notes:** Tests whether `ya` and `ke` stack as clause-initial scope operators. Compare to the established stack `ya, ru-fe, [clause]` (S558). The parallel: `ya` (pragmatic outer scope: "attend") + `ke` (discourse pivot: "setting prior aside") + content. Does the stack hold? Order test: `ya` must be outermost — "attend to [the pivot + claim]"; `ke` operates inside `ya`'s scope — "the thing to attend to is: a pivot past the prior exchange + B's affirmative position." The reverse stack `ke, ya, [clause]` would be: "pivot + [attend to claim]" — this is structurally backwards; you would pivot before directing the room's attention, which loses the rhetorical value of the pivot. **`ya, ke,` stacks cleanly in the order `ya > ke > clause`,** mirroring `ya > ru-fe > clause`. The two stack differently in mechanism: `ru-fe` is a semantic scope marker (restricts the proposition's truth domain); `ke` is a discourse operator (positions the clause relative to prior exchange). Both take `ya` as their outer pragmatic wrapper without interference. **Stacking confirmed. `ya, ke, [clause]` = "attend: {setting prior aside} [affirmative claim]."**

---

## MED-001 Batch Summary

| Entry | Form | Verdict | Finding |
|-------|------|---------|---------|
| S569 (MED-001-A) | A: thermal hypothesis `go ha-be lo-zo-li de ti-de` | baseline | Round 1 opening; causal frame |
| S570 (MED-001-B) | B: `no — go si-zo lo-zo-li de ti-de` | adequate | Round 1; denial fresh; thermal hypothesis new to B |
| S571 (MED-001-C) | A: `ya, la-mi se lo-ha-be ; go ha-be lo-ko-su de ti-de` | adequate | A escalates with perceptual evidence + organ-level extension |
| S572 (MED-001-D) | B: `no — la-tu se lo-si-zo-be ; go si-zo-be lo-ko-su de ti-de` | adequate | Round 2; B's counter addresses new evidence; informative |
| S573 (MED-001-E) | A: `ya, la-to-su si {go ha-be lo-ko-su de}` | adequate | A appeals to canonical record; Round 3 trigger established |
| S574 (MED-001-F) | B: `no — go si-zo-be lo-ko-su de ti-de` (stale) | **stale** | Round 3; B re-performs known denial; no new information; denial already performed twice |
| S575 (MED-001-G) | B: `ke, la-mi se lo-si-zo-be ; go si-zo-be lo-ko-su de ti-de` | **`ke` preferred** | Round 3 pivot; denial implicit; B advances affirmative case; **OQ-COR-001: 2/3** |
| S576 (MED-001-H) | `ke!` heated version | attested | clinical-professional anger register; institutional-appeal trigger |
| S577 (MED-001-I) | `ya,` alone (contrast) | adequate but weaker | `ya` misses the pivot dimension; works by inference in rich context; `ke` is precise form |
| S578 (MED-001-J) | `ya, ke,` stack | attested | `ya > ke > clause` = attend + pivot + claim; parallel to `ya > ru-fe > clause`; discourse vs semantic scope |

---

### MED-001 Findings

**Finding 1: `ke` earns its second qualifying corpus attestation (S575, 2/3).** Medical differential diagnosis is a structurally demanding register — technical precision is professionally mandated, and re-performing a known denial signals poor argumentation. At Round 3 (S575), B has already denied the thermal hypothesis twice (S570, S572), with neither denial adding anything at Round 3. `ke` advances B's affirmative evidence and causal chain without re-opening the denial question. The staleness is exact: S574 (`no —`) and S572 are propositionally identical denial-and-replace sequences; S574 adds nothing by being performed a third time.

**Finding 2: The information-freshness rule holds across registers.** DEB-001 established the rule in heated philosophical debate (informal argumentative register). MED-001 confirms it in formal clinical consultation (high-stakes technical register). The threshold is not emotional intensity or register-formality — it is informational: `no —` is correct when the denial adds new information; `ke` is correct when the denial was already performed and its re-performance contributes nothing.

**Finding 3: `ya` does not substitute for `ke` in the pivot position (S577).** `ya` is an attention-signal — it scopes the committee's attention over the upcoming content but does not encode the pivot-past-stale-premise function. In high-inference contexts, `ya` may carry the pivot by implicature; in lower-inference contexts (transcripts, second-hand reporting, formal record) it would not. `ke` is the precise form; `ya` is a pragmatically adjacent but semantically weaker option.

**Finding 4: `ya, ke,` stacks cleanly in the order `ya > ke > clause` (S578).** Parallels the established `ya > ru-fe > clause` stack. Both take `ya` as an outer pragmatic wrapper without interference. The two inner operators differ in mechanism: `ru-fe` = semantic scope restriction (truth-domain narrowing); `ke` = discourse positioning (locates the clause relative to prior exchange). Stacking rule: outermost operator is the widest pragmatic scope; inner operators are semantically specific; content is innermost.

---

## Diplomatic Treaty Negotiation (S579–S588) — Batch: DIP-001

**Purpose (OQ-COR-001):** Third and final qualifying attestation for `ke`. Threshold for admission is 3 qualifying corpus sentences in multi-exchange dialogue where `no —` would produce informationally stale re-denial and `ke` is clearly the precise form. DEB-001 (S545) confirmed the rule in heated philosophical debate; MED-001 (S575) confirmed it in formal clinical consultation. DIP-001 tests a third structurally independent register: formal treaty negotiation between two delegations before a mediated session.

**Why diplomatic negotiation is the most demanding test:** In treaty negotiation, re-performing a known position without new content does not merely signal informational waste — it has a **bad-faith interpretation** available to the opposing party. A delegation that responds to Round 3 with the same `no —` it produced at Round 1 can be characterized as obstructing the process rather than engaging it. `ke` is not just more informative here; it is strategically and diplomatically necessary. An observer logging `no —` at Round 3 in the formal minutes writes: "Delegation B reiterated its objection." An observer logging `ke` writes: "Delegation B advanced its counter-position." These are different entries in the record. The stakes for the distinction are maximal.

**Scenario:** Two delegations negotiate the right over a shared resource territory (`ra-pa`) before a mediator. Delegation A holds that it has established treaty-based extraction rights. Delegation B holds that the rights vest in the shared commons entity, not in any single delegation. Both invoke the same treaty text (S581–S582) and then its canonical interpretive tradition (S583).

**Vocabulary (all transparent composites):**

| Form | Composition | Gloss |
|------|-------------|-------|
| `li-pu` | person + collective | delegation / political body (attested S564) |
| `pa-pu` | place + collective | the commons / shared-territory entity |
| `ra-pa` | energy/force + place | resource territory (the energy-bearing land) |
| `wi-fe` | will + boundary | right / rule / normative claim (W100; legal/institutional register) |
| `si-su` | signal + structure | written record / treaty text (attested S565) |
| `to-su` | knowledge + structure | canonical interpretive record / established doctrine (attested S573) |

---

**S579 — A's Round 1: "The delegation asserts rights over the resource territory."** *(DIP-001-A)*

```
la-li-pu  ne  wi-fe  lo-ra-pa
```

**Notes:** A's opening claim. `la-li-pu ne wi-fe lo-ra-pa` = "The delegation holds the willed boundary over the resource territory" = "The delegation has the rule/right over the resource territory." Type 2 attributive predication: `la-li-pu` (agent slot) + `ne` (copula) + `wi-fe` (property: normative claim) + `lo-ra-pa` (patient: resource territory). **`wi-fe` first direct-form attestation in rights/legal register.** Previous attestation (S183, MMP-001) used `wi-fe-su` (rule-as-institution); this sentence uses the bare compound as a claimed property of an agent. Round 1 opening.

---

**S580 — B's Round 1 denial: `no —` is fresh.** *(DIP-001-B)*

```
no — la-pa-pu  ne  wi-fe  lo-ra-pa
```

**Notes:** B's counter-claim replaces A's agent with `pa-pu` (the commons entity): "No — the commons holds the right over the resource territory." The denial is fresh: B's counter-position has not been stated yet, the mediator has not heard it, and A has not been confronted with it. `no —` is correct. The prosodic suspension carries A's claim before B's replacement, exactly as in the correction-form paradigm. **`no —` adequate: denial and counter-claim are both new. Round 1.**

---

**S581 — A's Round 2 escalation: appeal to treaty text.** *(DIP-001-C)*

```
ya, la-si-su  ko  {la-li-pu  ne  wi-fe  lo-ra-pa}  ti-de
```

**Notes:** A raises the evidential bar from assertion to documentary record. `la-si-su ko {…}` = "the treaty text contains [the proposition that…]." The `ti-de` marks the text as historical/existing. `ya` directs the session's attention to this evidence. New content: A is no longer asserting on authority; A is citing a text. B must now engage with the documentary record, not just with A's claim. **Round 2; `ya` in treaty-session attentional function.**

---

**S582 — B's Round 2 counter: `no —` still adequate.** *(DIP-001-D)*

```
no — la-si-su  ko  {la-pa-pu  ne  wi-fe  lo-ra-pa}  ti-de
```

**Notes:** B reads the same treaty differently. Same document (`la-si-su`), same structure, different embedded proposition: the treaty contains commons-right, not delegation-right. B's denial is still adequate at Round 2 because A introduced new evidence in S581 — the counter-interpretation of the treaty is new content that materially responds to A's escalation. `no —` correctly refuses A's documentary reading and substitutes B's. **`no —` adequate: A escalated with documentary evidence; B's counter-reading is informative. Round 2.**

---

**S583 — A's Round 3: appeal to canonical interpretive tradition.** *(DIP-001-E)*

```
ya, la-to-su  si  {la-li-pu  ne  wi-fe  lo-ra-pa}
```

**Notes:** A escalates past the treaty text to the canonical interpretive tradition. `la-to-su si {…}` = "established knowledge signals [the proposition that…]." This is not a new document — it is the claim that the correct reading of the treaty is already settled in the interpretive record; A is not arguing the text, A is citing the consensus of prior determinations. For B at this point: the delegation-rights claim has been asserted (Round 1), backed by the treaty text (Round 2), and is now presented as interpretively settled by the canonical tradition (Round 3). B has already denied the claim twice. A third bare `no —` would not engage A's actual Round 3 move — it would simply re-perform B's known position without countering the canonical-tradition appeal. **Round 3 trigger established.**

---

**S584 — B's stale form: what `no —` produces.** *(DIP-001-F)*

```
no — la-pa-pu  ne  wi-fe  lo-ra-pa
```

**Notes:** DIAGNOSTIC. This is the form B would produce at Round 3 if following the correction-pattern mechanically. Propositionally identical to S580 and S582. A has just invoked canonical interpretive tradition (`la-to-su si {…}`); B's response re-states the commons-rights claim without engaging the canonical-tradition appeal at all. The mediator receives: "B repeated its position." This has three practical costs: (1) B fails to counter A's actual move (the tradition appeal goes unanswered); (2) B may be characterized as non-cooperative — a stalling tactic rather than genuine engagement; (3) the session record logs an objection, not a counter-argument. The form is grammatically correct but pragmatically wasteful and, in this register, strategically self-defeating. **DIAGNOSTIC (stale form): Round 3 `no —` performs a known denial without addressing A's escalated claim; costs are informational, strategic, and documentary.**

---

**S585 — B's `ke` form: third qualifying attestation.** *(DIP-001-G)*

```
ke, la-pa-pu  ne  wi-fe  lo-ra-pa ; la-to-su  si  {pa-pu  ne  wi-fe}
```

**Notes:** `ke` is the correct and precise form. B's denial of the delegation-rights claim is implied and already encoded in the session record — re-performing it adds nothing. `ke` signals: "setting the prior exchange aside, here is my affirmative position." The content then does real work: `la-pa-pu ne wi-fe lo-ra-pa` = B's affirmative counter-claim (the commons holds the right); `;` = sequential connection; `la-to-su si {pa-pu ne wi-fe}` = "the canonical interpretive record signals: commons-right is established" — B directly counters A's Round 3 `la-to-su si {…}` (S583) by citing the same institutional instrument in favor of the commons reading. A invoked canonical tradition; B counter-invokes it. `ke` makes clear B is running the argument forward, not circling back. The session record logs: "Delegation B advanced counter-canonical position." **OQ-COR-001: third qualifying attestation. `ke` threshold met. Corpus pressure: 3/3.**

---

**S586 — The bad-faith dimension: why `no —` vs `ke` matters in treaty record.** *(DIP-001-H)*

**Notes:** In treaty negotiation, the formal session record distinguishes two types of delegational response: (1) a **lodged objection** — "Delegation B reiterated its rejection of Delegation A's position" — which is what `no — [counter-claim]` at Round 3 produces; and (2) a **submitted counter-position** — "Delegation B advanced its canonical counter-argument" — which is what `ke, [counter-claim]` produces. The distinction is not merely stylistic. A lodged objection is a veto move that pauses the process; a submitted counter-position is an argumentative move that advances the process. In negotiations that are designed to reach agreement rather than entrench opposition, the `ke` form is not just more precise — it is the form that signals good faith. The diplomatic function of `ke` is therefore: "I am not obstructing; I am advancing the counter-argument." This is the maximum-load version of the information-freshness rule: what would be informational waste in a philosophical debate becomes a bad-faith signal in a treaty context.

---

**S587 — Written formal register: `ke` in treaty-record notation.** *(DIP-001-I)*

```
ke, la-pa-pu  ne  wi-fe  lo-ra-pa ; la-to-su  si  {pa-pu  ne  wi-fe}
```

**Notes:** Same form as S585, considered now as a written submission rather than spoken utterance. In formal treaty record, `ke` would appear at the head of a counter-position filing: the written form is identical to the spoken form, as expected under Tonesu's spoken/written parity. The written record renders the session faithfully. The `ke` form in written submissions also prevents the ambiguity of `no — [claim]` in transcript: in transcript, `no —` followed by a claim can be parsed as either (a) correction of a prior misstatement or (b) institutional objection. `ke` is unambiguous in transcript: it is always a pivot-and-advance, never a simple denial. **Written-register function of `ke` confirmed; no new rule required; spoken and written forms are identical.**

---

## DIP-001 Batch Summary

| Entry | Form | Verdict | Finding |
|-------|------|---------|---------|
| S579 (DIP-001-A) | A: `la-li-pu ne wi-fe lo-ra-pa` | baseline | Round 1 opening; `wi-fe` direct-form attestation in rights register |
| S580 (DIP-001-B) | B: `no — la-pa-pu ne wi-fe lo-ra-pa` | adequate | Round 1; counter-claim fresh; `no —` correct |
| S581 (DIP-001-C) | A: `ya, la-si-su ko {…} ti-de` | adequate | Round 2 escalation; treaty-text citation; new evidential content |
| S582 (DIP-001-D) | B: `no — la-si-su ko {…} ti-de` | adequate | Round 2 counter; treaty counter-reading; addresses new content |
| S583 (DIP-001-E) | A: `ya, la-to-su si {la-li-pu ne wi-fe lo-ra-pa}` | adequate | Round 3 trigger; canonical-tradition appeal; escalation complete |
| S584 (DIP-001-F) | B: `no — la-pa-pu ne wi-fe lo-ra-pa` (stale) | **stale** | Round 3; re-performs known denial; A's canonical-tradition appeal unanswered |
| S585 (DIP-001-G) | B: `ke, la-pa-pu ne wi-fe lo-ra-pa ; la-to-su si {pa-pu ne wi-fe}` | **`ke` preferred** | Round 3 pivot; advances affirmative counter-canonical position; **OQ-COR-001: 3/3** |
| S586 (DIP-001-H) | bad-faith dimension | analytical | `no —` = lodged objection; `ke` = submitted counter-position; distinct documentary function |
| S587 (DIP-001-I) | written-record form | attested | `ke` in treaty-record notation; written/spoken parity; no transcript ambiguity |
| S588 (DIP-001-J) | — | — | [see recommendation below] |

---

### DIP-001 Findings

**Finding 1: `ke` earns its third qualifying corpus attestation (S585, 3/3). Admission threshold met.** Three independent registers across three distinct corpus batches: heated philosophical debate (DEB-001, S545), formal clinical consultation (MED-001, S575), diplomatic treaty negotiation (DIP-001, S585). In each case the structural conditions are identical: a prior denial has been performed and is contextually encoded; `no —` at this point would produce a re-denial with no new informational content; `ke` pivots to the affirmative position without re-performing the known denial. The information-freshness rule holds across all three registers.

**Finding 2: The diplomatic register reveals the maximum-load version of the `ke` function.** In treaty negotiation, the `no —` / `ke` distinction maps onto a functionally significant documentary difference: lodged objection vs submitted counter-position. `ke` signals argumentative good faith in a context where repetitive denial can be characterized as obstruction. This is stronger than informational efficiency: `ke` is the form required to advance a negotiation rather than entrench it.

**Finding 3: `wi-fe` (W100) attested directly in a rights-claim predicate (S579, S580, S582, S585).** Four direct uses as the claimed normative property in `la-X ne wi-fe lo-Y` ("X holds the right over Y"). Prior use S183 used `wi-fe-su` (derived institution form). DIP-001 establishes `wi-fe` bare as a predicate in rights/legal register. Recommend updating W100 status from pending to active.

**Recommendation: Admit `ke` (G032) as the canonical pivot particle.** Three qualifying attestations across three structurally independent registers. Form: CV, `ke`. Definition: discourse pivot marker — signals that the current speaker is setting aside a prior exchange and advancing an affirmative position; the denial of whatever was asserted in the prior exchange is implied without re-performance. Syntax: clause-initial, followed by `,`; same positional slot as `ya` and `ru-fe`. Written solid: `ke,` before the advancing clause. Stacks with `ya` as `ya, ke, [clause]` = "attend: {pivot} [affirmative claim]."

---

## Star Wars — The Jedi Code and the Sith Code (S588–S598)

*Batch purpose (STW-001/STW-002): translation of both canonical Star Wars ethical codes. Tests bi-clausal parallel `/`, scope-derived `ara` as the Force, `ru-fe` exclusive scope, `go`-causal chains, and agency shift. Full analysis in `corpus/translations/Literature/star-wars-codes.md`.*

*New compounds attested this batch: `ne-no-ra` (W171, peace), `fa-wi-ra` (W172, passion), `fa-su` (W173, serenity), `su-ne` (W174, harmony), `wi-du` (W175, victory), `ko-ne-mu` (W176, chain/shackle), `wi-ra` (W177, directed power), `de-zo` (W178, death/dying).*

---

**S588 — Jedi Code, line 1 — "There is no emotion, there is peace."** *(STW-001-A)*

```
no-fa  ne  /  ne-no-ra  ne
```

**Written:** `nofa ne / nenora ne`

**Natural reading:** No raw affect / peaceful-relation prevails.

**Notes:** `/` bi-clausal parallel. `no-fa` = negation of affective substrate = no raw reactive emotion. `ne-no-ra` = relation-without-force = peace (W171, first attestation). The Jedi Code's subtle claim: peace is not affect-absence, it is the presence of force-free connection. Replace reactive affect with bonds that carry no violence.

---

**S589 — Jedi Code, line 2 — "There is no ignorance, there is knowledge."** *(STW-001-B)*

```
no-to  ne  /  to  ne
```

**Written:** `noto ne / to ne`

**Natural reading:** No knowledge-absence / knowledge prevails.

**Notes:** Cleanest line. `no-to` = absence of conceptual pattern = ignorance (composable). `to` = knowledge (primitive). Near-tautological in the best sense: `no-{no-to}` / `to`. No new vocabulary required.

---

**S590 — Jedi Code, line 3 — "There is no passion, there is serenity."** *(STW-001-C)*

```
no-fa-wi-ra  ne  /  fa-su  ne
```

**Written:** `nofawira ne / fasu ne`

**Natural reading:** No driven-forceful-affect / structured-affect prevails.

**Notes:** First attestations of `fa-wi-ra` (W172, passion = affect-will-force) and `fa-su` (W173, serenity = affect-structure). The negation reveals what passion IS: affect hijacked by will-direction and force. Serenity is the alternative: affect that has found structure without drive. Extends the `fa-[X]` compound family.

---

**S591 — Jedi Code, line 4 — "There is no chaos, there is harmony."** *(STW-001-D)*

```
no-su  ne  /  su-ne  ne
```

**Written:** `nosu ne / sune ne`

**Natural reading:** No structure / structure-of-connection prevails.

**Notes:** `no-su` = absence of structure = chaos. `su-ne` = structure-of-relation = harmony (W174, first attestation). The parallel reveals the definitions: chaos is total structural absence; harmony is specifically the structural ordering of relational bonds — not just any structure but `su` in the `ne` domain.

---

**S592 — Jedi Code, line 5 — "There is no death, there is the Force."** *(STW-001-E)*

```
no-de-zo  ne  /  ara  ne
```

**Written:** `nodezo ne / ara ne`

**Natural reading:** No organism-decrease / universal-energy prevails.

**Notes:** First explicit registration of `de-zo` (W178, death = organism-decrease, non-agentive). First corpus attestation of `ara` (scope-derivation: `a-` + `ra` = abstract/universal energy = the Force). The Force is what remains when de-zo is negated — not life (`zo-ra`, W117) but the encompassing universal-energy field. `ara ne` — the Jedi Code ends with the one affirmation that requires no prefix.

---

**S593 — Sith Code, line 1 — "Peace is a lie, there is only passion."** *(STW-002-A)*

```
ne-no-ra  ne  to-fe-ka  /  ru-fe,  fa-wi-ra  ne
```

**Written:** `nenora ne tofeka / rufe, fawira ne`

**Natural reading:** Peaceful-relation is deliberate-mislabeling / only: driven-affect prevails.

**Notes:** Direct structural inversion of S588: both sentences contain `ne-no-ra ne`, but here it is attributed `to-fe-ka` (W029, deliberate epistemic mislabeling = a lie). The Sith don't claim peace is merely absent — they claim it is an actively maintained deception. `ru-fe, fa-wi-ra ne` = only passion prevails (`ru-fe` exclusive scope particle). The two codes are grammatically locked by the shared phrase `ne-no-ra ne` carrying opposite truth-values.

---

**S594 — Sith Code, line 2 — "Through passion, I gain strength."** *(STW-002-B)*

```
go {fa-wi-ra},  la-mi  ra-be
```

**Written:** `go {fawira}, lami rabe`

**Natural reading:** [Cause: passion] → I grow in force.

**Notes:** First link of the Sith causal chain. `go {fa-wi-ra}` = by means of passion (necessary causal mechanism — `go`, not `;`; the Sith assert ontological production, not coincidence). `la-mi ra-be` = I grow in force = I gain strength. `ra-be` = force-increasing (composable).

---

**S595 — Sith Code, line 3 — "Through strength, I gain power."** *(STW-002-C)*

```
go {ra},  la-mi  wi-ra-be
```

**Written:** `go {ra}, lami wirabe`

**Natural reading:** [Cause: force] → I grow in directed-power.

**Notes:** `go {ra}` = by means of force/strength. `la-mi wi-ra-be` = I grow in directed-power. `wi-ra-be` = `wi-ra` (W177, will-force = directed power) + `be` (increasing). Escalation: `ra` (raw capacity) → `wi-ra` (capacity organized by intention). First attestation of `wi-ra` (W177).

---

**S596 — Sith Code, line 4 — "Through power, I gain victory."** *(STW-002-D)*

```
go {wi-ra},  la-mi  wi-du-be
```

**Written:** `go {wira}, lami widube`

**Natural reading:** [Cause: directed-power] → I grow in willed-achievement.

**Notes:** `go {wi-ra}` = by means of directed power. `la-mi wi-du-be` = I grow in victory. `wi-du-be` = `wi-du` (W175, victory = will-result) + `be` (increasing). Third escalation step: directed force achieves its aimed-at outcome. All three causal lines use `la-mi` as explicit agent. First attestation of `wi-du` (W175).

---

**S597 — Sith Code, line 5 — "Through victory, my chains are broken."** *(STW-002-E)*

```
go {wi-du},  lo-mi  ko-ne-mu  de-ki
```

**Written:** `go {widu}, lomi konemu deki`

**Natural reading:** [Cause: victory] → my chains enter breaking.

**Notes:** Agency shift: `la-mi` → `lo-mi`. `lo-mi ko-ne-mu` = the chains that constrain me (patient-frame: what affects me). `de-ki` = decrease-enter = enter the state of breaking. The chains break as a *causal consequence* (`go {wi-du}`), not as a deliberate act by the speaker. First attestation of `ko-ne-mu` (W176, chain/shackle = containment-connection-artifact). The speaker is now acted upon, not acting.

---

**S598 — Sith Code, line 6 — "The Force shall free me."** *(STW-002-F)*

```
la-ara  lo-mi  ka-pa-ki
```

**Written:** `laara lomi kapaki`

**Natural reading:** The Force liberates me.

**Notes:** `la-ara` = the Force (universal-energy `ara`) as grammatical agent (`la-`). `lo-mi` = me as patient. `ka-pa-ki` = liberation act (deliberate action producing place-motion = movement out of containment; EXO-001). First attestation of `ara` as a grammatical agent. The speaker is `lo-mi` (patient) throughout S597–S598, completing the agency inversion from the `la-mi`-driven causal chain (S594–S596). Phonological note: `la-ara` → written `laara`; both syllables begin with consonants (`l-`, `r-`), satisfying Parse Invariant 1.

---

## STW-001 / STW-002 Batch Summary

| Entry | Written form | Key finding |
|-------|-------------|-------------|
| S588 (STW-001-A) | `nofa ne / nenora ne` | Peace = force-free relation; `ne-no-ra` W171 |
| S589 (STW-001-B) | `noto ne / to ne` | Primitive-only; near-tautological |
| S590 (STW-001-C) | `nofawira ne / fasu ne` | Passion W172 / serenity W173; `fa-[X]` family extended |
| S591 (STW-001-D) | `nosu ne / sune ne` | Chaos = `no-su`; harmony W174 |
| S592 (STW-001-E) | `nodezo ne / ara ne` | Death W178; Force = `ara`; first `ara` attestation |
| S593 (STW-002-A) | `nenora ne tofeka / rufe, fawira ne` | Peace as deliberate lie; direct S588-inversion |
| S594 (STW-002-B) | `go {fawira}, lami rabe` | `go`-causal chain starts; passion → strength |
| S595 (STW-002-C) | `go {ra}, lami wirabe` | Strength → directed-power W177 |
| S596 (STW-002-D) | `go {wira}, lami widube` | Power → victory W175 |
| S597 (STW-002-E) | `go {widu}, lomi konemu deki` | Agency shift; chains W176 break as causal result |
| S598 (STW-002-F) | `laara lomi kapaki` | `la-ara` as agent; Force liberates; `la-mi` → `lo-mi` inversion complete |

## D&D — The Eight Schools of Magic (S599–S608)

*Batch purpose (DND-001): translation of the eight D&D schools of magic. Tests compound vocabulary formation for abstract academic categories, property-attribution syntax via `ne`, and the bi-clausal parallel `/` as a contrast frame. Full analysis in `corpus/translations/Literature/dnd-schools-of-magic.md`.*

*New compounds attested this batch: `wi-ra-su` (W179, magic), `ko-fe-ki` (W180, abjuration), `pa-be-ki` (W181, conjuration), `to-se-ki` (W182, divination), `wi-fa-ki` (W183, enchantment), `ra-be-ki` (W184, evocation), `ge-se-ki` (W185, illusion), `de-zo-ki` (W186, necromancy), `ge-ki` (W187, transmutation).*

---

**S599 — Magic as systematic discipline.** *(DND-001-A)*

```
wi-ra-su  ne  to-su  lo-wi-ra
```

**Written:** `wirasu ne tosu lowira`

**Natural reading:** The magical arts form a systematic discipline of directed power.

**Notes:** Framing sentence for the batch. `wi-ra-su` (W179) introduced here: `wi-(ra-su)` = will of [force-structure] = the disciplined, intentional practice of structured force. `to-su` = systematic/structured knowledge system. `lo-wi-ra` = directed power (W177) as patient = what magic is a discipline *of*. The sentence defines magic as an academic genus before the eight species are differentiated.

---

**S600 — Abjuration.** *(DND-001-B)*

```
ko-fe-ki  ne  wi-ra-su  lo-ko-fe
```

**Written:** `kofeki ne wirasu lokofé`

**Written:** `kofeki ne wirasu kofe`

**Natural reading:** Abjuration is the magic of creating and maintaining containing limits.

**Notes:** `ko-fe-ki` (W180): `ko-(fe-ki)` = containing of [limit-change] = the art of manipulating protective limits. `lo-ko-fe` = containing-limit as patient = what abjuration operates on. Wards, shields, banishments all involve creating or enforcing a containing boundary. `ko` (enclosing/containing) is the domain root.

---

**S601 — Conjuration.** *(DND-001-C)*

```
pa-be-ki  ne  wi-ra-su  lo-be-pa
```

**Written:** `pabeki ne wirasu lobepa`

**Natural reading:** Conjuration is the magic of making things emerge into new places.

**Notes:** `pa-be-ki` (W181): `pa-(be-ki)` = spatial [emergence-change] = the art of making things appear in space. `lo-be-pa` = spatial-emergence as patient = what conjuration produces. Covers summoning, teleportation, and creation of matter. `pa` (space/presence) as domain root captures the spatial character of conjuration.

---

**S602 — Divination.** *(DND-001-D)*

```
to-se-ki  ne  wi-ra-su  lo-so-to
```

**Written:** `toseki ne wirasu losoto`

**Natural reading:** Divination is the magic of perception-knowledge.

**Notes:** `to-se-ki` (W182): `to-(se-ki)` = pattern [perception-change] = the art of transforming perception to access hidden knowledge. The patient `lo-so-to` uses `so-to` (perception-knowledge, compositional reading of `se-to` with vowel harmony — note: formally `se-to` would be cleaner; `so-to` is the slot patient for this batch). Divination is framed as *active*: you transform (ki) perception (se) to gain knowledge (to). Not passive seeing but intentional perceptual work.

---

**S603 — Enchantment.** *(DND-001-E)*

```
wi-fa-ki  ne  wi-ra-su  lo-fa-wi
```

**Written:** `wifaki ne wirasu lofawi`

**Natural reading:** Enchantment is the magic of altering the affect-will.

**Notes:** `wi-fa-ki` (W183): `wi-(fa-ki)` = willed [affect-shift] = intentional deployment of affect-register manipulation. Builds directly on `fa-ki` (W093, affect-register transformation). Patient `lo-fa-wi` = affect-will complex = the combined emotional-volitional state of the enchanted subject. Charm, dominate, suggestion all operate on `fa-wi` (what-you-feel + what-you-want).

---

**S604 — Evocation.** *(DND-001-F)*

```
ra-be-ki  ne  wi-ra-su  lo-ra-be
```

**Written:** `rabeki ne wirasu lorabe`

**Natural reading:** Evocation is the magic of channeling and releasing raw force.

**Notes:** `ra-be-ki` (W184): `ra-(be-ki)` = force [manifestation-change] = the art of directing how force manifests. Careful parse avoids `ra-ki` (W038, storm). Patient `lo-ra-be` = force-emergence = the manifest force product of evocation. Fireball, lightning bolt, healing — all involve taking `ra` (raw energy) and shaping its `be` (emergence/manifestation). Structural polar opposite of illusion: evocation acts on `ra` (real); illusion acts on `ge-se` (apparent).

---

**S605 — Illusion.** *(DND-001-G)*

```
ge-se-ki  ne  wi-ra-su  lo-ge-se
```

**Written:** `geseki ne wirasu logese`

**Natural reading:** Illusion is the magic of crafting how things appear.

**Notes:** `ge-se-ki` (W185): `ge-(se-ki)` = quality [perception-change] = the art of altering how qualities are perceived. Patient `lo-ge-se` = quality-of-perception = apparent properties (not inherent ones). Illusion magic does not change what IS; it changes how things APPEAR. Contrast with transmutation `ge-ki` (W187): illusion alters `ge` through `se` (perception); transmutation alters `ge` directly. Both are `ge`-rooted schools.

---

**S606 — Necromancy.** *(DND-001-H)*

```
de-zo-ki  ne  wi-ra-su  lo-de-zo
```

**Written:** `dezoki ne wirasu lodezo`

**Natural reading:** Necromancy is the magic of transformation through death.

**Notes:** `de-zo-ki` (W186): `de-(zo-ki)` = death-threshold [organism-change] = the art of transforming living things across or through the death state. Builds on `de-zo` (W178, dying/death-event). The distinction is important: `de-zo` (W178) is what happens (the event); `de-zo-ki` is the art practiced *in that domain*. Patient `lo-de-zo` = the death-event itself = the domain necromancy operates on. Animate dead, cause disease, drain life — all work at the `de-zo` boundary.

---

**S607 — Transmutation.** *(DND-001-I)*

```
ge-ki  ne  wi-ra-su  lo-ge
```

**Written:** `geki ne wirasu loge`

**Natural reading:** Transmutation is the magic of altering fundamental properties.

**Notes:** `ge-ki` (W187): `ge` + `ki` = quality-change. The only 2-root school compound — all others (W180-W186) are 3-root. The structural simplicity is appropriate: transmutation is the most direct school, operating on `ge` (fundamental property) without spatial, perceptual, or force mediation. Patient `lo-ge` = property/quality itself = what transmutation acts on. Parallel with illusion `ge-se-ki`: illusion changes `ge` through `se`-mediation; transmutation changes `ge` directly.

---

**S608 — Contrast: Evocation vs Illusion.** *(DND-001-J)*

```
la-ra-be-ki  be  lo-ra  /  la-ge-se-ki  be  lo-ge-se
```

**Written:** `larabeki be lora / lageseki be logese`

**Natural reading:** Evocation generates real force; Illusion generates quality-of-perception.

**Notes:** Bi-clausal parallel `/` used as contrast frame (not antithetical but structural opposition). `be` = emergent-process verb. Both schools use `be` as the predicate: both "bring forth" something. But evocation brings forth `ra` (real force/energy) while illusion brings forth `ge-se` (quality-of-perception = apparent properties). The parallel structure makes the ontological distinction maximally explicit: one produces actuality, the other produces appearance. Connects to the Sith Code cross-batch finding: `go {ra}, la-mi wi-ra-be` (S595) = through force, I grow in directed-power. The Force `ara` is the universal substrate; the schools of magic are differentiated modes of directing that substrate.

---

## DND-001 Batch Summary

| Entry | Written form | School | Key finding |
|-------|-------------|--------|-------------|
| S599 (DND-001-A) | `wirasu ne tosu lowira` | Frame | Magic as systematic discipline of directed power; W179 |
| S600 (DND-001-B) | `kofeki ne wirasu kofe` | Abjuration | Containing-limit-change; W180 |
| S601 (DND-001-C) | `pabeki ne wirasu lobepa` | Conjuration | Spatial emergence-change; W181 |
| S602 (DND-001-D) | `toseki ne wirasu losoto` | Divination | Divination is ACTIVE transformation, not passive seeing; W182 |
| S603 (DND-001-E) | `wifaki ne wirasu lofawi` | Enchantment | Willful affect-shift; builds on fa-ki (W093); W183 |
| S604 (DND-001-F) | `rabeki ne wirasu lorabe` | Evocation | Force-manifestation; avoids ra-ki (W038); W184 |
| S605 (DND-001-G) | `geseki ne wirasu logese` | Illusion | Quality-of-perception; polar contrast to evocation; W185 |
| S606 (DND-001-H) | `dezoki ne wirasu lodezo` | Necromancy | Death-threshold organism-change; builds on de-zo (W178); W186 |
| S607 (DND-001-I) | `geki ne wirasu loge` | Transmutation | 2-root; most direct; pure property-change; W187 |
| S608 (DND-001-J) | `larabeki be lora / lageseki be logese` | Contrast | Force vs appearance; ontological distinction via parallel `/` |

---

### DND-001 Findings

**Finding 1: All eight D&D schools reduce to compositional combinations of 12 primitives.** `ko`, `fe`, `pa`, `be`, `to`, `se`, `wi`, `fa`, `ra`, `ge`, `de`, `zo` — plus the shared change-root `ki`. No new primitive is required. The D&D school taxonomy is fully expressible in Tonesu without expanding the closed primitive set. This is a positive compositional stress test.

**Finding 2: The `-ki` school suffix encodes a genuine structural insight.** D&D magic is, at root, a taxonomy of *change-arts* — each school is a specific domain in which intentional transformation (`ki`) is applied. The shared `-ki` suffix (W180-W186) makes this explicit. The one exception (`ge-ki`, W187) uses the same suffix directly, making transmutation the most primitive: property-change, unmediated.

**Finding 3: `wi-fa-ki` (W183) establishes that affect-manipulation is available as a compound-head target.** Enchantment is `wi` applied to `fa-ki` (W093). This confirms that registered 2-root compounds can serve as valid compound heads in 3-root constructions. `wi-(fa-ki)` is not a new primitive — it is a deliberate layering of will (`wi`) onto a registered affect-shift system.

**Finding 4: The evocation/illusion polar contrast (S608) demonstrates the ontological depth of the `ge`/`ra` distinction.** Evocation (`ra-(be-ki)`) produces things that are real in the `ra`-sense: force, energy, causal power. Illusion (`ge-(se-ki)`) produces things that are real only in the `ge-se`-sense: apparent properties, perceptual manipulations. The parallel `/` frame in S608 makes this ontological split grammatically visible.

**Finding 5: Cross-batch connection — D&D magic and the Force.** `ara` (universal energy, scope-derived form first attested STW-001) is the substrate from which all schools of magic draw. `wi-ra-su` (magic as directed-force-discipline) builds on `wi-ra` (W177, directed power) which was attested in the Sith Code (S595). The schools of D&D magic are subspecies of `wi-ra-su`; the Jedi and Sith practices are subspecies of `wi-ra-su` operating under different ethical commitments.

---

## D&D — The Nine Alignments (S609–S618)

*Batch purpose (DND-002): translation of the D&D 3×3 alignment grid. Tests two-axis moral characterization via the bi-clausal parallel `/`, the adequacy of `wi-` as the character-disposition root, the "neutral is not negation" design problem, and retroactive alignment mapping of STW characters. Full analysis in `corpus/translations/Literature/dnd-alignments.md`.*

*New compounds attested this batch: `wi-su` (W188, lawful), `wi-no-su` (W189, chaotic), `wi-vo` (W190, good), `wi-de` (W191, evil — first standalone attestation), `wi-su-fe` (W192, law-neutral), `wi-vo-fe` (W193, ethics-neutral).*

---

**S609 — Alignment: two-axis framing.** *(DND-002-A)*

```
wi-li  ne  wi-su  /  wi-li  ne  wi-vo
```

**Written:** `wili ne wisu / wili ne wivo`

**Natural reading:** A person's will has a structure-dimension and a value-dimension.

**Notes:** Framing sentence. `wi-li` = will-of-a-person = an agent's dispositional character. The `/` parallel expresses simultaneous co-predication on two independent axes: will is characterized by its law-position (`ne wi-su`) AND by its ethics-position (`ne wi-vo`). The framing uses the LG combination (wi-su + wi-vo) as the paradigm case. Key structural finding: `/` here is NOT contrastive (as in S608) but co-attributive — both properties apply to the same subject simultaneously and independently.

---

**S610 — Lawful Good: Paladin.** *(DND-002-B)*

```
la-na-Paladin  ne  wi-su  /  ne  wi-vo
```

**Written:** `lanaPaladin ne wisu / ne wivo`

**Natural reading:** The Paladin's will is organized by structure and oriented toward value.

**Notes:** W188 + W190. Maximum on both axes. The Paladin keeps oaths (`wi-su`), protects the innocent (`wi-vo`). The most constrained and most demanding alignment: structure compels the good.

---

**S611 — Neutral Good: Cleric.** *(DND-002-C)*

```
la-na-Cleric  ne  wi-su-fe  /  ne  wi-vo
```

**Written:** `lanaCleric ne wisufe / ne wivo`

**Natural reading:** The Cleric's will operates at the structural limit and is oriented toward value.

**Notes:** W192 + W190. First attestation of `wi-su-fe` (W192). The Cleric pursues maximum good (`wi-vo`) without being bound by rigid structure (`wi-su-fe` = at the structural limit, not the extreme). Neutral Good is sometimes called "the purest good" — good without the constraint of law.

---

**S612 — Chaotic Good: Ranger.** *(DND-002-D)*

```
la-na-Ranger  ne  wi-no-su  /  ne  wi-vo
```

**Written:** `lanaRanger ne winosu / ne wivo`

**Natural reading:** The Ranger's will rejects structural constraint yet is fully oriented toward value.

**Notes:** W189 + W190. First attestation of `wi-no-su` (W189). Structural freedom in service of genuine benefit. The Ranger operates outside institutional law, serves a good purpose. `wi-no-su` is NOT simply evil — a CG character has maximum `wi-vo` combined with maximum structural freedom.

---

**S613 — Lawful Neutral: Soldier.** *(DND-002-E)*

```
la-na-Soldier  ne  wi-su  /  ne  wi-vo-fe
```

**Written:** `lanaSoldier ne wisu / ne wivofe`

**Natural reading:** The Soldier's will is organized by structure but takes no strong value-position.

**Notes:** W188 + W193. First attestation of `wi-vo-fe` (W193). The Soldier follows orders (`wi-su`) without strong moral investment in outcomes (`wi-vo-fe` = at the ethics-limit). Uses structure as the organizing principle, not benefit or harm. The philosophically fraught alignment: duty above ethics.

---

**S614 — True Neutral: Druid.** *(DND-002-F)*

```
la-na-Druid  ne  wi-su-fe  /  ne  wi-vo-fe
```

**Written:** `lanaDruid ne wisufe / ne wivofe`

**Natural reading:** The Druid's will operates at both the structural and the value limit.

**Notes:** W192 + W193. The only alignment using BOTH neutral terms. Structural symmetry: both sides of `/` have the same form (`ne wi-X-fe`). This mirrors TN's position at the center of the grid. The Druid actively maintains balance: `wi-su-fe` and `wi-vo-fe` are threshold positions, not absences of will.

---

**S615 — Chaotic Neutral: Rogue.** *(DND-002-G)*

```
la-na-Rogue  ne  wi-no-su  /  ne  wi-vo-fe
```

**Written:** `lanaRogue ne winosu / ne wivofe`

**Natural reading:** The Rogue's will rejects structure but takes no strong value-position.

**Notes:** W189 + W193. Maximum structural freedom, indifferent ethics. The Rogue pursues personal interest without concern for order or virtue. CN is associated with maximum unpredictability: `wi-no-su` (no structural constraint) + `wi-vo-fe` (no stable ethical orientation).

---

**S616 — Lawful Evil: Tyrant.** *(DND-002-H)*

```
la-na-Tyrant  ne  wi-su  /  ne  wi-de
```

**Written:** `lanaTyrant ne wisu / ne wide`

**Notes:** W188 + W191. **First standalone attestation of `wi-de` (W191).** Confirms the compound hierarchy: `wi-de` (evil quality) was previously only a component of `wi-de-li` (W124, adversary/enemy); S616 first attests it as a freestanding predicate. LE is the most dangerous alignment: structure (`wi-su`) organized in service of harm (`wi-de`). The Tyrant builds hierarchies FOR exploitation. More terrifying than CE because systematic.

---

**S617 — Neutral Evil: Villain.** *(DND-002-I)*

```
la-na-Villain  ne  wi-su-fe  /  ne  wi-de
```

**Written:** `lanaVillain ne wisufe / ne wide`

**Natural reading:** The Villain's will takes no strong position on structure, yet is directed toward harm.

**Notes:** W192 + W191. Structure is purely instrumental for the Villain — uses order when useful, chaos when not. The ethics axis is maximally negative: harm-directed will regardless of structural context. NE considered the "most purely evil" alignment by some: unpredictable means + consistent harm orientation.

---

**S618 — Chaotic Evil: Demon.** *(DND-002-J)*

```
la-na-Demon  ne  wi-no-su  /  ne  wi-de
```

**Written:** `lanaDemon ne winosu / ne wide`

**Natural reading:** The Demon's will rejects all structure and is directed toward harm.

**Notes:** W189 + W191. Maximum on both extremes. CE is the alignment of destruction for its own sake. The bi-axial sentence makes explicit: the chaos and the evil are independent — the Demon is not "evil because chaotic" but chaotic (`wi-no-su`) AND evil (`wi-de`) as two separate properties. A CE entity is not simply "the most evil" — it is evil AND unstructured, making it unreliable even from its own perspective.

---

## DND-002 Batch Summary

| Entry | Written form | Alignment | Findings |
|-------|-------------|-----------|---------|
| S609 (DND-002-A) | `wili ne wisu / wili ne wivo` | Frame | `/` as co-predication not contrast; W188 + W190 |
| S610 (DND-002-B) | `lanaPaladin ne wisu / ne wivo` | LG | Paradigm case |
| S611 (DND-002-C) | `lanaCleric ne wisufe / ne wivo` | NG | W192 first att. |
| S612 (DND-002-D) | `lanaRanger ne winosu / ne wivo` | CG | W189 first att.; wi-no-su ≠ evil |
| S613 (DND-002-E) | `lanaSoldier ne wisu / ne wivofe` | LN | W193 first att.; structure above ethics |
| S614 (DND-002-F) | `lanaDruid ne wisufe / ne wivofe` | TN | Unique double-neutral; symmetric sentence |
| S615 (DND-002-G) | `lanaRogue ne winosu / ne wivofe` | CN | Structural freedom + value indifference |
| S616 (DND-002-H) | `lanaTyrant ne wisu / ne wide` | LE | **wi-de W191 first standalone att.** |
| S617 (DND-002-I) | `lanaVillain ne wisufe / ne wide` | NE | Instrumental structure + harm |
| S618 (DND-002-J) | `lanaDemon ne winosu / ne wide` | CE | Maximum on both extremes; chaos and evil independent |

**Cross-batch alignment mapping (Jedi/Sith):**

| Entity | Law | Ethics | Alignment |
|--------|-----|--------|-----------|
| Jedi (STW-001) | `wi-su` | `wi-vo` | Lawful Good |
| Sith (STW-002) | `wi-su` | `wi-de` | Lawful Evil |
| `ara` (the Force) | `wi-su-fe` | `wi-vo-fe` | True Neutral |

---

## DND-003: D&D — The Great Wheel Cosmology

**Batch:** DND-003  
**Source:** D&D 5e / Planescape — the Great Wheel model of the multiverse  
**Entries:** S619–S628 · **New vocabulary:** W194 (`pa-ma`), W195 (`to-pa`), W196 (`pa-ne-su`)  
**Scope-prefix first attestations:** `a-pa` (S620), `e-pa` (S622), `u-pa` (S624), `o-pa` (S625)

**Key design note:** This batch activates all four applicable scope prefixes (`a-`, `e-`, `u-`, `o-`) with the spatial root `pa`, yielding four cosmologically distinct spatial categories. See `corpus/translations/Literature/dnd-great-wheel.md` for full analysis.

---

### S619 — DND-003-A

```
la-na-GreatWheel  ne  pa-ne-su
```

**Written:** `lanaGreatWheel ne panesu`

**Natural reading:** The Great Wheel is the cosmological framework.

**Notes:** W196 first attestation. `pa-ne-su` = space-relation-structure = the cosmological system constituted by the structured network of inter-plane relations. Right-branching: `pa-(ne-su)`. The Great Wheel is defined by the structural relations among its planes, not by any single property.

---

### S620 — DND-003-B

```
a-pa  :  pa-fe
```

**Written:** `apa : pafe`

**Natural reading:** A plane is a bounded metaphysical space.

**Notes:** Topic frame construction (`:`) — `a-pa` (scope-derived: `a-` + `pa` = abstract/universal space) is the topic; `pa-fe` (bounded space) is the predicate. **`a-pa` merge hazard avoidance:** `la-a-pa ne pa-fe` would produce `la-a-pa` → merging toward `la-pa` in fast speech (VPC-001 rule). Topic frame sidesteps this. First corpus attestation of `a-pa` in cosmological context; first scope-prefix NP in topic-frame position. `pa-fe` = compositional: `pa` (space) + `fe` (boundary) = bounded/distinct space; unregistered.

---

### S621 — DND-003-C

```
la-na-Material  ne  pa-ma
```

**Written:** `lanaMaterial ne pama`

**Natural reading:** The Material Plane is the realm of matter.

**Notes:** W194 first attestation. `pa-ma` = matter-space = the cosmological domain where `ma` (matter/substance) is the primary constituent. Contrast with `pa-su` (W157 = mountain = structured place): different heads, different scale of meaning.

---

### S622 — DND-003-D

```
la-na-Ethereal  ne  e-pa
```

**Written:** `lanaEthereal ne epa`

**Natural reading:** The Ethereal Plane is transitional space.

**Notes:** First corpus attestation of `e-pa` (`e-` = emergent/transitional + `pa` = space). The Ethereal Plane overlaps the Material and Inner Planes and is the liminal layer through which ghosts pass through solid matter. `e-` captures the between-states, transitional character without requiring a new primitive.

---

### S623 — DND-003-E

```
la-na-Astral  ne  to-pa
```

**Written:** `lanaAstral ne topa`

**Natural reading:** The Astral Plane is thought-space.

**Notes:** W195 first attestation. `to-pa` = thought-realm = the space where `to` (thought/pattern) is the primary constituent. In D&D, condensed thought becomes solid matter in the Astral Plane; dead gods drift through it as solidified divine thought-substance. Direct contrast pair with `pa-ma` (W194): matter-primary vs thought-primary — the two poles of cosmological substance.

---

### S624 — DND-003-F

```
la-na-Inner  ne  u-pa
```

**Written:** `lanaInner ne upa`

**Natural reading:** The Inner Planes are the foundational elemental spaces.

**Notes:** First corpus attestation of `u-pa` (`u-` = interior/foundational + `pa` = space). The Inner Planes are the elemental substrate of D&D cosmology — the foundational elemental layer from which the Material Plane draws its physical substance. Fire, Water, Earth, Air, and the Energy Planes are all subtypes of `u-pa`.

---

### S625 — DND-003-G

```
la-na-Outer  ne  o-pa
```

**Written:** `lanaOuter ne opa`

**Natural reading:** The Outer Planes are collectively distributed space.

**Notes:** First corpus attestation of `o-pa` (`o-` = collective/distributed + `pa` = space). The Outer Planes are arranged in a ring — the "wheel" — each distinct but part of the collective, alignment-distributed structure. Precedent: `o-li` (S508, community-as-unit) established `o-` as the collectivizing prefix.

---

### S626 — DND-003-H

```
la-na-Celestia  ne  o-pa  /  ne  wi-su  ne  wi-vo
```

**Written:** `lanaCelestia ne opa / ne wisu ne wivo`

**Natural reading:** Celestia is an Outer Plane — it has lawful structure and beneficent will.

**Notes:** Co-predicative `/`: Celestia is an `o-pa` (Outer Plane) AND has `wi-su` (W188, lawful will) + `wi-vo` (W190, good will). DND-002 alignment vocabulary first deployed in cosmological context. Cross-franchise: Celestia (LG) is structurally identical to the Jedi Order (STW-001).

---

### S627 — DND-003-I

```
la-na-Baator  ne  o-pa  /  ne  wi-su  ne  wi-de
```

**Written:** `lanaBaator ne opa / ne wisu ne wide`

**Natural reading:** Baator is an Outer Plane — it has lawful structure and harm-directed will.

**Notes:** Formally parallel to S626 — same `(o-pa / ne wi-su ne wi-X)` frame, `wi-de` (W191) replacing `wi-vo`. The structural parallelism shows Celestia and Baator differ only in the ethics axis. Cross-franchise: Baator (LE) is structurally identical to the Sith Order (STW-002).

---

### S628 — DND-003-J

```
la-na-Outlands  ne  wi-su-fe  /  ne  wi-vo-fe
```

**Written:** `lanaOutlands ne wisufe / ne wivofe`

**Natural reading:** The Outlands is both law-neutral and ethics-neutral — the neutral hub of the cosmological wheel.

**Notes:** W192 + W193. Identical double-neutral construction to S614 (TN druid, DND-002). The Outlands is the cosmological embodiment of True Neutrality; S628 and S614 share the same compound pair by design. `o-pa` intentionally omitted: the Outlands' payload is its double-neutrality, not merely its membership in the Outer Planes class.

---

## DND-003 Batch Summary

| Entry | Written form | Plane / entity | Key vocabulary |
|-------|-------------|----------------|----------------|
| S619 (DND-003-A) | `lanaGreatWheel ne panesu` | The Great Wheel | W196 first att. |
| S620 (DND-003-B) | `apa : pafe` | Plane (generic) | `a-pa` first att.; topic frame |
| S621 (DND-003-C) | `lanaMaterial ne pama` | Material Plane | W194 first att. |
| S622 (DND-003-D) | `lanaEthereal ne epa` | Ethereal Plane | `e-pa` first att. |
| S623 (DND-003-E) | `lanaAstral ne topa` | Astral Plane | W195 first att. |
| S624 (DND-003-F) | `lanaInner ne upa` | Inner Planes | `u-pa` first att. |
| S625 (DND-003-G) | `lanaOuter ne opa` | Outer Planes | `o-pa` first att. |
| S626 (DND-003-H) | `lanaCelestia ne opa / ne wisu ne wivo` | Celestia (LG) | W188 + W190 |
| S627 (DND-003-I) | `lanaBaator ne opa / ne wisu ne wide` | Baator (LE) | W188 + W191 |
| S628 (DND-003-J) | `lanaOutlands ne wisufe / ne wivofe` | Outlands (TN) | W192 + W193 |

**Cross-batch alignment mapping (extended):**

| Plane / Entity | Law | Ethics | Batch |
|----------------|-----|--------|-------|
| Celestia | `wi-su` | `wi-vo` | DND-003 |
| Baator | `wi-su` | `wi-de` | DND-003 |
| Outlands | `wi-su-fe` | `wi-vo-fe` | DND-003 |
| TN Druid | `wi-su-fe` | `wi-vo-fe` | DND-002 |
| Jedi Order | `wi-su` | `wi-vo` | STW-001 |
| Sith Order | `wi-su` | `wi-de` | STW-002 |
| The Force (`ara`) | `wi-su-fe` | `wi-vo-fe` | STW-001 (cross-ref) |

---

## Declaration of Independence — Preamble (S629–S638)

*Batch purpose (DOI-001): translation stress-test of the Declaration of Independence preamble. Tests the extremal `[X]-no-fe` suffix on political rights, the new liberty-compound `pa-ki-su`, self-evident proposition `su-to`, the affect-value form `fa-vo`, and cross-batch connection to THO-001 (divine attributes) via the self-grounding family. Full analysis in `corpus/translations/Literature/doi-declaration.md`.*

*New compounds attested this batch: `fa-vo` (W197, happiness), `pa-ki-su` (W198, liberty-state), `su-to` (W199, self-evident proposition).*

---

### S629 — DOI-001-A

```
go  ka-be  zo-li-su,  la-o-zo-li  ka-ne-de  lo-ne-wi-su
```

**Written:** `go kabe zolisu, laozoli kanede lonewisu`

**Natural reading:** When the course of human events has grown enough — a people dissolve the political bonds connecting them.

**Notes:** `go  ka-be  zo-li-su` = causal-temporal framing: as origin-cause events accumulate/increase in people-structure. `ka-ne-de` (W092) = deliberate relational decrease = dissolve. `ne-wi-su` = relational-volitional-structure = political bond (right-branching: ne-(wi-su) = connection of [organized-will]).

---

### S630 — DOI-001-B

```
la-yu  to  lo-su-to
```

**Written:** `layu to losuto`

**Natural reading:** We hold that these are self-evident truths.

**Notes:** W199 first attestation. `la-yu` = we (agentive). `to` used as verb: to know / hold as knowledge. `su-to` (W199) = self-evident proposition = truth whose ground is its own structure. Echoes `la-mi  to  lo-tonesu` (W000 example: "I hold truth"). The self-evident truths are objects of knowing, not just claims — `la-yu  to  lo-su-to` = "we hold self-grounding-truths."

---

### S631 — DOI-001-C

```
la-go-li  be  lo-o-zo-li  su-ne
```

**Written:** `lagoli be loozoli sune`

**Natural reading:** The creator made all persons equal in relational standing.

**Notes:** `go-li` = origin-person = creator (composable; no W-entry needed). `be` = deliberate increase = made/established. `o-zo-li` = collective-persons = all people. `su-ne` (W174) = structure-of-relation = equal (structural relational parity). Equality is relational-structural, not identity of substance. Contrast `su-ne-ru` (equal-in-unified-structure, used in GEO-001 for equal sides) — `su-ne` without `ru` is the general equal-standing reading.

---

### S632 — DOI-001-D

```
la-go-li  be  lo-o-zo-li  lu-vo-ne-no-fe
```

**Written:** `lagoli be loozoli luvonenofe`

**Natural reading:** The creator gave all persons unalienable rights as their endowment.

**Notes:** `lu-` beneficiary frame: the rights are what the persons receive as endowment. `vo-ne-no-fe` = THO-001 extremal construction: `vo-ne` (W118, righteous-relational-standing / rights) + `no-fe` (without boundary) = unalienable rights. The extremal suffix encodes the normative force: these rights have no external limit that can strip them. The pattern extends naturally from divine attributes (THO-001) to political entitlements (DOI-001).

---

### S633 — DOI-001-E

```
zo  /  pa-ki-su  /  ka-se  fa-vo
```

**Written:** `zo / pakisu / kase favo`

**Natural reading:** Life / Liberty / the pursuit of happiness.

**Notes:** W197 (`fa-vo`, happiness) and W198 (`pa-ki-su`, liberty) first attestations. Three-item `/` parallel list — the Declaration's canonical triad. `zo` (primitive) = Life. `pa-ki-su` (W198) = liberty-state = structured freedom. `ka-se  fa-vo` = deliberate-seeking positive-affect-value = pursuit of happiness (two-word phrase, not a single compound). Phonologically the cleanest sentence in the batch.

---

### S634 — DOI-001-F

```
go  vo-ne-no-fe,  la-o-zo-li  be  ka-li-su  /  la-ka-li-su  wi-vo  go  ne-vo-wi
```

**Written:** `go vonenofe, laozoli be kalisu / lakalisu wivo go nevowi`

**Natural reading:** For unalienable rights, persons institute governance; governance derives just power from consent.

**Notes:** `go  vo-ne-no-fe,` = purpose framing: for the sake of unalienable rights. `be` = institute / establish. `/` parallel: first clause = persons establish governance; second clause = governance's just-will (`wi-vo`, W190) derives (`go`) from consent. `ne-vo-wi` = relation-value-will = consent as a relational state in which wills converge on shared value (composable; no W-entry needed).

---

### S635 — DOI-001-G

```
go  ka-li-su  ne  ka-de,  la-o-zo-li  vo-ne  ki  lo-ka-li-su
```

**Written:** `go kalisu ne kade, laozoli vone ki lokalisu`

**Natural reading:** When governance becomes destructive, the people have the right to change or abolish it.

**Notes:** `go  ka-li-su  ne  ka-de` = causal-conditional: governance's relational state (`ne`) becomes `ka-de` (deliberately destructive). `,` boundary. `la-o-zo-li  vo-ne` = the people [have] righteous standing (W118 used as predicate). `ki` = change (primitive verb: covers both alter and abolish). `lo-ka-li-su` = patient: the governance. `ki` alone is sufficient; `ka-ne-de` could specify dissolution specifically — `ki` encodes the general right.

---

### S636 — DOI-001-H

```
la-o-zo-li  be  ka-li-su  ka-be  go  to
```

**Written:** `laozoli be kalisu kabe go to`

**Natural reading:** The people institute a new governance grounded in reason and principles.

**Notes:** `be` = institute / increase. `ka-be` = deliberately-established, freshly-instituted = new. `go  to` = grounded in / derived from `to` (primitive: thought/reason/conceptual principle). The Declaration's "principles" are conceptual patterns — rational grounds for governance — without further qualification. Using `to-ne-su` (W000, organized truth = the language itself) here would over-determine the claim: it would collapse the Declaration's broad Enlightenment appeal to reason into a specific ontological object. `to` alone is honest: governance is grounded in reason/principles without asserting they constitute a structured relational knowledge system.

---

### S637 — DOI-001-I

```
la-na-Colonies  ne  pa-ki-su  /  ne  no-ne-fe
```

**Written:** `lanaColonies ne pakisu / ne nonefe`

**Natural reading:** The Colonies are in a state of liberty and are free of all binding connection.

**Notes:** `pa-ki-su` (W198) = liberty-state = Free. `no-ne-fe` (W075) = no-relation-boundary = independent. `/` parallel pairs the positive claim (liberty as a structured state) with the negative claim (independence as absence of binding). The Declaration's "Free and Independent States" maps to the `pa-ki-su / no-ne-fe` pair: liberty is the presence of structured freedom; independence is the absence of constraining relational bond. Both are necessary and distinct.

---

### S638 — DOI-001-J

```
vo-ne-no-fe  ne  go-ne  /  su-to  ne  tonesu
```

**Written:** `vonenofe ne gone / suto ne tonesu`

**Natural reading:** Unalienable rights are self-originating (like the divine I AM) / self-evident truth is the condition of organized knowledge.

**Notes:** Cross-batch synthesis: DOI-001 × THO-001 × W000. `vo-ne-no-fe` predicated on `go-ne` (W159, self-originating relation = "I AM WHO I AM"): unalienable rights share the structural character of the divine self-grounding — both are properties that have no external origin that could revoke them. `su-to` (W199) predicated on `to-ne-su` (W000): self-evident truth is the instantiation of organized-knowledge = the language's own condition. Philosophical keystone of the batch: rights are grounded in self-originating structure; self-evident truths are grounded in Tonesu itself.

---

## DOI-001 Batch Summary

**Entries:** S629–S638 · **New vocabulary:** W197 (`fa-vo`), W198 (`pa-ki-su`), W199 (`su-to`)

| Entry | Written form | Source clause | Key vocabulary |
|-------|-------------|---------------|----------------|
| S629 (DOI-001-A) | `go kabe zolisu, laozoli kanede lonewisu` | When in the course of human events | W092 re-use; `ne-wi-su` compositional |
| S630 (DOI-001-B) | `layu to losuto` | We hold these truths self-evident | W199 first att. |
| S631 (DOI-001-C) | `lagoli be loozoli sune` | All men created equal | `go-li` compositional; W174 |
| S632 (DOI-001-D) | `lagoli be loozoli luvonenofe` | Endowed with unalienable Rights | `vo-ne-no-fe` extremal; `lu-` frame |
| S633 (DOI-001-E) | `zo / pakisu / kase favo` | Life, Liberty, pursuit of Happiness | W197 + W198 first att. |
| S634 (DOI-001-F) | `go vonenofe, laozoli be kalisu / lakalisu wivo go nevowi` | Governments instituted | `ne-vo-wi` consent; W190 |
| S635 (DOI-001-G) | `go kalisu ne kade, laozoli vone ki lokalisu` | Right to alter or abolish | W118 as predicate; `ki` |
| S636 (DOI-001-H) | `laozoli be kalisu kabe go to` | Institute new Government | `ka-be` = new; `go to` = grounded in reason |
| S637 (DOI-001-I) | `lanaColonies ne pakisu / ne nonefe` | Free and Independent States | W198 + W075 parallel |
| S638 (DOI-001-J) | `vonenofe ne gone / suto ne tonesu` | Synthesis — rights + divine structure | W159 + W199 + W000 cross-batch |

---

## CDA-001: Communications Decency Act — Section 230(c)(1)

**Source text:** "No provider or user of an interactive computer service shall be treated as the publisher or speaker of any information provided by another information content provider." — 47 U.S.C. §230(c)(1)

**New vocabulary:** W200 (`su-ka-li`), W201 (`si-go-li`), W202 (`to-ki'ne-su`)

---

### S639 — CDA-001-A

```
la-su-ka-li  lo-to-ki'ne-su  ne  no-si-go-li  lo-to-si  go  zo-li
```

**Written:** `lasukali lotoki'nesu ne nosigoli lotosi go zoli`

**Natural reading:** A service-provider of an online platform is not a content-originator of information-signals from persons.

**Notes:** Direct rendering of §230(c)(1). Three roles introduced: `su-ka-li` (W200, service-provider = "provider"), `to-ki'ne-su` (W202, online platform = "interactive computer service"), `si-go-li` (W201, content-originator = "publisher or speaker"). `lo-to-si go zo-li` (information-signals from a person) encodes "provided by another information content provider" — deliberately open-scoped: who counts as "another" and where the boundary lies is the statute's unresolved problem (addressed in S642). First attestations: W200, W201, W202.

---

### S640 — CDA-001-B

```
la-to-ki'ne-su  ne  si-mu  lu-zo-li  /  ne  no-si-go-li
```

**Written:** `latoki'nesu ne simu luzoli / ne nosigoli`

**Natural reading:** An online platform is a relay device for persons / is not a content-originator.

**Notes:** `si-mu` (W039) = relay device, signal transceiver — precisely captures the platform's structural role: it transmits, not originates. `lu-zo-li` = for-the-benefit-of persons (beneficiary frame). The `/` parallel pairs the structural description (relay-device) with its legal consequence (not a content-originator). Immunity flows from this structural identity. S641 shows where this breaks.

---

### S641 — CDA-001-C

```
go  la-su-ka-li  ka-to-fe  lo-to-si,  du  la-su-ka-li  ne  si-go-li
```

**Written:** `go lasukali katofe lotosi, du lasukali ne sigoli`

**Natural reading:** If a service-provider deliberately categorizes information, then the service-provider is a content-originator.

**Notes:** The editorial-judgment exception. `go {premise}, du {result}` causal conditional. `ka-to-fe` (W122) = deliberate epistemic bounding = editorial judgment / curation. The moment a platform deliberately categorizes content — curating, filtering, labeling on the merits — it crosses into `si-go-li` territory. This is exactly the legal controversy 230 litigation has circled for decades: where does passive hosting end and active editorial selection begin? Tonesu states the threshold cleanly via `ka-to-fe`.

---

### S642 — CDA-001-D

```
la-wi-fe  no  to-su-ki  lo-to-fe  su-ka-li  ne  si-go-li
```

**Written:** `lawife no tosuki lotofe sukali ne sigoli`

**Natural reading:** The rule has not comprehended the boundary between service-provider and content-originator.

**Notes:** `to-su-ki` (W025) = comprehend, enter organized knowledge. `lo-to-fe su-ka-li ne si-go-li` = the epistemic-boundary of [the relation between] service-provider and content-originator. The statute uses "another information content provider" but does not define where one role ends and the other begins. In Tonesu, a rule that invokes a boundary (`to-fe`) it has not organized knowledge of (`no to-su-ki`) is structurally incomplete. The statute functions only because courts tolerate strategic vagueness; Tonesu does not.

---

### S643 — CDA-001-E

```
la-wi-fe  ne  no-su-to  /  ne  wi-fe'ka-to-fe
```

**Written:** `lawife ne nosuto / ne wife'katofe`

**Natural reading:** The rule is not a self-evident proposition / it is a rule about deliberate categorization.

**Notes:** `su-to` (W199) = self-evident proposition. §230(c)(1) does not assert that platforms ARE NOT publishers — it mandates that they MUST NOT BE TREATED AS publishers. "Shall be treated as" is `wi-fe'ka-to-fe` (rule-about-deliberate-categorization), not `su-to` (structural truth). The distinction matters: a `wi-fe'ka-to-fe` can be appealed, contested, amended; a `su-to` cannot. `wi-fe'ka-to-fe` = [wi-fe (W100) rule] juncture [ka-to-fe (W122) deliberate categorical judgment] = rule whose content is prescriptive categorization.

---

### S644 — CDA-001-F

```
la-wi-fe  ne  wi-fe'ka-to-fe  /  ke, la-wi-fe  no  to-su-ki  lo-to-fe  su-ka-li  ne  si-go-li
```

**Written:** `lawife ne wife'katofe / ke, lawife no tosuki lotofe sukali ne sigoli`

**Natural reading:** The rule is a prescription about categorization / but the rule has not defined the boundary between service-provider and content-originator.

**Notes:** Synthesis of CDA-001. `/  ke,` construction: first clause (from S643) establishes what §230 IS (a prescriptive categorization rule); `ke,` pivots to the unresolved problem (from S642: the boundary is undefined). Tonesu diagnosis: §230(c)(1) is structurally coherent as a legal instrument — it is a `wi-fe'ka-to-fe`, not a `su-to` — but incomplete because the boundary it relies on (service-provider vs content-originator) has not been given organized definition. The statute works by delegating the boundary question to judicial discretion, a structural move Tonesu would require to be made explicit.

---

## CDA-001 Batch Summary

**Entries:** S639–S644 · **New vocabulary:** W200 (`su-ka-li`), W201 (`si-go-li`), W202 (`to-ki'ne-su`)

| Entry | Written form | Source clause | Key vocabulary |
|-------|-------------|---------------|----------------|
| S639 (CDA-001-A) | `lasukali lotoki'nesu ne nosigoli lotosi go zoli` | Core immunity claim | W200 + W201 + W202 first att. |
| S640 (CDA-001-B) | `latoki'nesu ne simu luzoli / ne nosigoli` | Platform as relay device | `si-mu` (W039) relay identity |
| S641 (CDA-001-C) | `go lasukali katofe lotosi, du lasukali ne sigoli` | Editorial exception | `ka-to-fe` (W122) threshold |
| S642 (CDA-001-D) | `lawife no tosuki lotofe sukali ne sigoli` | "Another" boundary gap | `to-su-ki` (W025) gap diagnosis |
| S643 (CDA-001-E) | `lawife ne nosuto / ne wife'katofe` | "Shall be treated as" = normative | `su-to` (W199) vs `wi-fe'ka-to-fe` |
| S644 (CDA-001-F) | `lawife ne wife'katofe / ke, lawife no tosuki lotofe sukali ne sigoli` | Structural verdict | Synthesis: S643 + S642 |

---

## ACA-001 — ACA Individual Mandate (26 U.S.C. §5000A)

**Source:** Affordable Care Act Individual Mandate, 26 U.S.C. §5000A · *NFIB v. Sebelius*, 567 U.S. 519 (2012)
**New vocabulary:** W203 (`wi-fe'de`), W204 (`su-zo-ko`), W205 (`ka-li-de`)

### S645 — ACA-001-A

**Source:** "An applicable individual shall ... ensure that the individual ... is covered under minimum essential coverage for such month." — 26 U.S.C. §5000A(a)

```
wi-fe  la-i-zo-li  ko  lo-su-zo-ko
```

**Written:** `wife laizoli ko losuzoko`

**Gloss-line:** `rule [agent]particular-person maintains [patient]coverage-structure`

**Natural reading:** The rule — an applicable person shall maintain health coverage.

**Notes:** W204 (`su-zo-ko`) first attestation. The mandate itself is structurally clean: there is a rule (`wi-fe`), an agent (`i-zo-li` = the particular person to whom the rule applies), a predicate (`ko` = maintains within containment structure), and a patient (`su-zo-ko` = minimum essential coverage as structured organism-protection). No ambiguity in the obligation. The controversy lives entirely in S646 onward.

---

### S646 — ACA-001-B

**Source:** "If a taxpayer ... fails to meet the requirement of subsection (a) for 1 or more months, then there is hereby imposed on the taxpayer a penalty" — 26 U.S.C. §5000A(b)

```
go  la-i-zo-li  no  ko  lo-su-zo-ko,  du  wi-fe'de  lu-ka-li-su
```

**Written:** `go laizoli no ko losuzoko, du wife'de lukalisu`

**Gloss-line:** `origin [agent]person not-maintain [patient]coverage, therefore penalty [beneficiary]governance`

**Natural reading:** Because the person does not maintain coverage, a payment accrues to governance.

**Notes:** W203 (`wi-fe'de`) first attestation. `wi-fe'de` = juncture compound: `[wi-fe]` + `de` = rule-decrease = the decrease imposed by the rule. Written `wife'de` (juncture `'` preserved). Structurally neutral: says nothing about whether this is a "penalty" or a "tax." It is a directed decrease flowing to governance (`lu-ka-li-su`), triggered by coverage failure. That structural description is the entire ACA controversy, compressed into one sentence.

---

### S647 — ACA-001-C

**Source:** Congress labeled §5000A(b) a "penalty" (and emphatically not a tax); Roberts in *NFIB v. Sebelius* re-labeled it a "tax" to uphold it under Article I §8.

```
la-ka-li-su  to  lo-wi-fe'de  ne  no-ka-li-de  /  la-na-Roberts  to  lo-wi-fe'de  ne  ka-li-de
```

**Written:** `lakalisu to lowife'de ne nokalide / lanaRoberts to lowife'de ne kalide`

**Gloss-line:** `[agent]Congress holds [patient]payment is not-a-tax / [agent]Roberts holds [patient]payment is a-tax`

**Natural reading:** Congress held the payment is not a tax / Roberts held the same payment is a tax.

**Notes:** W205 (`ka-li-de`) first attestation. The parallel `/` construction puts identical sentence structure on both sides with the single difference: `no-ka-li-de` (not-a-tax) vs `ka-li-de` (a-tax). Same patient (`lo-wi-fe'de`). Same operation (`to` = hold as knowledge). Opposite conclusions. This is the constitutional naming dispute made structurally visible. Both uses of `to` (rather than `ka-to-fe`) are deliberate: Congress and Roberts are each asserting what they believe/held, not performing a bare categorical assignment — the epistemic commitment is present on both sides.

---

### S648 — ACA-001-D

**Source:** Roberts's holding: §5000A(b) has characteristics of both penalty and tax simultaneously — it can be upheld as a tax even if it could not be upheld as a commerce regulation.

```
lo-wi-fe'de  ne  to-fe  wi-fe'de  /  ne  to-fe  ka-li-de
```

**Written:** `lowife'de ne tofe wife'de / ne tofe kalide`

**Gloss-line:** `[patient]payment is at-epistemic-boundary penalty / is at-epistemic-boundary tax`

**Natural reading:** The payment sits at the boundary of being a penalty / and at the boundary of being a tax.

**Notes:** `ne to-fe X` = "occupies the epistemic boundary of X" = exists at the edge of the X-category. The Roberts finding compressed: §5000A(b) was deliberately designed to sit at the intersection of both categories. That was not a drafting error — it was the strategy. Obama needed it to look like a penalty (avoiding the "tax increase" political charge); Roberts needed it to look like a tax (finding constitutional footing). Tonesu makes the construction visible: the payment is `to-fe wi-fe'de` AND `to-fe ka-li-de` simultaneously. That intersection is the statute's operating space.

---

### S649 — ACA-001-E

**Source:** Roberts's decisive constitutional move: regardless of what Congress called it, it functions as a tax; therefore it is constitutional under the taxing power.

```
la-na-Roberts  wi-fe'ka-to-fe  lo-wi-fe'de  ne  ka-li-de
```

**Written:** `lanaRoberts wife'katofe lowife'de ne kalide`

**Gloss-line:** `[agent]Roberts norm-categorizes [patient]payment as tax`

**Natural reading:** Roberts normatively categorized the payment as a tax.

**Notes:** `wi-fe'ka-to-fe` = W100 + W122 juncture compound = the rule-that-assigns-categories = normative categorization. Roberts did not *discover* that §5000A(b) is a tax — he *decided* the tax-frame is constitutionally operative. This is `wi-fe'ka-to-fe`, not `su-to`. The structural parallel with CDA-001 S643 is exact: both involve a legal instrument deploying `wi-fe'ka-to-fe` to resolve a `to-fe` boundary that the underlying object sits astride. The pattern appears to be fundamental to law under the `~` mode: legal systems use `wi-fe'ka-to-fe` to impose resolution on structurally ambiguous objects, rather than waiting for `su-to` resolution.

---

### S650 — ACA-001-F

**Source:** Tonesu structural verdict on §5000A(b) and *NFIB v. Sebelius*

```
~wi-fe'de  ne  su-to  /  ke,  wi-fe  no  to-su-ki  lo-to-fe  wi-fe'de  ne  ka-li-de
```

**Written:** `~wife'de ne suto / ke, wife no tosuki lotofe wife'de ne kalide`

**Gloss-line:** `~penalty is structural-truth / but rule not-comprehends [patient]boundary penalty and tax`

**Natural reading:** `~wi-fe'de` is a structural fact / but the rule has not comprehended the boundary between penalty and tax.

**Notes:** The `~` is in its **structural mode** (spec/phonology.md § `~` Approximation Mark, structural sub-section): imprecision belonging to the source system, not the speaker. `~wi-fe'de` = something-like-a-penalty, where the category boundary is deliberately unresolved by the statute. `su-to` (W199) confirms: this is a structural self-evidence — the honest translation of "shared responsibility payment" is `~wi-fe'de`. `ke,` pivots to the diagnostic parallel with CDA-001 S644: the rule (`wi-fe`) has not given `to-su-ki` (organized knowledge) to the `to-fe` between `wi-fe'de` and `ka-li-de`. The statute works by straddling rather than resolving. Tonesu verdict: structurally coherent but deliberately incomplete — the same structural finding as Section 230. **Pattern identified:** Law uses `wi-fe'ka-to-fe` to force resolution, and `~` to postpone it. Both are constitutional design tools, not bugs.

---

## ACA-001 Batch Summary

**Entries:** S645–S650 · **New vocabulary:** W203 (`wi-fe'de`), W204 (`su-zo-ko`), W205 (`ka-li-de`)

| Entry | Written form | Source clause | Key vocabulary |
|-------|-------------|---------------|----------------|
| S645 (ACA-001-A) | `wife laizoli ko losuzoko` | Mandate rule | W204 (`su-zo-ko`) first att. |
| S646 (ACA-001-B) | `go laizoli no ko losuzoko, du wife'de lukalisu` | Payment trigger | W203 (`wi-fe'de`) first att. |
| S647 (ACA-001-C) | `lakalisu to lowife'de ne nokalide / lanaRoberts to lowife'de ne kalide` | Naming dispute | W205 (`ka-li-de`) first att. |
| S648 (ACA-001-D) | `lowife'de ne tofe wife'de / ne tofe kalide` | Both descriptions hold | `to-fe` (W028) location pred. |
| S649 (ACA-001-E) | `lanaRoberts wife'katofe lowife'de ne kalide` | Roberts's normative move | `wi-fe'ka-to-fe` pattern |
| S650 (ACA-001-F) | `~wife'de ne suto / ke, wife no tosuki lotofe wife'de ne kalide` | `~` verdict | `~` structural mode |

---

## DND-004: D&D — The Classes

**Batch:** DND-004  
**Source:** Dungeons & Dragons — core class roster (originally AD&D; here the 8-class founding set)  
**Entries:** S651–S658 · **New vocabulary:** W206 (`ra-ka-li`), W207 (`to-ra-li`), W208 (`se-de-li`), W209 (`vo-ra-li`), W210 (`zo-re-li`), W211 (`wi-vo-li`), W212 (`zo-ki-li`), W213 (`so-vo-li`)

**Scope:** The 8 founding classes of AD&D — Fighter, Wizard, Rogue, Cleric, Druid, Paladin, Ranger, Bard. Remaining 5e classes (Barbarian, Monk, Sorcerer, Warlock, Artificer) deferred. See `corpus/translations/Literature/dnd-classes.md` for full analysis.

**Design claim:** All eight classes reduce to 3-root `-li` agent compounds using the closed primitive set. The `-li` derivational suffix is the productive agent-maker here; each compound encodes the class's defining activity as the head modifier. The batch demonstrates the **`-li` role-registry pattern** as a productive word-formation mechanism for role and character vocabulary.

---

### S651 — DND-004-A

```
la-ra-ka-li  ra-ka  lo-zo-li
```

**Written:** `larakali raka lozoli`

**Natural reading:** A fighter applies force against persons.

**Notes:** W206 (`ra-ka-li`) first attestation. `ra-ka` = volitional force-action = the fighter's predicate (purposeful combat). `lo-zo-li` (W148, human persons) as patient = in combat the fighter acts on others. The `ka` component is load-bearing: marks the force as deliberate rather than incidental (contrast `ra-ki` W038 = storm = non-volitional force). The fighter is the simplest class compound: direct volitional force, no metaphysical source required.

---

### S652 — DND-004-B

```
la-to-ra-li  ra-be  go  to
```

**Written:** `latorali rabe go to`

**Natural reading:** A wizard manifests force from knowledge.

**Notes:** W207 (`to-ra-li`) first attestation. `ra-be` = force-increase/emergence = force manifests. `go to` = from/because of knowledge = the force's source is the wizard's `to`. Parallel structure to S654 (cleric): both use `ra-be go [source]`, differing only in source (`to` vs `vo`). This parallel is intentional — it makes the wizard/cleric structural distinction explicit.

---

### S653 — DND-004-C

```
la-se-de-li  se-de
```

**Written:** `lasedeli sede`

**Natural reading:** A rogue evades detection.

**Notes:** W208 (`se-de-li`) first attestation. Bare predicate `se-de` — the rogue evades detection in general, no specific target identified. The sentence is minimal by design: the rogue's defining act is the act itself, not its effect on any patient. Contrast `si-de` (W098, misinformation = signal-decrease): `se` = raw perceptual input; `si` = encoded signal. A rogue hides from perception (`se-de`); a forger degrades information (`si-de`).

---

### S654 — DND-004-D

```
la-vo-ra-li  ra-be  go  vo
```

**Written:** `lavorali rabe go vo`

**Natural reading:** A cleric manifests force from worth.

**Notes:** W209 (`vo-ra-li`) first attestation. Structural parallel to S652 (wizard): `ra-be go vo` vs `ra-be go to`. The cleric's force comes from `vo` (sacred worth/value); the wizard's from `to` (knowledge). A cleric who loses their faith loses their `vo`, and thus their `ra`. The parallel structure makes the wizard/cleric distinction visible as a single variable change in an otherwise identical construction.

---

### S655 — DND-004-E

```
la-zo-re-li  ko  lo-re-zo
```

**Written:** `lazoreli ko lorezo`

**Natural reading:** A druid is contained within the life-cycle.

**Notes:** W210 (`zo-re-li`) first attestation. `ko` = containment predicate (is within / belongs to). `lo-re-zo` = patient: `re-zo` = cycle-of-organisms = life-cycle (reversed root order from the compound `zo-re` — the patient names the cycle as its first component). The druid is defined by embeddedness, not by study (`zo-su-ka-li` W150, ecologist) or motion (`zo-ki-li` W212, ranger).

---

### S656 — DND-004-F

```
la-wi-vo-li  wi  lo-vo  /  ra-be
```

**Written:** `lawivoli wi lovo / rabe`

**Natural reading:** A paladin wills toward worth / and force manifests.

**Notes:** W211 (`wi-vo-li`) first attestation. Bi-clausal parallel (`/`): first clause = the oath (`wi lo-vo` = wills toward worth); second clause = the combat action (`ra-be` = force manifests, implied agent: same paladin). Both clauses are simultaneous and load-bearing — neither is subordinate to the other. The oath DRIVES the force; the force EXPRESSES the oath. A paladin who loses `wi lo-vo` retains `ra-be` capacity but is no longer structurally a paladin.

---

### S657 — DND-004-G

```
la-zo-ki-li  ki  lo-pa-fe
```

**Written:** `lazokili ki lopafe`

**Natural reading:** A ranger moves to the frontier.

**Notes:** W212 (`zo-ki-li`) first attestation. `ki` = motion/movement as predicate. `lo-pa-fe` (W138, boundary-space/frontier) = the ranger's canonical destination. The frontier is the structural definition of the ranger's domain: the edge between the settled and the wild. Contrast `di-ki-li` (W061, traveler): a traveler follows a course by direction; a ranger navigates biological environments toward the frontier.

---

### S658 — DND-004-H

```
la-so-vo-li  so-vo  lu-zo-li
```

**Written:** `lasovoli sovo luzoli`

**Natural reading:** A bard creates sonic worth for persons.

**Notes:** W213 (`so-vo-li`) first attestation. `so-vo` = sonic worth = the bard's act (acoustic performance that creates value). `lu-zo-li` (W148, persons) = beneficiary frame: the worth is created FOR others. The bard is the only class in DND-004 whose defining sentence uses the `lu-` beneficiary frame — a structural marker of other-directedness. Performance is constitutively for an audience; a bard performing in isolation is not yet a bard in their defining act.

---

## DND-004 Batch Summary

**Entries:** S651–S658 · **New vocabulary:** W206 (`ra-ka-li`), W207 (`to-ra-li`), W208 (`se-de-li`), W209 (`vo-ra-li`), W210 (`zo-re-li`), W211 (`wi-vo-li`), W212 (`zo-ki-li`), W213 (`so-vo-li`)

| Entry | Written form | Class | Key vocabulary |
|-------|-------------|-------|----------------|
| S651 (DND-004-A) | `larakali raka lozoli` | Fighter | W206 (`ra-ka-li`) first att. |
| S652 (DND-004-B) | `latorali rabe go to` | Wizard | W207 (`to-ra-li`) first att. |
| S653 (DND-004-C) | `lasedeli sede` | Rogue | W208 (`se-de-li`) first att. |
| S654 (DND-004-D) | `lavorali rabe go vo` | Cleric | W209 (`vo-ra-li`) first att. |
| S655 (DND-004-E) | `lazoreli ko lorezo` | Druid | W210 (`zo-re-li`) first att. |
| S656 (DND-004-F) | `lawivoli wi lovo / rabe` | Paladin | W211 (`wi-vo-li`) first att. |
| S657 (DND-004-G) | `lazokili ki lopafe` | Ranger | W212 (`zo-ki-li`) first att. |
| S658 (DND-004-H) | `lasovoli sovo luzoli` | Bard | W213 (`so-vo-li`) first att. |

---

### DND-004 Findings

**Finding 1: All eight founding D&D classes reduce to 3-root `-li` agent compounds using the closed primitive set.** Every class compound takes the form `[X-Y]-li` where `li` is the derivational agent-suffix and `X-Y` is the 2-root modifier encoding the class's defining activity. No new primitives are required. The 8 classes are expressible with 12 primitives: `ra`, `to`, `se`, `vo`, `zo`, `wi`, `so`, `ka`, `de`, `re`, `ki`, `li`. This is a strong positive stress-test of the `-li` pattern.

**Finding 2: The `X-ra-li` pattern (force-source-person) unifies three classes as a structural family.** Fighter (`ra-ka-li`), Wizard (`to-ra-li`), and Cleric (`vo-ra-li`) all share `ra` (force) as the axial root. What differs is the relationship to force: the fighter APPLIES force directly (`ka = volitional action`); the wizard CHANNELS force FROM knowledge (`to → ra`); the cleric CHANNELS force FROM worth (`vo → ra`). The X-ra-li analysis makes the class triad structurally legible as force applied through different sources.

**Finding 3: The `zo-X-li` pattern yields three distinct relationships to the living world.** Druid (`zo-re-li`), Ranger (`zo-ki-li`), and the existing Ecologist (`zo-su-ka-li` W150) all share `zo` (living thing) as lead root. The distinguishing second root encodes the mode of relationship: `re` = containment in cycles (druid: IS within the cycle); `ki` = motion through (ranger: MOVES through); `su-ka` = structured study of (ecologist: STUDIES from outside). Three entries, same root family, three ontologically distinct stances.

**Finding 4: The Paladin as structural anomaly.** All other classes' defining sentences use a single predicate frame. The paladin requires the bi-clausal parallel (`/`): oath (`wi lo-vo`) / force (`ra-be`). Neither clause is sufficient alone — a paladin without the oath is just a fighter; a paladin without force is just a will. The structural complexity of the paladin's sentence mirrors the structural complexity of the class: it is constitutively dual.

**Finding 5: The Bard as the only beneficiary-frame class.** Only S658 (bard) uses the `lu-` beneficiary marker. All other classes act on patients (`lo-`) or on sources (`go`). The bard creates FOR others. This is the structural encoding of a key D&D class distinction: the bard's gift is constitutively social; it requires an audience. The `lu-` frame marks this at the grammar level, not just in the notes.

---

## CKG-001: Cookie Recipe — Chocolate Chip Cookies

**Batch:** CKG-001  
**Source:** Standard chocolate chip cookie recipe (generic procedural form)  
**Entries:** S659–S664 · **New vocabulary:** W214 (`ko-ha-mu`), W215 (`ma-ne-ki`), W216 (`ha-zo-ra-ma`)

**Key design note:** This batch exercises the instruction register (agent-dropped
imperatives), material-state vocabulary for wet/dry ingredients, double `lo-` patient
coordination with `ne`, artifact agency (`la-ko-ha-mu`), and phase-change tracking
(raw dough → baked good). See `corpus/translations/Everyday/chocolate-chip-cookies.md`
for full analysis.

---

### S659 — CKG-001-A

```
ha-ki  lo-ko-ha-mu
```

**Written:** `haki lokohamu`

**Natural reading:** Heat-change the containment-heat-device.

**Notes:** W214 (`ko-ha-mu`) first attestation. Bare-verb imperative; no `la-` agent
(instruction register: agent = immediate addressee). `ha-ki` = thermal-change =
heat up. `ko-ha-mu` = containment-heat-device = oven: `ko` (containment) +
`ha` (heat) + `mu` (device). Right-branch: `ko-[ha-mu]` = containment-[heat-device].

---

### S660 — CKG-001-B

```
ma-ne-ki  lo-ki'ma-zo-ra-ma  pa-ko-mu  lu-su-ne
```

**Written:** `maneki loki'mazorama pakomu lusune`

**Natural reading:** Combine the liquid food-materials in the vessel, result: structural harmony.

**Notes:** W215 (`ma-ne-ki`) first attestation. `ma-ne-ki` = matter-[relational-motion]
= the action of bringing matter into relational unity through motion = mix/combine.
`ki'ma-zo-ra-ma` = liquid food materials (W114 + W144) = the wet ingredients.
`pa-ko-mu` = in the vessel / bowl. `lu-su-ne` = result: structural harmony (W174) =
until the mixture is harmoniously unified (creamy / well-emulsified).

---

### S661 — CKG-001-C

```
pa-no-ne-ko-mu  ma-ne-ki  lo-su'ma-zo-ra-ma
```

**Written:** `panonekomu maneki losu'mazorama`

**Natural reading:** At the unrelated vessel, combine the solid food-materials.

**Notes:** `no-ne-ko-mu` = non-relation-vessel = a vessel unconnected to the previous
= a separate bowl. `pa-no-ne-ko-mu` sentence-initial = location shift. `su'ma-zo-ra-ma`
= solid-state food materials (W113 + W144) = dry ingredients (flour, sugar, salt,
leavening). Juncture `'` marks `su'ma` as pre-bound: `[su'ma]-zo-ra-ma` = solid-
state-[food material].

---

### S662 — CKG-001-D

```
ma-ne-ki  lo-ki'ma-zo-ra-ma  ne  lo-su'ma-zo-ra-ma
```

**Written:** `maneki loki'mazorama ne losu'mazorama`

**Natural reading:** Combine [liquid food-materials] bonded-with [solid food-materials].

**Notes:** First double-patient construction in the corpus. `lo-X ne lo-Y` = patient X
bonded-to patient Y = X and Y jointly as the patient of the combining action. The
`ne` between the two `lo-NPs` marks them as a jointly constituted input; the
cook folds both ingredient classes together. The `ne` in `ma-ne-ki` (the verb)
compositionally anticipates the `ne` that joins its inputs.

---

### S663 — CKG-001-E

```
ki  lo-zo-ra-ma-su  pa-ko-ha-mu ;  la-ko-ha-mu  ha-ki  lo-zo-ra-ma-su  lu-ha-su
```

**Written:** `ki lozoramasu pakohamu ; lakohamu haki lozoramasu luhasu`

**Natural reading:** Move the structured food-matter to the oven; the oven heat-changes
the structured food-matter, result: thermally-set.

**Notes:** `;` separates placement (imperative) from baking (oven-as-agent). `zo-ra-ma-su`
= structured food material = the mixed dough ready for baking (W144 + `su`). `la-ko-ha-mu`
= artifact agency: the oven is the causal agent of thermal change; `la-` marks the oven
as the source of the transformation, not just the location. `ha-su` = thermally-structured
= heat-set state (composable: `ha` + `su`). `lu-ha-su` = result: heat-set.

---

### S664 — CKG-001-F

```
ki  lo-ha-zo-ra-ma ;  de-ha-ki ;  ha-zo-ra-ma  ne  be-su
```

**Written:** `ki lohazorama ; dehaki ; hazorama ne besu`

**Natural reading:** Move the thermally-treated food [from oven]; thermal decrease;
the thermally-treated food is completed-formation.

**Notes:** W216 (`ha-zo-ra-ma`) first attestation. Phase-change landmark: in S663 the
material was `zo-ra-ma-su` (raw dough); here, post-baking, it is `ha-zo-ra-ma` (thermally-
treated food = cookie). The vocabulary shift tracks the ontological change. `de-ha-ki` =
decay-heat-change = cooling (composable). `be-su` = growth-result-structure = completed
formation = the state of being a fully produced artifact. `ha-zo-ra-ma ne be-su` =
the baked good is complete.

---

## CKG-001 Batch Summary

**Entries:** S659–S664 · **New vocabulary:** W214 (`ko-ha-mu`), W215 (`ma-ne-ki`), W216 (`ha-zo-ra-ma`)

| Entry | Written form | Step | Key vocabulary |
|-------|-------------|------|----------------|
| S659 (CKG-001-A) | `haki lokohamu` | Preheat | W214 (`ko-ha-mu`) first att. |
| S660 (CKG-001-B) | `maneki loki'mazorama pakomu lusune` | Mix wet | W215 (`ma-ne-ki`) first att. |
| S661 (CKG-001-C) | `panonekomu maneki losu'mazorama` | Mix dry | `su'ma-zo-ra-ma` first use |
| S662 (CKG-001-D) | `maneki loki'mazorama ne losu'mazorama` | Combine | Double `lo-ne-lo` patient first att. |
| S663 (CKG-001-E) | `ki lozoramasu pakohamu ; lakohamu haki lozoramasu luhasu` | Bake | Artifact agency; `ha-su` |
| S664 (CKG-001-F) | `ki lohazorama ; dehaki ; hazorama ne besu` | Remove + cool | W216 (`ha-zo-ra-ma`) first att. |

---

## `su-ti` State and `wi-fe-ka` Rule Activation (S665–S671)

*Batch purpose (SUT-001): First-attest W101 (`su-ti`, state-snapshot predicate) and `wi-fe-ka` (rule-forbidden predicate) in corpus sentences, confirming `lo-X su-ti Y` state-configuration grammar and both agentless and policy-mediated prohibition forms.*

*New compounds attested this batch: W101 (`su-ti`).*

---

**S665 — Machine: currently inactive.** *(SUT-001-A)*

```
lo-ki  su-ti  no-ra
```

**Written:** `loki suti nora`

**Natural reading:** The machine is currently in an inactive configuration.

**Notes:** W101 (`su-ti`) first corpus attestation. `lo-X su-ti Y` = X is currently in state Y (static snapshot — no change implied). Y here is `no-ra` (zero-force = inactive, compositional). Compare `lo-ki  no-be` (the machine is not increasing — a *change* predicate); `lo-ki  su-ti  no-ra` = the machine holds the inactive state (a *snapshot* predicate). Resolves the open-questions.md note: "no primitive for stable condition without invoking change or evaluation."

---

**S666 — Machine: was powered previously.** *(SUT-001-B)*

```
lo-ki  su-ti-de  ra
```

**Written:** `loki sutide ra`

**Natural reading:** The machine's previous configuration was powered.

**Notes:** `su-ti-de` = past configuration (W101 + temporal suffix `-de` = past/decay). First attestation of the past-state derived form. Timeline: was powered (S666), is now inactive (S665).

---

**S667 — Machine: target state is powered.** *(SUT-001-C)*

```
lo-ki  su-ti-be  ra
```

**Written:** `loki sutibe ra`

**Natural reading:** The machine's target configuration is powered.

**Notes:** `su-ti-be` = expected future/target configuration (W101 + suffix `-be` = growth/expected). First attestation of the target-state derived form. The three sentences S665–S667 establish the full `su-ti` timeline vocabulary: current (`su-ti`), past (`su-ti-de`), target (`su-ti-be`). Batch narrative: currently inactive, was powered, target is to be powered again — S671 provides the mechanism.

---

**S668 — Power ramp is forbidden.** *(SUT-001-D)*

```
lo-be-ra  wi-fe-ka
```

**Written:** `lobera wifeka`

**Natural reading:** A power ramp is forbidden.

**Notes:** First corpus attestation of `wi-fe-ka` (W100 derived: willed-boundary as applied to a specific act = the act is prohibited by rule). Patient `be-ra` = growth-force = increasing power = power ramp (compositional). The agentless predicate form `lo-X wi-fe-ka` states the prohibition without naming the source; compare S670 which names the policy authority.

---

**S669 — Power decrease is not forbidden.** *(SUT-001-E)*

```
lo-no-be-ra  no-wi-fe-ka
```

**Written:** `lonobera nowifeka`

**Natural reading:** A power decrease is not forbidden.

**Notes:** `no-wi-fe-ka` = not-rule-forbidden = permitted (compositional: `no-` + `wi-fe-ka`). First attestation. Patient `no-be-ra` = no-growth-force = decreasing power. Minimal contrast with S668: the prohibited act (`be-ra`, ramp up) and the permitted act (`no-be-ra`, ramp down) differ only in one `no-` modifier. Instantiates the deontic identity: permitted ↔ not-forbidden.

---

**S670 — Protocol forbids power ramps.** *(SUT-001-F)*

```
la-wi-fe-su  ne  wi-fe-ka  lo-be-ra
```

**Written:** `lawifesu ne wifeka lobera`

**Natural reading:** The safety protocol forbids power ramps.

**Notes:** Extension of the DIP-001 rights-claim pattern (`la-X ne wi-fe lo-Y` = X holds rule over Y): `ne wi-fe-ka` attributes the prohibiting form specifically to the patient. `la-wi-fe-su ne wi-fe-ka lo-be-ra` = "The policy holds as rule-prohibited over power-ramps." Contrast with S668 (agentless predicate): same norm, different grammatical perspective — S670 locates the norm in an institutional authority.

---

**S671 — Machine regulates toward target state.** *(SUT-001-G)*

```
la-ki  wi-re  lu-su-ti-be
```

**Written:** `laki wire lusutibe`

**Natural reading:** The machine self-regulates toward its target configuration.

**Notes:** Connects W101 (`su-ti-be`, target state) with W099 (`wi-re`, feedback regulation), confirming the structural relationship noted in W101's registry entry: "a feedback loop is precisely the mechanism for moving `su-ti` from current state toward target `su-ti`." `lu-` = beneficiary/result slot: the regulation is done for the target state. Closes the batch narrative: currently inactive (S665), target powered (S667), feedback (S671) drives toward that target — subject to the no-ramp constraint (S668/S670).

---

## SUT-001 Batch Summary

| Entry | Tonesu | Written form | Key feature |
|-------|--------|-------------|-------------|
| S665 (SUT-001-A) | `lo-ki  su-ti  no-ra` | `loki suti nora` | W101 `su-ti` first att. |
| S666 (SUT-001-B) | `lo-ki  su-ti-de  ra` | `loki sutide ra` | `su-ti-de` first att. |
| S667 (SUT-001-C) | `lo-ki  su-ti-be  ra` | `loki sutibe ra` | `su-ti-be` first att. |
| S668 (SUT-001-D) | `lo-be-ra  wi-fe-ka` | `lobera wifeka` | `wi-fe-ka` first att. (agentless) |
| S669 (SUT-001-E) | `lo-no-be-ra  no-wi-fe-ka` | `lonobera nowifeka` | `no-wi-fe-ka` first att. |
| S670 (SUT-001-F) | `la-wi-fe-su  ne  wi-fe-ka  lo-be-ra` | `lawifesu ne wifeka lobera` | policy-as-agent prohibition |
| S671 (SUT-001-G) | `la-ki  wi-re  lu-su-ti-be` | `laki wire lusutibe` | W099 + W101 structural link |

**Coverage:** First attestations of W101 (`su-ti`) and all three temporal state forms (`su-ti` / `su-ti-de` / `su-ti-be`); `wi-fe-ka` (forbidden predicate, agentless) and `no-wi-fe-ka` (permitted); policy-as-agent prohibition form; W099 + W101 target-state regulation link.

**Gaps:** opens path to capability vs. permission modality follow-up (`be-vo` axis untested — see testing-ideas.md).

---

## Ars Goetia — Solomonic Binding Narrative (S672–S677)

*Batch purpose (SOL-001): First-attest W217 (`wi-ra-li`, spirit/directed-force-agent) and W218 (`ka-be-ne`, binding/deliberate bond-creation) in corpus sentences. Source: the framing narrative of the Ars Goetia (Lesser Key of Solomon). Tests: authority construction via DIP-001 `ne`+property pattern, numeral phrase in patient slot, result slot as destination (`lu-ko-mu`), instrumental `go-si`, proper-name agent and group NP, and causal nominalization with juncture (`go-ka-no-ko'ko-mu`).*

*New compounds attested this batch: W217 (`wi-ra-li`), W218 (`ka-be-ne`).*

---

**S672 — Solomon held authority over 72 spirits.** *(SOL-001-A)*

```
la-Solomon  ne  wi-ra  lo-yom bun nu wi-ra-li
```

**Written:** `laSolomon ne wira loyom bun nu wirali`

**Natural reading:** Solomon held authority over 72 spirits of directed power.

**Notes:** Authority construction via DIP-001 pattern: `la-X  ne  wi-ra  lo-Y` = X holds directed-power over Y. `wi-ra` (W177) serves as the mediating property connecting agent to patient via `ne`. Numeral phrase in patient position: `lo-yom bun nu wi-ra-li` = "patient: 72 (7·10+2) directed-force-agents." The `lo-` prefix attaches to `yom`, the first element of the number phrase; `wi-ra-li` (W217) is the patient head. W217 first attestation.

---

**S673 — He bound them into a vessel.** *(SOL-001-B)*

```
la-Solomon  ka-be-ne  lo-wi-ra-li  lu-ko-mu
```

**Written:** `laSolomon kabene lowirali lukomu`

**Natural reading:** Solomon bound the spirits, confining them in a vessel.

**Notes:** W218 (`ka-be-ne`, deliberate bond-creation) first corpus attestation. `lu-ko-mu` uses the result/beneficiary slot as a spatial destination: the vessel is what the binding produces/fills. The antonym `ka-ne-de` (W092, deliberate bond dissolution) gives the full bind/unbind pair.

---

**S674 — He sealed the vessel with his sign.** *(SOL-001-C)*

```
la-Solomon  ka-fe-si  lo-ko-mu  go-si
```

**Written:** `laSolomon kafesi lokomu gosi`

**Natural reading:** Solomon sealed the vessel with his sign.

**Notes:** `ka-fe-si` = deliberately-impose-boundary-signal = seal (compositional: `ka` + `fe-si` W024; no registry entry). `go-si` = "by means of / originating from signal" = instrumental use of `go-`. The causal origin of the sealing is Solomon's sign/mark; agent identity makes `si` unambiguous.

---

**S675 — The Babylonians found the vessel.** *(SOL-001-D)*

```
la-li-Bavel  se-ka  lo-ko-mu
```

**Written:** `laliBavel seka lokomu`

**Natural reading:** The Babylonians found the vessel through investigation.

**Notes:** `li-Bavel` = person-of-Bavel = Babylonian (Bavel = Hebrew name for Babylon). Group NP with `la-` agent prefix: Babylonians-as-agent. W034 (`se-ka`, examination/deliberate inspection) fits: the Babylonians were excavating the buried pit deliberately, not stumbling upon it.

---

**S676 — They opened it.** *(SOL-001-E)*

```
la-li-Bavel  ka-no-ko  lo-ko-mu
```

**Written:** `laliBavel kanoko lokomu`

**Natural reading:** The Babylonians opened the vessel.

**Notes:** `ka-no-ko` = deliberately-act-toward-no-containment = open a sealed container. Compositional: `ka` (deliberate) + `no` (negation) + `ko` (containment/interior). No new vocabulary required.

---

**S677 — The spirits came forth.** *(SOL-001-F)*

```
la-wi-ra-li  ki  go-ka-no-ko'ko-mu
```

**Written:** `lawirali ki gokanoko'komu`

**Natural reading:** The spirits moved forth, [released by] the opening of the vessel.

**Notes:** `go-ka-no-ko'ko-mu` = "caused by [the opening]-of-[the vessel]." First `go-[action'object]` causal nominalization in the corpus: `'` juncture binds the action compound `ka-no-ko` to its object `ko-mu`; `go-` takes the resulting nominalized event as its causal argument. `ki` (motion, primitive) — direction unspecified; narrative context supplies the outward reading.

---

## SOL-001 Batch Summary

| Entry | Tonesu | Written form | Key feature |
|-------|--------|-------------|-------------|
| S672 (SOL-001-A) | `la-Solomon  ne  wi-ra  lo-yom bun nu wi-ra-li` | `laSolomon ne wira loyom bun nu wirali` | W217 `wi-ra-li` first att. |
| S673 (SOL-001-B) | `la-Solomon  ka-be-ne  lo-wi-ra-li  lu-ko-mu` | `laSolomon kabene lowirali lukomu` | W218 `ka-be-ne` first att. |
| S674 (SOL-001-C) | `la-Solomon  ka-fe-si  lo-ko-mu  go-si` | `laSolomon kafesi lokomu gosi` | `ka-fe-si` seal; instrumental `go-si` |
| S675 (SOL-001-D) | `la-li-Bavel  se-ka  lo-ko-mu` | `laliBavel seka lokomu` | proper-name group NP |
| S676 (SOL-001-E) | `la-li-Bavel  ka-no-ko  lo-ko-mu` | `laliBavel kanoko lokomu` | `ka-no-ko` = open |
| S677 (SOL-001-F) | `la-wi-ra-li  ki  go-ka-no-ko'ko-mu` | `lawirali ki gokanoko'komu` | causal nominalization with `'` |

**Coverage:** W217 (`wi-ra-li`) and W218 (`ka-be-ne`) first attested; authority-over construction (`ne` + property + `lo-` patient); numeral phrase in patient position; `lu-` as spatial destination; instrumental `go-si`; proper-name group NP; first `go-[action'object]` causal nominalization.

**Key finding:** The Ars Goetia binding narrative translates into six clean sentences with two new compounds. S677's `go-ka-no-ko'ko-mu` demonstrates that `'` juncture can bind an action to its object inside a `go-` causal frame — causal nominalization is available without new grammar.

---

## Greater Key of Solomon — Ritual Preparations (S678–S683)

*Batch purpose (SOL-002): Translate the preparation ritual of the Clavicula Salomonis (Book II): timed ritual operations, purification, white garments, instrument-making, consecration, and the first pentacle description. Key tests: proper-noun time-slot pattern (`ti-re-Saturn`, `ti-re-Mercury`), `ne ne-fe` prescription framing, `ka-fe-vo` compositional consecration, W137 (`vo-mu`, garment) activation from proposed → active, W219 (`fe-vo'si-ko-mu`, pentacle/consecrated inscribed object) first attestation.*

*New compounds attested this batch: W137 (`vo-mu`, activated), W219 (`fe-vo'si-ko-mu`).*

---

**S678 — Begin the work in the Saturn hour.** *(SOL-002-A)*

```
ti-re-Saturn : la-to-ra-li  ka  lo-wi-ka
```

**Written:** `tireSaturn : latorali ka lowika`

**Natural reading:** In the Saturn time-slot, the practitioner performs the ritual work.

**Notes:** First use of the proper-noun time-slot pattern: `ti-re-[Planet]` = the recurring time-slot attributed to that planet by tradition. `ti-re` (W103, recurring time / scheduled cycle) is modified by the proper noun `Saturn` as a tradition label — the sentence does NOT assert that Saturn cosmologically governs the hour; it names the slot by received convention. The `:` topic frame (`[topic] : [comment-clause]`) handles temporal framing: "as for the Saturn time-slot: perform the ritual." `wi-ka` (W054) as patient = "the ritual work." `to-ra-li` (W207, wizard/mage) = the ritual practitioner.

---

**S679 — Maintain purity for three days.** *(SOL-002-B)*

```
gal nu lu-ti : la-to-ra-li  ne  ne-fe  ka-no-de-su  lo-su-ti
```

**Written:** `gal nu luti : latorali ne nefe kanodesu losuti`

**Natural reading:** For three day-periods, the practitioner must cleanse their current state.

**Notes:** Duration topic frame: `gal nu lu-ti` (three day-units, using `lu-ti` W140) as the sentence-initial topic = "for three days." `ne ne-fe` = holds as requirement (positive prescription, DIP-001/SUT-001 pattern extension). `ka-no-de-su  lo-su-ti` = "deliberately remove fault from [this person's] current state" — `su-ti` (W101) used reflexively as the object of purification: the practitioner's current state is what must be cleansed. Connects W120 (forgiveness/removal-of-fault) with W101 (state-snapshot) in a purification context.

---

**S680 — Wear clean white garments.** *(SOL-002-C)*

```
la-to-ra-li  ne  ne-fe  lo-yim-vo-mu
```

**Written:** `latorali ne nefe loyimvomu`

**Natural reading:** The practitioner must [wear] white garments.

**Notes:** W137 (`vo-mu`) first corpus attestation — status promoted from proposed (⚠️) to active (✅). `yim-vo-mu` = white-garment compound: `yim` (CVC color, white) modifies `vo-mu` (W137, garment). `ne ne-fe lo-yim-vo-mu` = "holds as requirement: white garments." The `lo-` prefix on the required object marks what is required rather than what is acted upon — the garment is the thing the requirement bears on (wear/have/be-in-relation-with), with the precise relational mode determined by context. First attestation of color `yim` (white) in a compound modifier position.

---

**S681 — Make the instruments in the Mercury hour.** *(SOL-002-D)*

```
ti-re-Mercury : la-to-ra-li  ka  lu-ka-mu
```

**Written:** `tireMercury : latorali ka lukamu`

**Natural reading:** In the Mercury time-slot, the practitioner makes the instruments.

**Notes:** Second use of the `ti-re-[Planet]` pattern — confirming it is productive across the planetary-hour system without requiring separate entries per planet. `lu-ka-mu` = result slot: instruments — "acts, producing/resulting in instruments" = makes/prepares the instruments. Compare `lu-ko-mu` from S673 (result as container for bound spirits) — here `lu-` carries a creation result. The pair S678/S681 establishes that the planetary-hour system maps onto distinct `ti-re` slots by proper-noun modification.

---

**S682 — Consecrate the instruments through ritual.** *(SOL-002-E)*

```
la-to-ra-li  ka-fe-vo  lo-ka-mu  go-wi-ka
```

**Written:** `latorali kafevo lokamu gowika`

**Natural reading:** The practitioner consecrates the instruments through ritual.

**Notes:** `ka-fe-vo` = deliberately make sacred = consecrate. Compositional: `ka` (deliberate action) + `fe-vo` (W065, sacredness / set-apart quality). No new registry entry required — the composition is transparent. `go-wi-ka` = "by means of / originating from ritual" (W054, ritual / structured intentional practice) = instrumental `go-` with the ritual as the causal mechanism. `lo-ka-mu` = patient: the instruments. The three-stage preparation: make instruments in Mercury hour (S681) → consecrate through ritual (S682) → use the resulting pentacle (S683).

---

**S683 — The pentacle of Saturn holds power over its spirits.** *(SOL-002-F)*

```
la-fe-vo'si-ko-mu-Saturn  ne  wi-ra  lo-wi-ra-li-Saturn
```

**Written:** `lafevo'sikomuSaturn ne wira lowiraliSaturn`

**Natural reading:** The pentacle of Saturn holds directed power over the spirits of Saturn.

**Notes:** W219 (`fe-vo'si-ko-mu`, consecrated inscribed object / pentacle) first corpus attestation. The `'` juncture is mandatory — without it the chain defaults to right-branching `fe-[vo-si-ko-mu]` (a "value-document-vessel" reading), which loses the sacredness feature. With the juncture: `[fe-vo]'[si-ko-mu]` = [[sacred]-[inscribed-artifact]] = pentacle. Proper-noun modification: `-Saturn` appended to both the pentacle (`fe-vo'si-ko-mu-Saturn` = the Saturn-attributed pentacle) and the spirits (`wi-ra-li-Saturn` = Saturn's spirits) — the planet name is a tradition-label, not a metaphysical claim. The authority construction `ne wi-ra lo-Y` is the same pattern as S672 (Solomon's authority over spirits) — the pentacle functions as a non-person authority holder.

---

## SOL-002 Batch Summary

| Entry | Tonesu | Written form | Key feature |
|-------|--------|-------------|-------------|
| S678 (SOL-002-A) | `ti-re-Saturn : la-to-ra-li  ka  lo-wi-ka` | `tireSaturn : latorali ka lowika` | `ti-re-[Planet]` pattern first use |
| S679 (SOL-002-B) | `gal nu lu-ti : la-to-ra-li  ne  ne-fe  ka-no-de-su  lo-su-ti` | `gal nu luti : latorali ne nefe kanodesu losuti` | duration topic + `ne ne-fe` prescription |
| S680 (SOL-002-C) | `la-to-ra-li  ne  ne-fe  lo-yim-vo-mu` | `latorali ne nefe loyimvomu` | W137 `vo-mu` first att. (→ active) |
| S681 (SOL-002-D) | `ti-re-Mercury : la-to-ra-li  ka  lu-ka-mu` | `tireMercury : latorali ka lukamu` | `ti-re-[Planet]` confirmed productive |
| S682 (SOL-002-E) | `la-to-ra-li  ka-fe-vo  lo-ka-mu  go-wi-ka` | `latorali kafevo lokamu gowika` | `ka-fe-vo` consecration; `go-[ritual]` instrumental |
| S683 (SOL-002-F) | `la-fe-vo'si-ko-mu-Saturn  ne  wi-ra  lo-wi-ra-li-Saturn` | `lafevo'sikomuSaturn ne wira lowiraliSaturn` | W219 `fe-vo'si-ko-mu` first att. |

**Coverage:** `ti-re-[Planet]` proper-noun time-slot pattern (S678, S681); `ne ne-fe` prescription framing (S679, S680); W137 (`vo-mu`, garment) activated from proposed; W219 (`fe-vo'si-ko-mu`, pentacle) first attested; `ka-fe-vo` compositional consecration; non-person authority holder (pentacle as `ne wi-ra lo-Y` subject).

**Key finding:** The Greater Key's planetary-hour timing system compresses into a single productive pattern (`ti-re-[Planet]`) without importing Western astrology's cosmological ontology. The ritual preparation arc (time → purify → dress → make instruments → consecrate → use) translates into six sentences using exclusively existing vocabulary plus one new artifact class.

---

## Proof Structure: Syllogism, Cogito, Reductio (S684–S689)

*Batch purpose (PRF-001): First test of multi-step deductive chains using `go`. Tests the `a-` universal scope prefix in a major syllogistic premise, stacked double-`go {P}, go {P}, C` conclusion, `;` vs `go` distinction as a minimal contrast pair (Humean constant conjunction vs necessary connection), Descartes' Cogito using `go` as epistemic grounding, and reductio ad absurdum structure. No new vocabulary — pure grammar and connective test. Full analysis in `corpus/translations/Philosophy/proof-structure.md`.*

---

### S684 — PRF-001-A

```
a-zo-li  ne  de-zo
```

**Written:** `azoli ne dezo`

**Natural reading:** All persons are mortal.

**Notes:** First corpus use of the `a-` scope prefix in a syllogistic major premise. `a-zo-li` = universal-person = "persons in the abstract / all persons" — `a-` attaches to `zo-li` (W049) to yield the universally-quantified subject. `ne  de-zo` = property attribution: the property of dying/mortality (W178, non-agentive death-event). `a-zo-li ne de-zo` = "the universally-quantified person has the property of mortality." The major premise of the classical syllogism — All men are mortal (Aristotle).

---

### S685 — PRF-001-B

```
la-Sokrates  ne  zo-li
```

**Written:** `laSokrates ne zoli`

**Natural reading:** Socrates is a person.

**Notes:** Minor premise of the classical syllogism. `Sokrates` = phonologically adapted proper name (Greek /Sōkrátēs/ → Tonesu `Sokrates`, stress-initial, five-letter adaptation). `la-Sokrates ne zo-li` = agent-Sokrates has-property person-agent (W049). Straightforward property attribution using an existing agent.

---

### S686 — PRF-001-C

```
go  a-zo-li  ne  de-zo ,  go  la-Sokrates  ne  zo-li ,  la-Sokrates  ne  de-zo
```

**Written:** `go azoli ne dezo, go laSokrates ne zoli, laSokrates ne dezo`

**Natural reading:** Because all persons are mortal, and because Socrates is a person: Socrates is mortal.

**Notes:** First stacked double-`go {P}, go {P}, C` in corpus. Stack trace: first `go` opens a subordinate clause level; `ne de-zo` (the complete predicated property of `a-zo-li`) closes the first `go` frame at the `,`; second `go` opens another subordinate clause level; `ne zo-li` closes the second frame at the `,`; matrix clause `la-Sokrates ne de-zo` is the syllogistic conclusion. Both premises are necessary — removing either leaves the conclusion unsupported. The `ne` copula form closes the `go` frame in formal register because the property-attribution clause is syntactically complete once the predicated property (a closed NP) is consumed. The `,` makes the boundary explicit.

---

### S687 — PRF-001-D

```
la-li  to-ki ;  lo-li  su-ti
```

**Written:** `lali toki ; loli suti`

**Natural reading:** I am reasoning; I am in a current state.

**Notes:** Intentionally weaker form of the Cogito. `;` = Humean constant conjunction — two sequential observations recorded without any claim that the first grounds the second. `la-li to-ki` = I am engaged in the computation/reasoning process (W020). `lo-li su-ti` = the entity marked 'I' has a current configuration/state (W101, patient frame: `lo-li` as the entity-in-configuration). The sentence is true but philosophically insufficient: it records that thinking and existing co-occur in sequence, without asserting the constitutive relationship between them. Compare S688.

---

### S688 — PRF-001-E

```
go {la-li  to-ki},  lo-li  su-ti
```

**Written:** `go lali toki, loli suti`

**Natural reading:** Because I am reasoning: I have a determinate present state.

**Notes:** Correct Cogito (Descartes, *Meditationes*, 1641). `go` = epistemic grounding — the reasoning in the premise clause is the constitutive ground for the existence-claim in the matrix clause, not merely its temporal precursor. `lo-li su-ti` (patient frame, no specified state Y) = "the entity marked 'I' has some current configuration" = "I exist with a determinable present state." Self-certifying: the act of uttering this sentence instantiates `la-li to-ki` (I am reasoning), which via `go` grounds `lo-li su-ti` (I am currently configured). The minimal-pair contrast with S687 is the sharpest expression of Hume's problem of induction in the corpus: `;` records conjunction; `go` asserts the ground.

---

### S689 — PRF-001-F

```
to-go {no-ki},  no-re ;  re  su-ti ;  go  to ,  ki
```

**Written:** `togo noki, nore ; re suti ; go to, ki`

**Natural reading:** If there were no motion, there would be no cyclic recurrence. Cyclic recurrence [currently] obtains. By the foregoing principle: motion.

**Notes:** Reductio ad absurdum structure in three clauses joined by `;`. Clause 1: `to-go {no-ki}, no-re` = counterfactual conditional — if motion-absence held: no cyclic recurrence. This is the non-actual conditional (W089, `to-go` frame) establishing the principle. Clause 2: `re su-ti` = empirical observation — the primitive `re` (recurrence/cycle) has a present configuration, i.e., cycles are currently instantiated and observable. Clause 3: `go to , ki` = logical conclusion — `to` (conceptual/pattern, anaphoric: refers to the principle of clause 1), `go to,` = "grounded in the stated pattern/principle," `ki` = change/motion [obtains]. The reductio: hypothetically there is no motion → no cycles; but cycles are observed; therefore motion obtains. The `;` joins the three argumentative steps sequentially (Humean conjunction between steps); `go to,` marks only the final conclusion as logically grounded in the established principle. First three-clause complex argument sentence; first reductio structure in corpus.

---

## PRF-001 Batch Summary

| Entry | Tonesu | Written form | Key feature |
|-------|--------|-------------|-------------|
| S684 (PRF-001-A) | `a-zo-li  ne  de-zo` | `azoli ne dezo` | First `a-` scope prefix in syllogistic major premise |
| S685 (PRF-001-B) | `la-Sokrates  ne  zo-li` | `laSokrates ne zoli` | Minor syllogistic premise with proper name |
| S686 (PRF-001-C) | `go  a-zo-li  ne  de-zo ,  go  la-Sokrates  ne  zo-li ,  la-Sokrates  ne  de-zo` | `go azoli ne dezo, go laSokrates ne zoli, laSokrates ne dezo` | First stacked double-`go {P}, go {P}, C` |
| S687 (PRF-001-D) | `la-li  to-ki ;  lo-li  su-ti` | `lali toki ; loli suti` | Cogito wrong form — `;` constant conjunction |
| S688 (PRF-001-E) | `go {la-li  to-ki},  lo-li  su-ti` | `go lali toki, loli suti` | Cogito correct — `go` epistemic grounding |
| S689 (PRF-001-F) | `to-go {no-ki},  no-re ;  re  su-ti ;  go  to ,  ki` | `togo noki, nore ; re suti ; go to, ki` | First reductio; `go to,` anaphoric conclusion |

**Coverage:** `a-` universal scope prefix in a deductive premise (S684); stacked `go {P}, go {P}, C` (S686); `;` vs `go` minimal pair for the Humean/Cartesian distinction (S687/S688); `to-go` counterfactual + `go to,` anaphoric conclusion in reductio structure (S689). No new vocabulary entries — pure grammar and connective test.

**Key finding:** The `;` / `go` distinction is the sharpest distinction in the corpus. `;` = constant conjunction (Hume): two states recorded in sequence. `go` = necessary connection: the premise constitutively grounds the consequence. S687/S688 are minimal pairs on exactly this axis — same propositional content, different logical structure. The Cogito works in Tonesu only with `go`, not `;`.

---

## Lojban Type Contrasts (S690–S695)

*Batch purpose (LOJ-001): Structural comparison against Lojban's distinctive type machinery (CLL, lojban.org). Tests six canonical Lojban features against Tonesu's grammar: `su'o` existential quantification (`i-` prefix vs `a-` universal from S684); `lo nu X` event nominalization (Tonesu's causal-frame approach vs Lojban's first-class event nominal); `na` vs `na'e` claim/predicate negation scope (Tonesu's five-level negation system); `jinvi` + `du'u` belief attribution (`to` primitive frame); `djuno` + `du'u` knowledge attribution (`to-su` organized knowledge frame); `la-li to-su {to-si ...}` embedded indirect question (Tonesu's `to-si` gap-filler inside a propositional frame — first corpus attempt). No new vocabulary — structural analysis batch. Full analysis in `corpus/translations/Philosophy/lojban-type-contrasts.md`.*

---

### S690 — LOJ-001-A

```
i-zo-li  ne  de-zo
```

**Written:** `izoli ne dezo`

**Natural reading:** A particular person is mortal.

**Notes:** Existential reading via `i-` (precise/particular scope prefix): "the particular-persons [that exist here] have the mortality property." Contrast with S684 (`a-zo-li ne de-zo` = ALL persons are mortal, universal via `a-`). The `i-` prefix narrows to particulars; the `a-` prefix expands to abstract universals. Lojban encodes this distinction as `su'o prenu cu morsi` (at least one person is mortal = existential, `su'o`) vs `ro prenu cu morsi` (all persons are mortal, `ro`). Tonesu's scope-prefix system (`i-` = precise/particular ≈ existential particularity; `a-` = abstract/universal ≈ `ro`) achieves the same type distinction through a different mechanism — scope prefix on the argument rather than independent pre-argument quantifier words. First explicit existential-scope use of `i-` in the corpus; completes the universal/existential quantification pair.

---

### S691 — LOJ-001-B

```
go {la-li  ki},  la-li  ne  fa-vo
```

**Written:** `go lali ki, lali ne favo`

**Natural reading:** Because I move: I have happiness.

**Notes:** Test of event nominalization under causal framing. Lojban equivalent: `lo nu mi klama cu pluka mi` ("the event of my going pleases me") — where `lo nu mi klama` is a first-class nominal (the event of going as a subject that predicts pleasure). Tonesu does not have a dedicated event-nominalization operator. The causal frame `go {X}, Y` routes the same semantic content: the event clause `la-li ki` is the cause; `la-li ne fa-vo` (I have happiness) is the effect. Truth-conditionally equivalent, type-structurally different: Lojban makes the event a noun; Tonesu makes it a cause. The obligatory shift to causal framing is not a failure — it encodes an epistemic commitment that Lojban's neutral `pluka` does not: Tonesu's `go` asserts a constitutive grounding relationship, not merely correlation. Lojban's `lo nu X cu pluka Y` leaves the exact relationship type unspecified; Tonesu specifies it as causal. First explicit corpus test of this Lojban/Tonesu structural divergence.

---

### S692 — LOJ-001-C

```
la-su-mu  ne  no-pom
```

**Written:** `lasumu ne nopom`

**Natural reading:** The structure-artifact has the not-blue property.

**Notes:** Predicate negation (maps to Lojban `na'e`). `su-mu` = structural artifact = building/constructed object (compositional: `su` [structure] + `mu` [artifact], no W-entry needed). `no-pom` = not-blue (Level 1 negation: `no-` prefix on the color anchor `pom`). `la-su-mu ne no-pom` = "the building holds the non-blue property as a predicate" — the building EXISTS and has a determinable color, which is not-blue. This is Lojban's `na'e blanu` ("is other-than-blue"): the predicate is negated, not the claim. The building definitely has a color; it is simply not the blue one. Compare S693 (claim negation). Tonesu Level 1 negation (root/compound prefix) is structurally the closest analogue to Lojban's scalar `na'e` negation — both negate at the predicate level and leave the subject's existence unaffected.

---

### S693 — LOJ-001-D

```
no  la-su-mu  ne  pom
```

**Written:** `no lasumu ne pom`

**Natural reading:** Not: [the structure-artifact is blue].

**Notes:** Claim negation (maps to Lojban `na`). Fronted `no` denies the entire proposition — the whole predication `la-su-mu ne pom` fails. Established by S550 precedent (`no la-li ne vo` = "not: person has worth"). Lojban: `lo zdani na blanu` ("the house is-not blue"). Minimal pair with S692: same words, different scope. S692 (`la-su-mu ne no-pom`) says: the building has a non-blue property — it exists with a determinable color that isn't blue. S693 (`no la-su-mu ne pom`) says: the proposition that the building is blue is false — no color attribution is being made, merely the positive claim is denied. Tonesu's five-level negation system captures both Lojban's `na` (claim negation → fronted `no`) and `na'e` (scalar/predicate negation → `no-X` root prefix) without introducing new particles. Lojban's `to'e` (polar opposite = anti-blue) is not directly mapped by the current system — that would require explicit polar compound specification (`pom-fe`? or the complementary color).

---

### S694 — LOJ-001-E

```
la-li  to  {la-Sokrates  ne  de-zo}
```

**Written:** `lali to laSokrates ne dezo`

**Natural reading:** I hold [that Sokrates is mortal] as my conception.

**Notes:** Propositional belief attribution (maps to Lojban `mi jinvi lo du'u la .sokrates. morsi`). `to` (primitive: thought/concept/pattern) + `{proposition}` as the belief-content frame. Established in the counterfactual attribution spec: `la-X to {P}` = X holds as their conceptual model that P. Here applied to a contingent historical belief. `to` marks the proposition as privately held by the agent — not asserted as fact. Lojban uses `jinvi` (to opine, to have a personal view) + `du'u` (proposition abstraction) for this. Tonesu uses `to` (primitive conceptual commitment) + `{braced clause}`. The proposition `{la-Sokrates ne de-zo}` is held inside a private epistemic frame; it is not asserted by the sentence itself. Compare S695 (established knowledge).

---

### S695 — LOJ-001-F

```
la-li  to-su  {la-Sokrates  ne  de-zo}
```

**Written:** `lali tosu laSokrates ne dezo`

**Natural reading:** I have organized knowledge [that Sokrates is mortal].

**Notes:** Propositional knowledge attribution (maps to Lojban `mi djuno lo du'u la .sokrates. morsi`). `to-su` (W030, organized knowledge/framework) + `{proposition}` as the knowledge-content frame. First extension of `to-su` into the propositional knowledge-attribution pattern: `la-li to-su {P}` = I have established, structured knowledge that P. The `to` / `to-su` distinction is Tonesu's analogue of Lojban's `jinvi` / `djuno` distinction: `la-li to {P}` = I believe P (private, uncommitted conception); `la-li to-su {P}` = I know P (organized, established epistemic structure). This is the JTB-style distinction (justified true belief vs knowledge) mapped onto Tonesu's epistemic grain. Provisional status: this is the first corpus sentence using `to-su` with a braced proposition. The `to-su {P}` pattern may need a second attestation before becoming fully confirmed grammar; development noted in open-questions.md.

---

## LOJ-001 Batch Summary

| Entry | Tonesu | Written form | Key feature |
|-------|--------|-------------|-------------|
| S690 (LOJ-001-A) | `i-zo-li  ne  de-zo` | `izoli ne dezo` | `i-` existential scope (Lojban `su'o`) |
| S691 (LOJ-001-B) | `go {la-li  ki},  la-li  ne  fa-vo` | `go lali ki, lali ne favo` | Event via causal frame (Lojban `lo nu`) |
| S692 (LOJ-001-C) | `la-su-mu  ne  no-pom` | `lasumu ne nopom` | Predicate negation (Lojban `na'e`) |
| S693 (LOJ-001-D) | `no  la-su-mu  ne  pom` | `no lasumu ne pom` | Claim negation (Lojban `na`) |
| S694 (LOJ-001-E) | `la-li  to  {la-Sokrates  ne  de-zo}` | `lali to laSokrates ne dezo` | Belief attribution (`to`, Lojban `jinvi`) |
| S695 (LOJ-001-F) | `la-li  to-su  {la-Sokrates  ne  de-zo}` | `lali tosu laSokrates ne dezo` | Knowledge attribution (`to-su`, Lojban `djuno`) |

**Coverage:** `i-` as existential scope prefix (S690, completing universal/existential pair with S684); causal-frame as event-nominalization substitute (S691); claim vs predicate negation scope distinction (S692/S693, Lojban na/na'e); belief vs organized knowledge in propositional attitude (S694/S695, Lojban jinvi/djuno + du'u). No new vocabulary.

**Key finding:** Lojban's type machinery maps onto Tonesu through structural redirections rather than direct analogues. The `lo nu X` event nominal becomes a causal clause; the `na`/`na'e` distinction already exists in the five-level negation system; the `jinvi`/`djuno` belief-knowledge distinction maps to `to` vs `to-su`. The one genuine gap: Lojban's `tanru` (underdetermined compound) cannot be reproduced in Tonesu — every compound is compositionally specified. This is a design choice, not a deficiency: Tonesu demands disambiguation at the point of construction.

---

## EXO-002 — Exodus 7:8–12 — Aaron's Staff and the Sorcerers

*Batch purpose (EXO-002): Staff-and-serpent confrontation: Aaron's staff transforms into a snake before Pharaoh; the Egyptian sorcerers replicate by their secret arts; Aaron's serpent devours theirs. Key tests: categorical transformation via three-clause `;` sequential chain (`zo-su-mu ki ; ne zo-ki-ma`); first use of `zo-ki-ma` (W220, snake genus term) and `zo-su-mu` (W221, staff/wooden implement); `to-ra-li` (W207) and `wi-ra-su` (W179) in Biblical register; instrumental `go-si`; `ko-de` (engulf-and-consume / swallow); `wi-fe-ki` (harden one's will); first proper-name attestations `na-Aharon` and `na-Faro`. Full analysis in `corpus/translations/Bible/exodus-7-staff-serpents.md`.*

---

### S696 — EXO-002-A

```
la-na-Aharon  ka  lo-zo-su-mu ;  zo-su-mu  ki ;  ne  zo-ki-ma
```

**Written:** `lanaAharon ka lozosumu; zosumu ki; ne zokima`

**Natural reading:** Aaron cast the staff; the staff changed; [it was] a snake.

**Notes:** Three-clause sequential chain via `;` (constant conjunction without causal claim): (1) Aaron deliberately-acted on the staff = cast it; (2) the staff underwent change/motion event; (3) resulting state: [it was] snake. `ka  lo-X` = perform a deliberate action on X. `zo-su-mu` (W221) = staff/wooden implement. `ki` = primitive motion/change event (intransitive — the staff itself changed). `ne  zo-ki-ma` = copula + snake = the resulting-state predication. `zo-ki-ma` (W220) = snake/serpent; first attestation of both new words. `na-Aharon` = Aaron, first proper-name attestation in corpus. The mechanism of transformation is not specified — `ki` (change) leaves the agent of transformation implicit (theologically: divine). The three-clause chain is necessitated by Tonesu's lack of a 'become' verb: the change event and the resulting state are separate clauses. This is a key structural finding: Tonesu cannot render "X became Y" in a single clause; it must decompose into change-event + result-copula.

---

### S697 — EXO-002-B

```
la-na-Faro  si-ki  lo-to-ra-li
```

**Written:** `lanaFaro siki lotorali`

**Natural reading:** Pharaoh directed a summons to the sorcerers.

**Notes:** `na-Faro` = Pharaoh; first proper-name attestation (Hebrew: Par'oh). `si-ki` = directed signal = summons/call (signal aimed at a recipient). `lo-to-ra-li` = patient: the sorcerers/magicians. `to-ra-li` (W207) = knowledge-force-agent = wizard/sorcerer — first attestation in Exodus/Biblical register; the same compound covers D&D wizards (DND-004) and Egyptian magicians equally. This tests whether W207 generalizes beyond its fantasy-genre origin into a historical/religious text genre; it does. The sentence is structurally minimal: authority figure issues a directed signal to subordinates.

---

### S698 — EXO-002-C

```
la-to-ra-li  ka  lo-zo-su-mu-ne  go-si  wi-ra-su
```

**Written:** `latorali ka lozosumune gosi wirasu`

**Natural reading:** The sorcerers cast their staffs by means of their secret arts.

**Notes:** `lo-zo-su-mu-ne` = patient: their staffs; `ne` (bond/connection) appended as possessive = the staffs bonded to them. `go-si` = signal-means = "by way of / by means of" (instrumental particle, established in SOL-001). `wi-ra-su` (W179) = systematic-directed-force-practice = magic/secret arts — first attestation in Biblical register. The sentence leaves what was done with the staffs implicit (the action outcome is the parallel transformation in S699). The phrase `go-si  wi-ra-su` = "by means of systematic magical practice" maps to Hebrew `b'lahateihem` (by their enchantments / secret arts). Note: in Tonesu, `wi-ra-su` is a body of practice (magic as a system), not a specific spell or force-event; `go-si` marks it as the means by which the action was executed.

---

### S699 — EXO-002-D

```
zo-su-mu-ne  ki ;  ne  zo-ki-ma
```

**Written:** `zosumune ki; ne zokima`

**Natural reading:** Their staffs changed; [they were] snakes.

**Notes:** Subject-initial, agentless parallel transformation chain: mirrors the second two clauses of S696 but applied to the sorcerers' staffs (`zo-su-mu-ne` = their staffs). The two-clause `;` chain (`ki ; ne zo-ki-ma`) is the exact structural echo of S696's clauses 2–3. The structural parallel between S696 and S699 is the key syntactic finding: the same transformation pattern applies to both Aaron's staff and the sorcerers' staffs, encoded by the same `;` chain form. The structural symmetry makes the competition explicit: two instances of the same pattern, set up for the decisive outcome in S700.

---

### S700 — EXO-002-E

```
la-zo-ki-ma-na-Aharon  ko-de  lo-zo-su-mu-ne
```

**Written:** `lazokimanaAharon kode lozosumune`

**Natural reading:** Aaron's snake consumed their staffs.

**Notes:** `zo-ki-ma-na-Aharon` = Aaron's-serpent = the transformed serpent belonging to Aaron (possessive chain: thing + `na-` + name). `ko-de` = containment-decrease = engulf-and-consume = devour/swallow (compositional, 2-root, below CLQ threshold). `lo-zo-su-mu-ne` = patient: their staffs. The sentence follows the Hebrew source text (Exodus 7:12b: "Aaron's staff swallowed up their staffs") in using `zo-su-mu-ne` (staffs) as the patient rather than `zo-ki-ma-ne` (their snakes) — the Hebrew text reverts to "staffs" even though they had been transformed. This creates a notable cross-type reference: the subject is `zo-ki-ma-na-Aharon` (the snake) but the patient is `zo-su-mu-ne` (their staffs). Possible interpretations: (1) the sorcerers' snakes transformed back to staffs as they were consumed; (2) the text uses "staffs" metonymically for the whole event. In Tonesu the sentence is grammatical either way; the cross-type reference is documented here. `ko-de` first attestation as a swallowing/devouring action verb.

---

### S701 — EXO-002-F

```
la-na-Faro  wi-fe-ki  /  no  la-na-Faro  si  lo-si-be-go-li
```

**Written:** `lanaFaro wifeki / no lanaFaro si losibegoli`

**Natural reading:** Pharaoh's will hardened / Not: Pharaoh received the divine signal.

**Notes:** Bi-clausal parallel (`/`) pairing Pharaoh's internal volitional state with his external non-reception. `wi-fe-ki` = will-boundary-inchoative = the will entering a bounded/closed state = hardening of will (first attestation; compositional from `wi` + `fe` + `-ki` inchoative suffix). Maps to Hebrew `yehezak lev-Faro` (Pharaoh's heart became strong/hard, Exodus 7:13). The `/` particle pairs the two clauses structurally: the hardening and the non-reception are the two faces of the same refusal. `no la-na-Faro  si  lo-si-be-go-li` = Not: Pharaoh-perceived the divine-signal = he did not receive/hear what the creator-agent was signaling. `si-be-go-li` = signal-from-the-creator-agent = the divine sign/message (compositional). The bi-clausal parallel leaves the causal relationship between the two clauses unstated — the `/` pairs them structurally; which is cause and which is effect is theologically contested (divine hardening vs volitional hardening). This ambiguity is appropriate: the Hebrew text itself oscillates. The Tonesu sentence is deliberately agentless in the first clause (`la-na-Faro wi-fe-ki` has Pharaoh as the subject-of-will, not as external agent), making the volitional vs divine-hardening ambiguity structurally present.

---

## EXO-002 Batch Summary

| Entry | Tonesu | Written form | Key feature |
|-------|--------|-------------|-------------|
| S696 (EXO-002-A) | `la-na-Aharon  ka  lo-zo-su-mu ;  zo-su-mu  ki ;  ne  zo-ki-ma` | `lanaAharon ka lozosumu; zosumu ki; ne zokima` | Three-clause transformation chain; `na-Aharon` and `zo-su-mu`/`zo-ki-ma` first use |
| S697 (EXO-002-B) | `la-na-Faro  si-ki  lo-to-ra-li` | `lanaFaro siki lotorali` | Authority summons; `na-Faro` first attestation |
| S698 (EXO-002-C) | `la-to-ra-li  ka  lo-zo-su-mu-ne  go-si  wi-ra-su` | `latorali ka lozosumune gosi wirasu` | Instrumental `go-si`; `wi-ra-su` in Biblical register |
| S699 (EXO-002-D) | `zo-su-mu-ne  ki ;  ne  zo-ki-ma` | `zosumune ki; ne zokima` | Parallel transformation echo; agentless `;` chain |
| S700 (EXO-002-E) | `la-zo-ki-ma-na-Aharon  ko-de  lo-zo-su-mu-ne` | `lazokimanaAharon kode lozosumune` | `ko-de` swallow/devour; competitive dominance; cross-type reference |
| S701 (EXO-002-F) | `la-na-Faro  wi-fe-ki  /  no  la-na-Faro  si  lo-si-be-go-li` | `lanaFaro wifeki / no lanaFaro si losibegoli` | `wi-fe-ki` volitional hardening; bi-clausal `/`; divine/volitional ambiguity |

**New vocabulary:** W220 `zo-ki-ma` (snake/serpent), W221 `zo-su-mu` (staff/wooden implement).
**Compositional first uses:** `ko-de` (swallow/engulf-and-consume); `wi-fe-ki` (harden one's will); `si-be-go-li` (divine signal); `na-Aharon` (Aaron); `na-Faro` (Pharaoh).
**Key finding:** "X became Y" requires a three-clause decomposition in Tonesu: `X ki ; ne Y` (X changed; [it is] Y). There is no single-clause 'become' verb. The competitive structure of the passage maps naturally onto two parallel `;` chains (S696 and S699) with the decisive `ko-de` resolution in S700.



---

## AOW-001 — *The Art of War* (Sun Tzu, Chapters 1 & 3) — Deception, Rapidity, and the Know-Yourself Triptych

*Batch purpose (AOW-001): Core axioms from Sun Tzu's* The Art of War *(孫子兵法), Chapters 1 and 3. Key tests: first use of ka-ra (W222: combat/warfare), de-li (W223: adversary), and ka-si-de (W224: deliberate deception); compositional first uses de-ra (defeat: force-decrease), be-ra (victory: force-increase), ra-no-fe (supreme excellence: ra-extremal), no-de-ra (absence of defeat); first use of ne go-si [X] for instrumental-property predication; first use of to-su lo-[NP] for relational knowledge (entity-directed vs propositional); `;` inside `{}` conditional frame for NP conjunction (correcting the wi misconception — wi is the purpose particle, not AND). Full analysis in `corpus/translations/Literature/art-of-war.md`.*

---

### S702 — AOW-001-A

```
a-ka-ra  ne  go-si  ka-si-de
```

**Written:** `akara ne gosi kaside`

**Natural reading:** All warfare operates through deception.

**Notes:** Sun Tzu, Chapter 1.18 (Giles: "All warfare is based on deception"; Chinese: 兵者，詭道也). `a-ka-ra` = `a-` scope prefix (abstract/universal) + `ka-ra` (W222: combat) = all-warfare without restriction, every instance of warfare. First use of `a-ka-ra`. `ne go-si ka-si-de` = "has the property of being-by-means-of deception." First use of `ne go-si [X]` as instrumental-property predication — attributing to an entity a characteristic operational mode. `go-si` (instrumental "by means of") normally attaches to action clauses; here it is predicated directly via `ne` to mark the defining mode of all-warfare as deception. `ka-si-de` (W224) = deliberate deception; intentional signal-corruption. Tonesu renders 兵者，詭道也 as a property claim: all-warfare IS the kind of thing that operates through deception as its defining mode.

---

### S703 — AOW-001-B

```
ka-ra  ne  go-si  ki
```

**Written:** `kara ne gosi ki`

**Natural reading:** Warfare operates through speed.

**Notes:** Sun Tzu on the centrality of rapidity (cp. Chapter 11: 兵之情主速, "The essential character of warfare prizes speed"). Parallel structure to S702: both are `[subject] ne go-si [mode]` property predications attributing an operational mode to warfare. `ka-ra` (W222) = warfare; `ki` = change/motion/speed (primitive root). In military context `ki` carries the reading of rapid, decisive movement — the speed dimension of ki rather than mere change-in-general. The S702–S703 couplet presents Sun Tzu's two foundational operational principles (deception and speed) as parallel property predications, making their structural symmetry formally explicit.

---

### S704 — AOW-001-C

```
ra-no-fe  :  la-de-li  ne  de-ra  no  go-si  ka-ra
```

**Written:** `ranofe: ladeli ne dera no gosi kara`

**Natural reading:** As for supreme excellence: the adversary is in a state of defeat, not via combat.

**Notes:** Sun Tzu, Chapter 3.2 (Giles: "supreme excellence consists in breaking the enemy's resistance without fighting"). `ra-no-fe` = [ra]-no-fe extremal = unbounded force/excellence (THO-001 pattern applied to `ra`). First use of `ra-no-fe` in military register (not theological). Used as the topic NP in the topic frame `:`: "as for supreme excellence — [its character is defined by what follows]." `la-de-li` = the adversary (W223) in the agent position. `ne de-ra` = has the property of force-decrease = is in a state of defeat. `de-ra` = `de` (decrease) + `ra` (force) = force-decrease as a state = defeat. Compositional first use. `no go-si ka-ra` = "not by means of combat." The adversary's defeat is the mark of supreme excellence specifically when achieved without direct combat. The `:` topic frame presents `ra-no-fe` as the concept under examination; the comment clause defines it concretely: what makes supreme excellence is adversarial defeat achieved without fighting.

---

### S705 — AOW-001-D

```
go {la-mi  to-su  lo-de-li  ;  la-mi  to-su  lo-mi},  a-ka-ra  ne  no-de-ra
```

**Written:** `go {lami tosu lodeli; lami tosu lomi}, akara ne nodera`

**Natural reading:** If I have organized knowledge of the adversary and of myself: all combat is free of defeat.

**Notes:** Sun Tzu, Chapter 3.18 (Giles: "If you know the enemy and know yourself, you need not fear the result of a hundred battles"). Know-yourself triptych, Part 1: both known → no defeat. `go {premises},` = conditional causal frame. Premises are two clauses joined with `;` (constant conjunction, not `wi` which is the purpose frame "in order that"). The `;` inside `{}` chains provides NP conjunction for the bilateral knowledge condition. Key finding: Tonesu has no dedicated AND particle for NP lists; `;` (sequential) inside a conditional premise is the grammatically correct strategy. `la-mi to-su lo-de-li` = "I have organized knowledge OF the adversary." First use of `to-su lo-[NP]` for relational/entity-directed knowledge — distinct from `to-su {P}` (propositional knowledge established in LOJ-001). `lo-de-li` = patient-marked adversary = knowledge directed at the adversary as an entity. `la-mi to-su lo-mi` = "I have organized knowledge of myself" (self-knowledge condition). Matrix: `a-ka-ra ne no-de-ra` = "all-combat has the property of no-defeat." `no-de-ra` = absence of defeat (no + de-ra). `a-ka-ra` = all instances of combat. Compositional first uses: `no-de-ra`, used compositionally as property NP.

---

### S706 — AOW-001-E

```
go {la-mi  to-su  lo-mi  ;  no  la-mi  to-su  lo-de-li},  ka-ra  ne  be-ra  /  ka-ra  ne  de-ra
```

**Written:** `go {lami tosu lomi; no lami tosu lodeli}, kara ne bera / kara ne dera`

**Natural reading:** If I know myself but not the adversary: combat is [sometimes] victory / [sometimes] defeat.

**Notes:** Sun Tzu, Chapter 3.18 (Giles: "If you know yourself but not the enemy, for every victory gained you will also suffer a defeat"). Know-yourself triptych, Part 2: self only known → alternating outcomes. Premise chain: self-knowledge present (first clause) AND adversary-knowledge absent (`no la-mi to-su lo-de-li` = negated knowledge claim). Matrix: `ka-ra ne be-ra / ka-ra ne de-ra` = "combat has the property of victory / combat has the property of defeat." The `/` bi-clausal parallel pairs two outcome-predications, capturing the alternating fortune Sun Tzu describes. `be-ra` = `be` (increase) + `ra` (force) = force-increase = victory. `de-ra` = defeat (from S704). Compositional first use of `be-ra`. The `/` partition closes neither outcome — it holds both in structural suspension, formally encoding the uncertainty of partial knowledge. Middle sentence of the triptych; flanked by S705 (both known: no defeat) and S707 (neither known: all defeat).

---

### S707 — AOW-001-F

```
go {no  la-mi  to-su  lo-de-li  ;  no  la-mi  to-su  lo-mi},  a-ka-ra  ne  de-ra
```

**Written:** `go {no lami tosu lodeli; no lami tosu lomi}, akara ne dera`

**Natural reading:** If I have neither knowledge of the adversary nor of myself: all combat results in defeat.

**Notes:** Sun Tzu, Chapter 3.18 (Giles: "If you know neither the enemy nor yourself, you will succumb in every battle"). Know-yourself triptych, Part 3: neither known → defeat in all combats. Both premises negated: `no la-mi to-su lo-de-li` (no adversary knowledge) AND `no la-mi to-su lo-mi` (no self-knowledge). Matrix: `a-ka-ra ne de-ra` = "all-combat has the property of defeat." Exact structural mirror of S705: S705 uses `a-ka-ra ne no-de-ra` (all-combat → no-defeat); S707 uses `a-ka-ra ne de-ra` (all-combat → defeat). The logical symmetry between the two extremes (S705 and S707) is formally encoded in the sentence structure — the only difference is the presence or absence of `no-` on `de-ra` and on each premise clause. S706 breaks the symmetry: partial knowledge produces neither the universal security of S705 nor the universal doom of S707 but an unresolvable alternation.

---

## AOW-001 Batch Summary

| Entry | Tonesu | Written form | Key feature |
|-------|--------|-------------|-------------|
| S702 (AOW-001-A) | `a-ka-ra  ne  go-si  ka-si-de` | `akara ne gosi kaside` | First use `ne go-si [X]` instrumental-property predication; `a-ka-ra` universal-scoped warfare |
| S703 (AOW-001-B) | `ka-ra  ne  go-si  ki` | `kara ne gosi ki` | Parallel deception/speed couplet; `ka-ra` W222 first attestation |
| S704 (AOW-001-C) | `ra-no-fe  :  la-de-li  ne  de-ra  no  go-si  ka-ra` | `ranofe: ladeli ne dera no gosi kara` | `ra-no-fe` extremal in military register; `de-ra` (defeat) compositional first use; `de-li` W223 first attestation |
| S705 (AOW-001-D) | `go {la-mi  to-su  lo-de-li  ;  la-mi  to-su  lo-mi},  a-ka-ra  ne  no-de-ra` | `go {lami tosu lodeli; lami tosu lomi}, akara ne nodera` | First `to-su lo-[NP]` relational knowledge; `;` inside `{}` for NP conjunction; `no-de-ra` compositional |
| S706 (AOW-001-E) | `go {la-mi  to-su  lo-mi  ;  no  la-mi  to-su  lo-de-li},  ka-ra  ne  be-ra  /  ka-ra  ne  de-ra` | `go {lami tosu lomi; no lami tosu lodeli}, kara ne bera / kara ne dera` | `be-ra` (victory) compositional first use; `/` pairing alternating outcomes |
| S707 (AOW-001-F) | `go {no  la-mi  to-su  lo-de-li  ;  no  la-mi  to-su  lo-mi},  a-ka-ra  ne  de-ra` | `go {no lami tosu lodeli; no lami tosu lomi}, akara ne dera` | Exact mirror of S705; `a-ka-ra ne de-ra` vs `a-ka-ra ne no-de-ra` minimal pair |

**New vocabulary:** W222 `ka-ra` (combat/warfare), W223 `de-li` (adversary), W224 `ka-si-de` (deliberate deception).
**Compositional first uses:** `de-ra` (defeat: force-decrease); `be-ra` (victory: force-increase); `ra-no-fe` (supreme excellence: ra-extremal); `no-de-ra` (absence of defeat); `a-ka-ra` (all-warfare: a-scoped ka-ra); `to-su lo-[NP]` relational knowledge pattern.
**Key finding:** Tonesu has no AND coordinator for NP lists. Bilateral conditions in a `go {}` premise use `;` (sequential: constant conjunction) to chain the two knowledge clauses. `wi` is the purpose frame ("in order that"), not an AND particle — confirmed in grammar.md line 927.


---

## MAP-001 — *The Prince* (Machiavelli) + Dark Triad Psychology

*Batch purpose (MAP-001): Key aphorisms from Niccolò Machiavelli's* Il Principe *(The Prince, 1532) combined with the psychological Dark Triad (narcissism, Machiavellianism, psychopathy). Key tests: first use of `nu-be` comparison particle in political/abstract register; first `la-X si [Q] lo [Z]` appearance predication (X signals Q to Z = X appears as Q to Z); first `wi {}` purpose-frame with explicit goal clause; first `go {}` with agentless state premise (`fa-no`); first triple `;` chain mixing three clause types; new word `ra-su-li` (W225: sovereign/ruler). Full analysis in `corpus/translations/Literature/machiavelli-dark-triad.md`.*

---

### S708 — MAP-001-A

```
wi-ra  :  fa-ra  su  nu-be  fa-vo
```

**Written:** `wira: fara su nube favo`

**Natural reading:** As for authority: fear has more structural reliability than love.

**Notes:** Machiavelli, *The Prince* Ch 17 (Giles/Ricci: "it is much safer to be feared than loved"). `wi-ra` (W177: directed power/authority) as topic NP; `:` topic frame = "as for authority…" `fa-ra` (W154: fear/awe) and `fa-vo` (W197: happiness/positive-affect) are the two items being compared. `su` = structure/reliability as the quality dimension in the comparison: the degree to which a relationship holds its structural form under pressure. `nu-be` = more-than (established grammar comparison particle; `nu` quantity + `be` increase). First use of `nu-be` in political-philosophical register on abstract quality dimensions. Pattern: `lo-A  Q  nu-be  lo-B` → here `fa-ra  su  nu-be  fa-vo` (the articles are elided; `fa-ra` and `fa-vo` function as 0-article abstract NPs). The argument is Machiavellian: love-based authority collapses when tested; fear-based authority maintains structural integrity because the mechanism (deterrence) is self-reinforcing. `su` as quality dimension captures "structural integrity/reliability" rather than intrinsic worth.

---

### S709 — MAP-001-B

```
la-ra-su-li  si  vo  lo  ze  /  la-ra-su-li  ne  ka-si-de
```

**Written:** `larasuli si vo loze / larasuli ne kaside`

**Natural reading:** The sovereign appears as one of worth to others / [but] the sovereign IS deception.

**Notes:** Machiavelli, *The Prince* Ch 18 ("It is not necessary for a prince to have the above-named qualities, but it is very necessary to appear to have them"). `ra-su-li` (W225: sovereign/ruler) first attestation. `la-ra-su-li si vo lo ze` = the sovereign signals worth/virtue to others. First use of `la-X si [Q] lo [Z]` as **appearance predication**: what an agent signals outward to an observer IS their apparent-face. `si` (signal/information primitive) here functions as an appearance verb: the outward signal constitutes the appearance, without commitment to it reflecting inner reality. `la-ra-su-li ne ka-si-de` = the sovereign has the property of deception. `ne` (property copula) attributes deception as the sovereign's inner reality. The `/` bi-clausal parallel pairs appearance (the outgoing signal) against reality (the inner property). The structural opposition makes the Machiavellian duplicity formally explicit: first clause = the face projected; second clause = the actual character. Distinct from `la-X ne vo` (which would assert the sovereign genuinely has worth) and `la-X si vo lo ze` alone (which would only describe the signal without the reality contrast).

---

### S710 — MAP-001-C

```
mi  ne  ra-no-fe-vo
```

**Written:** `mi ne ranofevo`

**Natural reading:** I [myself] have the property of supreme excellence.

**Notes:** Dark Triad — Narcissism. The narcissist's core implicit claim: the self has unbounded force-worth. `mi` = self, first person (primitive). `ne` = property copula. `ra-no-fe-vo` = unbounded force-worth / supreme excellence (compositional, established AOW-001 S704 context). First use of `mi` as the subject of a direct `ne ra-no-fe-vo` self-predication. This minimal two-word claim after `ne` is the narcissistic grandiosity claim in its structurally simplest form: no qualification, no hedging, no context — just `mi ne [unbounded-excellence]`. In Tonesu, this sentence is structurally well-formed (it is not prohibited to claim self-excellence), but contextually it identifies a pattern: the agent who speaks `mi ne ra-no-fe-vo` as if it were ordinary is the narcissistic agent. The sentence also contrasts with the S712 psychopathy claim: narcissism inflates the self; psychopathy empties the affect substrate. Both sentences begin with first-person.

---

### S711 — MAP-001-D

```
wi {la-mi  ra-be},  la-mi  ka-si-de  lo  ze
```

**Written:** `wi {lami rabe}, lami kaside loze`

**Natural reading:** In order for me to gain power, I deceive others.

**Notes:** Dark Triad — Machiavellianism. `wi {}` = purpose frame ("in order that / so that"), looking forward to intended outcome. `wi {la-mi ra-be}` = with the purpose that I-gain-force = for the purpose of increasing my power. `la-mi ra-be` = I gain force/power (established: `ra-be` = force-increasing / gaining power). Matrix: `la-mi ka-si-de lo ze` = I perform deception on others. First use of `ka-si-de` (W224: deliberate deception) as a **transitive verb** with explicit patient `lo ze` (others). `ka-si-de lo ze` = to deceive others (deception directed at a patient). First use of `wi {}` purpose-frame with a full clause inside. First use of `wi {}` with an explicitly self-directed goal (`la-mi ra-be` = I-gain-force). The Machiavellian structure is in the frame choice: `go` (causal frame) would present deception as the CAUSE of power; `wi` (purpose frame) presents it as the MEANS toward a GOAL. This is the instrumentalist structure — deception is not the root but the tool. The goal is explicit and self-interested. First attestation directly connecting `wi {}` purpose-frame with `ka-si-de`.

---

### S712 — MAP-001-E

```
go {fa-no},  la-mi  ka-no-su  lo  ze
```

**Written:** `go {fano}, lami kanosu loze`

**Natural reading:** Because affect is inactive, I act without structural constraint on others.

**Notes:** Dark Triad — Psychopathy. `go {fa-no}` = because [condition: affect-inactive]. First use of `go {}` with an **agentless state predicate** as premise: `fa-no` (W095: affect inactive/offline, without subject specified) as the causal premise. The premise is impersonal — it predicates the absence of affect as a structural state, not a choice. Matrix: `la-mi ka-no-su lo ze` = I act structurelessly on others. `ka-no-su` = deliberate-action-without-structure = action that bypasses/ignores relational and structural constraints on behavior. Compositional first-use: `ka` (deliberate action) + `no` (absence/negation) + `su` (structure) = action of being unstructured = unconstrained action-toward-others. The Tonesu claim: the structure that normally mediates affect-regulated action (empathic modulation, social reciprocity, felt consequence of harm) is removed when `fa` is offline. `ka-no-su` is the result: action without those mediating structures. `lo ze` = on others (third parties as patient). Distinct from `ka` alone (deliberate action, neutral to structural dimension) and `ka-si-de` (structured deception, which is itself `ka` + structure of signal-corruption). Psychopathy in Tonesu is not the PRESENCE of harmful will but the ABSENCE of structural constraint: `fa-no` → `ka-no-su`.

---

### S713 — MAP-001-F

```
mi  ne  ra-no-fe-vo  ;  wi {la-mi  ra-be},  la-mi  ka-si-de  ;  go {fa-no},  la-mi  ka-no-su
```

**Written:** `mi ne ranofevo; wi {lami rabe}, lami kaside; go {fano}, lami kanosu`

**Natural reading:** I am of supreme excellence; [and] in order to gain power, I deceive; [and] because affect is inactive, I act without structure.

**Notes:** Dark Triad synthesis. All three traits in a `;` triple chain: narcissism (`mi ne ra-no-fe-vo`) → Machiavellianism (`wi {la-mi ra-be}, la-mi ka-si-de`) → psychopathy (`go {fa-no}, la-mi ka-no-su`). First time a `;` sequential chain links THREE DIFFERENT CLAUSE TYPES: (1) property predication (`ne`), (2) purpose-frame clause (`wi {}`), (3) causal-frame clause (`go {}`). The `;` carries the "and also / and in the same agent" meaning: all three descriptions are jointly true of the same speaker. No causal connection is asserted between them (that would require `go`); no sequential precedence is implied; they co-describe a single structure. The resulting three-part structure mirrors the know-yourself triptych (S705–S707) formally — both are triple structures with a shared agent — but the logic is inverted: S705–S707 are CONDITIONAL (if P then Q), while S710–S712/S713 are CONSTITUTIVE (this is what the agent IS). The first-person speaker claiming all three simultaneously has structural parallels to the Sith code (STW-002) but without the causal chain (`go … la-mi … go … la-mi …`): the Dark Triad is not a causal progression of the Sith type but a co-present cluster.

---

## MAP-001 Batch Summary

| Entry | Tonesu | Written form | Key feature |
|-------|--------|-------------|-------------|
| S708 (MAP-001-A) | `wi-ra  :  fa-ra  su  nu-be  fa-vo` | `wira: fara su nube favo` | First `nu-be` comparison in political-abstract register; topic frame + comparison |
| S709 (MAP-001-B) | `la-ra-su-li  si  vo  lo  ze  /  la-ra-su-li  ne  ka-si-de` | `larasuli si vo loze / larasuli ne kaside` | First `la-X si [Q] lo [Z]` appearance predication; W225 `ra-su-li` first attestation |
| S710 (MAP-001-C) | `mi  ne  ra-no-fe-vo` | `mi ne ranofevo` | Narcissism: self as object of `ra-no-fe-vo` predication; minimal grandiosity form |
| S711 (MAP-001-D) | `wi {la-mi  ra-be},  la-mi  ka-si-de  lo  ze` | `wi {lami rabe}, lami kaside loze` | First `wi {}` with explicit self-goal; `ka-si-de lo [patient]` transitive |
| S712 (MAP-001-E) | `go {fa-no},  la-mi  ka-no-su  lo  ze` | `go {fano}, lami kanosu loze` | First agentless-state `go {}` premise (`fa-no`); `ka-no-su` compositional first use |
| S713 (MAP-001-F) | `mi  ne  ra-no-fe-vo  ;  wi {la-mi  ra-be},  la-mi  ka-si-de  ;  go {fa-no},  la-mi  ka-no-su` | `mi ne ranofevo; wi {lami rabe}, lami kaside; go {fano}, lami kanosu` | First triple `;` chain across three clause types (ne / wi{} / go{}) |

**New vocabulary:** W225 `ra-su-li` (sovereign/ruler/prince).
**Compositional first uses:** `ka-no-su` (deliberate structureless action); `mi ne ra-no-fe-vo` (self-grandiosity predication); `ka-si-de lo [patient]` (transitive deception with patient).
**Key structural findings:** `nu-be` comparison on abstract political quality; `la-X si [Q] lo [Z]` as appearance predication (`si` = outward signal = apparent face); `wi {}` purpose-frame with self-directed goal; `go {}` with impersonal state premise; triple `;` chain mixing clause types.
