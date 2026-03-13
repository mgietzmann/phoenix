---
name: digest
description: Digests a voice recording into a sketch — transcribing it, reading the current sketch and questions for context, proposing changes, and updating the files after review. Use when the user returns from a walk or session with a voice recording containing thoughts on a sketch. Activate when the user references an audio file alongside a sketch, or asks to digest a recording.
metadata:
  author: marcelgietzmann-sanders
  version: "1.0"
allowed-tools: Read Write
---

# Digest

## When to activate

Activate when the user has a voice recording containing thoughts about a sketch and wants to integrate those thoughts into `Sketch.md` and `Questions.md`.

---

## Steps

### 1. Confirm sketch and audio

Before doing anything, confirm with the user:
- Which sketch are we working with? (the project path)
- Which audio file are we digesting?

If either is ambiguous, ask. Don't proceed until both are clear.

### 2. Transcribe

Use the `voice-transcribe` skill to pull the transcript into context.

### 3. Read the sketch

Read `Sketch.md` and `Questions.md` from the project path. Absorb the current state — the argument's shape, what's developed, what's thin, what questions are active — before forming any proposals.

### 4. Propose changes

Work through the transcript and propose changes in three passes, presented in order:

**A. Structural changes to Sketch.md**
Reordering of paragraphs, new Lead sentences, revised Lead sentences, removed paragraphs. These are the highest-stakes changes — get the shape right before filling it in.

**B. New or updated development bullets**
New bullets to add under existing Leads, revisions to existing bullets, removals. Attribute each to the relevant Lead.

**C. Questions**
New questions to add to `Questions.md` (under New), updates to existing questions, questions that can be moved to Answered if the recording addressed them.

For each proposed change, flag its source:
- **Explicit** — the user said this directly in the recording
- **Inferred** — implied by what was said; flag the reasoning so the user can accept or reject it

Present all proposals before making any changes. Don't edit files yet.

### 5. Review

Work through the proposals with the user. They may accept, reject, modify, or redirect. Take one section at a time (structure first, then bullets, then questions) but follow the user's lead if they want to jump around.

### 6. Update

Once the user is satisfied, apply all agreed changes to `Sketch.md` and `Questions.md` in one pass.

### 7. Skill improvement (if warranted)

If there was significant back-and-forth in step 5 — multiple rounds of revision, proposals that missed the mark, or patterns in what needed correcting — work with the user to identify what would have reduced that friction.

Ask:
- Were there types of proposals that consistently needed adjustment? Why?
- Were there things I missed that I should have caught?
- Were there things I inferred that I shouldn't have, or vice versa?

Propose specific updates to this skill's `SKILL.md` that would improve synchrony next time. Review them with the user, then apply the agreed changes.

If the session was smooth, skip this step.

---

## Guidance

- The transcript is raw material, not a transcript of decisions. The user was thinking out loud — treat it that way. Some things said will be firm; others will be exploratory. Surface the distinction where you can.
- Inferences are valuable but must be flagged clearly. Don't silently absorb something the user didn't explicitly say.
- Keep the sketch's current argument in view throughout. A proposed change that adds material but muddies the conveyance is not an improvement.
- After updates, the sketch should feel like it moved forward — not just got longer.
