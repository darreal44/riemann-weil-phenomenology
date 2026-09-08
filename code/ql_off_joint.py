#!/usr/bin/env python3
"""Finite-section ||Off|| vs triangle. Not a majorant. Not RH."""
from __future__ import annotations
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ql_schur_neumann import Q
from ql_schur_tail import theta_hat, LOG2
from ql_operator_bound import CHARS, w2_of
from ql_off_s1 import s1_off_q_upper

def pack(n0: int, n1: int, name: str = "chi3"):
    w2 = w2_of(CHARS[name]["d"])
    dim = n1 - n0
    Off = np.zeros((dim, dim))
    H = np.zeros((dim, dim))
    Th = np.zeros((dim, dim))
    for i, n in enumerate(range(n0, n1)):
        for j, m in enumerate(range(n0, n1)):
            if i == j:
                continue
            Off[i, j] = Q(name, n, m)
            H[i, j] = 0.5 / (n + m)
            Th[i, j] = theta_hat(n, m, LOG2)
    def nrm(A):
        return float(np.linalg.norm(A, 2)), float(np.max(np.sum(np.abs(A), axis=1)))
    o2, oinf = nrm(Off)
    h2, _ = nrm(H)
    t2, _ = nrm(Th)
    return {"n0": n0, "n1": n1, "off2": o2, "row": oinf, "H2": h2, "Th2": t2,
            "tri_sec": h2 + abs(w2) * t2}

def main() -> int:
    w2 = w2_of(CHARS["chi3"]["d"])
    print(f"chi3 w2={w2:.3f} s1_up={s1_off_q_upper(32,w2):.4f} need<1.72")
    for n0, n1 in ((32, 48), (32, 64), (32, 96)):
        r = pack(n0, n1)
        print(f"[{n0},{n1}) Off2={r['off2']:.4f} row={r['row']:.4f} "
              f"tri_sec={r['tri_sec']:.4f} Th2={r['Th2']:.3f}")
    print("row-sum already >1.72 on finite pieces -> not a majorant")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
