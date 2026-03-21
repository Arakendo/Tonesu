#!/usr/bin/env python3
"""
extract_conversations.py — Extract conversations.yaml from c*-plus.md intake files.

Reads corpus/conversations/c*-plus.md (current intake files).
Preserves frozen entries (c001-c004.md, c005-c007.md) unchanged.
Preserves computed fields (words_attested, first_attests) from existing YAML.

Mirrors the design of extract_sentences.py:
  - Only intake files (matching c*-plus.md) are re-parsed
  - Existing entries from legacy files are kept verbatim
  - Merge key: cnum
"""
import re
import sys
import yaml
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONV_DIR = REPO / "corpus" / "conversations"
CONV_YAML = REPO / "corpus" / "conversations.yaml"

sys.stdout.reconfigure(encoding="utf-8")

# ── YAML serialiser ────────────────────────────────────────────────────────────

class _WideDumper(yaml.Dumper):
    pass

_WideDumper.add_representer(
    str,
    lambda dumper, data: (
        dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
        if "\n" in data
        else dumper.represent_scalar("tag:yaml.org,2002:str", data)
    ),
)

def _dump(data: object) -> str:
    return yaml.dump(
        data,
        Dumper=_WideDumper,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=2**30,
    )

# ── Helpers ────────────────────────────────────────────────────────────────────

_RE_CONV_HEADER = re.compile(
    r"^\*\*(?P<cnum>C\d{3})\s+—\s+(?P<gloss>.+?)\*\*\s*$"
)
_RE_TURN_HEADER = re.compile(
    r"^\*\*Turn\s+(?P<turn>[A-Z]\d+)(?:\s+—\s+(?P<subtitle>.+?))?\*\*\s*$"
)


def _strip_italic(text: str) -> str:
    """Remove surrounding * or _ italic markers."""
    text = text.strip()
    if text.startswith("*") and text.endswith("*"):
        return text[1:-1].strip()
    return text


def _parse_scene_tests(lines: list[str]) -> tuple[str, list[str]]:
    """
    From lines between conversation header and first turn header,
    extract scene (string) and tests (list of strings).

    Scene: italic paragraph starting with *Scene:
    Tests: italic paragraph starting with *Tests:
    """
    full_text = "\n".join(lines)

    # Scene — everything from *Scene: up to closing *
    scene = ""
    m = re.search(r"\*Scene:\s*(.*?)\*(?:\n|$)", full_text, re.DOTALL)
    if m:
        raw = m.group(1).strip()
        # Collapse continuation lines
        scene = " ".join(ln.strip() for ln in raw.splitlines() if ln.strip())

    # Tests — everything from *Tests: up to closing *
    tests: list[str] = []
    m = re.search(r"\*Tests:\s*(.*?)\*(?:\n|$)", full_text, re.DOTALL)
    if m:
        raw = m.group(1).strip()
        flat = " ".join(ln.strip() for ln in raw.splitlines() if ln.strip())
        # Split on "; " or ", " but preserve backtick-wrapped items
        # Simple approach: split on "; " first then ", "
        parts = re.split(r";\s*", flat)
        result: list[str] = []
        for part in parts:
            result.extend(p.strip() for p in re.split(r",\s*(?![^`]*`)", part) if p.strip())
        tests = result

    return scene, tests


def _parse_code_block(block_lines: list[str]) -> dict:
    """
    Parse the fenced code block inside a turn and return a dict with
    'tonesu', 'gloss_line', 'natural'.

    Code block format (lines inside the ```, no fences):
      Gloss:    <tonesu notation>
      Literal:  <gloss line>
      Natural:  <fluent English>

    Multi-line values: continuation lines are indented (start with whitespace,
    no label prefix).
    """
    result = {"tonesu": "", "gloss_line": "", "natural": ""}
    _LABELS = {
        "Gloss:": "tonesu",
        "Literal:": "gloss_line",
        "Natural:": "natural",
    }
    current_key: str | None = None
    current_val: list[str] = []

    def _flush() -> None:
        if current_key:
            joined = "\n".join(current_val).strip()
            result[current_key] = joined

    for raw in block_lines:
        # Try to match a known label at the start of the line
        matched = False
        for label, key in _LABELS.items():
            if raw.lstrip().startswith(label):
                _flush()
                current_key = key
                current_val = [raw.lstrip()[len(label):].strip()]
                matched = True
                break
        if not matched:
            # Continuation line
            stripped = raw.strip()
            if stripped and current_key:
                current_val.append(stripped)

    _flush()
    return result


