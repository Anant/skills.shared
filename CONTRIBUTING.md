# Contributing Skills

## Add a skill

1. Create `skills/<lowercase-hyphenated-name>/SKILL.md`.
2. Add YAML frontmatter whose `name` matches the directory name and whose
   `description` explains both the capability and when Claude should load it.
3. Keep the skill self-contained. Store any supporting files beside `SKILL.md`
   and reference them with relative paths.
4. Add the new directory to the `skills` array in
   `.claude-plugin/marketplace.json`.
5. Review the skill for accurate instructions, accidental secrets, and
   references to local-only paths before opening a pull request.

Start with this minimal shape:

```markdown
---
name: my-skill
description: Explain what this skill does and when Claude should use it.
---

# My Skill

Instructions Claude should follow when this skill is active.
```

## Validate a change

Run the following from the repository root:

```sh
python3 -m json.tool .claude-plugin/marketplace.json >/dev/null
```

Then confirm that each path listed in the marketplace exists and contains a
`SKILL.md` file, and that its frontmatter name matches its directory name.
