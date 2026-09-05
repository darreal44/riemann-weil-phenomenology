#!/usr/bin/env python3
"""T of a zeros list, and Hecke T_p = a_p.

    python code/compute_T.py zeros_11a1_weyl.pkl
    python code/compute_T.py zeros_11a1_weyl.pkl --hecke 11a1 40

T_p on v0 is not implemented: T_p acts on S_k, not on the
cosine window.
"""
from __future__ import annotations

import math
import os
import pickle
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def load_zeros(path):
    if not os.path.exists(path):
        path = os.path.join(HERE, path)
    z = sorted(float(x) for x in pickle.load(open(path, "rb")))
    return [t for t in z if t > 1e-12]


def weyl_dirichlet(T, q=1):
    if T <= 0:
        return 0.0
    return (T / math.pi) * math.log(max(q * T / (2 * math.pi), 2.0))


def weyl_gl2(T, N):
    if T <= 0:
        return 0.0
    return (T / math.pi) * math.log(max(T * math.sqrt(N) / (2 * math.pi), 2.0)) - T / math.pi


def hecke_11(cap):
    sys.path.insert(0, HERE)
    from scan_q_gl2 import AP_11, hecke_an
    return hecke_an(AP_11, 11, cap)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    path = sys.argv[1]
    z = load_zeros(path)
    T = z[-1] if z else 0.0
    print(f"n={len(z)}  T={T:.6f}  g1={z[0] if z else float('nan'):.6f}")
    name = os.path.basename(path)
    if "a1" in name or "sym2" in name:
        N = 11
        for tok in ("67", "61", "53", "43", "37", "32", "19", "11"):
            if tok in name:
                N = int(tok)
                break
        W = weyl_gl2(T, N)
        tag = f"GL2 N={N}"
    else:
        W = weyl_dirichlet(T, 1)
        tag = "GL1"
    print(f"  Weyl {tag:12s} {W:.1f}  ratio={len(z)/max(W,1):.3f}")
    if "--hecke" in sys.argv:
        i = sys.argv.index("--hecke")
        label = sys.argv[i + 1] if i + 1 < len(sys.argv) else "11a1"
        cap = int(sys.argv[i + 2]) if i + 2 < len(sys.argv) else 40
        if label != "11a1":
            sys.exit("hecke table only for 11a1")
        an = hecke_11(cap)
        print(f"T_p = a_p for 11a1, p<={cap}:")
        for p in sorted(p for p in an if p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)):
            print(f"  T_{p} ↦ {an[p]}")


if __name__ == "__main__":
    main()
