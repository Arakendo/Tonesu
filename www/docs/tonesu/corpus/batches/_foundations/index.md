---
title: "Early & Unbatched Sentences"
---

# Early & Unbatched Sentences

*Theme: [Foundations](../../foundations/)* · 45 sentences.

[← Foundations](../../foundations/) · [← Corpus](../../overview.md)

---

## Unbatched

<span id="S001"></span>
**S001** · *legacy*
`la-engineer  lo-machine  ka-build  ta-now`
*The engineer builds the machine.*

<span id="S002"></span>
**S002** · *legacy*
`la-researcher  lo-knowledge-system  ka-improve  ta-future`
*The researcher will improve the knowledge system.*

<span id="S003"></span>
**S003** · *legacy*
`la-engineer  lo-machine  ro-tool  ka-build-now`
*The engineer builds the machine with a tool.*

<span id="S004"></span>
**S004** · *legacy*
`la-engineer  lo-machine  ka-no-build  ta-past`
*The engineer did not build the machine.*

<span id="S005"></span>
**S005** · *legacy*
`la-engineer  lo-machine  ka-build-now  ?`
*Is the engineer building the machine?*

<span id="S006"></span>
**S006** · *legacy*
`la-engineer  pa-workshop  ka-work  ta-now`
*The engineer works in the workshop.*

<span id="S010"></span>
**S010** · *legacy*
`la-to-li  lo-[to-su-mu]  ka-design  ta-past`
*The scholar designed the database.*

<span id="S011"></span>
**S011** · *legacy*
`go-ra-excess  du-machine-fail`
*The machine failed because of excess energy.*

<span id="S012"></span>
**S012** · *legacy*
`la-na-Derik  ne-li-na-Mira  vo-close`
*Derek and Mira have a close relationship.*

<span id="S013"></span>
**S013** · *legacy*
`la-to  ka-be  ta [la-si  ka-ne-ki]`
*Knowledge grows at the time that information connects.*

!!! annotation "Notes"
    - **`la-to` is now clean.** With the agent particle renamed to `la`, abstract agents no longer collide with the person/agent root `li`. `la-to` = "agent: conceptual-pattern" unambiguously.
    - **Attempt 2 is canonical.** The causal frame (`go`/`du`) naturally handles "when X, Y follows" without a dedicated conditional particle. Formalized in spec/grammar.md as the Causal Conditional structure.
    - **`ne-ki` = connect** (relation + motion → become-related) is the first attested use of the inchoative pattern `ROOT + ki`, now formalized in spec/morphology.md.
    - The original attempts were written before the `li`/`la` split — the old forms `li-to`/`li-si` are replaced above with canonical `la-to`/`la-si`.
    
    **Verdict:** Primitives held. Both grammar gaps identified here are resolved:
    1. ~~Particle/root collision for `li`~~ → resolved: agent particle renamed to `la`
    2. ~~Inchoative derivation undefined~~ → resolved: `ROOT + ki` = enter state ROOT (spec/morphology.md)

<span id="S014"></span>
**S014** · *legacy*
`la zo-li  lo si-ko-mu  ka-be`
*People create information-storage artifacts.*

!!! annotation "Notes"
    - `zo-li` = living-person: the natural compound for "people." With `la` as the unambiguous agent particle, `la zo-li` is clean — particle followed by root compound, no collision.
    - `si-ko-mu` = signal + containment + artifact. Head-final rule: `mu` (artifact) is the head; characterized by containing (`ko`) signals (`si`). The purpose clause "to store information" is absorbed into the compound — the artifact's nature encodes its purpose.
    - `ka-be` = action:generate/create. `be` (growth/creation) covers intentional fabrication at this stage.
    - **Purpose clause absorbed by compounding:** Works here because purpose IS the artifact's nature. For external purpose — "She studies *to understand*", "He runs *to escape*" — a general purpose-clause structure is now formalized in spec/grammar.md: `wi [clause]` introduces the intended outcome. `wi` is a transparent overlap with root `wi` (will/intention).
    
    **Gaps exposed:**
    1. ~~**Purpose clauses**~~ → resolved: `wi [clause]` formalized in spec/grammar.md.
    2. `si` (signal/representation) is carrying "information" in both S013 and S014. Confirm this is the right root vs. `to` (conceptual pattern) or `to+si` (encoded knowledge).

<span id="S015"></span>
**S015** · *legacy*
`ta [la-yu  ka-to-ki]  la-to  ka-be`
*When they study, knowledge grows.*

!!! annotation "Notes"
    - **Boundary rule test (pass):** `ta` opens the subordinate clause `la-yu  ka-to-ki`. The matrix clause begins at `la-to` — the next matrix-level argument marker. The subordinate agent `la-yu` is already consumed, so `la-to` is unambiguously matrix-level. Boundary recovered without explicit delimiters. No new machinery needed for this case. ✓
    - **`ta` vs `go` doing real work:** S013 used `go` to *assert causation* — "because information connects, knowledge grows." This sentence uses `ta` for temporal correlation only — "when studying happens, knowledge grows" — without claiming studying is the cause. The `ta`/`go` distinction is not cosmetic; the two frames make genuinely different claims.
    - **`yu` first corpus appearance:** `la-yu` is the first gloss use of the renamed group pronoun. No collision with root `wi` (will/intention). Clean.
    - **`to-ki`** = W020 (learning/computation/reasoning). "Study" is the deliberate human variant; `to-ki` covers it at this stage.

<span id="S025"></span>
**S025** · *legacy*
`la-su-mu-li  lo-mu  ka-se-past`
*The engineer inspected the machine.*

!!! annotation "Notes"
    - `su-mu-li` (W002) = engineer / systems-builder. First narrative use of this role compound.
    - `ka-se` = action of perceiving = inspect / examine deliberately. `se` (perception) used as verbal root with action particle. The act is intentional (`ka`), the mode is perceptual (`se`). No separate compound word needed; particle + root form is sufficient. Noun form `se-ka` (examination / inspection) registered as W034.
    - `-past` tense marker is placeholder gloss.

<span id="S026"></span>
**S026** · *legacy*
`lo-ze  de-past`
*It was damaged.*

