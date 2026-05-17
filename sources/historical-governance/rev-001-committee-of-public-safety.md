# REV-001 — Committee of Public Safety

## Status

Core two-source basis settled. Both the founding / authority-defining side and the action-routing side are now preserved in settled, image-checked packet forms. The remaining work is optional citation cleanup, optional surface upgrades, or deciding whether `REV-001` needs a third supporting text.

## Target structure

- batch code: `REV-001`
- candidate specimen: Committee of Public Safety
- intended role in track: clean revolutionary emergency-legitimacy control specimen

## What this batch needs

The batch should begin with:

1. one authority-defining text
2. one action-routing / enforcement text

The current hunt status is:

- authority-defining text: settled packet
- action-routing text: settled packet

## Confirmed authority-defining source

### National Convention decree of 6 April 1793 organizing the Committee of Public Safety

- source surface: Stanford / Chicago `Archives Parlementaires` PhiloLogic corpus
- corpus home: `https://sul-philologic.stanford.edu/philologic/archparl/`
- volume surface: `https://sul-philologic.stanford.edu/philologic/archparl/reports/bibliography.py?filename=APvol61.tei`
- decisive text objects recovered:
	- `https://sul-philologic.stanford.edu/philologic/archparl/scripts/get_text_object.py?philo_id=61%203%2011%201%20103`
	- `https://sul-philologic.stanford.edu/philologic/archparl/scripts/get_text_object.py?philo_id=61%203%2011%201%20127`
	- `https://sul-philologic.stanford.edu/philologic/archparl/scripts/get_text_object.py?philo_id=61%203%2011%201%20130`
- session date surfaced in text-object metadata: `1793-04-06`
- supporting editorial citation carried in the corpus note: `Collection Baudouin, tome 28, page 42, et P. V., tome 9, page 113`

### Why this matters

This is now a strong authority-defining text for `REV-001` because it does the constituting work directly. The recovered decree text includes:

- formal creation of the committee by nominal call
- fixed initial composition of nine Convention members
- secret deliberation
- supervisory and accelerative control over the provisional executive council
- suspension power over executive decrees subject to reporting back to the Convention
- urgent defense powers with explicit execution routing
- a one-month term limit in the founding form

### Important source note

The Stanford corpus surface is materially useful but slightly awkward bibliographically:

- `APvol61` is present and searchable on the backend
- top-level volume metadata surfaces as `1792`
- the actual recovered decree paragraphs carry `id = 1793-04-06`
- the volume's chronological table also spans late March to mid-April 1793

So this is a strong near-primary recovery surface, but the packet should still preserve the exact recovered clauses and note the metadata anomaly.

### Current packet state

Settled packet: `sources/historical-governance/rev-001-founding-decree.md`

## Confirmed strong candidate source

### Law of 14 Frimaire / 4 December 1793

- source surface: Internet Archive scan
- URL: `https://archive.org/details/decretdu14frimai00bill_0`
- title as surfaced: `Décret du 14 frimaire : précédé du rapport fait au nom du Comité de salut public sur un mode de gouvernement provisoire & révolutionnaire`
- publication date surfaced: 1793
- repository / collection: Newberry French Pamphlet Collection via Internet Archive

### Why this matters

This is a strong action-routing text for `REV-001` because it visibly centralizes revolutionary governance under the Committee of Public Safety and routes execution through a formalized administrative channel. Even the discovery-stage summary is already structurally useful:

- revolutionary government is made provisional and explicit
- coercive execution is foregrounded as part of governance machinery
- committee authority is linked to centralized publication and implementation

### Packet trigger

High. The source is a scan with OCR artifacts and older typography. If used in the batch, preserve exact quoted clauses in a dedicated packet rather than relying on downstream summaries.

### Current packet state

Settled packet: `sources/historical-governance/rev-001-law-of-14-frimaire.md`

## Discovery / context source

### Liberty, Equality, Fraternity glossary page

- URL: `https://revolution.chnm.org/items/show/1025`
- citation surface: `Committee of Public Safety`, Liberty, Equality, Fraternity: Exploring the French Revolution

### Why it is useful

This page is not the operative decree text, but it is useful as a discovery aid because it confirms the institutional timeline:

- provisional executive group after 15 August 1792
- Committee of General Defense on 1 January 1793
- Committee of Public Safety formalized in March 1793
- stable twelve-member Great Committee from 10 July 1793 to 27 July 1794

Use this only as a guide to source-hunting and framing, not as the final authority text.

## Open source gap

### Verification and cleaner-surface upgrade still needed

The core source recovery and scan verification work is now done. Two optional follow-up tasks remain:

1. verify the recovered wording against the linked page images or another direct facsimile surface
2. if possible, recover a cleaner French archival or print surface for citation convenience alongside the Stanford corpus object URLs

The first item is now satisfied for the currently selected clause set in both packets; the remaining open work is essentially item 2.

### Extra pass result

One additional public-surface hunt was run after the scan verification pass.

- No clearly better public web surface was recovered for the 6 April 1793 founding decree than the current Stanford `Archives Parlementaires` corpus plus page-image combination.
- `Collection Baudouin, tome 28, page 42` and `P. V., tome 9, page 113` remain the strongest print citations visible from the recovered decree notes, but no directly accessible public digital copy was surfaced in this pass.
- Archive.org `Bulletin des lois` items dated `1793` were investigated as possible cleaner surfaces for the 14 Frimaire decree. Their metadata looks plausible, but first-pass OCR/content checks did not verify the operative clause set, so they remain near-miss leads rather than confirmed upgrades.

For now, the current settled packets remain the strongest verified source surfaces in the repo.

## Next hunt targets

1. find a cleaner French archival or print surface for the 6 April 1793 founding decree alongside the Stanford corpus object URLs
2. find a cleaner French archival or transcription surface for the Law of 14 Frimaire than the current scan-backed packet
3. decide whether `REV-001` needs a third supporting source such as a Revolutionary Tribunal or surveillance-committee procedural text

## Next likely source surfaces

- Gallica / Bibliotheque nationale de France
- French Revolution Digital Archive / Liberty, Equality, Fraternity cross-links
- Yale Avalon or other university legal-history reproductions
- archival decree compilations or Convention proceedings

## Provenance note

This note records the first live hunt pass for `REV-001`. It now preserves both identified source pillars for the batch and the remaining verification work, so future packet work does not need to restart from zero.
