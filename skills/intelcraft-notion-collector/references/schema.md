# Schema

What `init` creates. One collection is one Notion home page holding a Config page and two databases.

```
<Topic> Collection        home page
  Config                  page, plain property list
  Sources                 database
  Items                   database, with Pipeline and To review views
```

## Config page

A plain list of `Key: value` lines so a person can edit it without knowing the skill.

```
Topic: Agent skills for sales teams
Item type: Skill
One item is: One SKILL.md file or one skill folder
Extra fields: Trigger (text), Tools required (multi-select)
Tag vocabulary: open
Review criteria: Reject anything that asks for credentials or sends data to a third party
Sources per explore: 8
Items per source per seek: 5
```

| Key | Meaning | Default |
| --- | --- | --- |
| Topic | What the collection is about | Required |
| Item type | One of the presets in `item-types.md`, or Custom | Required |
| One item is | The unit Seek creates one row for | From preset |
| Extra fields | Columns added to Items beyond the core, as `Name (type)` | From preset |
| Tag vocabulary | `open`, or a comma-separated closed list | open |
| Review criteria | What Organize should flag for the reviewer | None |
| Sources per explore | Cap on new sources per Explore run | 8 |
| Items per source per seek | Cap on new items per source per Seek run | 5 |

If a key is missing, use the default and say so in the run report.

## Sources database

| Property | Type | Values |
| --- | --- | --- |
| Name | title | |
| URL | url | |
| Type | select | Repo, Registry, Marketplace, Blog, Newsletter, List |
| Seek method | select | API, RSS, Search, Scrape |
| Status | select | Proposed, Active, Paused, Dead |
| Added by | select | Agent, Human |
| Last sought | date | |
| Notes | text | |

Status meanings:

| Status | Meaning | Who sets it |
| --- | --- | --- |
| Proposed | Found by Explore. Seek ignores it. | Agent |
| Active | Approved. Seek collects from it. | Human |
| Paused | Good source, skipped for now. | Human |
| Dead | Gone or useless. Kept so Explore does not propose it again. | Human |

## Items database

Core properties, the same for every collection:

| Property | Type | Values |
| --- | --- | --- |
| Name | title | |
| URL | url | |
| Type | select | The Config item type |
| Source | relation | To Sources |
| Status | select | New, Organized, Approved, Rejected |
| Domain | select | Starts empty |
| Tags | multi-select | Seeded from Config vocabulary, or empty |
| Summary | text | |
| Possible duplicate | checkbox | |
| Collected at | date | |
| Review notes | text | |

Plus one column per entry in Config `Extra fields`. The page body of each row holds the collected content; what goes there depends on the item type.

Status meanings:

| Status | Meaning | Who sets it |
| --- | --- | --- |
| New | Collected by Seek. Raw. | Agent |
| Organized | Tagged and summarized. Waiting for review. | Agent |
| Approved | Accepted. Understand reads these. | Human |
| Rejected | Declined. Kept so Seek does not collect it again. | Human |

Use select for Status, not Notion's native status type, so the options are exactly these.

## Views on Items

| View | Type | Setup |
| --- | --- | --- |
| Pipeline | Board | Grouped by Status |
| To review | Table | Filter Status = Organized. Show Name, Domain, Tags, Summary, Possible duplicate, Review notes. |

If view creation fails, tell the user: on the Items database click **+** beside the view tabs, choose Board, set Group by to Status. Then continue; views are a convenience, not a dependency.

## Repair

When a run finds the schema differs from this file:

- A property renamed or added by the user: use it as it is. Do not rename it back.
- A core property missing: ask before adding it.
- A select option missing (for example a new Domain): add the option.
- A Status option missing or renamed: stop and ask. The stages depend on these.
