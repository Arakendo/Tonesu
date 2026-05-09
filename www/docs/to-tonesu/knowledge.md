---
title: Knowledge & Claims
---

# Knowledge & Claims

*How Tonesu tracks what you know, what you claim to know, and whether the two match.*

Tonesu does not have a word for "lie." It has something more structural: a vocabulary that forces speakers to commit to the epistemic status of every claim they make — and makes violations visible. This page traces the design from the epistemic pipeline through to debate fallacy resistance, and connects it to the scientific tradition that shaped the language.

> Tonesu does not tell you what is true. It tells you what kind of claim is being made.

---

## The epistemic pipeline

English collapses many cognitive states into "know." Tonesu draws a pipeline with distinct stages:

| Written | Parse | Meaning | Stage |
|---------|-------|---------|-------|
| se | `se` | raw sensory detection | I perceived something |
| si | `si` | encoded representation | I have a report or recording |
| to | `to` | conceptual pattern / knowledge | I understand a model |
| tosu | `to-su` | organized structured knowledge | it is established in a body of knowledge |

Each stage is a genuine epistemic upgrade. Moving from `se` to `to` means processing raw perception into an explanatory model. Moving from `to` to `tosu` (to-su) means the model has survived scrutiny and integration into a larger structure.

Two more forms complete the space:

| Written | Parse | Meaning |
|---------|-------|---------|
| toko | `to-ko` | retained knowledge — memory; persisting model |
| tosi | `to-si` | knowledge-seeking signal — query; reaching toward understanding |
| tosuki | `to-su-ki` | entering organized understanding — comprehension; the threshold moment |

The pipeline is directional. A speaker who says `to` when they have only `se` is not being imprecise — they are overclaiming. And Tonesu has a word for that.

---

## The boundary: tofe

tofe (to-fe) — the epistemic boundary. The place where a claim's actual evidence meets the tier it's being presented at. Every claim in Tonesu carries an implicit `tofe` — the line between what the evidence supports and what the speaker asserts.

`fe` is the same root used for physical limits, danger thresholds, and category edges. In Tonesu, a dishonest claim and a structural-engineering failure are the same kind of event: a boundary was violated. Intellectual dishonesty is not a separate moral domain — it is a species of boundary violation.

---

## Two kinds of crossing: tofeka and tofeki

When a speaker presents a claim at a higher (or lower) tier than its evidence supports, the language forces a commitment about *why*:

| Written | Parse | Meaning | Social weight |
|---------|-------|---------|--------------|
| tofeki | `to-fe-ki` | epistemic boundary-crossing by motion — accidental | Correctable; low social cost |
| tofeka | `to-fe-ka` | epistemic boundary-crossing by intentional action — deliberate | Epistemic fraud; equivalent to perjury in high-stakes contexts |

The distinction rests on `ki` (change, possibly passive) versus `ka` (intentional action). There is no convenient grammatical ambiguity between honest error and deliberate misrepresentation. The speaker must commit.

### Two failure modes

Epistemic misrepresentation has two directions:

**Inflation** — presenting `se` or `si` as `to` or `tosu` (to-su). "This is established science" when it is a preliminary observation. The classic case: pseudoscience, propaganda, overclaiming.

**Deflation** — downgrading `tosu` (to-su) to `si`: "this is only a report" when it is in fact an established finding. Harder to prove, because it requires showing what epistemic status the claim had actually reached. The classic case: strategic doubt, manufactured ignorance.

Both directions are `tofeka` (to-fe-ka) when deliberate.

---

## Connection to Popper

Karl Popper's demarcation criterion — a claim is scientific only if it is in principle falsifiable — maps directly onto Tonesu's epistemic scale:

- `se` is directly testable (perceptual).
- `si` is externalized and checkable (documented report).
- `to` is a model, testable through its implications.
- `tosu` (to-su) is registered as established, but remains revisable.

Claims that resist placement on this scale are exhibiting exactly the failure mode Popper named. `tofeka` (to-fe-ka) is Tonesu's grammatical marker for presenting a claim at a higher tier than its evidence supports. Popper would call this pseudoscience. Tonesu calls it epistemic misrepresentation and makes it structurally visible.

