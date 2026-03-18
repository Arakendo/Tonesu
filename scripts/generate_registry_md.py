#!/usr/bin/env python3
"""
generate_registry_md.py

Reads registry/entries.yaml and regenerates the browsable markdown artifacts
in registry/derived/:

  w001-w050.md   — entries W000–W050
  w051-w100.md   — entries W051–W100
  w101-plus.md   — entries W101+
  index.md       — quick-reference index (Sections A, B, C)

Run from repo root:
    python scripts/generate_registry_md.py

Commit the outputs alongside any changes to registry/entries.yaml so that
GitHub browsing always shows current, readable entries.
"""

import re
import sys
import yaml
from pathlib import Path
from collections import defaultdict

REPO    = Path(__file__).resolve().parent.parent
ENTRIES = REPO / "registry" / "entries.yaml"
OUT_DIR = REPO / "registry" / "derived"

# Header added to every generated file
GEN_HEADER = (
    "<!-- Generated from registry/entries.yaml by scripts/generate_registry_md.py -->\n"
    "<!-- Edit registry/entries.yaml, not this file. -->\n\n"
)

STATUS_EMOJI = {
    "active":   "✅",
    "pending":  "⏳",
    "proposed": "⚠️",
    "cold":     "❄️",
    "retired":  "🚫",
}

