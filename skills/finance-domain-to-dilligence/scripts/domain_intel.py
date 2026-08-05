#!/usr/bin/env python3
"""Phase 0 — Domain & Infrastructure Intelligence.

Collects RDAP registration data, DNS-over-HTTPS records (A/MX/NS + SPF/DKIM/DMARC),
and Certificate Transparency subdomains (crt.sh with a Cert Spotter fallback), all from
free/keyless public sources. Emits a JSON blob of findings with confidence tags suitable
for appending to the analysis state object.

Usage:
    python domain_intel.py example.com
    python domain_intel.py example.com --json > phase0.json

Stdlib only. Endpoints/limits documented in ../references/data-sources.md.
"""
import argparse
import json
import sys
import time
import urllib.error
import urllib.request

UA = "domain-to-diligence/1.0 (public-signal screening)"


def _get(url, headers=None, timeout=20, tries=3):
    """GET with basic backoff. Returns (status, body_text) or (None, None) on failure."""
    hdrs = {"User-Agent": UA}
    if headers:
        hdrs.update(headers)
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers=hdrs)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.status, resp.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and attempt < tries - 1:
                time.sleep(2 ** attempt)
                continue
            return e.code, None
        except Exception:
            if attempt < tries - 1:
                time.sleep(2 ** attempt)
                continue
            return None, None
    return None, None


def rdap(domain):
    """Registration/expiration events, registrar, status, nameservers, DNSSEC."""
    status, body = _get(f"https://rdap.org/domain/{domain}",
                         headers={"Accept": "application/rdap+json"})
    out = {"source": "rdap.org", "confidence": "Verified"}
    if status != 200 or not body:
        return {"source": "rdap.org", "confidence": "Speculative", "error": f"status={status}"}
    data = json.loads(body)
    events = {e.get("eventAction"): e.get("eventDate") for e in data.get("events", [])}
    out["registration"] = events.get("registration")
    out["expiration"] = events.get("expiration")
    out["last_changed"] = events.get("last changed")
    out["status"] = data.get("status", [])
    out["nameservers"] = [ns.get("ldhName") for ns in data.get("nameservers", [])]
    out["dnssec"] = bool(data.get("secureDNS", {}).get("delegationSigned"))
    for ent in data.get("entities", []):
        if "registrar" in ent.get("roles", []):
            for item in ent.get("vcardArray", [[], []])[1]:
                if item[0] == "fn":
                    out["registrar"] = item[3]
    return out


def doh(name, rtype):
    """DNS-over-HTTPS via Google. Returns list of record data strings."""
    status, body = _get(f"https://dns.google/resolve?name={name}&type={rtype}")
    if status != 200 or not body:
        return []
    data = json.loads(body)
    return [a.get("data", "").strip('"') for a in data.get("Answer", [])]


def dns_profile(domain):
    """A/MX/NS records + email-auth (SPF/DMARC) presence + email-stack inference."""
    a = doh(domain, "A")
    mx = doh(domain, "MX")
    ns = doh(domain, "NS")
    spf = [t for t in doh(domain, "TXT") if t.lower().startswith("v=spf1")]
    dmarc = [t for t in doh(f"_dmarc.{domain}", "TXT") if "v=dmarc1" in t.lower()]
    stack = "unknown"
    mx_join = " ".join(mx).lower()
    if "google" in mx_join or "googlemail" in mx_join:
        stack = "Google Workspace"
    elif "outlook" in mx_join or "protection.outlook" in mx_join:
        stack = "Microsoft 365"
    elif mx:
        stack = "self-hosted / other"
    return {
        "source": "dns.google (DoH)",
        "confidence": "Verified",
        "a": a, "mx": mx, "ns": ns,
        "email_stack": stack,
        "spf_present": bool(spf),
        "dmarc_present": bool(dmarc),
        "email_auth_gap": not (spf and dmarc),  # missing = easy quick-win
    }


def subdomains(domain):
    """Certificate Transparency subdomain enumeration; crt.sh -> Cert Spotter fallback."""
    status, body = _get(f"https://crt.sh/?q=%25.{domain}&output=json")
    names = set()
    src = "crt.sh"
    if status == 200 and body:
        try:
            for row in json.loads(body):
                for n in row.get("name_value", "").splitlines():
                    n = n.strip().lstrip("*.").lower()
                    if n.endswith(domain):
                        names.add(n)
        except json.JSONDecodeError:
            status = None
    if status != 200 or not names:  # fallback
        src = "certspotter (fallback)"
        s2, b2 = _get(
            f"https://api.certspotter.com/v1/issuances?domain={domain}"
            "&include_subdomains=true&expand=dns_names")
        if s2 == 200 and b2:
            for row in json.loads(b2):
                for n in row.get("dns_names", []):
                    n = n.strip().lstrip("*.").lower()
                    if n.endswith(domain):
                        names.add(n)
    interesting = [p for p in ("app", "api", "status", "careers", "shop", "staging", "admin", "dev")
                   if any(s.startswith(p + ".") for s in names)]
    return {
        "source": src,
        "confidence": "Corroborated" if names else "Speculative",
        "count": len(names),
        "subdomains": sorted(names),
        "signals": interesting,  # product surface / eng maturity / e-commerce tells
    }


def main():
    ap = argparse.ArgumentParser(description="Phase 0 domain & infrastructure intel.")
    ap.add_argument("domain")
    ap.add_argument("--json", action="store_true", help="emit raw JSON only")
    args = ap.parse_args()
    d = args.domain.strip().lower().replace("https://", "").replace("http://", "").rstrip("/")

    result = {
        "phase": 0,
        "domain": d,
        "rdap": rdap(d),
        "dns": dns_profile(d),
        "subdomains": subdomains(d),
    }

    if args.json:
        print(json.dumps(result, indent=2))
        return

    r, dn, sub = result["rdap"], result["dns"], result["subdomains"]
    print(f"# Phase 0 — {d}\n")
    print(f"Registered: {r.get('registration')}   Expires: {r.get('expiration')}")
    print(f"Registrar: {r.get('registrar')}   DNSSEC: {r.get('dnssec')}   [{r['confidence']}]")
    print(f"Email stack: {dn.get('email_stack')}   SPF: {dn.get('spf_present')}   "
          f"DMARC: {dn.get('dmarc_present')}"
          f"{'   ⚠ email-auth quick-win' if dn.get('email_auth_gap') else ''}")
    print(f"Subdomains: {sub.get('count')}   signals: {', '.join(sub.get('signals')) or 'none'}"
          f"   [{sub['confidence']}]")


if __name__ == "__main__":
    sys.exit(main())