Popper's epistemology is inherently social — claims are advanced into a critical discourse and either survive scrutiny or are revised. The `tofeka` discourse-pattern mechanism (repeated misclassification becomes visible over time) implements this without institutional enforcement. Over enough exchanges, a speaker's pattern of epistemic commitments builds a track record. No referee is required; the language records the evidence.

This connects to Popper's vision of the Open Society: epistemically open institutions where claims compete on their merits rather than being enforced by authority. Tonesu encodes the tools for tracking epistemic stance. It does not enforce correctness.

---

## How grammar enforces accountability

Tonesu's grammar provides several independent mechanisms that work together to make epistemic commitments auditable:

### The evidential frame: `()`

Wrapping a clause in `()` marks it as reported, inferred, or unattributed — not directly asserted. A speaker who says `latoli to losemu` ("the scholar knows the data") makes a first-person assertion. A speaker who says `(latoli to losemu)` flags it as something they've heard or inferred. Removing the parentheses is a visible upgrade in commitment.

### The topic frame: `:`

The `:` particle pins a topic explicitly at the sentence opening. Once a topic is set, shifting to a different topic requires a new `:` — making topic substitution (a common rhetorical evasion) structurally visible. You cannot slide from the issue to the person without grammatically announcing it.

### Causal chains: `go` vs `ta`

`go` asserts a causal mechanism — this thing *produced* that result. `ta` marks temporal sequence only — this happened, then that happened. Confusing the two is a named fallacy (*post hoc ergo propter hoc*), and Tonesu separates them at the particle level. A speaker who uses `go` where only `ta` is warranted is overclaiming causation.

### Predicate distinctness

When a speaker retreats from a bold claim to a weaker one (motte-and-bailey), the two claims require different predicates in Tonesu. The grammar does not allow the substitution to happen silently — the predicate change is visible in the sentence structure.

### Per-link epistemic marking

In a multi-step argument, each link can carry its own epistemic marker (`se`, `si`, `to`, `tosu`, or `nose` — no perception at all). A chain that begins grounded and then launches into speculation is visible step by step. Borrowed grounding — using the credibility of Step 1 to smuggle in Step 4 — becomes auditable.

---

## Fallacy resistance: the corpus evidence

Seven corpus batches (FAL-001 through FAL-007, sentences S364–S397) systematically test how Tonesu's grammar responds to classical and rhetorical fallacies:

### FAL-001: Classical fallacy resistance (S364–S373)

Each sentence demonstrates a classical fallacy and shows which grammatical mechanism blocks or exposes it:

| Fallacy | Mechanism | What happens in Tonesu |
|---------|-----------|----------------------|
| Equivocation | `tofe` (to-fe) vs `wife` (wi-fe) | Different boundary types produce different compounds — homonyms are structurally impossible |
| Straw man | `()` evidential frame | Attributed version must be wrapped in `()` — the original claim remains accessible |
| False dichotomy | Scope particle + unlisted alternatives | Only `ru-fe` creates true exclusion; regular disjunction leaves space open |
| Circular reasoning | `go`-chain audit | Causal chain loops back to the premise — circularity visible in the argument structure |
| Ad hominem | `:` topic frame | Shifting from policy-topic to person-topic requires explicit `:` change |
| Appeal to authority | Epistemic scale | Authority provides `si` (report) or `to` (model), not automatic `tosu` (to-su, established) |
| Post hoc | `ta` vs `go` | Temporal sequence (`ta`) is grammatically distinct from causal claim (`go`) |
| Composition / division | `pe` (part) vs `o-` (collective) | Part-whole reasoning requires explicit structural marking |
| Is/ought | `to` vs `vo` + `wi` | Descriptive claims (`to`) are grammatically separate from value claims (`vo`) and will claims (`wi`) — Hume's guillotine |
| Modal fallacy | Epistemic tier markers | Each step in a modal chain carries its own certainty marker |

### FAL-002: Rhetorical fallacies (S374–S378)

