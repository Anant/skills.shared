# Scoring Rubrics — 1–10 anchors, weighting presets, verdict logic

Each dimension is scored **1–10** with explicit anchors, multiplied by its weight, and summed
to a **0–100 composite**. Run `scripts/score.py` for the arithmetic and verdict — don't do it
by hand. Wrap every numeric output in a confidence band.

---

## The 8 dimensions

| # | Dimension | What it measures | Primary phases |
|---|-----------|------------------|----------------|
| 1 | Market Attractiveness | Size, growth, fragmentation, defensibility | 5 |
| 2 | Business Model Quality | Revenue quality, recurring/ARR, pricing power, retention | 1,4,6 |
| 3 | Growth Trajectory | Headcount/hiring velocity, traffic trend, funding momentum | 3,4,5 |
| 4 | Digital/Tech Maturity | Stack modernity, data/automation, security | 0,1,2 |
| 5 | Team Strength | Leadership pedigree, org depth, culture | 3 |
| 6 | Financial Health Proxy | Scale, funding, runway, profitability signals | 4 |
| 7 | Risk Profile | Litigation, compliance, concentration, key-person | 7 |
| 8 | Technology Uplift Opportunity | Size & feasibility of tech/AI/automation value-add | 2,8 |

---

## Rubric anchors

### Dimension 8 — Technology Uplift Opportunity (the worked example)

- **1–2:** Already best-in-class tech; little to add.
- **3–4:** Modern stack, marginal gains.
- **5–6:** Some clear gaps (e.g., no marketing automation).
- **7–8:** Multiple high-value gaps + strong business = strong thesis.
- **9–10:** Pervasive tech neglect on top of an excellent, profitable business = ideal.

### Dimension 4 — Digital/Tech Maturity

- **1–3:** Shared hosting, no CDN, no email auth, no analytics, stale/neglected site.
- **4–6:** Common CMS (e.g., WordPress), basic analytics, partial security headers.
- **7–8:** Modern CDN, DNSSEC, full email auth, marketing automation, clean subdomain architecture.
- **9–10:** Headless/custom stack, integrated data, strong Core Web Vitals, mature security posture.

> **Note — this dimension is intentionally NOT inverted.** For a technology-focused firm the
> highest-value quadrant is *low* dim 4 + *high* fundamentals + *high* dim 8. Low maturity is
> the opportunity, captured by dim 8. See "The key insight" below.

### General anchor pattern (apply to dims 1,2,3,5,6,7)

- **1–2:** Fatal/absent — the signal argues against the deal (tiny/shrinking market, no revenue
  quality, no growth, weak/absent team, distressed financials, severe unmitigated risk).
- **3–4:** Below average — real weaknesses that would need fixing.
- **5–6:** Average / mixed — some strengths, some gaps; the base case.
- **7–8:** Strong — a clear positive with corroboration.
- **9–10:** Best-in-class — verified, durable advantage.

For **Risk Profile (dim 7), score inversely:** more/severe risks → *lower* score (10 = clean,
1 = fatal flags).

---

## Weighting presets

### Platform / Acquisition target (default)
Balances fundamentals with uplift; Risk and Financial Health weighted higher because you're
buying control.

| Dim | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|-----|---|---|---|---|---|---|---|---|
| Weight | 15% | 15% | 12% | 10% | 10% | 13% | 10% | 15% |

### Growth Partnership
You're betting on trajectory, not buying the whole thing. Raise Growth Trajectory and
Technology Uplift; lower Financial Health.

- Growth Trajectory → **18%**, Technology Uplift → **18%**, Financial Health → **8%**.
  (Redistribute the remaining weight across the other dimensions so the total = 100%.)

### Services Client
You just need a fixable problem and the ability to pay. Raise Technology Uplift and the Digital
Maturity gap; lower Market/Financial.

- Technology Uplift → **25%**, with Market Attractiveness and Financial Health reduced accordingly.

> Weights are a starting template — calibrate them to the firm's actual deal outcomes over time.

---

## The key insight (encoded in verdict logic)

For a technology-focused firm the highest-value quadrant is **low Digital/Tech Maturity
(dim 4 low) + high Business Fundamentals (dims 1, 2, 6 high) + high Technology Uplift
(dim 8 high)**. The scoring intentionally *rewards* this combination rather than penalizing
low tech maturity outright — broken tech on a good business is the cheapest, fastest value-add.

---

## Verdict taxonomy

| Composite + pattern | Verdict |
|---------------------|---------|
| 75+ with high uplift + strong fundamentals | **Platform Investment** |
| 65–80, strong fit within a thesis, smaller | **Bolt-on / Add-on** |
| 60–75, high trajectory, minority/growth | **Growth Partnership** |
| 55–75, fixable tech gap + ability to pay, but not investable | **Services Opportunity** |
| 45–65, weak now but salvageable | **Turnaround / Watch** |
| <45 or fatal risk flags | **Pass** |

Bands overlap — the *pattern* disambiguates. A fatal risk flag (dim 7 ≤ 2) forces **Pass**
regardless of composite. When two verdicts are plausible, state both and explain the swing
factor.
