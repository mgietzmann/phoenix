---
name: assemble
description: Assembles multiple Draft.md files into a single Document.md, guided by a TOC.md. Activate when the user asks to assemble, compile, or build a complete document from drafts.
metadata:
  author: marcelgietzmann-sanders
  version: "2.0"
---

# Assemble

## When to activate

Activate when the user asks to assemble a document from drafts, e.g. "assemble the document at `path/to/docs/`" or "build the document from the drafts".

## Steps

### 1. Confirm the directory

Extract the directory path from the user's message. Confirm with the user:

> "I'll assemble `Document.md` using `<path>/TOC.md`. Is that the right directory?"

Wait for confirmation before proceeding.

### 2. Read the TOC and scan the folder structure

Read `<path>/TOC.md`. Also list the contents of `<path>` to find numbered top-level folders (e.g. `1-introduction`, `2-what-is-known`).

For any top-level folder that itself contains only subfolders (no `Draft.md`), list its contents to find numbered subfolders (e.g. `2.1-migration`, `2.2-searching`).

### 3. Build the section map

The TOC headers have no section numbers — folders are numbered only to keep them ordered on disk. Map headers to folders **by order**:

- Collect numbered top-level folders sorted by their leading number (e.g. `1-`, `2-`, `3-`, ...).
- Walk the TOC top-to-bottom. Each `##` header (in order) maps to the next top-level folder.
- Each `###` header (in order within its parent `##`) maps to the next numbered subfolder within that parent's folder.
- `#`-level lines are the document title — no folder.
- Non-header lines in the TOC are ignored.

For each entry, record:
- `level`: 1, 2, or 3
- `header`: exact header text from TOC (no leading `#` markers)
- `folder`: absolute path to the mapped folder, or `null` if it's the title (`#`)
- `has_draft`: `true` if `Draft.md` exists in that folder, else `false`

### 4. Run the assembly script

The skill directory contains `assemble.py` (at the base directory of this skill). Run it via Bash, passing the section map as a JSON string and the output path:

```
python3 <skill_base_dir>/assemble.py '<json_map>' <path>/Document.md
```

The script reads each `Draft.md`, strips lead/development labels, renders prose paragraphs, and writes `Document.md`. It prints a summary of filled and empty sections.

### 5. Report to the user

Share the summary printed by the script (sections filled, sections empty, names of empty sections).

---

## Guidance

- The Claude steps (2–3) are purely read-only mapping — no file writing, no draft reading.
- All file I/O (reading drafts, writing Document.md) happens in the Python script via Bash.
- Never modify or paraphrase draft content — preserve every word exactly, only remove structural labels.
- Never modify the header text from the TOC — use it exactly as written.
- The goal is faithful assembly, not editing.
