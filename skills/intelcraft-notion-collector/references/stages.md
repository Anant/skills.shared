# Stages

Step-by-step procedure for each command. Before any of them, do the four start-of-run steps in `SKILL.md`.

## init

Ask these in one message. Offer the preset defaults from `item-types.md` for the chosen item type so the user can accept them in a word.

1. Topic, in a phrase.
2. Item type: skill, link, repo, MCP server, paper, tool, or custom.
3. What counts as one item.
4. Extra fields to extract per item.
5. Tag vocabulary: a seed list, or open.
6. Review criteria: what should be flagged for rejection.
7. Where in Notion to create it (parent page), or workspace top level.

Before creating anything, search Notion for an existing `<Topic> Collection` page. If one exists, stop and ask whether to reuse it.

Then create, in order, per `schema.md`:

1. Home page titled `<Topic> Collection`.
2. Config page inside it.
3. Sources database inside it.
4. Items database inside it, with the extra fields added as columns.
5. The Pipeline and To review views on Items.

Report the home page link and stop. Do not run Explore unless asked.

## explore

1. Read all Sources rows, including Dead. These are the exclusion list.
2. Search the web for places that publish items of the Config type on the Config topic. Use the "Where to look" hints in `item-types.md`. Prefer primary places (registries, official repos, maintained lists) over aggregators and listicles.
3. Open each candidate to confirm it exists and actually lists items.
4. Add up to `Sources per explore` new rows: Name, URL, Type, Seek method, Status = Proposed, Added by = Agent, and one line in Notes on why it is worth watching.
5. Report what was added, and remind the user to set the ones they want to Active.

Never set a source to Active.

## seek

1. Query Sources where Status = Active. If none, say so and point to the Proposed rows.
2. Load the URL of every existing Items row once, in every status, normalized per the Dedupe rule.
3. For each source, open it and find up to `Items per source per seek` items matching Config `One item is`.
4. Skip any item whose normalized URL is already in Items. Rejected rows count; do not collect them again.
5. Create a row per new item: Name, URL, Type, Source (relation), Status = New, Collected at = today, and any extra fields that can be read directly from the page. Put the content in the page body per `item-types.md`.
6. Set Last sought = today on each source processed.
7. Report items added per source, items skipped as already present, and sources that could not be read. Suggest Paused for unreadable sources; do not change it.

Leave Domain, Tags, and Summary empty. That is Organize's job.

## organize

1. Query Items where Status = New. If none, say so.
2. Read the existing Domain and Tags options. Reuse before inventing. If Config gives a closed vocabulary, use only that.
3. For each item, read the page body and set:
   - Domain: one value.
   - Tags: 2 to 4 values for what the item does.
   - Summary: two sentences. What it is, and when you would use it.
   - Any extra fields still empty that the body answers. Leave a field empty rather than guess.
4. Where two items do the same job, tick Possible duplicate on the weaker one and name the other in Review notes.
5. Where an item appears to fail the Config review criteria, say why in Review notes. Do not reject it.
6. Set Status = Organized.
7. Report the tag list with counts, and flag near-duplicate tags for the user to merge.

## understand

Works only from Items where Status = Approved, unless the user explicitly widens it. If fewer than three items are Approved, say so before answering.

- **Question:** answer from the approved items. Name each item used and link its Notion row.
- **Digest:** create a page in the home page titled `<Topic> digest - <date>`. Group by Domain, one line per item with a link, then list gaps the collection does not cover.
- **Generate:** produce a new item from approved ones (a combined skill, a comparison, a shortlist). Save it to Items with Status = Organized and Review notes = `Generated from: <names>`. Generated items go through review like collected ones.

## status

Read both databases and report:

- Sources: count per Status, and Active sources not sought in the last 14 days.
- Items: count per Status, and how many are flagged Possible duplicate.
- What is waiting on a person: Proposed sources and Organized items, with a link to the To review view.

Write nothing.

## run

`seek`, then `organize`, in one pass. Give one combined report. If Seek adds nothing, still run Organize; New rows may be left from an earlier stopped run.
