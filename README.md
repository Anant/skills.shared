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

Every release has a download for each skill and each plugin. Pick the section
for the app you use.

| App | What to install | How |
| --- | --- | --- |
| Claude Code | Plugin | Add the marketplace from this repo |
| Claude (web and desktop app) | Plugin, or one skill at a time | Add the marketplace from this repo, or upload a `.zip` |
| ChatGPT desktop app | Plugin or skill | Add the marketplace, or copy a skill folder |
| ChatGPT on the web | Plugin | Install a plugin that your workspace published or imported |

### Claude Code

```text
/plugin marketplace add Anant/skills.shared
/plugin install intelcraft-growth@anant-labs
/plugin install intelcraft-knowledge@anant-labs
```

On Claude Code 2.1.275 or later you can do it in one step:
`/plugin install intelcraft-growth --marketplace Anant/skills.shared`.

<!-- TODO(screenshot): docs/images/claude-code-plugin-install.png showing /plugin install intelcraft-growth@anant-labs -->

### Claude on the web (claude.ai) and the Claude desktop app

The steps are the same on the web and in the desktop app's Chat and Cowork
tabs. Plugins you add are saved to your Claude account, so they also show up in
Claude Code (v2.1.273 or later) when you sign in with that account.

**Add the marketplace (Pro, Max, Team, and Enterprise plans)**

1. Open **Customize** in the left sidebar, then the **Plugins** tab.
2. Choose **Add > Add marketplace** and enter `Anant/skills.shared`, or the full
   URL `https://github.com/Anant/skills.shared`.
3. Open **intelcraft-growth** or **intelcraft-knowledge** and click **Add**.
4. In a chat, type `/` or click **+** to pick an Intelcraft skill. You can also
   just describe the task, and Claude uses the matching skill.

To pick up new releases, open the marketplace and choose **Check for updates**,
or turn on **Sync automatically**. On Team and Enterprise plans, an Owner
decides whether members can add their own marketplaces.

<!-- TODO(screenshot): docs/images/claude-add-marketplace.png showing Customize > Plugins > Add > Add marketplace with Anant/skills.shared -->
<!-- TODO(screenshot): docs/images/claude-plugin-added.png showing intelcraft-growth after it is added -->

**Upload a file instead**

- **Plugin:** choose **Add > Upload plugin** and pick `intelcraft-growth.zip`
  or `intelcraft-knowledge.zip` from the
  [latest release](https://github.com/Anant/skills.shared/releases/latest).
- **Single skill (any plan, including Free):** turn on **Code execution and
  file creation** under **Settings > Capabilities**. Then open
  **Customize > Skills**, click **+**, choose **Create skill > Upload a skill**,
  and pick the skill's `.zip`, for example `intelcraft-notion-collector.zip`.

See Anthropic's guides [Plugins](https://claude.com/docs/plugins/overview),
[Use plugins in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude),
and [Use skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude).

<!-- TODO(screenshot): docs/images/claude-upload-skill.png showing Customize > Skills > + > Upload a skill -->

### ChatGPT desktop app (and Codex)

The ChatGPT desktop app reads this repository's
`.claude-plugin/marketplace.json`, so you can install the plugins directly.

1. Add the marketplace. Run this in a terminal with the Codex CLI:

   ```sh
   codex plugin marketplace add Anant/skills.shared
   ```

2. Restart the ChatGPT desktop app and open the **Plugins** tab.
3. Choose the **anant-labs** marketplace, open **intelcraft-growth** or
   **intelcraft-knowledge**, and click **+** to install it.
4. Start a new chat. Describe the task, or type `@` to pick a skill, for example
   `@intelcraft-rfp-responder`.

To install one skill without a plugin, unzip its `.zip` from the
[latest release](https://github.com/Anant/skills.shared/releases/latest) into
`~/.agents/skills/`. You should end up with
`~/.agents/skills/intelcraft-rfp-responder/SKILL.md`. The skill then appears
under **Skills** in the sidebar. In Codex CLI, type `$` to mention it.

See OpenAI's guides [Plugins](https://developers.openai.com/codex/plugins) and
[Build skills](https://developers.openai.com/codex/skills).

<!-- TODO(screenshot): docs/images/chatgpt-desktop-plugins-marketplace.png showing the anant-labs marketplace in the Plugins tab -->
<!-- TODO(screenshot): docs/images/chatgpt-desktop-at-skill.png showing @intelcraft-... in the prompt box -->

### ChatGPT on the web

ChatGPT on the web doesn't load standalone skills. It uses skills only when they
come bundled in a plugin, so you install `intelcraft-growth` or
`intelcraft-knowledge` from the **Plugins** tab at
[chatgpt.com/plugins](https://chatgpt.com/plugins).

- **Workspace plans:** an admin can import this GitHub marketplace under
  **Admin > Plugins**, or publish a plugin from **Personal > ... > Publish**
  after adding it in the desktop app. The plugins then appear under your
  workspace's tab in the Plugins Directory.
- **Personal accounts:** add the plugins in the desktop app first (see above).
  Plugins from personal marketplaces are listed under **Personal** in the
  Plugins Directory.

Once a plugin is installed, start a new chat and type `@` to pick an Intelcraft
skill.

<!-- TODO: Submit intelcraft-growth and intelcraft-knowledge to the public Plugins Directory (https://developers.openai.com/plugins/deploy/submission), then replace this section with a direct install link. -->
<!-- TODO(screenshot): docs/images/chatgpt-web-plugins-tab.png showing the Intelcraft plugin in chatgpt.com/plugins -->

### Other agents and plugin directories

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
