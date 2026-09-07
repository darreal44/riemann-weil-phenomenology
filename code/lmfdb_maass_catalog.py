#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""LMFDB maass_rigor search dump (CSV from the Download form).

    python code/lmfdb_maass_catalog.py

35416 rows: label, N, k, χ, R, symmetry, Fricke.
No L-zeros, no a_n. Not Weil.

Cite: The LMFDB Collaboration, The L-functions and modular
forms database, https://www.lmfdb.org, 2026, [Online;
accessed 7 September 2026]. Object: Maass forms of weight 0
on GL(2) over Q, /ModularForm/GL2/Q/Maass/. BibTeX in
notes/lmfdb.bib. See notes/scrape-lmfdb-maass.md.
"""
from __future__ import annotations

import ast
import csv
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
COL_RE = re.compile(r'"([a-z0-9_]+)"\)\s*$')


def csv_path() -> str:
    hits = sorted(glob.glob(os.path.join(ROOT, "lmfdb_maass_rigor_*.csv")))
    if not hits:
        sys.exit("missing lmfdb_maass_rigor_*.csv at repo root")
    return hits[-1]


def _col(h: str) -> str:
    m = COL_RE.search(h.strip())
    return m.group(1) if m else h


def load_csv(path: str | None = None) -> list[dict]:
    path = path or csv_path()
    rows: list[dict] = []
    with open(path, encoding="utf-8", newline="") as f:
        r = csv.reader(f)
        header = [_col(h) for h in next(r)]
        for raw in r:
            if len(raw) < 7:
                continue
            rec = dict(zip(header, raw))
            rec["N"] = int(rec["level"])
            rec["weight"] = int(float(rec["weight"]))
            rec["R"] = float(rec["spectral_parameter"])
            rec["symmetry"] = int(float(rec["symmetry"]))
            rec["fricke"] = int(float(rec["fricke_eigenvalue"]))
            rec["label"] = rec["maass_label"]
            rec["degree"] = 2
            chi = rec.get("character") or "[1, 1]"
            if chi.startswith("["):
                q, n = ast.literal_eval(chi)
                rec["character"] = f"{q}.{n}"
            rows.append(rec)
    return rows


def load(path: str | None = None) -> list[dict]:
    """Prefer the slim pkl used by scanners; CSV only to (re)encode."""
    pkl = os.path.join(HERE, "lmfdb_maass_gl2.pkl")
    if path is None and os.path.exists(pkl):
        import pickle

        return pickle.load(open(pkl, "rb"))["rows"]
    return load_csv(path)


def main() -> int:
    recs = load()
    levels = sorted({r["N"] for r in recs})
    print(
        f"n={len(recs)} levels={len(levels)} "
        f"N={levels[0]}..{levels[-1]} "
        f"first={recs[0]['label']} R={recs[0]['R']:.6f} "
        f"last={recs[-1]['label']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
