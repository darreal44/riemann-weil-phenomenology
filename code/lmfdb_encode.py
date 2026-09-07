#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Re-encode LMFDB Maass CSVs as slim pickles for the scanners.

    python code/lmfdb_encode.py

Writes code/lmfdb_maass_gl2.pkl and code/lmfdb_maass_gl3.pkl.
CSV stays local (gitignored). Scanners load the pkl. Not Weil.

Cite: The LMFDB Collaboration, https://www.lmfdb.org, 2026,
[Online; accessed 7 September 2026]. notes/lmfdb.bib.
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


def load_gl2() -> list[dict]:
    with open(GL2_PKL, "rb") as f:
        return pickle.load(f)["rows"]


def load_gl3() -> list[dict]:
    with open(GL3_PKL, "rb") as f:
        return pickle.load(f)["rows"]


def by_label_gl2() -> dict[str, dict]:
    return {r["label"]: r for r in load_gl2()}


def load_dirichlet() -> list[dict]:
    path = os.path.join(HERE, "lmfdb_dirichlet.pkl")
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
    encode()