# Canonical ordering for Section B groups
GROUP_ORDER = [
    "Person / Agent", "Kinship", "Place / Space", "Artifact / Device",
    "Time", "Knowledge / Epistemic", "Signal / Communication",
    "Affect / Emotional substrate", "Ritual / Sacred",
    "Social / Institutional", "Organism / Biology",
    "Energy / Matter / Physics", "Relation / State / Quality",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_entries() -> list:
    if not ENTRIES.exists():
        sys.exit(f"ERROR: {ENTRIES} not found.")
    data = yaml.safe_load(ENTRIES.read_text(encoding="utf-8"))
    return data.get("entries", [])


def wnum_int(entry: dict) -> int:
    return int(entry["wnum"][1:])


def written(form: str) -> str:
    return form.replace("-", "")


def _indent_block(text: str, first_col: int, cont_col: int) -> str:
    """
    Format a multiline text value for a registry fenced-block field.
    First line is placed at first_col, continuations at cont_col.
    """
    lines = text.splitlines()
    if not lines:
        return ""
    out = [lines[0]]
    pad = " " * cont_col
    for ln in lines[1:]:
        out.append(pad + ln if ln.strip() else "")
    return "\n".join(out)


def _field(key: str, value, key_width: int = 14) -> str:
    """Format a single field line (or None if value is absent)."""
    if value is None:
        return None
    key_col = f"{key}:".ljust(key_width)
    val_str = str(value).strip()
    if not val_str:
        return None
    col1 = len(key_col) + 1  # +1 for the space after the colon
    formatted = _indent_block(val_str, col1, key_width + 1)
    return f"{key_col} {formatted}"


# ---------------------------------------------------------------------------
# Entry markdown renderer
# ---------------------------------------------------------------------------

FIELD_ORDER = [
    ("form",           "Form"),
    ("type",           "Type"),
    ("class",          "Class"),
    ("definition",     "Definition"),
    ("composition",    "Composition"),
    ("register",       "Register"),
    ("domain",         "Domain"),
    ("status_display", "Status"),
    ("first_use",      "First use"),
    ("notes",          "Notes"),
    ("related",        "Related"),
    ("examples",       "Examples"),
    ("verbal_form",    "Verbal form"),
    ("agent_form",     "Agent form"),
    ("qualified_form", "Qualified form"),
    ("suffix_stacking","Suffix stacking order"),
    ("derived_family", "Derived compound family"),
    ("extensions",     "Extension forms"),
]


def render_entry(entry: dict) -> str:
    """Render a single entry as a markdown fenced block."""
    wnum = entry["wnum"]
    status = entry.get("status", "pending")
    emoji = STATUS_EMOJI.get(status, "⏳")

    # Build augmented entry dict with display status
    e = dict(entry)
    e["status_display"] = f"{emoji} {status}"

    lines = [f"**{wnum}**", "```"]
    for field_key, field_label in FIELD_ORDER:
        val = e.get(field_key)
        line = _field(field_label, val)
        if line:
            lines.append(line)
    lines.append("```")
    lines.append("")
    lines.append("---")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Split ranges
# ---------------------------------------------------------------------------

def file_for_entry(entry: dict) -> str:
    n = wnum_int(entry)
    if n <= 50:
        return "w001-w050.md"
    if n <= 100:
        return "w051-w100.md"
    return "w101-plus.md"


FILE_HEADERS = {
    "w001-w050.md": (
        "# Derived Registry — W000–W050\n\n"
        "Full entries for derived compounds W000 through W050.\n"
        "Quick-reference index: [index.md](index.md).\n"
        "New entries always go into [w101-plus.md](w101-plus.md) first.\n"
    ),
    "w051-w100.md": (
        "# Derived Registry — W051–W100\n\n"
        "Full entries for derived compounds W051 through W100.\n"
        "Quick-reference index: [index.md](index.md).\n"
    ),
    "w101-plus.md": (
        "# Derived Registry — W101+\n\n"
        "Full entries for derived compounds W101 and above.\n"
        "Quick-reference index: [index.md](index.md).\n"
        "**New entries always go here first.**\n"
    ),
}


# ---------------------------------------------------------------------------
# Index.md generator
# ---------------------------------------------------------------------------

def generate_index(entries: list) -> str:
    active  = sum(1 for e in entries if e.get("status") == "active")
    pending = sum(1 for e in entries if e.get("status") == "pending")
    proposed = sum(1 for e in entries if e.get("status") == "proposed")
    cold    = sum(1 for e in entries if e.get("status") == "cold")
    retired = sum(1 for e in entries if e.get("status") == "retired")
    total   = len(entries)

    # --- File count table ---
    ranges = {
        "w001-w050.md": (0,  50),
        "w051-w100.md": (51, 100),
        "w101-plus.md": (101, 9999),
    }
    file_counts = defaultdict(int)
    for e in entries:
        file_counts[file_for_entry(e)] += 1

    lines = [
        "# Derived Registry — Quick Reference Index",
        "",
        "## Status: Normative",
        "",
        "Full entry format and validation rules: [w001-w050.md](w001-w050.md).",
        "New entries always go into **[w101-plus.md](w101-plus.md)** regardless of eventual W-number.",
        "",
        "---",
        "",
        "## Entry Counts",
        "",
        "| File | Range | Entries |",
        "|------|-------|---------|",
        f"| [w001-w050.md](w001-w050.md) | W000–W050 | {file_counts['w001-w050.md']} |",
        f"| [w051-w100.md](w051-w100.md) | W051–W100 | {file_counts['w051-w100.md']} |",
        f"| [w101-plus.md](w101-plus.md) | W101+ | {file_counts['w101-plus.md']} |",
        "",
        f"**Total: {total} W-series entries** — "
        f"active: {active} · proposed: {proposed} · pending: {pending} · "
        f"cold: {cold} · retired: {retired}",
        "",
        "Status key: ✅ active/accepted · ⏳ pending · ⚠️ proposed · ❄️ cold · 🚫 retired",
        "",
        "---",
        "",
        "## A. Alphabetical Quick Reference",
        "",
        "Sorted by form. Use this to look up a known compound. "
        "For concept-first lookup, see § B.",
        "",
        "| Form | W# | Gloss | St | File |",
        "|------|----|-------|----|------|",
    ]

    # Section A rows
    non_retired = [e for e in entries if e.get("status") != "retired"]
    for e in sorted(non_retired, key=lambda x: x["form"]):
        emoji = STATUS_EMOJI.get(e.get("status", "pending"), "⏳")
        fname = file_for_entry(e)
        stem = fname.replace(".md", "")
        lines.append(
            f'| `{e["form"]}` | {e["wnum"]} | {e["gloss"]} | {emoji} | [{stem}]({fname}) |'
        )

    retired_entries = [e for e in entries if e.get("status") == "retired"]
    if retired_entries:
        names = ", ".join(
            f'W{wnum_int(e):03d} `{e["form"]}`' for e in retired_entries
        )
        lines.append("")
        lines.append(f"*Retired entries ({names}) — see their entries for details.*")

    lines += ["", "---", ""]

    # Section B
    lines += [
        "## B. Semantic Groupings",
        "",
        "Concept-first lookup: find the compound you need by domain.",
        "",
    ]

    groups: dict = defaultdict(list)
    for e in non_retired:
        for g in e.get("groups", []):
            groups[g].append(e)

    seen = set()
    for g in GROUP_ORDER:
        if g in groups:
            _append_group(lines, g, groups[g])
            seen.add(g)
    for g in sorted(groups):
        if g not in seen:
            _append_group(lines, g, groups[g])

    lines += ["---", ""]

    # Section C
    lines += [
        "## C. Root Families",
        "",
        "Quick lookup by lead primitive root.",
        "",
        "| Lead root | Key entries (W#) |",
        "|-----------|-----------------|",
    ]

    root_groups: dict = defaultdict(list)
    for e in non_retired:
        root_groups[e.get("lead_root", "?")].append(e)
    for root in sorted(root_groups):
        members = root_groups[root]
        parts = [
            f"{e['form']} {e['wnum']}"
            for e in sorted(members, key=lambda x: x["wnum"])
        ]
        lines.append(f'| `{root}` | {", ".join(parts)} |')

    return "\n".join(lines)


def _append_group(lines: list, name: str, group_entries: list):
    parts = [
        f"`{e['form']}` {e['wnum']} {e['gloss'].split(',')[0].split(';')[0].strip()}"
        for e in sorted(group_entries, key=lambda x: x["form"])
    ]
    lines.append(f"**{name}**")
    lines.append(" · ".join(parts))
    lines.append("")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    entries = load_entries()
    print(f"Loaded {len(entries)} entries from {ENTRIES.relative_to(REPO)}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Group entries by file
    by_file: dict = defaultdict(list)
    for e in sorted(entries, key=wnum_int):
        by_file[file_for_entry(e)].append(e)

    # Write w*.md files
    for fname, header in FILE_HEADERS.items():
        file_entries = by_file.get(fname, [])
        content_lines = [GEN_HEADER + header, ""]
        for e in file_entries:
            content_lines.append(render_entry(e))
            content_lines.append("")
        path = OUT_DIR / fname
        path.write_text("\n".join(content_lines), encoding="utf-8")
        print(f"  {fname}: {len(file_entries)} entries")

    # Write index.md
    index_content = GEN_HEADER + generate_index(entries)
    (OUT_DIR / "index.md").write_text(index_content, encoding="utf-8")
    print(f"  index.md: {len(entries)} entries indexed")

    print("Done.")


if __name__ == "__main__":
    main()
