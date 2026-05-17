# Source Artifacts

This folder preserves source-side materials that Tonesu content derives from.

The goal is not to duplicate every public-domain or easily recoverable text in full. The goal is to keep proof-grade ride-along artifacts for claims, analyses, and structured comparisons that appear in the repository or on tonesu.org when the operative source surface is brittle, time-sensitive, scattered, or easy to misremember.

## What belongs here

- source packets for translation stress tests
- source packets for website pages or notes that derive claims from external texts
- archival excerpts for difficult-to-recover legal, historical, institutional, or policy documents
- exact operative quotations used to justify a batch, page, or analytic claim

## What does not belong here

- arbitrary reading notes with no downstream use
- full-text mirrors of sources that are stable and trivial to recover unless the exact edition matters
- secondary summaries when the operative primary text is available

## Packet rule

When a repo file or tonesu.org page makes a claim that depends on an external source, create a packet here if any of the following are true:

- the source is brittle, archived, dynamically rendered, or likely to disappear
- the operative text is buried inside a long document and needs exact line preservation
- translations differ materially and the chosen wording matters
- the source is a scan, image PDF, OCR artifact, or otherwise awkward to recover cleanly
- the page or batch depends on a historically or legally sensitive wording distinction

## Recommended structure

Organize packets by topic or project in subfolders, for example:

- `sources/covid-era-mandates/`
- `sources/historical-governance/`
- `sources/translations/<theme>/`

Each topic folder should keep its own `README.md` index of current packets.

## Packet contents

Each packet should preserve:

- source title
- issuing body, author, or institution
- original URL or archive location when known
- publication / decree / filing date when known
- retrieval or capture date
- exact operative lines relied on
- the repo file, batch, or tonesu.org page that uses the source
- short provenance note explaining why the packet exists

## Working rule for tonesu.org

If a page on tonesu.org derives analysis, examples, historical framing, or comparison claims from an external source, the source packet should live in this folder even if the public site does not expose the packet directly. The packet is the ride-along provenance record for the repository and future rebuilds.

## Existing specialized folders

- `covid-era-mandates/` already follows this pattern for the COVID comparison work.
- `historical-governance/` holds packets and hunt notes for the comparative legitimacy morphology track.
