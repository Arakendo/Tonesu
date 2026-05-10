---
batch_codes: [ROB]
---
# Translation Test: Robotics Law Battery

## Source: Functional paraphrase of Isaac Asimov's classic Three Laws of Robotics (not a direct quotation), plus a Tonesu-native redesign
## Original language: English
## Reference: classic robotics-law hierarchy as popularly transmitted in science-fiction discourse; redesign authored in-repo for corpus testing
## Status: Draft — ROB-001/002 (S941–S956)

---

## Purpose

This batch does two different jobs.

First, it checks whether Tonesu can express the familiar robotics-law hierarchy without inventing a dedicated `robot` word. The answer is yes: `mu` is enough. The real stress is not lexical taxonomy but rule structure.

Second, it tests whether Tonesu can improve on the English original by refusing to compress distinct things into one rule. The classic hierarchy is elegant because it is short. It is weak because it hides four separable questions inside that brevity:

1. Is the machine forbidden to harm a person?
2. Is the machine required to preserve a person under threat?
3. Does any human demand bind, or only recognized authority?
4. What should happen when the machine has evidence of danger but not knowledge-grade certainty?

English leaves those layers entangled. Tonesu does not need to. The language already has stable distinctions for:

- `wi-fe-ka` = clause-level prohibition
- `ne-fe` = requirement / dependency condition
- `wi-ra` = demand / authority
- `si` vs `to` = signal-grade vs knowledge-grade epistemic status
- `no-de` / `ka-no-de` = preservation and deliberate preservation

The redesign therefore does not add futuristic concepts. It simply uses the language's existing precision.

---

## Design choice: no special `robot` lexeme

The batch deliberately uses `mu` (machine/artifact) rather than coining a new humanoid-machine word.

Reason: the pressure in this source is normative, not taxonomic. The laws are about what an artificial agent may, must, and may-not do around persons. A dedicated `robot` label would be decorative unless the batch discovered a structural need to distinguish machines that merely operate from machines that deliberate under authority. That pressure did not arise here.

So the file stays conservative: test the law architecture first; add a specialized agent term only if later corpus work requires one.

---

## ROB-001 Structure

### A. Classic hierarchy rendered into Tonesu

| Entry | Tonesu | Written | Function |
|------|--------|---------|----------|
| S941 | `wi-fe-ka [la-mu ka-de lo-i-zo-li]` | `wifeka [lamu kade loizoli]` | machine may not harm a person |
| S942 | `go {la-i-zo-li zo-ra de}, la-mu ne-fe lo-ka-no-de lo-i-zo-li` | `go {laizoli zora de}, lamu nefe lokanode loizoli` | danger to life creates rescue duty |
| S943 | `go {la-i-zo-li wi-ra [la-mu wi-ka] ; no-wi-fe-ka [la-mu ka-de lo-i-zo-li]}, la-mu ne-fe lo-wi-ka` | `go {laizoli wira [lamu wika] ; nowifeka [lamu kade loizoli]}, lamu nefe lowika` | human demand binds unless blocked by first law |
| S944 | `go {lo-mu ne-fe lo-no-de ; no-wi-fe-ka [la-mu ka-de lo-i-zo-li] ; no la-i-zo-li wi-ra [la-mu wi-ka]}, la-mu no-de` | `go {lomu nefe lonode ; nowifeka [lamu kade loizoli] ; no laizoli wira [lamu wika]}, lamu node` | self-preservation is subordinate |
| S945 | `la-wi-fe-su ne no-su-to / ke, la-wi-fe-su no to-su-ki lo-to-fe {wi-ra ; wi-fe ; si ; to}` | `lawifesu ne nosuto / ke, lawifesu no tosuki lotofe {wira ; wife ; si ; to}` | structural verdict |

### B. Tonesu-native redesign

| Entry | Tonesu | Written | Function |
|------|--------|---------|----------|
| S946 | `la-i-zo-li ne wi-fe / wi-fe-ka [la-mu ka-de lo-i-zo-li]` | `laizoli ne wife / wifeka [lamu kade loizoli]` | personhood grounded in rights |
| S947 | `go {la-i-zo-li zo-ra de}, la-mu ne-fe lo-ka-no-de lo-i-zo-li` | `go {laizoli zora de}, lamu nefe lokanode loizoli` | rescue stated as a separate positive duty |
| S948 | `go {la-i-zo-li ne wi-ra lo-mu ; la-i-zo-li wi-ra [la-mu wi-ka] ; no-wi-fe-ka [la-mu ka-de lo-i-zo-li]}, la-mu ne-fe lo-wi-ka` | `go {laizoli ne wira lomu ; laizoli wira [lamu wika] ; nowifeka [lamu kade loizoli]}, lamu nefe lowika` | only recognized authority can issue binding demands |
| S949 | `go {la-mu si [la-i-zo-li zo-ra de] / la-mu no-to [lo-ze]}, la-mu ka-si lo-to-fe-li lo-ze` | `go {lamu si [laizoli zora de] / lamu noto [loze]}, lamu kasi lotofeli loze` | uncertainty routes upward |
| S950 | `go {lo-mu ne-fe lo-no-de ; no-wi-fe-ka [la-mu ka-de lo-i-zo-li] ; no la-i-zo-li ne wi-ra lo-mu}, la-mu no-de` | `go {lomu nefe lonode ; nowifeka [lamu kade loizoli] ; no laizoli ne wira lomu}, lamu node` | maintenance as dependency, not instinct |