!!! annotation "Notes"
    - **Agentless-event construction tested:** `lo-ze  de-past` = the machine (as patient) underwent a decay event; no agent specified. This is distinct from `la-[agent]  lo-ze  ka-de-past` (someone intentionally damaged it). The absence of `la` + bare `lo` = passive / agentless event.
    - **Copula gap flagged:** "It was damaged" is a predicative adjective in English (state attribution). Tonesu handles this by treating the state as a past event (`de-past`). A dedicated copula structure for "X is [in state] Y" without implying an event remains undefined. Logged in open-questions.md.
    - **`ze` as non-person pronoun:** first use of `ze` for an inanimate artifact. Confirms `ze` covers all non-speaker/non-addressee referents, including objects.
    - **T006 parallel:** "The old structure collapsed" (T006) is structurally identical — agentless past event, patient as subject. This sentence gives concrete corpus evidence for that pattern.

<span id="S027"></span>
**S027** · *legacy*
`la-ze  lo-ze  ka-de-be-past  wi [ka-ra-be  pa-li-pu]`
*She repaired it to restore power to the city.*

!!! annotation "Notes"
    - **`de-be`** = decay-growth = process of reversing decay = repair / restoration. Head-final: `be` (growth) is the head; `de` (decay) specifies the starting condition. `de-be` = growth characterized as recovery from decay. `ka-de-be` = the act of repairing. Candidate W035; registered in registry/derived.md.
    - **`ra-be`** = energy-growth = energy restoration / power return. `ra` (energy) + `be` (growth/increase) = energy increasing. In the purpose clause: the intended outcome is energy being restored to the city.
    - **`li-pu`** = person-collective = city (colloquial short form of `li-pu-pa`). `li` (social agent) + `pu` (plurality) = organized collective of persons. Full compound: `li-pu-pa` (person-collective-place). In the `pa` particle position: `pa-li-pu` = at/to the city. Candidate W036; registered in registry/derived.md.
    - **Agent inheritance (5th corpus confirmation):** `wi` clause omits agent → matrix agent `ze` inherited. Canonical.
    - **Cross-sentence pronoun tracking:** `mu` (machine, introduced S025) is tracked as `ze` from S026 onward. First multi-sentence pronoun tracking test in the corpus.
    
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
    - **Boundary rule tested (S015–S027):** matrix-level argument marker unambiguously signals return to matrix clause in single-level embedding. `ne` inside subordinate clause confirmed as argument marker, not boundary signal. Nested subordination untested.
    - **Agent inheritance rule (wi-clauses, 5th confirmation at S027):** omitting the purpose-clause agent unambiguously inherits the matrix agent. Rule formally stated in spec/grammar.md § Purpose Frame.
    - ~~**Compounding vs relative clause (S019):** compounding covers noun-naming but breaks for capability expression.~~ Relativizer gap confirmed (S019); imperative gap closed (spec/grammar.md § Imperatives).
    - **Intentionality split (S021–S022):** `ka` on a verb marks deliberate action; bare `be` marks non-intentional production. `ro` marks instrument; `la` marks causal source. Tools use `ro`; natural sources use `la` with bare `be`. Split first attested S021–S022.
    - **Agentless-event construction (S021, S026):** `lo-[patient]  [verb]` without `la` marks a patientive event with no specified agent. First used for instrument-mediated action (S021) and state description (S026). Formal grammar rule pending; see open-questions.
    - **Cross-sentence pronoun tracking (S025–S027):** `ze` successfully tracks a machine referent across three sentences. First multi-sentence pronoun coherence test. `ze` confirmed as covering non-person referents.
    - **Directional destination gap (S024):** `pa` does not distinguish rest-at from move-toward. `di` root candidate for destination particle; see open-questions.

<span id="S093"></span>
**S093**
`lo-di-ki-li  zo-ne-go  la-mi`
*The navigator is my parent.*

!!! annotation "Notes"
    - **First corpus use of `zo-ne-go` (W077).** `zo-ne` = living kin relation (base);
      `go` = origin/source. Together: the entity that is the living-kin-source of the
      reference person. "The navigator is [my] living-kin-origin" = the navigator is
      my parent.
    - No sex distinction. `zo-ne-go` is sex-neutral — it covers what English splits
      into "mother" and "father." Tonesu has no sex or gender primitive, so kinship
      terms are structurally sex-blind. The language cannot say "my mother" vs "my
      father" without additional vocabulary that does not naturally derive from the
      existing primitives. This is a Tonesu cultural result, not a gap: the
      kinship system treats the parent-child bond as structurally prior to sex.
    - **`la-mi` in the second participant position.** The relational predicate has two
      participants: `lo-di-ki-li` (the entity BEING described as a kin-type) and
      `la-mi` (the reference anchor = the speaker, from whose perspective the
      kin-relation is defined). The speaker uses `la-mi` (not `lo-mi`) — consistent
      with the established pattern where first-person always marks its speaker as `la`
      ("agent" in the broad sense of: perspective-holder, perspective-anchor). This
      is a semantic extension of `la` beyond strict intentional action — `la` serves
      as the relational perspective anchor in stative-relational predicates. Flag as
      new grammatical use pressure.

<span id="S094"></span>
**S094**
`lo-ra-ki-li  zo-ne-du  la-mi`
*The pilot is my child.*

!!! annotation "Notes"
    - **First corpus use of `zo-ne-du` (W078).** `zo-ne` base + `du` (result/effect) =
      the entity that is the kin-result of the reference person = child/offspring.
    - The structural parallel with S093 is exact: `lo-[described-party]  [kin-type]
      la-[reference-person]`. The kin-type (`zo-ne-go` vs `zo-ne-du`) encodes the
      direction: toward the source (parent) vs away from the source (child). The
      reference person (`la-mi`) is always in the same position.
    - **`go`/`du` as relational direction qualifiers.** Already established as origin/
      result for causal relations (`go-du` frame). Here they extend into kinship:
      `go` = the source party in the kin-bond; `du` = the result party. The extension
      is semantically transparent — biological parentage is a special case of the
      origin/result polarity. No new semantic burden on either primitive.

<span id="S095"></span>
**S095**
`lo-ra-ki-li  zo-ne-ru  la-mi`
*The pilot is my sibling.*

