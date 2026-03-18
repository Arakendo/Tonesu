#!/usr/bin/env python3
"""
migrate_to_yaml.py

One-time migration: parse the three registry/derived/w*.md source files
and index.md (for glosses, statuses, and Section B group memberships) into
a single canonical registry/entries.yaml file.

Run once from repo root:
    python scripts/migrate_to_yaml.py
"""

import re
import sys
import yaml
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SOURCE_FILES = [
    REPO / "registry" / "derived" / "w001-w050.md",
    REPO / "registry" / "derived" / "w051-w100.md",
    REPO / "registry" / "derived" / "w101-plus.md",
]
INDEX_MD = REPO / "registry" / "derived" / "index.md"
OUT_YAML = REPO / "registry" / "entries.yaml"

FENCE = "```"

# ---------------------------------------------------------------------------
# YAML literal-block representer (multiline strings use | style)
# ---------------------------------------------------------------------------

def _str_representer(dumper, data):
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    # Quote if the string looks like a boolean, null, or starts with a
    # YAML-special character.
    if data.lower() in {"true", "false", "null", "yes", "no", "on", "off"}:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style='"')
    if data and data[0] in "#:&*!|>{[":
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style='"')
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


class _WideDumper(yaml.Dumper):
    """Dumper that never wraps lines (best_width = 2**30)."""
    def __init__(self, stream, **kwargs):
        super().__init__(stream, **kwargs)
        self.best_width = 2 ** 30


_WideDumper.add_representer(str, _str_representer)


# ---------------------------------------------------------------------------
# Field name normalisation
# ---------------------------------------------------------------------------

FIELD_NORM = {
    "form":                   "form",
    "type":                   "type",
    "class":                  "class",
    "gloss":                  "gloss",
    "definition":             "definition",
    "composition":            "composition",
    "register":               "register",
    "domain":                 "domain",
    "status":                 "status",
    "first use":              "first_use",
    "notes":                  "notes",
    "related":                "related",
    "examples":               "examples",
    "verbal form":            "verbal_form",
    "agent form":             "agent_form",
    "qualified form":         "qualified_form",
    "suffix stacking order":  "suffix_stacking",
    "derived compound family":"derived_family",
    "extension forms":        "extensions",
    "extension form":         "extensions",
}

# Index A status-emoji → normalised string
STATUS_NORM = {
    "✅": "active",
    "⏳": "pending",
    "⚠️": "proposed",
    "❄️": "cold",
    "🚫": "retired",
    # legacy text variants (in case they appear)
    "✅ active": "active",
    "pending":   "pending",
    "proposed":  "proposed",
    "cold":      "cold",
    "retired":   "retired",
}


def normalise_status(raw: str) -> str:
    raw = raw.strip()
    # Strip leading/trailing emoji clusters then try exact match
    s = STATUS_NORM.get(raw)
    if s:
        return s
    # Try stripping emoji prefix (e.g. "✅ active")
    for emoji, val in STATUS_NORM.items():
        if raw.startswith(emoji):
            return val
    return "pending"


# ---------------------------------------------------------------------------
# Source-file parsing
# ---------------------------------------------------------------------------

def parse_source_file(path: Path) -> dict:
    """
    Parse a w*.md source file.
    Returns {wnum_int: raw_fields_dict}.
    raw_fields_dict also includes a synthetic '__header__' key with the
    full entry header line for detecting retired/proposed annotations.
    """
    text = path.read_text(encoding="utf-8")
    result = {}

    # Find all **WXXX** header positions
    headers = [(int(m.group(1)), m.start()) for m in re.finditer(r"\*\*W(\d+)\*\*", text)]

    for i, (wnum, start) in enumerate(headers):
        end = headers[i + 1][1] if i + 1 < len(headers) else len(text)
        chunk = text[start:end]

        fenced_lines = _extract_fenced_block(chunk)
        if fenced_lines is None:
            continue

        fields = _parse_fields(fenced_lines)
        # Capture the header line (first line of chunk) for annotation detection
        fields["__header__"] = chunk.splitlines()[0]
        result[wnum] = fields

    return result


def _extract_fenced_block(text: str):
    """Return list of lines inside the first ``` block, or None."""
    lines = text.splitlines()
    in_fence = False
    content = []
    for line in lines:
        if line.rstrip() == FENCE:
            if in_fence:
                return content
            in_fence = True
        elif in_fence:
            content.append(line)
    return None


