#!/usr/bin/env python3
"""Pull Maass L-function zeros from the LMFDB API.

    python code/harvest_maass.py
    python code/harvest_maass.py --level 1 --limit 3

Writes code/zeros_maass_<label>_weyl.pkl and prints g1.
LMFDB sometimes serves only the first ~20–40 zeros (positive_zeros).
That is enough for a Gram at μ=22 if g1 is not huge.

If the API is blocked (captcha), the script exits with the URL to open.
"""
from __future__ import annotations

import argparse
import json
import os
import pickle
import ssl
import sys
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
API = "https://www.lmfdb.org/api/lfunc_lfunctions/"


def fetch(params: dict) -> dict:
    q = urllib.parse.urlencode(params)
    url = API + "?" + q
    req = urllib.request.Request(url, headers={"User-Agent": "riemann-weil-phenomenology/maass"})
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
        raw = r.read()
    if raw[:1] == b"<":
        raise RuntimeError(
            "LMFDB returned HTML (captcha). Open in a browser:\n"
            "  https://www.lmfdb.org/L/degree2/MaassForm/\n"
            "and save positive zeros by hand."
        )
    return json.loads(raw)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--level", type=int, default=1)
    p.add_argument("--limit", type=int, default=3)
    args = p.parse_args()
    data = fetch({
        "_format": "json",
        "_per_page": str(args.limit),
        "degree": "2",
        "motivic_weight": "0",
        "conductor": str(args.level),
        "_fields": "label,conductor,origin,positive_zeros",
    })
    recs = data if isinstance(data, list) else data.get("data") or data.get("records") or []
    if isinstance(data, dict) and not recs:
        # some API wrappers nest under 'response'
        recs = data.get("response", [])
    if not recs:
        print("keys", list(data)[:20] if isinstance(data, dict) else type(data))
        sys.exit("no records — LMFDB schema changed or empty query")
    n_ok = 0
    for rec in recs:
        zeros = rec.get("positive_zeros") or []
        zeros = [float(z) for z in zeros if float(z) > 1e-12]
        label = (rec.get("label") or rec.get("origin") or "maass").replace("/", "_")
        print(f"{label} n={len(zeros)} g1={zeros[0] if zeros else float('nan'):.3f}")
        if not zeros:
            continue
        dest = os.path.join(HERE, f"zeros_maass_{label}_weyl.pkl")
        pickle.dump(zeros, open(dest, "wb"))
        print(f"  -> {dest}")
        n_ok += 1
    if n_ok == 0:
        sys.exit("API answered but no positive_zeros fields")
    print("Gram: python code/scan_gl2.py  (add the basename to CURVES) ")


if __name__ == "__main__":
    main()
