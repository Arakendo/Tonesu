#!/usr/bin/env python3
"""
Backfill missing `natural` fields in corpus/sentences.yaml.

Three strategies:
1. s398-plus (190 entries): gloss IS the English heading text → copy to natural
2. s335-s397 (32 entries): mix of embedded English and descriptive glosses
3. s101-s175 (3 entries): multi-part minimal pairs with embedded English

Run from repo root:  python scripts/backfill_natural.py
"""
import yaml, re, sys, copy
from pathlib import Path

YAML_PATH = Path('corpus/sentences.yaml')

def extract_english_lines(tonesu: str) -> list[str]:
    """Extract lines that look like English natural translations from multi-line tonesu."""
    results = []
    for line in tonesu.split('\n'):
        stripped = line.strip()
        if not stripped:
            continue
        # Explicit Natural: label
        m = re.match(r'(?:Natural\s*[AB]?\s*:\s*)(.*)', stripped)
        if m:
            results.append(m.group(1).strip())
            continue
    return results

def extract_third_line_english(tonesu: str) -> list[str]:
    """For entries with pattern: Label: [Tonesu] / [literal] / [English],
    extract the English (third line in each triplet)."""
    lines = [l.strip() for l in tonesu.split('\n') if l.strip()]
    results = []
    # Group into blocks separated by blank lines in the original
    blocks = []
    current = []
    for line in tonesu.split('\n'):
        if line.strip():
            current.append(line.strip())
        else:
            if current:
                blocks.append(current)
                current = []
    if current:
        blocks.append(current)
    
    for block in blocks:
        if len(block) >= 3:
            # Third line in the block is often the English
            candidate = block[2]
            # Skip if it looks like Tonesu notation (contains la-, lo-, etc.)
            if not re.search(r'\bla-|\blo-|\blu-|\bne\b.*patient|\bagent:', candidate):
                # Skip if it's a literal breakdown
                if not re.search(r'patient:|agent:|action:', candidate):
                    results.append(candidate)
    return results


# Manual extraction map for entries where automated extraction is complex
MANUAL_NATURAL = {
    # s101-s175.md multi-part minimal pairs
    'S112': '(A) The machine detected the limit. (B) The machine began encoding the limit as a signal.',
    'S113': '(A) The sound archive is degraded. (B) The signal archive is degraded.',
    'S153': '(A) I detected something; no model formed of what it was. (B) My affective substrate is active; no model of why.',
    
    # s335-s397.md entries with embedded English in tonesu
    'S341': 'Have you seen the mycelium? / Yes — [I] see it. / [I\'ll] come here.',
    'S343': 'Did you see a deer? (casual vs formal register)',
    'S344': 'This plant is actively growing right now. (emphatic present; contingent state)',
    'S348': 'What does a plant produce? / A plant produces reproductive bodies.',
    
    # Theology short entries — extract from gloss
    'S350': 'The creator knows everything.',
    'S353': 'The creator is the uncaused cause.',
    'S355': 'Eternal vs atemporal: two distinct claims.',
    'S356': 'God is love.',
}


def backfill():
    data = yaml.safe_load(YAML_PATH.read_text(encoding='utf-8'))
    
    filled = 0
    skipped = 0
    
    for s in data['sentences']:
        if s.get('natural'):
            continue  # already has a natural
        
        snum = s['snum']
        gloss = s.get('gloss', '') or ''
        source = s.get('source_file', '')
        
        # Strategy 1: Manual map
        if snum in MANUAL_NATURAL:
            s['natural'] = MANUAL_NATURAL[snum]
            filled += 1
            print(f"  {snum}: manual → {s['natural'][:60]}")
            continue
        
        # Strategy 2: s398-plus — gloss IS the English
        if source == 'sentences/s398-plus.md':
            if gloss:
                s['natural'] = gloss
                filled += 1
                # print(f"  {snum}: gloss-copy → {gloss[:60]}")
            else:
                skipped += 1
                print(f"  {snum}: SKIP — no gloss")
            continue
        
        # Strategy 3: s335-s397 — use gloss as descriptive natural
        if source == 'sentences/s335-s397.md':
            # Try extracting quoted English from gloss first (smart or straight quotes)
            m = re.search(r'[\u201c"]([^"\u201d]+)[\u201d"]', gloss)
            if m:
                s['natural'] = m.group(1)
                filled += 1
                print(f"  {snum}: quoted → {s['natural'][:60]}")
            elif gloss:
                # Use the descriptive gloss as-is
                s['natural'] = gloss
                filled += 1
                print(f"  {snum}: gloss-desc → {gloss[:60]}")
            else:
                skipped += 1
                print(f"  {snum}: SKIP — no gloss")
            continue
        
        # Fallback
        if gloss:
            s['natural'] = gloss
            filled += 1
            print(f"  {snum}: fallback → {gloss[:60]}")
        else:
            skipped += 1
            print(f"  {snum}: SKIP — no data")
    
    print(f"\nFilled: {filled}, Skipped: {skipped}")
    
    # Write back
    YAML_PATH.write_text(
        yaml.dump(data, allow_unicode=True, default_flow_style=False, sort_keys=False, width=200),
        encoding='utf-8'
    )
    print(f"Wrote {YAML_PATH}")


if __name__ == '__main__':
    backfill()
