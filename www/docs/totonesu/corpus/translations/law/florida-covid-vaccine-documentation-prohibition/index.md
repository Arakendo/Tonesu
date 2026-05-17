---
title: "Florida COVID-19 Vaccine Documentation Prohibition"
batch_codes: [COV-STA-001]
source: "Florida Statute 381.00316 (2021) COVID-19 vaccine documentation"
sentences: S1310-S1314
w_entries: none
status: active
---

# Florida COVID-19 Vaccine Documentation Prohibition

## Source

Working from the 2021 Florida statute because it provides a clean state-level anti-mandate / preemption specimen with explicit scope and enforcement.

Operative lines used for this first state slice:

> "A business entity ... may not require patrons or customers to provide any documentation certifying COVID-19 vaccination or postinfection recovery to gain access to, entry upon, or service from the business operations in this state."

> "A governmental entity ... may not require persons to provide any documentation certifying COVID-19 vaccination or postinfection recovery to gain access to, entry upon, or service from the governmental entity's operations in this state."

> "An educational institution ... may not require students or residents to provide any documentation certifying COVID-19 vaccination or postinfection recovery for attendance or enrollment, or to gain access to, entry upon, or service from such educational institution in this state."

> "This subsection does not otherwise restrict businesses [or governmental entities or educational institutions] from instituting screening protocols consistent with authoritative or controlling government-issued guidance to protect public health."

> "The department may impose a fine not to exceed $5,000 per violation."

> "This section does not apply to a health care provider ..."

This batch is not trying to cover the entire later Florida anti-mandate landscape. It isolates the first strong state-level contrast the repo needs: can Tonesu show a statewide rule that forbids proof-of-status demands at the entry or service layer while still allowing narrower screening governance and backing the prohibition with administrative fines?

It tests:

- whether the state layer is best modeled as a public-law prohibition on proof-demand rather than as a positive medical directive
- whether the same anti-document rule can bind private business, government bodies, and educational institutions without collapsing those authority types together
- whether Florida's carveout for screening protocols shows that the statute targets certification demands more narrowly than it targets all public-health management
- whether the enforcement path is a fine for violation rather than a workplace protocol or inspection regime
- whether the comparison track now contains both a mandate-shaped federal specimen and an anti-mandate state specimen

## Vocabulary Framework

| Form | Reading | Notes |
|------|---------|-------|
| `ne-su` | organization / business-body | reused here for the private business layer |
| `li-pu-su` | governance-body / governmental entity | compositional first use; derivationally available from W036 notes |
| `to-ki-ne-su` | educational institution / schooling-body | compositional first use: knowledge-change organization |
| `si-ko-mu` | document / record | W067; used for certification demands |
| `su-ti lo-ka-fe-zo` | treatment-status / vaccination-status | reused from COV-FED-001 |
| `su-ti lo-de-be` | recovery-status | compositional: restored-state |
| `wi-fe-su` | rule / law / statutory norm-structure | W100 extension; the right source for statewide legal prohibition |
| `wi-fe-ka` | prohibited | used with a clausal argument to encode the banned demand |
| `wi-re-su si [ka-se lo-i-zo-li]` | screening protocol | recurring examination protocol, kept distinct from proof-of-status demand |
| `wi-fe'de` | penalty / sanction | W203; used for fine-based enforcement |

## Sentence Analyses

### S1310 - COV-STA-001-A: State law forbids businesses from demanding status proof for entry

**Notation:** `la-wi-fe-su ne wi-fe-ka [la-ne-su wi-ra [la-i-zo-li ka-si lo-si-ko-mu si [lo-i-zo-li su-ti lo-ka-fe-zo / lo-i-zo-li su-ti lo-de-be]] wi ki lo-ne-su]`

**Written:** `lawifesu ne wifeka [lanesu wira [laizoli kasi losikomu si [loizoli suti lokafezo / loizoli suti lodebe]] wi ki lonesu]`

**Natural reading:** The rule forbids a business-body from requiring a person to provide a document showing treatment-status or recovery-status in order to enter the organization.

**Notes:** The statute says access, entry, or service. This first sentence compresses that cluster to entry-control because that is where the anti-pass structure is clearest. The state is not ordering a medical act here. It is forbidding a private organization from making status certification the condition of admission.

### S1311 - COV-STA-001-B: The same ban binds governmental entities

**Notation:** `la-wi-fe-su ne wi-fe-ka [la-li-pu-su wi-ra [la-i-zo-li ka-si lo-si-ko-mu si [lo-i-zo-li su-ti lo-ka-fe-zo / lo-i-zo-li su-ti lo-de-be]] wi ki lo-li-pu-su]`

**Written:** `lawifesu ne wifeka [lalipusu wira [laizoli kasi losikomu si [loizoli suti lokafezo / loizoli suti lodebe]] wi ki lolipusu]`

**Natural reading:** The rule forbids a government body from requiring a person to provide a document showing treatment-status or recovery-status in order to enter the government body's operations.

**Notes:** This is where the state layer shows its preemptive shape most clearly. Florida does not stop at private businesses. It extends the same anti-document rule to public bodies. That is structurally different from OSHA's federal model, which works through employer governance rather than forbidding proof-demand by the public sector itself.

### S1312 - COV-STA-001-C: Educational institutions are also blocked from making status proof a condition of attendance

**Notation:** `la-wi-fe-su ne wi-fe-ka [la-to-ki-ne-su wi-ra [la-i-zo-li ka-si lo-si-ko-mu si [lo-i-zo-li su-ti lo-ka-fe-zo / lo-i-zo-li su-ti lo-de-be]] wi ki lo-to-ki-ne-su]`

**Written:** `lawifesu ne wifeka [latokinesu wira [laizoli kasi losikomu si [loizoli suti lokafezo / loizoli suti lodebe]] wi ki lotokinesu]`

