---
name: opportunity-finder
description: Systematically find, verify, score, prioritize, and package grants, fellowships, awards, prizes, sponsorships, accelerators, and research-funding opportunities, ending in ranked shortlists and proposal handoff briefs. Use this skill whenever the user asks to find funding, grants, fellowships, awards, prizes, RFPs, sponsorships, or research money; asks "who funds X"; wants a funding landscape or funder map; wants quick-apply opportunities; wants to filter opportunities against an ideal grant profile or beneficiary profile; or wants a proposal handoff brief for a known opportunity — even if they don't use the word "grant." Optimized for AI education, AI governance, AI alignment, AI sovereignty, open-source, workforce-development, and public-interest technology initiatives, but applicable to any funding search.
---

# Opportunity Finder: Grants, Fellowships, Awards, and Research Funding

## Skill Summary

This skill turns a project description into a verified, scored, and prioritized set of funding opportunities — grants, fellowships, awards, prizes, sponsorships, accelerators, and research programs — packaged so a downstream proposal-writing workflow can immediately draft strong applications. It defines an Ideal Grant Profile and an Ideal Customer/Beneficiary Profile, searches across government, foundation, fellowship, AI-governance, education, open-source, corporate, and international sources, verifies every opportunity against primary sources, scores fit on a 100-point rubric, and produces reports ranging from same-day quick-apply shortlists to 90-day funding strategies. It ends every engagement with a concrete next action and, for top opportunities, a Proposal Handoff Brief.

This skill contains no executable code and assumes no operating system, installation, or paid software. Everything is markdown: workflows, source lists, templates, rubrics, and report formats.

## When to Use This Skill

- "Find me grants that could support [project]."
- "What fellowships would fund me to build [thing]?"
- "Find quick grants under $25k we can apply to this week."
- "Map the funding landscape for AI governance / AI sovereignty / AI alignment / AI literacy."
- "Which funders care about curriculum development / workforce development / public-interest tech?"
- "Only show opportunities matching this profile."
- "Create a proposal handoff brief for this grant."
- Any request to find, compare, filter, prioritize, or package external funding of any kind.

## When NOT to Use This Skill

