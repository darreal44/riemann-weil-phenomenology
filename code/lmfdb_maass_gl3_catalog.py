#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""LMFDB Maass GL3 catalog (L-search Download, origin MaassGL3).

    python code/lmfdb_maass_gl3_catalog.py

1532 rows, degree 3, N∈{1,4}. Columns include label, conductor,
central character, mus (three Γ_R shifts), z1 (first zero only).
No full positive_zeros, no a_n. Not GL2. Not Weil.

Gamma is Γ_R(s+iμ₁) Γ_R(s+iμ₂) Γ_R(s+iμ₃), μ₁+μ₂+μ₃=0,
not Γ_R(s±iR) of scan_q_maass.

Cite: The LMFDB Collaboration, The L-functions and modular
forms database, https://www.lmfdb.org, 2026, [Online;
accessed 7 September 2026]. Object: L-functions of GL(3)
Maass forms, origin MaassGL3. BibTeX in notes/lmfdb.bib.
See notes/scrape-lmfdb-maass.md.
"""
from __future__ import annotations

import ast
import csv
import glob
import os
import sys

import lmfdb_maass_catalog as gl2

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def csv_path() -> str:
    hits = sorted(glob.glob(os.path.join(ROOT, "lmfdb_lfunc_search_*.csv")))
    if not hits:
        sys.exit("missing lmfdb_lfunc_search_*.csv at repo root")
    return hits[-1]


def _truth(s: str) -> bool:
    return s.strip() in ("True", "true", "1")


def load_csv(path: str | None = None) -> list[dict]:
    path = path or csv_path()
    rows: list[dict] = []
    with open(path, encoding="utf-8", newline="") as f:
        r = csv.reader(f)
        header = [gl2._col(h) for h in next(r)]
        for raw in r:
            if len(raw) < 17:
                continue
            rec = dict(zip(header, raw))
            if int(rec["degree"]) != 3:
                continue
            mus = ast.literal_eval(rec["mus"])
            rec["N"] = int(rec["conductor"])
            rec["degree"] = 3
            rec["mus"] = [(float(a), float(b)) for a, b in mus]
            rec["mu"] = [b for _, b in rec["mus"]]
            rec["z1"] = float(rec["z1"])
            rec["self_dual"] = _truth(rec["self_dual"])
            rec["algebraic"] = _truth(rec["algebraic"])
            rec["primitive"] = _truth(rec["primitive"])
            rec["origin"] = ast.literal_eval(rec["instance_urls"])[0]
            rows.append(rec)
    return rows


def load(path: str | None = None) -> list[dict]:
    pkl = os.path.join(HERE, "lmfdb_maass_gl3.pkl")
    if path is None and os.path.exists(pkl):
        import pickle

        return pickle.load(open(pkl, "rb"))["rows"]
    return load_csv(path)


def main() -> int:
    recs = load()
    levels = sorted({r["N"] for r in recs})
    n1 = sum(1 for r in recs if r["N"] == 1)
    z = [r["z1"] for r in recs]
    print(
        f"n={len(recs)} levels={levels} "
        f"n1={n1} n4={len(recs) - n1} "
        f"first={recs[0]['label']} z1={recs[0]['z1']:.5f} "
        f"last={recs[-1]['label']} "
        f"z1min={min(z):.6f} z1max={max(z):.5f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