| Fallacy | Mechanism |
|---------|-----------|
| Motte-and-bailey | `:` predicates must match at each retreat — switching predicates is visible |
| Moving goalposts | `wife be` (wi-fe be) marks retroactive condition change; old condition preserved in `()` |
| Slippery slope | Unjustified cascade produces a tower of `(du ...)` marks — each step's commitment level shown |
| Appeal to emotion | Affective states (`fa`) valid in causal chains but require value-commitment (`vowi`, vo-wi) alongside |
| Loaded question | Presuppositions must be extracted to `()` before the question is well-formed |

### FAL-003–FAL-006: Nested and composite (S379–S392)

These batches escalate complexity: nested presuppositions, double topic-substitution, compound slippery slopes, and full political-rhetoric composites. Key finding: the mechanisms compose cleanly. A five-move political speech (evidential laundering + topic substitution + catastrophe cascade + normative leap + modal inflation) produces five independently diagnosable stack-trace items (S388).

### FAL-007: Good-faith control (S393–S397)

The final batch tests well-formed political speech: honest attribution, topic consistency, warranted causal chains, and conservative epistemic calibration. This confirms the mechanisms are not adversarial — they do not penalize speakers who are arguing in good faith.

---

## Discourse accountability at scale

Three additional corpus batches test how epistemic accountability works across multi-turn exchanges:

**DEB-001** (S539–S548) — a heated philosophy debate on knowledge vs. action. By Round 3, explicit denial (`no —`) becomes informationally stale. The `ke` correction particle signals position advance without re-performing the denial. Finding: the information-freshness rule — `no —` is correct when denial adds new information; `ke` is correct when denial is already contextually encoded.

**MED-001** (S569–S578) — medical differential diagnosis. Same information-freshness rule in a formal clinical register. Evidence that the rule generalizes across discourse contexts.

**DIP-001** (S579–S588) — diplomatic treaty negotiation. Third attestation of `ke`. In negotiation (designed for agreement), continued explicit denial at Round 3 signals obstruction; `ke` signals good-faith counter-position. The bad-faith dimension emerges naturally from the epistemic tracking.

---

## The irony

A language with precise epistemic vocabulary does not eliminate political manipulation. It *formalizes* it.

Political argument in Tonesu looks like academic peer review. The dominant political maneuver is not the direct lie (`tofeka` inflation — too visible, too dangerous) but *category management*: argumentation about which epistemic tier applies. "Your climate data is only `si`, not `to`" is a legitimate move in this system. Strategic precision — using `to` carefully where `tosu` (to-su) might be warranted — stays within bounds while applying political pressure.

The moderator's question — "Is your claim `si`, `to`, or `tosu`?" — is a realistic institutional procedure, not an absurdity.

Tonesu's answer to dishonesty is not enforcement but transparency: make the commitments visible, track the patterns, and let the discourse do the rest.

---

## Beyond tofeka: legitimized epistemic closure

All of the above assumes the accountability mechanisms are accessible — that a speaker *can* be called on their epistemic commitments. But there is a structural condition in which the accountability apparatus itself operates inside a legitimized boundary. Tonesu has a compound for this:

**wife'atofeka** (wi-fe · a-to-fe-ka) — legitimized epistemic closure.

| Parse | Reading |
|-------|---------|
| `wi-fe` | entitlement / right (will-boundary: the boundary a right-claim creates) |
| `a-` | universal scope prefix |
| `to-fe-ka` | deliberate epistemic boundary-crossing |
| `[wi-fe]'[a-to-fe-ka]` | entitlement-framing of universal knowledge-boundary-enactment |

The juncture `'` is load-bearing: without it, `a-` would attach to `wi-fe` rather than crystallizing `[a-to-fe-ka]` as a pre-bound unit. The compound is written `wife'atofeka`; the apostrophe is part of the word.

### Why it is not propaganda

`tofeka` (to-fe-ka) — deliberate epistemic misrepresentation — dissolves under exposure. Once a speaker knows they are being deceived, the mechanism fails. Propaganda is parasitic on the target's ignorance.

