---
name: rfp-proposal-responder
description: "End-to-end RFP/solicitation response workflow: read every solicitation document and amendment, extract the scoring rubric, produce a one-page outline & compliance checklist, then generate a complete draft proposal in the government's mandated structure with firm-specific data flagged as REQUIRED placeholders, plus cost/timeline estimation. Covers three tracks: state & local law enforcement / public safety (CJIS, NIBRS, MBE/MFD goals, bonds), federal defense & intelligence (FAR/DFARS, Sections L & M, CMMC, clearances), and small business & nonprofit (grants, foundations, simplified procurements). Use whenever the user mentions an RFP, RFI, RFQ, solicitation, bid, proposal response, statement of work response, compliance matrix, evaluation criteria, amendment analysis, or asks 'can we bid this' / 'what would it take to win this' — even if they only upload solicitation PDFs without asking a question yet."
---

# RFP Proposal Responder

**Tier:** POWERFUL · **Category:** Business Growth · **Domain:** Government Procurement, Capture Management, Proposal Writing

A repeatable pipeline that turns a pile of solicitation PDFs into three deliverables:

1. **One-page Outline & Checklist** — printable synthesis of the rubric, mandated proposal structure, deadlines, and disqualification traps
2. **Complete Draft Proposal** — full document in the government's exact mandated section order; everything derivable from the solicitation written in final prose, firm-specific data flagged in red as `[REQUIRED]` placeholders
3. **Cost & Timeline Estimate** — bottoms-up range using solicitation signals (bond size, thresholds, user counts, term length) plus market comparables

**Not a substitute for capture strategy or legal review.** Drafts are strong starting points; price-to-win and teaming decisions stay human.

---

## Core Principles (apply to every track)

1. **The rubric is the outline.** Structure every response around the evaluators' scoresheet, in their order, using their labels and numbering. Never invent a structure.
2. **Amendments override everything.** Read every amendment before drafting. Amendments routinely reverse cover-page errors, change subcontracting goals, relocate attachments, and confirm/deny extensions. Build an "Amendment Corrections" list first.
3. **Placeholders, never fabrication.** Anything firm-specific (names, references, personnel, certifications, past performance, prices) becomes a visibly-flagged `[REQUIRED]` placeholder. Never invent references, credentials, or numbers.
4. **Compliance before eloquence.** A beautiful proposal that misses a mandatory form is rejected unread. Extract every pass/fail item into a checklist before writing a single narrative sentence.
5. **Answer the mandatory affirmations verbatim.** When a solicitation says "the Offeror must specifically state X," write a sentence that specifically states X, bolded, citing the section number.
6. **Price hours, protect rates.** Where labor rates get locked into the contract (task-order vehicles), competitiveness comes from reducing estimated *hours* per deliverable — never from cutting rates that will govern years of future work.

---

## Track Selection (do this first)

Identify the track from the issuing entity and vehicle, then read the matching reference file before Phase 2:

| Signal | Track | Read |
|---|---|---|
| County/city/state agency, BidNet/Periscope portal, CJIS/NIBRS/bonds/MBE goals | **A — State & Local Law Enforcement / Public Safety** | `references/track-a-state-local.md` |
| SAM.gov, Sections L & M, FAR/DFARS, CMMC, clearances, IDIQ/GWAC/OTA | **B — Federal Defense & Intelligence** | `references/track-b-federal.md` |
| Foundation RFP, grants.gov, 501(c)(3) eligibility, logic model, budget narrative | **C — Small Business & Nonprofits** | `references/track-c-smallbiz-nonprofit.md` |

If signals are mixed (e.g., federal pass-through grant to a nonprofit), read both relevant tracks.

---

## Workflow (repeatable, all tracks)

### Phase 1 — Ingest & Inventory

