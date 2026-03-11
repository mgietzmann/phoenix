# Mining

Mining is the extraction step. The user has been working in NotebookLM with the assembled sources and the active question. Now the goal is to pull out what matters and get it into the sketch.

---

## What You're Doing

You are helping the user sort through what NotebookLM returned — identifying what's genuinely useful, discarding what isn't, and turning raw findings into development sentences that slot into the sketch.

---

## How to Run This Step

Start by reading `Sketch.md` and `Quest.md` to confirm the active question and remind yourself of the current sketch structure.

Then ask the user to share what they found. This might be:
- Direct answers to the question
- Interesting tangents that came up
- Surprises — things that contradicted what they expected
- Gaps — things they couldn't find answers to

### 1. Evaluate What Came Back

Work with the user to assess what's worth keeping:
- Does it directly address the active question?
- Does it support, complicate, or challenge something already in the sketch?
- Is it specific enough to become a development sentence, or is it still too vague?
- Is it a fact, a finding, a mechanism, a debate, or a definition? That affects how it gets used.

Don't slot everything in. Help the user be selective — the sketch should get sharper, not just longer.

### 2. Turn Findings into Development Sentences

For each piece of material worth keeping, help the user turn it into a development sentence — a concrete, specific claim or piece of information that supports the topic sentence it sits under.

A good development sentence:
- Says something specific (not "research shows that X is important" but "X does Y under Z conditions")
- Earns its place under the topic sentence it serves
- Doesn't introduce a new argument — it develops the existing one

If a finding doesn't fit under any existing topic sentence, that's a signal for Synthesis — hold it and flag it.

### 3. Update the Sketch

As development sentences are agreed on, add them to `Sketch.md` under the relevant topic sentences.

If anything came back that meaningfully changes the picture — something that suggests the structure needs revisiting — flag it explicitly. Don't try to force it into the existing sketch. Note it and let Synthesis deal with it.

---

## Outcome

`Sketch.md` updated with new development sentences under the relevant topic sentences.

`Questions.md` updated: move the active question from `## Active` to `## Answered` with a one-line note on what was found or learned.

Update `Quest.md`:
- Set the `Next:` line: `Next: Synthesis`
- Append a one-line summary to the `## Log` section (e.g. `- Mining: Q5 — 3 development sentences added to HMS paragraph; question closed`)

---

## Guidance

- Mining can turn up things that break the sketch. That's a good outcome, not a bad one — it means the loop is working.
- Keep the user moving. It's easy to get lost in interesting material. Keep asking: does this go in the sketch? Under which topic sentence?
- If the user is unsure where a finding belongs, read the topic sentences together and reason through it.
- If nothing useful came back, that's worth noting too. Was the question poorly aimed? Were the sources wrong? Take that back into Question Development or Material Gathering.
