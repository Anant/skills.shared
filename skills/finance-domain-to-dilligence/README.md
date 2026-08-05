# domain-to-diligence

A [Claude Skill](https://docs.claude.com/en/docs/claude-code/skills) that takes a single
**domain name** and produces an investment-grade company breakdown for a technology-focused
investor — using **public data only**, with **every finding confidence-tagged**.

It runs a 10-phase public-signal pipeline, scores 8 weighted dimensions to a 0–100 composite,
and assigns a PE-style verdict: **Platform / Bolt-on / Growth Partnership / Services /
Turnaround / Pass**.

> **The core thesis (the "sweet spot"):** LOW Digital/Tech Maturity + HIGH Business
> Fundamentals = the highest-value target. Broken tech on top of a good business is the
> cheapest, fastest value to add. The scoring intentionally *rewards* this combination.

## Layout

```
domain-to-diligence/
├── SKILL.md                    # the workflow: 10 phases + scoring + verdict logic (lean)
├── references/
│   ├── phase-playbooks.md       # detailed per-phase signal interpretation
│   ├── data-sources.md          # exact API endpoints, headers, rate limits (SSOT)
│   └── scoring-rubrics.md       # 1–10 anchors per dimension + weighting presets
├── scripts/
│   ├── domain_intel.py          # RDAP + DNS-over-HTTPS + crt.sh (Phase 0)
│   ├── sec_lookup.py            # SEC EDGAR submissions/facts (Phase 4)
│   ├── score.py                 # composite scoring + verdict (Phase 9)
│   └── render_memo.py           # investment-memo / HTML scorecard renderer (Phase 9)
└── templates/
    └── investment_memo.md       # the 8-section memo template
```

## Install

Symlink (or copy) this folder into your Claude skills directory:

```bash
ln -s "$(pwd)" ~/.claude/skills/domain-to-diligence
```

The skill auto-invokes when you ask Claude to evaluate, screen, or diligence a company from
its domain/website.

## Scripts

Stdlib-only (Python 3) — no dependencies. All data sources are free/keyless except where noted
in `references/data-sources.md`.

```bash
# Phase 0 — domain & infrastructure intel
python scripts/domain_intel.py example.com

# Phase 4 — SEC EDGAR (SEC requires a "Name email" User-Agent)
SEC_UA="Jane Doe jane@firm.com" python scripts/sec_lookup.py --ticker CRM

# Phase 9 — score a filled-in state object, then render the memo
python scripts/score.py --state state.json --preset platform
python scripts/render_memo.py --state state.json --scorecard scorecard.json -o memo.md --html
```

## Confidence taxonomy

Every finding is tagged: **Verified** (authoritative primary source) · **Corroborated** (2+
independent sources) · **Inferred** (indirect signals) · **Speculative** (single weak signal /
model estimate). Everything Inferred/Speculative is routed into the memo's Human Diligence
Items section.

## Guardrails

Public data only — no scraping behind logins, no pretexting, no circumventing paywalls/auth.
Respect robots.txt and platform ToS, honor API rate limits and required headers (e.g. the SEC
User-Agent), and never attempt to de-anonymize redacted (GDPR) registrant PII.

This is a **screening** tool, not confirmatory diligence — its output is a prioritized
hypothesis set, not a decision. Revenue/traffic/headcount are modeled with wide error bands.

## Portability

The phase/state design ports to other agent frameworks: **LangGraph** (phase = node, state =
graph state, Phase 9 = reducer), **CrewAI** (agent per track + synthesis agent), **n8n** (HTTP
Request nodes + Function node for scoring), **OpenAI Agents** (tools = search/fetch/code,
phases = handoffs).