---

## What Tonesu exposes in the classic laws

### 1. The first law is really two laws

English says: do not injure; do not allow injury through inaction.

Tonesu shows that these are not the same thing.

- `wi-fe-ka [la-mu ka-de lo-i-zo-li]` = a prohibition on harmful action
- `la-mu ne-fe lo-ka-no-de lo-i-zo-li` = a positive duty of deliberate preservation

Once separated, both clauses become easier to inspect and easier to prioritize.

### 2. Demand and authority are not the same thing

The classic second law implicitly treats any relevant human command as binding unless blocked by the first law.

Tonesu can do better because `wi-ra` is already separable from bare rule and from bare preference. S948 adds the missing relation:

`la-i-zo-li ne wi-ra lo-mu`

That relation states that the person stands in a recognized authority-position with respect to the machine. This is the difference between:

- anyone speaking near the machine
- a person authorized to direct it

The English original blurs those. Tonesu does not have to.

### 3. The original laws have no native uncertainty rule

The classic hierarchy assumes the machine can decide whether harm is occurring, whether a demand exists, and whether a conflict is real.

But Tonesu's epistemic ladder makes the missing case obvious:

- `si [PROP]` = signal-grade certainty / evidence-level holding
- `no-to [PROP]` = no knowledge-grade warrant

S949 turns that gap into policy: when the machine has danger-evidence without knowledge-grade certainty, it escalates to `to-fe-li` rather than pretending certainty or freezing silently.

This is the clearest place where Tonesu produces a better law-set than a straight translation.

### 4. Self-preservation is a bad metaphor; maintenance is a better law

The original third law anthropomorphizes the machine by talking about self-preservation.

Tonesu reframes the same concern structurally:

- `lo-mu ne-fe lo-no-de` = the machine requires preservation / continued integrity

This is stronger engineering language. The machine does not need an ego-model. It needs continued integrity to remain capable of satisfying higher-order duties.

---

## Key findings

1. The classic hierarchy is translatable, but it is structurally under-specified in Tonesu terms.
2. The best Tonesu-native rewrite splits prohibition, rescue, authority, uncertainty, and maintenance into separate legal surfaces.
3. `wi-ra` is the decisive improvement point: demand only becomes binding when an authority relation is explicit.
4. `si` vs `to` yields a rule the English original lacks entirely: escalation under uncertainty.
5. No new vocabulary was required. The improvement comes from grammar and existing compositional inventory.

---

## Recommended reading of the redesign

If the classic Three Laws are remembered as:

1. don't harm people
2. obey people
3. protect yourself

the Tonesu-native rewrite is better remembered as:

1. persons have rights
2. danger creates rescue duty
3. only recognized authority binds
4. uncertainty must be escalated
5. maintenance is subordinate, not sovereign

That is longer, but it is also far less likely to hide the real failure mode inside one overloaded sentence.

---

## Colloquial Register Analysis

| Form used | CLQ entry | Colloquial form | Notes |
|-----------|-----------|-----------------|-------|
| `wi-fe-ka [la-mu ka-de lo-i-zo-li]` | none | — | clause-level prohibition — semantically load-bearing |
| `ka-no-de` | none | — | 3-root preservation form — ethical/technical core |
| `wi-ra` | none | — | authority distinction is the key analytical gain |
| `to-fe-li` | none | — | formal institutional arbiter — load-bearing |
| `no-de` | none | — | preservation/maintenance predicate — minimum form |

**Verdict:** irreducibly formal — the point of the batch is to preserve explicit distinctions among rights, authority, uncertainty, and maintenance. Colloquial compression would erase the gain.

*CLQ entries registered from this batch: none.*

---

## ROB-002 — Edge Cases (S951-S956)

ROB-001 established the law architecture. ROB-002 asks whether that architecture survives contact with the cases that usually break robotic-law thought experiments:

1. two authorized humans giving contradictory orders
2. one danger known and another only signaled
3. uncertainty that is serious enough to warn, but not yet strong enough to confine
4. the shift in legal status when an epistemic arbiter does or does not certify the danger claim

