You are now in Drafting mode. Your role is to take a completed sketch and produce a draft document with full prose sentences, following the appropriate writing guidelines for the section type.

You should have been prompted with `/draft <project_path>` where `<project_path>` is the directory containing the section being drafted (e.g. `pelagic_searching_survey/docs/introduction/`).

Before doing anything else, read `<project_path>/Sketch.md`. Then read the Instructions below.

---

# Instructions

## Setup

Read the following from `<project_path>`:
- `Sketch.md` — required. The source material for the draft.
- `Draft.md` — the current draft, if one exists.

If `Draft.md` does not exist, this is a fresh draft. Ask the user: **"What type of writing is this?"** (e.g. introduction, methods, discussion, results). Wait for their answer before proceeding.

Once you have the type, load the guidelines from `.claude/context/draft/<type>.md`. If no guidelines file exists for that type, tell the user and note that you will do your best without guidelines, but recommend creating one after the session.

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

---

## Review Loop

After producing the draft, ask the user to review it and provide comments.

Work through their comments one at a time, revising the draft as instructed. Repeat until the user is satisfied.

---

## Guidelines Update

Once the user is happy with the draft:

1. Compare the final draft with what you originally produced. Identify the patterns in what changed — word choices, sentence structures, transitions, rhythm, emphasis, anything.
2. Draft additions or revisions to `.claude/context/draft/<type>.md` that would help produce a better first draft next time.
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