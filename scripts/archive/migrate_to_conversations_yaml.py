#!/usr/bin/env python3
"""
migrate_to_conversations_yaml.py

Phase 5: Migrate corpus/conversations/c*.md -> corpus/conversations.yaml

Schema (per conversations.yaml design in notes/corpus-yaml-schema-draft.md):

  - cnum: C001
    gloss: "First conversation: backup unit failure"
    scene: "The relay platform, shortly after S027. ..."
    tests:
      - "content question"
      - "copula gap"
    status: normative
    source_file: conversations/c001-c004.md
    turns:
      - turn: A1
        tonesu: "la-mi  pa-re-mu  lo-de  ka-se-past"
        gloss_line: "agent:I  location:backup-unit ..."
        natural: "I found damage in the backup unit."
        words_attested: []
        first_attests: []
        notes: null

Notes:
- All conversations are status=normative (no legacy conversations exist).
- Turn subtitles (e.g. "**Turn A1 — Person-reading...**") are preserved as
  turn_subtitle field only when present.
- Multi-line Gloss:/Natural: values are joined with newline.
- `tests` is parsed from *Tests: ...* lines; comma/semicolon separated.
- `scene` is the full multi-sentence text of the *Scene: ...* block.
- Turn notes stay null (Tier 1 rule: prose stays in .md).

Usage:
  python scripts/migrate_to_conversations_yaml.py
"""

import re
import sys
import yaml
from pathlib import Path

REPO      = Path(__file__).resolve().parent.parent
CONV_DIR  = REPO / "corpus" / "conversations"
OUT_FILE  = REPO / "corpus" / "conversations.yaml"

SOURCE_FILES = [
    "c001-c004.md",
    "c005-c007.md",
    "c008-plus.md",
]

# ── Regex patterns ────────────────────────────────────────────────────────────

# **C001 — Some gloss text**
CONV_HEADER_RE = re.compile(
    r"^\*\*C(\d+)\s*—\s*(.+?)\*\*\s*$"
)

# *Scene: ...*  (may be multi-line up to next blank or *Tests* line)
SCENE_START_RE = re.compile(r"^\*Scene:\s*(.+)")

# *Tests: ...*  (may be multi-line up to close *)
TESTS_START_RE = re.compile(r"^\*Tests:\s*(.+)")

# **Turn A1** or **Turn A1 — Subtitle text**
TURN_HEADER_RE = re.compile(
    r"^\*\*Turn\s+([A-Za-z]\d+)(?:\s*—\s*(.+?))?\*\*\s*$"
)

FENCED_OPEN  = re.compile(r"^```\s*$")
FENCED_CLOSE = re.compile(r"^```\s*$")

GLOSS_RE   = re.compile(r"^Gloss:\s*(.*)")
LITERAL_RE = re.compile(r"^Literal:\s*(.*)")
NATURAL_RE = re.compile(r"^Natural:\s*(.*)")


# ── YAML dumper that avoids line-wrapping ─────────────────────────────────────

class _WideDumper(yaml.Dumper):
    pass

_WideDumper.best_width = 2 ** 30


# ── Helpers ───────────────────────────────────────────────────────────────────

def strip_italic_markers(text: str) -> str:
    """Remove surrounding * from a markdown italic run-on paragraph."""
    text = text.strip()
    if text.startswith("*") and text.endswith("*") and len(text) >= 2:
        text = text[1:-1]
    return text.strip()


def parse_tests(raw: str) -> list:
    """Split *Tests: a; b, c* into a clean list of strings."""
    # Remove trailing * and punctuation
    raw = raw.rstrip("*").rstrip().rstrip(".")
    # Split on semicolons (preferred) or commas
    items = re.split(r";", raw)
    if len(items) == 1:
        items = re.split(r",", raw)
    result = []
    for item in items:
        # Strip whitespace, trailing periods, and inline backtick-codes
        item = item.strip().rstrip(".")
        # Collapse internal whitespace
        item = re.sub(r"\s+", " ", item).strip()
        if item:
            result.append(item)
    return result


def collect_multiline(lines: list, start_idx: int, opening_text: str) -> tuple:
    """
    From `start_idx`, collect continuation lines for a run-on italic block.
    A run-on italic block (*Scene: ... or *Tests: ...) continues until we hit
    a line that ends the block (ends with *) or is blank.
    Returns (full_text, next_line_index).
    """
    text_parts = [opening_text.rstrip("*").rstrip()]
    # Check if the opening line already closes the block
    if opening_text.rstrip().endswith("*"):
        return " ".join(text_parts).strip(), start_idx + 1

    i = start_idx + 1
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            break
        text_parts.append(line.rstrip("*").rstrip())
        if lines[i].rstrip().endswith("*"):
            i += 1
            break
        i += 1
    return " ".join(text_parts).strip(), i


