# Intelcraft Skills by Anant Labs

Agent skills from [Anant Corporation Labs](https://anant.co/labs). We use these
skills on our own client engagements, and we release them to the community
because Labs works open by default: we publish what we learn.

Intelcraft is the Labs practice that trains people to work with AI. These skills
are the same playbooks we teach: each one turns a piece of expert work, such as
screening a company, finding funding, answering an RFP, or curating a
knowledge base, into a repeatable workflow an agent can run.

Every skill is a directory with a `SKILL.md` file, the format read by Claude,
ChatGPT/Codex, and other agents that support [agent skills](https://agentskills.io).

## Skills

| Skill | Plugin | What it does |
| --- | --- | --- |
| [`intelcraft-domain-due-diligence`](skills/intelcraft-domain-due-diligence) | `intelcraft-growth` | Screens a company from its domain name alone and writes a scored, investment-style diligence memo from public data. |
| [`intelcraft-opportunity-finder`](skills/intelcraft-opportunity-finder) | `intelcraft-growth` | Finds, verifies, scores, and ranks grants, fellowships, awards, and other funding, ending in proposal handoff briefs. |
| [`intelcraft-rfp-responder`](skills/intelcraft-rfp-responder) | `intelcraft-growth` | Reads a solicitation and produces a compliance checklist, outline, and full draft proposal in the required structure. |
| [`intelcraft-notion-collector`](skills/intelcraft-notion-collector) | `intelcraft-knowledge` | Runs a Notion-backed collection harness: finds sources, collects and tags items, and holds them for human review. |
| [`intelcraft-skill-authoring`](skills/intelcraft-skill-authoring) | `intelcraft-knowledge` | Creates and reviews portable skills for a shared collection like this one. |

Download any skill or plugin from the
[latest release](https://github.com/Anant/skills.shared/releases/latest).

## Install

### Claude Code

```text
/plugin marketplace add Anant/skills.shared
/plugin install intelcraft-growth@anant-labs
/plugin install intelcraft-knowledge@anant-labs
```

On Claude Code 2.1.275 or later, one step also works:
`/plugin install intelcraft-growth --marketplace Anant/skills.shared`.

### Claude.ai and the Claude desktop app

Download `<skill>.zip` from the latest release, then upload it under
**Customize > Skills**.

### ChatGPT desktop and Codex

The ChatGPT desktop app and Codex read this repository's
`.claude-plugin/marketplace.json` as a marketplace, so add the repository as a
marketplace and install `intelcraft-growth` or `intelcraft-knowledge`. To
install a single skill instead, unzip `<skill>.zip` from the latest release into
`~/.agents/skills/`.

### Plugin directories and other agents

Each release includes `intelcraft-growth.zip` and `intelcraft-knowledge.zip`.
Each archive holds a portable `plugin.json`, a `.claude-plugin/plugin.json`, and
the plugin's skills under `skills/`. Upload these to plugin directories, or
copy a skill folder into any agent's skills directory.

## Build the packages

```sh
python3 scripts/build_skills.py check   # validate skills and marketplace.json
python3 scripts/build_skills.py build   # write dist/
```

`build` writes `dist/skills/<skill>.zip`, an identical `<skill>.skill`,
`dist/plugins/<plugin>.zip`, and `dist/SHA256SUMS`. It uses only the Python
standard library, and it skips files excluded by a skill's `.gitignore`.
The GitHub workflow runs the build on every pull request. When a `v*` tag
matching `metadata.version` in the marketplace file is pushed, it attaches the
packages to a GitHub Release.

## Repository layout

```text
.claude-plugin/marketplace.json  Marketplace: anant-labs, plugins and their skills
skills/<skill>/SKILL.md          One directory per skill
scripts/build_skills.py          Validator and packager
.github/workflows/skills.yml     Build on PRs, release on v* tags
CONTRIBUTING.md                  How to add or change a skill
```

## Work with Anant Labs

These skills are free and MIT-licensed. If you have a problem they don't
solve, especially one that has resisted the obvious approaches, that is what
[Anant Labs](https://anant.co/labs) is for. We run workshops and retainers, and
Intelcraft trains teams to build and run skills like these.

## License

[MIT](LICENSE)
