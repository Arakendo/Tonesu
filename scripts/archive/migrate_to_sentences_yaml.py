#!/usr/bin/env python3
"""
migrate_to_sentences_yaml.py

One-time migration: parses all corpus/sentences/s*.md files and produces
corpus/sentences.yaml (Tier 1 thin index).

Run from repo root:
    python scripts/migrate_to_sentences_yaml.py

Output fields per entry:
    snum, gloss, batch, batch_sub, status, tonesu,
    gloss_line, natural, words_attested (empty), first_attests (empty),
    gap_refs (auto-extracted), source_file, source_anchor, notes (null)

See notes/corpus-yaml-schema-draft.md for field definitions.
"""

import re
import sys
import yaml
from pathlib import Path

REPO          = Path(__file__).resolve().parent.parent
SENTENCES_DIR = REPO / "corpus" / "sentences"
OUT_FILE      = REPO / "corpus" / "sentences.yaml"

# S001–S039 are legacy (English-placeholder Tonesu, pre-development era).
# Status is assigned per entry by S-number (<= 39 → legacy), not by source file.
# Note: s001-s039.md also physically contains S114–S131 entries (corpus org issue);
# those get normative status because their S-numbers are > 39.
LEGACY_THRESHOLD = 39

# Analytical entries intentionally without a canonical Tonesu sentence.
# tonesu: null is expected here; suppress the missing-tonesu warning for these.
KNOWN_NO_TONESU = {"S390", "S488", "S586"}

# Canonical processing order (S-number order)
SENTENCE_FILES = [
    "s001-s039.md",
    "s040-s071.md",
    "s072-s100.md",
    "s101-s175.md",
    "s176-s227.md",
    "s228-s251.md",
    "s252-s278.md",
    "s279-s334.md",
    "s335-s397.md",
    "s398-plus.md",
]


# ---------------------------------------------------------------------------
# Wide YAML dumper — no mid-string wrapping
# ---------------------------------------------------------------------------

