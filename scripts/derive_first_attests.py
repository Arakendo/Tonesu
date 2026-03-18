#!/usr/bin/env python3
"""
derive_first_attests.py

Phase 4: Derive first_attests in corpus/sentences.yaml and backfill
missing first_use fields in registry/entries.yaml.

Algorithm:
  1. Sort sentences by S-number (numeric).
  2. For each W-number, find the lowest S-number that lists it in
     words_attested. That is its "first attestation sentence."
  3. Populate first_attests on each sentence with the W-numbers for which
     that sentence is the first attestation.
  4. For each entry in entries.yaml that has no first_use, set
     first_use = <snum> if a first-attestation sentence was found.

Rules:
  - first_attests is machine-generated; never hand-edit.
  - Existing first_use values in entries.yaml are preserved unchanged
    (they are hand-authored prose that may contain extra context).
  - Only entries with status != retired are considered.

Usage:
  python scripts/derive_first_attests.py --dry-run   # print changes only
  python scripts/derive_first_attests.py              # write both YAML files
"""

import sys
import yaml
from pathlib import Path

REPO          = Path(__file__).resolve().parent.parent
SENTENCES     = REPO / "corpus" / "sentences.yaml"
CONVERSATIONS = REPO / "corpus" / "conversations.yaml"
ENTRIES       = REPO / "registry" / "entries.yaml"


# ── YAML dumper that avoids line-wrapping ────────────────────────────────────

class _WideDumper(yaml.Dumper):
    pass

_WideDumper.best_width = 2 ** 30


def snum_key(snum: str) -> int:
    """Numeric sort key for S-numbers and C-turn ids.

    S042 -> 42    (sentences sort first)
    C001-A1 -> 1000001  (c_num * 1_000_000 + turn_within)
    This guarantees sentences always precede conversations.
    """
    if snum.startswith("S"):
        try:
            return int(snum[1:])
        except ValueError:
            return 999_999
    if snum.startswith("C"):
        # C001-A1  C002-B3
        parts = snum.split("-", 1)
        try:
            c = int(parts[0][1:])
        except (ValueError, IndexError):
            c = 999
        return 1_000_000 + c * 1_000
    return 999_999_999


def main():
    dry_run = "--dry-run" in sys.argv

    # ── Load data ─────────────────────────────────────────────────────────────
    sent_data    = yaml.safe_load(SENTENCES.read_text(encoding="utf-8"))
    entries_data = yaml.safe_load(ENTRIES.read_text(encoding="utf-8"))
    sentences = sent_data["sentences"]
    entries   = entries_data["entries"]

    conv_data = None
    if CONVERSATIONS.exists():
        conv_data = yaml.safe_load(CONVERSATIONS.read_text(encoding="utf-8"))

    # ── Build flat list of all annotated items (sentences + conv turns) ───────
    all_items = []
    for sent in sentences:
        all_items.append({"id": sent["snum"], "obj": sent})
    if conv_data:
        for conv in conv_data.get("conversations", []):
            cnum = conv["cnum"]
            for turn in conv.get("turns", []):
                turn_id = f"{cnum}-{turn['turn']}"
                all_items.append({"id": turn_id, "obj": turn})

    # Sort by snum_key so sentences always win over conversations on tie
    all_items.sort(key=lambda x: snum_key(x["id"]))

    # ── Step 1: build first-attestation map {wnum -> id} ─────────────────────
    first_sent: dict = {}   # wnum -> id of first attestation
    for item in all_items:
        item_id = item["id"]
        for wnum in item["obj"].get("words_attested") or []:
            if wnum not in first_sent:
                first_sent[wnum] = item_id

    print(f"W-numbers with a first-attestation: {len(first_sent)}")

    # ── Step 2: invert to {id -> [W-numbers first attested here]} ────────────
    first_at: dict = {}   # id -> [wnum, ...]
    for wnum, item_id in first_sent.items():
        first_at.setdefault(item_id, []).append(wnum)
    for item_id in first_at:
        first_at[item_id].sort(key=lambda w: int(w[1:]))

    # ── Step 3a: populate first_attests on sentences ──────────────────────────
    sent_changes = 0
    for sent in sentences:
        snum = sent.get("snum", "")
        new_fa = first_at.get(snum, [])
        existing_fa = sent.get("first_attests") or []
        if new_fa != existing_fa:
            if dry_run:
                print(f"  sentence {snum}: first_attests {existing_fa} -> {new_fa}")
            sent["first_attests"] = new_fa
            sent_changes += 1

    print(f"Sentences updated (first_attests): {sent_changes}")

    # ── Step 3b: populate first_attests on conversation turns ─────────────────
    conv_turn_changes = 0
    if conv_data:
        for conv in conv_data.get("conversations", []):
            cnum = conv["cnum"]
            for turn in conv.get("turns", []):
                turn_id = f"{cnum}-{turn['turn']}"
                new_fa = first_at.get(turn_id, [])
                existing_fa = turn.get("first_attests") or []
                if new_fa != existing_fa:
                    if dry_run:
                        print(f"  turn {turn_id}: first_attests {existing_fa} -> {new_fa}")
                    turn["first_attests"] = new_fa
                    conv_turn_changes += 1
        print(f"Conversation turns updated (first_attests): {conv_turn_changes}")

    # ── Step 4: backfill first_use in entries.yaml ────────────────────────────
    entries_changed = 0
    entries_already_set = 0
    for entry in entries:
        wnum   = entry.get("wnum", "")
        status = entry.get("status", "")
        if status == "retired":
            continue
        existing_fu = entry.get("first_use")
        if existing_fu:
            entries_already_set += 1
            continue   # preserve hand-authored prose
        first_id = first_sent.get(wnum)
        if first_id:
            if dry_run:
                print(f"  entry {wnum} ({entry.get('form','')}): first_use -> {first_id}")
            entry["first_use"] = first_id
            entries_changed += 1

    print(f"Entries backfilled (first_use): {entries_changed}")
    print(f"Entries with existing first_use (preserved): {entries_already_set}")
    not_found = sum(
        1 for e in entries
        if e.get("status") != "retired"
        and not e.get("first_use")
        and e.get("wnum") not in first_sent
    )
    print(f"Entries not yet attested in corpus: {not_found}")

    if dry_run:
        print("\n[dry-run] No files written.")
        return

    # ── Write sentences.yaml ──────────────────────────────────────────────────
    sent_text = yaml.dump(
        sent_data,
        Dumper=_WideDumper,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    )
    SENTENCES.write_text(sent_text, encoding="utf-8")
    print(f"\nWrote: {SENTENCES.relative_to(REPO)}")

    # ── Write entries.yaml ────────────────────────────────────────────────────
    entries_text = yaml.dump(
        entries_data,
        Dumper=_WideDumper,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    )
    ENTRIES.write_text(entries_text, encoding="utf-8")
    print(f"Wrote: {ENTRIES.relative_to(REPO)}")

    # ── Write conversations.yaml ──────────────────────────────────────────────
    if conv_data is not None:
        conv_text = yaml.dump(
            conv_data,
            Dumper=_WideDumper,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False,
        )
        CONVERSATIONS.write_text(conv_text, encoding="utf-8")
        print(f"Wrote: {CONVERSATIONS.relative_to(REPO)}")


if __name__ == "__main__":
    main()
