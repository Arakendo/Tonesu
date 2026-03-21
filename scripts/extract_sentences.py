#!/usr/bin/env python3
"""
extract_sentences.py — Extract sentences from v4-current markdown → sentences.yaml

Reads v4-current/*.md sentence files, extracts sentence records, merges with
existing v1/v2/v3 entries from sentences.yaml, and writes the updated YAML.

v1/v2/v3 entries are preserved as-is (frozen).  v4 entries are re-extracted on
each run.  Computed fields (words_attested, first_attests) are left empty for
re-derivation by downstream pipeline steps (annotate_words_attested.py,
derive_first_attests.py).

Hand-populated fields (gap_refs, gloss_line) are preserved from the existing
YAML when the extraction does not find them in the markdown source.

Run from repo root:
    python scripts/extract_sentences.py
    python scripts/extract_sentences.py --dry-run
"""

import re
import sys
import yaml
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
V4_DIR = REPO / "corpus" / "sentences" / "v4-current"
SENT_YAML = REPO / "corpus" / "sentences.yaml"

sys.stdout.reconfigure(encoding="utf-8")


# ── YAML formatting (matches annotate_words_attested.py) ─────────────────────

class _WideDumper(yaml.Dumper):
    pass

_WideDumper.best_width = 2 ** 30


# ── Patterns ─────────────────────────────────────────────────────────────────

# Batch-code + sub-label: EXO-001-A → (EXO-001, A)
_RE_BATCH_SUB = re.compile(r"^([A-Za-z]+-\d+)-([A-Z])$")

# Batch code from ## heading:  "— Batch: CODE"  |  "## CODE: ..."  |  "## CODE — ..."
_RE_HEADING_BATCH_EXPLICIT = re.compile(r"—\s*Batch:\s*([A-Za-z]+-\d+)")
_RE_HEADING_BATCH_PREFIX = re.compile(r"^##\s+([A-Za-z]+-\d+)\s*[:\s—]")
# Batch code from purpose line:  *Batch purpose (CODE): ...*
_RE_PURPOSE_BATCH = re.compile(r"^\*Batch purpose\s*\(([^)]+)\)")

# ### heading: ### S659 — CKG-001-A
_RE_SENT_H3 = re.compile(r"^###\s+S(\d+)\s*[—–-]\s*(.+)")


# ── Parsing helpers ──────────────────────────────────────────────────────────

def _split_batch(code: str):
    """Split 'EXO-001-A' → ('EXO-001', 'A').  Returns (code, None) if no sub."""
    m = _RE_BATCH_SUB.match(code)
    if m:
        return m.group(1), m.group(2)
    return code, None


def _extract_batch_from_heading(line: str) -> str | None:
    """Try to extract a batch code from a ## heading line."""
    m = _RE_HEADING_BATCH_EXPLICIT.search(line)
    if m:
        return m.group(1)
    m = _RE_HEADING_BATCH_PREFIX.match(line)
    if m:
        return m.group(1)
    return None


def _match_sentence_header(line: str):
    """Try to parse a sentence heading.

    Returns (snum, gloss, batch, batch_sub) or None.
    Handles three format variants:
      A) **S### — gloss text** *(CODE-SUB)*            (standard)
      B) **S### — gloss text (CODE-SUB)**              (code inside bold)
      C) ### S### — CODE-SUB                           (h3 format, e.g. CKG-001)
    """
    # ── Format C: ### heading ──
    m = _RE_SENT_H3.match(line)
    if m:
        snum = f"S{m.group(1)}"
        text = m.group(2).strip()
        bm = _RE_BATCH_SUB.match(text)
        if bm:
            return snum, None, bm.group(1), bm.group(2)
        return snum, text, None, None

    # ── Formats A & B: bold **S### — ...** ──
    if not line.startswith("**S"):
        return None
    m = re.match(r"^\*\*S(\d+)\s*[—–-]\s*", line)
    if not m:
        return None

    snum = f"S{m.group(1)}"
    rest = line[m.end():]

    # Check for trailing *(CODE...)*  after the closing **
    trailing = re.search(r"\*\(([^)]+)\)\*\s*$", rest)
    if trailing:
        before = rest[: trailing.start()].rstrip()
        code_text = trailing.group(1).strip()
    else:
        before = rest.rstrip()
        code_text = None

    # Strip the closing **
    if before.endswith("**"):
        gloss = before[:-2].strip()
    else:
        gloss = before.strip()

    batch, batch_sub = None, None

    # Try to get batch from trailing *(CODE-SUB ...)*
    if code_text:
        cm = re.match(r"([A-Za-z]+-\d+-[A-Z])", code_text)
        if cm:
            batch, batch_sub = _split_batch(cm.group(1))

    # If no batch from trailing, check for (CODE-SUB) at the end of gloss
    if not batch:
        cm = re.search(r"\(([A-Za-z]+-\d+-[A-Z])\)\s*$", gloss)
        if cm:
            batch, batch_sub = _split_batch(cm.group(1))
            gloss = gloss[: cm.start()].strip()

    return snum, gloss, batch, batch_sub


