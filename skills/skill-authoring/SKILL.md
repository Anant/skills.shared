---
name: skill-authoring
description: Create, update, and review portable shared Claude skills. Use when adding a skill to a shared collection or improving an existing skill for team reuse.
---

# Shared Skill Authoring

## Create or update a skill

1. Use a lowercase, hyphenated directory name under `skills/`.
2. Create `SKILL.md` with `name` and `description` YAML frontmatter. The name
   must match the directory name.
3. Write instructions that state the expected inputs, workflow, and useful
   completion criteria. Keep the description specific enough to trigger only
   for relevant requests.
4. Put supporting files in the same directory and link to them with relative
   paths. Do not rely on a contributor's machine-specific paths, credentials,
   or unstated tools.
5. Add the directory to `.claude-plugin/marketplace.json` so Claude Code users
   can install it from this repository.

## Review checklist

- The frontmatter is valid and the name matches the directory.
- The description says both what the skill does and when to use it.
- Instructions are accurate, actionable, and safe to run.
- Supporting content is necessary, contains no secrets, and uses relative
  paths.
- The marketplace entry points to the skill directory.