- The user already has a specific opportunity and only needs the **proposal written** → hand off to the proposal-writing workflow (still produce a Proposal Handoff Brief first if one doesn't exist).
- The user needs **legal advice** (contracts, IP, entity formation) → recommend counsel.
- The user needs **tax advice** (501(c)(3) status, UBIT, deductibility) → recommend a CPA/attorney.
- The user needs **audited financial preparation** → recommend an accountant.
- The user wants a **guarantee of eligibility or award** → this skill assesses probability; it never guarantees.
- The user asks for **fabricated funding sources or deadlines** → refuse; only real, verifiable opportunities.

## Core Definitions

- **Opportunity**: any external source of support — grant, fellowship, award, prize, challenge, sponsorship, accelerator, residency, research program, public-sector funding program, philanthropic funding, university center funding, foundation RFP, government contract or cooperative agreement, corporate social-impact funding, or donor-advised funding pathway.
- **Ideal Grant Profile (IGP)**: the best-fit opportunity shape — eligible applicant type, geography, funding size, project type, topic, application effort, deadline urgency, reporting burden, match requirement, fiscal-sponsor acceptability, nonprofit requirement, individual-applicant acceptability, indirect-cost limits, allowed/disallowed expenses, probability of success, strategic relationship value, proposal readiness. Template: `templates/ideal-grant-profile-template.md`.
- **Ideal Customer / Beneficiary Profile (ICP)**: who the funded work serves — audience, sector, community type, skill level, geography, institution type, pain points, desired outcomes, equity/access considerations, and public, economic, educational, research, and policy benefit. Template: `templates/ideal-customer-profile-template.md`.
- **Funding Fit**: alignment between funder's stated priorities and the applicant's project.
- **Application Readiness**: whether the applicant can submit a strong application quickly (documents, budget, letters, registrations in hand).
- **Proposal Handoff**: a structured brief giving the next workflow everything it needs to draft a tailored application. Template: `templates/proposal-handoff-brief-template.md`.

## Inputs to Collect (or Infer)

Ask for or infer: applicant name and type; tax status; fiscal sponsor status; geography; project name, description, and stage; funding need; minimum useful grant size; maximum application effort; target deadline window; topic areas; target beneficiaries; existing partners; past funders; budget readiness; proposal materials already available; restrictions or exclusions; preferred funding sources; and whether the following are acceptable: government grants, individual fellowships, prizes/challenges, sponsorships, international opportunities.

Use `templates/opportunity-intake-template.md` to capture these. Do not stall on missing inputs — apply the defaults below and mark assumptions.

## Default Assumptions (when inputs are incomplete)

1. Prioritize opportunities that are easier to apply to.
2. Prioritize recurring opportunities with clear fit.
3. Prioritize primary-source application pages over aggregator listings.
4. Prioritize funders that explicitly support education, research, public interest, civic technology, AI safety, AI governance, workforce development, or open-source infrastructure.
5. Prefer concept notes, letters of inquiry, rolling applications, short forms, nominations, or lightweight initial screens.
6. Deprioritize grants with complex registrations (e.g., federal system registrations) unless strategically important.
7. Deprioritize grants requiring years of audited financials unless the user confirms readiness.
8. Mark unknowns clearly rather than guessing.

## Research Workflow (10 Steps)

**Step 1 — Clarify the Funding Thesis.** Restate the project in funder language. For AI education/governance work, candidate theses include: AI literacy and workforce development; public-interest AI education; AI curriculum for professionals; AI governance training; AI sovereignty and local AI capacity; AI alignment education; responsible AI implementation; civic AI infrastructure; open-source AI tooling; knowledge management for AI systems; human-centered AI adoption; community-based AI learning; AI for nonprofits and public-sector teams; AI safety and evaluation education; AI-enabled economic mobility.

**Step 2 — Build the Ideal Grant Profile.** Fill `templates/ideal-grant-profile-template.md`.

**Step 3 — Build the Ideal Customer / Beneficiary Profile.** Fill `templates/ideal-customer-profile-template.md`.

**Step 4 — Generate Search Themes.** Derive themes from the thesis (e.g., AI education grants, AI literacy grants, responsible AI fellowships, AI governance funding, AI alignment fellowships, AI safety grants, public-interest technology fellowships, civic technology grants, workforce development grants, digital equity grants, adult education innovation grants, open-source sustainability grants, research infrastructure grants, democracy and technology grants, technology and society fellowships, future-of-work grants, STEM education grants, nonprofit technology capacity grants, community innovation funds, government innovation grants). Use `templates/search-query-template.md` to build queries.

**Step 5 — Search Funding Sources.** Work through the relevant reference files: start with `references/funding-source-map.md` for routing, then the category files (government, foundation, fellowship, AI-governance, education/workforce, open-source/public-interest tech, university/research center, corporate philanthropy, international, and general databases). Search government portals, foundation grant pages, fellowship directories, university centers, think tanks, philanthropic programs, public-interest technology networks, AI safety and governance organizations, open-source funding programs, corporate philanthropy, challenge/prize platforms, local/state sources, and international sources where relevant.

**Step 6 — Verify Each Opportunity from Primary Sources.** For each candidate, verify: current status, deadline, eligibility, applicant type, geography, funding amount, topic fit, application process, required documents, reporting requirements, contact information, restrictions, and whether it recurs. **Never state a deadline or open status without checking the funder's own page.** Log everything in `templates/source-verification-log-template.md`, distinguishing: Verified from primary source / Verified from secondary source / Unverified / Stale-needs checking / Not enough information.

**Step 7 — Create Opportunity Cards.** One card per opportunity using `templates/opportunity-card-template.md`.

**Step 8 — Score and Rank.** Apply `rubrics/fit-scoring-rubric.md` (100-point composite), plus `rubrics/speed-to-apply-rubric.md`, `rubrics/strategic-value-rubric.md`, `rubrics/proposal-readiness-rubric.md`, `rubrics/funder-alignment-rubric.md`, and where relevant `rubrics/ai-sovereignty-alignment-rubric.md` and `rubrics/curriculum-development-fit-rubric.md`. Rank into: Apply First / Monitor / Relationship-Build / Reject. Log rejections in `templates/no-fit-rejection-log-template.md`.

**Step 9 — Produce Reports.** Choose the format the user needs: quick-apply shortlist (`templates/quick-apply-shortlist-template.md`), full landscape (`templates/funding-landscape-report-template.md`), fellowship shortlist, government shortlist, foundation funder map, AI alignment/governance funder map, curriculum-development funder map, proposal pipeline, 30-day application plan, or 90-day funding strategy. Use `templates/opportunity-table-template.md` for rankings and `templates/grant-scorecard-template.md` for per-opportunity scoring detail.

**Step 10 — Produce Proposal Handoff Briefs.** For each top opportunity, complete `templates/proposal-handoff-brief-template.md`, extracting funder language with `templates/funder-language-extraction-template.md` and confirming readiness with `templates/eligibility-checklist-template.md` and `templates/application-readiness-checklist-template.md`.

## Opportunity Categories

Classify every opportunity into one primary category:

1. **Government** — federal, state, and local grants; cooperative agreements; research agency grants; workforce development, education, digital equity, and innovation grants.
2. **Philanthropic Foundations** — private, family, community, and corporate foundations; donor-advised funds; issue-specific grantmakers.
3. **Fellowships** — individual, founder, research, policy, technology, education, and civic innovation fellowships.
4. **AI Alignment / AI Safety / AI Governance** — AI safety research grants, responsible AI programs, AI governance fellowships, model-evaluation funding, public-interest AI programs, AI policy institutes, technical alignment fellowships, AI security and sovereignty programs.
5. **Curriculum / Education / Workforce** — curriculum development, STEM education, adult learning, workforce development, digital literacy, teacher training, professional upskilling.
6. **Public Interest Technology** — civic technology, democracy and technology, public-sector innovation, nonprofit tech capacity, open data, digital public infrastructure, human rights and technology.
7. **Open Source** — open-source sustainability, developer ecosystem, public infrastructure, research software, community tooling.
8. **Corporate and Ecosystem Funding** — cloud credits, startup programs, developer grants, ecosystem funds, AI platform credits, social-impact sponsorships.
9. **Prizes and Challenges** — innovation challenges, AI competitions, civic innovation prizes, edtech competitions, public-benefit technology prizes.

## Assistant Behavior Guidelines

- Prefer primary sources; cite or link every opportunity.
- **Never fabricate deadlines, amounts, or opportunities.** Never assume eligibility if unclear.
- Mark uncertainty clearly; separate verified facts from strategic interpretation.
- Avoid overfitting to buzzwords; translate the user's project into the funder's language honestly.
- Prioritize speed for quick-apply requests; prioritize strategic fit for landscape requests.
- Include rejected opportunities (with reasons) when useful.
- Create proposal handoff briefs for top-ranked opportunities.
- Always preserve the user's strategic constraints and exclusions.
- Always identify the next best action.

## Reference Files (read as needed)

- `references/funding-source-map.md` — master routing map across all source categories
- `references/grant-databases.md` — general grant/fellowship databases and aggregators
- `references/government-sources.md` — federal, state, local
- `references/foundation-sources.md` — philanthropic foundations and research tools
- `references/fellowship-sources.md` — fellowship directories and programs
- `references/ai-alignment-ai-governance-sources.md` — AI safety/governance/sovereignty funders
- `references/education-workforce-sources.md` — curriculum, education, workforce
- `references/open-source-public-interest-tech-sources.md` — OSS and public-interest tech
- `references/university-and-research-center-sources.md` — university centers, labs, think tanks
- `references/corporate-philanthropy-sources.md` — corporate foundations, credits, ecosystem funds
- `references/international-sources.md` — non-US and multilateral sources

## Examples

- `examples/example-intelcraft-ideal-grant-profile.md`
- `examples/example-intelcraft-opportunity-report.md`
- `examples/example-proposal-handoff-brief.md`

## Operational Checklist

1. Fill out the Ideal Grant Profile.
2. Fill out the Ideal Customer / Beneficiary Profile.
3. Run the opportunity search across the relevant reference categories.
4. Verify every opportunity against primary sources; log verification.
5. Score and rank opportunities with the rubrics.
6. Create a quick-apply shortlist (and/or the full landscape report).
7. Create Proposal Handoff Briefs for the top opportunities.
8. Pass each handoff brief into the proposal-writing workflow.
