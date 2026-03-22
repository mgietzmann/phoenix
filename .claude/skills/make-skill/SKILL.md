---
name: make-skill
description: Create a new AgentSkill following the agentskills.io specification. Activate when the user asks you to "make a skill", "create a skill", or "add a skill" for a new capability.
compatibility: Designed for Claude Code
metadata:
  author: marcelgietzmann-sanders
  version: "1.0"
allowed-tools: Write Bash
---

# Make Skill

## When to activate

Activate when the user asks you to create, make, or add a new skill.

## Where to put skills

Place all new skills under `.claude/skills/<skill-name>/` unless the user specifies a different location.

## How to create a skill

### 1. Determine the skill name

The `name` must:
- Match the directory name exactly
- Be 1–64 characters, lowercase letters, numbers, and hyphens only
- Not start or end with a hyphen, and not contain consecutive hyphens (`--`)

### 2. Create the directory structure

```
.claude/skills/<skill-name>/
├── SKILL.md          # Required
├── scripts/          # Optional: shell/python scripts the agent runs
├── references/       # Optional: detailed docs loaded on demand
└── assets/           # Optional: templates, data files
```

### 3. Write SKILL.md

The file must have YAML frontmatter followed by Markdown instructions.

**Required frontmatter fields:**

| Field         | Notes                                                                 |
|---------------|-----------------------------------------------------------------------|
| `name`        | Must match directory name. Lowercase, hyphens only, max 64 chars.    |
| `description` | Max 1024 chars. Describe what the skill does AND when to activate it. |

**Optional frontmatter fields:**

| Field           | Notes                                                                 |
|-----------------|-----------------------------------------------------------------------|
| `license`       | License name or reference to a bundled LICENSE file.                  |
| `compatibility` | Environment requirements (tools needed, network access, etc.).        |
| `metadata`      | Arbitrary key-value map (e.g. `author`, `version`).                  |
| `allowed-tools` | Space-delimited list of pre-approved tools (experimental).            |

**Minimal template:**

```markdown
---
name: skill-name
description: What this skill does and when to use it.
---

# Skill Name

## When to activate

...

## How to use

...
```

**Full template:**

```markdown
---
name: skill-name
description: What this skill does and when to use it. Include trigger keywords.
compatibility: Requires curl and SOME_API_KEY in the environment.
metadata:
  author: marcelgietzmann-sanders
  version: "1.0"
allowed-tools: Bash Read
---

# Skill Name

## When to activate

Activate when...

## Steps

1. ...
2. ...

## Error handling

- If X is missing, tell the user and stop.
```

### 4. Body content guidelines

- Keep `SKILL.md` under 500 lines
- Recommended sections: activation conditions, step-by-step instructions, examples, edge cases, error handling
- Move lengthy reference material to `references/` files and link to them
- Scripts go in `scripts/`; reference them with relative paths from the skill root

### 5. Description field best practices

The description is the first thing loaded — it determines when the skill activates. Make it:
- Specific about what the skill does
- Rich with trigger keywords so activation happens reliably
- No longer than necessary (max 1024 chars)

### 6. After creating the skill

Tell the user:
- Where the skill was created
- What triggers it (the key phrases or conditions from the description)
- Any environment requirements (API keys, system tools)

---

## Designing a good skill

### Avoid whack-a-mole

Do not add a rule for every bad output. A laundry list of patches creates confusion and rarely produces coherent behavior. Instead: step back, identify what's going well and what isn't, find good abstractions. Sometimes that means consulting domain experts or books and encoding those insights. Aim for a small set of principles, not a long list of fixes.

### Collaborate with Claude on the skill itself

Don't hand Claude a document you wrote alone — things obvious to you will be opaque to it. When helping a user build a skill, ask: what makes sense here? what's confusing? how would you interpret this rule? Ask Claude to demonstrate how it would behave given the skill to surface mismatches before they become bad outputs.

### Build in a feedback mechanism

No non-trivial skill works perfectly off the bat. Build in a review step: examine what was created, what went well, what didn't. Use that to identify missing rules, bad abstractions, or gaps — then update the skill. Iterate until corrections become minor or disappear.

### Scope the workflow tightly

A skill for "write a paper" is doomed. A skill for "draft paragraphs in a section" can be made to work reliably. Small, bounded workflows produce tight feedback loops and skills that actually improve. Once individual steps work well, they can be composed — but only then.

### Design around atomic artifacts

Skills should operate on specific components and leave the rest alone. Monolithic generation feels fast but editing becomes catastrophic — if one section changes, nothing else should be touched. Encourage users to structure their work so each skill operates on one piece.

### Suit the user

The goal is not automation or raw intelligence — it is removing friction from workflows that bring out the user's best work. Ask: what does the user enjoy? what makes them effective? Design the skill around that, not just what is technically possible.

### Keep skills human-readable

A good skill must be a document a person can read, review, and understand. Collaborating on a skill is like collaborating on code — you need to review changes. As a skill grows, invest in structure and organization, not just content. A mature skill is effectively a guide to the domain.
