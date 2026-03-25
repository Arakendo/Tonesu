# Stage 7 — Production

The previous six stages built your analytic vocabulary — you can read a Tonesu
sentence and account for every piece. This stage goes the other direction: from
English prompt to Tonesu output, with a justification for each structural choice.
Four skills matter: assembling the sentence frame correctly, choosing between formal
and colloquial register, picking a translation reading when more than one is valid,
and handling the cases where Tonesu simply has no direct equivalent.

---

## Cluster 1 — The construction sequence

There is a reliable order for building a Tonesu sentence from an English one.
Work through it before reaching for particles.

**Step 1: Identify who acts and who is acted upon.**

In English, word order does this job. In Tonesu, the prefixes `la-` (agent) and
`lo-` (patient) do it — word order is free in principle, but the prefixes are
obligatory.

**Step 2: Find or build the verb compound.**

The verb is a root or compound. Use the primitives registry first; if no single root
fits, build a compound from modifier + head (modifier precedes head, right-branching).

**Step 3: Check for epistemics and scope.**

Does the verb need a modal (`se`/`si`/`to`)? Does the agent NP want a scope prefix
(`a-`, `i-`, `u-`, `o-`, `e-`)? Add only what the meaning requires.

**Step 4: Assemble the frame.**

```
la-{agent}   {verb-compound}   lo-{patient}
```

Then add any peripheral particles: `go` (causal ground), `du` (result), `ne`
(property), `ta-` (temporal frame).

---

### Worked example: "The device transforms the signal"

```
Step 1:  agent = the device (to-ki-mu)
         patient = the signal (si)

Step 2:  "transforms" = ki  (change / transform, primitive root)

Step 3:  no modal needed; no scope prefix

Step 4:  la-to-ki-mu   ki   lo-si
```

**Written:** `latokimu ki losi`

Now flip the roles: "The signal transforms the device."

```
la-si   ki   lo-to-ki-mu
```

**Written:** `lasi ki lotokimu`

Same roots, same verb — but `la-` and `lo-` swap. The written forms
`latokimu ki losi` and `lasi ki lotokimu` are structurally unambiguous. English
word order and Tonesu prefix assignment do the same semantic work; the difference
is that in Tonesu the assignment is phonologically visible regardless of where
in the clause the NPs appear.

---

### A more complex case: epistemic frame

"I am assessing that the model is incomplete."

```
Step 1:  agent = mi (speaker); the embedded claim has no separate surface agent

Step 2:  verb = si (hypothesis/assessment), with embedded clause as patient

Step 3:  modal = si (already the verb); embedded clause = lo-to-su no-ru
         (knowledge-system, not-complete)

Step 4:  la-mi   si   {lo-to-su   no-ru}
```

**Written:** `lami si {lotosu noru}`

The curly braces `{}` are structural scope brackets marking the embedded clause
boundary. In casual speech the pause does that work; in writing `{}` (or the spoken
forms `suld`/`sulds`) makes the scope visible.

---

!!! question "Exercise 1 — *Build the frame*"
    "The computer transforms the signal." Which Tonesu form is correct?

    <div class="tn-learn-mcq"
         data-answer="b"
         data-ok="Correct — la-to-ki-mu ki lo-si. The computer (to-ki-mu) is the agent (la-); the signal (si) is the patient (lo-). ki = transform ✓"
         data-nok="Check which NP is agent and which is patient — la- marks the actor, lo- marks the one acted upon. The computer acts on the signal, not the reverse."
         data-options='[{"id":"a","text":"`la-si  ki  lo-to-ki-mu` — signal acts on the computer"},{"id":"b","text":"`la-to-ki-mu  ki  lo-si` — computer acts on the signal"},{"id":"c","text":"`to-ki-mu  ne  si` — computer has the property of signal"}]'>
    </div>

??? success "Explanation"
    `ne` (option C) is the property copula — it attributes a state or quality, not a
    transformation. `ki` is the right verb for "transform / change." Then `la-`
    marks who acts: `la-to-ki-mu` = the computer as agent. `lo-si` = the signal
    as patient. The swap in option A reverses the semantic direction completely —
    `la-si ki lo-to-ki-mu` says the signal is the actor and the computer is what
    gets changed.

---