def parse_fenced_block(lines: list, start_idx: int) -> tuple:
    """
    Parse a fenced code block starting at start_idx (the opening ```).
    Returns (tonesu, gloss_line, natural, next_idx).
    """
    tonesu_parts    = []
    gloss_line_parts = []
    natural_parts   = []
    current_field   = None

    i = start_idx + 1  # skip opening ```
    while i < len(lines):
        line = lines[i]
        if FENCED_CLOSE.match(line):
            i += 1
            break

        mg = GLOSS_RE.match(line)
        ml = LITERAL_RE.match(line)
        mn = NATURAL_RE.match(line)

        if mg:
            current_field = "gloss"
            if mg.group(1).strip():
                tonesu_parts.append(mg.group(1).strip())
        elif ml:
            current_field = "literal"
            if ml.group(1).strip():
                gloss_line_parts.append(ml.group(1).strip())
        elif mn:
            current_field = "natural"
            if mn.group(1).strip():
                natural_parts.append(mn.group(1).strip())
        elif line.strip():
            # Continuation of current field
            if current_field == "gloss":
                tonesu_parts.append(line.strip())
            elif current_field == "literal":
                gloss_line_parts.append(line.strip())
            elif current_field == "natural":
                natural_parts.append(line.strip())
        i += 1

    tonesu    = "\n".join(tonesu_parts)    or None
    gloss_line = "\n".join(gloss_line_parts) or None
    natural   = "\n".join(natural_parts)   or None
    return tonesu, gloss_line, natural, i


def parse_file(filepath: Path) -> list:
    """
    Parse a conversations .md file and return a list of conversation dicts.
    """
    text  = filepath.read_text(encoding="utf-8")
    lines = text.splitlines()
    fname = "conversations/" + filepath.name

    conversations = []
    current_conv  = None
    current_turn  = None

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # ── Conversation header ───────────────────────────────────────────────
        mc = CONV_HEADER_RE.match(stripped)
        if mc:
            # Save previous conversation
            if current_conv is not None:
                if current_turn is not None:
                    current_conv["turns"].append(current_turn)
                    current_turn = None
                conversations.append(current_conv)

            cnum = f"C{int(mc.group(1)):03d}"
            current_conv = {
                "cnum":        cnum,
                "gloss":       mc.group(2).strip(),
                "scene":       None,
                "tests":       [],
                "status":      "normative",
                "source_file": fname,
                "turns":       [],
            }
            i += 1
            continue

        # ── Scene line ────────────────────────────────────────────────────────
        if current_conv is not None and current_conv["scene"] is None:
            ms = SCENE_START_RE.match(stripped)
            if ms:
                scene_text, i = collect_multiline(lines, i, ms.group(1))
                current_conv["scene"] = scene_text
                continue

        # ── Tests line ────────────────────────────────────────────────────────
        if current_conv is not None and not current_conv["tests"]:
            mt = TESTS_START_RE.match(stripped)
            if mt:
                tests_text, i = collect_multiline(lines, i, mt.group(1))
                current_conv["tests"] = parse_tests(tests_text)
                continue

        # ── Turn header ───────────────────────────────────────────────────────
        mtu = TURN_HEADER_RE.match(stripped)
        if mtu and current_conv is not None:
            # Save previous turn
            if current_turn is not None:
                current_conv["turns"].append(current_turn)

            turn_id       = mtu.group(1)
            turn_subtitle = mtu.group(2).strip() if mtu.group(2) else None
            current_turn  = {
                "turn":           turn_id,
                "tonesu":         None,
                "gloss_line":     None,
                "natural":        None,
                "words_attested": [],
                "first_attests":  [],
                "notes":          None,
            }
            if turn_subtitle:
                current_turn["turn_subtitle"] = turn_subtitle
            i += 1
            continue

        # ── Fenced block ──────────────────────────────────────────────────────
        if FENCED_OPEN.match(line) and current_turn is not None:
            tonesu, gloss_line, natural, i = parse_fenced_block(lines, i)
            # Merge: a turn may have multiple code blocks (rare).
            if current_turn["tonesu"] is None:
                current_turn["tonesu"]     = tonesu
                current_turn["gloss_line"] = gloss_line
                current_turn["natural"]    = natural
            else:
                # Append continuation block
                if tonesu:
                    current_turn["tonesu"] = (
                        (current_turn["tonesu"] or "") + "\n" + tonesu
                    ).strip()
                if natural:
                    current_turn["natural"] = (
                        (current_turn["natural"] or "") + "\n" + natural
                    ).strip()
            continue

        i += 1

    # Flush last turn and conversation
    if current_turn is not None and current_conv is not None:
        current_conv["turns"].append(current_turn)
    if current_conv is not None:
        conversations.append(current_conv)

    return conversations


def main():
    all_conversations = []
    for fname in SOURCE_FILES:
        fpath = CONV_DIR / fname
        if not fpath.exists():
            print(f"WARNING: {fpath} not found, skipping.")
            continue
        convs = parse_file(fpath)
        print(f"  {fname}: {len(convs)} conversations, "
              f"{sum(len(c['turns']) for c in convs)} turns")
        all_conversations.extend(convs)

    # Summary stats
    total_turns  = sum(len(c["turns"]) for c in all_conversations)
    null_tonesu  = [
        f"{c['cnum']} Turn {t['turn']}"
        for c in all_conversations
        for t in c["turns"]
        if t.get("tonesu") is None
    ]

    print(f"\nTotal conversations: {len(all_conversations)}")
    print(f"Total turns: {total_turns}")
    if null_tonesu:
        print(f"Turns with null tonesu ({len(null_tonesu)}): {null_tonesu[:10]}")
    else:
        print("All turns have tonesu.")

    out_data = {"conversations": all_conversations}
    text = yaml.dump(
        out_data,
        Dumper=_WideDumper,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    )
    OUT_FILE.write_text(text, encoding="utf-8")
    print(f"\nWrote: {OUT_FILE.relative_to(REPO)}")


if __name__ == "__main__":
    main()
