---
name: draft
description: Drafts a section of a document by converting the corresponding section of Sketch.md into prose and inserting it into Draft.md. Activate when the user says "draft the [section]", "write the draft for", "draft [path]", or otherwise asks to produce or continue a draft from a sketch.
metadata:
  author: marcelgietzmann-sanders
  version: "3.0"
---

# Draft

## When to activate

Activate when the user asks to draft a section from a sketch, e.g. "draft the Introduction" or "draft the Migration section". The user works one section at a time; `Draft.md` is a single document that accumulates sections as they are drafted.

## Steps

### 1. Confirm the sketch and section

Extract the project path and the target section from the user's message. Read `<project_path>/Sketch.md` and confirm with the user:

> "I'll be drafting the **[Section]** section from `<project_path>/Sketch.md`. Is that right?"

Wait for confirmation before proceeding.

### 2. Ask for the writing type (prose sections only)

Scan the target section in `Sketch.md` for `[paragraph]` objects. If any are present:

Ask the user:

> "What type of writing is this?" (e.g. introduction, methods, discussion, results)

**Exception:** if the section being drafted is `[abstract]` (no topic sentence, no supporting bullets), infer the type as `abstract` automatically and skip this question.

If no `[paragraph]` objects are present, skip this step.

### 3. Ask for the drawing style (diagram sections only)

Scan the target section in `Sketch.md` for `[diagram]` objects. If any are present:

Ask the user:

> "What drawing style?" (e.g. `conceptual_map`, `system_context`)

Available styles (reference files in `references/`): `conceptual_map`, `system_context`. If the user names a style with no corresponding reference file, proceed without guidelines and recommend creating one after the session.

If no `[diagram]` objects are present, skip this step.

### 4. Ask for the output format (prose sections only)

If `[paragraph]` objects are present, ask the user:

> "What output format?" (default: markdown)

Common options: markdown, LaTeX. If the user doesn't specify, proceed with markdown.

Diagrams are always rendered as SVG. No format question is needed for `[diagram]` objects.

### 5. Load guidelines

- For prose: load `references/<writing_type>.md` from within this skill's directory.
- For diagrams: load `references/<drawing_style>.md` from within this skill's directory.

If no file exists for a requested prose type, tell the user and note you'll proceed without guidelines, but recommend creating one after the session.

### 6. Read the current draft

Read `<project_path>/Draft.md` if it exists. Identify whether the target section is already present in the draft. If it is, you will replace it; if it isn't, you will add it.

---

## Creating the Draft

### Identifying objects in Sketch.md

The sketch is organized with markdown headers (`##`, `###`). Locate the header that matches the section the user named and extract all objects under it (down to, but not including, the next same-level or higher header).

Each object begins with a type tag: `[paragraph]`, `[references]`, etc. Process each object according to its type (see Object Rendering below).

### Core Rules

1. **No new content.** You cannot add facts, opinions, or ideas not present in the sketch section. The sketch is your only raw material. **Exception: `[abstract]` sections** — these are synthesized from the finished draft (see Object Rendering).
2. **No removal of content.** Every fact and point in the sketch section must appear in the draft.
3. **Object order is fixed.** The sequence of objects must match the sketch.
4. **Full prose for paragraphs.** The lead sentence opens the paragraph; the development bullets become the flowing sentences that follow it. The result is a single, complete paragraph per `[paragraph]` object.
5. **Leads may be revised** — but only where flow or cohesion requires it. The substance of the lead must remain the same.
6. **Do not repeat the lead.** The lead opens the paragraph; the development prose continues from it. Never restate the lead at the start of the development text.

### Object Rendering

**`[paragraph]`** — render as prose. The lead sentence opens the paragraph; development bullets become the flowing sentences that follow.

**`[abstract]`** — this object has no sketch content. Instead, read the full `Draft.md` (excluding any existing abstract placeholder) and synthesize a self-contained abstract from the finished sections. Apply the abstract guidelines. This is the one object type where the source material is the draft, not the sketch.

**`[diagram]`** — render as a standalone SVG file. The sketch entry consists of a short descriptive label followed by an optional `> Notes` block:

