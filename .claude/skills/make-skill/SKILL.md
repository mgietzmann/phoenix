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
