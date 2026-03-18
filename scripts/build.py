#!/usr/bin/env python3
"""
build.py — Tonesu pipeline runner

Runs the full rebuild pipeline in the correct dependency order:

  Step 1  generate_registry_md.py    — sync registry/derived/*.md from entries.yaml
                                        (GitHub-browsable human-readable files)
  Step 2  annotate_words_attested.py — populate words_attested on sentences and
                                        conversation turns by matching registry forms
  Step 3  derive_first_attests.py    — derive first_attests per sentence/turn and
                                        backfill first_use in entries.yaml
  Step 4  build_registry.py          — generate all www/docs/tonesu/registry/ pages,
                                        word detail pages, and corpus.md

Run from repo root:
    python scripts/build.py

Flags:
    --dry-run    Pass --dry-run to steps 2 and 3 (no files written)
    --skip N     Skip step N (e.g. --skip 1 to skip generate_registry_md)
"""

import subprocess
import sys
from pathlib import Path

REPO        = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = REPO / "scripts"

STEPS = [
    (1, "generate_registry_md.py",    "Sync registry/derived/*.md from entries.yaml"),
    (2, "annotate_words_attested.py", "Annotate words_attested on sentences and turns"),
    (3, "derive_first_attests.py",    "Derive first_attests; backfill first_use"),
    (4, "build_registry.py",          "Generate www/docs/tonesu/ pages"),
]

DRY_RUN_STEPS = {2, 3}


def run_step(n: int, script: str, description: str, dry_run: bool) -> bool:
    args = [sys.executable, str(SCRIPTS_DIR / script)]
    if dry_run and n in DRY_RUN_STEPS:
        args.append("--dry-run")

    print(f"\n{'='*60}")
    print(f"Step {n}: {description}")
    print(f"  {script}{' --dry-run' if dry_run and n in DRY_RUN_STEPS else ''}")
    print(f"{'='*60}")

    result = subprocess.run(args, cwd=REPO)
    if result.returncode != 0:
        print(f"\nERROR: Step {n} failed (exit code {result.returncode}). Stopping.")
        return False
    return True


def main() -> None:
    args     = sys.argv[1:]
    dry_run  = "--dry-run" in args
    skip_raw = [a for i, a in enumerate(args) if args[i - 1] == "--skip"] if "--skip" in args else []
    skipped  = set(int(s) for s in skip_raw if s.isdigit())

    if dry_run:
        print("[dry-run mode: steps 2 and 3 will not write files]")

    for n, script, description in STEPS:
        if n in skipped:
            print(f"\nSkipping step {n}: {description}")
            continue
        if not run_step(n, script, description, dry_run):
            sys.exit(1)

    print(f"\n{'='*60}")
    print("Build complete.")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
