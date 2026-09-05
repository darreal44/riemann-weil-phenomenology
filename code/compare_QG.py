#!/usr/bin/env python3
"""Q and Gram on the same cosine window.

    RETURN_S=1 python code/compare_QG.py chi29 11 24 40
"""
from __future__ import annotations

import math
import os
import pickle
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.environ["RETURN_S"] = "1"
from scan_s import assemble  # noqa: E402


def gram(name, mu, NB):
    path = os.path.join(HERE, f"zeros_{name}_weyl.pkl")
    z = np.array(sorted(float(x) for x in pickle.load(open(path, "rb"))))
    z = z[z > 1e-12]
    L = math.log(mu)
    om = np.array([2 * math.pi * n / L for n in range(NB + 1)])
    zz = z[(z > 1e-12) & (z < om[-1] * 1.1)]
    rows = []
    for g in zz:
        s = math.sin(g * L / 2)
        v = np.empty_like(om)
        v[0] = 2 * s / (g * math.sqrt(L))
        v[1:] = math.sqrt(2 / L) * s * 2 * g / (g * g - om[1:] ** 2)
        rows.append(v)
    G = 2 * np.array(rows).T @ np.array(rows)
    return G, len(zz)


def main():
    name, mu, NB, dps = sys.argv[1], float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    out = assemble(name, mu, NB, dps)
    lamQ, _, _, S = out
    Q = np.array([[float(S[i, j]) for j in range(NB + 1)] for i in range(NB + 1)])
    G, nz = gram(name, mu, NB)
    froQ = np.linalg.norm(Q, "fro")
    froD = np.linalg.norm(G - Q, "fro")
    evQ = np.sort(np.linalg.eigvalsh(Q))
    evG = np.sort(np.linalg.eigvalsh(G))
    print(
        f"[{name} mu={mu} N={NB+1}] nz={nz}  "
        f"lam0_Q={evQ[0]:.4e} lam0_G={evG[0]:.4e}  "
        f"G/Q={evG[0]/evQ[0] if evQ[0] else float('nan'):.3f}  "
        f"||G-Q||_F / ||Q||_F={froD/froQ:.3f}"
    )


if __name__ == "__main__":
    main()
