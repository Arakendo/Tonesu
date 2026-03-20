# Communications Decency Act §230(c)(1) — Translation Analysis (CDA-001)

**Source:** Communications Decency Act of 1996 (47 U.S.C. §230), Section 230(c)(1)
**Batch:** CDA-001
**Sentences:** S639–S644
**New entries:** W200 (`su-ka-li`), W201 (`si-go-li`), W202 (`to-ki'ne-su`)
**First attestations:** W200 (S639), W201 (S639), W202 (S639)

---

## Source text

> "No provider or user of an interactive computer service shall be treated as the publisher or speaker of any information provided by another information content provider."
> — 47 U.S.C. §230(c)(1), "Treatment of publisher or speaker"

This six-sentence batch is a structural stress test, not a word-for-word translation. The goal is to expose exactly where the statute's language breaks down when subjected to Tonesu's compositional constraints.

---

## Vocabulary design

### Existing vocabulary used

| Concept | Form | W# | Notes |
|---------|------|----|-------|
| Rule / prohibition | `wi-fe` | W100 | policy-imposed limit |
| Relay device | `si-mu` | W039 | signal transceiver — the platform's structural identity |
| Information-signal | `to-si` | W026 | proposition / thought-signal |
| Comprehend / enter organized knowledge | `to-su-ki` | W025 | used to diagnose the statute's undefined boundary |
| Epistemic boundary | `to-fe` | W028 | the boundary between knowledge states — invoked but undefined by 230 |
| Judge / categorize | `ka-to-fe` | W122 | deliberate epistemic bounding = editorial judgment |
| Self-evident proposition | `su-to` | W199 | used to distinguish normative rule from structural truth |
| Person | `zo-li` | W148 | stands in for "another information content provider" |

### New vocabulary: W200–W202

#### W200 — `su-ka-li` — service provider / platform operator

**Construction:** su (structure/order) + ka (intentional action) + li (social agent). Head-final: `li` is head; `su-ka` (structure-action) describes the defining activity. A `su-ka-li` is the agent who actively maintains a structured system for others to use.

**Role distinction:** `su-ka-li` (maintains the platform) vs `mu-ka-li` (uses the platform) vs `si-go-li` (W201, originates content on the platform). These are three structurally distinct roles. Section 230's immunity depends on correctly identifying which one the defendant occupies.

**First attestation:** S639.

#### W201 — `si-go-li` — content originator / speaker

**Construction:** si (signal/representation) + go (cause/origin) + li (social agent). Head-final: `li` is head; `si-go` (signal-origin) is the defining attribute. A `si-go-li` is the causal source of a piece of content.

**Unification value:** Section 230 uses "publisher or speaker" as a disjunction. In Tonesu, both roles collapse into `si-go-li`: both a publisher and a speaker are defined by being the causal origin of content. The distinction between them is editorial vs authorial — interesting legally but structurally the same class for 230 purposes.

**The editorial exception (S641):** When a `su-ka-li` exercises `ka-to-fe` (deliberate categorization/judgment) over content, it converts from relay-agent into `si-go-li`. The transition is structural, not incidental.

**First attestation:** S639.

#### W202 — `to-ki'ne-su` — online platform / interactive computer service

**Construction:** `to-ki` (W020, computation) + `ne-su` (network-structure: `ne`=relation + `su`=structure). Juncture `'` marks `[to-ki]` as pre-bound before `[ne-su]`. The form encodes the platform as a computation-network-structure — emphasized as a structured relational system, not merely a device.

**Contrast with `to-ki-mu` (W011, computer):** A single computer is a device (`-mu`). An online platform is the structured network (`ne-su`) within which computation occurs. The distinction is the difference between a telephone handset and the telephone network.

**First attestation:** S639.

---

## Translation entries

### S639 — CDA-001-A: Core immunity claim

**Source:** "No provider... shall be treated as the publisher or speaker of any information provided by another information content provider."

```
la-su-ka-li  lo-to-ki'ne-su  ne  no-si-go-li  lo-to-si  go  zo-li
```

**Written:** `lasukali lotoki'nesu ne nosigoli lotosi go zoli`

**Gloss-line:** `[agent]service-provider [patient]online-platform is not-content-originator [patient]information-signal from person`

**Natural reading:** A service-provider of an online platform is not a content-originator of information-signals from persons.

**Notes:** Three roles introduced in one sentence: `su-ka-li` (provider), `to-ki'ne-su` (the ICS), `si-go-li` (the publisher/speaker role being denied). The phrase `lo-to-si go zo-li` (information-signals from a person) translates "information provided by another information content provider" — deliberately scope-open. The "another" boundary question is the entire legislative controversy; Tonesu surfaces it immediately by leaving `zo-li` without quantification. See S642 for the diagnosis.

---

### S640 — CDA-001-B: The platform's structural identity

```
la-to-ki'ne-su  ne  si-mu  lu-zo-li  /  ne  no-si-go-li
```

