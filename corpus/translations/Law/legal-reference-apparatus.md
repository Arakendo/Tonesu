---
batch_codes: [LRF]
---
# Legal Reference Apparatus Probe (LRF-001)

**Source:** Synthetic legal drafting stress test modeled on annotated statute and contract prose.
**Batch:** LRF-001
**Sentences:** S1274–S1278
**New entries:** none

---

## Source text

Representative annotated-clause target:

> Rule 1. No party may enter without recorded notice.
>
> Rule 2¹. After recorded notice and twenty-four hours, a party may enter only to inspect or repair.
>
> Note 1. The permission in Rule 2 is narrow; it is not a general liberty of entry.

This batch is not a translation of a single statute. It is a legal-register notation probe.

The question is narrower than USA Freedom Act-scale suffering:

- can legal Tonesu keep rule labels in ordinary line-level prose
- can superscript numerals function as compact note pointers
- do actual words want to migrate into super/subscript notation, or should they remain in the rule line and note body

The hypothesis tested here is strict: **numeric reference pointers are good legal apparatus; lexical words are not.**

---

## Vocabulary and notation framework

| Form | Reading | Notes |
|------|---------|-------|
| `wi-fe` | rule / mandate | W100; legal-rule anchor |
| `si-de` | recorded note / recorded notice | W098; reused here for document note as a recorded signal |
| `wi-fe-ka [clause]` | the clause is forbidden | deontic prohibition on a full clause |
| `no-wi-fe-ka [clause]` | the clause is permitted | permission as absence of prohibition |
| `bun mol nu re-ti` | twenty-four hours | existing exact-duration expression from LSE-001 |
| `[wi-fe na N]` | Rule N | body-line rule label |
| `[si-de na N]` | Note N | note label in body prose |
| `¹` | note-pointer numeral | written-only legal apparatus; not a spoken word |

---

## Sentence analyses

### S1274 — LRF-001-A: Rule 1 states the baseline prohibition

```
[wi-fe  na  1] : go {la-ze  no  si  lo-si-de},  wi-fe-ka  [la-ze  ki  lo-ko-pa]
```

**Written:** `[wife na 1] : go {laze no si loside}, wifeka [laze ki lokopa]`

**Natural reading:** Rule 1: if the party gives no recorded notice, entry into the room is forbidden.

**Notes:** The rule label stays in ordinary body prose as `[wi-fe na 1]`. Nothing needs to rise into superscript here because the label itself is part of the readable clause line, not side apparatus.

### S1275 — LRF-001-B: Rule 2 carries a superscript note pointer

```
[wi-fe  na  2]¹ : go {la-ze  si  lo-si-de ; bun mol  nu  re-ti  ki},  no-wi-fe-ka  [la-ze  ki  lo-ko-pa  wi {ka-se  lo-ko-pa / ka-de-be  lo-ko-pa}]
```

**Written:** `[wife na 2]¹ : go {laze si loside ; bun mol nu reti ki}, nowifeka [laze ki lokopa wi {kase lokopa / kadebe lokopa}]`

**Natural reading:** Rule 2: once the party gives recorded notice and twenty-four hours pass, entry into the room is permitted for inspection or repair. Superscript 1 points to a later note.

**Notes:** This is the core notation test. The rule name remains plain body text (`[wi-fe na 2]`). The superscript numeral is added as document apparatus, not as a clause word. That split is the point of the batch.

### S1276 — LRF-001-C: Note 1 states the narrow reading of Rule 2

```
[si-de  na  1] : lo-[wi-fe  na  2]  ne  no-wi-fe-ka  [la-ze  ki  lo-ko-pa  wi {ka-se  lo-ko-pa / ka-de-be  lo-ko-pa}]
```

**Written:** `[side na 1] : lo-[wife na 2] ne nowifeka [laze ki lokopa wi {kase lokopa / kadebe lokopa}]`

**Natural reading:** Note 1: Rule 2 is permission for a party to enter the room for inspection or repair.

**Notes:** The explanatory content stays in ordinary line-level prose. The batch deliberately does **not** try to raise a lexical note word such as "exception" or "inspection-only" into superscript. The numeral points; the words explain.

