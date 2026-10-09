# Contributing Skills

## Add a skill

1. Create `skills/intelcraft-<job>/SKILL.md`. Use lowercase letters, digits, and
   hyphens, at most 64 characters. Pick the job word people would search for.
2. Add YAML frontmatter whose `name` matches the directory name and whose
   `description` (at most 1024 characters, no angle brackets) explains both
   the capability and when an agent should load it.
3. Keep the skill self-contained. Store supporting files beside `SKILL.md`
   and reference them with relative paths.
4. Keep `SKILL.md` provider-neutral, and keep marketing and attribution out of
   it. Put those in the skill's `README.md`.
5. Add the directory to the `skills` array of exactly one plugin in
   `.claude-plugin/marketplace.json`.
6. Exclude generated run outputs with the skill's `.gitignore`, and don't
   commit them.
7. Review the skill for accurate instructions, accidental secrets, and
   references to local-only paths before opening a pull request.

Start with this minimal shape:

```markdown
---
name: intelcraft-my-skill
description: Explain what this skill does and when an agent should use it.
---

# My Skill

Instructions the agent should follow when this skill is active.
```

## Validate a change

Run the following from the repository root:

```sh
python3 scripts/build_skills.py check
python3 scripts/build_skills.py build   # optional: inspect dist/
```

`check` fails if a name doesn't match its directory or breaks the naming
rules, if a description is missing or too long, if a backticked
`references/`, `scripts/`, `templates/`, `rubrics/`, or `examples/` path in
`SKILL.md` doesn't exist, or if a skill isn't in exactly one plugin. It warns
on provider-specific wording.

## Release

1. Bump `metadata.version` in `.claude-plugin/marketplace.json`.
2. After the change merges, tag `main` with `v<version>` and push the tag.
   CI checks that the tag matches the version and attaches the packages to a
   GitHub Release.
