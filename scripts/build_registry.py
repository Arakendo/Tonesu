#!/usr/bin/env python3
"""
build_registry.py

Reads registry/entries.yaml and generates four MkDocs pages:
  www/docs/tonesu/registry/index.md      -- full alphabetical word list
  www/docs/tonesu/registry/english.md    -- English -> Tonesu lookup
  www/docs/tonesu/registry/by-domain.md  -- semantic groupings
  www/docs/tonesu/registry/by-root.md    -- root families

Run:   python scripts/build_registry.py
       (from repo root)
"""

import re
import sys
import yaml
from pathlib import Path
from collections import defaultdict

REPO          = Path(__file__).resolve().parent.parent
ENTRIES       = REPO / "registry" / "entries.yaml"
SENTENCES     = REPO / "corpus" / "sentences.yaml"
CONVERSATIONS = REPO / "corpus" / "conversations.yaml"
OUT_DIR       = REPO / "www" / "docs" / "tonesu" / "registry"
CORPUS_PAGE   = REPO / "www" / "docs" / "tonesu" / "corpus.md"

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
    return data.get("entries", [])


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


def _corpus_link(id_str: str) -> str:
    """Wrap a corpus id in a markdown link to corpus.md (relative from registry/)."""
    return f"[{id_str}](../corpus.md#{id_str})"


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

def generate_index_page(entries: list, attest_index: dict | None = None) -> str:
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
        "[By domain](by-domain.md) · [By root](by-root.md)",
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
        emoji = STATUS_EMOJI.get(e.get("status", "pending"), "⏳")
        if has_attestations:
            snums = attest_index.get(e["wnum"], [])
            corpus_cell = " · ".join(_corpus_link(i) for i in snums) if snums else "—"
            lines.append(
                f'| `{e["form"]}` | {written(e["form"])} | {e["wnum"]} '
                f'| {e["gloss"]} | {emoji} | {corpus_cell} |'
            )
        else:
            lines.append(
                f'| `{e["form"]}` | {written(e["form"])} | {e["wnum"]} '
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
        "See also: [Alphabetical list](index.md) · [By domain](by-domain.md)",
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
        "[English index](english.md) · [By root](by-root.md)",
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
        "[English index](english.md) · [By domain](by-domain.md)",
        "",
        "| Lead root | Derived compounds |",
        "|-----------|------------------|",
    ]
    for r in root_families:
        lines.append(f'| `{r["root"]}` | {r["entries_raw"]} |')
    lines += ["", "---", "", NOTE]
    return "\n".join(lines)


def generate_corpus_page(sentences: list, conv_data: dict | None) -> str:
    convs = (conv_data or {}).get("conversations", [])
    n_turns = sum(len(c.get("turns", [])) for c in convs)
    n_sents = len(sentences)

    lines = [
        "---",
        "title: Corpus",
        "---",
        "",
        "# Corpus",
        "",
        f"{n_sents} sentences · {n_turns} conversation turns.",
        "",
        "---",
        "",
        "## Sentences",
        "",
    ]

    for sent in sentences:
        snum = sent.get("snum", "")
        tonesu_lines = (sent.get("tonesu") or "").split("\n")
        natural = sent.get("natural") or ""
        batch = sent.get("batch") or ""
        status = sent.get("status", "")

        lines.append(f'<span id="{snum}"></span>')

        label_parts = [f"**{snum}**"]
        if batch:
            label_parts.append(batch)
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

    if convs:
        lines += ["---", "", "## Conversations", ""]
        for conv in convs:
            cnum = conv.get("cnum", "")
            gloss = conv.get("gloss", "")
            scene = conv.get("scene", "")

            lines += [
                f'<span id="{cnum}"></span>',
                f"### {cnum} · {gloss}",
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
    sentences     = load_sentences()
    conv_turns    = load_conversations()
    conv_data     = load_conv_data()
    attest_index  = build_attestation_index(sentences, conv_turns)
    domain_groups = build_domain_groups(entries)
    root_families = build_root_families(entries)
    english_rows  = build_english_index(entries)

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    (OUT_DIR / "index.md").write_text(generate_index_page(entries, attest_index), encoding="utf-8")
    (OUT_DIR / "english.md").write_text(generate_english_page(english_rows), encoding="utf-8")
    (OUT_DIR / "by-domain.md").write_text(generate_by_domain_page(domain_groups), encoding="utf-8")
    (OUT_DIR / "by-root.md").write_text(generate_by_root_page(root_families), encoding="utf-8")
    CORPUS_PAGE.write_text(generate_corpus_page(sentences, conv_data), encoding="utf-8")

    visible_count   = sum(1 for e in entries if visible(e))
    attested_count  = sum(1 for e in entries if e.get("wnum") in attest_index)
    n_conv_turns = sum(len(c.get("turns", [])) for c in (conv_data or {}).get("conversations", []))
    print(f"Generated {visible_count} entries -> {OUT_DIR.relative_to(REPO)}/")
    print(f"  index.md    : {visible_count} words ({attested_count} with corpus attestations)")
    print(f"  english.md  : {len(english_rows)} English terms")
    print(f"  by-domain.md: {len(domain_groups)} domains")
    print(f"  by-root.md  : {len(root_families)} root families")
    print(f"  corpus.md   : {len(sentences)} sentences · {n_conv_turns} conversation turns")
    if conv_turns:
        conv_attested = sum(1 for t in conv_turns if t.get("words_attested"))
        print(f"  (conv turns contributing attestations: {conv_attested}/{len(conv_turns)})")


if __name__ == "__main__":
    main()
