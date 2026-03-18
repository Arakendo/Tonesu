#!/usr/bin/env python3
"""
annotate_words_attested.py

Phase 3: Auto-populate words_attested in corpus/sentences.yaml.

Strategy:
  For each sentence, tokenize tonesu, strip grammar prefixes (la-/lo-/lu-),
  and match against all registry forms. Each matching form's W-number is
  added to words_attested.

  Also splits juncture-marked compounds on ' to match sub-compounds.

  This is an over-generous first pass: it finds all plausible matches.
  Review the output with --dry-run before writing back.

Usage:
  python scripts/annotate_words_attested.py --dry-run   # print changes only
  python scripts/annotate_words_attested.py              # write sentences.yaml
"""

import re
import sys
import yaml
from pathlib import Path
from collections import defaultdict

REPO      = Path(__file__).resolve().parent.parent
SENTENCES = REPO / "corpus" / "sentences.yaml"
ENTRIES   = REPO / "registry" / "entries.yaml"

# ── Grammar particles that are NOT registry compounds ─────────────────────────

# These tokens (standalone, after stripping la-/lo-/lu-) are grammar words
# and should never generate a words_attested annotation even if they
# accidentally appear in the registry.
GRAMMAR_TOKENS = {
    "ne", "go", "he", "ya", "ke", "ru", "ru-fe",
    "wi", "ro", "pa", "ta", "na", "du", "de",
    "nu-be", "no", "no-ne", "la", "lo", "lu",
    "ma", "ka", "ze", "si", "ti", "ra",
}

# Grammar prefixes to strip from the *start* of a space-separated token
# before attempting registry lookup.
CASE_PREFIXES = re.compile(r"^(la|lo|lu)-")

# Strip from "Parse:" onwards (appears in some sentences with inline annotation)
PARSE_SUFFIX = re.compile(r"\s*Parse:.*$", re.DOTALL)

# Strip structural/evidential brackets but keep the content
# (we want the words inside {}, (), [] — except [Sxxx] anchor labels)
ANCHOR_RE   = re.compile(r"\[S\d+[a-z]?\]")   # e.g. [S100a]
BRACKET_RE  = re.compile(r"[{}()\[\]]")
PUNCT_RE    = re.compile(r"[,;|/!?—~]")


def clean_tonesu(tonesu: str) -> str:
    """Normalize a tonesu string to a form suitable for tokenization."""
    # Strip inline parse annotations
    tonesu = PARSE_SUFFIX.sub("", tonesu)
    # Strip S-anchor labels like [S100a]
    tonesu = ANCHOR_RE.sub(" ", tonesu)
    # Remove remaining bracket characters (keep content)
    tonesu = BRACKET_RE.sub(" ", tonesu)
    # Remove punctuation
    tonesu = PUNCT_RE.sub(" ", tonesu)
    return tonesu


def extract_lookup_forms(tonesu: str) -> list[str]:
    """
    Return a list of candidate registry-lookup strings from a tonesu value.

    Steps:
    1. Clean and tokenize by whitespace
    2. Strip leading case prefix (la-/lo-/lu-) from each token
    3. Also split each resulting token on juncture ' to get sub-compounds
    4. Deduplicate while preserving order
    """
    cleaned = clean_tonesu(tonesu)
    tokens = cleaned.split()
    candidates = []
    seen = set()

    def add(form: str):
        form = form.strip("-' ")
        if form and form not in seen:
            seen.add(form)
            candidates.append(form)

    for raw_token in tokens:
        # Strip leading case prefix
        m = CASE_PREFIXES.match(raw_token)
        if m:
            token = raw_token[m.end():]
        else:
            token = raw_token

        # Try the full form (may contain ')
        add(token)

        # Also split on juncture ' to match sub-compounds
        if "'" in token:
            for part in token.split("'"):
                add(part)

    return candidates


def load_registry() -> dict:
    """Return {form_string: wnum} for all non-retired entries."""
    data = yaml.safe_load(ENTRIES.read_text(encoding="utf-8"))
    result = {}
    for e in data.get("entries", []):
        if e.get("status") == "retired":
            continue
        form = e.get("form", "")
        wnum = e.get("wnum", "")
        if form and wnum:
            result[form] = wnum
    return result


def find_matches(tonesu: str, form_index: dict) -> list[str]:
    """Return sorted list of W-numbers found in tonesu."""
    candidates = extract_lookup_forms(tonesu)
    wnums = []
    seen = set()
    for cand in candidates:
        if cand in GRAMMAR_TOKENS:
            continue
        wnum = form_index.get(cand)
        if wnum and wnum not in seen:
            seen.add(wnum)
            wnums.append(wnum)
    # Sort by numeric W-number value
    wnums.sort(key=lambda w: int(w[1:]))
    return wnums


# ── YAML dumper that avoids line-wrapping ─────────────────────────────────────

class _WideStr(str):
    pass


class _WideDumper(yaml.Dumper):
    pass


_WideDumper.best_width = 2 ** 30


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    dry_run = "--dry-run" in sys.argv

    form_index = load_registry()
    print(f"Registry: {len(form_index)} non-retired forms loaded")

    data = yaml.safe_load(SENTENCES.read_text(encoding="utf-8"))
    sentences = data["sentences"]

    changes = 0
    total_annotations = 0
    coverage: dict = defaultdict(int)  # wnum -> how many sentences

    for sent in sentences:
        tonesu = sent.get("tonesu")
        if not tonesu:
            continue
        existing = sent.get("words_attested") or []
        matches = find_matches(tonesu, form_index)

        # Merge: keep any human-annotated entries not found by auto; add new
        merged = list(dict.fromkeys(existing + matches))
        merged.sort(key=lambda w: int(w[1:]))

        if merged != existing:
            if dry_run:
                print(f"  {sent['snum']}: {existing} -> {merged}")
            sent["words_attested"] = merged
            changes += 1

        for wnum in merged:
            coverage[wnum] += 1
        total_annotations += len(merged)

    print(f"\nSentences updated: {changes}")
    print(f"Total (sentence, word) annotations: {total_annotations}")
    print(f"Distinct words attested: {len(coverage)}")
    print(f"Top 10 most-attested words:")
    for wnum, count in sorted(coverage.items(), key=lambda x: -x[1])[:10]:
        form = next((f for f, w in form_index.items() if w == wnum), "?")
        print(f"  {wnum} ({form}): {count} sentences")

    if dry_run:
        print("\n[dry-run] No file written.")
        return

    out_data = {"sentences": sentences}
    text = yaml.dump(
        out_data,
        Dumper=_WideDumper,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    )
    SENTENCES.write_text(text, encoding="utf-8")
    print(f"\nWrote: {SENTENCES.relative_to(REPO)}")


if __name__ == "__main__":
    main()
