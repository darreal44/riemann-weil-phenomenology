#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""One catalog for GL2 Maass rigor, for scanners and other code.

    from lmfdb_encode import by_label_gl2, load_zeros, load_an, load_lfunc
    rec = by_label_gl2()["1.0.1.1.1"]
    rec["R"], rec["zeros"], rec["lfunc"]["z1"]
    load_zeros("maass1")
    load_lfunc("11.0.1.1.1")   # L-search columns, reconstructed
    load_an("11.0.1.1.1")      # 1000 a_n from replica

L-search columns on rec["lfunc"] (same names as LMFDB /L/ table):
  alpha, A, d, N, chi, mu, nu, w, prim, arith, rational,
  self_dual, arg_eps, r, z1, origin
GL2 rigor L-functions are not stored in lfunc_search (0 rows at
N=1 and N=11, degree 2, w=0). Completeness: 15659 *dynamic* GL2
Maass L. Columns are rebuilt from maass_rigor; A is the LMFDB
analytic conductor (verified on GL3 CSV). z1 from Booker–Then
Table 1 when we have zeros. Not Weil.

    python code/lmfdb_encode.py --reconcile
"""
from __future__ import annotations

import os
import pickle
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
GL2_PKL = os.path.join(HERE, "lmfdb_maass_gl2.pkl")
GL3_PKL = os.path.join(HERE, "lmfdb_maass_gl3.pkl")
CITE = {
    "source": "LMFDB",
    "url": "https://www.lmfdb.org",
    "year": 2026,
    "accessed": "2026-09-07",
    "gl2": "https://www.lmfdb.org/ModularForm/GL2/Q/Maass/",
    "gl3": "https://www.lmfdb.org/L/",
}


def encode() -> None:
    sys.path.insert(0, HERE)
    import lmfdb_maass_catalog as gl2
    import lmfdb_maass_gl3_catalog as gl3

    rows2 = []
    for r in gl2.load_csv():
        rows2.append(
            {
                "label": r["label"],
                "N": r["N"],
                "weight": r["weight"],
                "degree": r.get("degree", 2),
                "character": r["character"],
                "R": r["R"],
                "symmetry": r["symmetry"],
                "fricke": r["fricke"],
            }
        )
    blob2 = {"cite": CITE, "kind": "gl2_maass_rigor", "n": len(rows2), "rows": rows2}
    with open(GL2_PKL, "wb") as f:
        pickle.dump(blob2, f, protocol=4)
    print(f"gl2 n={len(rows2)} -> {GL2_PKL} ({os.path.getsize(GL2_PKL)} bytes)", flush=True)

    rows3 = []
    for r in gl3.load_csv():
        rows3.append(
            {
                "label": r["label"],
                "N": r["N"],
                "degree": r.get("degree", 3),
                "mu": r["mu"],
                "z1": r["z1"],
                "origin": r["origin"],
                "self_dual": r["self_dual"],
                "primitive": r["primitive"],
            }
        )
    blob3 = {"cite": CITE, "kind": "gl3_lfunc_search", "n": len(rows3), "rows": rows3}
    with open(GL3_PKL, "wb") as f:
        pickle.dump(blob3, f, protocol=4)
    print(f"gl3 n={len(rows3)} -> {GL3_PKL} ({os.path.getsize(GL3_PKL)} bytes)", flush=True)


# LMFDB /L/ table: Label, α, A, d, N, χ, μ, ν, w, prim, arith, ℚ,
# self-dual, Arg(ε), r, First zero, Origin.
LFUNC_COLUMNS = (
    "label", "alpha", "A", "d", "N", "chi", "mu", "nu", "w",
    "prim", "arith", "rational", "self_dual", "arg_eps", "r", "z1", "origin",
)
ARBITRAGE = [
    {
        "topic": "GL2 rigor L-functions not in lfunc_search",
        "lfunc_search": "0 rows for degree=2, motivic_weight=0, conductor 1 and 11",
        "lfunc_lfunctions": "origin ModularForm/GL2/Q/Maass/ empty; type=MaassGL2 is two N=101 leftovers",
        "lmfdb_completeness": "15659 dynamically computed GL2 Maass L (not stored)",
        "lmfdb_page_11.0.1.1.1": "L-function not computed",
        "action": "reconstruct L-search columns from maass_rigor; z1 from Booker–Then Table 1 when present",
    },
    {
        "topic": "analytic conductor A and alpha",
        "formula": "A = N exp(2 Re L_inf'(1/2)/L_inf(1/2)), alpha = A^(1/d), L_inf = product Gamma_R(s+mu)",
        "verified_on": "GL3 first CSV row A=0.048865567236632115, alpha=0.3655956178456336",
    },
    {
        "topic": "Arg(epsilon)",
        "action": "self-dual: root_angle 0 if Fricke=+1 else 1/2 (units of 2π). Not stored by LMFDB for these forms.",
    },
]


def analytic_conductor_gammaR(N: int, mus: list[tuple[float, float]]) -> float:
    """LMFDB A for Gamma_R factors. mus are (real, imag) shifts."""
    import mpmath as mp

    def dlog_gr(z):
        return -mp.log(mp.pi) / 2 + mp.digamma(z / 2) / 2

    s = mp.mpf("0.5")
    tot = sum(dlog_gr(s + a + 1j * b) for a, b in mus)
    return float(N * mp.exp(2 * mp.re(tot)))


def lfunc_from_rigor(r: dict, zeros) -> dict:
    """L-search row rebuilt from maass_rigor. stored_in_lmfdb is False."""
    even = int(r.get("symmetry") or 0) > 0
    R = float(r["R"])
    N = int(r["N"])
    if even:
        mu = [(0.0, R), (0.0, -R)]
    else:
        mu = [(1.0, R), (1.0, -R)]
    A = analytic_conductor_gammaR(N, mu)
    z1 = float(zeros[0]) if zeros is not None and getattr(zeros, "size", len(zeros)) else None
    fr = r.get("fricke")
    arg_eps = None if fr is None else (0.0 if int(fr) > 0 else 0.5)
    src = "reconstructed from maass_rigor"
    if z1 is not None:
        src += "; z1 from booker-then-table1"
    return {
        "label": None,
        "alpha": A ** 0.5,
        "A": A,
        "d": 2,
        "N": N,
        "chi": r["character"],
        "mu": mu,
        "nu": [],
        "w": 0,
        "prim": True,
        "arith": False,
        "rational": False,
        "self_dual": True,
        "arg_eps": arg_eps,
        "r": 0 if z1 is not None else None,
        "z1": z1,
        "origin": f"ModularForm/GL2/Q/Maass/{r['label']}",
        "stored_in_lmfdb": False,
        "source": src,
    }


def attach_zeros_lfunc(rows: list[dict]) -> None:
    """Table 1 γ + reconstructed L-search columns on every rigor row."""
    from maass_table1 import ALIAS

    have: dict[str, tuple[str, np.ndarray]] = {}
    for name, lab in ALIAS.items():
        path = os.path.join(HERE, f"zeros_{name}_weyl.pkl")
        if not os.path.exists(path):
            continue
        z = np.array(
            sorted(float(x) for x in pickle.load(open(path, "rb"))),
            dtype=np.float64,
        )
        have[lab] = ("booker-then-table1", z)
    for r in rows:
        lab = r["label"]
        if lab in have:
            src, z = have[lab]
            r["zeros"] = z
            r["zeros_source"] = src
        else:
            r["zeros"] = np.zeros(0, dtype=np.float64)
            r["zeros_source"] = None
        r["lfunc"] = lfunc_from_rigor(r, r["zeros"])
        r["lfunc_note"] = r["lfunc"]["source"]


def reconcile_gl2() -> None:
    with open(GL2_PKL, "rb") as f:
        blob = pickle.load(f)
    attach_zeros_lfunc(blob["rows"])
    blob["kind"] = "gl2_maass_rigor"
    blob["lfunc_columns"] = ",".join(LFUNC_COLUMNS)
    blob["arbitrage"] = ARBITRAGE
    with open(GL2_PKL, "wb") as f:
        pickle.dump(blob, f, protocol=4)
    n_z = sum(1 for r in blob["rows"] if r["zeros"].size)
    print(
        f"reconcile {GL2_PKL} n={blob['n']} with_zeros={n_z} "
        f"{os.path.getsize(GL2_PKL)} bytes",
        flush=True,
    )


def load_gl2() -> list[dict]:
    with open(GL2_PKL, "rb") as f:
        return pickle.load(f)["rows"]


def load_gl3() -> list[dict]:
    with open(GL3_PKL, "rb") as f:
        return pickle.load(f)["rows"]


def by_label_gl2() -> dict[str, dict]:
    return {r["label"]: r for r in load_gl2()}


def load_zeros(label: str):
    """γ > 0 for one rigor form. Empty if we have no list.

    Accepts maass1, 1.2, 1.0.1.1.1.
    """
    from maass_table1 import resolve

    rec = by_label_gl2()[resolve(label)]
    z = rec.get("zeros")
    if z is None:
        return np.zeros(0, dtype=np.float64)
    return np.asarray(z, dtype=np.float64)


def load_lfunc(label: str) -> dict:
    """L-search columns for one rigor form (reconstructed if not stored)."""
    from maass_table1 import resolve

    rec = by_label_gl2()[resolve(label)]
    lf = rec.get("lfunc")
    if lf is None:
        return lfunc_from_rigor(rec, rec.get("zeros"))
    return lf


def load_dirichlet() -> list[dict]:
    path = os.path.join(HERE, "lmfdb_dirichlet.pkl")
    with open(path, "rb") as f:
        return pickle.load(f)["rows"]


def load_lfunc_maass() -> list[dict]:
    path = os.path.join(HERE, "lmfdb_lfunc_maass.pkl")
    with open(path, "rb") as f:
        return pickle.load(f)["rows"]


def load_lfunc_dirichlet() -> list[dict]:
    path = os.path.join(HERE, "lmfdb_lfunc_dirichlet.pkl")
    with open(path, "rb") as f:
        return pickle.load(f)["rows"]


def load_lfunc_cmf() -> list[dict]:
    path = os.path.join(HERE, "lmfdb_lfunc_cmf.pkl")
    with open(path, "rb") as f:
        return pickle.load(f)["rows"]


def load_mf_newforms() -> list[dict]:
    path = os.path.join(HERE, "lmfdb_mf_newforms.pkl")
    with open(path, "rb") as f:
        return pickle.load(f)["rows"]


_AN = None


def load_an(label: str | None = None):
    """All rigor a_n (every level). Prefers local sqlite, else N-shards."""
    global _AN
    if _AN is None:
        _AN = {}
        sqlite = os.path.join(ROOT, "data", "lmfdb_mirror.sqlite")
        if os.path.exists(sqlite):
            import sqlite3

            db = sqlite3.connect(sqlite)
            for lab, blob in db.execute("SELECT maass_label, coeffs FROM maass_an"):
                _AN[lab] = np.frombuffer(blob, dtype=np.float32).copy()
            db.close()
        else:
            import glob

            for path in sorted(glob.glob(os.path.join(HERE, "lmfdb_maass_an_N*.pkl"))):
                blob = pickle.load(open(path, "rb"))
                _AN.update(blob["an"])
    if label is None:
        return _AN
    return _AN[label]


if __name__ == "__main__":
    if "--reconcile" in sys.argv:
        reconcile_gl2()
    else:
        encode()
        reconcile_gl2()
