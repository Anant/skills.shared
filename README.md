# Shared Claude Skills

This repository is the team source of truth for reusable Claude skills. Each
skill is a self-contained directory with a `SKILL.md` file, so it can be
reviewed, versioned, and shared through Git without a custom service.

## Available skills

| Skill | What it does |
| --- | --- |
| [anant-financial-domain-to-diligence](skills/anant-financial-domain-to-diligence/SKILL.md) | Analyzes a company from only its domain name and produces an investment-grade diligence memo with scores, via a 10-phase public-signal pipeline. |
| [anant-growth-opportunity-finder](skills/anant-growth-opportunity-finder/SKILL.md) | Finds, verifies, scores, and prioritizes grants, fellowships, awards, sponsorships, and research funding, ending in ranked shortlists and proposal handoff briefs. |
| [anant-sales-proposal-responder](skills/anant-sales-proposal-responder/SKILL.md) | End-to-end RFP/solicitation response workflow: extracts the scoring rubric, builds a compliance checklist, and drafts a complete proposal with cost and timeline estimates. |
| [skill-authoring](skills/skill-authoring/SKILL.md) | Creates, updates, and reviews portable shared Claude skills; also serves as the skill format example. |

## Use the skills

### Claude Code marketplace

Register this repository as a marketplace, then install the collection:

```text
/plugin marketplace add Anant/skills.shared
/plugin install shared-skills@anant-shared-skills
```

### Checked-out repository

Clone the repository and copy an individual skill into a project's Claude Code
skills directory:

```sh
git clone https://github.com/Anant/skills.shared.git
mkdir -p /path/to/project/.claude/skills
cp -R skills.shared/skills/skill-authoring /path/to/project/.claude/skills/
```

## Repository layout

```text
.claude-plugin/marketplace.json          Claude Code marketplace definition
skills/
  anant-financial-domain-to-diligence/   Domain-only company diligence memo pipeline
  anant-growth-opportunity-finder/       Funding and grant opportunity research
  anant-sales-proposal-responder/        RFP/solicitation response workflow
  skill-authoring/                       Skill authoring guidance and format example
CONTRIBUTING.md                          Review and authoring requirements
```

Each skill directory contains a `SKILL.md` plus any supporting references,
templates, or scripts. Every additional skill belongs in
`skills/<lowercase-hyphenated-name>/SKILL.md`.
Its YAML frontmatter must include a matching `name` and a `description` that
states both what the skill does and when Claude should use it.

## Distribution roadmap

Git and the Claude Code marketplace are the supported distribution mechanisms
today. The directory-per-skill layout keeps future options open without
duplicating the skill content.

1. **Skill registry:** select the team's registry and its versioning policy,
   then publish immutable tagged releases from this repository. Add registry
   metadata and automated publishing only after selecting the target registry.
2. **MCP resources:** provide a read-only MCP server that discovers the same
   `skills/*/SKILL.md` files and exposes them as stable `skills://<name>`
   resources. Start with `resources/list` and `resources/read`; keep skill
   instructions separate from any executable MCP tools.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the process for adding a skill.
