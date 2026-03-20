# Conversation Template — corpus/conversations/

A conversation entry documents a multi-turn Tonesu exchange. It lives in
two parallel places:

- **`.md` narrative file** (`corpus/conversations/c001-c004.md` or current
  intake file) — human-readable, annotated turn by turn
- **`corpus/conversations.yaml`** — machine-readable; the pipeline reads
  exclusively from here for site generation

Both must be kept in sync. Write the `.md` first (easier to author); then
add the corresponding YAML block.

---

## When to use a conversation vs. a sentence

Use a conversation entry when:

- The test requires more than one turn to set up
- The critical construction appears in the reply, not the prompt
- The construct depends on prior discourse context (`ze` back-reference,
  epistemic floor tracking, attribution chains, question–answer pairing)

Single sentences that happen to be dialogue lines go in the sentence files
(S-series) with a note — not here.

---

## .md Narrative Format

New conversations go in the current intake file (`c008-plus.md` or successor).

```markdown
## [Title] ([Cnum])

---

**[Cnum] — [One-line English gloss / scene title]**

*Scene: [One paragraph describing the situation, participants, and discourse context.
Name participant roles as Tonesu compound readings: `to-fe-li` (epistemic arbiter,
role B) etc. Explain what discourse-level construct is under test.]*

*Tests: [comma-separated list of the specific constructions or rules being tested]*

---

**Turn A1 — [Short label for what this turn does]**

```
Gloss:    [morpheme breakdown — label:form arrangement]
Literal:  [same morphemes, English values]
Natural:  [fluent English reading]
```

**Notes:**
- [bullet: parse decision or design choice]
- [bullet: state of discourse after this turn — what referents are active,
  what epistemic floor has been established]

---

**Turn B1 — [Short label]**

```
Gloss:    [...]
Literal:  [...]
Natural:  [...]
```

**Notes:**
- [...]
- **State of discourse after B1:** [...]

---

[...repeat for each turn...]

---

## [Cnum] Summary

| Turn | Natural | Key test |
|------|---------|----------|
| A1 | [natural gloss] | [what construction is tested] |
| B1 | [natural gloss] | [what construction is tested] |

**Key finding:** [one sentence: what the conversation establishes or resolves]

**Issues resolved / logged:** [ISSUE-NNN or "none"]
```

---

## YAML Format (`corpus/conversations.yaml`)

Add one block per conversation to `corpus/conversations.yaml`.
The `turns` list order must match the `.md` file exactly.

```yaml
- cnum: C009              # Stable C-number. Never reassigned.
  gloss: "Short gloss"    # English title — matches .md bold header
  scene: >-               # Scene description — same as .md italicised paragraph
    [One paragraph. Multi-line fine. Agents, context, what is under test.]
  tests:                  # List of constructions tested — matches .md *Tests:* line
    - ze back-reference
    - propositional anaphora
    - predicate-type disambiguation
  status: normative       # normative | draft
  source_file: conversations/c008-plus.md   # relative to repo root
  turns:
    - turn: A1
      tonesu: "la-ze  de  lo-si-de  ta-ti-de"   # notation form (hyphens preserved)
      gloss_line: "agent:ze  decayed  patient:record-signal  at:past-time"
      natural: "The archivist suppressed the record."
      words_attested: []   # W-numbers used in this turn; populated by annotate pass
      first_attests: []    # W-numbers first attested here; populated by derive pass
      notes: null          # string or null
    - turn: B1
      tonesu: "la-mi  si  [la-ze  no-de  lo-si-de]"
      gloss_line: "agent:I  hypothesize  [agent:ze  not-decayed  patient:record-signal]"
      natural: "I hypothesize: ze did not suppress the record."
      words_attested: []
      first_attests: []
      notes: null
```

---

## YAML field reference

| Field | Required | Description |
|-------|----------|-------------|
| `cnum` | yes | Stable C-number (C001, C002 …). Never reassigned. |
| `gloss` | yes | One-line English gloss / scene title. |
| `scene` | yes | Prose scene description. Go multiline freely. |
| `tests` | yes | List of specific constructions under test. |
| `status` | yes | `normative` or `draft`. |
| `source_file` | yes | Path relative to repo root to the `.md` narrative file. |
| `turns[].turn` | yes | Turn label: A1, B1, A2, B2 … (uppercase role + 1-based index). |
| `turns[].tonesu` | yes | Tonesu notation (hyphens preserved). Multi-line OK with `\|`. |
| `turns[].gloss_line` | recommended | Morpheme-by-morpheme breakdown with English slots. |
| `turns[].natural` | yes | Fluent English reading. |
| `turns[].words_attested` | yes | Empty list `[]` on authoring; populated by `annotate_words_attested.py`. |
| `turns[].first_attests` | yes | Empty list `[]` on authoring; populated by `derive_first_attests.py`. |
| `turns[].notes` | optional | String or `null`. Brief parse note if needed. |

---

## Pipeline integration

`generate_conversations_page()` in `scripts/build_registry.py` reads
`corpus/conversations.yaml` exclusively. It uses: `cnum`, `gloss`, `scene`,
`turns[].turn`, `turns[].tonesu`, `turns[].natural`. The `.md` narrative
file is not read by the pipeline.

The generated page writes to:
`www/docs/totonesu/corpus/conversations/overview.md`

---

## After writing a conversation

1. Add the `.md` narrative to the current intake file (`c008-plus.md` or successor)
2. Add the YAML block to `corpus/conversations.yaml` (append to `conversations:` list)
3. Run `python scripts/build.py` to regenerate site pages
4. Verify the conversation appears at `totonesu/corpus/conversations/`
5. Update `corpus/conversations/index.md` — add a row to the file table if a new intake
   file was created, or update the summary column for the existing file
