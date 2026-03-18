#!/usr/bin/env python3
"""
Extract batch metadata from corpus source markdown files → batches.yaml.

Reads each format-era file, finds batch titles and purposes, maps to theme.
"""
import yaml, re, sys, collections
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

SENT_DIR = Path('corpus/sentences')
SENT_YAML = Path('corpus/sentences.yaml')
OUT = Path('corpus/batches.yaml')

# Theme classification (copied from build_registry.py)
_GRAMMAR_PREFIXES  = {"GRM","VPC","VPT","CVP","EXC","SCL","EMD","COR","CF","FAL",
                      "LPR","MG","OPX","IPX","PMS","MTH","NEW","SA","BSH","DEB","DIP"}
_DOMAIN_PREFIXES   = {"KNM","ODL","GEO","LGL","PLT","MED","FNG","PAV","NUM"}
_THEOLOGY_PREFIXES = {"THO","GOD","DKN","WIT","TAO","ROM","MMP"}
_TRANS_PREFIXES    = {"EXO","MAT","JOH","LSP","HAM"}
_T_GRAMMAR_SUBS    = {"AX", "CMP"}
_T_THEOLOGY_SUBS   = {"APO", "REL"}

def batch_to_theme(batch: str) -> str:
    if not batch:
        return "Foundations"
    if re.match(r"^T\d", batch):
        return "Foundations"
    if batch.startswith("Hidden"):
        return "Theology & philosophy"
    if batch.startswith("T-"):
        sub = batch[2:].split("-")[0].upper()
        if sub in _T_THEOLOGY_SUBS: return "Theology & philosophy"
        if sub in _T_GRAMMAR_SUBS: return "Grammar & syntax"
        return "Domains"
    if batch.lower().startswith("fa"):
        return "Grammar & syntax"
    if re.match(r"^P[-\d]", batch) or re.match(r"^P\d", batch):
        return "Grammar & syntax"
    first = batch.split("-")[0].upper()
    if first in _GRAMMAR_PREFIXES: return "Grammar & syntax"
    if first in _DOMAIN_PREFIXES: return "Domains"
    if first in _THEOLOGY_PREFIXES: return "Theology & philosophy"
    if first in _TRANS_PREFIXES: return "Translation"
    return "Foundations"


# Batch-code → readable title overrides for batches whose markdown heading
# gives a good title.  Extracted manually from the source files.
BATCH_TITLES = {}
BATCH_PURPOSES = {}

def extract_from_markdown():
    """Scan markdown files for ## headings with batch codes and extract titles/purposes."""
    for md in sorted(SENT_DIR.rglob('s*.md')):
        text = md.read_text(encoding='utf-8')
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            # Pattern: ## Title (Srange) — Batch: CODE
            m = re.match(r'^##\s+(.+?)\s*\(S\d+', line)
            if m:
                title = m.group(1).strip()
                # Extract batch code
                code_m = re.search(r'Batch:\s*([A-Z]+-\d+)', line)
                if code_m:
                    code = code_m.group(1)
                    BATCH_TITLES[code] = title
                    
                    # Check next non-empty line for purpose (italicized)
                    for j in range(i+1, min(i+5, len(lines))):
                        purpose_line = lines[j].strip()
                        if purpose_line.startswith('*Batch purpose'):
                            pm = re.match(r'\*Batch purpose.*?:\s*(.*?)\*', purpose_line)
                            if pm:
                                BATCH_PURPOSES[code] = pm.group(1).strip()
                            break
                        elif purpose_line.startswith('*') and purpose_line.endswith('*'):
                            BATCH_PURPOSES[code] = purpose_line.strip('* ')
                            break
                        elif purpose_line and not purpose_line.startswith('#'):
                            break
            
            # Pattern: ## Title *(CODE)*
            m2 = re.match(r'^##\s+(.+?)\s*\*\(([A-Z]+-\d+)\)\*', line)
            if m2:
                title = m2.group(1).strip().rstrip('—').strip()
                code = m2.group(2)
                if code not in BATCH_TITLES:
                    BATCH_TITLES[code] = title


def build_batches_yaml():
    """Build batches.yaml from sentences.yaml + extracted markdown metadata."""
    extract_from_markdown()
    
    data = yaml.safe_load(SENT_YAML.read_text(encoding='utf-8'))
    
    # Group sentences by batch
    batch_groups = collections.OrderedDict()
    for s in data['sentences']:
        b = s.get('batch') or ''
        if not b:
            continue
        batch_groups.setdefault(b, []).append(s)
    
    batches = []
    for code, sents in batch_groups.items():
        snums = [s['snum'] for s in sents]
        first_s, last_s = snums[0], snums[-1]
        theme = batch_to_theme(code)
        
        entry = {
            'code': code,
            'title': BATCH_TITLES.get(code, ''),
            'theme': theme,
            'range': f"{first_s}–{last_s}" if first_s != last_s else first_s,
            'count': len(sents),
        }
        
        purpose = BATCH_PURPOSES.get(code, '')
        if purpose:
            entry['purpose'] = purpose
        
        batches.append(entry)
    
    result = {'batches': batches}
    OUT.write_text(
        yaml.dump(result, allow_unicode=True, default_flow_style=False, sort_keys=False, width=200),
        encoding='utf-8'
    )
    
    # Stats
    titled = sum(1 for b in batches if b.get('title'))
    purposed = sum(1 for b in batches if b.get('purpose'))
    print(f"Total batches: {len(batches)}")
    print(f"  With title: {titled}")
    print(f"  With purpose: {purposed}")
    print(f"Wrote: {OUT}")


if __name__ == '__main__':
    build_batches_yaml()
