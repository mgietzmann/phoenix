---
name: sketch
description: Explains what a sketch is and how to interact with one. A sketch is a structured fact/idea gathering artifact in preparation for drafting, consisting of a Sketch.md (topic sentences with collapsible development blocks) and a Questions.md (questions in three states — new, developed, answered). Activate when working with, updating, or building a sketch; when the user references Sketch.md or Questions.md; or when a workflow involves developing material before drafting.
metadata:
  author: marcelgietzmann-sanders
  version: "3.2"
---

# Sketch

A sketch is a structured artifact for gathering facts, generating ideas, and synthesizing material **before** drafting begins. It has two files that always travel together:

- `Sketch.md` — the structure and content of the piece
- `Questions.md` — the questions driving its development

---

## Sketch.md

`Sketch.md` is a sequence of typed objects, organized under section headers. Every object begins with a **type tag** in square brackets that declares what kind of content it is. The type tag tells any tool processing the sketch what kind of output each entry should produce.

The document uses markdown headers (`##`, `###`) to organize sections and subsections. Objects are stacked with blank lines between them. Both headers and blockquotes are collapsible in VS Code, which allows the writer to focus on a section or level of detail at a time.

### Supported object types

- **`[paragraph]`** — a prose argument unit. Consists of a topic sentence (the claim the paragraph is making) followed by a `> Supporting` blockquote with development bullets.
- **`[table]`** — a schema or data structure unit. Consists of a description of what the table represents, followed by the markdown table as the body, then an optional `> Notes` blockquote with clarifying notes.
- **`[code]`** — a code example unit. Consists of a language identifier and description on the same line as the tag, followed by a fenced code block.
- **`[enumeration]`** — a named list unit. Consists of a lead sentence introducing the set, followed by a `> Supporting` blockquote where each bullet is a named, parallel item. Use when the content is a set of distinct items a reader would scan rather than read linearly.
- **`[diagram]`** — a diagram unit. Consists of a short descriptive label, followed by an optional `> Notes` blockquote with drawing decisions (which nodes to include, how to group them, edge labels, annotations, scale, sequence, title overrides). Use when a relationship, hierarchy, or system boundary is more efficiently communicated visually than in prose.
- **`[abstract]`** — a placeholder for an abstract. No content follows the tag — the abstract is synthesized from the finished draft at drafting time, not written in the sketch. Use at the top of the sketch to reserve the abstract's position in the document.
- **`[references]`** — a reference list. The file path to the `.bib` file containing the raw citation data follows the tag on the same line.

### Annotations

Annotations are inline markers that can appear anywhere in the sketch — before any object or before any development bullet — to modify how that content is treated.

- **`[hidden]`** — marks content that has been captured but should not appear in the draft. It is a suppression signal, not a communication type. It can prefix any object (hiding the whole thing) or any development bullet (hiding just that detail). The content remains in the sketch for completeness and future reference; the drafter treats anything marked `[hidden]` as invisible.

```
[hidden] [paragraph] a whole paragraph that should not be drafted

> - [hidden] a single bullet that should not be drafted
```

### Format

```
## Section Title

### Subsection Title (if needed)

[paragraph] topic sentence — a single, concrete claim
> Supporting
> - [development sentence or fact]
> - [development sentence or fact]


[table] description of what the table represents
| col | col |
| --- | --- |
| val | val |
> Notes
> - [clarifying note]


[code] language — description of what the example illustrates
```language
...code...
```


[diagram] short descriptive label
> Notes
> - [drawing decision]
> - [drawing decision]


[abstract]


[references] path/to/references.bib
```

The type tag is always the first thing on the line. For `[paragraph]`, the topic sentence follows on the same line. For `[table]`, the description follows on the same line and the markdown table comes immediately after. For `[code]`, the language and description follow on the same line and the fenced code block comes immediately after. For `[diagram]`, the label follows on the same line and the optional `> Notes` blockquote comes immediately after. For `[abstract]`, nothing follows the tag. For `[references]`, the file path follows on the same line. There are no `---` separators between objects; blank lines and collapsible blockquotes do the work.

### Rules

- Every object must have an explicit type tag. There are no untagged entries.
- Every `[paragraph]` lead must make a claim, not just name a topic.
- Development bullets are for capture, not style — rough is fine.
- Order of objects reflects the intended sequence of the argument.
- Do not write prose in `Sketch.md`. That belongs in `Draft.md`.

---

## Questions.md

`Questions.md` is a running record of the questions driving the sketch forward. It has three sections, one per question state:

### New

Questions that have been identified but not yet developed. They may be rough, half-formed, or speculative. They exist to be captured, not answered yet.

### Developed

Questions that have been sharpened and are ready to be answered. A developed question is specific enough that you know what a good answer looks like and where to look for it.

### Answered

Questions with answers. The answer is recorded inline below the question. Answered questions are the primary source of new development bullets in `Sketch.md`.

### Format

```
## New

- [question]
- [question]

## Developed

- [question]
- [question]

## Answered

- [question]
  **Answer:** [answer — can be multi-line]

- [question]
  **Answer:** [answer]
```

---

## How to interact with a sketch

When working with a sketch in any workflow:

1. **Read both files first.** Always read `Sketch.md` and `Questions.md` before making any changes. The current state of both files is your ground truth.

2. **Updating Sketch.md.** Add, remove, reorder, or revise objects as needed. Add development bullets under the relevant `[paragraph]` lead. Never write prose — only topic sentences and bullet-point material. Never disturb existing development bullets unless the lead they belong to has changed substantially. All entries must have explicit type tags.

3. **Updating Questions.md.** Move questions between states as they progress (New → Developed → Answered). When a question is answered, record the answer inline. New questions can be added to the New section at any time.

4. **The sketch is the artifact.** Every action — gathering material, developing questions, synthesizing structure — is in service of the sketch. Keep it accurate and up to date.

---

## What a sketch is not

- It is not a draft. Do not write prose in `Sketch.md`.
- It is not a plan. It captures material and structure, not process.
- It is not finished when it feels complete — it's finished when drafting begins.