### S1277 — LRF-001-D: Note 1 is not Rule 2 itself

```
lo-[si-de  na  1]  no  helms  lo-[wi-fe  na  2]
```

**Written:** `lo-[side na 1] no helms lo-[wife na 2]`

**Natural reading:** Note 1 is not by definition Rule 2.

**Notes:** This is the cheap discriminating check for the notation hypothesis. If the note and the rule collapse into one written object, then superscript notation has eaten the clause. The batch rejects that collapse explicitly.

### S1278 — LRF-001-E: Superscript 1 represents Note 1

```
¹  helm  [si-de  na  1]
```

**Written:** `¹ helm [side na 1]`

**Natural reading:** Superscript 1 represents Note 1.

**Notes:** This is the positive verdict sentence. The numeral is useful as an indexical pointer in written legal apparatus. It is not useful as a carrier of lexical content.

---

## LRF-001 Batch Summary

| Entry | Tonesu | Written | Claim | Key feature |
|-------|--------|---------|-------|-------------|
| S1274 | `[wi-fe na 1] : go {la-ze no si lo-si-de}, wi-fe-ka [la-ze ki lo-ko-pa]` | `[wife na 1] : go {laze no si loside}, wifeka [laze ki lokopa]` | Rule 1 baseline prohibition | body-line rule label stays ordinary |
| S1275 | `[wi-fe na 2]¹ : go {la-ze si lo-si-de ; bun mol nu re-ti ki}, no-wi-fe-ka [la-ze ki lo-ko-pa wi {ka-se lo-ko-pa / ka-de-be lo-ko-pa}]` | `[wife na 2]¹ : go {laze si loside ; bun mol nu reti ki}, nowifeka [laze ki lokopa wi {kase lokopa / kadebe lokopa}]` | Rule 2 plus note pointer | superscript numeral as compact apparatus |
| S1276 | `[si-de na 1] : lo-[wi-fe na 2] ne no-wi-fe-ka [la-ze ki lo-ko-pa wi {ka-se lo-ko-pa / ka-de-be lo-ko-pa}]` | `[side na 1] : lo-[wife na 2] ne nowifeka [laze ki lokopa wi {kase lokopa / kadebe lokopa}]` | Note 1 gives the narrow reading | lexical explanation stays in line-level prose |
| S1277 | `lo-[si-de na 1] no helms lo-[wi-fe na 2]` | `lo-[side na 1] no helms lo-[wife na 2]` | note and rule are distinct objects | anti-collapse check |
| S1278 | `¹ helm [si-de na 1]` | `¹ helm [side na 1]` | superscript numeral maps to note 1 | pointer semantics stated directly |

**Key findings:**

1. Legal Tonesu wants **rule and note names in ordinary body prose**: `[wi-fe na 2]`, `[si-de na 1]`.
2. Superscript numerals work cleanly as **written-only reference apparatus**.
3. Actual lexical content does **not** want to move into super/subscript notation. Lexical super/subscript would blur clause content with metadata and would have no clean spoken recovery path.
4. This makes the next legal step clearer: USA Freedom Act-style cross-reference density should use numeric indices and plain body labels, not superscript words.

**Rejected notation direction:** lexical superscript/subscript strings such as `wifeˢᵘᵇ`, `ᵉxcept`, or similar raised word-fragments are dispreferred. They are harder to parse, harder to recover in speech, and less honest about the distinction between the rule line and the document apparatus.

---

## Colloquial Register Analysis

| Form used | CLQ entry | Colloquial form | Notes |
|-----------|-----------|-----------------|-------|
| `wi-fe` | none | — | W100, 2-root legal anchor; load-bearing |
| `si-de` | none | — | W098, 2-root — below threshold |
| `wi-fe-ka` | none | — | 3-root legal operator — semantically load-bearing |
| `no-wi-fe-ka` | none | — | negated legal operator — semantically load-bearing |
| `¹` | none | — | written-only reference apparatus; outside CLQ scope |

**Verdict:** irreducibly formal — the whole batch exists to keep document apparatus separate from clause content.

*CLQ entries registered from this batch: none.*