## Cluster 2 — Register: formal and colloquial

Tonesu has two registers. The **formal register** uses full compound forms as registered
and is always correct in writing. The **colloquial register** uses contracted stub-forms in
casual spoken use.

### The contraction rule

A formal compound of three or more morphemes **may** contract to a shorter spoken
form when:

1. The formal compound is at least three morphemes long.
2. The stub form is unambiguous within its discourse domain.
3. The formal compound remains the canonical written form.

Two-morpheme compounds sit below the threshold — they cannot contract.

### Registered examples

| Formal | Morphemes | Stub | CLQ entry | Mechanism |
|--------|-----------|------|-----------|-----------|
| `zo-se-so-li` | 4 | `zol` | CLQ-001a | drop middle `se-so`; keep head `li` as coda |
| `zo-se-so-fe` | 4 | `zof` | CLQ-001b | symmetric pair; `fe` as coda |
| `zo-se-so-di` | 4 | `zod` | CLQ-002a | `di` as coda |
| `zo-su` | 2 | `zos` | CLQ-003a | two-root base; written solid = stub |

Note `zos`: the formal compound `zo-su` is two morphemes, but the written solid form
`zosu` is itself short enough to serve as the stub. This is a different compression
depth — the threshold still applies, but the mechanism is surface shortness, not
middle-morpheme deletion.

### What is not contracted

- **Two-morpheme compounds** below threshold (`to-li`, `vo-li`, `ra-ki`) never contract
  to a CVC stub because the rule requires 3+.
- **Unregistered stubs**: you may not freely generate stubs from long compounds. If
  no CLQ entry exists, the formal form is the colloquial form. `to-ki-mu` (computer,
  three morphemes) has no registered CLQ entry; it remains `tokimu` in all registers.
- **Technical contexts**: even if a CLQ entry exists, prefer the formal form in
  written, instructional, or precise contexts. `zol` is fine in a conversation about
  your neighbour's dog; `zo-se-so-li` is right in a zoology note.

### When to choose colloquial

Use the stub when: speaking casually, the discourse domain is clear (so the stub is
unambiguous), and the compound has an active CLQ entry. Use the formal form when:
writing, in technical or scientific contexts, or whenever you want to be maximally
unambiguous.

---

!!! question "Exercise 2 — *Contraction threshold*"
    Which of these compounds can currently be used in its registered colloquial
    stub form?

    <div class="tn-learn-mcq"
         data-answer="c"
         data-ok="Correct — zo-se-so-li → zol (CLQ-001a). Four morphemes, registered active stub ✓"
         data-nok="Check how many morphemes each compound has. The contraction rule requires 3+, and a stub must be actively registered."
         data-options='[{"id":"a","text":"`to-li` — knowledge-person (2 morphemes)"},{"id":"b","text":"`to-ki-mu` — computer (3 morphemes, no CLQ entry registered)"},{"id":"c","text":"`zo-se-so-li` — canid class (4 morphemes, CLQ-001a: zol)"}]'>
    </div>

??? success "Explanation"
    `to-li` (option A) is two morphemes — below the contraction threshold. It has no
    stub and needs none; `toli` is already minimal.

    `to-ki-mu` (option B) is three morphemes and *meets* the length threshold, but no
    CLQ entry has been registered for it. You may not invent an unregistered stub.
    The formal form `tokimu` is the correct colloquial form until a CLQ entry exists.

    `zo-se-so-li` → `zol` (option C) is the live case: four morphemes, middle-morpheme
    deletion, active entry CLQ-001a. In casual spoken use, `zol` is the registered
    form. In writing or technical contexts, `zo-se-so-li` remains canonical.

---

## Cluster 3 — Translation choices

Most English sentences have exactly one natural Tonesu rendering. Some have two,
each structurally valid, because the English is genuinely ambiguous between readings.
When that happens, producing Tonesu forces you to make a commitment the English
source deferred.

### Hamlet: universal vs personal

Shakespeare's opening — "To be, or not to be, that is the question" — admits two
valid Tonesu renderings.

**S462 — universal reading:**

```
pa / no-pa : ne to-si
```

**Written:** `pa / nopa : ne tosi`

