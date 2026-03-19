# Project Design Guidelines

## Purpose
A project design section relays the why, what, and how of a design decision to stakeholders and implementers. Each paragraph leaves the reader with a clear understanding of what problem the design element solves, what it is, and how it works — in that order.

## Audience
Stakeholders and implementers. Both must be satisfied in the same prose — do not split motivation from mechanics into separate sections. Stakeholders need the motivation and high-level behavior; implementers need the precise structure and consequences.

## Tone
Precise and technical. Name things with their real names. Avoid vague qualifiers ("somewhat", "generally", "in some cases"). Avoid hedging. Commit to descriptions.

## Structure within each paragraph

### The lead establishes necessity
The lead should answer: what problem does this element solve, or what gap does it fill? A lead that only names and defines fails to motivate. The best leads state what the thing *is* and embed the reason for its existence in the same breath.

### Development unpacks structure and consequence
Development sentences follow this pattern:

1. **Unpack the components** — if the lead names parts ("key, version, global properties…"), the development explains the role of each.
2. **State the design consequence** — what does this structure enable or prevent? What becomes possible that wasn't before?
3. **Be concrete and specific** — use the actual names of things; avoid abstract restatements of the lead.

### Name things precisely
Use canonical names exactly as they appear in the design. Do not paraphrase or generalize.

### State architectural insights explicitly
If a design choice has a non-obvious consequence — a version field that enables dependency detection, a pointer that decouples identity from content — name that consequence directly. Do not leave it implicit.

## Paragraph-to-paragraph transitions
Design elements depend on each other. Make those dependencies explicit in how paragraphs connect — a reader should see the architecture emerge as they read.

## Preferred verbs
Prefer precise verbs over vague ones:
- Instead of "handles", "manages", "deals with": use "maps", "detects", "records", "retrieves", "pins", "tags"
- Instead of passive constructions that hide the actor: name what performs the action

## Length and elaboration

Prefer concise paragraphs. State the essential role, behavior, or mechanism and stop — do not unpack every consequence or add closing synthesis sentences that restate what the structure already implies. Trust the reader to draw inferences.

## What to avoid
- Restating the lead as the first sentence of development
- Vague motivation ("this is important because it helps")
- Passive constructions that obscure agency
- Hedged claims ("may", "can sometimes", "in certain cases") unless the hedge is a real property of the design
