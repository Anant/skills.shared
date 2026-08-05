# Phase Playbooks — detailed per-phase signal interpretation

Each phase collects public signals and appends `{finding, source, confidence}` to the state
object. Tag confidence per the taxonomy in `SKILL.md`. Endpoints/headers/limits live in
`data-sources.md`; 1–10 anchors live in `scoring-rubrics.md`.

---

## PHASE 0 — Domain & Infrastructure Intelligence

**Goal:** Establish the digital foundation and age/scale of the company from the domain alone.

**Collect:** RDAP (registration/expiration events, registrar, EPP status, nameservers,
DNSSEC), DNS-over-HTTPS (A, MX, NS, TXT for SPF/DKIM/DMARC), Certificate Transparency /
subdomain enumeration (crt.sh with Cert Spotter fallback), Wayback Machine snapshots.

**Signals & interpretation:**

- **Domain age** (RDAP registration event): old domain + modern site = established,
  reinvested; old domain + stale site = neglect / opportunity.
- **MX records** reveal the email stack (Google Workspace vs Microsoft 365 vs self-hosted →
  IT-sophistication proxy).
- **Missing SPF/DMARC** = weak security hygiene = an easy quick-win to add.
- **Subdomains** reveal hidden infrastructure: `app.`, `api.`, `status.`, `careers.`,
  `shop.`, `staging.` → product surface, engineering maturity, e-commerce.
- **CDN/hosting** (from DNS/headers): Cloudflare/Fastly/AWS vs bare shared hosting →
  scalability posture.

**Scoring (feeds Digital/Tech Maturity + Risk):** 1–10 on infrastructure modernity.
1–3 = shared hosting, no CDN, no email auth, expiring soon; 8–10 = modern CDN, DNSSEC, full
email auth, clean subdomain architecture.

---

## PHASE 1 — Website & Digital Presence Analysis

**Goal:** Understand what the company does, who it sells to, and how actively it maintains
its presence.

**Collect:** web_fetch the homepage, `/about`, `/products`, `/pricing`, `/careers`, `/blog`,
`/customers`, plus `sitemap.xml` and `robots.txt`.

**Signals & interpretation:**

- **Positioning/messaging** → business model (B2B/B2C/SaaS/services/e-commerce), ICP, value prop.
- **Pricing page** present + transparent → mature GTM; "contact us only" → enterprise/high-touch sales.
- **Blog recency** → marketing investment (posts within 30 days = active; nothing for 12+ months = neglected).
- **Careers page** → growth intent and (critically) the tech-gap signal (see Phase 3).
- **Copyright year in footer** → a stale year (e.g., "© 2019") is a classic neglected-web-presence tell.
- **Product/service catalog breadth** → revenue diversification and complexity.

**Scoring (feeds Business Model Quality + Digital Maturity):** clarity of positioning, GTM
sophistication, content freshness.

---

## PHASE 2 — Technology Stack Detection

**Goal:** Fingerprint the tech stack to assess sophistication and locate automation/AI gaps.

**Collect:** Wappalyzer/BuiltWith-style detection via HTTP headers (Server, X-Powered-By,
Set-Cookie), HTML, `<script>`/meta tags, JS variables, and DNS; or a hosted detector API.
Also check security headers, page speed (Core Web Vitals), mobile responsiveness, accessibility.

**Signals & interpretation (the value-creation map):**

- **CMS:** WordPress (per W3Techs, April 2025, ~43.4% of all websites, ~9× nearest competitor
  Shopify at 4.8%) is common/low-cost; headless/custom = higher maturity.
- **E-commerce:** Shopify/BigCommerce vs custom vs none.
- **Analytics present?** No GA/analytics = flying blind = a data-infrastructure opportunity.
- **Marketing automation** (HubSpot/Marketo/Klaviyo) absent = automation opportunity.
- **CRM signals** (forms, chat, tracking) → sales-ops maturity.
- **Security headers missing / old TLS** → risk + quick win.
- **No CDN, slow pages, poor mobile** → conversion drag + easy uplift.
- **Caveat:** passive fingerprinting misses hidden backends (stripped headers, Node behind
  Nginx, apps behind Cloudflare). Tag detections with confidence; carry a detector's own
  confidence through.

