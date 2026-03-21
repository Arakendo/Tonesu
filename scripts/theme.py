#!/usr/bin/env python3
"""
theme.py — Shared theme classification for Tonesu corpus batches.

Single source of truth for batch_to_theme() and THEME_ORDER.
Imported by build_registry.py and extract_batches.py.
"""

import re

THEME_ORDER = [
    "Foundations",
    "Grammar & syntax",
    "Domains",
    "Theology & philosophy",
    "Translation",
]

_GRAMMAR_PREFIXES  = {"GRM","VPC","VPT","CVP","EXC","SCL","EMD","COR","CF","FAL",
                      "LPR","MG","OPX","IPX","PMS","MTH","NEW","SA","BSH","DEB","DIP"}
_DOMAIN_PREFIXES   = {"KNM","ODL","GEO","LGL","PLT","MED","FNG","PAV","NUM"}
_THEOLOGY_PREFIXES = {"THO","GOD","DKN","WIT","TAO","ROM","MMP"}
_TRANS_PREFIXES    = {"EXO","MAT","JOH","LSP","HAM"}
_T_GRAMMAR_SUBS    = {"AX", "CMP"}
_T_THEOLOGY_SUBS   = {"APO", "REL"}


def batch_to_theme(batch: str | None) -> str:
    """Classify a batch code into one of the five corpus themes."""
    if not batch:
        return "Foundations"
    if re.match(r"^T\d", batch):
        return "Foundations"
    if batch.startswith("Hidden"):
        return "Theology & philosophy"
    if batch.startswith("T-"):
        sub = batch[2:].split("-")[0].upper()
        if sub in _T_THEOLOGY_SUBS:
            return "Theology & philosophy"
        if sub in _T_GRAMMAR_SUBS:
            return "Grammar & syntax"
        return "Domains"
    if batch.lower().startswith("fa"):
        return "Grammar & syntax"
    if re.match(r"^P[-\d]", batch) or re.match(r"^P\d", batch):
        return "Grammar & syntax"
    first = batch.split("-")[0].upper()
    if first in _GRAMMAR_PREFIXES:
        return "Grammar & syntax"
    if first in _DOMAIN_PREFIXES:
        return "Domains"
    if first in _THEOLOGY_PREFIXES:
        return "Theology & philosophy"
    if first in _TRANS_PREFIXES:
        return "Translation"
    return "Foundations"
