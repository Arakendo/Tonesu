# GOV-001 — Napoleonic Administrative State

## Status

In-progress hunt note. Selected as the third phase-1 control specimen after `REV-001`, `CGV-001`, and `REL-001` were opened.

The authority-defining side is now substantially narrowed: the Constitution of Year VIII is a stable public-domain anchor and already exposes the governing chain through the First Consul, ministers, the Council of State, and subordinated local administrations. The action-routing side now has a stable official primary surface as well: Legifrance exposes the law of `28 pluviôse an VIII` on territorial division and administration under a direct JORF text ID, and scan-backed secondary witnesses confirm that this is the prefect-creating implementation surface. The remaining gap is no longer source discovery or source identity, but clean article-level extraction and optional wording-sensitive strengthening for packet quoting.

## Target structure

- batch code: `GOV-001`
- candidate specimen: Napoleonic prefect / ministry administration
- intended role in track: formal state-bureaucracy control specimen centered on delegated office, reporting chains, territorial administration, and executive implementation

## Why this case belongs in phase 1

`GOV-001` gives the track a clean formal-state specimen with strong recoverable rule texts and less ideological noise than later fused or totalizing cases.

It is useful because it can pressure:

- explicit delegated authority through office
- center-periphery reporting and execution chains
- administrative rather than purely charismatic legitimacy
- the relation between ministry, prefect, and local execution

This makes it the right state-side complement to `REV-001`, `CGV-001`, and `REL-001`.

## What this batch needs

The batch should begin with:

1. one authority-defining text
2. one action-routing / reporting text

Working rule: do not file the batch until both surfaces are recovered clearly enough to quote operative clauses.

## Preferred authority-defining source family

Start with a constituting administrative text that defines the prefectural or ministry-centered governance chain.

Preferred first anchor families:

- prefect-system establishment law or decree
- constitutional or administrative text that fixes executive territorial authority

Structural questions for the anchor text:

- who appoints and who governs territorially
- whether the prefect is defined as representative, executor, or supervisor
- how local administration is subordinated to central executive authority

## Current best authority-defining source

- selected anchor: `Constitution du 13 décembre 1799` / `Constitution du 22 frimaire an VIII`
- packet file: `sources/historical-governance/gov-001-constitution-of-year-viii.md`
- stable public text: `https://fr.wikisource.org/wiki/Constitution_du_13_d%C3%A9cembre_1799`
- why it fits: this is the cleanest available phase-1 state-administration anchor because it states the executive chain before the later prefect law operationalizes it

Most useful operative clauses recovered so far:

- Article 41: `Le Premier consul promulgue les lois; il nomme et révoque à volonté ... les ministres ... les membres des administrations locales ...`
- Article 44: `Le gouvernement propose les lois, et fait les règlements nécessaires pour assurer leur exécution.`
- Article 52: `Sous la direction des consuls, un Conseil d'État est chargé de rédiger les projets de lois et les règlements d'administration publique, et de résoudre les difficultés qui s'élèvent en matière administrative.`
- Article 54: `Les ministres procurent l'exécution des lois et des règlements d'administration publique.`
- Article 59: `Les administrations locales ... sont subordonnées aux ministres.`

Structural value:

- central executive nomination power is explicit
- rule-making and execution are distinguished but chained
- local administration is directly subordinated upward through ministers
- the administrative state is already visible before prefect-specific territorial detail is added

## Preferred action-routing source family

The second text should show how the administrative chain actually carries orders, reports, or enforcement.

Best candidate families:

- ministry circular
- prefect instruction or reporting rule
- Council of State administrative procedure or implementation text

Structural questions for the second text:

- how orders move downward
- how reports move upward
- where review exists, if at all
- how administrative action differs from direct force

## Current best action-routing candidate