def _parse_fields(lines: list) -> dict:
    """
    Parse fenced-block field lines into a dict.

    Field lines look like:
        Key:          value text here
    Continuation lines are indented (≥4 spaces) and contain no colon at col 0.
    """
    fields = {}
    current_key = None
    current_parts = []

    for line in lines:
        # New field: starts at column 0 with "Word(s):" pattern, not indented
        if not line.startswith((" ", "\t")):
            m = re.match(r'^([A-Za-z][A-Za-z /]+):\s*(.*)', line)
            if m:
                _flush(fields, current_key, current_parts)
                key_raw = m.group(1).strip().lower()
                current_key = FIELD_NORM.get(key_raw, key_raw.replace(" ", "_"))
                val_first = m.group(2).strip()
                current_parts = [val_first] if val_first else []
                continue
            # Non-field line at col 0 (e.g. separator dashes) — end current field
            _flush(fields, current_key, current_parts)
            current_key = None
            current_parts = []
        else:
            # Continuation line
            if current_key is not None:
                current_parts.append(line.strip())

    _flush(fields, current_key, current_parts)
    return fields


def _flush(fields, key, parts):
    if key is None:
        return
    # Join, collapse runs of blank lines, strip
    val = "\n".join(parts)
    # Remove leading/trailing blank lines
    val = val.strip()
    if val:
        fields[key] = val


# ---------------------------------------------------------------------------
# Index.md parsing (Section A and B)
# ---------------------------------------------------------------------------

def parse_index_a(text: str) -> dict:
    """
    Parse Section A table into {wnum_int: {form, gloss, status}}.
    Status values are normalised strings (active/pending/proposed/cold/retired).
    """
    sec = re.search(
        r"## A\. Alphabetical Quick Reference.*?\n(.*?)(?=\n---|\n## [B-Z]\.)",
        text, re.S,
    )
    if not sec:
        sys.exit("ERROR: Could not find Section A in index.md")

    result = {}
    for line in sec.group(1).splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) < 4:
            continue
        form_cell, wnum_cell, gloss_cell, status_cell = cells[0], cells[1], cells[2], cells[3]
        if "Form" in form_cell or "---" in form_cell:
            continue
        m = re.search(r"W(\d+)", wnum_cell)
        if not m:
            continue
        wnum = int(m.group(1))
        forms = re.findall(r"`([^`]+)`", form_cell)
        form = forms[0] if forms else None
        gloss = re.sub(r"\s+", " ", gloss_cell).strip()
        status = normalise_status(status_cell.strip())
        result[wnum] = {"form": form, "gloss": gloss, "status": status}

    return result


def parse_index_b(text: str) -> dict:
    """
    Parse Section B into {wnum_int: [group_name, ...]}.
    """
    sec = re.search(
        r"## B\. Semantic Groupings.*?\n(.*?)(?=\n---|\n## [C-Z]\.)",
        text, re.S,
    )
    if not sec:
        return {}

    groups_by_wnum: dict = {}
    current_group = None

    for line in sec.group(1).splitlines():
        line_s = line.strip()
        if not line_s:
            continue
        m = re.match(r"\*\*(.+?)\*\*", line_s)
        if m:
            current_group = m.group(1).strip()
            rest = line_s[m.end():].strip()
            if rest and current_group:
                _add_group_memberships(rest, current_group, groups_by_wnum)
        elif current_group:
            _add_group_memberships(line_s, current_group, groups_by_wnum)

    return groups_by_wnum


def _add_group_memberships(text: str, group: str, out: dict):
    for m in re.finditer(r"W(\d+)", text):
        wnum = int(m.group(1))
        if wnum not in out:
            out[wnum] = []
        if group not in out[wnum]:
            out[wnum].append(group)


# ---------------------------------------------------------------------------
# Lead-root computation
# ---------------------------------------------------------------------------

def lead_root(form: str) -> str:
    """First CV root before first - or ' separator."""
    return re.split(r"[-']", form)[0]


# ---------------------------------------------------------------------------
# Entry assembly
# ---------------------------------------------------------------------------

PROSE_FIELDS = ("definition", "composition", "notes", "related", "examples",
                "verbal_form", "agent_form", "qualified_form", "suffix_stacking",
                "derived_family", "extensions", "first_use")

SCALAR_FIELDS = ("type", "class", "register", "domain")


