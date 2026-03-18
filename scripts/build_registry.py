#!/usr/bin/env python3
"""
build_registry.py

Reads registry/derived/index.md and generates four MkDocs pages:
  www/docs/tonesu/registry/index.md      — full alphabetical word list
  www/docs/tonesu/registry/english.md    — English → Tonesu lookup
  www/docs/tonesu/registry/by-domain.md  — semantic groupings
  www/docs/tonesu/registry/by-root.md    — root families

Run:   python scripts/build_registry.py
       (from repo root)
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

REPO = Path(__file__).resolve().parent.parent
INDEX_MD = REPO / "registry" / "derived" / "index.md"
OUT_DIR = REPO / "www" / "docs" / "tonesu" / "registry"

NOTE = "*Generated from [`registry/derived/index.md`](https://github.com/Arakendo/Tonesu/blob/main/registry/derived/index.md).*"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def written(parse: str) -> str:
    """Written form: remove hyphens, preserve ' (juncture marker)."""
    return parse.replace("-", "")


def strip_backticks(s: str) -> str:
    return s.strip().strip("`")


# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------

def parse_section_a(text: str) -> list:
    """Parse the alphabetical table (Section A). Returns list of entry dicts."""
    sec = re.search(
        r"## A\. Alphabetical Quick Reference.*?\n(.*?)(?=\n---|\n## [B-Z]\.)",
        text, re.S
    )
    if not sec:
        sys.exit("ERROR: Could not find Section A in index.md")

    entries = []
    for line in sec.group(1).splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) < 4:
            continue
        form_cell, wnum_cell, gloss_cell, status_cell = (
            cells[0], cells[1], cells[2], cells[3]
        )

        # Skip header and separator rows
        if "Form" in form_cell or "---" in form_cell:
            continue

        m = re.search(r"(W\d+)", wnum_cell)
        if not m:
            continue
        wnum = m.group(1)

        # Extract primary form (first backtick-wrapped token)
        forms = re.findall(r"`([^`]+)`", form_cell)
        if not forms:
            continue
        form = forms[0]

        entries.append({
            "form": form,
            "written": written(form),
            "wnum": wnum,
            "gloss": gloss_cell.strip(),
            "status": status_cell.strip(),
            "all_forms": forms,
        })

    return entries


def parse_entry_list(s: str) -> list:
    """Parse a · -delimited list like: `form` W### gloss · `form` W### gloss ..."""
    entries = []
    for part in re.split(r"\s*·\s*", s):
        part = part.strip()
        if not part:
            continue
        m = re.match(r"`([^`]+)`\s+(W\d+)\s+(.*)", part)
        if m:
            form = m.group(1)
            entries.append({
                "form": form,
                "written": written(form),
                "wnum": m.group(2),
                "gloss": m.group(3).strip(),
            })
    return entries


def parse_section_b(text: str) -> list:
    """Parse semantic groupings (Section B). Returns [(domain_name, [entries]), ...]."""
    sec = re.search(
        r"## B\. Semantic Groupings.*?\n(.*?)(?=\n---|\n## [C-Z]\.)",
        text, re.S
    )
    if not sec:
        return []

    domains = []
    current_name = None
    current_entries = []

    for line in sec.group(1).splitlines():
        line = line.strip()
        if not line:
            continue

        m = re.match(r"\*\*(.+?)\*\*", line)
        if m:
            if current_name and current_entries:
                domains.append((current_name, current_entries))
            current_name = m.group(1)
            current_entries = []
            # Entries may follow on the same line after the header
            rest = line[m.end():].strip()
            if rest:
                current_entries.extend(parse_entry_list(rest))
        elif current_name and "`" in line:
            current_entries.extend(parse_entry_list(line))

    if current_name and current_entries:
        domains.append((current_name, current_entries))

    return domains


def parse_section_c(text: str) -> list:
    """Parse root families table (Section C). Returns list of {root, entries_raw}."""
    sec = re.search(r"## C\. Root Families.*?\n(.*?)$", text, re.S)
    if not sec:
        return []

    roots = []
    for line in sec.group(1).splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) < 2:
            continue
        root_cell, entries_cell = cells[0], cells[1]
        if "Lead root" in root_cell or "---" in root_cell:
            continue
        root = strip_backticks(root_cell)
        roots.append({"root": root, "entries_raw": entries_cell.strip()})

    return roots


# ---------------------------------------------------------------------------
# English index builder
# ---------------------------------------------------------------------------