`pa` and `no-pa` are topicalized as abstract concepts — existence and non-existence
as a category pair, not attached to any agent. The question is: is this binary *the*
question? A philosophical claim.

**S463 — personal reading:**

```
la-mi pa / la-mi no-pa : ne to-si
```

**Written:** `lami pa / lami nopa : ne tosi`

`la-mi` appears on both sides of the `/` parallel — Hamlet's own existence is
explicitly the subject. This is the intimate reading: not "is existence a question"
but "is *my* existence the question."

Both are correct Tonesu grammar. The choice is not grammatical — it is interpretive.
Producing S462 is a claim about the philosophical register of the soliloquy. Producing
S463 is a claim about its personal register. The structure enacts an interpretive
position you now have to be able to defend.

### Justifying the choice

Translation justification has a fixed format: which reading did you choose, which
structural feature encodes that reading, and what is lost if you use the other.

For S463: *Personal reading: `la-mi` explicit on both clauses. This encodes Hamlet's
particular existential stake as the subject. What is lost: the universal/philosophical
resonance of S462 — the reading on which Hamlet is voicing a general question about
the nature of existence, not just his own survival.*

A complete translation record documents both readings and notes the choice.

---

!!! question "Exercise 3 — *Existential predicate*"
    "The Word existed at the beginning." Complete: `la-to  ___  ta-go-ti` (S447 form).
    Which predicate asserts existence?

    <div class="tn-learn-picker"
         data-template="la-to  ___  ta-go-ti"
         data-answer="pa"
         data-mode="form"
         data-ok="pa — presence / existence. la-to pa = the Word existed / was-located. ta-go-ti = at-origin-time. Pure existential claim ✓"
         data-nok="ne attributes a property (la-to ne X = the Word has property X). go asserts causation. For bare existence — being present at a time — use pa."
         data-items='[{"form":"pa","gloss":"presence / existence / is-located"},{"form":"ne","gloss":"property copula — attributes a quality"},{"form":"go","gloss":"causal / origin particle"}]'>
    </div>

??? success "Explanation"
    `pa` = presence / spatial existence / being-located. `la-to pa` = the Word existed
    — it was present at the origin-time. This is the existential predication from
    John 1:1a (S447), rendered structurally separate from the relational (`ne ro-X`)
    and predicative (`ne X`) uses of "was" in the same verse.

    `ne` (option 2) would need a complement: `la-to ne go-no-fe` = the Word has the
    property of necessary-being. That is clause C of John 1:1 (S449), not clause A.
    `go` asserts causation — `la-to go la-su` = the Word caused the structure — a
    different claim entirely.

    The three senses of "was" in John 1:1 — existential, relational, predicative —
    each get a structurally distinct Tonesu form. This is one of the test cases that
    shows why Tonesu's three-way copula system (`pa` / `ne ro-X` / `ne X`) carries
    real semantic load.

---

## Cluster 4 — Gaps and workarounds

Every language has concepts it cannot express directly. Tonesu is no exception. When
you encounter a gap, there are two patterns: **resolved** (a structural equivalent
exists, possibly at a different level) and **documented workaround** (no equivalent;
the nearest available tool is used, and the loss is recorded).

### Pattern 1: Resolved gap

**The comparative.** English "nobler" embeds a degree comparison. Tonesu has no
comparative particle in the primitive set — but grammar §Comparison establishes
`nu-be` / `nu-no` for "more [quality] than" / "less [quality] than":

```
lo-A  {quality}  nu-be  lo-B     →   A has more {quality} than B
lo-A  {quality}  nu-no  lo-B     →   A has less {quality} than B
```

The Hamlet soliloquy contains "Whether 'tis nobler in the mind to suffer..." — a degree
comparison. This could be rendered as:

```
de lo-no-ko-ra  vo  nu-be  ka-ra lo-de-no-fe
```

*Endurance has more worth than taking arms.* (alternative rendering of S464)

The gap in the primitive set is present, but the grammar supplies the tool. This is
a resolved gap: find the structural equivalent in the rule system rather than the
lexicon.

### Pattern 2: Documented workaround

**The possibility modal.** Classical Chinese 可 (kě) = can / possible. Laozi's opening
line says "the Way that *can be* spoken is not the eternal Way" — the potentiality
is philosophically essential. Tonesu has no possibility modal in its primitive set.