!!! annotation "Notes"
    - **First corpus use of `zo-ne-ru` (W079).** `zo-ne` base + `ru` (unity/oneness
      /singularity) = kin-unity = a person who shares one origin with the reference
      person. The `ru` qualifier marks that the kin-bond is one of sameness: pilot and
      speaker have the same source. Semantically: `ru` (unity) applied to the kinship
      relation = "we are one in terms of origin."
    - Same structural pattern as S093/S094.
    - Tonesu sibling is also sex-neutral: no distinction between brother and sister.
      `zo-ne-ru` covers both. The language has no mechanism for sex-typed kin terms
      without an unregistered sex primitive — and the design pressure for such a
      primitive has not yet appeared.
    - The sibling relation is symmetric: `lo-A  zo-ne-ru  lo-B` ↔ `lo-B  zo-ne-ru
      lo-A`. The directionality (`la`/`lo`) signals only WHOSE perspective anchors
      the description, not the direction of the bond itself.

<span id="S096"></span>
**S096**
`[S096a]  lo-di-ki-li  zo-ne-go  la-mi`
*The pilot is the navigator's sibling.*

!!! annotation "Notes"
    - **First multi-step kinship path in corpus.** English compresses this to "aunt"
      or "uncle." Tonesu does not. The path is TWO SENTENCES because the kin-bond
      is two steps: from speaker → to parent → to parent's sibling.
    - S096b uses `lo-di-ki-li` in the reference position rather than `la-mi`. This
      confirms the reference participant is not limited to first-person — any
      patient-marked entity can anchor a kinship predicate.
    - KEY FINDING: **Tonesu cannot compress this into a single noun phrase without
      a relative clause.** "My parent's sibling" used as a single noun phrase
      argument (e.g. "I spoke to my parent's sibling" in one sentence) requires
      describing the pilot as "the entity who has kin-unity with the entity who has
      kin-origin status toward me" — which is a relative clause embedding. NO
      relative clause introducer exists in Tonesu grammar yet. This is the first
      corpus moment that definitively requires one. (See NM-001 in open questions.)
    - Tonesus handle this by stating the path declaratively, in sequence. The
      meaning accumulates across sentences. This is fully coherent as a communicative
      strategy — and from a Tonesu perspective, the longer path is actually
      *more informative*, not a workaround. There is no pressure to abbreviate it.

<span id="S097"></span>
**S097**
`lo-di-ki-li  zo-ne-go-re  la-mi`
*The navigator is my ancestor.*

