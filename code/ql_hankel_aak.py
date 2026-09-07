#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Finite AAK / SVD of the Hilbert–Hankel tail section.

    H_{ij} = 1 / (n_i + n_j),   n = head, head+1, ..., head+N-1

Not a take of W_L. Atoms are outside this matrix.
The infinite-norm bound used in ql_schur_tail is π.
This script measures σ_max of a large section and the first
singular values (AAK numbers of the section).

    python code/ql_hankel_aak.py
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

PI = math.pi
HEADS = (2, 8, 16, 24)
SIZES = (32, 64, 128)


def hankel_section(head: int, n: int) -> np.ndarray:
    idx = np.arange(head, head + n, dtype=float)
    return 1.0 / (idx[:, None] + idx[None, :])


def spectrum(head: int, n: int) -> dict:
    H = hankel_section(head, n)
    sig = np.linalg.svd(H, compute_uv=False)
    return {
        "head": head,
        "n": n,
        "s0": float(sig[0]),
        "s1": float(sig[1]) if n > 1 else None,
        "s2": float(sig[2]) if n > 2 else None,
        "s0_over_pi": float(sig[0] / PI),
        "pi_minus_s0": float(PI - sig[0]),
    }


def main() -> None:
    rows = [spectrum(h, n) for h in HEADS for n in SIZES]
    print("head  N    σ0        σ1        σ2        σ0/π    π-σ0")
    for r in rows:
        print(
            f"{r['head']:4d} {r['n']:4d}  {r['s0']:.6f}  {r['s1']:.6f}  "
            f"{r['s2']:.6f}  {r['s0_over_pi']:.4f}  {r['pi_minus_s0']:.4f}"
        )
    # What the scripts use: 0.5*π + 1/(4 head)
    print()
    print("script hankel bound 0.5*π + 1/(4h):")
    for h in HEADS:
        b = 0.5 * PI + 1.0 / (4.0 * h)
        # comparable object is 0.5 * σ0_section + diag leftover
        s128 = next(r["s0"] for r in rows if r["head"] == h and r["n"] == 128)
        print(f"  h={h:2d}  bound={b:.4f}  0.5*σ0(128)={0.5*s128:.4f}  saved={b-0.5*s128:.4f}")
    out = os.path.join(os.path.dirname(__file__), "..", "report", "ql-hankel-aak.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        json.dump({"rows": rows}, f, indent=2)
    print("wrote", os.path.abspath(out))


if __name__ == "__main__":
    main()
