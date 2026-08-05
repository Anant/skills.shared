# Investment Memo � The Browser Company of New York — Dia Browser (acquired by Atlassian Oct 21, 2025)

## 1. Executive Summary
The Browser Company of New York built Dia, an AI-first web browser launched in beta June 2025 and publicly on Mac in October 2025. Roughly 11 months after the diabrowser.com domain was registered, Atlassian acquired the company for $610M (announced Sep 4, 2025; closed Oct 21, 2025) to anchor its push into agentic, AI-mediated knowledge work. The screen is therefore retrospective: this is no longer an investable standalone target. The composite of 69/100 reflects a high-trajectory, well-engineered, design-led company with a modern stack and a strong team — but the Technology Uplift Opportunity scores LOW (3/10) because Dia is itself the AI/automation play. This is the opposite of the framework's sweet spot (low tech + high fundamentals); it is high tech + high fundamentals + already-acquired, leaving little headroom for an outside technology investor to add value.

**Verdict: Growth Partnership**  �  Composite: **69.2/100**
(preset: platform)

> Public-signal screening tool, not confirmatory diligence. All Inferred/Speculative items
> appear in �8 for human verification.

## 2. Company Snapshot
- **What they do:** AI-first web browser ('Dia') that reads between the tabs — Morning Brief, cross-app synthesis (Slack/Notion/GSuite/Calendar), Skills gallery, agentic reports, split views, profiles. Successor to Arc browser (frozen May 2025).  _[Verified]_
- **Model:** Freemium consumer browser + $20/mo Pro subscription (launched Aug 2025) + Dia for Work (SSO/admin enterprise tier). Recurring SaaS, pre-ARR-disclosure scale.  _[Verified]_
- **Size estimate:** Pre-acquisition: ~$550M valuation (Mar 2024 Series, $50M raised). Acquired for $610M cash (some sources cite $936M AUD). Headcount not disclosed; LinkedIn shows ~150–250 range (Inferred).  _[Corroborated]_
- **Founded:** 2019 (The Browser Company of New York). diabrowser.com domain registered Oct 18, 2024.  _[Verified]_
- **HQ:** New York, NY  _[Verified]_
- **Leadership:** Josh Miller (CEO, ex-White House CTO under Obama, ex-Facebook/Thread). Marco Triverio (Safari lead designer, joined Jan 2026 from Apple). Tara Feener (search lead, Fast Company feature Dec 2025).  _[Verified]_

## 3. Scorecard
| Dimension | Score | Weight | Contribution |
|-----------|:-----:|:------:|:------------:|
| Market Attractiveness | 8.0 | 15% | 12.00 |
| Business Model Quality | 6.0 | 15% | 9.00 |
| Growth Trajectory | 8.0 | 12% | 9.60 |
| Digital/Tech Maturity | 9.0 | 10% | 9.00 |
| Team Strength | 9.0 | 10% | 9.00 |
| Financial Health Proxy | 7.0 | 13% | 9.10 |
| Risk Profile | 7.0 | 10% | 7.00 |
| Technology Uplift Opportunity | 3.0 | 15% | 4.50 |
| **Composite** | | | **69.20** |

**Verdict rationale:** high trajectory; minority/growth bet

## 4. Dimension-by-Dimension Findings
- Domain registered 2024-10-18 via Cloudflare; expires 2026-10-18. Hosted on Cloudflare nameservers; A records point to Vercel (76.76.21.142, 66.33.60.66).  _[Verified]_  (src: RDAP + DoH)
- Email stack: Google Workspace (MX smtp.google.com). SPF present, DMARC present — no email-auth quick-win available.  _[Verified]_  (src: DoH)
- Subdomain architecture is mature and product-led: ai-service., ai-service.sandbox., auth., help., links., public., releases., skills., status., students., trust. Indicates a real engineering org with staging, an AI service backend, a Skills platform, and a Trust Center.  _[Corroborated]_  (src: Cert Spotter (crt.sh failed))
- Marketing site stack: Next.js (SSG, buildId HnJIcl_U7J0dtMhWbHRER), Sanity CMS (cdn.sanity.io), Mux video (mux.video assets), Vercel hosting, Cloudflare DNS. Modern headless JAMstack — high digital maturity.  _[Verified]_  (src: Homepage HTML inspection)
- Atlassian (TEAM, Nasdaq, CIK 0001650372) acquired The Browser Company for $610M, announced Sep 4, 2025; closed Oct 21, 2025. Atlassian FY26 Q3 (10-Q, period ending 2026-03-31): revenue $4.81B, operating loss -$200M, net loss -$193M.  _[Verified]_  (src: SEC EDGAR + Reuters/Business Wire/TechCrunch)
- Pre-acquisition funding: $50M round at $550M valuation (Mar 2024, TechCrunch). Prior investors include LinkedIn CEO Jeff Weiner, Tom Warren, Tom Hanks (Inferred from prior reporting).  _[Corroborated]_  (src: TechCrunch)
- Product velocity: Dia teased Dec 2024; private beta Jun 11, 2025; public Mac launch Oct 9, 2025; Pro plan ($20/mo) Aug 7, 2025; Skills gallery Jul 21, 2025; Arc 'greatest hits' backported Nov 3, 2025. Currently macOS 14+ M1+ only; Windows waitlist.  _[Verified]_  (src: TechCrunch / Engadget / 9to5Mac / Verge)
- Team strength: CEO Josh Miller (ex-White House CTO, ex-Facebook). Continued Apple talent poaching — Marco Triverio (Safari lead designer) joined Jan 2026. Tara Feener featured in Fast Company (Dec 2025) for AI-era search work.  _[Verified]_  (src: AppleInsider / MacRumors / Fast Company)
- Market: AI-browser / agentic-web category. Direct competitors: Arc (frozen, same company), Chrome, Edge, Brave, Opera, Perplexity Comet, Spyglass. Chrome ~65% market share is the moat to displace; AI is the entry wedge. Atlassian positions Dia for enterprise work-search, not consumer.  _[Inferred]_  (src: Industry inference + Computerworld / spyglass.org)
- Reputation: Mixed. Positive coverage of Dia's design and AI integration (Forbes, The Verge). Negative sentiment from Arc power users who felt abandoned when Arc was frozen May 2025 (tidbits.com, MakeUseOf). Thurrott headline: 'It Looks Like Atlassian is Going to Ruin Dia for Everyone.'  _[Corroborated]_  (src: Google News RSS)
- Risk: macOS-only at launch is a real concentration constraint (Apple platform dependence). Acquisition integration risk — Atlassian's track record on consumer products is mixed. No litigation or regulatory flags found in public news.  _[Inferred]_  (src: News search)
- Technology Uplift Opportunity is LOW. Dia already has: in-house AI service (ai-service subdomain), Skills (custom automation gallery), agentic reports, cross-app context synthesis, marketing automation implied by Substack newsletter + Typeform waitlist, modern analytics implied by Vercel/Sanity. A technology-focused investor adds little here — Dia IS the tech uplift thesis.  _[Inferred]_  (src: Stack + product surface)