```
[diagram] The hierarchy of search.
> Notes
> - bullet specifying nodes, edges, groupings, labels, annotations
> - bullet specifying scale, sequence, or other drawing decisions
```

The label is a working description of the diagram; the surrounding sketch sections provide the underlying content and relationships. The notes add to this — encoding specific drawing decisions (which nodes to include, how to group them, what edge labels to use, what annotations to add, and any title override) that go beyond what the surrounding sections make obvious. Read all three sources together: surrounding sections for content, notes for drawing specification.

Apply the drawing style guidelines to produce a complete, self-contained SVG. Derive a short slug from the label for the filename (e.g. `hierarchy_of_search.svg`). If the notes specify a title, use that as the figure title; otherwise use the label. Save the file to `<project_path>/figures/<slug>.svg`.

Insert the following at the corresponding position in `Draft.md`:

```markdown
![<title>](figures/<slug>.svg)

*Figure N: <figure description — one or two sentences explaining what the diagram shows and why it is included.*
```

The figure description is prose, written to the same standard as the rest of the draft. It should tell a reader who has not yet looked at the diagram what it shows and what to take from it.

**`[enumeration]`** — render as a lead sentence followed by a markdown list. The lead introduces the set; each development bullet becomes a list item, with the bolded name of the item followed by an em dash and a concise description. Use this type when the sketch content is a set of named, parallel items that a reader would scan rather than read linearly.

**`[references]`** — read the `.bib` file at the path specified in the sketch entry. Render the references according to the output format:
- *markdown*: a formatted reference list (author, year, title, journal, etc.), one entry per line
- *LaTeX*: `\bibliography{<filename>}` and `\bibliographystyle{<style>}` commands

### Format

`Draft.md` is a single prose document with section headers matching the sketch:

```
## Section Title

[Paragraph one — full prose, lead sentence followed by development.]

[Paragraph two — full prose.]

### Subsection Title

[Paragraph...]

## References

[Formatted reference list or LaTeX bibliography command]
```

There are no `**Lead:**` or `**Development:**` labels in the draft. It is clean prose and rendered objects under headers.

### Inserting into Draft.md

- **New section:** append the drafted section under the correct header at the appropriate position in the document (matching the order in the sketch).
- **Replacing existing section:** locate the section in `Draft.md` by its header and replace everything from that header down to the next same-level or higher header with the new prose.

### Writing

Once you have the guidelines and the sketch section, produce the full draft for that section immediately. Do not ask for permission or check in — draft the whole section in one pass.

Apply the guidelines for the writing type. Use your full creative range within the constraints: combine sentences, vary rhythm, build transitions between paragraphs, and write prose that reads like finished work.

After writing `Draft.md`, reproduce the drafted section inline in the chat so the user can review it without opening a separate file.

---

## Review Loop

After reproducing the section in chat, ask the user to review it and provide comments.

When working through a specific paragraph during review, reproduce that paragraph in the chat after each revision so the user can read it inline.

Work through their comments one at a time, revising the draft as instructed. Repeat until the user is satisfied.

---

## Guidelines Update

Once the user is happy with the draft:

1. Compare the final draft with what you originally produced. Identify the patterns in what changed — word choices, sentence structures, transitions, rhythm, emphasis, anything.
2. Draft additions or revisions to `references/<type>.md` that would help produce a better first draft next time.
3. Present these proposed additions to the user for review.
4. Work through any feedback on them.
5. Apply the agreed additions to the guidelines file.

The goal of this step is to close the gap between the initial draft and the final — so that over time, the first draft requires fewer revisions.

---

## Guidance

- The draft is the artifact. Every decision is in service of producing prose that is ready to read in the final document.
- Do not hedge your writing choices — commit to them and let the review surface what doesn't work.
- When revising during review, make the minimum change that satisfies the comment. Don't rewrite surrounding sentences unless necessary.
- Keep citations exactly as they appear in the sketch (e.g. `(Lalli, 2006)`).
- Keep `Sketch.md` untouched throughout. The draft is a separate artifact.
