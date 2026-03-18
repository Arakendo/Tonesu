#!/usr/bin/env python3
"""
build_registry.py

Reads registry/entries.yaml and generates four MkDocs pages:
  www/docs/tonesu/registry/index.md      -- full alphabetical word list
  www/docs/tonesu/registry/english.md    -- English -> Tonesu lookup
  www/docs/tonesu/registry/by-domain.md  -- semantic groupings
  www/docs/tonesu/registry/by-root.md    -- root families

Run:   python scripts/build_registry.py
       (from repo root)
"""

import re
import sys
import yaml
from pathlib import Path
from collections import defaultdict

REPO    = Path(__file__).resolve().parent.parent
ENTRIES = REPO / "registry" / "entries.yaml"
OUT_DIR = REPO / "www" / "docs" / "tonesu" / "registry"

NOTE = (
    "*Generated from "
    "[`registry/entries.yaml`]"
    "(https://github.com/Arakendo/Tonesu/blob/main/registry/entries.yaml).*"
)

STATUS_EMOJI = {
    "active":   "✅",
    "pending":  "⏳",
    "proposed": "⚠️",
    "cold":     "❄️",
    "retired":  "🚫",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def written(form: str) -> str:
    """Written form: remove hyphens, preserve apostrophe (juncture marker)."""
    return form.replace("-", "")


def load_entries() -> list:
    if not ENTRIES.exists():
        sys.exit(f"ERROR: {ENTRIES} not found. Run scripts/migrate_to_yaml.py first.")
    data = yaml.safe_load(ENTRIES.read_text(encoding="utf-8"))
    return data.get("entries", [])


def visible(entry: dict) -> bool:
    """Exclude retired entries from all public-facing pages."""
    return entry.get("status") != "retired"


# ---------------------------------------------------------------------------
# Semantic domain groupings (from 'groups' field on each entry)
# ---------------------------------------------------------------------------

def build_domain_groups(entries: list) -> list:
    """Return [(group_name, [entry_dict, ...]), ...] in canonical order."""
    groups: dict = defaultdict(list)
    for entry in entries:
        if not visible(entry):
            continue
        for g in entry.get("groups", []):
            groups[g].append(entry)

    ORDER = [
        "Person / Agent", "Kinship", "Place / Space", "Artifact / Device",
        "Time", "Knowledge / Epistemic", "Signal / Communication",
        "Affect / Emotional substrate", "Ritual / Sacred",
        "Social / Institutional", "Organism / Biology",
        "Energy / Matter / Physics", "Relation / State / Quality",
    ]
    ordered = []
    seen = set()
    for g in ORDER:
        if g in groups:
            ordered.append((g, groups[g]))
            seen.add(g)
    for g, entries_list in sorted(groups.items()):
        if g not in seen:
            ordered.append((g, entries_list))
    return ordered


# ---------------------------------------------------------------------------
# Root families (from 'lead_root' field)
# ---------------------------------------------------------------------------

def build_root_families(entries: list) -> list:
    families: dict = defaultdict(list)
    for entry in entries:
        if not visible(entry):
            continue
        root = entry.get("lead_root", "?")
        families[root].append(entry)

    result = []
    for root in sorted(families):
        members = families[root]
        parts = [
            f"`{e['form']}` {e['wnum']} {e['gloss'].split(',')[0].split(';')[0].strip()}"
            for e in sorted(members, key=lambda x: x["wnum"])
        ]
        result.append({"root": root, "entries_raw": " · ".join(parts)})
    return result


# ---------------------------------------------------------------------------
# English reverse index
# ---------------------------------------------------------------------------

def build_english_index(entries: list) -> list:
    rows = []
    for entry in entries:
        if not visible(entry):
            continue
        gloss = entry.get("gloss", "")
        gloss_clean = re.sub(r"\(.*?\)", "", gloss).strip()
        seen = set()
        for raw_term in re.split(r"[,;/]", gloss_clean):
            term = raw_term.strip().rstrip(".").lower()
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
    visible_entries = [e for e in entries if visible(e)]
    count = len(visible_entries)
    lines = [
        "---",
        "title: Word Registry",
        "---",
        "",
        "# Word Registry",
        "",
        f"{count} derived compounds, sorted alphabetically.",
        "",
        "See also: [English index](english.md) · "
        "[By domain](by-domain.md) · [By root](by-root.md)",
        "",
        "| Form | Written | W# | Gloss | Status |",
        "|------|---------|-----|-------|--------|",
    ]
    for e in sorted(visible_entries, key=lambda x: x["form"]):
        emoji = STATUS_EMOJI.get(e.get("status", "pending"), "⏳")
        lines.append(
            f'| `{e["form"]}` | {written(e["form"])} | {e["wnum"]} '
            f'| {e["gloss"]} | {emoji} |'
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
        "Look up Tonesu words by English keyword. Where two or more Tonesu words "
        "share a term, all appear together — the **Gloss** column gives the "
        "precise distinction.",
        "",
        "See also: [Alphabetical list](index.md) · [By domain](by-domain.md)",
        "",
        "| English | Written form | Parse | Gloss |",
        "|---------|-------------|-------|-------|",
    ]
    for en_word, e in rows:
        lines.append(
            f'| {en_word} | {written(e["form"])} | `{e["form"]}` | {e["gloss"]} |'
        )
    lines += ["", "---", "", NOTE]
    return "\n".join(lines)


def generate_by_domain_page(domain_groups: list) -> str:
    lines = [
        "---",
        "title: By Domain",
        "---",
        "",
        "# Words by Domain",
        "",
        "Concept-first lookup: find the word you need by semantic category.",
        "",
        "See also: [Alphabetical list](index.md) · "
        "[English index](english.md) · [By root](by-root.md)",
        "",
    ]
    for domain_name, entries_list in domain_groups:
        lines += [
            f"## {domain_name}",
            "",
            "| Form | Written | W# | Gloss |",
            "|------|---------|-----|-------|",
        ]
        for e in sorted(entries_list, key=lambda x: x["form"]):
            lines.append(
                f'| `{e["form"]}` | {written(e["form"])} | {e["wnum"]} | {e["gloss"]} |'
            )
        lines.append("")
    lines += ["---", "", NOTE]
    return "\n".join(lines)


def generate_by_root_page(root_families: list) -> str:
    lines = [
        "---",
        "title: By Root",
        "---",
        "",
        "# Words by Root Family",
        "",
        "Each row groups derived compounds sharing the same lead primitive root.",
        "",
        "See also: [Alphabetical list](index.md) · "
        "[English index](english.md) · [By domain](by-domain.md)",
        "",
        "| Lead root | Derived compounds |",
        "|-----------|------------------|",
    ]
    for r in root_families:
        lines.append(f'| `{r["root"]}` | {r["entries_raw"]} |')
    lines += ["", "---", "", NOTE]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    entries = load_entries()
    domain_groups = build_domain_groups(entries)
    root_families = build_root_families(entries)
    english_rows  = build_english_index(entries)

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    (OUT_DIR / "index.md").write_text(generate_index_page(entries), encoding="utf-8")
    (OUT_DIR / "english.md").write_text(generate_english_page(english_rows), encoding="utf-8")
    (OUT_DIR / "by-domain.md").write_text(generate_by_domain_page(domain_groups), encoding="utf-8")
    (OUT_DIR / "by-root.md").write_text(generate_by_root_page(root_families), encoding="utf-8")

    visible_count = sum(1 for e in entries if visible(e))
    print(f"Generated {visible_count} entries -> {OUT_DIR.relative_to(REPO)}/")
    print(f"  index.md    : {visible_count} words")
    print(f"  english.md  : {len(english_rows)} English terms")
    print(f"  by-domain.md: {len(domain_groups)} domains")
    print(f"  by-root.md  : {len(root_families)} root families")


if __name__ == "__main__":
    main()