## 5. Technology Uplift Roadmap
**Quick Wins (0�90 days):**
- None material. Email auth (SPF/DMARC) already in place. Analytics, CDN, marketing automation, modern CMS all present. The site is well-instrumented.  _[Verified]_

**Strategic Plays:**
- Windows launch (currently waitlist) — the single biggest product gap and the most direct lever on TAM.  _[Verified]_
- Enterprise distribution via Atlassian's existing Jira/Confluence/Trello customer base — the obvious post-acquisition synergy.  _[Inferred]_
- Mobile (iOS/Android) — Dia is desktop-only; Arc had iPhone app. Mobile is a gap relative to Chrome/Safari.  _[Inferred]_

## 6. Deal Thesis
This screen is retrospective — The Browser Company was acquired by Atlassian for $610M on Oct 21, 2025, so it is no longer an investable standalone target. Quadrant placement: HIGH Digital/Tech Maturity (9) × HIGH Business Fundamentals (market 8, growth 8, team 9). This is the OPPOSITE of the framework's sweet spot (low tech + high fundamentals = cheap, fast value-add). Dia is itself the AI/automation play — there is no broken tech on top of a good business for an outside investor to fix. The $610M price implies Atlassian paid for (a) a mature AI-browser product shipped in ~12 months, (b) a design-led team with Apple pedigree, and (c) enterprise distribution synergies with its $4.8B-revenue work-management franchise. For a technology-focused investor today, the only relevant question is whether Atlassian's integration preserves Dia's velocity — not whether to invest in Dia.

## 7. Risks & Red Flags
- Acquisition integration risk — Atlassian's track record on consumer products is unproven; press headline risk ('Atlassian is Going to Ruin Dia').  _[Corroborated]_
- Platform concentration — macOS 14+ M1+ only at public launch; Windows still waitlisted. Excludes the majority of the desktop market.  _[Verified]_
- Arc user-base alienation — freezing Arc in May 2025 to pivot to Dia created goodwill damage among power users; some may not migrate.  _[Corroborated]_
- AI-browser category crowding — Chrome, Edge, Brave, Opera, Perplexity Comet, Spyglass all competing; Chrome's ~65% share is a structural moat.  _[Inferred]_
- Parent financial drag — Atlassian FY26 Q3 operating loss -$200M, net loss -$193M on $4.81B revenue; Dia's contribution not separately disclosed.  _[Verified]_
- No litigation, regulatory, or breach-history flags found in public news search.  _[Inferred]_

## 8. Recommended Next Steps / Human Diligence Items
- Confirm Dia's standalone ARR / paying-subscriber count and Pro-tier conversion rate (not disclosed).  _[Inferred]_
- Confirm current headcount and post-acquisition retention of key design/AI talent (Josh Miller, Marco Triverio, Tara Feener).  _[Inferred]_
- Verify Windows launch timeline — the single biggest TAM lever.  _[Inferred]_
- Verify Atlassian's integration roadmap: is Dia a standalone product, an embedded feature of Jira/Confluence, or both?  _[Speculative]_
- Audit Dia's data-handling and privacy posture for enterprise sales (Trust Center exists at trust.diabrowser.com — review SOC 2 / ISO 27001 status).  _[Inferred]_
- Sanity-check the $610M vs $936M figure discrepancy across sources (USD vs AUD currency conversion likely).  _[Speculative]_
- Review CourtListener for any litigation once a free token is available (anonymous access now 401s).  _[Speculative]_

---
_Generated by the domain-to-diligence skill. Revenue/traffic/headcount are modeled with wide
error bands; review signals can be gamed. Corroborate before acting._