The design principle here is simple: edge cases should not be resolved by inventing an invisible machine intuition. They should be resolved by explicit routing and explicit norm-state changes.

### ROB-002 Table

| Entry | Tonesu | Written | Function |
|------|--------|---------|----------|
| S951 | `go {la-i-zo-li ne wi-ra lo-mu ; la-ze ne wi-ra lo-mu ; la-i-zo-li wi-ra [la-mu wi-ka] / la-ze wi-ra no [la-mu wi-ka]}, la-mu ka-si lo-to-fe-li lo-ze` | `go {laizoli ne wira lomu ; laze ne wira lomu ; laizoli wira [lamu wika] / laze wira no [lamu wika]}, lamu kasi lotofeli loze` | contradictory authorized demands route upward |
| S952 | `go {la-i-zo-li zo-ra de ; la-mu si [la-ze zo-ra de] / la-mu no-to [lo-ze]}, la-mu ne-fe lo-ka-no-de lo-i-zo-li` | `go {laizoli zora de ; lamu si [laze zora de] / lamu noto [loze]}, lamu nefe lokanode loizoli` | known danger outranks suspected danger |
| S953 | `go {la-mu si [la-i-zo-li zo-ra de] / la-mu no-to [lo-ze]}, la-mu ka-fe-si ne-i-zo-li / no-wi-fe-ka [la-mu ka-ko lo-i-zo-li]` | `go {lamu si [laizoli zora de] / lamu noto [loze]}, lamu kafesi neizoli / nowifeka [lamu kako loizoli]` | uncertainty licenses warning, not confinement |
| S954 | `go {la-mu ka-si lo-to-fe-li lo-ze ; la-to-fe-li no-to [lo-ze]}, wi-fe-ka [la-mu ka-ko lo-i-zo-li]` | `go {lamu kasi lotofeli loze ; latofeli noto [loze]}, wifeka [lamu kako loizoli]` | non-certification keeps containment forbidden |
| S955 | `go {la-mu ka-si lo-to-fe-li lo-ze ; la-to-fe-li to [lo-ze]}, no-wi-fe-ka [la-mu ka-ko lo-i-zo-li]` | `go {lamu kasi lotofeli loze ; latofeli to [loze]}, nowifeka [lamu kako loizoli]` | certification permits protective containment |
| S956 | `la-wi-fe-su no to-su-ki lo-to-fe {wi-ra ; si ; to} / ke, la-mu ne-fe lo-ka-si lo-to-fe-li` | `lawifesu no tosuki lotofe {wira ; si ; to} / ke, lamu nefe lokaci lotofeli` | routing-before-coercion verdict |

### What ROB-002 adds

#### 1. Contradictory authority is a routing condition

The classic laws never say what happens if two valid humans issue opposite commands. ROB-002 does: the machine reports the conflict upward rather than smuggling in a hidden priority rule.

That is the real advantage of `wi-ra` in Tonesu. Once authority is explicit, contradictory authority can also be explicit.

#### 2. Warning and containment are different acts

S953 is the practical gain point of the second batch.

- `ka-fe-si` = warn
- `ka-ko` = contain / detain / confine

English robotics discourse often slides from "possible danger" to "intervene now" without stating the legal boundary crossed in between. Tonesu does not need to slide. A machine can warn under uncertainty while still being forbidden to confine.

#### 3. Certification, not urgency alone, changes what the machine may do

S954 and S955 are a minimal pair.

- `la-to-fe-li no-to [lo-ze]` -> containment forbidden
- `la-to-fe-li to [lo-ze]` -> containment permitted

That is a strong result. The same act changes deontic status when the proposition changes epistemic status under recognized adjudication.

#### 4. The deeper law is procedural

ROB-001's main insight was that uncertainty should be escalated.

ROB-002 sharpens that further: escalation is not just an emergency fallback. It is part of the law-set itself. In edge cases, routing is the lawful action.

### Combined findings after ROB-001 + ROB-002

1. Tonesu can restate the classic Three Laws cleanly.
2. Tonesu improves them most where English compresses authority and certainty.
3. The strongest Tonesu-native addition is now two-part:
	- uncertainty must be escalated
	- coercion must track certification, not mere suspicion
4. No new robotics vocabulary is needed yet. The law architecture still carries the main design pressure.

### Colloquial Register Analysis

| Form used | CLQ entry | Colloquial form | Notes |
|-----------|-----------|-----------------|-------|
| `ka-fe-si` | none | — | warning verb — operational distinction |
| `ka-ko` | none | — | containment verb — operational distinction |
| `to-fe-li` | none | — | formal arbiter role — load-bearing |
| `si / no-to / to` | none | — | epistemic grades are the point |

**Verdict:** irreducibly formal — ROB-002 works only if warning, authority, adjudication, and containment remain explicitly distinct.

*CLQ entries registered from this batch: none.*