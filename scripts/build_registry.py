#!/usr/bin/env python3
"""
build_registry.py

Reads registry/entries.yaml and generates:
  www/docs/tonesu/registry/index.md      -- full alphabetical word list
  www/docs/tonesu/registry/english.md    -- English -> Tonesu lookup
  www/docs/tonesu/registry/by-domain.md  -- semantic groupings
  www/docs/tonesu/registry/by-root.md    -- root families
  www/docs/tonesu/registry/words/W***.md -- one detail page per entry
  www/docs/tonesu/corpus/index.md        -- corpus master index
  www/docs/tonesu/corpus/{theme}/        -- theme index pages
  www/docs/tonesu/corpus/batches/{slug}/ -- batch detail pages
  www/docs/tonesu/corpus/conversations/  -- conversation corpus

Run:   python scripts/build_registry.py
       (from repo root)
"""

import re
import sys
import json
import yaml
from pathlib import Path
from collections import defaultdict

REPO          = Path(__file__).resolve().parent.parent
ENTRIES       = REPO / "registry" / "entries.yaml"
PRIMITIVES    = REPO / "registry" / "primitives.yaml"
SENTENCES     = REPO / "corpus" / "sentences.yaml"
BATCHES       = REPO / "corpus" / "batches.yaml"
CONVERSATIONS = REPO / "corpus" / "conversations.yaml"
OUT_DIR       = REPO / "www" / "docs" / "tonesu" / "registry"
WORD_DIR      = OUT_DIR / "words"
CORPUS_DIR    = REPO / "www" / "docs" / "tonesu" / "corpus"
BATCH_DIR     = CORPUS_DIR / "batches"
DATA_JSON     = REPO / "www" / "docs" / "js" / "tonesu-data.json"

NOTE = (
    "*Generated from "
    "[`registry/entries.yaml`]"
    "(https://github.com/Arakendo/Tonesu/blob/main/registry/entries.yaml).*"
)

