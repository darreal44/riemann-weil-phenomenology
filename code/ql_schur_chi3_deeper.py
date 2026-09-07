#!/usr/bin/env python3
# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
"""Deeper near block for chi3. Hilbert constant unchanged.

    python code/ql_schur_chi3_deeper.py
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ql_schur_neumann as neu


def main() -> int:
    for n_near, m_c in ((32, 40), (40, 52), (48, 60)):
        neu.N_NEAR = n_near
        neu.M_C = m_c
        neu._cache.clear()
        r = neu.row_of("chi3")
        slo = r["s_lo"]
        print(
            f"N_NEAR={n_near:2d} M_C={m_c:2d}  "
            f"ρ={r['rho']:.3f} (N={r['rho_near']:.3f} B={r['rho_B']:.3f} "
            f"far={r['rho_far']:.3f})  Sdiag={r['s_diag']:+.4f}  "
            f"Slo={slo:+.4f}" if slo is not None else "Slo=None",
            flush=True,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