def _collect_notes(lines: list[str]) -> str | None:
    """
    From a turn's trailing lines (after the code block), extract the
    **Notes:** section as a single string. Returns None if absent.

    Stops at a standalone '---' separator (which marks the boundary
    between turn notes and the next turn or conversation-level sections).
    """
    in_notes = False
    note_lines: list[str] = []
    for line in lines:
        stripped = line.strip()
        if re.match(r"^\*\*Notes:\*\*", stripped):
            in_notes = True
            rest = stripped[len("**Notes:**"):].strip()
            if rest:
                note_lines.append(rest)
            continue
        if in_notes:
            if stripped == "---":
                break  # stop at section separator
            note_lines.append(line.rstrip())
    if not note_lines:
        return None
    # Trim trailing blank lines
    while note_lines and not note_lines[-1].strip():
        note_lines.pop()
    return "\n".join(note_lines) if note_lines else None


# ── Main parser ────────────────────────────────────────────────────────────────

def _parse_intake_file(path: Path) -> list[dict]:
    """
    Parse a c*-plus.md intake file and return a list of conversation dicts.
    """
    source_file = f"conversations/{path.name}"
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    conversations: list[dict] = []
    current_conv: dict | None = None
    current_conv_turns: list[dict] = []  # built separately, appended last
    current_turn: dict | None = None
    header_lines: list[str] = []   # lines between conv header and first turn
    turn_lines: list[str] = []     # lines within a turn (after header)
    in_code_block = False
    code_lines: list[str] = []

    def _close_turn() -> None:
        nonlocal current_turn, turn_lines, code_lines
        if current_turn is None:
            return
        # Code block should already be parsed inline; fall back if not
        if current_turn.get("tonesu") is None and code_lines:
            parsed = _parse_code_block(code_lines)
            current_turn.update(parsed)
        notes = _collect_notes(turn_lines)
        current_turn["notes"] = notes
        current_conv_turns.append(current_turn)
        current_turn = None
        turn_lines = []
        code_lines = []

    def _close_conv() -> None:
        nonlocal current_conv, current_conv_turns, header_lines
        if current_conv is None:
            return
        _close_turn()
        scene, tests = _parse_scene_tests(header_lines)
        # Build the final conv dict with turns LAST (canonical field order)
        current_conv["scene"] = scene
        current_conv["tests"] = tests
        current_conv["status"] = "normative"
        current_conv["source_file"] = source_file
        current_conv["turns"] = current_conv_turns
        conversations.append(current_conv)
        current_conv = None  # type: ignore[assignment]
        current_conv_turns = []
        header_lines = []

    for line in lines:
        stripped = line.strip()

        # ── Code fence toggle ──
        if stripped.startswith("```"):
            if in_code_block:
                # Close code block
                if current_turn is not None:
                    parsed = _parse_code_block(code_lines)
                    current_turn.update(parsed)
                in_code_block = False
                code_lines = []
            else:
                in_code_block = True
            continue

        if in_code_block:
            code_lines.append(line)
            continue

        # ── Conversation header: **CXXX — gloss** ──
        m_conv = _RE_CONV_HEADER.match(stripped)
        if m_conv:
            _close_conv()
            current_conv = {
                "cnum": m_conv.group("cnum"),
                "gloss": m_conv.group("gloss").rstrip("."),
            }
            current_conv_turns = []
            header_lines = []
            continue

        # ── Turn header: **Turn A1** / **Turn A1 — subtitle** ──
        m_turn = _RE_TURN_HEADER.match(stripped)
        if m_turn and current_conv is not None:
            _close_turn()
            current_turn = {
                "turn": m_turn.group("turn"),
                "tonesu": None,  # populated by code block
                "gloss_line": None,
                "natural": None,
                "words_attested": [],
                "first_attests": [],
                "notes": None,
            }
            subtitle = m_turn.group("subtitle")
            if subtitle:
                current_turn["turn_subtitle"] = subtitle.strip()
            turn_lines = []
            continue

        # Accumulate lines
        if current_turn is not None:
            turn_lines.append(line)
        elif current_conv is not None:
            header_lines.append(line)

    # Flush final conversation
    _close_conv()

    return conversations


