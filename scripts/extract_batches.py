#!/usr/bin/env python3
"""
Extract batch metadata from corpus source markdown files → batches.yaml.

Reads sentences.yaml (produced by extract_sentences.py) and scans markdown
headings to extract batch titles and purposes.  Preserves existing titles
for batches whose headings are not found in the current format.
"""
import yaml, re, sys, collections
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from theme import batch_to_theme

sys.stdout.reconfigure(encoding='utf-8')

REPO     = Path(__file__).resolve().parent.parent
SENT_DIR = REPO / "corpus" / "sentences"
SENT_YAML = REPO / "corpus" / "sentences.yaml"
OUT       = REPO / "corpus" / "batches.yaml"


# ── Heading parsers ──────────────────────────────────────────────────────────

def _extract_titles_from_markdown() -> tuple[dict[str, str], dict[str, str]]:
    """Scan markdown files for ## headings; return (titles, purposes) dicts."""
    titles: dict[str, str] = {}
    purposes: dict[str, str] = {}

    for md in sorted(SENT_DIR.rglob("s*.md")):
        text = md.read_text(encoding="utf-8")
        lines = text.split("\n")
        for i, line in enumerate(lines):
            if not line.startswith("## "):
                continue
            # Skip batch-summary headings (e.g. "## CKG-001 Batch Summary")
            if re.match(r"^##\s+[A-Z]+-\d+.*Batch Summary", line):
                continue

            code, title = _parse_heading(line)
            if code and title and code not in titles:
                titles[code] = title

            # Extract purpose from the next few lines
            if code:
                for j in range(i + 1, min(i + 5, len(lines))):
                    pline = lines[j].strip()
                    if pline.startswith("*Batch purpose"):
                        pm = re.match(r"\*Batch purpose.*?:\s*(.*?)\*", pline)
                        if pm:
                            purposes[code] = pm.group(1).strip()
                        break
                    elif pline.startswith("*") and pline.endswith("*") and len(pline) > 2:
                        purposes[code] = pline.strip("* ")
                        break
                    elif pline and not pline.startswith("#"):
                        break

    return titles, purposes


def _parse_heading(line: str) -> tuple[str | None, str | None]:
    """Parse a single ## heading line → (batch_code, title) or (None, None).

    Handles four heading patterns:
      A) ## Title (Srange) — Batch: CODE
      B) ## CODE: Title
      C) ## CODE — Title
      D) ## Title (Srange)   [no explicit code — code derived from sentences]
    """
    body = line[3:].strip()  # strip "## "

    # Pattern A: explicit "— Batch: CODE"
    m = re.search(r"—\s*Batch:\s*([A-Za-z]+-\d+)", body)
    if m:
        code = m.group(1)
        title = body[: m.start()].strip()
        # Strip trailing (S###–S###) or (S###)
        title = re.sub(r"\s*\(S\d+(?:[–\-]S\d+)?\)\s*$", "", title).strip()
        return code, title

    # Pattern B: "CODE: Title"
    m = re.match(r"([A-Z]+-\d+):\s*(.+)", body)
    if m:
        return m.group(1), m.group(2).strip()

    # Pattern C: "CODE — Title"
    m = re.match(r"([A-Z]+-\d+)\s*—\s*(.+)", body)
    if m:
        code = m.group(1)
        title = m.group(2).strip()
        # Strip trailing (S###–S###) or (S###) but keep other parentheticals
        title = re.sub(r"\s*\(S\d+(?:[–\-]S\d+)?\)\s*$", "", title).strip()
        return code, title

    # Pattern D: "Title (S###–S###)" with no explicit code
    m = re.search(r"\(S(\d+)[–\-]S(\d+)\)", body)
    if m:
        title = body[: m.start()].strip()
        # No code derivable from heading alone — return title keyed to None;
        # caller will need to map via sentence data
        return None, title

    return None, None


def build_batches_yaml() -> None:
    """Build batches.yaml from sentences.yaml + markdown headings."""
    md_titles, md_purposes = _extract_titles_from_markdown()

    # Load existing batches.yaml for fallback titles
    existing_titles: dict[str, str] = {}
    existing_purposes: dict[str, str] = {}
    if OUT.exists():
        old = yaml.safe_load(OUT.read_text(encoding="utf-8")) or {}
        for b in old.get("batches", []):
            if b.get("title"):
                existing_titles[b["code"]] = b["title"]
            if b.get("purpose"):
                existing_purposes[b["code"]] = b["purpose"]

    # Group sentences by batch
    data = yaml.safe_load(SENT_YAML.read_text(encoding="utf-8"))
    batch_groups: dict[str, list] = collections.OrderedDict()
    for s in data["sentences"]:
        b = s.get("batch") or ""
        if not b:
            continue
        batch_groups.setdefault(b, []).append(s)

    batches = []
    for code, sents in batch_groups.items():
        snums = [s["snum"] for s in sents]
        first_s, last_s = snums[0], snums[-1]
        theme = batch_to_theme(code)

        # Title priority: markdown extraction > existing YAML > empty
        title = md_titles.get(code) or existing_titles.get(code) or ""
        purpose = md_purposes.get(code) or existing_purposes.get(code) or ""

        entry: dict = {
            "code": code,
            "title": title,
            "theme": theme,
            "range": f"{first_s}–{last_s}" if first_s != last_s else first_s,
            "count": len(sents),
        }
        if purpose:
            entry["purpose"] = purpose

        batches.append(entry)

    result = {"batches": batches}
    OUT.write_text(
        yaml.dump(result, allow_unicode=True, default_flow_style=False,
                  sort_keys=False, width=200),
        encoding="utf-8",
    )

    titled = sum(1 for b in batches if b.get("title"))
    purposed = sum(1 for b in batches if b.get("purpose"))
    print(f"Total batches: {len(batches)}")
    print(f"  With title: {titled}")
    print(f"  With purpose: {purposed}")
    print(f"Wrote: {OUT.relative_to(REPO)}")


if __name__ == "__main__":
    build_batches_yaml()
