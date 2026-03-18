---
name: diff-draft
description: Diffs a Draft.md file against the last git commit and walks through the changes section by section, summarizing what changed in plain language. Activate when the user wants to review draft changes, walk through a diff, see what changed in the draft, or go through changes section by section. Trigger phrases: "diff the draft", "walk through draft changes", "review draft changes", "what changed in the draft".
metadata:
  author: marcelgietzmann-sanders
  version: "2.3"
---

# Diff Draft

## When to activate

Activate when the user wants to review changes to a Draft.md — walking through them section by section with plain-language summaries.

## Steps

### 1. Find the Draft.md

Look for `Draft.md` in the current working directory or any subdirectory. If the user specifies a path, use that. If multiple are found, ask the user which one.

### 2. Extract both versions

Run the bundled script with the resolved Draft.md path:

```bash
python3 .claude/skills/diff-draft/scripts/get_headers.py <path-to-Draft.md>
```

If the script exits with an error (e.g. no commits, not a git repo), tell the user and stop.

### 3. Compare structure and clarify mapping

Show the user the old and new section headers side by side. If the headers are identical, the mapping is 1:1. If headers were added, removed, renamed, or reordered, show the discrepancy and ask the user to clarify what maps to what before proceeding.

### 4. Ask which section to start with

Present the list of new sections and ask: "Which section would you like to diff first?" Wait for the user's answer.

### 5. Extract and compare the chosen section

Run the bundled script with the Draft.md path, the new section name, and (if it was renamed) the old section name:

```bash
# Same name in old and new:
python3 .claude/skills/diff-draft/scripts/get_section.py <path-to-Draft.md> "Section Name"

# Renamed section (old name differs from new):
python3 .claude/skills/diff-draft/scripts/get_section.py <path-to-Draft.md> "New Name" "Old Name"
```

The script prints `=== OLD ===` and `=== NEW ===` blocks. Read both, then write a plain-language summary of what changed.

### 6. Summarise the section

Write a plain-language summary of what changed between old and new — what was cut, what was added, what was reworded, how the structure shifted. Focus on meaning and substance, not surface edits.

After summarising, offer to update the corresponding Sketch section to match (see **Sketch sync rules** below). If the user accepts, make all edits before moving on.

Then ask: "Next section, or would you like to discuss this one further?" Wait for the user's response.

### 7. Style digest

After the Sketch sync, offer to run a style digest for the section — a review of what the changes reveal about the writing guidelines.

**Steps:**

1. **Ask what type of writing this section is.** (e.g. "Introduction", "Discussion", "Methods") — don't assume from context or section name.
2. **Pull the matching reference file** from `.claude/skills/draft/references/`. If no file matches the type, tell the user and proceed without a baseline.
3. **Map the changes against the guidelines** using three buckets:
   - **Confirms** — changes that are already explained by an existing rule
   - **Contradicts** — changes that seem to go against an existing rule (raise these; they may reflect a deliberate choice or a rule that needs revision)
   - **Suggests new** — changes that aren't covered by any existing rule and may warrant a new one
4. **Propose candidate rules collaboratively.** For each "suggests new" or "contradicts" item, describe the pattern you observed and propose a principle — then wait for the user to confirm, refine, or dismiss it. Do not write rules directly. The user may identify that a change was a one-off mistake rather than a principle; in that case, drop it.
5. **Write agreed rules** into the reference file once the user confirms the wording.

### 8. Repeat for each section

Continue section by section at the user's direction. The user may say "next", name a specific section, or ask questions. Answer questions before moving on.

### 8. Close

After the last section (or when the user is done), let them know you've reached the end.

## Guidance on summarising changes

- **Trim vs. expand**: Note when content was cut (details removed, sentences shortened) vs. when new content was added.
- **Restructuring**: If paragraphs were reordered or merged, describe the new structure.
- **Tone/register shifts**: Note if language became more or less assertive, hedged, or precise.
- **Citations**: Note if citations were added, removed, or changed.
- **Don't quote long passages** — paraphrase and point to the key differences.

## Sketch sync rules

After diffing a section, offer to update the corresponding section of `Sketch.md` to match the new Draft. The Sketch tracks what the Draft *intends to say* — when the Draft changes, the Sketch should too. Apply these rules:

1. **Merged paragraphs → merge in the Sketch.** Combine the two `[paragraph]` blocks into one, merging their supporting bullets under the new combined topic sentence.

2. **Removed details → `[hidden]`, never deleted.** If the Draft drops a specific fact, figure, or mechanism, move it to its own bullet prefixed with `[hidden]`. Citations travel with the detail they belong to.

3. **Partially hidden bullets → split first.** If only part of a bullet is being hidden, split it into two lines before hiding one. Never hide half a bullet in-place.

4. **Changed topic sentences → update the Sketch topic sentence.** If the Draft rephrases or restructures the opening claim of a paragraph, update the `[paragraph]` line to match.

5. **New citations → add them to the relevant bullet.** If the Draft adds a citation that wasn't in the Sketch, add it to the bullet that contains the corresponding fact.

6. **Structural abstractions → split and hide the specific.** If the Draft replaces a specific mechanism with a more abstract statement, keep the abstract version as the bullet and add a `[hidden]` bullet below it with the specific detail.

7. **Dropped paragraph (standalone) → hide the whole block.** Prefix the `[paragraph]` line with `[hidden]` and leave all development points in place beneath it. Do not delete anything.

For **merges**: rule 1 applies — build the merged paragraph with the new topic sentence and carry the absorbed paragraph's bullets into it, hiding any that didn't make the cut. There is no need to also preserve the old paragraph block separately, since the merge is the new form of that content.

## Error handling

- If `git` is not available or the file is not in a git repo, say so and stop.
- If `git show HEAD` fails (no commits yet), tell the user and stop.
- If no `Draft.md` can be found, ask the user to provide the path.
- If a section name doesn't exist in the old draft, tell the user and ask how to proceed.
