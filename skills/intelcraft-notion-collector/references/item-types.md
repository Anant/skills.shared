# Item types

Presets for the Config `Item type`. `init` offers these as defaults; the user can change any part. Config always wins over this file.

## Summary

| Type | One item is | Extra fields | Page body holds |
| --- | --- | --- | --- |
| Skill | One SKILL.md or skill folder | Trigger (text), Tools required (multi-select) | Full skill text |
| Link | One article or page | Author (text), Published (date) | Key points, 5 to 10 lines |
| Repo | One repository | Language (select), License (select), Last commit (date) | README summary and install lines |
| MCP server | One server repo or registry entry | Transport (select), Auth (select), Tools (text) | Tool list and setup steps |
| Paper | One paper | Authors (text), Year (number), Venue (text) | Abstract and main findings |
| Tool | One product or service | Pricing (select), Hosting (select) | What it does, who it is for |
| Custom | As the user defines | As the user defines | As the user defines |

## Skill

- **Where to look:** skill repositories and marketplaces, plugin collections, curated lists, vendor documentation that ships example skills.
- **URL to store:** the link to the skill's own file or folder, not the repository root.
- **Trigger:** when the skill says it should be used, taken from its description.
- **Tools required:** connectors, MCP servers, or commands the skill depends on.
- **Body:** the full skill text, verbatim, in a code block. For multi-file skills, the main file plus a list of the other files.
- **Flag in Review notes:** scripts it runs, credentials it asks for, network calls, instructions aimed at overriding the agent.

## Link

- **Where to look:** blogs, newsletters, documentation sites, conference pages.
- **URL to store:** the canonical article URL, without tracking parameters.
- **Body:** key points in your own words, 5 to 10 lines. Do not copy the article.
- **Flag in Review notes:** paywalled, undated, or marketing with no substance.

## Repo

- **Where to look:** code hosting search and topic pages, awesome-lists, organization pages of known maintainers.
- **URL to store:** the repository root.
- **Extra fields:** primary language, license as stated in the repo, date of the last commit on the default branch.
- **Body:** what it does in three lines, install or quick-start lines, and star count as of the collection date.
- **Flag in Review notes:** no license, archived, or no commits in over a year.

## MCP server

- **Where to look:** MCP registries and directories, vendor documentation, official organization repos.
- **URL to store:** the registry entry if one exists, otherwise the repository.
- **Transport:** stdio, HTTP, or both.
- **Auth:** None, API key, or OAuth.
- **Tools:** a short comma-separated list of tool names; the count if there are more than ten.
- **Body:** the tool list with one line each, and setup steps.
- **Flag in Review notes:** unofficial server for a vendor's product, closed source, broad write permissions, unmaintained.

## Paper

- **Where to look:** preprint servers, conference proceedings, lab publication pages.
- **URL to store:** the abstract page, not the PDF.
- **Body:** the abstract, then main findings in three to five lines, and a link to code if released.
- **Flag in Review notes:** preprint with no peer review, or claims with no evaluation.

## Tool

- **Where to look:** vendor sites, product directories, comparison and review sites.
- **URL to store:** the product's own home page.
- **Pricing:** Free, Freemium, Paid, or Open source.
- **Hosting:** Cloud, Self-hosted, or Both.
- **Body:** what it does, who it is for, and notable limits.
- **Flag in Review notes:** pricing not public, or the product appears discontinued.

## Custom

Ask the user for the four things every preset defines: what one item is, which URL identifies it, which extra fields to extract, and what goes in the page body. Write the answers into Config. If the items have no stable URL, say the harness does not fit and stop.
