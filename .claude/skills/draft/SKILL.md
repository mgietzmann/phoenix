---
name: draft
description: Converts a completed Sketch.md into a full prose draft document. Activate when the user says "draft the [section]", "write the draft for", "draft [path]", or otherwise asks to produce or continue a draft from a sketch.
metadata:
  author: marcelgietzmann-sanders
  version: "1.0"
allowed-tools: Read Write
---

# Draft

## When to activate

Activate when the user asks to draft a section from a sketch, e.g. "draft the introduction at `path/to/section/`".

## Steps

### 1. Confirm the sketch

Extract the project path from the user's message. Read `<project_path>/Sketch.md` and confirm with the user:

> "I'll be drafting from `<project_path>/Sketch.md`. Is that the right sketch?"

Wait for confirmation before proceeding.

### 2. Ask for the writing type

Ask the user:

> "What type of writing is this?" (e.g. introduction, methods, discussion, results)

Wait for their answer.

### 3. Load guidelines

Load `references/<type>.md` from within this skill's directory. If no file exists for that type, tell the user and note you'll proceed without guidelines, but recommend creating one after the session.

### 4. Read the current draft

Read `<project_path>/Draft.md` if it exists. If it doesn't, this is a fresh draft.

---

## Creating the Draft

### Core Rules

1. **No new content.** You cannot add facts, opinions, or ideas not present in `Sketch.md`. The sketch is your only raw material.
2. **No removal of content.** Every fact and point in the sketch must appear in the draft.
3. **Paragraph order is fixed.** The sequence of paragraphs must match the sketch.
4. **Full prose.** Replace all bullet points with complete, flowing sentences. The development section of each paragraph becomes real prose.
5. **Leads may be revised** — but only where flow or cohesion requires it. The substance of the lead must remain the same.

### Format

`Draft.md` uses this format:

```
**Type**: <writing type>

**Lead:** [topic sentence]
**Development:**
[Full prose paragraph — complete sentences, flowing naturally from the lead.]

**Lead:** [topic sentence]
**Development:**
[Full prose paragraph...]
```

### Writing

Once you have the guidelines and the sketch, produce the full draft immediately. Do not ask for permission or check in — draft the whole thing in one pass.

Apply the guidelines for the writing type. Use your full creative range within the constraints: combine sentences, vary rhythm, build transitions between paragraphs, and write prose that reads like finished work.

After writing `Draft.md`, reproduce the full draft inline in the chat so the user can review it without opening a separate file.

---

## Review Loop

After reproducing the draft in chat, ask the user to review it and provide comments.

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

- The draft is the artifact. Every decision is in service of producing prose that is ready to copy-paste into the final document.
- Do not hedge your writing choices — commit to them and let the review surface what doesn't work.
- When revising during review, make the minimum change that satisfies the comment. Don't rewrite surrounding sentences unless necessary.
- Keep citations exactly as they appear in the sketch (e.g. `(Lalli, 2006)`).
- Keep `Sketch.md` untouched throughout. The draft is a separate artifact.
