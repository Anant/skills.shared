---
name: intelcraft-skill-authoring
description: Create, update, and review portable agent skills for a shared skill collection. Use when adding a skill to a shared collection or improving an existing skill for team or community reuse.
---

# Shared Skill Authoring

## Create or update a skill

1. Use a lowercase, hyphenated directory name under `skills/`, at most 64
   characters. Shared skills use the collection's prefix (for example
   `intelcraft-<job>`), where the job word is what people would search for.
2. Create `SKILL.md` with `name` and `description` YAML frontmatter. The name
   must match the directory name. The description (at most 1024 characters, no
   angle brackets) says what the skill does and when to use it; agents choose
   skills from it, so put trigger keywords there rather than in the name.
3. Write instructions that state the expected inputs, workflow, and useful
   completion criteria. Keep the description specific enough to trigger only
   for relevant requests.
4. Put supporting files in the same directory and link to them with relative
   paths. Do not rely on a contributor's machine-specific paths, credentials,
   or unstated tools.
5. Keep instructions provider-neutral so the skill works in any agent that
   reads `SKILL.md`. Keep marketing and attribution out of `SKILL.md`; put them
   in the skill's README instead.
6. Add the directory to exactly one plugin's `skills` list in the collection's
   marketplace file (`.claude-plugin/marketplace.json`).
7. If the collection has a validator, run it (for example
   `python3 scripts/build_skills.py check`).

## Review checklist

- The frontmatter is valid and the name matches the directory.
- The description says both what the skill does and when to use it.
- Instructions are accurate, actionable, provider-neutral, and safe to run.
- Supporting content is necessary, contains no secrets or generated run
  outputs, and uses relative paths.
- The marketplace entry points to the skill directory.
