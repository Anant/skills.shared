#!/usr/bin/env python3
"""Phase 4 — SEC EDGAR lookup (submissions, company facts, ticker->CIK).

The SEC requires a descriptive User-Agent of the form "Name email" and enforces a 10 req/s
limit. Set your contact via --ua or the SEC_UA env var; a placeholder is used otherwise
(replace it before real use).

Usage:
    python sec_lookup.py --ticker CRM
    python sec_lookup.py --cik 0001108524
    python sec_lookup.py --ticker CRM --facts Revenues --ua "Jane Doe jane@firm.com"

Only public companies (and entities named in filings) appear here. Stdlib only.
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

DEFAULT_UA = os.environ.get("SEC_UA", "Domain-to-Diligence placeholder@example.com")
_last_call = [0.0]


def _get(url, ua):
    """GET honoring the SEC 10 req/s limit and required UA header."""
    gap = time.monotonic() - _last_call[0]
    if gap < 0.11:  # ~9 req/s to stay under the ceiling
        time.sleep(0.11 - gap)
    req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            _last_call[0] = time.monotonic()
            return json.loads(resp.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as e:
        print(f"[sec] HTTP {e.code} for {url}", file=sys.stderr)
    except Exception as e:
        print(f"[sec] error {e} for {url}", file=sys.stderr)
    return None


def ticker_to_cik(ticker, ua):
    data = _get("https://www.sec.gov/files/company_tickers.json", ua)
    if not data:
        return None
    for row in data.values():
        if row.get("ticker", "").upper() == ticker.upper():
            return str(row["cik_str"]).zfill(10)
    return None


def submissions(cik, ua):
    return _get(f"https://data.sec.gov/submissions/CIK{cik}.json", ua)


def company_facts(cik, ua):
    return _get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json", ua)


def latest_fact(facts, concept):
    """Most recent USD value for an XBRL concept (e.g. 'Revenues', 'Assets')."""
    node = facts.get("facts", {}).get("us-gaap", {}).get(concept)
    if not node:
        return None
    best = None
    for unit_vals in node.get("units", {}).values():
        for v in unit_vals:
            if v.get("end") and (best is None or v["end"] > best["end"]):
                best = v
    return best


def main():
    ap = argparse.ArgumentParser(description="Phase 4 SEC EDGAR lookup.")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--ticker")
    g.add_argument("--cik", help="10-digit zero-padded CIK")
    ap.add_argument("--facts", nargs="*", default=["Revenues"],
                    help="us-gaap concepts to pull (default: Revenues)")
    ap.add_argument("--ua", default=DEFAULT_UA, help='SEC User-Agent "Name email"')
    args = ap.parse_args()

    if "placeholder@example.com" in args.ua:
        print("[sec] WARNING: using placeholder User-Agent — set --ua or $SEC_UA "
              '(SEC requires "Name email").', file=sys.stderr)

    cik = args.cik.zfill(10) if args.cik else ticker_to_cik(args.ticker, args.ua)
    if not cik:
        print(json.dumps({"phase": 4, "confidence": "Speculative",
                          "error": "CIK not found — likely private company"}, indent=2))
        return

    sub = submissions(cik, args.ua) or {}
    facts = company_facts(cik, args.ua) or {}
    recent = sub.get("filings", {}).get("recent", {})
    out = {
        "phase": 4,
        "source": "SEC EDGAR",
        "confidence": "Verified",  # primary source
        "cik": cik,
        "name": sub.get("name"),
        "sic": sub.get("sicDescription"),
        "tickers": sub.get("tickers"),
        "exchanges": sub.get("exchanges"),
        "recent_filings": [
            {"form": f, "date": d}
            for f, d in list(zip(recent.get("form", []), recent.get("filingDate", [])))[:5]
        ],
        "financials": {},
    }
    for concept in args.facts:
        val = latest_fact(facts, concept)
        if val:
            out["financials"][concept] = {"value": val["val"], "end": val["end"],
                                          "form": val.get("form")}
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    sys.exit(main())