**Natural reading:** The rule forbids an educational institution from requiring a person to provide a document showing treatment-status or recovery-status in order to enter the educational institution.

**Notes:** The source text names attendance, enrollment, access, entry, and service. The Tonesu compression again centers the entry condition, because the statute's structural move is to bar the school from converting status documentation into the gate for participation. `to-ki-ne-su` is a new compositional institutional form, but it behaves transparently enough for this batch.

### S1313 - COV-STA-001-D: The statute still allows screening protocols that follow government guidance

**Notation:** `la-wi-fe-su no ne wi-fe-ka lo-wi-re-su si [ka-se lo-i-zo-li] go-si lo-to-su-ki lo-li-pu-su`

**Written:** `lawifesu no ne wifeka lowiresu si [kase loizoli] gosi lotosuki lolipusu`

**Natural reading:** The rule does not prohibit a screening protocol for examining persons that follows published guidance from a government body.

**Notes:** This is the narrowness clause. Florida is not banning all health-governance surfaces at these sites. It is targeting documentation demands while leaving room for screening protocols aligned with government guidance. That distinction matters for the comparison track because it shows the state rule is not simple libertarian negation. It is a selective preemption of one compliance mechanism.

### S1314 - COV-STA-001-E: Violating the rule routes to state-imposed penalty

**Notation:** `go {la-ne-su de lo-wi-fe-su}, du wi-fe'de lu-li-pu-su`

**Written:** `go {lanesu de lowifesu}, du wife'de lulipusu`

**Natural reading:** If an organization violates the rule, a penalty goes to the government body.

**Notes:** The statute's exact ceiling is $5,000 per violation, and the section also contains a health-care-provider carveout. This sentence deliberately models the enforcement path rather than the arithmetic ceiling. The state layer therefore differs from both the federal OSHA specimen and a purely symbolic declaration: violation triggers an administrative sanction.

## COV-STA-001 Batch Summary

| Entry | Tonesu | Written | Claim | Key feature |
|-------|--------|---------|-------|-------------|
| S1310 | `la-wi-fe-su ne wi-fe-ka [la-ne-su wi-ra [la-i-zo-li ka-si lo-si-ko-mu si [lo-i-zo-li su-ti lo-ka-fe-zo / lo-i-zo-li su-ti lo-de-be]] wi ki lo-ne-su]` | `lawifesu ne wifeka [lanesu wira [laizoli kasi losikomu si [loizoli suti lokafezo / loizoli suti lodebe]] wi ki lonesu]` | private business may not demand status proof for entry | anti-pass rule at business layer |
| S1311 | `la-wi-fe-su ne wi-fe-ka [la-li-pu-su wi-ra [la-i-zo-li ka-si lo-si-ko-mu si [lo-i-zo-li su-ti lo-ka-fe-zo / lo-i-zo-li su-ti lo-de-be]] wi ki lo-li-pu-su]` | `lawifesu ne wifeka [lalipusu wira [laizoli kasi losikomu si [loizoli suti lokafezo / loizoli suti lodebe]] wi ki lolipusu]` | government body may not demand the same proof | state preemption reaches public bodies |
| S1312 | `la-wi-fe-su ne wi-fe-ka [la-to-ki-ne-su wi-ra [la-i-zo-li ka-si lo-si-ko-mu si [lo-i-zo-li su-ti lo-ka-fe-zo / lo-i-zo-li su-ti lo-de-be]] wi ki lo-to-ki-ne-su]` | `lawifesu ne wifeka [latokinesu wira [laizoli kasi losikomu si [loizoli suti lokafezo / loizoli suti lodebe]] wi ki lotokinesu]` | educational institution may not make status proof the gate to participation | school-layer extension |
| S1313 | `la-wi-fe-su no ne wi-fe-ka lo-wi-re-su si [ka-se lo-i-zo-li] go-si lo-to-su-ki lo-li-pu-su` | `lawifesu no ne wifeka lowiresu si [kase loizoli] gosi lotosuki lolipusu` | screening protocols remain allowed when they follow government guidance | selective preemption |
| S1314 | `go {la-ne-su de lo-wi-fe-su}, du wi-fe'de lu-li-pu-su` | `go {lanesu de lowifesu}, du wife'de lulipusu` | violation routes to penalty | fine-based enforcement |

**Key findings:**

1. The first state COVID layer is the inverse of the federal OSHA layer. It does not route a compliance burden through employer policy. It prohibits organizations from using status documentation as the gate.
2. The same anti-document shape binds private business, government bodies, and educational institutions. Tonesu makes the cross-sector extension explicit instead of hiding it inside repeated statutory prose.
3. The screening-protocol carveout is load-bearing. Florida is not forbidding all health-management surfaces. It is forbidding one particular proof mechanism while leaving a narrower examination path intact.
4. The state's coercive center is preemption plus penalty, not protocol plus recordkeeping. That gives the comparison track a different authority geometry even when the lived dispute still concerns vaccination status.

## Colloquial Register Analysis

| Form used | CLQ entry | Colloquial form | Notes |
|-----------|-----------|-----------------|-------|
| `li-pu-su` | none | - | 3-root governance-body form - below threshold |
| `to-ki-ne-su` | none | - | 4-root educational-institution form - semantically load-bearing |
| `su-ti lo-de-be` | none | - | recovery-status phrase - below threshold |
| `wi-fe'su` | none | - | formal legal register already load-bearing as rule structure |
| `wi-fe'de` | none | - | formal sanction term - legal register |

**Verdict:** irreducibly formal - the batch depends on keeping statute, prohibition, screening carveout, and enforcement structurally distinct.

*CLQ entries registered from this batch: none.*