STATUS_EMOJI = {
    "active":   "✅",
    "pending":  "⏳",
    "proposed": "⚠️",
    "cold":     "❄️",
    "retired":  "🚫",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def written(form: str) -> str:
    """Written form: remove hyphens, preserve apostrophe (juncture marker)."""
    return form.replace("-", "")


def load_entries() -> list:
    if not ENTRIES.exists():
        sys.exit(f"ERROR: {ENTRIES} not found. Run scripts/migrate_to_yaml.py first.")
    data = yaml.safe_load(ENTRIES.read_text(encoding="utf-8"))
    entries = data.get("entries", [])
    # Backfill structured roots[] from form field if not set
    for entry in entries:
        if not entry.get("roots") and entry.get("form"):
            parts = re.split(r"[-']", entry["form"])
            entry["roots"] = [p for p in parts if re.fullmatch(r"[bcdfghklmnprstvwyz][aeiou]", p)]
    return entries


def load_primitives() -> dict:
    """Load registry/primitives.yaml; returns {by_cv: {cv: root}, families: [...]}."""
    if not PRIMITIVES.exists():
        return {"by_cv": {}, "families": []}
    data = yaml.safe_load(PRIMITIVES.read_text(encoding="utf-8"))
    return {
        "by_cv":    {r["cv"]: r for r in data.get("roots", [])},
        "families": data.get("families", []),
    }


def load_sentences() -> list:
    """Load corpus/sentences.yaml; return empty list if not found."""
    if not SENTENCES.exists():
        return []
    data = yaml.safe_load(SENTENCES.read_text(encoding="utf-8"))
    return data.get("sentences", [])


def load_conversations() -> list:
    """Load corpus/conversations.yaml turns as flat list; return [] if not found."""
    if not CONVERSATIONS.exists():
        return []
    data = yaml.safe_load(CONVERSATIONS.read_text(encoding="utf-8"))
    turns = []
    for conv in data.get("conversations", []):
        cnum = conv.get("cnum", "")
        for turn in conv.get("turns", []):
            # Synthesise a unique id: C001-A1
            turns.append({
                "snum": f"{cnum}-{turn.get('turn','')}",
                "words_attested": turn.get("words_attested") or [],
            })
    return turns


def build_attestation_index(sentences: list, conv_turns: list | None = None) -> dict:
    """Return {wnum: [id, ...]} built from words_attested fields of
    both sentences and (optionally) conversation turns.

    Tolerates empty words_attested lists (Phase 1 / Phase 2 state).
    Returns a non-empty index only once Phase 3 annotation is done.
    """
    index: dict = defaultdict(list)
    for item in (sentences or []) + (conv_turns or []):
        snum = item.get("snum", "")
        for wnum in item.get("words_attested") or []:
            index[wnum].append(snum)
    return {wnum: sorted(set(ids)) for wnum, ids in index.items()}


def load_conv_data() -> dict | None:
    """Load raw conversations.yaml; return None if not found."""
    if not CONVERSATIONS.exists():
        return None
    return yaml.safe_load(CONVERSATIONS.read_text(encoding="utf-8"))


def build_sentence_lookup(sentences: list) -> dict:
    """Return {snum: sentence_dict} for fast corpus look-ups."""
    return {s["snum"]: s for s in sentences}


def build_turn_lookup(conv_data: dict | None) -> dict:
    """Return {turn_id: turn_dict} for fast conversation-turn look-ups."""
    lookup: dict = {}
    if not conv_data:
        return lookup
    for conv in conv_data.get("conversations", []):
        cnum = conv.get("cnum", "")
        for turn in conv.get("turns", []):
            turn_id = f"{cnum}-{turn.get('turn', '')}"
            lookup[turn_id] = turn
    return lookup


def load_batches() -> list:
    """Load corpus/batches.yaml; return empty list if not found."""
    if not BATCHES.exists():
        return []
    data = yaml.safe_load(BATCHES.read_text(encoding="utf-8"))
    return data.get("batches", [])


def batch_page_key(code: str) -> str:
    """Normalize a batch code to a page-level filename key.

    Multiple related batches (e.g. FAL-001 through FAL-007) share one page
    keyed by prefix.  Special compound codes get explicit mappings.
    """
    if not code:
        return "_foundations"
    if code.startswith("GOD-RES"):
        return "GOD-RES"
    if code.startswith("SCL-001"):
        return "SCL"
    if code.startswith("FAL-001"):
        return "FAL"
    if code.startswith("fa-CON"):
        return "fa-CON"
    if code.startswith("Hidden"):
        return "Hidden"
    if code.startswith("T-WIT"):
        return "T-WIT"
    # T-XX-NNN → T-XX
    m = re.match(r"^(T-[A-Z]+)-\d+", code)
    if m:
        return m.group(1)
    # CODE-NNN → CODE
    m = re.match(r"^([A-Z]+)-\d+", code)
    if m:
        return m.group(1)
    # P-GP-NNN
    m = re.match(r"^(P-GP)-\d+", code)
    if m:
        return m.group(1)
    # P001..P004 → P
    m = re.match(r"^P\d+", code)
    if m:
        return "P"
    # T021..T025 → T
    m = re.match(r"^T\d+", code)
    if m:
        return "T"
    return code


def _batch_page_slug(page_key: str) -> str:
    """Convert a page key to a URL-safe slug for the batch page filename."""
    return page_key.lower().replace(" ", "-")


def _corpus_link_from_registry(id_str: str, batch_code: str = "") -> str:
    """Build a corpus link relative from registry/words/ → corpus/batches/."""
    slug = _batch_page_slug(batch_page_key(batch_code))
    return f"[{id_str}](../../corpus/batches/{slug}/#{id_str})"



def visible(entry: dict) -> bool:
    """Exclude retired entries from all public-facing pages."""
    return entry.get("status") != "retired"


# ---------------------------------------------------------------------------
# Semantic domain groupings (from 'groups' field on each entry)
# ---------------------------------------------------------------------------

def build_domain_groups(entries: list) -> list:
    """Return [(group_name, [entry_dict, ...]), ...] in canonical order."""
    groups: dict = defaultdict(list)
    for entry in entries:
        if not visible(entry):
            continue
        for g in entry.get("groups", []):
            groups[g].append(entry)

    ORDER = [
        "Person / Agent", "Kinship", "Place / Space", "Artifact / Device",
        "Time", "Knowledge / Epistemic", "Signal / Communication",
        "Affect / Emotional substrate", "Ritual / Sacred",
        "Social / Institutional", "Organism / Biology",
        "Energy / Matter / Physics", "Relation / State / Quality",
    ]
    ordered = []
    seen = set()
    for g in ORDER:
        if g in groups:
            ordered.append((g, groups[g]))
            seen.add(g)
    for g, entries_list in sorted(groups.items()):
        if g not in seen:
            ordered.append((g, entries_list))
    return ordered


# ---------------------------------------------------------------------------
# Root families (from 'lead_root' field)
# ---------------------------------------------------------------------------

def build_root_families(entries: list) -> list:
    families: dict = defaultdict(list)
    for entry in entries:
        if not visible(entry):
            continue
        root = entry.get("lead_root", "?")
        families[root].append(entry)

    result = []
    for root in sorted(families):
        members = families[root]
        parts = [
            f"`{e['form']}` {e['wnum']} {e['gloss'].split(',')[0].split(';')[0].strip()}"
            for e in sorted(members, key=lambda x: x["wnum"])
        ]
        result.append({"root": root, "entries_raw": " · ".join(parts)})
    return result


# ---------------------------------------------------------------------------
# English reverse index
# ---------------------------------------------------------------------------

def build_english_index(entries: list) -> list:
    rows = []
    for entry in entries:
        if not visible(entry):
            continue
        gloss = entry.get("gloss", "")
        gloss_clean = re.sub(r"\(.*?\)", "", gloss).strip()
        seen = set()
        for raw_term in re.split(r"[,;/]", gloss_clean):
            term = raw_term.strip().rstrip(".").lower()
            if not term or len(term) > 35 or len(term.split()) > 4:
                continue
            if term in seen:
                continue
            seen.add(term)
            rows.append((term, entry))
    rows.sort(key=lambda x: x[0])
    return rows


# ---------------------------------------------------------------------------
# Page generators
# ---------------------------------------------------------------------------

def generate_index_page(
    entries: list,
    attest_index: dict | None = None,
    sentence_batch_map: dict | None = None,
) -> str:
    if attest_index is None:
        attest_index = {}
    has_attestations = bool(attest_index)
    visible_entries = [e for e in entries if visible(e)]
    count = len(visible_entries)
    lines = [
        "---",
        "title: Word Registry",
        "---",
        "",
        "# Word Registry",
        "",
        f"{count} derived compounds, sorted alphabetically.",
        "",
        "See also: [English index](english.md) · "
        "[By domain](by-domain.md) · [By root](by-root.md) · "
        "[Building words](../words.md)",
        "",
    ]
    if has_attestations:
        lines += [
            "| Form | Written | W# | Gloss | Status | Corpus |",
            "|------|---------|-----|-------|--------|--------|",
        ]
    else:
        lines += [
            "| Form | Written | W# | Gloss | Status |",
            "|------|---------|-----|-------|--------|",
        ]
    for e in sorted(visible_entries, key=lambda x: x["form"]):
        emoji  = STATUS_EMOJI.get(e.get("status", "pending"), "⏳")
        wnum   = e["wnum"]
        wlink  = f"[{wnum}](words/{wnum}.md)"
        if has_attestations:
            snums = attest_index.get(wnum, [])
            def _idx_link(sn: str) -> str:
                bc = (sentence_batch_map or {}).get(sn, "")
                slug = _batch_page_slug(batch_page_key(bc))
                return f"[{sn}](../corpus/batches/{slug}/#{sn})"
            corpus_cell = " · ".join(_idx_link(i) for i in snums) if snums else "—"
            lines.append(
                f'| `{e["form"]}` | {written(e["form"])} | {wlink} '
                f'| {e["gloss"]} | {emoji} | {corpus_cell} |'
            )
        else:
            lines.append(
                f'| `{e["form"]}` | {written(e["form"])} | {wlink} '
                f'| {e["gloss"]} | {emoji} |'
            )
    lines += ["", "---", "", NOTE]
    return "\n".join(lines)


def generate_english_page(rows: list) -> str:
    lines = [
        "---",
        "title: English Index",
        "---",
        "",
        "# English Index",
        "",
        "Look up Tonesu words by English keyword. Where two or more Tonesu words "
        "share a term, all appear together — the **Gloss** column gives the "
        "precise distinction.",
        "",
        "See also: [Alphabetical list](index.md) · [By domain](by-domain.md) · "
        "[Building words](../words.md)",
        "",
        "| English | Written form | Parse | Gloss |",
        "|---------|-------------|-------|-------|",
    ]
    for en_word, e in rows:
        lines.append(
            f'| {en_word} | {written(e["form"])} | `{e["form"]}` | {e["gloss"]} |'
        )
    lines += ["", "---", "", NOTE]
    return "\n".join(lines)


def generate_by_domain_page(domain_groups: list) -> str:
    lines = [
        "---",
        "title: By Domain",
        "---",
        "",
        "# Words by Domain",
        "",
        "Concept-first lookup: find the word you need by semantic category.",
        "",
        "See also: [Alphabetical list](index.md) · "
        "[English index](english.md) · [By root](by-root.md) · "
        "[Building words](../words.md)",
        "",
    ]
    for domain_name, entries_list in domain_groups:
        lines += [
            f"## {domain_name}",
            "",
            "| Form | Written | W# | Gloss |",
            "|------|---------|-----|-------|",
        ]
        for e in sorted(entries_list, key=lambda x: x["form"]):
            lines.append(
                f'| `{e["form"]}` | {written(e["form"])} | {e["wnum"]} | {e["gloss"]} |'
            )
        lines.append("")
    lines += ["---", "", NOTE]
    return "\n".join(lines)


def generate_by_root_page(root_families: list) -> str:
    lines = [
        "---",
        "title: By Root",
        "---",
        "",
        "# Words by Root Family",
        "",
        "Each row groups derived compounds sharing the same lead primitive root.",
        "",
        "See also: [Alphabetical list](index.md) · "
        "[English index](english.md) · [By domain](by-domain.md) · "
        "[Building words](../words.md)",
        "",
        "| Lead root | Derived compounds |",
        "|-----------|------------------|",
    ]
    for r in root_families:
        lines.append(f'| `{r["root"]}` | {r["entries_raw"]} |')
    lines += ["", "---", "", NOTE]
    return "\n".join(lines)


def generate_word_page(
    entry: dict,
    attest_index: dict,
    sentence_lookup: dict,
    turn_lookup: dict,
    sentence_batch_map: dict | None = None,
) -> str:
    wnum  = entry["wnum"]
    form  = entry["form"]
    w     = written(form)
    gloss = entry.get("gloss", "")
    emoji = STATUS_EMOJI.get(entry.get("status", "pending"), "⏳")

    lines = [
        "---",
        f"title: {form} ({wnum})",
        "---",
        "",
        f"# `{form}` · {wnum}",
        "",
        f"**{w}** · {gloss} · {emoji}",
        "",
        "[← Word Registry](../index.md) · [Building words](../../words.md)",
        "",
    ]

    # Metadata table
    meta: list[tuple[str, str]] = []
    if entry.get("domain"):
        meta.append(("Domain", entry["domain"]))
    if entry.get("class"):
        meta.append(("Class", entry["class"]))
    if entry.get("type"):
        meta.append(("Type", entry["type"]))
    if entry.get("register"):
        meta.append(("Register", entry["register"]))
    first_use_raw = entry.get("first_use") or ""
    if first_use_raw:
        fu_m = re.match(r"(S\d+|C\d+-\w+)", first_use_raw)
        if fu_m:
            fu_id = fu_m.group(1)
            fu_batch = (sentence_batch_map or {}).get(fu_id, "")
            fu_link = _corpus_link_from_registry(fu_id, fu_batch)
            fu_display = re.sub(
                r"^(S\d+|C\d+-\w+)",
                fu_link,
                first_use_raw,
                count=1,
            )
        else:
            fu_display = first_use_raw
        meta.append(("First use", fu_display))

    if meta:
        lines += ["| | |", "|---|---|"]
        for label, value in meta:
            lines.append(f"| {label} | {value} |")
        lines.append("")

    if entry.get("composition"):
        lines += ["## Composition", "", entry["composition"], ""]

    if entry.get("definition"):
        lines += ["## Definition", "", entry["definition"], ""]

    if entry.get("notes"):
        lines += ["## Notes", "", entry["notes"], ""]

    if entry.get("related"):
        lines += ["## Related", "", entry["related"], ""]

    if entry.get("examples"):
        lines += ["## Examples", "", entry["examples"], ""]

    # Corpus attestations
    snums = attest_index.get(wnum, [])
    if snums:
        lines += [
            "## In the corpus",
            "",
            "| # | Tonesu | English |",
            "|---|--------|---------|",
        ]
        for snum in snums:
            item = sentence_lookup.get(snum) or turn_lookup.get(snum)
            s_batch = (sentence_batch_map or {}).get(snum, "")
            s_link = _corpus_link_from_registry(snum, s_batch)
            if item:
                tonesu  = (item.get("tonesu") or "").replace("\n", " / ")
                natural = (item.get("natural") or "").replace("\n", " / ")
                lines.append(
                    f"| {s_link} | `{tonesu}` | {natural} |"
                )
            else:
                lines.append(f"| {s_link} | | |")
        lines.append("")

    lines += ["---", "", NOTE]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Corpus theme grouping
# ---------------------------------------------------------------------------

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


def _group_sentences_by_page(sentences: list) -> dict[str, list]:
    """Group sentences by their batch page key."""
    groups: dict[str, list] = defaultdict(list)
    for sent in sentences:
        key = batch_page_key(sent.get("batch") or "")
        groups[key].append(sent)
    return dict(groups)


# Page-level group titles (used for batch page H1 and theme table display)
PAGE_GROUP_TITLES = {
    "_foundations": "Early & Unbatched Sentences",
    "P": "Early Grammar Probes",
    "T": "Foundational Sentences",
    "Hidden": "Hidden Property Stress Tests",
    "T-HA": "Human Activity Domain",
    "T-XX": "Cross-Domain Sentences",
    "T-APO": "Apophatic Theology",
    "T-PRM": "Primitive Attestation",
    "T-CMP": "Compound Structure Tests",
    "T-KO": "Knowledge & Ontology",
    "T-MYS": "Abstract & Mystery Domain",
    "T-REL": "Relational Theology",
    "T-WIT": "Organizational Roles & Witness",
    "T-PHN": "Phonology & Naming",
    "T-AX": "Particle & Axiom Tests",
    "CF": "Core Function Attestation",
    "fa-VAL": "Valence Frame Test",
    "fa-CON": "Connective Attestation",
    "MG": "Morphological Merge Test",
    "P-GP": "Grammar Pattern Probes",
    "SA": "Scope & Aspect Test",
    "OPX": "Operator Extension Test",
    "IPX": "Inflection Pattern Test",
    "PMS": "Particle Modifier Stress Test",
    "EMD": "Em-Dash Attestation",
    "MMP": "Moral & Metaphysical Paradox",
    "KNM": "Kind Naming (Biology)",
    "ODL": "Everyday Objects & Domestic Life",
    "GEO": "Geography & Terrain",
    "NUM": "Numeral System",
    "LGL": "Legal & Governance",
    "GOD-RES": "Theological Residuals",
    "TAO": "Tao Te Ching — Way & Non-Action",
    "EXO": "Exodus 3 — Burning Bush",
    "MAT": "Rock, Mineral, Soil",
    "SCL": "Sequential Connector Tests",
}

THEME_DESCRIPTIONS = {
    "Foundations": "Core sentences from the earliest Tonesu attestations — basic agent-patient structures, property attribution, and foundational constructions.",
    "Grammar & syntax": "Systematic tests of particles, operators, valence frames, connectives, scope, aspect, and sentence-level constructions.",
    "Domains": "Vocabulary attestation across semantic domains — biology, geography, numerals, everyday life, legal, and specialized terminology.",
    "Theology & philosophy": "Stress tests of theological, metaphysical, and philosophical constructions — divine attributes, apophatic claims, paradoxes, and cross-tradition texts.",
    "Translation": "Translation stress tests from external source texts — scripture, literature, philosophy, and poetry rendered in Tonesu.",
}


def _page_group_title(page_key: str, batch_meta_list: list) -> str:
    """Get the best title for a batch page group."""
    if page_key in PAGE_GROUP_TITLES:
        return PAGE_GROUP_TITLES[page_key]
    if batch_meta_list and batch_meta_list[0].get("title"):
        return batch_meta_list[0]["title"]
    return page_key


def _group_batches_by_page(batches: list) -> dict[str, list]:
    """Group batch metadata entries by their page key."""
    groups: dict[str, list] = defaultdict(list)
    for b in batches:
        key = batch_page_key(b.get("code", ""))
        groups[key].append(b)
    return dict(groups)


def generate_corpus_index(sentences: list, conv_data: dict | None, page_groups: dict) -> str:
    """Master corpus index page with theme summaries and links."""
    convs = (conv_data or {}).get("conversations", [])
    n_turns = sum(len(c.get("turns", [])) for c in convs)
    n_sents = len(sentences)

    # Build per-theme stats
    theme_stats: dict[str, dict] = {t: {"sents": 0, "pages": set()} for t in THEME_ORDER}
    for sent in sentences:
        theme = batch_to_theme(sent.get("batch"))
        key = batch_page_key(sent.get("batch") or "")
        theme_stats[theme]["sents"] += 1
        theme_stats[theme]["pages"].add(key)

    lines = [
        "---",
        "title: Corpus",
        "---",
        "",
        "# Corpus",
        "",
        "The canonical body of attested Tonesu sentences. Every entry is numbered, "
        "parsed, and glossed — organized by theme and batch.",
        "",
        f"**{n_sents}** sentences · **{n_turns}** conversation turns · "
        f"**{len(page_groups)}** batch pages.",
        "",
        NOTE,
        "",
        "---",
        "",
        "## Themes",
        "",
        "| Theme | Sentences | Pages |",
        "|-------|-----------|-------|",
    ]
    theme_slugs = {
        "Foundations": "foundations",
        "Grammar & syntax": "grammar",
        "Domains": "domains",
        "Theology & philosophy": "theology",
        "Translation": "translation",
    }
    for theme in THEME_ORDER:
        s = theme_stats[theme]
        slug = theme_slugs[theme]
        lines.append(f"| [{theme}]({slug}/) | {s['sents']} | {len(s['pages'])} |")

    lines += [
        "",
        f"[Conversations](conversations/) — {n_turns} turns",
        "",
    ]
    return "\n".join(lines)


def generate_theme_page(
    theme: str,
    sentences: list,
    page_groups: dict,
    batch_meta: dict[str, list],
) -> str:
    """Generate a theme index page listing all batch groups in the theme."""
    theme_sents = [s for s in sentences if batch_to_theme(s.get("batch")) == theme]
    desc = THEME_DESCRIPTIONS.get(theme, "")

    lines = [
        "---",
        f"title: \"{theme}\"",
        "---",
        "",
        f"# {theme}",
        "",
    ]
    if desc:
        lines += [desc, ""]
    lines += [
        f"{len(theme_sents)} sentences.",
        "",
        "[← Corpus](../index.md)",
        "",
        "---",
        "",
        "| Batch group | Batches | Sentences | Link |",
        "|-------------|---------|-----------|------|",
    ]

    # Collect page keys that belong to this theme
    theme_keys: list[str] = []
    for sent in theme_sents:
        key = batch_page_key(sent.get("batch") or "")
        if key not in theme_keys:
            theme_keys.append(key)

    for key in theme_keys:
        slug = _batch_page_slug(key)
        group_sents = page_groups.get(key, [])
        group_batches = batch_meta.get(key, [])
        n_batches = len(group_batches) if group_batches else 1
        title = _page_group_title(key, group_batches)
        lines.append(
            f"| {title} | {n_batches} | {len(group_sents)} | "
            f"[→ batches/{slug}](../batches/{slug}/) |"
        )

    lines += ["", "---", "", NOTE]
    return "\n".join(lines)


def generate_batch_page(
    page_key: str,
    sents: list,
    batch_meta_list: list,
) -> str:
    """Generate a batch detail page showing all sentences for a page-key group."""
    slug = _batch_page_slug(page_key)
    title = _page_group_title(page_key, batch_meta_list)

    # Derive theme from first sentence's batch
    theme_slugs = {
        "Foundations": "foundations",
        "Grammar & syntax": "grammar",
        "Domains": "domains",
        "Theology & philosophy": "theology",
        "Translation": "translation",
    }
    first_batch = sents[0].get("batch") if sents else None
    theme = batch_to_theme(first_batch)
    theme_slug = theme_slugs.get(theme, "foundations")

    lines = [
        "---",
        f"title: \"{title}\"",
        "---",
        "",
        f"# {title}",
        "",
        f"*Theme: [{theme}](../../{theme_slug}/)* · {len(sents)} sentences.",
        "",
        f"[← {theme}](../../{theme_slug}/) · [← Corpus](../../index.md)",
        "",
        "---",
        "",
    ]

    # Sub-group by individual batch code for ordering
    batch_groups: dict[str, list] = {}
    for sent in sents:
        bc = sent.get("batch") or ""
        batch_groups.setdefault(bc, []).append(sent)

    for bc, bc_sents in batch_groups.items():
        # Find batch metadata
        bm = None
        for b in batch_meta_list:
            if b.get("code") == bc:
                bm = b
                break
        batch_title = bm.get("title", bc) if bm else bc
        if bc:
            lines += [f"## {bc} · {batch_title}", ""]
        else:
            lines += ["## Unbatched", ""]

        for sent in bc_sents:
            snum = sent.get("snum", "")
            tonesu_lines = (sent.get("tonesu") or "").split("\n")
            natural = sent.get("natural") or ""
            status = sent.get("status", "")

            lines.append(f'<span id="{snum}"></span>')

            label_parts = [f"**{snum}**"]
            if status == "legacy":
                label_parts.append("*legacy*")
            lines.append(" · ".join(label_parts))

            for t in tonesu_lines:
                t = t.strip()
                if t:
                    lines.append(f"`{t}`")

            if natural:
                lines.append(f"*{natural.replace(chr(10), '<br>')}*")

            lines.append("")

    lines += ["---", "", NOTE]
    return "\n".join(lines)


def generate_conversations_page(conv_data: dict | None) -> str:
    """Generate a standalone page for conversation corpus."""
    convs = (conv_data or {}).get("conversations", [])
    n_turns = sum(len(c.get("turns", [])) for c in convs)

    lines = [
        "---",
        "title: Conversations",
        "---",
        "",
        "# Conversations",
        "",
        f"{len(convs)} conversations · {n_turns} turns.",
        "",
        "[← Corpus](../index.md)",
        "",
        "---",
        "",
    ]

    for conv in convs:
        cnum = conv.get("cnum", "")
        gloss = conv.get("gloss", "")
        scene = conv.get("scene", "")

        lines += [
            f'<span id="{cnum}"></span>',
            f"## {cnum} · {gloss}",
            "",
        ]
        if scene:
            lines += [f"*{scene}*", ""]

        for turn in conv.get("turns", []):
            turn_label = turn.get("turn", "")
            turn_id = f"{cnum}-{turn_label}"
            turn_tonesu = (turn.get("tonesu") or "").split("\n")
            turn_natural = turn.get("natural") or ""

            lines.append(f'<span id="{turn_id}"></span>')
            lines.append(f"**{turn_label}**")

            for t in turn_tonesu:
                t = t.strip()
                if t:
                    lines.append(f"`{t}`")

            if turn_natural:
                lines.append(f"*{turn_natural.replace(chr(10), '<br>')}*")

            lines.append("")

    lines += ["---", "", NOTE]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    entries       = load_entries()
    primitives    = load_primitives()
    sentences     = load_sentences()
    conv_turns    = load_conversations()
    conv_data     = load_conv_data()
    batches_data  = load_batches()
    attest_index  = build_attestation_index(sentences, conv_turns)
    domain_groups = build_domain_groups(entries)
    root_families = build_root_families(entries)
    english_rows  = build_english_index(entries)
    sent_lookup   = build_sentence_lookup(sentences)
    turn_lookup   = build_turn_lookup(conv_data)

    # Build sentence → batch map for cross-links
    sentence_batch_map: dict[str, str] = {}
    for sent in sentences:
        snum = sent.get("snum", "")
        if snum:
            sentence_batch_map[snum] = sent.get("batch") or ""
    # Include conversation turns
    for conv in (conv_data or {}).get("conversations", []):
        cnum = conv.get("cnum", "")
        for turn in conv.get("turns", []):
            turn_id = f"{cnum}-{turn.get('turn', '')}"
            sentence_batch_map[turn_id] = ""

    # Group sentences and batch metadata by page key
    page_groups = _group_sentences_by_page(sentences)
    batch_meta  = _group_batches_by_page(batches_data)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    WORD_DIR.mkdir(parents=True, exist_ok=True)
    CORPUS_DIR.mkdir(parents=True, exist_ok=True)
    BATCH_DIR.mkdir(parents=True, exist_ok=True)

    # --- Registry pages ---
    (OUT_DIR / "index.md").write_text(generate_index_page(entries, attest_index, sentence_batch_map), encoding="utf-8")
    (OUT_DIR / "english.md").write_text(generate_english_page(english_rows), encoding="utf-8")
    (OUT_DIR / "by-domain.md").write_text(generate_by_domain_page(domain_groups), encoding="utf-8")
    (OUT_DIR / "by-root.md").write_text(generate_by_root_page(root_families), encoding="utf-8")

    # --- Corpus: master index ---
    (CORPUS_DIR / "index.md").write_text(
        generate_corpus_index(sentences, conv_data, page_groups), encoding="utf-8"
    )

    # --- Corpus: theme pages ---
    theme_slugs = {
        "Foundations": "foundations",
        "Grammar & syntax": "grammar",
        "Domains": "domains",
        "Theology & philosophy": "theology",
        "Translation": "translation",
    }
    for theme in THEME_ORDER:
        slug = theme_slugs[theme]
        theme_dir = CORPUS_DIR / slug
        theme_dir.mkdir(parents=True, exist_ok=True)
        (theme_dir / "index.md").write_text(
            generate_theme_page(theme, sentences, page_groups, batch_meta),
            encoding="utf-8",
        )

    # --- Corpus: batch pages ---
    batch_page_count = 0
    for page_key, sents in page_groups.items():
        slug = _batch_page_slug(page_key)
        page_dir = BATCH_DIR / slug
        page_dir.mkdir(parents=True, exist_ok=True)
        meta_list = batch_meta.get(page_key, [])
        (page_dir / "index.md").write_text(
            generate_batch_page(page_key, sents, meta_list), encoding="utf-8"
        )
        batch_page_count += 1

    # --- Corpus: conversations ---
    conv_dir = CORPUS_DIR / "conversations"
    conv_dir.mkdir(parents=True, exist_ok=True)
    (conv_dir / "index.md").write_text(
        generate_conversations_page(conv_data), encoding="utf-8"
    )

    emit_data_json(entries, primitives)

    # --- Word detail pages ---
    word_pages = 0
    for entry in entries:
        if not visible(entry):
            continue
        page_text = generate_word_page(
            entry, attest_index, sent_lookup, turn_lookup, sentence_batch_map
        )
        (WORD_DIR / f"{entry['wnum']}.md").write_text(page_text, encoding="utf-8")
        word_pages += 1

    visible_count   = sum(1 for e in entries if visible(e))
    attested_count  = sum(1 for e in entries if e.get("wnum") in attest_index)
    n_conv_turns = sum(len(c.get("turns", [])) for c in (conv_data or {}).get("conversations", []))
    print(f"Generated {visible_count} entries -> {OUT_DIR.relative_to(REPO)}/")
    print(f"  index.md    : {visible_count} words ({attested_count} with corpus attestations)")
    print(f"  english.md  : {len(english_rows)} English terms")
    print(f"  by-domain.md: {len(domain_groups)} domains")
    print(f"  by-root.md  : {len(root_families)} root families")
    print(f"  corpus/     : {len(sentences)} sentences · {n_conv_turns} conversation turns")
    print(f"    themes    : {len(THEME_ORDER)} theme pages")
    print(f"    batches   : {batch_page_count} batch pages")
    print(f"  words/      : {word_pages} detail pages")
    if conv_turns:
        conv_attested = sum(1 for t in conv_turns if t.get("words_attested"))
        print(f"  (conv turns contributing attestations: {conv_attested}/{len(conv_turns)})")


def emit_data_json(entries: list, primitives: dict) -> None:
    """Emit www/docs/js/tonesu-data.json for the root browser/builder UI."""
    by_cv = primitives.get("by_cv", {})
    prim_list = [
        {
            "cv":       r["cv"],
            "gloss":    r["gloss"],
            "family":   r["family"],
            "category": r["category"],
            "includes": r.get("includes", ""),
            "excludes": r.get("excludes", ""),
            "status":   r["status"],
        }
        for r in by_cv.values()
        if r["status"] in ("active", "reserved")
    ]

    entry_list = [
        {
            "wnum":    e["wnum"],
            "form":    e.get("form", ""),
            "written": written(e.get("form", "")),
            "gloss":   e.get("gloss", ""),
            "status":  e.get("status", ""),
            "domain":  e.get("domain", ""),
            "roots":   e.get("roots") or [],
        }
        for e in entries
        if e.get("status") in ("active", "pending", "proposed")
    ]

    payload = {
        "primitives": prim_list,
        "families":   primitives.get("families", []),
        "entries":    entry_list,
    }
    DATA_JSON.parent.mkdir(parents=True, exist_ok=True)
    DATA_JSON.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"  tonesu-data.json: {len(prim_list)} primitives, {len(entry_list)} entries")


if __name__ == "__main__":
    main()