**Scoring (heavily feeds Digital/Tech Maturity + Technology Uplift):** invert for opportunity
— LOW maturity here + strong business = HIGH uplift.

---

## PHASE 3 — Company & People Intelligence

**Goal:** Assess team, headcount trajectory, leadership, and read job posts as growth/tech-gap
signals.

**Collect:** LinkedIn company page (public headcount, growth trend, leadership), founder/exec
backgrounds (public bios, prior exits), Glassdoor (employee sentiment; ~3.3/5 is a common
industry baseline), job boards / the company's own careers page. **Public, no-login data only
— no scraping behind auth.**

**Signals & interpretation:**

- **Headcount growth on LinkedIn** = proxy for growth rate; department mix reveals strategy
  shifts (all-sales six months ago → all-engineers now = strategic pivot).
- **Job postings = the highest-value inferred signal.** Hiring precedes announcements:
  - Hiring data / ML engineers = investing in analytics/AI infrastructure.
  - First-ever RevOps / SDR / data role = building a function from zero (high intent).
  - Role clusters + velocity spikes = compressed urgency, real budget.
  - Job descriptions name the stack (Snowflake, Salesforce, Kubernetes) → technographic confirmation.
  - **Absence of tech/data roles despite growth = the technology gap a tech investor fills.**
- **Founder/leadership pedigree** → execution confidence (Thoma Bravo's leadership test:
  open-mindedness, cares about numbers, strong followership).
- **Glassdoor** → culture/retention risk; watch for divergence from public messaging.

**Scoring (feeds Team Strength + Growth Trajectory):** headcount trend, leadership quality,
hiring-signal strength.

---

## PHASE 4 — Financial & Business Signals

**Goal:** Estimate scale, funding, revenue, and business-model economics from public proxies.

**Collect:** SEC EDGAR (submissions, company facts, full-text search, ticker→CIK), business
registries (OpenCorporates, state Secretary of State), funding history (Crunchbase/PitchBook
public profiles), revenue estimates (triangulated: headcount × revenue-per-employee, pricing
× customer-count, third-party estimates — all Inferred/Speculative), case studies / logos /
customer counts on the site.

**Signals & interpretation:**

- Funding stage + recency → runway and growth phase.
- Pricing model × customer signals → revenue quality (recurring vs project; SaaS ARR is the
  PE gold standard, 90%+ renewal rates).
- Registry status (active/good standing vs delinquent) → basic health/risk.
- Enterprise logos → contract value; few large logos → customer-concentration risk.

**Scoring (feeds Financial Health Proxy):** be explicit that most values here are Inferred;
**never present modeled revenue as Verified.**

---

## PHASE 5 — Market & Competitive Analysis

**Goal:** Classify the industry, size the market, map competitors, gauge share of voice.

**Collect:** industry classification (SIC/NAICS from filings or inference), TAM/SAM
(triangulated public research), competitor identification (search + "similar to" reasoning),
SEO share of voice, traffic estimates (SimilarWeb/Semrush/Ahrefs-style).

**Signals & interpretation:**

- **Traffic estimates are directional only.** Per Omniconvert's 1,787-site study, SimilarWeb
  overreported sessions by ~94%; unreliable under ~100K monthly visits (error can exceed 70%
  on small sites), most reliable for large sites and on time-on-site rather than raw sessions.
  Use as a trend/relative signal; tag Speculative for SMBs.
- Competitor set + positioning → differentiation and pricing power.
- Fragmented market = roll-up/bolt-on opportunity (the Thoma Bravo/Vista buy-and-build thesis).
- SEO share of voice → demand-gen strength.

**Scoring (feeds Market Attractiveness):** size, growth, fragmentation, competitive intensity,
defensibility.

---

## PHASE 6 — Customer & Reputation Signals

**Goal:** Gauge customer sentiment, satisfaction trend, brand strength.

