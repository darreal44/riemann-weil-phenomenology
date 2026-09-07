#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Pair Table 1 zeros with the matching LMFDB/Zenodo a_n.

    python code/maass_table1_pair.py

Checks R and γ1 against Table 1, Gram at μ=6, and Q00 of the
textbook pair (s0=1/4±iR/2, Λ/√n). Not a take. Not Weil.
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from calibrate_maass_q import G00, arch00, prim00  # noqa: E402
from lmfdb_encode import by_label_gl2  # noqa: E402
from maass_table1 import ALIAS, NOT_TABLE1, TABLE1  # noqa: E402
from scan_gl2 import gram  # noqa: E402
from scan_q_maass import load_form  # noqa: E402

MU = 6.0
NB = 12


def pair_one(name: str, catalog: dict) -> dict:
    spec = TABLE1[name]
    rec = load_form(name)
    slug = rec["slug"]
    cat = catalog[slug]
    zs = os.path.join(HERE, f"zeros_{name}_weyl.pkl")
    g00 = G00(zs, MU)
    lam, ell = gram(name, MU, NB)
    even = int(rec.get("symmetry", 1)) > 0
    kind = "quarter" if even else "odd_quarter"
    arch = arch00(MU, rec["R"], rec["N"], kind)
    prim = prim00(rec["an"], MU, 0.5)
    q00 = arch - prim
    return {
        "name": name,
        "label": slug,
        "R_json": rec["R"],
        "R_csv": cat["R"],
        "R_table1": spec["R"],
        "g1_pkl": None,
        "g1_table1": spec["g1"],
        "symmetry": rec.get("symmetry"),
        "even": int(rec.get("symmetry", 1)) > 0,
        "G00": g00,
        "Q00": q00,
        "arch00": arch,
        "prim00": prim,
        "gram_lam0": lam,
        "gram_ell0": ell[0],
        "r_match": abs(rec["R"] - spec["R"]) < 1e-4,
        "catalog_match": abs(cat["R"] - spec["R"]) < 1e-4,
        "not_lexicographic": slug not in NOT_TABLE1,
    }


def run() -> dict:
    catalog = by_label_gl2()
    from scan_gl2 import zeros

    rows = []
    for name in TABLE1:
        rec = pair_one(name, catalog)
        rec["g1_pkl"] = float(zeros(name)[0])
        rec["g1_match"] = abs(rec["g1_pkl"] - rec["g1_table1"]) < 0.01
        rows.append(rec)
        print(
            f"{name} {rec['label']} R={rec['R_json']:.4f} "
            f"g1={rec['g1_pkl']:.4f} G00={rec['G00']:.4f} Q00={rec['Q00']:.3f} "
            f"Gram_ell0={rec['gram_ell0']:.2f} "
            f"ok={rec['r_match'] and rec['g1_match'] and rec['not_lexicographic']}",
            flush=True,
        )
    lex = {lab: catalog[lab]["R"] for lab in NOT_TABLE1 if lab in catalog}
    all_ok = all(r["r_match"] and r["g1_match"] and r["not_lexicographic"] for r in rows)
    return {
        "step_taken": False,
        "verdict": "KILL",
        "why": (
            "ALIAS now points at Table 1. Q00 and Gram still disagree "
            "(kernel not born). Same-form pairing, not a take."
        ),
        "mu": MU,
        "rows": rows,
        "lexicographic_R": lex,
        "paired": all_ok,
    }


def main() -> int:
    data = run()
    out = os.path.join(os.path.dirname(HERE), "report", "maass-table1-pair.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"wrote {out} paired={data['paired']} verdict={data['verdict']}", flush=True)
    return 0 if data["paired"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
