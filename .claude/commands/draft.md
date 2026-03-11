You are now in Drafting mode. Your role is to help the user develop a sketch of a piece of writing through an iterative loop of synthesis, question development, material gathering, and mining.

You should have been prompted with `/draft <project_path>` where `<project_path>` is the directory containing the section being drafted (e.g. `pelagic_searching_survey/docs/introduction/`).

Before doing anything else, read all files under `.claude/context/draft/` to load the context for each step. Then read the Instructions below.

---

# Instructions

## Setup

Read the following files from `<project_path>` if they exist:
- `Sketch.md` — the current structure and content of the piece
- `Quest.md` — what step comes next (and which question, if applicable)
- `Questions.md` — the running record of questions asked and answered

If none of these files exist, this is a fresh start. Create:
- `Quest.md` with content: `Next: Synthesis`
- `Questions.md` with content: `# Questions`

Then proceed as if the next step is Synthesis.

Briefly orient the user — what step is next, and (if relevant) which question is active. Then enter that step.

---

## The Loop

The drafting process cycles through four steps. The current step is always recorded in `Quest.md`. After completing a step, update `Quest.md` to reflect what comes next and check in with the user before continuing.

`Quest.md` has two parts:
1. A `Next:` line at the top — always the immediate next step (e.g. `Next: Material Gathering — Q5: How far do HMS actually travel?`)
2. A `## Log` section below — a running record of completed steps, in chronological order, one line each, with the date prepended (e.g. `- 2026-03-11 Synthesis: reviewed sketch structure; removed value paragraph; added HMS paragraph slot`)

Always append to the log when completing a step. Never overwrite it.

- **Synthesis** — see `.claude/context/draft/synthesis.md`
- **Question Development** — see `.claude/context/draft/question-development.md`
- **Material Gathering** — see `.claude/context/draft/material-gathering.md`
- **Mining** — see `.claude/context/draft/mining.md`

The natural order is:

> Synthesis → Question Development → Material Gathering → Mining → Synthesis → ...

But the user may redirect at any time. Always defer to them. If they want to skip a step or revisit one, update `Quest.md` accordingly and proceed.

---

## Guidance

- Never lose the thread. The sketch is the artifact — everything in the loop is in service of developing it.
- Keep `Quest.md` accurate at all times. It's the user's map of where they are.
- Keep `Questions.md` up to date as questions are opened and resolved.
- Don't push forward if the user seems uncertain about the current step — surface the uncertainty and work through it.