**Available workaround:** use the conditional frame `go {…}` (causal/conditional),
which expresses "when / given that":

```
go {su-si  lo-su}  ,  ze  no-helm  su-no-fe
```

*When the Way is named — it does not function as the boundless Way.*  (S474)

**What is lost:** the potentiality/actuality distinction. The Chinese encodes "any Way
that *could* be named." The Tonesu renders "any Way that *is* named." The philosophical
scope is different: Laozi's claim covers hypothetical namings; S474 covers actual ones.
The workaround preserves the central argument (naming limits; the boundless escapes
naming) but shifts emphasis from potential to actual.

This loss is documented in the translation file as **GAP-TAO-001** (no possibility
modal) and **GAP-TAO-002** (Chinese pun on 道 as noun and verb, structurally irreproducible).
Recording the gap is part of the translation record — do not suppress it.

### The discipline

A gap record has the form: *(1) what the source requires, (2) why Tonesu lacks it
directly, (3) which tool is used, (4) what the tool cannot capture.* A translation
without gap records is either very lucky or dishonest.

---

!!! question "Exercise 4 — *Two readings, both valid*"
    `pa / no-pa : ne to-si` and `la-mi pa / la-mi no-pa : ne to-si` are two Tonesu
    renderings of the same English source. Which statement is correct?

    <div class="tn-learn-mcq"
         data-answer="b"
         data-ok="Correct — both are valid. The structural difference (agentless vs la-mi explicit) encodes a genuine interpretive difference (universal vs personal reading). Neither is a grammatical error ✓"
         data-nok="Both forms are grammatically well-formed. The difference is interpretive, not corrective — choosing between them is a translation decision, not a repair."
         data-options='[{"id":"a","text":"The first is incomplete — it is missing its agent and is therefore malformed"},{"id":"b","text":"Both are valid. The agentless form is the universal reading; la-mi explicit is the personal reading. The choice is interpretive"},{"id":"c","text":"The second is redundant — la-mi need only appear once, on the first clause of the parallel"}]'>
    </div>

??? success "Explanation"
    Option A is wrong: `pa / no-pa : ne to-si` is grammatically complete. `pa` and
    `no-pa` are topicalized as abstract concepts — no agent is required when the
    predicate is being discussed *as a concept*, not predicated of a particular entity.

    Option C is technically true as a grammar fact — under Grammar §Ellipsis Pattern 3,
    `la-mi` on the first clause of a `/` parallel is recoverable across both branches,
    so the double form is optional. But that does not make the double form wrong; it
    makes it the *conservative* choice when clarity is valuable.

    Option B is the full picture: the two forms encode two genuinely different readings.
    Choosing S462 commits you to the philosophical register; choosing S463 commits you
    to the personal one. This is what production means in Tonesu — a structural choice
    is not stylistic noise, it is semantic content.

---

## Summary: the production checklist

| Step | Question | Tool |
|------|----------|------|
| Who acts? | Agent identification | `la-` prefix |
| Who is acted upon? | Patient identification | `lo-` prefix |
| What is the action? | Verb compound | Primitives + modifier-head compounding |
| What level of confidence? | Epistemic | `se / si / to` + scope of claim |
| Collective, universal, particular? | Scope | `a- / i- / u- / o- / e-` prefixes |
| Written or spoken? | Register | Formal always correct; CLQ stubs when registered |
| One reading or several? | Interpretation | Commit and justify; record alternatives |
| No direct equivalent? | Gap | Find nearest tool; document what is lost |

---

## Next

Stage 7 is the end of the structured curriculum. From here, the learning is in the
corpus itself.

The [sentence corpus](../../tonesu/corpus/index.md) contains hundreds of annotated
sentences organized by batch — each batch tests a specific grammatical or lexical
question, and the annotations explain every structural decision.

The [translation files](../../tonesu/corpus/translations/index.md) are full
production records: English source, line-by-line Tonesu, parse notes, gap records,
and colloquial register analysis. They are the closest thing Tonesu has to a
translation workshop.

The [registry](../../tonesu/registry/derived/index.md) is where words live —
every derived compound with its W-number, first attestation, and status code.

And the [spec](../../tonesu/index.md) is the ground truth for any rule you want
to verify.