`wife'atofeka` does not dissolve under exposure. Knowing about it does not remove you from it. The mechanism:

| Written | Parse | Reading |
|---------|-------|---------|
| `lakaside ki lo kaside` | `la-ka-si-de ki lo-ka-si-de` | Knowing propaganda dissolves propaganda. |
| `ke, latowife'atofeka no [ki lowife'atofeka]` | — | But knowing wife'atofeka does not dissolve wife'atofeka. |

The difference is the `wi-fe` wrapper. The limits on knowing are framed as *entitlements* — the rightful shape of knowledge — rather than as external constraints. Inside the condition, the boundary does not feel like a limit. It presents as the structure of knowledge itself:

```
lawife'atofeka no ne tofe
→ Epistemic closure does not present as a knowledge-boundary.

lawife'atofeka ne tosu
→ Epistemic closure presents as the structure of knowledge.
```

### Self-licensing

The structural signature of `wife'atofeka` — what distinguishes it from any other epistemic condition — is that it licenses itself:

```
lawife'atofeka ne gosi wife'atofeka
→ Epistemic closure operates by means of epistemic closure.
```

Compare propaganda:

```
lakaside no ne gosi kaside
→ Propaganda does not operate by means of propaganda.
```

Propaganda requires an external truth-ground to distort. `wife'atofeka` has no such dependency: the legitimating frame and the thing being legitimated are the same structure. This is the canonical diagnostic: `lawife'atofeka ne gosi wife'atofeka / lakaside no ne gosi kaside`.

### Three levels of failure

Meta-awareness does not exit the condition:

| Level | Sentence | Result |
|-------|----------|--------|
| Object-level exposure | I know the specific false claim | Fails — still inside |
| Meta-awareness | I know that knowing does not dissolve it | Fails — still inside |
| Knowing the mechanism | I know it is self-licensing | Fails — still inside |

The conditional form: `go {lazoli to [wife'atofeka ne gosi wife'atofeka]}, lazoli ne wife'atofeka` — given a person knows that epistemic closure is self-licensing, that person is still inside epistemic closure.

The scholarly study of the condition is also inside it: `latosu lowife'atofeka ne wife'atofeka` — structured knowledge about epistemic closure is itself epistemic closure.

### The exits

Two escape conditions are available:

**Omniscience** (`tonofe`, to-no-fe — knowledge without any limiting boundary). An unbounded knower has no `fe` boundary; the self-licensing structure cannot apply: `latonofe to [wife'atofeka ne gosi wife'atofeka] / no ne wife'atofeka`. Not available to finite beings.

**Natality** (`beki`, be-ki — the capacity for new beginning). Natality does not operate *through* epistemic closure — it is constitutively novel: `labeki ne nogosi wife'atofeka`. A new beginning is not licensed by the prior legitimizing structure, because it is by definition structurally new.

The exclusive claim: `rufe, labeki ne nogosi wife'atofeka` — for finite agents, natality is the only exit. All finite epistemic moves (exposure, meta-awareness, critical analysis) remain inside. Only the structural novelty of genuine new beginning (`beki`) is constitutively outside.

### Where this shows up

The concept emerged from Hannah Arendt's analysis of totalitarianism — specifically the observation that ideological systems require subjects to be active agents of legitimation, not merely passive witnesses. The `wi-fe` wrapper encodes Arendt's key insight: the coercion is not experienced as coercion but as right. The cascade: atomization → structural force → the total-power-structure presents itself as the legitimate shape of knowledge (`lanoNezoli ; lasura ; laarase ne wife'atofeka`).

The compound is not limited to this context. It applies wherever the entitlement-frame around a knowledge-limit is successfully naturalized:

- Institutional credentialing that defines what counts as valid inquiry
- Legal frameworks that determine what evidence is admissible
- Professional consensus that sets the epistemic boundary for a field
- Cultural inheritance that treats certain questions as settled by definition

In each case, the diagnostic question is the same: does the legitimizing frame dissolve under exposure, or does it absorb it?

`lawife'atofeka ne gosi wife'atofeka` — if yes, it licenses itself.

