#!/usr/bin/env python3
"""Phase 9 — Composite scoring + verdict.

Reads a JSON state object with per-dimension 1-10 scores, applies a weighting preset,
computes the 0-100 composite, and assigns a PE-style verdict. Rubric anchors and preset
rationale live in ../references/scoring-rubrics.md.

State schema (scores 1-10; extra keys ignored):
    {
      "company": "Acme Inc",
      "scores": {
        "market": 7, "business_model": 8, "growth": 6, "digital_maturity": 3,
        "team": 6, "financial_health": 7, "risk": 8, "tech_uplift": 9
      }
    }

Usage:
    python score.py --state state.json --preset platform
    echo '{"scores":{...}}' | python score.py --preset growth
"""
import argparse
import json
import sys

DIMENSIONS = [
    ("market", "Market Attractiveness"),
    ("business_model", "Business Model Quality"),
    ("growth", "Growth Trajectory"),
    ("digital_maturity", "Digital/Tech Maturity"),
    ("team", "Team Strength"),
    ("financial_health", "Financial Health Proxy"),
    ("risk", "Risk Profile"),
    ("tech_uplift", "Technology Uplift Opportunity"),
]

PRESETS = {
    # weights must sum to 1.0
    "platform": {"market": .15, "business_model": .15, "growth": .12, "digital_maturity": .10,
                 "team": .10, "financial_health": .13, "risk": .10, "tech_uplift": .15},
    "growth":   {"market": .13, "business_model": .14, "growth": .18, "digital_maturity": .10,
                 "team": .10, "financial_health": .08, "risk": .09, "tech_uplift": .18},
    "services": {"market": .08, "business_model": .12, "growth": .10, "digital_maturity": .12,
                 "team": .08, "financial_health": .08, "risk": .12, "tech_uplift": .25},
}


def verdict(composite, s):
    """Assign verdict from composite + the fundamentals/uplift pattern."""
    if s.get("risk", 10) <= 2:
        return "Pass", "fatal risk flag (Risk ≤ 2) overrides composite"
    uplift = s.get("tech_uplift", 0)
    fundamentals = (s.get("market", 0) + s.get("business_model", 0) + s.get("financial_health", 0)) / 3
    growth = s.get("growth", 0)
    if composite < 45:
        return "Pass", "composite below 45"
    if composite >= 75 and uplift >= 7 and fundamentals >= 6.5:
        return "Platform Investment", "high composite, high uplift, strong fundamentals — the sweet spot"
    if 60 <= composite <= 75 and growth >= 7:
        return "Growth Partnership", "high trajectory; minority/growth bet"
    if 65 <= composite <= 80:
        return "Bolt-on / Add-on", "strong fit within a thesis, smaller"
    if 55 <= composite <= 75 and uplift >= 6:
        return "Services Opportunity", "fixable tech gap + ability to pay, but not investable"
    if 45 <= composite <= 65:
        return "Turnaround / Watch", "weak now but salvageable"
    return "Turnaround / Watch", "ambiguous band — human review of the swing factors"


def main():
    ap = argparse.ArgumentParser(description="Phase 9 composite scoring + verdict.")
    ap.add_argument("--state", help="path to JSON state file (default: stdin)")
    ap.add_argument("--preset", choices=PRESETS, default="platform")
    args = ap.parse_args()

    raw = open(args.state).read() if args.state else sys.stdin.read()
    state = json.loads(raw)
    scores = state.get("scores", state)  # allow a bare scores dict too
    weights = PRESETS[args.preset]

    missing = [k for k, _ in DIMENSIONS if k not in scores]
    if missing:
        print(f"[score] WARNING: missing dimensions treated as 0: {missing}", file=sys.stderr)

    rows, composite = [], 0.0
    for key, label in DIMENSIONS:
        raw_score = float(scores.get(key, 0))
        w = weights[key]
        contribution = raw_score * w * 10  # 1-10 * weight, scaled to 0-100
        composite += contribution
        rows.append((label, raw_score, w, contribution))

    v, why = verdict(composite, scores)

    print(f"# Scorecard — {state.get('company', 'company')}  (preset: {args.preset})\n")
    print(f"{'Dimension':<32}{'Score':>6}{'Weight':>9}{'Contrib':>10}")
    print("-" * 57)
    for label, sc, w, c in rows:
        print(f"{label:<32}{sc:>6.1f}{w*100:>8.0f}%{c:>10.2f}")
    print("-" * 57)
    print(f"{'COMPOSITE':<32}{'':>6}{'':>9}{composite:>10.2f}")
    print(f"\nVerdict: {v}\nReason:  {why}")

    result = {
        "company": state.get("company"),
        "preset": args.preset,
        "composite": round(composite, 2),
        "verdict": v,
        "verdict_reason": why,
        "dimensions": [{"dimension": l, "score": s, "weight": w, "contribution": round(c, 2)}
                       for l, s, w, c in rows],
    }
    with open("scorecard.json", "w") as f:
        json.dump(result, f, indent=2)
    print("\n(wrote scorecard.json)")


if __name__ == "__main__":
    sys.exit(main())