- narrowed candidate: law of `28 pluviôse an VIII` (`17 February 1800`) concerning the division of the territory and administration
- formal title now recovered from legal-history references: `loi concernant la division du territoire de la République et l'administration`
- stable official primary text recovered: `https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000522248`
- official Legifrance title form: `Loi du 28 pluviôse an VIII (17-02-1800) concernant la division du territoire français et l'administration`
- structure recovered from legal-history references: two titles, 24 articles, plus an annex
- working role: prefectural implementation text establishing the territorial administrative chain below the central executive
- packet file: `sources/historical-governance/gov-001-law-of-28-pluviose.md`

Why this is the right second surface:

- it is the canonical prefect-system law rather than a later commentary on the system
- it should expose the department / arrondissement hierarchy directly
- it is the most likely place to recover prefect, subprefect, and local execution/reporting relations in one text

Verified secondary corroboration now on hand:

- `Histoire de Belgique/Tome 6/Texte entier` on French Wikisource identifies the law of `17 février 1800 (28 pluviôse an VIII)` as the act that `créa l'organisation` of the prefectural state and then summarizes the resulting chain through prefects, subprefects, and departmental councils
- the same scan-backed source describes the prefecture as the `rouage central` of the new administrative machine and distinguishes it from the weaker Directoire-era commissioners
- `Histoire socialiste/Consulat et Empire/02A` on French Wikisource explicitly treats the law of `28 pluviôse an VIII` as the measure that completed the constitution administratively and summarizes core features including the prefect, subprefect, mayor, and the article-3 formula `Le préfet sera seul chargé de l'administration`
- `carnetsdenotes.fr/loi_du_28_pluviose_an_8.htm` preserves a quote-friendly transcription of the full law text, article by article, and cites the matching Gallica `Bulletin des lois` witness at `f268.image`
- the INSP documentation portal record for the law points directly to the same Gallica witness, which makes the scan path more stable than the older dead university PDF route
- modern legal-history reference mirrors independently preserve the same official title and article-3 wording, which reduces the chance that the routing-law identification is off by one text

Primary-source recovery result:

- Legifrance JORF search now returns the law directly when queried by date string `28 pluviôse an VIII`
- the direct official URL resolves to the correct law title on Legifrance and is stable enough to treat as the primary public source surface for the routing text
- this closes the earlier hunt-stage blocker about whether a stable official source existed at all

Current caveat:

- the Legifrance body is still unreliable in this environment because it intermittently collapses into shell-only rendering or a Cloudflare challenge
- that is no longer a blocker, because a quote-friendly duplicate text witness and a Gallica scan path are now on hand
- the remaining task is only to select and copy the article-level clauses worth keeping in the dedicated source packet, with direct confirmation against the official or scan-backed surfaces where later wording-sensitive use makes that worthwhile

## Likely Tonesu pressure points

- `wi-ra` vs `wi-fe-su` in formal state office
- delegated execution and reporting chains
- `to-fe-su` / promulgation questions where rule and implementation separate
- `to-fe-li` if review or administrative challenge surfaces appear
- distinction between recognized office, permitted action, and coercive execution

## First tightening targets

1. preserve the Constitution of Year VIII as the settled authority-defining anchor for GOV-001
2. capture article-level clauses from the Legifrance law surface for the law of `28 pluviôse an VIII`
3. if Legifrance remains shell-only in this environment, recover a scan-backed duplicate or ministry/prefect instruction that shows downward orders and upward reporting

## Likely source surfaces

- Gallica or French legal-history libraries
- French administrative-law compilations
- HathiTrust or Internet Archive scans of decree collections
- university legal-history reproductions where the primary text is quoted directly
- Wayback-recoverable copies of older university PDF reproductions, if the live host is gone

## Ready-to-file standard

`GOV-001` is ready only when the repo has:

- one settled authority-defining source packet or directly stable source surface
- one settled action-routing source packet or directly stable source surface
- enough quoted clauses to distinguish administrative office, reporting, and execution from one another

Current readiness:

- authority-defining side: ready
- action-routing side: source surfaces recovered; only compact clause selection and optional wording-sensitive tightening remain