def _is_block_end(line: str) -> bool:
    """True if line marks the end of a sentence block (next entry or section)."""
    if line.startswith("## "):
        return True
    if line.startswith("### S") and re.match(r"^### S\d+", line):
        return True
    if line.startswith("**S") and re.match(r"^\*\*S\d+\s*[—–-]", line):
        return True
    return False


def _starts_field(line: str) -> str | None:
    """If line starts a known field, return the field name.  Otherwise None."""
    for prefix in ("**Written:**", "Written:"):
        if line.startswith(prefix):
            return "written"
    if line.startswith("**Natural reading:**"):
        return "natural"
    if line.startswith("**Gloss:**"):
        return "gloss_line"
    if line.startswith("**Notes:**"):
        return "notes"
    if line.startswith("Notation:"):
        return "notation"
    return None


def _strip_field_prefix(line: str, field: str) -> str:
    """Strip the field prefix from a line."""
    prefixes = {
        "written": ("**Written:**", "Written:"),
        "natural": ("**Natural reading:**",),
        "gloss_line": ("**Gloss:**",),
        "notes": ("**Notes:**",),
        "notation": ("Notation:",),
    }
    for p in prefixes.get(field, ()):
        if line.startswith(p):
            return line[len(p):].strip()
    return line.strip()


def _parse_body(lines: list[str], start: int):
    """Parse sentence body from `start`.  Returns (fields_dict, next_line_index)."""
    tonesu = None
    written = None
    natural = None
    gloss_line = None
    notes_parts: list[str] = []

    in_code = False
    code_buf: list[str] = []
    in_notes = False
    i = start

    while i < len(lines):
        raw = lines[i]
        line = raw.rstrip()

        # ── block terminator (outside code fence) ──
        if not in_code:
            if _is_block_end(line):
                break
            if line.strip() == "---":
                i += 1
                break

        # ── code fence toggle ──
        if line.strip().startswith("```"):
            if not in_code:
                in_code = True
                in_notes = False
            else:
                in_code = False
                if code_buf and tonesu is None:
                    tonesu = "\n".join(code_buf).strip()
                code_buf = []
            i += 1
            continue

        if in_code:
            code_buf.append(line)
            i += 1
            continue

        # ── field detection ──
        field = _starts_field(line)

        if field == "written":
            in_notes = False
            text = _strip_field_prefix(line, "written").strip("`")
            written = text or None
            i += 1
            continue

        if field == "natural":
            in_notes = False
            parts = [_strip_field_prefix(line, "natural")]
            while i + 1 < len(lines):
                nxt = lines[i + 1].rstrip()
                if (
                    not nxt.strip()
                    or nxt.startswith("**")
                    or nxt.startswith("---")
                    or nxt.startswith("## ")
                    or nxt.startswith("### ")
                    or nxt.startswith("```")
                    or _starts_field(nxt)
                ):
                    break
                i += 1
                parts.append(nxt.strip())
            natural = " ".join(parts).strip() or None
            i += 1
            continue

        if field == "gloss_line":
            in_notes = False
            gloss_line = _strip_field_prefix(line, "gloss_line") or None
            i += 1
            continue

        if field == "notation":
            in_notes = False
            text = _strip_field_prefix(line, "notation").strip("`")
            if tonesu is None:
                tonesu = text or None
            i += 1
            continue

        if field == "notes":
            in_notes = True
            notes_parts = []
            first = _strip_field_prefix(line, "notes")
            if first:
                notes_parts.append(first)
            i += 1
            continue

        # ── notes continuation ──
        if in_notes:
            notes_parts.append(line)
            i += 1
            continue

        i += 1

    # ── collapse notes into a single string ──
    notes = _collapse_notes(notes_parts)

    fields = {
        "tonesu": tonesu,
        "written": written,
        "natural": natural,
        "gloss_line": gloss_line,
        "notes": notes,
    }
    return fields, i


def _collapse_notes(parts: list[str]) -> str | None:
    """Join multi-line notes into a single string, preserving paragraph breaks."""
    if not parts:
        return None
    # Join lines, collapsing single-line wraps but keeping intentional paragraph breaks
    collapsed: list[str] = []
    for p in parts:
        stripped = p.strip()
        if stripped:
            collapsed.append(stripped)
        elif collapsed and collapsed[-1] != "":
            collapsed.append("")  # paragraph break marker

    # Remove trailing blank markers
    while collapsed and collapsed[-1] == "":
        collapsed.pop()

    text = " ".join(seg for seg in collapsed if seg)
    return text.strip() or None


# ── Main extraction ──────────────────────────────────────────────────────────