class _WideDumper(yaml.Dumper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.best_width = 2 ** 30


def _str_representer(dumper, data):
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


_WideDumper.add_representer(str, _str_representer)


# ---------------------------------------------------------------------------
# Regex patterns
# ---------------------------------------------------------------------------

# Matches: **S001 — Some gloss text** *(BATCH-001-A)*
# Group 1: S-number digits
# Group 2: gloss text (between — and closing **)
# Group 3: batch code inside *(...)* (optional)
# Only em-dash (—) separates S-number from gloss in real entry headers.
# Section summary headers use en-dash (–) for ranges like **S114–S125 Summary**
# and must NOT match.
HEADER_RE = re.compile(
    r"^\*\*S(\d+)\s*—\s*(.*?)\*\*(?:\s*\*\(([^)]*)\)\*)?",
    re.MULTILINE,
)

# Fenced code block content
FENCED_RE = re.compile(r"```[^\n]*\n(.*?)\n```", re.DOTALL)

# Inline Notation: field (TAO-001 style — no fenced block, uses backtick-enclosed inline)
NOTATION_RE = re.compile(r"^Notation:\s+`([^`]+)`", re.MULTILINE)

# Batch code embedded at end of gloss in plain parens (TAO-001 style: "...(TAO-001-A)")
BATCH_IN_GLOSS_RE = re.compile(r"\s*\(([A-Z]{2,}-\d+(?:-[A-Z])?)\)\s*$")

# Labeled field lines inside old/middle fenced blocks: "Gloss:    ...", "Literal:  ..."
LABELED_FIELD_RE = re.compile(r"^(Gloss|Literal|Natural|Notes):\s+(.*)", re.IGNORECASE)

# GAP-xxx and OQ-xxx references in notes text
GAP_REF_RE = re.compile(r"\b(GAP-[A-Z0-9][A-Z0-9-]*|OQ-[A-Z0-9][A-Z0-9-]*)\b")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def parse_batch_code(raw: str) -> tuple[str | None, str | None]:
    """
    Parse a raw batch code string into (batch, batch_sub).

    Examples:
        'EXO-001-A'  → ('EXO-001', 'A')
        'GRM-001'    → ('GRM-001', None)
        'T-XX-001'   → ('T-XX-001', None)
        ''           → (None, None)
    """
    raw = (raw or "").strip()
    if not raw:
        return None, None
    # A batch sub-label is a single uppercase letter at the very end after a dash
    m = re.match(r"^(.+)-([A-Z])$", raw)
    if m:
        return m.group(1), m.group(2)
    return raw, None


def extract_labeled_fields(fenced_text: str) -> dict:
    """
    Extract Gloss:/Literal:/Natural:/Notes: fields from old/middle format fenced block.

    Returns a dict with lowercase keys: gloss, literal, natural, notes.
    Multi-line continuations (indented lines after a labeled line) are joined.
    """
    result: dict = {}
    current_key: str | None = None
    current_lines: list = []

    for line in fenced_text.splitlines():
        m = LABELED_FIELD_RE.match(line)
        if m:
            if current_key is not None:
                result[current_key] = " ".join(l for l in current_lines if l).strip()
            current_key = m.group(1).lower()
            current_lines = [m.group(2).rstrip()]
        elif current_key is not None:
            current_lines.append(line.rstrip())

    if current_key is not None:
        result[current_key] = " ".join(l for l in current_lines if l).strip()

    return result


# ---------------------------------------------------------------------------
# Entry parser
# ---------------------------------------------------------------------------

def parse_entry(block: str, source_filename: str) -> dict | None:
    """Parse a single sentence block (from one **S### header to the next) into a dict."""
    header_match = HEADER_RE.search(block)
    if not header_match:
        return None

    snum_int = int(header_match.group(1))
    snum     = f"S{snum_int:03d}"
    gloss    = header_match.group(2).strip().strip('"').strip()
    batch, batch_sub = parse_batch_code(header_match.group(3))

    # Fallback: batch code embedded in gloss as trailing plain parens (TAO-001 style)
    if batch is None:
        m = BATCH_IN_GLOSS_RE.search(gloss)
        if m:
            batch, batch_sub = parse_batch_code(m.group(1))
            gloss = gloss[:m.start()].strip().strip('"').strip()

    # Find fenced block
    fenced_match = FENCED_RE.search(block)
    tonesu     = None
    gloss_line = None
    natural    = None
    notes_inline = ""

    if fenced_match:
        fenced = fenced_match.group(1)
        fields = extract_labeled_fields(fenced)

        if fields.get("gloss"):
            # Old format (Notes inside) or middle format (Notes outside):
            # fenced block contains Gloss:/Literal:/Natural: labeled fields
            tonesu     = fields["gloss"].strip() or None
            gloss_line = fields.get("literal", "").strip() or None
            natural    = fields.get("natural", "").strip() or None
            notes_inline = fields.get("notes", "")
        else:
            # Flat format (S398+): fenced block contains raw Tonesu sentence only
            tonesu = fenced.strip() or None

    # Fallback: Notation: `...` inline format (TAO-001 style — no fenced block)
    if tonesu is None:
        notation_match = NOTATION_RE.search(block)
        if notation_match:
            tonesu = notation_match.group(1).strip() or None

    # Collect notes text from outside-block **Notes:** section (middle + flat formats)
    notes_text = notes_inline
    outside_match = re.search(r"\*\*Notes:\*\*\s*(.*?)(?=\n---\n|\Z)", block, re.DOTALL)
    if outside_match:
        notes_text += "\n" + outside_match.group(1)

    # Extract GAP-xxx / OQ-xxx references from all notes text
    gap_refs = sorted(set(GAP_REF_RE.findall(notes_text)))

    return {
        "snum":           snum,
        "gloss":          gloss,
        "batch":          batch,
        "batch_sub":      batch_sub,
        "status":         "legacy" if snum_int <= LEGACY_THRESHOLD else "normative",
        "tonesu":         tonesu,
        "gloss_line":     gloss_line,
        "natural":        natural,
        "words_attested": [],
        "first_attests":  [],
        "gap_refs":       gap_refs,
        "source_file":    f"sentences/{source_filename}",
        "source_anchor":  snum,
        "notes":          None,
    }


# ---------------------------------------------------------------------------
# File parser
# ---------------------------------------------------------------------------

def parse_file(filename: str) -> list:
    path = SENTENCES_DIR / filename
    if not path.exists():
        print(f"  WARNING: {filename} not found, skipping")
        return []

    text = path.read_text(encoding="utf-8")

    # Locate all sentence header positions
    positions = [m.start() for m in HEADER_RE.finditer(text)]
    if not positions:
        print(f"  WARNING: no entries found in {filename}")
        return []

    entries = []
    for i, pos in enumerate(positions):
        end   = positions[i + 1] if i + 1 < len(positions) else len(text)
        block = text[pos:end]
        entry = parse_entry(block, filename)
        if entry:
            entries.append(entry)

    return entries


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    if OUT_FILE.exists():
        print(f"Output file already exists: {OUT_FILE.relative_to(REPO)}")
        print("Delete it first if you want to regenerate.")
        sys.exit(1)

    all_entries: list = []
    for fname in SENTENCE_FILES:
        entries = parse_file(fname)
        print(f"  {fname}: {len(entries)} entries")
        all_entries.extend(entries)

    # Sort by S-number, deduplicate
    all_entries.sort(key=lambda e: int(e["snum"][1:]))
    seen: set = set()
    deduped = []
    for e in all_entries:
        if e["snum"] not in seen:
            seen.add(e["snum"])
            deduped.append(e)

    if len(deduped) < len(all_entries):
        print(f"  (deduplicated {len(all_entries) - len(deduped)} duplicate headers)")

    print(f"\nTotal: {len(deduped)} sentences")

    # Status summary
    by_status: dict = {}
    for e in deduped:
        by_status[e["status"]] = by_status.get(e["status"], 0) + 1
    for k in sorted(by_status):
        print(f"  {k}: {by_status[k]}")

    # GAP ref summary
    with_gaps = [e["snum"] for e in deduped if e["gap_refs"]]
    print(f"  gap_refs populated: {len(with_gaps)} sentences")

    # Missing tonesu warning (suppress known analytical entries)
    missing_unexpected = [e["snum"] for e in deduped if not e["tonesu"] and e["snum"] not in KNOWN_NO_TONESU]
    missing_expected   = [e["snum"] for e in deduped if not e["tonesu"] and e["snum"] in KNOWN_NO_TONESU]
    if missing_expected:
        print(f"  tonesu null (expected — analytical entries): {', '.join(missing_expected)}")
    if missing_unexpected:
        print(f"\nWARNING: tonesu unexpectedly missing in {len(missing_unexpected)} entries:")
        print(f"  {', '.join(missing_unexpected[:20])}{'...' if len(missing_unexpected) > 20 else ''}")

    # Write YAML
    data = {"sentences": deduped}
    OUT_FILE.write_text(
        yaml.dump(
            data,
            Dumper=_WideDumper,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    print(f"\nWritten: {OUT_FILE.relative_to(REPO)}")


if __name__ == "__main__":
    main()
