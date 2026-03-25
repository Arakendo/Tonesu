---
title: "SUT"
---

# SUT

*Theme: [Foundations](../../foundations/overview.md)* · 7 sentences.

[← Foundations](../../foundations/overview.md) · [← Corpus](../../overview.md)

---

## SUT-001 · 

**Purpose:** First-attest W101 (`su-ti`, state-snapshot predicate) and `wi-fe-ka` (rule-forbidden predicate) in corpus sentences, confirming `lo-X su-ti Y` state-configuration grammar and both agentless and policy-mediated prohibition forms.

<span id="S665"></span>
**S665**
`lo-ki  su-ti  no-ra`
*The machine is currently in an inactive configuration.*

!!! annotation "Notes"
    W101 (`su-ti`) first corpus attestation. `lo-X su-ti Y` = X is currently in state Y (static snapshot — no change implied). Y here is `no-ra` (zero-force = inactive, compositional). Compare `lo-ki  no-be` (the machine is not increasing — a *change* predicate); `lo-ki  su-ti  no-ra` = the machine holds the inactive state (a *snapshot* predicate). Resolves the open-questions.md note: "no primitive for stable condition without invoking change or evaluation."

<span id="S666"></span>
**S666**
`lo-ki  su-ti-de  ra`
*The machine's previous configuration was powered.*

!!! annotation "Notes"
    `su-ti-de` = past configuration (W101 + temporal suffix `-de` = past/decay). First attestation of the past-state derived form. Timeline: was powered (S666), is now inactive (S665).

<span id="S667"></span>
**S667**
`lo-ki  su-ti-be  ra`
*The machine's target configuration is powered.*

!!! annotation "Notes"
    `su-ti-be` = expected future/target configuration (W101 + suffix `-be` = growth/expected). First attestation of the target-state derived form. The three sentences S665–S667 establish the full `su-ti` timeline vocabulary: current (`su-ti`), past (`su-ti-de`), target (`su-ti-be`). Batch narrative: currently inactive, was powered, target is to be powered again — S671 provides the mechanism.

<span id="S668"></span>
**S668**
`lo-be-ra  wi-fe-ka`
*A power ramp is forbidden.*

!!! annotation "Notes"
    First corpus attestation of `wi-fe-ka` (W100 derived: willed-boundary as applied to a specific act = the act is prohibited by rule). Patient `be-ra` = growth-force = increasing power = power ramp (compositional). The agentless predicate form `lo-X wi-fe-ka` states the prohibition without naming the source; compare S670 which names the policy authority.

<span id="S669"></span>
**S669**
`lo-no-be-ra  no-wi-fe-ka`
*A power decrease is not forbidden.*

!!! annotation "Notes"
    `no-wi-fe-ka` = not-rule-forbidden = permitted (compositional: `no-` + `wi-fe-ka`). First attestation. Patient `no-be-ra` = no-growth-force = decreasing power. Minimal contrast with S668: the prohibited act (`be-ra`, ramp up) and the permitted act (`no-be-ra`, ramp down) differ only in one `no-` modifier. Instantiates the deontic identity: permitted ↔ not-forbidden.

<span id="S670"></span>
**S670**
`la-wi-fe-su  ne  wi-fe-ka  lo-be-ra`
*The safety protocol forbids power ramps.*

!!! annotation "Notes"
    Extension of the DIP-001 rights-claim pattern (`la-X ne wi-fe lo-Y` = X holds rule over Y): `ne wi-fe-ka` attributes the prohibiting form specifically to the patient. `la-wi-fe-su ne wi-fe-ka lo-be-ra` = "The policy holds as rule-prohibited over power-ramps." Contrast with S668 (agentless predicate): same norm, different grammatical perspective — S670 locates the norm in an institutional authority.

<span id="S671"></span>
**S671**
`la-ki  wi-re  lu-su-ti-be`
*The machine self-regulates toward its target configuration.*

!!! annotation "Notes"
    Connects W101 (`su-ti-be`, target state) with W099 (`wi-re`, feedback regulation), confirming the structural relationship noted in W101's registry entry: "a feedback loop is precisely the mechanism for moving `su-ti` from current state toward target `su-ti`." `lu-` = beneficiary/result slot: the regulation is done for the target state. Closes the batch narrative: currently inactive (S665), target powered (S667), feedback (S671) drives toward that target — subject to the no-ramp constraint (S668/S670).

### Batch Summary

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

*Generated from [`registry/entries.yaml`](https://github.com/Arakendo/Tonesu/blob/main/registry/entries.yaml).*