def build_english_index(entries: list) -> list:
    """
    Build sorted [(english_term, entry_dict)] pairs from all glosses.
    Splits on comma and semicolon; filters out long descriptive phrases.
    """
    rows = []
    for entry in entries:
        gloss = entry["gloss"]
        # Remove parenthetical annotations
        gloss_clean = re.sub(r"\(.*?\)", "", gloss)
        # Remove status emoji
        gloss_clean = re.sub(r"[⏳✅⚠️❄️🚫]", "", gloss_clean).strip()

        seen = set()
        for raw_term in re.split(r"[,;/]", gloss_clean):
            term = raw_term.strip().rstrip(".").lower()
            # Skip empty, too long, or purely symbolic terms
            if not term or len(term) > 35 or len(term.split()) > 4:
                continue
            if term in seen:
                continue
            seen.add(term)
            rows.append((term, entry))

    rows.sort(key=lambda x: x[0])
    return rows


# ---------------------------------------------------------------------------
# Page generators
# ---------------------------------------------------------------------------

def generate_index_page(entries: list) -> str:
    count = len(entries)
    lines = [
        "---",
        "title: Word Registry",
        "---",
        "",
        "# Word Registry",
        "",
        f"{count} derived compounds, sorted alphabetically.",
        "",
        "See also: [English index](english.md) · [By domain](by-domain.md) · [By root](by-root.md)",
        "",
        "| Form | Written | W# | Gloss | Status |",
        "|------|---------|-----|-------|--------|",
    ]
    for e in sorted(entries, key=lambda x: x["form"]):
        lines.append(
            f'| `{e["form"]}` | {e["written"]} | {e["wnum"]} | {e["gloss"]} | {e["status"]} |'
        )
    lines += ["", "---", "", NOTE]
    return "\n".join(lines)


def generate_english_page(rows: list) -> str:
    lines = [
        "---",
        "title: English Index",
        "---",
        "",
        "# English Index",
        "",
        "Look up Tonesu words by English keyword. Where two or more Tonesu words share a term, "
        "all appear together — the **Gloss** column gives the precise distinction.",
        "",
        "See also: [Alphabetical list](index.md) · [By domain](by-domain.md)",
        "",
        "| English | Written form | Parse | Gloss |",
        "|---------|-------------|-------|-------|",
    ]
    for en_word, e in rows:
        lines.append(
            f'| {en_word} | {e["written"]} | `{e["form"]}` | {e["gloss"]} |'
        )
    lines += ["", "---", "", NOTE]
    return "\n".join(lines)


def generate_by_domain_page(domains: list) -> str:
    lines = [
        "---",
        "title: By Domain",
        "---",
        "",
        "# Words by Domain",
        "",
        "Concept-first lookup: find the word you need by semantic category.",
        "",
        "See also: [Alphabetical list](index.md) · [English index](english.md) · [By root](by-root.md)",
        "",
    ]
    for domain_name, entries in domains:
        lines += [
            f"## {domain_name}",
            "",
            "| Form | Written | W# | Gloss |",
            "|------|---------|-----|-------|",
        ]
        for e in entries:
            lines.append(
                f'| `{e["form"]}` | {e["written"]} | {e["wnum"]} | {e["gloss"]} |'
            )
        lines.append("")
    lines += ["---", "", NOTE]
    return "\n".join(lines)


def generate_by_root_page(roots: list) -> str:
    lines = [
        "---",
        "title: By Root",
        "---",
        "",
        "# Words by Root Family",
        "",
        "Each row groups derived compounds sharing the same lead primitive root.",
        "",
        "See also: [Alphabetical list](index.md) · [English index](english.md) · [By domain](by-domain.md)",
        "",
        "| Lead root | Derived compounds |",
        "|-----------|------------------|",
    ]
    for r in roots:
        lines.append(f'| `{r["root"]}` | {r["entries_raw"]} |')
    lines += ["", "---", "", NOTE]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if not INDEX_MD.exists():
        sys.exit(f"ERROR: {INDEX_MD} not found")

    text = INDEX_MD.read_text(encoding="utf-8")

    entries = parse_section_a(text)
    domains = parse_section_b(text)
    roots = parse_section_c(text)
    english_rows = build_english_index(entries)

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    (OUT_DIR / "index.md").write_text(
        generate_index_page(entries), encoding="utf-8"
    )
    (OUT_DIR / "english.md").write_text(
        generate_english_page(english_rows), encoding="utf-8"
    )
    (OUT_DIR / "by-domain.md").write_text(
        generate_by_domain_page(domains), encoding="utf-8"
    )
    (OUT_DIR / "by-root.md").write_text(
        generate_by_root_page(roots), encoding="utf-8"
    )

    print(f"Generated {len(entries)} entries → {OUT_DIR.relative_to(REPO)}/")
    print(f"  index.md    : {len(entries)} words")
    print(f"  english.md  : {len(english_rows)} English terms")
    print(f"  by-domain.md: {len(domains)} domains")
    print(f"  by-root.md  : {len(roots)} root families")


if __name__ == "__main__":
    main()