# ── Merge with existing YAML ───────────────────────────────────────────────────

def _empty_or_null(val: object) -> bool:
    return val is None or val == [] or val == ""


def _merge(
    extracted: list[dict],
    existing_by_cnum: dict[str, dict],
) -> list[dict]:
    """
    For each extracted conversation, preserve computed fields from existing YAML:
    words_attested and first_attests (per turn), and any hand-authored notes
    that the parser might have missed.
    """
    result: list[dict] = []
    for conv in extracted:
        cnum = conv["cnum"]
        existing = existing_by_cnum.get(cnum, {})

        # Build existing turn lookup
        existing_turns: dict[str, dict] = {}
        for t in existing.get("turns", []):
            existing_turns[t.get("turn", "")] = t

        merged_turns: list[dict] = []
        for turn in conv.get("turns", []):
            turn_label = turn.get("turn", "")
            ex_turn = existing_turns.get(turn_label, {})

            # Preserve computed fields
            for field in ("words_attested", "first_attests"):
                if not _empty_or_null(ex_turn.get(field)):
                    turn[field] = ex_turn[field]

            # Preserve hand-authored notes if parser got nothing
            if _empty_or_null(turn.get("notes")) and not _empty_or_null(ex_turn.get("notes")):
                turn["notes"] = ex_turn["notes"]

            merged_turns.append(turn)

        conv["turns"] = merged_turns

        # Preserve any extra top-level fields from existing entry
        # (e.g. hand-authored fields not in the template)
        for key, val in existing.items():
            if key not in conv and key not in ("turns",):
                conv[key] = val

        result.append(conv)

    return result


# ── Entry point ────────────────────────────────────────────────────────────────

def main() -> None:
    # Load existing YAML
    existing_data: dict = {"conversations": []}
    if CONV_YAML.exists():
        existing_data = yaml.safe_load(CONV_YAML.read_text(encoding="utf-8")) or {}

    all_conversations: list[dict] = existing_data.get("conversations", [])

    # Build lookup: cnum → existing entry (all conversations)
    existing_by_cnum: dict[str, dict] = {
        c["cnum"]: c for c in all_conversations if "cnum" in c
    }

    # Identify which cnums come from intake files (c*-plus.md)
    intake_cnums: set[str] = {
        c["cnum"]
        for c in all_conversations
        if "source_file" in c and c["source_file"].endswith("-plus.md")
    }

    # Parse all intake files
    intake_files = sorted(CONV_DIR.glob("c*-plus.md"))
    extracted: list[dict] = []
    for f in intake_files:
        extracted.extend(_parse_intake_file(f))

    extracted_cnums = {c["cnum"] for c in extracted}

    # Merge extracted with existing computed fields
    merged_extracted = _merge(extracted, existing_by_cnum)

    # Result = frozen legacy + merged extracted
    frozen = [c for c in all_conversations if c.get("cnum") not in intake_cnums]
    # Add newly seen cnums (not previously in YAML)
    new_from_md = [c for c in merged_extracted if c["cnum"] not in existing_by_cnum]
    updated = [c for c in merged_extracted if c["cnum"] in existing_by_cnum]

    # Reconstruct in stable order: frozen first (original order), then updated, then new
    frozen_cnums = {c["cnum"] for c in frozen}
    updated_by_cnum = {c["cnum"]: c for c in updated}

    result_conversations: list[dict] = []
    for c in all_conversations:
        cnum = c["cnum"]
        if cnum in frozen_cnums:
            result_conversations.append(c)
        elif cnum in updated_by_cnum:
            result_conversations.append(updated_by_cnum.pop(cnum))
    # Append any new cnums from MD not previously in YAML
    result_conversations.extend(new_from_md)

    n_intake = len(extracted)
    n_frozen = len(frozen)
    n_total = len(result_conversations)

    print(f"Extracted {n_intake} conversations from intake file(s)")
    print(f"Frozen: {n_frozen} conversations from legacy files")
    print(f"Total: {n_total}")

    out: dict = {"conversations": result_conversations}
    CONV_YAML.write_text(
        _dump(out),
        encoding="utf-8",
    )
    print(f"Wrote: {CONV_YAML.relative_to(REPO)}")


if __name__ == "__main__":
    main()