**Written:** `latoki'nesu ne simu luzoli / ne nosigoli`

**Gloss-line:** `[agent]online-platform is relay-device [beneficiary]persons / is not-content-originator`

**Natural reading:** An online platform is a relay device for persons / is not a content-originator.

**Notes:** `si-mu` (W039) = relay device, signal transceiver. The platform carries signals; it does not originate them. `lu-zo-li` = beneficiary frame: the relay exists for the benefit of persons using it. The `/` parallel is the structural argument for immunity: because the platform IS a relay-device, it IS NOT a content-originator. The immunity is structural, not incidental. S641 identifies where this structural identity breaks.

---

### S641 — CDA-001-C: The editorial exception

```
go  la-su-ka-li  ka-to-fe  lo-to-si,  du  la-su-ka-li  ne  si-go-li
```

**Written:** `go lasukali katofe lotosi, du lasukali ne sigoli`

**Gloss-line:** `if [agent]service-provider judges [patient]information, then [agent]service-provider is content-originator`

**Natural reading:** If a service-provider deliberately categorizes information, then the service-provider is a content-originator.

**Notes:** The `go... du` causal conditional expresses the editorial exception cleanly. `ka-to-fe` (W122) = deliberate epistemic bounding = the act of intentionally establishing where something falls within a category scheme. When a platform exercises `ka-to-fe` — curating, labeling, ranking content on the merits — the relay identity of S640 is suspended, and `su-ka-li` becomes `si-go-li`. This threshold is where platform-liability litigation lives. Tonesu names it: the conversion happens at the moment of `ka-to-fe`.

---

### S642 — CDA-001-D: The "another" gap

```
la-wi-fe  no  to-su-ki  lo-to-fe  su-ka-li  ne  si-go-li
```

**Written:** `lawife no tosuki lotofe sukali ne sigoli`

**Gloss-line:** `[agent]the-rule not comprehends [patient]epistemic-boundary service-provider [relation]content-originator`

**Natural reading:** The rule has not comprehended the boundary between service-provider and content-originator.

**Notes:** `to-su-ki` (W025) = to comprehend / enter organized knowledge. `lo-to-fe su-ka-li ne si-go-li` = the epistemic-boundary in the relational space between service-provider and content-originator. The statute uses "another information content provider" but never defines when a platform crosses the line into being that "another." Thirty years of litigation (Zeran v. AOL, Force v. Facebook, NetChoice v. Paxton) is the evidentiary record of this structural incompleteness. Tonesu's verdict: a rule that invokes a `to-fe` (boundary) it has not given `to-su-ki` (organized knowledge of) is structurally incomplete. The rule functions despite this only because courts tolerate strategic vagueness.

---

### S643 — CDA-001-E: "Shall be treated as" is normative, not epistemic

```
la-wi-fe  ne  no-su-to  /  ne  wi-fe'ka-to-fe
```

**Written:** `lawife ne nosuto / ne wife'katofe`

**Gloss-line:** `[agent]the-rule is not-self-evident / is rule-about-categorization`

**Natural reading:** The rule is not a self-evident proposition / it is a rule about deliberate categorization.

**Notes:** The statute says "shall be treated as" — not "is." This is the critical linguistic marker of a normative prescription (`wi-fe'ka-to-fe`) as opposed to a factual or structural claim (`su-to`, W199). `su-to` = a truth whose ground is its own structure, requiring no external justification. `wi-fe'ka-to-fe` = [rule (W100)] + [deliberate categorization (W122)] = a rule whose content is a mandate about how agents must classify. The `/` parallel is: what the statute is not (self-grounding truth) vs what it actually is (prescriptive categorization mandate). This distinction matters: a `su-to` cannot be amended by Congress; a `wi-fe'ka-to-fe` can — and regularly is.

---

### S644 — CDA-001-F: Structural verdict

```
la-wi-fe  ne  wi-fe'ka-to-fe  /  ke, la-wi-fe  no  to-su-ki  lo-to-fe  su-ka-li  ne  si-go-li
```

**Written:** `lawife ne wife'katofe / ke, lawife no tosuki lotofe sukali ne sigoli`

**Gloss-line:** `[agent]the-rule is rule-about-categorization / but [agent]the-rule not comprehends [patient]boundary service-provider [relation]content-originator`

**Natural reading:** The rule is a prescription about categorization / but the rule has not defined the boundary between service-provider and content-originator.

**Notes:** Synthesis sentence. `/ ke,` = parallel-partition + pivot: the first clause establishes S643's identification of what 230 is; `ke,` advances to the unresolved problem from S642. Tonesu's complete diagnosis of §230(c)(1): *It is a well-formed prescriptive categorization rule (`wi-fe'ka-to-fe`), not a foundational truth (`su-to`). Its structural incompleteness is the undefined boundary between `su-ka-li` and `si-go-li` — a gap the statute delegated to judicial discretion rather than organized knowledge (`to-su-ki`). In Tonesu, that delegation would need to be explicit.*

