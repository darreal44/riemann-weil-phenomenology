#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Finite-section s1 of the true Q tail (chi3). Not a proof.

    python code/ql_tail_s1.py
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_schur_neumann import Q  # noqa: E402


def section(n0: int, n1: int) -> dict:
    dim = n1 - n0
    T = np.zeros((dim, dim))
    for i, n in enumerate(range(n0, n1)):
        for j, m in enumerate(range(n0, n1)):
            T[i, j] = Q("chi3", n, m)
    d = np.diag(T)
    off = T - np.diag(d)
    a = off * np.outer(1.0 / np.sqrt(d), 1.0 / np.sqrt(d))
    return {
        "n0": n0,
        "n1": n1,
        "qmin": float(d.min()),
        "off_s1": float(np.linalg.norm(off, 2)),
        "A_s1": float(np.linalg.norm(a, 2)),
        "half_pi": 0.5 * math.pi,
    }


def main() -> int:
    for n0, n1 in ((32, 48),):
        r = section(n0, n1)
        print(
            f"[{r['n0']},{r['n1']})  ||Off||={r['off_s1']:.3f}  "
            f"||A||={r['A_s1']:.3f}  qmin={r['qmin']:.3f}  "
            f"½π={r['half_pi']:.3f}",
            flush=True,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