def extract_v4(v4_dir: Path) -> list[dict]:
    """Parse all v4-current sentence files and return sentence records."""
    sentences = []
    for md in sorted(v4_dir.glob("s*.md")):
        text = md.read_text(encoding="utf-8")
        lines = text.split("\n")
        i = 0

        # Batch context tracking
        ctx_batch: str | None = None      # current batch from ## heading
        ctx_batch_counter: int = 0         # positional counter within batch

        while i < len(lines):
            line = lines[i].rstrip()

            # ── Track batch context from ## headings ──
            if line.startswith("## "):
                b = _extract_batch_from_heading(line)
                if b:
                    ctx_batch = b
                    ctx_batch_counter = 0
                # Also check next few lines for *Batch purpose (CODE):*
                elif not b:
                    for j in range(1, 5):
                        if i + j >= len(lines):
                            break
                        pm = _RE_PURPOSE_BATCH.match(lines[i + j].strip())
                        if pm:
                            ctx_batch = pm.group(1)
                            ctx_batch_counter = 0
                            break
                i += 1
                continue

            sent = _match_sentence_header(line)
            if sent:
                snum, gloss, batch, batch_sub = sent
                fields, end_i = _parse_body(lines, i + 1)

                # If heading had no batch code, inherit from section context
                if not batch and ctx_batch:
                    batch = ctx_batch
                    ctx_batch_counter += 1
                    batch_sub = chr(ord("A") + ctx_batch_counter - 1)
                elif batch:
                    # Reset context to match this entry's batch
                    base, _ = _split_batch(batch + "-" + (batch_sub or "A"))
                    if base != ctx_batch:
                        ctx_batch = batch
                        ctx_batch_counter = 0

                # If heading had no English gloss, fall back to natural reading
                if gloss is None:
                    gloss = fields["natural"] or ""

                sentences.append({
                    "snum": snum,
                    "gloss": gloss,
                    "batch": batch,
                    "batch_sub": batch_sub,
                    "status": "normative",
                    "tonesu": fields["tonesu"] or "",
                    "gloss_line": fields["gloss_line"],
                    "natural": fields["natural"] or gloss,
                    "words_attested": [],
                    "first_attests": [],
                    "gap_refs": [],
                    "source_file": f"sentences/v4-current/{md.name}",
                    "source_anchor": snum,
                    "notes": fields["notes"],
                })
                i = end_i
            else:
                i += 1
    return sentences


def main() -> None:
    dry_run = "--dry-run" in sys.argv

    # ── Load existing YAML ──
    if SENT_YAML.exists():
        data = yaml.safe_load(SENT_YAML.read_text(encoding="utf-8"))
        existing = data.get("sentences", [])
    else:
        existing = []

    # Split into frozen (v1/v2/v3) and v4
    frozen = [
        s for s in existing
        if not s.get("source_file", "").startswith("sentences/v4")
    ]
    v4_old = {
        s["snum"]: s for s in existing
        if s.get("source_file", "").startswith("sentences/v4")
    }

    # ── Extract from v4 markdown ──
    v4_new = extract_v4(V4_DIR)
    print(f"Extracted {len(v4_new)} sentences from v4-current")

    # ── Merge: preserve hand-populated fields from old YAML ──
    for s in v4_new:
        old = v4_old.get(s["snum"])
        if old:
            # Preserve gap_refs if extraction didn't find any
            if not s["gap_refs"] and old.get("gap_refs"):
                s["gap_refs"] = old["gap_refs"]
            # Preserve gloss_line if extraction didn't find one
            if not s["gloss_line"] and old.get("gloss_line"):
                s["gloss_line"] = old["gloss_line"]

    # ── Combine and sort by S-number ──
    all_sentences = frozen + v4_new
    all_sentences.sort(key=lambda s: int(s["snum"][1:]))

    print(f"Total: {len(all_sentences)} ({len(frozen)} frozen + {len(v4_new)} v4)")

    # ── Diagnostics ──
    seen: set[str] = set()
    for s in all_sentences:
        if s["snum"] in seen:
            print(f"  WARNING: duplicate {s['snum']}")
        seen.add(s["snum"])

    old_snums = {s["snum"] for s in existing}
    new_snums = {s["snum"] for s in all_sentences}
    missing = sorted(old_snums - new_snums, key=lambda x: int(x[1:]))
    added = sorted(new_snums - old_snums, key=lambda x: int(x[1:]))
    if missing:
        print(f"  WARNING: missing from extraction: {missing}")
    if added:
        print(f"  New: {added}")

    if dry_run:
        print("\n[dry-run] No files written.")
        return

    # ── Write ──
    out = {"sentences": all_sentences}
    text = yaml.dump(
        out,
        Dumper=_WideDumper,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    )
    SENT_YAML.write_text(text, encoding="utf-8")
    print(f"\nWrote: {SENT_YAML.relative_to(REPO)}")


if __name__ == "__main__":
    main()
