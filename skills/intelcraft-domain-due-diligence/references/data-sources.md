# Data Sources — endpoints, headers, rate limits (single source of truth)

**Maintain this file actively.** Free API access, keys, and rate limits shift frequently.
Recalibrate quarterly. Start on the free tier; add paid data only once volume justifies it.
All sources below are public; obey robots.txt, ToS, and required headers.

`{domain}` = bare domain (e.g. `example.com`). `{query}` = URL-encoded search string.

---

## Phase 0 — Domain & Infrastructure

### RDAP (modern WHOIS replacement; free/keyless)
- Aggregator (auto-routes): `https://rdap.org/domain/{domain}` — ~10 req / 10s Cloudflare limit.
- Direct (example): `https://rdap.verisign.com/com/v1/domain/{domain}`.
- Returns: `events[]` (registration/expiration dates), registrar entity, EPP `status[]`,
  nameservers, DNSSEC.
- Note: gTLD WHOIS no longer mandated since **Jan 28, 2025** — use RDAP. Registrant PII is
  usually redacted (GDPR); do not attempt to de-anonymize it.

### DNS-over-HTTPS (free/keyless)
- Google: `https://dns.google/resolve?name={domain}&type={MX|TXT|A|NS}`
- Cloudflare: `https://cloudflare-dns.com/dns-query?name={domain}&type=MX`
  — requires header `Accept: application/dns-json`.
- Query A, MX, NS, and TXT for:
  - SPF → TXT on `{domain}`
  - DKIM → TXT on `default._domainkey.{domain}`
  - DMARC → TXT on `_dmarc.{domain}`

### Certificate Transparency / subdomain enumeration (free/keyless)
- crt.sh: `https://crt.sh/?q=%25.{domain}&output=json` — parse `name_value`, strip `*.`, dedupe.
  Flaky uptime + aggressive per-IP throttling: use backoff, check status codes, treat
  empty/non-200 as "source failed."
- Fallback — Cert Spotter:
  `https://api.certspotter.com/v1/issuances?domain={domain}&include_subdomains=true&expand=dns_names`

### Wayback Machine (Internet Archive)
- Historical snapshots to gauge domain age, redesign cadence, positioning shifts, neglect.

---

## Phase 2 — Technology Stack Detection

- Passive detection via HTTP response headers (Server, X-Powered-By, Set-Cookie),
  `<script>`/meta tags, JS variables, and DNS; or a hosted detector API (Wappalyzer/BuiltWith).
- Also check: security headers, page speed (Core Web Vitals), mobile responsiveness, accessibility.
- Caveat: passive fingerprinting misses hidden backends. Carry the detector's own confidence through.

---

## Phase 4 — Financial & Business Signals

### SEC EDGAR (free)
- **REQUIRED** header: `User-Agent: "Name email"`. Limit: **10 req/s**.
- Submissions: `https://data.sec.gov/submissions/CIK##########.json` (10-digit zero-padded CIK)
- Company Facts: `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json`
- Full-text search: `https://efts.sec.gov/LATEST/search-index?q=...`
- Ticker→CIK map: `https://www.sec.gov/files/company_tickers.json`
- Coverage: public companies + anyone named in filings.

### Business registries
- OpenCorporates API: `https://api.opencorporates.com/v0.4/...` — free for open-data/journalism,
  commercial from ~£2,250/yr. Incorporation date, status, officers, jurisdiction.
- State Secretary of State business search — free but fragmented (access, fields, bulk
  availability vary widely by state; Texas SOSDirect charges $1/search, others free).

### Funding history
- Crunchbase / PitchBook-style public profiles for rounds, investors, totals (paid at volume).

---

## Phase 6 — Customer & Reputation

### News (free/keyless)
- Google News RSS: `https://news.google.com/rss/search?q={query}`
- GDELT: `https://api.gdeltproject.org/api/v2/doc/doc?query={query}&mode=ArtList&format=json`
  — includes tone/sentiment.

### Review & community sources
- G2, Capterra, Trustpilot, Google, Yelp (respect ToS — no auth scraping).
- Reddit / forums = most honest sentiment; use to sanity-check curated review sites (which can
  be gamed — >26% of recent G2 reviews likely AI-generated per Originality.ai, Nov 2025).

---

## Phase 7 — Risk & Compliance

### CourtListener REST API v4
- `https://www.courtlistener.com/api/rest/v4/search/?q={query}&type=o`
- **Note (2026):** anonymous requests now return **401** — a free token is required:
  header `Authorization: Token {token}`.
- Free-tier limits: ~5 req/min, 50/hr, 125/day.
- Includes RECAP federal dockets (a free PACER mirror).

---

## Paid / add-later tier

Add only once volume justifies it: Crunchbase, SimilarWeb, BuiltWith, PitchBook.

## Known churn to watch (recalibrate quarterly)

- gTLD WHOIS mandate ended Jan 28, 2025 → RDAP only.
- CourtListener tightened anonymous limits in 2026 (now token-required).
- PatentsView went key-only in 2025, migrating to USPTO's Open Data Portal.
