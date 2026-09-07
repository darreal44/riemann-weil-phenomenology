#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""User-assisted LMFDB Maass zero scrape (Playwright).

You solve the captcha in the window. The script does not
bypass it. Not a harvest of Q. Not Weil.

    pip install playwright
    playwright install chromium
    python code/scrape_lmfdb_maass.py 1.0.1.1.1 11.0.1.1.1

Writes code/zeros_<label>.txt for import_maass_zeros.py.
"""
from __future__ import annotations

import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
SEARCH = "https://www.lmfdb.org/ModularForm/GL2/Q/Maass/"


def looks_blocked(html: str) -> bool:
    h = html.lower()
    return any(
        s in h
        for s in (
            "captcha",
            "unusual traffic",
            "cloudflare",
            "enable javascript",
            "checking your browser",
        )
    )


def parse_zeros(text: str) -> list[float]:
    nums = re.findall(r"[-+]?\d+\.\d+(?:[eE][-+]?\d+)?", text)
    z = sorted({float(x) for x in nums if 1.0 < float(x) < 1.0e5})
    return z


def main() -> int:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit("pip install playwright && playwright install chromium")

    labels = sys.argv[1:] or ["1.0.1.1.1"]
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(SEARCH, wait_until="domcontentloaded", timeout=60000)
        print("Solve any captcha in the window, then press Enter here.", flush=True)
        input()
        html = page.content()
        if looks_blocked(html):
            print("Still blocked. Solve and press Enter again.", flush=True)
            input()

        for lab in labels:
            # Search box: label is N.w.tr.fr.n — use the page search.
            page.goto(SEARCH, wait_until="domcontentloaded", timeout=60000)
            # Try the L-function origin URL pattern used by LMFDB Maass.
            url = SEARCH + lab + "/"
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            time.sleep(1.0)
            html = page.content()
            if looks_blocked(html):
                print(f"{lab}: captcha. Solve, press Enter.", flush=True)
                input()
                html = page.content()
            text = page.inner_text("body")
            z = parse_zeros(text)
            dest = os.path.join(HERE, f"zeros_{lab}.txt")
            open(dest, "w", encoding="utf-8").write("\n".join(f"{x:.12f}" for x in z) + "\n")
            print(f"{lab} n={len(z)} -> {dest}", flush=True)
            if z:
                print(f"  then: python code/import_maass_zeros.py {lab} {dest}", flush=True)
        browser.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
