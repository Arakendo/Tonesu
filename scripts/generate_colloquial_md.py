#!/usr/bin/env python3
"""
generate_colloquial_md.py — Generate registry/colloquial.md from colloquial.yaml

Makes colloquial.yaml the single source of truth for colloquial registry entries.
The generated colloquial.md is the normative human-readable reference document;
website pages (www/docs/tonesu/registry/colloquial*.md) are separately generated
by build_registry.py.
"""
import sys
import yaml
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CLQ_YAML = REPO / "registry" / "colloquial.yaml"
CLQ_MD = REPO / "registry" / "colloquial.md"

sys.stdout.reconfigure(encoding="utf-8")

HEADER = """\
# Colloquial Forms

Registered contractions and stub-forms used in the casual/spoken register. \
All entries must trace back to a canonical formal compound with a corpus \
attestation sentence. Formal compounds remain the canonical lexical entries; \
colloquial forms are spoken shortcuts, never the normative phonological form.

**Contraction rule (from spec/word-formation.md § Contraction and Compression):** \
A formal compound of 3+ morphemes may contract to a shorter spoken form when: \
(1) the formal compound is at least 3 morphemes long; (2) the short form is \
unambiguous within its discourse domain; (3) the formal compound remains the \
canonical registered entry.

**Compression mechanism for kind-term stubs:** When a kind-term base compound \
shares a productively distinguishable terminal root that uniquely identifies \
the class across all expected discourse contexts, the middle qualifier morphemes \
may be stripped. The terminal root is retained as the stub coda; the organism \
anchor `zo` is retained as the stub head. Pattern: `zo` + `{middle morphemes \
dropped}` + `{class root}` → `zo{class root}`.

**Ambiguity policy:** Colloquial stubs are CVC at maximum (the phonological \
ceiling is (C)V(C) — no clusters). The CVC namespace is large enough that \
inter-stub collisions are rare, but are not prevented by design. When two stubs \
collide, context disambiguates; the formal compound is always the unambiguous \
fallback. The registry does not police the CVC namespace — it documents what \
stubs exist and traces them to formal sources. A general-class stub coexists \
with species-level stubs in the same class; the formal compound is the \
species-precision fallback.

**Open design question — longer colloquial forms:** The CVC ceiling was defined \
for root-compression stubs (organism kind-terms, matter class stubs). It may not \
be the right ceiling for *prosodic shortening* of high-frequency juncture \
compounds — long `'`-bounded forms that have become pragmatically chunked through \
repeated use, where collapsing to a single CVC removes too much structural \
information. Whether a distinct rule for juncture-preserving colloquial shortening \
is warranted, and what its admission criteria would be, is an open question. \
See `notes/open-questions.md` (CLQ-EXT). Do not apply this registry's CVC ceiling \
to that case until the question is resolved.

**ID prefix:** colloquial entries use the `CLQ-` prefix (not `COL-`, which is \
reserved for the closed color-system question, COL-001 in notes/open-questions.md).
"""


def _group_key(clq_id: str) -> str:
    """CLQ-001a → CLQ-001."""
    return clq_id.rstrip("abcdefgh")


def _anchor_class(e: dict) -> str:
    """Return the kind class type based on the anchor root."""
    anchor = e.get("anchor", "")
    if anchor == "zo":
        return "entity (organism kind)"
    if anchor == "ma":
        return "entity (matter kind)"
    return "entity"


def _generate_entry_block(e: dict) -> str:
    """Render a single CLQ entry as a fenced code block."""
    lines = [
        f"Form:         {e['form']}",
        f"Formal source: {e['formal']}",
        f"Type:         contraction / colloquial stub",
        f"Class:        {_anchor_class(e)}",
        f"Compression:  {e.get('compression', '')}",
        f"Register:     colloquial / casual spoken",
        f"Domain:       general",
        f"Status:       {e.get('status', 'active')}",
        f"First use:    {e.get('first_use', '')}",
    ]
    notes = e.get("notes", "").strip()
    if notes:
        lines.append(f"Notes:        {notes}")
    related = e.get("related_clq") or []
    if related:
        lines.append(f"Related:      {', '.join(related)}")
    return "```\n" + "\n".join(lines) + "\n```"


def generate() -> str:
    """Generate the full colloquial.md content from colloquial.yaml."""
    data = yaml.safe_load(CLQ_YAML.read_text(encoding="utf-8"))
    entries = data.get("colloquial", [])
    ns_notes = data.get("namespace_notes", [])

    parts: list[str] = [HEADER, "---", ""]

    # Group entries by CLQ number (CLQ-001a + CLQ-001b → CLQ-001)
    groups: dict[str, list[dict]] = {}
    for e in entries:
        gk = _group_key(e["clq_id"])
        groups.setdefault(gk, []).append(e)

    for gk, group in groups.items():
        # Section heading
        forms = " and ".join(f"`{e['form']}`" for e in group)
        label = "Kind-term stub" if len(group) == 1 else "Kind-term stubs"
        parts.append(f"## {gk} — {label}: {forms}")
        parts.append("")

        # First-attested line
        first_uses = []
        for e in group:
            fu = e.get("first_use", "")
            if fu:
                first_uses.append(fu)
        if first_uses:
            parts.append(f"*First-attested: {', '.join(first_uses)}.*")
            parts.append("")

        parts.append("---")
        parts.append("")

        for e in group:
            parts.append(f"**{e['clq_id']}**")
            parts.append(_generate_entry_block(e))
            parts.append("")
            parts.append("---")
            parts.append("")

    # Registration log
    parts.append("## Registration log")
    parts.append("")
    parts.append("| ID | Form | Formal source | First attested | Status |")
    parts.append("|----|------|---------------|---------------|--------|")
    for e in entries:
        parts.append(
            f"| {e['clq_id']} | `{e['form']}` | `{e['formal']}` "
            f"| {e.get('first_use', '')} | {e.get('status', '')} |"
        )
    parts.append("")
    parts.append("---")
    parts.append("")

    # Namespace collision notes
    for n in ns_notes:
        nid = n.get("note_id", "")
        base = n.get("formal_base", "")
        cls = n.get("class_affected", "")
        blocked = n.get("form_blocked", "")
        by = n.get("blocked_by", "")
        doc_at = n.get("documented_at", "")
        notes_txt = n.get("notes", "").strip()

        parts.append(f"## {nid} namespace note — no CLQ entry for `{base}` ({cls.split('/')[0].strip()} base)")
        parts.append("")
        if doc_at:
            parts.append(f"*Documented: {doc_at}.*")
            parts.append("")

        parts.append(
            f"`{base}` ({cls}) cannot produce a CVC stub without collision. "
            f"`{base}` → `{blocked}` is already registered as {by}."
        )
        parts.append("")
        parts.append(
            f"**Resolution:** the {cls.split('/')[0].strip().lower()} base class uses the "
            f"disyllabic casual form `{base}`. No CLQ entry registered."
        )
        parts.append("")

        if notes_txt:
            parts.append(notes_txt)
            parts.append("")

        parts.append("---")
        parts.append("")

    # Footer
    parts.append("*Generated from `registry/colloquial.yaml`.*")

    return "\n".join(parts)


def main() -> None:
    content = generate()
    CLQ_MD.write_text(content, encoding="utf-8")
    print(f"Wrote: {CLQ_MD.relative_to(REPO)}")


if __name__ == "__main__":
    main()
