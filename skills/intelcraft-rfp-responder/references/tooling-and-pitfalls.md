# Tooling & Common Pitfalls

## Tooling (optional — suggest, never require)

This skill is fully functional with Markdown output alone. When the user wants polished deliverables, suggest installing:

| Need | Tool | Install |
|---|---|---|
| Markdown → Word | pandoc | `brew install pandoc` / `apt install pandoc` → `pandoc proposal.md -o proposal.docx --reference-doc=firm-template.docx` |
| Native .docx generation (styled tables, TOC, red placeholders) | docx (npm) | `npm install docx` |
| One-page printable checklist | plain HTML + `@page` CSS | none — any browser prints it |
| Scanned-PDF text extraction | pdfplumber / tesseract | `pip install pdfplumber` · `apt install tesseract-ocr` |
| Render/verify docx | LibreOffice + poppler | `apt install libreoffice poppler-utils` |

If none are available, deliver Markdown with an instruction block showing the pandoc command for later conversion.

Note: in environments with native document skills available (e.g., a docx skill), prefer those for producing the styled Word deliverable — red/bold placeholders, TOC, and tables render natively.

## Common Pitfalls (Phase 5 red-flag pass checklist)

1. **Trusting the cover page over amendments** — preference programs, goals, and attachment locations get corrected in Q&A amendments; the corrected value governs.
2. **Recreating official forms** — governments require *their* form with *their* signature block; always insert the real form, never a lookalike.
3. **Missing the "submit WITH proposal" trap** — some plans/certifications (subcontracting plans, security plans) are due at submission, not award; late = rejected.
4. **Inventing past performance or references** — placeholders only; fabrication is disqualifying and sometimes actionable.
5. **Page-limit violations (federal)** — excess pages are removed before evaluation; the rubric response buried on page 31 of 30 never gets read.
6. **Rate-cutting on task-order vehicles** — locked rates govern all future work; cut hours, not rates.
7. **Ignoring absorbed costs** — bonds, insurance, escrow, and prevailing-wage deltas must live inside the evaluated price.
8. **Submitting without re-checking the portal** — always verify no new amendment posted between draft and submission; acknowledge every amendment by number and date.