---

## CDA-001 Batch Summary

| Entry | Written form | Source clause | Key vocabulary |
|-------|-------------|---------------|----------------|
| S639 (CDA-001-A) | `lasukali lotoki'nesu ne nosigoli lotosi go zoli` | Core immunity claim | W200 + W201 + W202 first att. |
| S640 (CDA-001-B) | `latoki'nesu ne simu luzoli / ne nosigoli` | Platform as relay device | `si-mu` (W039) structural identity |
| S641 (CDA-001-C) | `go lasukali katofe lotosi, du lasukali ne sigoli` | Editorial exception | `ka-to-fe` (W122) as threshold |
| S642 (CDA-001-D) | `lawife no tosuki lotofe sukali ne sigoli` | The "another" gap | `to-su-ki` (W025) gap diagnosis |
| S643 (CDA-001-E) | `lawife ne nosuto / ne wife'katofe` | "Shall be treated as" = normative | `su-to` (W199) vs `wi-fe'ka-to-fe` |
| S644 (CDA-001-F) | `lawife ne wife'katofe / ke, lawife no tosuki lotofe sukali ne sigoli` | Structural verdict | Synthesis |

**New entries:** W200 (`su-ka-li`, service provider), W201 (`si-go-li`, content originator), W202 (`to-ki'ne-su`, online platform)

**Key design findings:**

1. **`su-ka-li` / `si-go-li` role distinction is the statute's load-bearing concept:** Section 230 protects agents in the `su-ka-li` role from liability that would attach to those in the `si-go-li` role. Tonesu gives these two distinct compounding structures, making the distinction structurally visible. The statute's entire controversy is the boundary between them.

2. **`to-ki'ne-su` as the platform environment:** The juncture compound `[to-ki]'[ne-su]` = computation-network-structure captures the "interactive computer service" as an organized relational system, not merely a device. The network character (`ne-su`) is the key property that enables multi-user information exchange — and is what makes `si-mu` (relay) the correct structural metaphor.

3. **`si-mu` (W039) is the right structural analogy:** The relay device (`si-mu`) is an already-registered Tonesu compound that captures the platform's structural role precisely. An online platform does for information what a telegraph relay did for signals: it carries without authoring. The immunity follows from this structural identity.

4. **`ka-to-fe` (W122) as the editorial threshold:** The conversion from relay-agent to content-originator happens at the moment of `ka-to-fe` (deliberate epistemic categorization / editorial judgment). Tonesu names this threshold precisely in S641. The legal controversy about platform moderation is, in Tonesu, a question of whether a specific action constitutes `ka-to-fe`.

5. **`su-to` vs `wi-fe'ka-to-fe` — normative vs epistemic:** Section 230 is not a structural truth; it is a legislative prescription about categorization. The "shall be treated as" formulation is legally significant: it means courts and litigants can contest the categorization in a way they could not contest a `su-to`. S643 makes this explicit.

6. **The statute works by delegating its hardest question:** S642 identifies that the `to-fe` (boundary) between `su-ka-li` and `si-go-li` has not been given `to-su-ki` (organized knowledge). This is not a flaw the statute can easily fix — the boundary is factually context-dependent and evolves with technology. Tonesu's verdict (S644): the statute is structurally coherent but explicitly incomplete; it delegates a boundary question through `ke,`-style implicit acknowledgment rather than `to-su-ki`-style organized resolution.

---

## Colloquial Register Analysis

| Form used | CLQ entry | Colloquial form | Notes |
|-----------|-----------|-----------------|-------|
| `su-ka-li` | none | — | 3-root; technical term; no CLQ entry at present |
| `si-go-li` | none | — | 3-root; technical-legal term; no CLQ entry at present |
| `to-ki'ne-su` | none | — | 4-root juncture compound; technical term; no CLQ entry at present |
| `wi-fe` (W100) | none | — | 2-root — below 3-morpheme contraction threshold |
| `ka-to-fe` (W122) | none | — | 3-root; no existing CLQ entry |
| `to-su-ki` (W025) | none | — | 3-root; no existing CLQ entry |
| `su-to` (W199) | none | — | 2-root — below 3-morpheme contraction threshold |
| `si-mu` (W039) | none | — | 2-root — below 3-morpheme contraction threshold |
| `to-si` (W026) | none | — | 2-root — below 3-morpheme contraction threshold |
| `wi-fe'ka-to-fe` | none | — | compositional juncture compound; analytical one-time form; outside CLQ scope |
| `go` (causal particle) | none | — | Primitive; semantically load-bearing |
| `ne` (copula) | none | — | Primitive; semantically load-bearing |

**Verdict:** irreducibly formal — all new compounds are technical-legal terms that do not naturally enter colloquial contexts; all primitives and particles are semantically load-bearing operators.

*CLQ entries registered from this batch: none.*
