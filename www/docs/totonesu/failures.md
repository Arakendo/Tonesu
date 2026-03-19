# Failures & Edge Cases

Every language has gaps — things it can't say cleanly, constructions that break under pressure, design choices that create downstream problems. This page documents the ones Tonesu knows about.

These aren't bugs to be fixed in the next release. Some are deliberate tradeoffs. Some are open research questions. All of them are places where a speaker will run into real difficulty.

---

## `ze` ambiguity

The pronoun `ze` picks up the most-recent salient referent. It works for both **persons** and **propositions** — and that dual use creates a known failure mode.

### When it works

Predicate type usually disambiguates:

- **Agent position + action verb** → person reading: `la-ze de lo-si-de` = "ze suppressed the record"
- **Predicate forces propositional** → proposition reading: `la-mi to [lo-ze se]` = "I hold that *that claim* is perception"

When the predicate can only apply to one type, `ze` is unambiguous.

### When it breaks

Some predicates accept both readings. `to-fe-ka` (epistemic fraud) can describe a person ("ze is a fraud") or a proposition ("that claim is fraudulent"):

```
la-mi  to  [lo-ze  to-fe-ka]
```

This sentence is **genuinely ambiguous**. A listener cannot resolve it from grammar alone. (See [C008 walkthrough](conversations.md#c008-arbitration-hearing-ze-collision) for the full exchange.)

### The repair

Speakers restate with explicit NPs:

```
la-ze  to-fe-ka  no  la-mi       →  Ze committed the fraud — not me.
```

Agent position + contrast forces the person reading. The ambiguity is resolved retroactively.

### The design choice

A morphological fix (separate person-`ze` and proposition-`ze`) would prevent this. Tonesu doesn't add it. The reasoning: discourse repair is cheaper than permanent morphological overhead, and the failure mode is *productive* — it surfaces exactly the cases where meaning is genuinely contested.

In formal registers (legal, arbitration), the institutional practice is to reset to full NPs after any `ze` ambiguity event.

---

## Performative / expressive register gap (EM-001)

Tonesu has no register for non-propositional emotional utterances.

"Ugh." "Oh no." A sigh of relief. Crying. These are not propositions — they don't assert, question, or command. They *express*.

In Tonesu, every utterance passes through the epistemic frame: `la-X se/si/to [content]`. But grief and joy don't have content in that sense. You can say `la-mi ne fade` ("I am in a state of felt loss"), but that's a clinical report, not an expression of grief.

### Two positions

1. **Paralinguistic default** — these utterances exist outside grammar in every language. Tonesu speakers cry, laugh, and sigh just like anyone else. The grammar doesn't claim jurisdiction.

2. **Cultural suppression** — a civilization built around epistemic precision may have *displaced* raw emotional expression. If your culture treats `se` (raw perception) as the lowest epistemic category, does that devalue the pre-verbal? What does it mean that the language has no word for "ow"?

### Status

Open question. No proposal on the table. The gap is documented because it's real and because both positions say something interesting about the language.

---

## The manufactured-doubt problem

Tonesu has `to-fe-ka` (deliberate epistemic fraud — W060) and `to-fe-ki` (honest epistemic misjudgment — W059). But from the outside, three positions look identical:

1. **Genuine conservative judgment** — speaker sincerely believes the evidence is insufficient
2. **`to-fe-ki` honest misjudgment** — speaker sincerely miscalibrated but the error is identifiable
3. **`to-fe-ka` deliberate deflation** — speaker is intentionally understating the epistemic status

How do you tell them apart? Only if `to-fe-su` (the epistemic standards body — W058) defines procedural thresholds that make (2) and (3) distinguishable from (1).

### Why this matters

"I don't think the evidence is strong enough" and "I am deliberately suppressing the evidence" produce the same observable behavior: a claim gets downgraded. The distinction is entirely about *intent* and *compliance with declared standards*.

A language that can name the crime (`to-fe-ka`) but can't reliably detect it isn't broken — it's honest about the limits of linguistic evidence. But it means that `to-fe-ka` accusations in formal proceedings are inherently high-stakes: you're claiming to know another person's intent.

### Status

Open question. Partial mitigation: if `to-fe-su` publishes explicit thresholds, then *failure to meet published standards* is observable even when intent isn't. The institutional solution compensates for the linguistic gap.

---

## Epistemic deflation vs inflation

`to-fe-ka` covers both directions:

- **Deflation** — claiming something is less established than it actually is
- **Inflation** — claiming something is more established than it actually is

Proving deflation requires establishing what status a claim *had actually reached* — which means the accuser must demonstrate the true epistemic status before they can demonstrate the misrepresentation. Inflation is somewhat simpler: you show the evidence was insufficient for the status claimed.

### Status

Open question. A directional qualifier might be needed when the direction of fraud matters legally. No proposal yet — the current solution is that context disambiguates in practice, and formal proceedings would specify the direction in the charge.

---

## Transfer without loss

`de` (decay, decrease) implies the giver's possession ends. That works for physical transfer — if I give you a tool, I no longer have it. But sharing, copying, and broadcasting don't work this way:

- Sharing knowledge: the teacher still knows it
- Copying a record: the original persists
- Broadcasting a signal: the source doesn't lose it

### The gap

There's no clean compound for "give without losing." `de` structurally implies loss. Candidates:

- `ka-ne` (intentional connection) — but that's about *linking*, not *duplicating*
- `de-ki-be` (decrease-change-growth) — but that's a strange composition: "loss that becomes growth"?

### Status

Open question. No corpus pressure yet — no sentence has needed this and failed to express it. When one does, the compound will be built to fit the actual communicative need rather than the hypothetical one.

---

## Maximum compound length

How long can a compound get before it needs compression or restructuring?

The longest registered compounds are 4–5 morphemes. The `'` juncture marker helps with parse clarity, but at some point a compound becomes a phrase pretending to be a word.

### Current practice

- 2–3 morphemes: normal compounds (`to-li`, `ra-ki-mu`)
- 4 morphemes: common, usually with `'` (`pa-wi'ka-su`)
- 5+ morphemes: rare, and each one should be questioned

### The question

Is there a firm ceiling? Should compounds above a certain length automatically require `'`? Should very long forms always have colloquial shortcuts?

### Status

Open question. The CVC colloquial contraction system (see [Register](register.md)) provides a pressure valve for high-frequency long forms, but there's no formal rule about when contraction becomes *mandatory*.

---

## Definiteness

Tonesu has no dedicated definiteness markers ("the" vs "a"). Context does the work most of the time, but there are cases where "the machine" and "a machine" need to be distinguished and the grammar provides no tool for it.

Candidates:

- Repurpose `ko` (containment) as a definite marker — but `ko` is now the containment primitive and reuse would create collision
- Repurpose `ne` (relation) — similar collision risk
- Create a new particle — but the design principles resist adding particles for things context can usually handle

### Status

Open question. No formal proposal. The current practice is that discourse context and `ze` back-reference handle most definiteness needs. The remaining cases are genuine gaps.

---

## Vowel length

Should vowel length be used as a morphological tool? It would expand the phonological space significantly, but at the cost of:

- Increased learning difficulty
- Potential parse ambiguity in fast speech
- Violation of the current simplicity of the tier system (CV, CVC, CVCC shapes would need length distinctions)

### Status

Open question. Current position: avoid the complexity unless a genuine structural need emerges that can't be solved by compounding.

---

## What these gaps mean

A language without documented failures is a language that hasn't been tested. These edge cases show where Tonesu's design choices create real consequences:

- **`ze` ambiguity** → discourse repair over morphological complexity
- **No expressive register** → epistemic precision may suppress raw expression
- **Manufactured doubt** → the language can name cognitive crimes it can't always detect
- **Transfer without loss** → physical-object metaphors don't cover information
- **No definiteness** → context-dependence has limits

None of these are scheduled for "fixing." Some may never be resolved. They're the price of the design choices that make the rest of the language work.
