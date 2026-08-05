---
name: domain-to-diligence
description: >-
  Analyze a company from only its domain name and produce an investment-grade diligence
  memo with scores. Runs a 10-phase public-signal pipeline (infrastructure, website, tech
  stack, people, financials, market, reputation, risk, tech-gap, synthesis), scores 8
  weighted dimensions to a 0-100 composite, and assigns a PE-style verdict (Platform /
  Bolt-on / Growth Partnership / Services / Turnaround / Pass). Every finding is tagged
  Verified / Corroborated / Inferred / Speculative. Use when given a domain or website and
  asked to evaluate, screen, diligence, or size the tech-uplift opportunity of a company.
metadata:
  stage: personal
---

# Domain-to-Diligence

Take a single domain name and produce an investment-grade company breakdown for a
technology-focused investor. Public data only. Every finding carries a confidence label.

**The core thesis (the "sweet spot"):** LOW Digital/Tech Maturity + HIGH Business
Fundamentals = the highest-value target — broken tech on top of a good business is the
cheapest, fastest value to add. The scoring intentionally *rewards* this combination
rather than penalizing low tech maturity.

## Confidence taxonomy (apply to EVERY finding)

- **Verified** — authoritative primary source (SEC filing, gov registry, the company's own site).
- **Corroborated** — consistent across 2+ independent public sources.
- **Inferred** — reasoned from indirect signals (e.g., job posts imply tech gaps).
- **Speculative** — single weak signal or model estimate (e.g., small-site traffic estimate).

Never present modeled revenue/traffic/headcount as Verified. Route every Inferred/Speculative
item into the memo's "Human Diligence Items" section.

## Workflow shape

Sequential with checkpoints, parallel within phases. **Phases 0–2** (infra/site/stack) run
in parallel; **Phases 3–7** run as parallel research tracks; **Phases 8–9** are synthesis
gates that require prior outputs. If a phase yields only Speculative data, flag it and
continue — never block the whole run.

Maintain a **JSON state object** that each phase appends to (`{finding, source, confidence}`),
which Phase 9 consumes.

## The 10 phases

| # | Phase | Goal | Feeds dimensions |
|---|-------|------|------------------|
| 0 | Domain & Infrastructure | Digital foundation, age/scale from the domain alone (RDAP, DoH, crt.sh, Wayback) | Digital Maturity, Risk |
| 1 | Website & Digital Presence | What they do, who they sell to, how actively maintained | Business Model, Digital Maturity |
| 2 | Technology Stack Detection | Fingerprint the stack; locate automation/AI gaps | Digital Maturity, Tech Uplift |
| 3 | Company & People Intel | Team, headcount trajectory, leadership, **job posts as growth/tech-gap signal** | Team, Growth |
| 4 | Financial & Business Signals | Scale, funding, revenue, economics from public proxies (SEC EDGAR, registries) | Financial Health |
| 5 | Market & Competitive | Industry, TAM/SAM, competitors, share of voice | Market Attractiveness |
| 6 | Customer & Reputation | Sentiment, review velocity, brand (G2/Trustpilot/Reddit, Google News, GDELT) | Business Model, Risk |
| 7 | Risk & Compliance | Litigation, regulatory, security, concentration (CourtListener) | Risk (inverse) |
| 8 | **Technology Gap & Opportunity** | What tech/AI/automation they LACK — **the differentiator** | Tech Uplift |
| 9 | Synthesis, Scoring & Memo | Composite score, verdict, memo artifact | — |

Detailed per-phase signal-interpretation guides: `references/phase-playbooks.md`.
Exact API endpoints, headers, and rate limits: `references/data-sources.md`.

### Phase 8 is the crown jewel

Synthesize Phases 0–3 into three scores, then plot the sweet spot:

1. **Digital Maturity Score** (Deloitte/TM Forum lens: Customer, Strategy, Technology,
   Operations, Organization & Culture, Data).
2. **AI-Readiness Score** — weight data maturity heavily (~30% data, ~15% infra, ~10% budget):
   Is data centralized? Clean, 12+ months of history? Cloud/API-connected?
3. **Automation Opportunity Map** — detected gaps → concrete plays (no marketing automation
   → lifecycle automation; manual reporting → BI/dashboards; no chatbot → support deflection;
   no analytics → data infrastructure).

**The sweet spot:** plot Tech Maturity (low↔high) vs Business Fundamentals (weak↔strong).
LOW tech + HIGH fundamentals = prime target. HIGH + HIGH = expensive, less headroom.
LOW + LOW = pass/turnaround only.

## Composite scoring (Phase 9)

Score each dimension 1–10 (anchors in `references/scoring-rubrics.md`), multiply by weight,
sum to a 0–100 composite. Weights below are the **Platform preset**:

| # | Dimension | Weight | Primary phases |
|---|-----------|--------|----------------|
| 1 | Market Attractiveness | 15% | 5 |
| 2 | Business Model Quality | 15% | 1,4,6 |
| 3 | Growth Trajectory | 12% | 3,4,5 |
| 4 | Digital/Tech Maturity | 10% | 0,1,2 |
| 5 | Team Strength | 10% | 3 |
| 6 | Financial Health Proxy | 13% | 4 |
| 7 | Risk Profile | 10% | 7 |
| 8 | Technology Uplift Opportunity | 15% | 2,8 |

Presets (rationale in `references/scoring-rubrics.md`): **Platform** (above), **Growth
Partnership** (Growth 18% + Uplift 18%, Financial 8%), **Services Client** (Uplift 25%,
lower Market/Financial).

Run the math with the script, don't do it by hand:
```bash
python scripts/score.py --state state.json --preset platform
```

### Verdict taxonomy

| Composite + pattern | Verdict |
|---------------------|---------|
| 75+ with high uplift + strong fundamentals | **Platform Investment** |
| 65–80, strong fit within a thesis, smaller | **Bolt-on / Add-on** |
| 60–75, high trajectory, minority/growth | **Growth Partnership** |
| 55–75, fixable tech gap + ability to pay, not investable | **Services Opportunity** |
| 45–65, weak now but salvageable | **Turnaround / Watch** |
| <45 or fatal risk flags | **Pass** |

## Scripts

Scripts run via bash without consuming context. See each file's `--help`.

- `scripts/domain_intel.py` — RDAP + DNS-over-HTTPS + crt.sh (Phase 0).
- `scripts/sec_lookup.py` — EDGAR submissions/facts, ticker→CIK (Phase 4; sets required UA header).
- `scripts/score.py` — composite scoring + verdict from the JSON state object (Phase 9).
- `scripts/render_memo.py` — render the 8-section memo (+ optional HTML scorecard) from state.

## Output artifact — the investment memo

Render `templates/investment_memo.md` filled from the state object. Eight sections:
Executive Summary, Company Snapshot, Scorecard Table, Dimension-by-Dimension Findings,
Technology Uplift Roadmap (Quick Wins 0–90 days vs Strategic Plays), Deal Thesis, Risks &
Red Flags, Recommended Next Steps / Human Diligence Items.

## Quick-run version (15–30 min triage screen)

Before a full deep-dive: (1) RDAP + DNS + homepage fetch, (2) one tech-stack read, (3)
careers page + LinkedIn headcount glance, (4) one reviews check + one news search, (5) score
just 4 dimensions — Business Model, Growth, Digital Maturity, Tech Uplift — and output a
provisional verdict + "worth a deep dive? Y/N". Deliver a half-page triage card with
provisional quadrant placement and the top 3 uplift hypotheses.

## Tool mapping (Claude)

- **web_search** — news, competitors, reviews, funding, leadership.
- **web_fetch** — homepage/subpages, sitemap, RDAP/DNS/crt.sh/SEC/CourtListener JSON, review pages.
- **code execution** — scoring math, revenue triangulation, parsing, memo rendering.
- **artifacts** — the final memo (and optionally an HTML scorecard).

## Ethical & legal guardrails (non-negotiable)

Public data only. No scraping behind logins, no pretexting/fake accounts, no circumventing
paywalls or auth. Respect robots.txt and platform ToS. Honor API rate limits and required
headers (e.g., the SEC User-Agent). GDPR: never attempt to de-anonymize redacted registrant
PII. Present all inferences as inferences.

## Caveats (state in every memo)

Public-signal *screening* tool, not confirmatory diligence — output is a prioritized
hypothesis set, not a decision. Revenue/traffic/headcount are modeled with wide error bands
(SimilarWeb error can exceed 70% on sub-100K-visit sites). Review sites can be gamed
(corroborate with unfiltered sources like Reddit). Free API access/limits shift frequently —
`references/data-sources.md` is the single source of truth; recalibrate quarterly.