**Collect:** G2, Capterra, Trustpilot, Google, Yelp reviews; social presence/engagement;
community (Reddit, forums); press coverage; awards. News via Google News RSS and GDELT
(free/keyless, includes tone/sentiment).

**Signals & interpretation:**

- **Review velocity** (rate + recency) matters more than raw count — a steady stream signals
  health; a burst then silence signals gaming; velocity decay erodes trust scores.
- **Cross-platform divergence** (G2 up, Trustpilot down) = different segments, different
  experiences — investigate.
- **Reddit/forums = most honest sentiment.** Curated review sites can be gamed: per
  Originality.ai's Nov 2025 study of 187,000 G2 reviews, >26% of G2 reviews since ChatGPT's
  launch are likely AI-generated (up 92.8%, peaking at 34.6% in June 2023). Use unfiltered
  sources to sanity-check.
- Rating level + trend → NPS proxy; press/awards → brand equity.

**Scoring (feeds Business Model Quality + Risk):** sentiment level, velocity trend,
reputational red flags.

---

## PHASE 7 — Risk & Compliance Signals

**Goal:** Surface litigation, regulatory, security, and concentration risks.

**Collect:** litigation (CourtListener REST API v4, includes RECAP federal dockets — a free
PACER mirror), regulatory/security (breach-history checks, security headers from Phase 2, SEC
litigation releases, news from Phase 6), key-person & concentration (inferred from Phases 3–4:
founder-dependence, few large logos).

**Signals & interpretation:** active litigation as defendant, regulatory actions, breach
history, single-founder dependence, and customer concentration all raise risk. AKF Partners'
"too good to be true" heuristic (Benford's-law-style anomalies, an over-dominant CEO answering
every technical question) flags areas warranting deeper human diligence.

**Scoring (feeds Risk Profile — inverse):** more/severe risks → lower score.

---

## PHASE 8 — Technology Gap & Opportunity Analysis (the differentiator)

**Goal:** Explicitly identify what tech/AI/automation the company LACKS that a
technology-focused investor could add. This is the heart of the framework.

**Method — synthesize Phases 0–3 into three scores:**

1. **Digital Maturity Score** (Deloitte/TM Forum lens: Customer, Strategy, Technology,
   Operations, Organization & Culture, Data).
2. **AI-Readiness Score** — weight data maturity heavily (common SMB frameworks: data ≈ 30%,
   infrastructure ~15%, budget alignment ~10%): Is data centralized (CRM + sales + ops
   integrated)? Clean, with 12+ months of history? Cloud/API-connected? MIT CISR's ladder
   implies firms below stage 3 underperform peers.
3. **Automation Opportunity Map** — detected gaps → concrete plays (no marketing automation →
   lifecycle automation; manual reporting → BI/dashboards; no chatbot → support deflection;
   no analytics → data infrastructure).

**Interpretation — the sweet spot:** plot Tech Maturity (low↔high) against Business
Fundamentals (weak↔strong). **LOW tech maturity + HIGH fundamentals = the prime target**
(broken tech, good business = cheap, fast value-add). HIGH tech + HIGH fundamentals =
expensive, less headroom. LOW + LOW = pass/turnaround only.

**Scoring (this IS the Technology Uplift Opportunity dimension):** magnitude × feasibility ×
business quality of the gaps.

---

## PHASE 9 — Synthesis, Scoring & Investment Memo Generation

Compute the composite (`scripts/score.py`), assign a verdict (see `scoring-rubrics.md`), and
render the memo (`scripts/render_memo.py` + `templates/investment_memo.md`). Carry confidence
labels into the output. Everything tagged Inferred/Speculative rises into the Human Diligence
Items section.

---

## Portability to other agent frameworks

- **LangGraph:** each phase = a node; the state object = graph state; Phase 9 = a reducer.
- **CrewAI:** one agent per research track + a synthesis agent.
- **n8n:** HTTP Request nodes for the free APIs, a Function node for scoring, an LLM node for the memo.
- **OpenAI Agents:** tools = search/fetch/code; phases = handoffs.