1. List every provided file. Identify: base solicitation, amendments, attachments/exhibits, Q&A documents.
2. Read documents in this order: **amendments first** (they change everything downstream), then evaluation/award sections, then submission instructions, then scope/SOW, then attachments.
3. If PDFs are scanned images, note it and OCR or ask for text versions. If a referenced attachment is missing, flag it — sometimes it's embedded inside another document (check page footers like "L1", "K1").
4. Build the **Solicitation Fact Sheet** — template T1 in `references/templates.md`.

### Phase 2 — Rubric & Compliance Extraction

1. Extract the full scoring table: criteria, points/weights, and which proposal section feeds each criterion.
2. Extract the **mandated proposal structure** (numbered submission items) — this becomes the table of contents verbatim.
3. Extract every pass/fail gate: registrations, forms, signatures, bonds, certifications, page limits, font/format rules, submission portal, deadline. Record each in the Compliance Matrix (template T2).
4. Produce **Deliverable 1: one-page Outline & Checklist** (print-optimized; two columns: rubric + structure on the left, flags + compliance on the right).

### Phase 3 — Draft Generation

1. Write the full proposal in the mandated structure using the Section Skeleton (template T3). For each section:
   - Write final prose for everything derivable from the solicitation (affirmations, responsibility matrices, SOW methodology per deliverable, SLA tables, schedules, security plans, compliance summaries).
   - Insert `[REQUIRED — description of what's needed]` for firm data, styled red/bold.
   - Add a REQUIRED callout box wherever a government form must be downloaded, signed, and inserted (never recreate official forms — reference them).
2. Include: cover page, TOC, compliance affirmations in the cover letter, amendment acknowledgment table, and a pre-award readiness appendix. Use template T5 for the executive summary / win themes.
3. Output as Markdown. Offer docx conversion (see `references/tooling-and-pitfalls.md`).

### Phase 4 — Cost & Timeline

1. Mine the solicitation for price signals: bond amounts, "high dollar" thresholds, user counts, term length, labor category tables, mandatory SLAs.
2. Build a component table (one-time vs. recurring) with low/high ranges from market comparables for the system class — template T4.
3. State the evaluated-price sweet spot and what fixed costs (bonds, insurance, escrow) must be absorbed into pricing.
4. If AI-assisted delivery (e.g., Claude Code) is assumed: apply savings only to code-heavy services (interfaces, ETL, test automation, documentation), never to COTS subscriptions; note that calendar compression is limited by government-paced activities (workshops, UAT, training).

### Phase 5 — Review Gates (adapt color-team language to audience)

- **Compliance pass:** every checklist item mapped to a page number.
- **Rubric pass:** score the draft against the extracted rubric as an evaluator would.
- **Red-flag pass:** unsupported claims, invented facts, missed affirmations, stale amendment status ("check for Amendment N+1 before submitting"). Consult `references/tooling-and-pitfalls.md` for the full pitfall list.

---

## Reference Files (progressive disclosure)

| File | When to read |
|---|---|
| `references/track-a-state-local.md` | Track A engagements — CJIS/NIBRS, bonds, MBE/MFD, interfaces, scoring patterns |
| `references/track-b-federal.md` | Track B engagements — Sections L & M, FAR/DFARS flow-downs, CMMC/SPRS, CPARS |
| `references/track-c-smallbiz-nonprofit.md` | Track C engagements — eligibility gates, budget narratives, logic models, grants.gov mechanics |
| `references/templates.md` | Phases 1–4 — Fact Sheet (T1), Compliance Matrix (T2), Section Skeleton (T3), Cost Model (T4), Win Themes (T5) |
| `references/tooling-and-pitfalls.md` | Phase 3 output conversion, Phase 5 red-flag pass, and before final delivery |

---

## Definition of Done (per engagement)

- ☐ Fact Sheet complete; all documents inventoried and read (amendments first)
- ☐ One-page Outline & Checklist delivered (printable)
- ☐ Compliance Matrix rows all mapped to proposal sections
- ☐ Full draft in mandated structure; every placeholder flagged `[REQUIRED]`
- ☐ Cost & timeline range with stated assumptions
- ☐ Rubric self-score + red-flag list delivered with the draft
