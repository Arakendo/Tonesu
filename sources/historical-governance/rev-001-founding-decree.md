# REV-001 — 6 April 1793 Founding Decree Packet

## Status

Settled packet. The operative clauses are verified against the Stanford page image for page 378, and no clearly better public surface was recovered in the subsequent upgrade pass. A cleaner print or archival surface would still improve citation convenience, but it is not needed to stabilize the record.

## Source

- Working title: National Convention decree organizing the Committee of Public Safety
- Date: 6 April 1793
- Source surface: Stanford / Chicago `Archives Parlementaires` PhiloLogic corpus
- Corpus home: `https://sul-philologic.stanford.edu/philologic/archparl/`
- Volume surface: `https://sul-philologic.stanford.edu/philologic/archparl/reports/bibliography.py?filename=APvol61.tei`
- Recovered text objects:
  - `https://sul-philologic.stanford.edu/philologic/archparl/scripts/get_text_object.py?philo_id=61%203%2011%201%20103`
  - `https://sul-philologic.stanford.edu/philologic/archparl/scripts/get_text_object.py?philo_id=61%203%2011%201%20127`
  - `https://sul-philologic.stanford.edu/philologic/archparl/scripts/get_text_object.py?philo_id=61%203%2011%201%20130`
- Supporting session surface: `https://sul-philologic.stanford.edu/philologic/archparl/scripts/get_text_object.py?philo_id=61%203%2011%201`
- Page image used for verification: `http://artflsrv03.uchicago.edu/images/archivesparlementaires//APvol61/sg325qs6321_00_0384.jpg`
- Editorial citation surfaced inside the corpus notes: `Collection Baudouin, tome 28, page 42, et P. V., tome 9, page 113`

## Used by

- authority-defining text for `REV-001`
- referenced from `sources/historical-governance/rev-001-committee-of-public-safety.md`

## Why this packet exists

This is the first recovered source surface that directly does the authority-defining work needed for `REV-001`. It is stronger than encyclopedia or glossary summaries because it preserves the operative decree text itself, tied to a dated National Convention session.

## Important source note

`APvol61` has awkward top-level metadata in the corpus:

- bibliography metadata surfaces the volume year as `1792`
- the recovered decree paragraphs themselves carry `id = 1793-04-06`
- the volume table includes sessions from late March through 12 April 1793

This looks like a volume-level metadata quirk rather than a problem with the session text. Preserve the anomaly in the record so later citation work stays honest.

## Operative clauses recovered so far

### 1. Constituting the committee

Recovered corpus text:

- `Art. 1er. Il sera formé, par appel nominal, un comité de salut public, composé de neuf membres de la Convention nationale.`

Structural value:

- directly constitutes the body
- fixes the initial composition
- gives a clean authority-establishing clause for the batch opening

### 2. Secret deliberation and supervisory control over the executive

Recovered corpus text:

- `Art. 2. Ce comité délibérera en secret; il sera chargé de surveiller et d'accélérer l'action de l'administration confiée au conseil exécutif provisoire, dont il pourra même suspendre les arrêtés lorsqu'il les croira contraires à l'intérêt national, à la charge d'en informer sans délai la Convention.`

Structural value:

- links secrecy, supervision, and executive acceleration in one article
- gives an explicit suspension power over executive acts
- preserves the reporting-back condition to the Convention

### 3. Urgent defense powers and execution routing

Recovered corpus text:

- `Art. 3. Il est autorisé à prendre, dans les circonstances urgentes, des mesures de défense générale extérieure et intérieure; et les arrêtés signés de la majorité de ses membres délibérants, qui ne pourront être au-dessous des deux tiers, seront exécutés sans délai par le conseil exécutif provisoire.`
- `Il ne pourra, en aucun cas, décerner des mandats d'amener ou d'arrêt, si ce n'est contre des agents d'exécution, et à la charge d'en rendre compte sans délai à la Convention.`

Structural value:

- distinguishes authorization from mere consultation
- routes committee decisions into immediate executive execution
- sets an internal threshold for valid committee action
- preserves a boundary on arrest power in the founding form

### 4. Secret-expense funding

Recovered corpus text:

- `Art. 4. La trésorerie nationale tiendra à la disposition du comité du salut public, jusqu'à concurrence de 100,000 livres, pour dépenses secrètes, qui seront délivrées par le comité, et payées sur les ordonnances, qui seront signées comme les arrêtés.`

Structural value:

- ties institutional authority to an immediate fiscal instrument
- shows that the body is not merely deliberative

### 5. Weekly written reporting, register, and time limit

Recovered corpus text:

- `Art. 5. Il fera chaque semaine un rapport général et par écrit de ses opérations, et de la situation de la République.`
- `Art. 6. Il sera tenu registre de toutes les délibérations.`
- `Art. 7. Ce comité n'est établi que pour un mois.`

Structural value:

- preserves explicit reporting cadence
- shows record-keeping is constitutive, not incidental
- gives the initial emergency-limited duration before later expansion

### 6. Treasury independence from the execution committee

Recovered corpus text:

- `Art. 8. La trésorerie nationale demeurera indépendante du comité d'exécution, et soumise à la surveillance immédiate de la Convention, suivant le mode fixé par les décrets.`

Structural value:

- helps map what remained outside committee control in the founding form
- useful for distinguishing concentrated authority from total administrative absorption

## Recovery note

The wording above comes from the Stanford `get_text_object.py` corpus output and has been checked against the linked page-378 image. Minor corpus/OCR-like errors appeared in a few places in the raw surface, so the clauses above are normalized only where the page image makes the intended reading textually obvious:

- `Iî sera, formé ... ui} comité` normalized to `Il sera formé ... un comité`
- page 378 appears to print `de comité du Salut public` in Article 4; the packet normalizes this to `du comité du salut public` as the intended reading while preserving the anomaly here
- `c'est établi` normalized to `n'est établi`

Articles 1 to 8 are image-checked. The only remaining textual judgment call is whether a later citation policy should preserve the apparent printed anomaly in Article 4 verbatim or continue using the current normalized reading with an editorial note.

## Future upgrade option

If a cleaner archival or printed reproduction becomes available, it can be added as a secondary citation surface. Until then, this packet is the settled authority-defining source record for `REV-001`.