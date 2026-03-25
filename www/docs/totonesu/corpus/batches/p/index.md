---
title: "Early Grammar Probes"
---

# Early Grammar Probes

*Theme: [Grammar & syntax](../../grammar/overview.md)* · 4 sentences.

[← Grammar & syntax](../../grammar/overview.md) · [← Corpus](../../overview.md)

---

## P002 · Early Grammar Probe

<span id="S016"></span>
**S016** · *legacy*
`la-mi  ka-be-past  lo-mu  wi [la-tu  ka-mu-ka  lo-mu]`
*I built the machine for you to use.*

!!! annotation "Notes"
    - **Boundary rule test (pass):** `wi` opens the purpose clause at `la-tu`. The clause extends to sentence end — no matrix-level marker follows; right edge is sentence termination. Boundary rule holds. ✓
    - **Different-agent confirmed:** Main-clause agent is `mi` (I); purpose-clause agent is `tu` (you). `la-tu` must be explicit. Same-agent reduction does not apply. Spec constraint correct.
    - **Same-patient reduction: provisionally valid.** `lo-mu` (patient:machine) appears in both clauses. The reduced form recovers the patient from the immediately preceding main-clause patient. Recovery is unambiguous in this configuration. First corpus evidence bearing on the open question from spec/grammar.md § Purpose Frame. Provisional verdict: same-patient reduction is valid when the shared patient is explicitly present in the main clause; update grammar spec accordingly.
    - **`mu-ka`** (W022) = operate/use an artifact. Head-final: artifact (`mu`) specifies the action (`ka`). Registered in registry/derived.md. Placeholder `ka-use` retired.
    - **`ka-be-past`:** tense marker is a placeholder gloss, consistent with current corpus convention.

## P003 · Early Grammar Probe

<span id="S017"></span>
**S017** · *legacy*
`la-ze  lo-si  ka-si-ki-past  wi [ka-fe-si  ne-yu]`
*She sent the message to warn them.*

!!! annotation "Notes"
    - **P003 is same-agent by default,** not different-agent. Plain English "warn them" has the sender as the warner; the message is the instrument, not an independent agent. This is a control property of the verb, not of the purpose-frame itself.
    - **Agent inheritance rule (3rd confirmation):** purpose clause omits `la-ze` → matrix agent `ze` inherited unambiguously. See spec/grammar.md § Purpose Frame — rule now formally stated.
    - **`ne` particle inside purpose clause:** `ne-yu` (recipient:them) appears inside the `wi` subordinate clause without issue. `ne` marks an argument within the clause; it is not a clause introducer and does not affect the boundary rule. Passes cleanly. ✓
    - **Boundary rule (pass):** `wi` opens, purpose clause runs to sentence end. Same right-edge pattern as S016. ✓
    - **P003b** exposes the genuinely different-agent case: `la-yu` required when purpose-clause agent ≠ matrix agent. Consistent with S016. The absence of an agent marker in a `wi` clause now has a confirmed, unambiguous interpretation: inherit the matrix agent.
    - **Two new vocabulary items registered:** `si-ki` (W023) = send/transmit; `fe-si` (W024) = warn/alert. Both proposed-status.
    - **`ka-si-ki-past` and `ka-fe-si`:** tense/aspect markers remain placeholder glosses.

## P001 · Early Grammar Probe

<span id="S018"></span>
**S018** · *legacy*
`la-yu  ka-to-ki  wi [ka-to-su-ki]`
*They study in order to comprehend.*

!!! annotation "Notes"
    - **Agent inheritance rule (4th confirmation):** purpose clause omits `la-yu` → matrix agent `yu` inherited without ambiguity. Rule confirmed.
    - **`to-su-ki` first corpus attestation:** W025 (to-su + inchoative `ki` = enter state of organized knowledge). The learning process (`to-ki`) + purpose marker (`wi`) + comprehension threshold (`to-su-ki`) encodes the full arc of understanding: ongoing process → arrival at organized grasping. The combination is productive.
    - **`wi` same-agent reduction (confirmed):** no agent in purpose clause; matrix agent inherited. Consistent with S016 (different-agent), S017 (same-agent with warning semantics). Fourth confirmation.
    - **P001 pass.** No new gaps.

## P004 · Early Grammar Probe

<span id="S019"></span>
**S019** · *legacy*
`lo-to-ko-mu  ne-mi  ka-be`
*Build me a memory device. (imperative: la-tu dropped)*

!!! annotation "Notes"
    - **Imperative resolved:** `la-tu` drop formalized in spec/grammar.md § Imperatives: drop `la-tu`, all other markers remain. Version A above uses the canonical form. Note the SOV argument order is maintained — the agent slot is simply absent.
    - **Relativizer gap confirmed:** "a system that remembers" requires a verbal relative clause; compounding handles this by encoding the capability in the noun itself. `to-ko-mu` (memory-containment-device) works for defining properties (the device IS a memory device) but cannot express incidental predication (a device that happened to already know something specific). Logged in notes/open-questions.md.
    - **`to-ko-mu`** = memory device; formal compound of W027 (`to-ko`). Colloquial short form drops `-mu`; documented in spec/morphology.md.
    - **P004 pass** (partial): imperative gap closed; relativizer remains open.

---

*Generated from [`registry/entries.yaml`](https://github.com/Arakendo/Tonesu/blob/main/registry/entries.yaml).*