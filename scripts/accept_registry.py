#!/usr/bin/env python3
"""
accept_registry.py

Formal acceptance pass — updates Status fields in registry source files
and the index.md quick-reference.

Run from repo root:
    python scripts/accept_registry.py
"""

import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# W-numbers to formally accept  (Status: pending  →  Status: ✅ active)
# ---------------------------------------------------------------------------
ACCEPT = {
    # ── w001-w050.md ────────────────────────────────────────────────────────
    22, 23, 24, 25, 26, 27,
    33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
    # ── w051-w100.md ────────────────────────────────────────────────────────
    51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
    61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
    71, 72, 73, 74, 75,
    # (W076 skipped — no corpus S-number)
    77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
    # (W090 skipped — explicit "corpus attestation pending" note)
    91, 92, 93, 94, 95, 96, 97, 98, 99,
    # ── w101-plus.md ────────────────────────────────────────────────────────
    102, 103,
    # (W104–W116 skipped — no S-numbers / triage-gated)
    117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130,
    131, 132, 133, 134, 135,
    # (W136 → proposed; W137 → proposed; W138–W149 skipped — Genesis 1,
    #  no S-numbers except W148)
    148,
    # (W149 skipped — Genesis 1, no S-number)
    # EXO-001 batch  S398–S417
    150, 151, 152, 153, 154, 155,
    # (W156 BLOCKED — form collision with W087; see open-questions)
    157, 158, 159, 160,
    # LSP-001 batch  S418–S438
    161, 162, 163, 164, 165, 166, 167, 168,
}

# W-numbers to change to proposed  (Status: pending  →  Status: ⚠️ proposed)
PROPOSE = {136, 137}

SOURCE_FILES = [
    REPO / "registry" / "derived" / "w001-w050.md",
    REPO / "registry" / "derived" / "w051-w100.md",
    REPO / "registry" / "derived" / "w101-plus.md",
]

INDEX_MD = REPO / "registry" / "derived" / "index.md"

# W000 and W100 were already ✅ active before this pass.
ALREADY_ACTIVE = {0, 100}

# ---------------------------------------------------------------------------
# Source-file updater
# ---------------------------------------------------------------------------

def update_source_file(path: Path) -> int:
    """
    Walk the file line-by-line.  Inside each **WXXX** entry's fenced code
    block, replace the Status field for entries in ACCEPT or PROPOSE.
    Returns the number of lines changed.
    """
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    result = []
    changes = 0
    current_wnum = None
    in_code_block = False

    for line in lines:
        # Detect entry header  **WXXX**
        m = re.match(r'^\*\*W(\d+)\*\*\s*$', line.strip())
        if m:
            current_wnum = int(m.group(1))
            in_code_block = False
            result.append(line)
            continue

        # Track fenced code-block boundaries  (``` alone on a line)
        if line.strip() == "```":
            in_code_block = not in_code_block
            result.append(line)
            continue

        # Inside a code block for a known entry — maybe update Status
        if in_code_block and current_wnum is not None:
            if re.match(r'^Status:\s+pending\s*$', line.rstrip()):
                if current_wnum in ACCEPT:
                    line = re.sub(r'^(Status:\s+)pending', r'\1✅ active', line)
                    changes += 1
                elif current_wnum in PROPOSE:
                    line = re.sub(r'^(Status:\s+)pending', r'\1⚠️ proposed', line)
                    changes += 1

        result.append(line)

    path.write_text("".join(result), encoding="utf-8")
    return changes


# ---------------------------------------------------------------------------
# Index.md updater
# ---------------------------------------------------------------------------

def update_index(path: Path) -> int:
    """
    In Section A of index.md, update the St emoji column for entries in
    ACCEPT (⏳ → ✅) and PROPOSE (⏳ → ⚠️).
    Returns the number of rows changed.
    """
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    result = []
    changes = 0
    in_section_a = False

    for line in lines:
        if re.match(r"## A\.", line):
            in_section_a = True
        elif re.match(r"## [B-Z]\.", line):
            in_section_a = False

        if in_section_a and line.startswith("|"):
            # Find W-number in the row
            wnum_match = None
            for cell in line.split("|"):
                m = re.search(r"\bW(\d+)\b", cell)
                if m:
                    wnum_match = int(m.group(1))
                    break

            if wnum_match is not None and "⏳" in line:
                if wnum_match in ACCEPT:
                    line = line.replace("⏳", "✅", 1)
                    changes += 1
                elif wnum_match in PROPOSE:
                    line = line.replace("⏳", "⚠️", 1)
                    changes += 1

        result.append(line)

    path.write_text("".join(result), encoding="utf-8")
    return changes


def update_header_counts(path: Path) -> None:
    """Update the accepted/pending/proposed/retired counts in index.md header."""
    total_entries = 155  # W000–W168 inclusive, minus gaps = 155 total entries
    accepted  = len(ACCEPT) + len(ALREADY_ACTIVE)   # 110 + 2 = 112
    proposed  = len(PROPOSE)                         # 2
    retired   = 2                                    # W111, W112
    pending   = total_entries - accepted - proposed - retired  # 39

    text = path.read_text(encoding="utf-8")
    # Replace the summary line: "accepted: N · pending: N"
    new_text = re.sub(
        r"accepted: \d+\s*·\s*pending: \d+",
        f"accepted: {accepted} · proposed: {proposed} · pending: {pending} · retired: {retired}",
        text,
    )
    path.write_text(new_text, encoding="utf-8")
    print(
        f"index.md header: accepted={accepted}, proposed={proposed}, "
        f"pending={pending}, retired={retired}"
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print(f"ACCEPT set: {len(ACCEPT)} entries")
    print(f"PROPOSE set: {len(PROPOSE)} entries\n")

    total_source_changes = 0
    for f in SOURCE_FILES:
        n = update_source_file(f)
        print(f"  {f.name}: {n} Status lines updated")
        total_source_changes += n

    print()
    n_index = update_index(INDEX_MD)
    print(f"  index.md: {n_index} St emoji updated")

    print()
    update_header_counts(INDEX_MD)

    print(f"\nDone. Total source-file changes: {total_source_changes}")