def assemble(wnum: int, raw: dict, idx_a: dict, idx_b: dict) -> dict:
    idx = idx_a.get(wnum, {})

    # Core identifiers — always present
    form_raw = raw.get("form") or idx.get("form") or f"UNKNOWN-W{wnum:03d}"
    # Strip inline ← annotation comments (e.g. "de-ti  ← INCORRECT ROOT ORDER...")
    form = re.split(r"\s*←", form_raw)[0].strip()

    gloss = idx.get("gloss") or raw.get("gloss") or ""

    # Status resolution:
    #   1. If entry header contains "retired" annotation → retired
    #   2. Source-file status if non-pending (active/proposed/cold/retired)
    #   3. Index status (updated by accept_registry.py acceptance pass)
    #   4. Fallback: pending
    header_line = raw.get("__header__", "")
    raw_status = normalise_status(raw.get("status", "")) if raw.get("status") else None
    idx_status = idx.get("status")  # already normalised

    if "retired" in header_line.lower():
        status = "retired"
    elif raw_status and raw_status != "pending":
        status = raw_status          # source file is explicit
    elif idx_status:
        status = idx_status          # index updated by acceptance pass
    elif raw_status:
        status = raw_status          # both say pending — use raw
    else:
        status = "pending"

    entry = {
        "wnum":      f"W{wnum:03d}",
        "form":      form,
        "gloss":     gloss,
        "status":    status,
        "lead_root": lead_root(form),
    }

    # Scalar fields
    for f in SCALAR_FIELDS:
        val = raw.get(f, "").strip()
        if val:
            entry[f] = val

    # Prose fields — normalise whitespace inside each paragraph
    for f in PROSE_FIELDS:
        val = raw.get(f, "")
        if not val:
            continue
        # Collapse each logical line: join continuation fragments into paragraphs
        lines = val.splitlines()
        # Re-join lines that are continuations of the same sentence
        para_lines = []
        for ln in lines:
            stripped = ln.strip()
            if not stripped:
                para_lines.append("")  # blank = paragraph break
            else:
                if para_lines and para_lines[-1] and not para_lines[-1].endswith("\n"):
                    # Decide: join or keep as new line.
                    # Keep separate if previous ends with sentence-ending punctuation
                    prev = para_lines[-1]
                    if prev.endswith((".", ":", "—", "-", "/")):
                        para_lines.append(stripped)
                    else:
                        # Continuation of same sentence — join with space
                        para_lines[-1] = prev + " " + stripped
                else:
                    para_lines.append(stripped)
        # Remove trailing blank lines
        while para_lines and not para_lines[-1]:
            para_lines.pop()
        normalized = "\n".join(para_lines).strip()
        if normalized:
            entry[f] = normalized

    # Groups from Section B
    groups = idx_b.get(wnum)
    if groups:
        entry["groups"] = groups

    return entry


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if OUT_YAML.exists():
        print(f"ERROR: {OUT_YAML} already exists. Delete it first to re-run migration.")
        sys.exit(1)

    # 1. Parse index.md
    index_text = INDEX_MD.read_text(encoding="utf-8")
    idx_a = parse_index_a(index_text)
    idx_b = parse_index_b(index_text)
    print(f"index.md  — Section A: {len(idx_a)} entries, Section B: {len(idx_b)} grouped entries")

    # 2. Parse source files
    all_raw: dict = {}
    for src in SOURCE_FILES:
        parsed = parse_source_file(src)
        all_raw.update(parsed)
        print(f"{src.name} — {len(parsed)} entries parsed")

    # 3. Union of all known W-numbers, sorted
    all_wnums = sorted(set(list(all_raw.keys()) + list(idx_a.keys())))

    # 4. Assemble entries
    entries = [assemble(w, all_raw.get(w, {}), idx_a, idx_b) for w in all_wnums]

    # 5. Emit YAML
    header = """\
# registry/entries.yaml
# Canonical derived-compound word registry for Tonesu.
#
# This is the single source of truth. Edit here; regenerate artifacts with:
#   python scripts/generate_registry_md.py   → registry/derived/w*.md + index.md
#   python scripts/build_registry.py         → www/docs/tonesu/registry/ pages
#
# Status values: active | pending | proposed | cold | retired
# W-numbers are permanent identifiers — never renumber or reuse.

"""
    body = yaml.dump(
        {"entries": entries},
        Dumper=_WideDumper,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        indent=2,
    )

    OUT_YAML.write_text(header + body, encoding="utf-8")
    print(f"\nWrote {len(entries)} entries → {OUT_YAML.relative_to(REPO)}")

    # Quick sanity check
    active  = sum(1 for e in entries if e["status"] == "active")
    pending = sum(1 for e in entries if e["status"] == "pending")
    proposed = sum(1 for e in entries if e["status"] == "proposed")
    retired = sum(1 for e in entries if e["status"] == "retired")
    print(f"  active={active}  pending={pending}  proposed={proposed}  retired={retired}")


if __name__ == "__main__":
    main()