!!! annotation "Notes"
    - **First corpus use of `zo-ne-go-re` (W080).** `zo-ne-go` (parent, W077) +
      `re` (recurrence/cycle) = the recurringly-iterated kin-source = ancestor.
      An ancestor is a parent of a parent of a parent... the `re` marks that the
      origin step recurs up the lineage.
    - `zo-ne-go-re` is **non-specific about generation distance**. It says "some
      iterated number of kin-steps back." The navigator could be the speaker's
      grandparent, great-grandparent, or any more distant ancestor. The compound
      captures the property of being IN the ancestral line, not the specific degree.
    - **Generation count is not expressible with current vocabulary.** To say
      "two generations back" (grandparent specifically) requires either:
      (a) a numeral system (integers, "two" — not yet in corpus); or
      (b) a two-sentence path (`lo-A  zo-ne-go  la-mi` / `lo-B  zo-ne-go  lo-A`
      — B is A's parent; A is my parent; therefore B is my grandparent).
      The language has `nu` (quantity/number) and `re` (recurrence) but no cardinal
      counting system yet. This is the first sentence that definitively requires one.
      (See NUM-001 in open questions.)

<span id="S098"></span>
**S098**
`lo-ra-ki-li  zo-ne-du-re  la-mi`
*The pilot is my descendant.*

!!! annotation "Notes"
    - **First corpus use of `zo-ne-du-re` (W081).** `zo-ne-du` (child, W078) +
      `re` (recurrence) = iterated kin-result = descendant. Parallel structure to
      W080 (`zo-ne-go-re`); the `re` adds the iteration.
    - The compound set is now symmetric at every level:
      - parent / child: `zo-ne-go` / `zo-ne-du`
      - ancestor / descendant: `zo-ne-go-re` / `zo-ne-du-re`
      - sibling: `zo-ne-ru` (no directional pair — the sibling bond is symmetric)

<span id="S099"></span>
**S099**
`lo-di-ki-li  zo-ne-go  lo-ra-ki-li — lo-to-fe-ki-li  zo-ne-go  lo-di-ki-li`
*The navigator is the pilot's parent. The keeper is the navigator's parent.           [Therefore: the keeper is the pilot's grandparent — by two-sentence path.]*

!!! annotation "Notes"
    - **Two-sentence path for "grandparent."** No single-sentence equivalent is
      available without a numeral (to quantify generation distance) or a
      relative clause (to embed a kin-noun phrase). Two declarations, two steps.
    - This sentence also shows `zo-ne-go` with non-first-person reference: both
      `lo-ra-ki-li` and `lo-di-ki-li` serve as the reference anchor (the `la`
      slot is replaced by `lo` for third-person parties). Confirms: the reference
      anchor position takes `la` for first/second person and `lo` for third-person —
      consistent with the existing case marking paradigm.
    - English compresses "grandparent" into a single word. Tonesu requires TWO
      sentences. This is not awkward — it's structurally honest about the fact that
      "grandparent" IS a two-step path. The compression in English is a convenience
      label, not deeper information. Tonesu makes the path explicit.

<span id="S100"></span>
**S100**
`[S100a]  lo-di-ki-li  zo-ne-go  la-mi`
*Someone is the pilot's child.*

!!! annotation "Notes"
    - **The "cousin" equivalence — three sentences.** Each step is one sentence.
      English "cousin" = parent's sibling's child = three structural facts.
      Tonesu states all three. No compression is attempted; none is needed.
    - S100c uses unspecific `lo-li` (patient: a person, unspecified) in subject
      position. This is the first use of bare `li` (person/social agent) as an
      existential rather than a specific named individual. The sentence asserts
      that SOME person is the pilot's child without naming them.
    - **The compression trap.** English speakers encountering this system might
      want to register a compound `zo-ne-ru-du` = kin-unity-result = "child of
      one's sibling" — the Tonesu analogue of "cousin." This would be legitimate
      as a compound. The question is whether Tonesus WANT it. Given what
      the language has shown: they probably don't. A compressed label drops the
      path information. "My cousin" in English is ambiguous about *which* parent's
      sibling's child — first cousin vs second cousin, once-removed vs twice-removed
      — precisely because the label compresses away the path. Tonesu deliberately
      does not compress it.
    - If Tonesu culture ever needs a kinship term for "the child of your
      assigned crew partner" or similar social bond (not biological kin), that would
      be built from `wi-ne` or `ne-li` (intentional-relation or relational-person),
      NOT from `zo-ne`. The `zo-ne` family is strictly biological lineage.

<span id="S101"></span>
**S101**
`[lo-ne-ra  ka-se]  lo-mu  ne-mi  ka-be`
*Build me the machine that perceived the resonance.*

!!! annotation "Notes"
    - **First corpus use of head-final clause modification.** The structure:
      `[lo-ne-ra  ka-se]` = a clause meaning "perceived the resonance" — with no `la-[agent]`
      present. The gap is in the `la` position. The head noun `lo-mu` (the machine) follows
      directly, filling that gap semantically: the machine IS the thing that perceived the
      resonance. In the main clause, `lo-mu` functions as patient of `ka-be` (build it
      for me). The `lo` marking on the head is its MAIN-CLAUSE role, not its inner-clause
      role (where it was the agent).
    - **This directly satisfies S019 Version B** — the target that was deferred at S019
      because no relativizer existed. "A machine that already perceived the resonance" is
      incidental predication (not "a sensing-device by class"). The relative clause form
      handles it; the compound form `se-mu` (W from corpus) handles the CLASS meaning. The
      distinction is now expressible.
    - **Key parsing fact:** `lo-ne-ra  ka-se` without a `la` agent is incomplete as a
      standalone sentence — an agent is expected but absent. This incompleteness is what
      signals to the parser that a gap exists and that the following `lo-mu` fills it.
      Standalone sentences in Tonesu require an agent or a licensed drop (imperative or
      established speaker-drop). Here neither license applies, so the gap is obligatorily
      filled by the following head.

<span id="S102"></span>
**S102**
`[la-di-ki-li  ka-se]  lo-ne-ra  no-to-fe`
*The resonance that the navigator perceived is uncertified.*

!!! annotation "Notes"
    - **Patient gap.** The inner clause `la-di-ki-li  ka-se` has an agent (navigator) but
      no patient. The gap is in the `lo` position. Head `lo-ne-ra` fills the patient gap
      semantically: the navigator perceived the resonance. In the matrix, `lo-ne-ra` is
      the subject of the stative predication `no-to-fe` (uncertified). Particle `lo` is
      consistent: the resonance is the patient/subject of both the inner clause (gap) and
      the matrix predication.
    - **Contrast with agent gap (S101):** in S101, the gap is `la-[head]` (agent) and the
      head exits with `lo` (patient in matrix). In S102, the gap is `lo-[head]` (patient)
      and the head exits with `lo` (also the role for a stative subject in the matrix). The
      critical difference: in S101 the head's inner role ≠ outer role (agent → patient); in
      S102 the head's inner role = outer role (patient → `lo`-subject). The `lo` marking
      is purely the matrix role; the inner role is whatever it needs to be to fill the gap.
    - **Matrix is stative (no `ka`).** `lo-ne-ra  no-to-fe` = "the resonance [is]
      uncertified" — a predication with no action particle. This confirms the matrix
      predicate does not need to be an action clause; any predication form that can take
      a `lo-head` argument is a valid matrix for a head-final relative NP.

<span id="S103"></span>
**S103**
`la-mi  lo-si-ki  [lo-ne-ra  ka-se]  ne-mu  ka-be`
*I gave the code to the machine that perceived the resonance.*

!!! annotation "Notes"
    - **Same inner clause as S101** (`[lo-ne-ra  ka-se]`, gap = agent) but the head exits
      with `ne-mu` (recipient) instead of `lo-mu` (patient). The head's MATRIX role is
      recipient, not patient. This demonstrates the key principle: **the particle on the
      head encodes the head's role in the MAIN CLAUSE, independently of its role in the
      inner clause.** The head-final position carries role information for the outer structure;
      the inner structure's role is inferred from the gap.
    - **Disambiguation:** a naive reading of `ne-mu` alone would be "to the machine"
      (recipient). In context, `[lo-ne-ra  ka-se]  ne-mu` is unambiguous: the bracket
      precedes and modifies `ne-mu`, so `ne-mu` is the head of that NP. The inner clause
      provides the relative description; `ne-mu` provides the matrix slot.
    - **Confirmed: the role-particle on the head is the external role anchor.** The same
      head `mu` (machine) can exit as `lo-mu` (S101, patient), `ne-mu` (S103, recipient),
      or — by analogy not yet tested — `la-mu` (agent of matrix) or `pa-mu` (location).

<span id="S104"></span>
**S104**
`la-mi  lo-si-ki  [zo-ne-go  la-mi]  ne-li  ka-be`
*I gave the code to the person who is my parent.*

!!! annotation "Notes"
    - **Stative inner clause — no `ka`.** `zo-ne-go  la-mi` is a kinship predication without
      an action particle: "kin-origin [from] my perspective." The gap is in the `lo`
      position — the entity BEING described as "my parent" is absent from the clause and
      filled by the head `ne-li`.
    - **`la-mi` appears twice in this sentence:** once as the action agent of the matrix
      (`la-mi ... ka-be` = "I give") and once as the relational anchor inside the kinship
      clause (`zo-ne-go  la-mi` = "my kin-origin"). These are structurally distinct: the
      outer `la-mi` anchors the matrix action; the inner `la-mi` anchors the relational
      definition from which the kin-type is determined. The brackets disambiguate which
      level each `la-mi` belongs to.
    - **`la` as perspective anchor confirmed in embedded context.** In the inner clause,
      `la-mi` is NOT the agent of any action — it is the reference entity from whose
      standpoint the kin-relationship is defined. This is the clearest corpus case yet that
      `la` marks "the participant from whose perspective the clause is evaluated," rather
      than "the intentional agent of an action." The construction is grammatically well-
      formed by applying the head-final modification rule to a stative kinship predication.

<span id="S105"></span>
**S105**
`la-mi  lo-si-ki  [zo-ne-ru  [zo-ne-go  la-mi]  lo-li]  ne-li  ka-be`
*I gave the code to my parent's sibling.*

!!! annotation "Notes"
    - **This sentence directly resolves the S096 NM-001 trigger.** S096 first exposed that
      "my parent's sibling" could not be embedded as a single argument. This sentence embeds
      it as a recipient argument of a matrix clause.
    - **Two-level nesting:**
      - Inner NP: `[zo-ne-go  la-mi]  lo-li` = "the person who is my parent." Gap = `lo-li`
        (patient slot — the entity being described as my parent). Head exits as `lo-li`
        because inside the outer relative clause it serves as the reference entity for the
        sibling relationship (the thing you are sibling TO, which takes `lo` marking per the
        existing kinship predicate structure: `lo-X  zo-ne-ru  lo-Y`). So this is a case where
        the inner head's inner-clause role IS `lo` — not a role change.
      - Outer NP: `[zo-ne-ru  [inner NP]  lo-li]  ne-li` = "the person who is sibling to
        [the person who is my parent]." The outer gap = `lo-[outer-head]` (the entity being
        described as the sibling). Head exits as `ne-li` (recipient in the matrix).
    - **Readability check:** the sentence is longer than any prior single-sentence kinship
      expression, but each bracket level is structurally well-formed and the nesting is two
      levels, not three. Two levels of head-final embedding appear to be routinely parseable.
      Three or more levels would approach the limit of working memory; Tonesu Tonesus
      likely use the multi-sentence path strategy for anything above two levels.

<span id="S106"></span>
**S106**
`[lo-si-de  ka-to-ko]  lo-mu  ne-mi  ka-be`
*Build me a machine that remembers past signals.*

!!! annotation "Notes"
    - **Direct satisfaction of S019 Version B** — the target that opened the relativizer
      gap in S019. The full original target was "Build me a system that remembers past
      queries." `lo-si-de` = signal-decay = prior/past signal data. `ka-to-ko` = action of
      containing knowledge = remembering/retaining. The machine is the agent of `ka-to-ko`
      (gap = `la-mu` position). Head exits as `lo-mu` (patient of `ka-be` = build).
    - **Comparison with `to-ko-mu` (memory-device compound):** S019 Version A used
      `lo-to-ko-mu  ne-mi  ka-be` = "build me a memory device." That expressed a CLASS
      property — the device is BY DESIGN a memory-keeping device. S106 expresses an
      INCIDENTAL property — build me the specific machine that currently has the record of
      past signals. Both are valid; both are now expressible; they mean different things.
      - `to-ko-mu`: "a memory device" = class membership
      - `[lo-si-de  ka-to-ko]  lo-mu`: "the machine that remembers X" = incidental predication about a specific entity
      This is the distinction the relativizer was always needed for. It is now in the language.
    - **`si-de`** (signal + decay = past signal) is its first appearance as a compound.
      Signal = `si`; decay = `de`; signal-that-has-undergone-decay = prior/historical signal
      record. Compositionally clean; not registered as it is an ad hoc compound in this
      context and may have narrower or broader application depending on future uses.

<span id="S107"></span>
**S107**
`la-mi  se  [lo-mu  ne-ra  no-to-fe]`
*I have a signal-level reading: the machine's resonance is uncertified.*

!!! annotation "Notes"
    - **First corpus use of positive perceptual floor `la-mi  se  [prop]`.** C007 B4
      established `la-mi  no-se  [prop]` (perceptual floor negated). This is the positive
      form: "I hold at perceptual / signal level: [prop]." Consistent with the modal scale
      formalized in spec/grammar.md § Epistemic Modality. The positive scale is now fully
      attested: `la-mi  se` (S107), `la-mi  si` (C001 A3, C006 A4), `la-mi  to` (C007 B1).
    - **The embedded proposition `[lo-mu  ne-ra  no-to-fe]` is a stative predication** —
      no `ka`. "The machine has uncertified resonance." The machine holds the `lo` patient
      position; `ne-ra` is a compound predicate; `no-to-fe` is the state modifier. The
      entire prop is a stative-predication clause, not an action clause. This confirms that
      the epistemic modal frame takes propositions of any predicate type (action and
      stative alike) — consistent with prior cases but here the first example where the
      prop is purely stative.
    - **Stative relative test (companion):** the same inner clause `lo-mu  ne-ra  no-to-fe`
      can be tested as a relative modifier. By the head-final rule: `[ne-ra  no-to-fe]  lo-mu`
      = "the machine with uncertified resonance" — a stative-predicate relative clause with
      no `ka`, gap = `lo-mu` (patient of predication). The head exits as `lo-mu`. This works
      by the same rule as action-predicate relatives (S101–S103): the gap-and-head structure
      is unchanged; only the predicate type differs. Stative modifying clauses are confirmed
      possible. (This secondary form is noted here rather than given its own sentence because
      S107 already tests the stative prop type through the epistemic frame, and the relative
      form is compositionally derived with no additional findings.)

<span id="S163"></span>
**S163**
`lo-li  vo`
*The person is [socially] valued.*

!!! annotation "Notes"
    - **Type 1 predication** (`lo-X  Q`): patient-slot subject, quality predicate. X occupies
      state Q as a current condition. The claim is contingent — social recognition can change.
    - **Contrastive Pair 3 (with S162):** Same noun (`li` = person), same quality (`vo` = value).
      Different slot → different claims:
      - `la-li  vo` → person *holds* worth — intrinsic, structural property of being a person
      - `lo-li  vo` → person *is in* a valued state — contingent social esteem
    - The distinction maps onto a meaningful philosophical line: intrinsic worth cannot be
      revoked by social consensus; social esteem can. Tonesu captures this via the `la`/`lo`
      slot distinction rather than with separate vocabulary.
    - **P-GP-001 resolution criterion (three contrastive pairs) now met.**
      Pair 1: `lo-X  Q` (C002 A3 `lo-si-mu  ru`) vs `la-X  Q` (S030 `la-to-su-mu  vo`)
      — pattern introduced.
      Pair 2: `lo` compound (S033 `lo-pa  ha-vo`) vs `la` compound (S034 `la-ra-ki-mu  ha-fe`)
      — compound predicates in both positions.
      Pair 3: S162 vs S163 — minimal pair, same noun and quality, different slot, different claim.

<span id="S190"></span>
**S190**
`la-mu  lo-si  se  no  lo-to`
*The machine detected the signal, not the pattern.*

!!! annotation "Notes"
    - **Second corpus attestation of `no` as intra-clause contrast coordinator.** First use: S090 (`lo-to-re-su  be  no  lo-wi-to` = "followed the doctrine, not the plan"). Here: `lo-si  se  no  lo-to` = "perceived the signal, not the pattern." Different predicate (`se` vs `be`), different domain (machine perception vs. mission instruction), parallel structure (patient contrast in both).
    - `no` in the contrast coordinator position negates only the following constituent (`lo-to`), not the predicate. The machine did perceive; what it perceived was `lo-si`, not `lo-to`. The predicate `se` is unaffected.
    - **Patient contrast:** `lo-si` (raw signal / signal data) vs. `lo-to` (conceptual pattern). In the Tonesu epistemic hierarchy, machines register signal-level data (`si`); only persons or sufficiently organized systems extract conceptual patterns (`to`). This sentence embodies that ceiling not as a doctrinal statement but as a bare perceptual report.
    - **Bare `se` (no epistemic frame):** The machine's perception is reported without an outer `la-mu  se  [prop]` frame. That frame would attribute a personal epistemic stance to the machine, which doesn't apply. Inanimate agents simply perceive; they don't hold epistemic positions. Verb as bare predicate; machine as grammatical agent.
    - With two attestations (S090, S190), the `no` contrast coordinator is ready to formalize. Structure confirmed: `[established constituent]  no  [rejected alternative]`, with both constituents grammatically parallel (`lo-` patients in both cases so far).
    
    **Verdict S190: clean.** `no` as contrast coordinator between parallel `lo-` patients is stable with `se` predicate. Generalizes beyond `be`. Ready to add as Level 4 in § Negation.

<span id="S191"></span>
**S191**
`la-si-su  ko  [la-ra-ki-li  se  lo-pa-ra]`
*The archive holds: the pilot perceived the field.*

!!! annotation "Notes"
    - **Second corpus attestation of `ko` with a clausal complement.** First: C005 A2 (`la-to-re-su  ko  [lo-mu  zo-to]` — doctrine contains propositional belief). Here: `la-si-su  ko  [la-ra-ki-li  se  lo-pa-ra]` — archive contains propositional observation record. Different container type (`si-su` archive vs. `to-re-su` doctrine), different propositional content (perceptual report vs. doctrinal claim), parallel grammatical structure.
    - The bracketed clause `[la-ra-ki-li  se  lo-pa-ra]` is a full propositional complement: agent (`la-ra-ki-li`), predicate (`se`), patient (`lo-pa-ra`). The archive contains this proposition as an entry — not the pilot, not the field, but the propositional record of the perception event.
    - **Container semantics confirm the extension principle:** `ko` asserts a containment relation between a container and its contents. The container type determines what register of contents makes sense:
      - Physical container (`ko-mu`) → physical objects
      - Archive (`si-su`) → records and logged propositions
      - Doctrine (`to-re-su`) → doctrinal claims
      In all three cases, `ko` is the same structural predicate. No special form is needed for propositional complements.
    - `la-si-su  ko  lo-si-mu` (S070) was the nominal-patient form for the same archive. That sentence says "the archive holds records" (a type of nominal contents). This sentence says "the archive holds that X happened" (a specific propositional entry). The nominal form describes the archive's character; the propositional form reports a specific log entry. Both are valid.
    - With two domain-varied attestations (C005 A2, S191), the `ko`-clausal complement pattern is ready to formalize.
    
    **Verdict S191: clean.** `la-si-su  ko  [embedded-prop]` follows the same `la-X  ko  Y` pattern with full clause as Y. No strain. Generalizes from doctrine to archive. Rule may now be written.

<span id="S192"></span>
**S192**
`la-yu  lo-to-su  be  ta-ti-be  lo-se-ka`
*The team consolidated their knowledge after the inspection.*

!!! annotation "Notes"
    - **Mirror of S092's event-anchor construction.** S092: `ta-ti-de  lo-ka-wi-de` = "before the mission departure" (`ti-de` = past/prior → before). S192: `ta-ti-be  lo-se-ka` = "after the inspection" (`ti-be` = future/following → after). Both use `ta  ti-[dir]  lo-[event]` with a `lo-`-marked event as the temporal anchor. Different domain (mission preparation vs. maintenance/inspection cycle), different directional compound (`ti-de` vs `ti-be`).
    - **`ta-ti-de  lo-X` = before X; `ta-ti-be  lo-X` = after X.** The directional component of the time compound (`de` = decay/prior, `be` = growth/following) sets the relative position; the `lo-[event]` bracket provides the anchor event. The structure is compositionally transparent: "at the [prior/following] time [of] [event]."
    - **`be` as matrix predicate:** `lo-to-su  be` = "knowledge grows" = they consolidated their knowledge. The group's organized understanding expanded as a result of the inspection. Same `be` as all growth predicates.
    - **`se-ka`** (W034, perceptual-agent/examination process) used as the anchor event. The inspection is the event they are temporalizing against. `lo-se-ka` = patient:inspection — the examination in its nominal role as a temporal anchor.
    - The two examples together confirm the pair: `ta-ti-de  lo-X` / `ta-ti-be  lo-X` = before-X / after-X. The construction is general: any `lo-[event]` noun phrase can serve as the anchor.
    
    **Verdict S192: clean.** `ta-ti-be  lo-[event]` = "after [event]" works identically to S092's `ta-ti-de  lo-[event]` = "before [event]." Event-anchor temporal construction confirmed as a general pattern. Ready to add rule to grammar.md.

<span id="S193"></span>
**S193**
`go [lo-zo-su  ne  lo-zo-su]  du [lo-zo-su  be]  du [lo-zo-su  be]`
*Because living-system A is in relation with living-system B, A grows and B grows.*

!!! annotation "Notes"
    - **Second corpus attestation for P-PR-002.** S189 demonstrated the gap in physics (`lo-ra-su  ne  lo-ra-su`, force-systems). S193 repeats the same construction in biology (`lo-zo-su  ne  lo-zo-su`, living-systems in mutualistic coupling). Two domain-distinct sentences, same structural failure.
    - **`zo-su`** = living-system / organized organism. Compositional parallel to `ra-su` (force-system, used in S189): `zo` (living thing) + `su` (organized structure) = organism understood as an organized biological system. Not separately registered; compositionally transparent.
    - **The gap is identical to S189:** (1) Double `du` forces sequential reading — living-system A grows first, then living-system B — but mutualistic symbiosis is a continuous coupled exchange with no sequencing between the two growth events. (2) `ne` describes the static relation enabling the coupling; it does not encode the mutual-transformation event itself. The language approximates the outcome (both grow because they are in relation) but cannot say the coupling *is* the event in which both transform simultaneously.
    - **Why `go...ne...du...du` is the best available:** A single `du` frame cannot take two agent-predicate pairs without coordinate structure. Using `ne` as inner coordinator (`du [lo-zo-su  be  ne  lo-zo-su  be]`) would read `ne` as a static copula between two growth-states, not as simultaneous mutual growth. The double-`du` chain is the least-distorting approximation available.
    - **Biology removes the physics-abstraction objection.** One might argue that physical simultaneity is a limiting edge case that natural language need not cover. Mutualistic symbiosis is a macroscopic, everyday-scale fact about organisms. If the language cannot express it without sequentiality distortion, the gap is not domain-specific.
    - The `go...ne...du...du` chain is grammatically well-formed. The insufficiency is ontological, not grammatical — the same conclusion as S189.
    - **Retroactive note (March 2026 — `zi` admitted as primitive 34):** The intended concept is now expressible as `lo-zo-su  zi-zo  lo-zo-su` — "living-system A and living-system B undergo mutual biological transformation." `zi-zo` (W106, proposed) is the compressed correct form. S193 is retained as the gap record.
    
    **Verdict S193: gap confirmed (2/3).** The P-PR-002 simultaneous-mutual-transformation gap is present in both physics (S189) and biology (S193). One further domain-varied wrong-reading is needed to reach the three-attestation threshold. Social domain (negotiation / mutual exchange) is the remaining candidate.

<span id="S194"></span>
**S194**
`go [la-li  ne  la-li]  du [la-li  wi-to-ki]  du [la-li  wi-to-ki]`
*Because delegate A is in relation with delegate B, A shifts position and B shifts position.*

!!! annotation "Notes"
    - **Third corpus attestation for P-PR-002.** S189: physics/force-systems. S193: biology/mutualistic symbiosis. S194: social/negotiation. Three-wrong-reading threshold is reached.
    - **`wi-to-ki`:** `wi` (intention) + `to` (conceptual pattern) + `ki` (inchoative) = entering a new intentional-conceptual configuration = revising one's stance. Head-final: the change-event (`ki`) in the domain of intentional-pattern (`wi-to`). Compositionally transparent; no registration needed for the test.
    - **Wrong reading (primary decomposition):** Double `du` forces sequencing — delegate A revises first, then delegate B revises. But negotiation revision is a coupled simultaneous exchange: both parties update their positions *at the exchange moment*, which is a single event, not two sequential ones. The language has no way to mark the two outcomes as concurrent.
    - **Alternative decompositions tested:**
      - *Two causal chains* (`go [la-li wi-to] du [la-li wi-to-ki]. go [la-li wi-to] du [la-li wi-to-ki].`): Loses the coupling entirely. Two independent internal revisions; the mutual-response is gone. Wrong reading: one event becomes two separate events.
      - *Relational + causal hybrid* (`la-li  ne  la-li  go  wi-to-ki`): Which party changes? Both changing is lost. Wrong reading: mutual change becomes undifferentiated one-way causation from the relation.
      - *`ne` between shift-events* (`du [la-li  wi-to-ki  ne  la-li  wi-to-ki]`): `ne` between two events reads as a static relation between two change-states, not as the assertion of their simultaneity. Wrong reading: interaction becomes static relation at the event-result level.
    - **Repair test:** `ne-ki` (relation-change) = the relation itself shifts — not both parties. `wi-to-ne` = a static shared-stance state, not the dynamic revision event. No compound of existing primitives asserts "these two events are simultaneous and mutually constitutive" without that compound being exactly the new concept needed. Repair fails.
    - **The social domain removes the natural-law objection.** Physics and biology involve simultaneous coupling as a matter of natural law (field interactions, metabolic mutualism). Negotiation is chosen, deliberate, one of the paradigm cases of intentional mutual transformation. If the gap persists here, it is not an edge case of physics formalisms — it is a structural gap in the language's treatment of coupled events generally.
    - Same `go...ne...du...du` canonical structure as S189 and S193; results are directly comparable. The wrong reading is the same in all three domains.
    - **Retroactive note (March 2026 — `zi` admitted as primitive 34):** The intended concept is now expressible as `la-li  zi-ka  lo-li` — "the delegates engage in mutual exchange / transaction." `zi-ka` (W105, proposed) is the compressed correct form. S194 is retained as the gap record showing why `zi` was needed.
    
    **Verdict S194: gap confirmed (3/3). Three-attestation threshold reached.** The P-PR-002 simultaneous-mutual-transformation gap is persistent across physics, biology, and social domains. All alternative decompositions fail. Repair by compounding fails. A primitive slot evaluation is now triggered. See open-questions.md for the updated entry.

<span id="S365"></span>
**S365**
`(la-ze  lo-wi-fe  be-si)  ,  du  la-ze  lo-wi-fe-no-fe  wi`
*(She reportedly said: let rules increase.) — Therefore she intends            unlimited-governance [rules-without-boundary].*

!!! annotation "Notes"
    - `(la-ze  lo-wi-fe  be-si)` = the evidential frame wraps the source's actual reported position. `be-si` = growth-signal = signaling in favor of increase. The `()` marks this as reported — the speaker is not personally asserting this as the source's exact words.
    - `wi-fe-no-fe` = rules-without-boundary = `wi-fe` (W100) + `no-fe` (without limit). Default right-branching: `wi` modifies [`fe-no-fe`] = will applied to [boundary-without-limit] = unlimited imposition = totalitarianism. This bare-asserted conclusion is outside `()` — the speaker presents it without reservation.
    - **Grammar doing the work:** the real position is `()`-framed; the distortion is bare-asserted. In Tonesu, anything outside `()` claims first-person certainty. The structural contrast — `(reported premise)  ,  du  [bare confident conclusion]` — makes the gap visible: the `du` (result/therefore) asserts the conclusion follows directly from what was only a reported claim.
    - Corrected form: `(la-ze  lo-wi-fe  be-si)  ,  (du  la-ze  lo-wi-fe-no-fe  wi)` — place both premise and conclusion inside `()`. Both are reported/uncertain. The result is the weaker, epistemically honest version.

<span id="S439"></span>
**S439**
`to-su  helm  ra`
Written: `tosu helm ra`
*Knowledge is power." (Francis Bacon, attributed)*

!!! annotation "Notes"
    `to-su` (W030) = knowledge-system / organized knowledge. `ra` = force/energy/power (primitive). `helm` (G011) = functional equivalence predicate: X is functionally understood as Y. Bacon's claim is pragmatic — organized knowledge *functions as* power, not that it metaphysically *is* power (`helms`) or merely *has* the property of power (`ne to-su ra`). The `helm` reading is precise: in the domain of human affairs, knowledge behaves as force.

<span id="S440"></span>
**S440**
`ti  helm  nu-vo`
Written: `ti helm nuvo`
*Time is money." (Benjamin Franklin, attributed)*

!!! annotation "Notes"
    `ti` = time (primitive). `nu-vo` = quantity-value = measurable worth / counted resource (compositional; unregistered; `nu` = quantity + `vo` = value). `helm` = is functionally understood as. The claim is economic: time, in productive contexts, *functions as* a countable valuable resource. Not a definitional identity (`helms`) nor a property attribution (`ne`). Contrast with S439: both S439–S440 are `helm` pragmatic/cultural assertions.

<span id="S441"></span>
**S441**
`go-no-fe  helm  de`
Written: `gonofe helm de`
*God is dead." (Friedrich Nietzsche, *Die fröhliche Wissenschaft* §125, 1882)*

!!! annotation "Notes"
    `go-no-fe` = necessary being (God; `go` + `no-fe` = origin without limiting boundary). `de` = decay/dissolution (primitive). `helm` = is culturally/functionally understood as. Nietzsche's claim is a cultural observation, not a metaphysical fact: the concept of God has functionally decayed in the modern imagination. `helm` is precisely right — `go-no-fe helms de` would be a logical contradiction (a necessary being is by definition incapable of dissolution). `helm` admits the tension: in the cultural-functional register, the necessary being is *understood as* dissolved. The force of the provocation is in the gap between `helm` and `helms`. Contrast immediately with S442.

<span id="S442"></span>
**S442**
`go-no-fe  helms  vo`
Written: `gonofe helms vo`
*God is love." (1 John 4:8)*

!!! annotation "Notes"
    `vo` = value/quality/worth (primitive; broadest reading = unconditional positive regard / *agape*). `helms` (G012) = is by definition. This is a theological essence claim: what the necessary being *is*, not merely what it does or how it functions. Contrast with S441: same subject (`go-no-fe`), different operator, different predicate — `helm de` vs `helms vo` — encodes Nietzsche vs John at the level of the identity predicate itself. Resolves the identity-copula ambiguity raised in GAP-LSP-001 (see LSP-001 Batch Summary, and S431/S436): `ne` would attribute love as a property; `helms` asserts it as constitutive essence. The three-way scale illustrated across S441–S442: `ne` (property) < `helm` (functional) < `helms` (definitional).

<span id="S443"></span>
**S443**
`zo-li  helms  to-zo`
Written: `zoli helms tozo`
*Man is a rational animal." (Aristotle, *Nicomachean Ethics* / *Politics*)*

!!! annotation "Notes"
    `zo-li` (W148) = living-agent = human person. `to-zo` = knowledge-living-being = a living thing defined by its knowledge-capacity = rational animal (compositional; unregistered: `to` modifier + `zo` head). `helms` = is by definition. Aristotle's core definition: being human *is* being a knowledge-structured living thing. Note compound polarity: `zo-to` (W068) = soul (living → knowledge: the knowledge-aspect of a living being); `to-zo` = rational animal (knowledge → living: a life-form categorized by its knowledge-capacity). The reversal encodes a different emphasis: soul is the knowledge-side of life; rational animal is the knowledge-*categorized* kind of creature.

<span id="S444"></span>
**S444**
`la-mi  to  go  la-mi  pa`
Written: `lami to go lami pa`
*I think, therefore I am." (René Descartes, *Discours de la méthode*, 1637)*

!!! annotation "Notes"
    `la-mi` = I (first-person agent). `to` = model/think (primitive, intransitive). `go` = cause/origin particle (here: causal connective = "therefore"). `pa` = place/existence (place-occupation as proxy for existence). Structure: [premise: `la-mi to`] `go` [conclusion: `la-mi pa`] = "I think, therefore I exist." Deliberately uses `go` (causal deduction) rather than `helm`/`helms`; the Cogito is *not* an identity claim but a logical inference from a premise to a conclusion. Descartes does not say "thinking *is* existing" but "from the fact that I think, existence follows." Structural contrast with S442–S443: `helms` asserts identity; `go` deduces consequence.

<span id="S445"></span>
**S445**
`pu-to-su  ne  ven  du-to`
Written: `putosu ne ven duto`
*All models are approximately correct." (George E. P. Box, paraphrase)*

!!! annotation "Notes"
    `pu-to-su` = all knowledge-systems / all models (plural prefix `pu-` + `to-su` W030). `ne` = property copula. `ven` (G010) = approximately (spoken/written form of `~`; pre-positional hedge). `du-to` = result-of-knowledge = the successful outcome of a modelling process = correct/accurate (compositional; unregistered: `du` = result/effect + `to` = pattern/knowledge). `ven du-to` = approximately correct. Forms a linked pair with S446: see that entry for the epistemological point.

<span id="S446"></span>
**S446**
`pu-to-su  ne  ven  no-du-to`
Written: `putosu ne ven noduto`
*All models are approximately wrong." (George E. P. Box, complementary reading)*

!!! annotation "Notes"
    Complement of S445. `no-du-to` = not-result-of-knowledge = incorrect (negated form; `no-` prefix + `du-to`). `ven no-du-to` = approximately wrong. S445 and S446 are both true of the same referent (`pu-to-su`), and this is not a contradiction: `ven X` and `ven no-X` co-hold when the subject is near the precision boundary — which is the condition of every finite model. `ven` is symmetric: a model that is `ven du-to` is the same model that is `ven no-du-to`. Tonesu's approximation system encodes this more faithfully than natural language: English "roughly correct" and "roughly wrong" feel contradictory; `ven du-to` and `ven no-du-to` are formally symmetric hedges. Box's full aphorism: "All models are wrong, but some are useful." A third sentence completing the aphorism — `ta pu-to-su-va ne vo` (and some models have value/utility) — is deferred.

---

*Generated from [`registry/entries.yaml`](https://github.com/Arakendo/Tonesu/blob/main/registry/entries.yaml).*