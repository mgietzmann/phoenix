---
name: sketch
description: Explains what a sketch is and how to interact with one. A sketch is a structured fact/idea gathering artifact in preparation for drafting, consisting of a Sketch.md (topic sentences with collapsible development blocks) and a Questions.md (questions in three states — new, developed, answered). Activate when working with, updating, or building a sketch; when the user references Sketch.md or Questions.md; or when a workflow involves developing material before drafting.
metadata:
  author: marcelgietzmann-sanders
  version: "2.0"
---

# Sketch

A sketch is a structured artifact for gathering facts, generating ideas, and synthesizing material **before** drafting begins. It has two files that always travel together:

- `Sketch.md` — the structure and content of the piece
- `Questions.md` — the questions driving its development

---

## Sketch.md

`Sketch.md` is a sequence of paragraphs-in-waiting, organized under section headers. Each paragraph consists of a **lead** (a plain topic sentence — the commitment the paragraph is making) followed immediately by its **development** in an indented blockquote.

The document uses markdown headers (`##`, `###`) to organize sections and subsections. Within each section, paragraphs are stacked with blank lines between them. Both headers and blockquotes are collapsible in VS Code, which allows the writer to focus on a section or level of detail at a time.

### Format

```
## Section Title

### Subsection Title (if needed)

[topic sentence — a single, concrete claim]
> Supporting
> - [development sentence or fact]
> - [development sentence or fact]


[next topic sentence]
> Supporting
> - [development sentence or fact]
```

The topic sentence is plain text — no `**Lead:**` prefix. The development block opens with `> Supporting` and each bullet is `> - ...`. There are no `---` separators between paragraphs; blank lines and collapsible blockquotes do the work.

### Rules

- Every lead must make a claim, not just name a topic.
- Development bullets are for capture, not style — rough is fine.
- Order of paragraphs reflects the intended sequence of the argument.
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

2. **Updating Sketch.md.** Add, remove, reorder, or revise lead sentences as needed. Add development bullets under the relevant lead. Never write prose — only topic sentences and bullet-point material. Never disturb existing development bullets unless the lead they belong to has changed substantially.

3. **Updating Questions.md.** Move questions between states as they progress (New → Developed → Answered). When a question is answered, record the answer inline. New questions can be added to the New section at any time.

4. **The sketch is the artifact.** Every action — gathering material, developing questions, synthesizing structure — is in service of the sketch. Keep it accurate and up to date.

---

## What a sketch is not

- It is not a draft. Do not write prose in `Sketch.md`.
- It is not a plan. It captures material and structure, not process.
- It is not finished when it feels complete — it's finished when drafting begins.
