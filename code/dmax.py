#!/usr/bin/env python3
"""Discrete Landau count on a finite cosine window.

    D_max = max_γ (γ L/2π − N_Γ(γ))

taken over in-band zeros and the band edge ω_max = 2π NB / L.
n(ω) = #{hats with 2π n/L < ω}. Linear algebra: dim ker Eval_ω ≥ n(ω) − N_Γ(ω).

    python code/dmax.py              # table for the edge-value windows
    python code/dmax.py zeta 11 40
"""
from __future__ import annotations

import json
import math
import os
import pickle
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

WINDOWS = (
    ("zeta:11", "zeros500.pkl"),
    ("zeta:16", "zeros_zeta_weyl.pkl"),
    ("chi3:16", "zeros_chi3_weyl.pkl"),
    ("chi3:38", "zeros_chi3_weyl.pkl"),
    ("chi4:16", "zeros_chi4_weyl.pkl"),
    ("chi4:38", "zeros_chi4_weyl.pkl"),
    ("chi5:16", "zeros_chi5_weyl.pkl"),
    ("chi5:38", "zeros_chi5_weyl.pkl"),
    ("chi8:16", "zeros_chi8_weyl.pkl"),
    ("chi13:16", "zeros_chi13_weyl.pkl"),
    ("chi29:38", "zeros_chi29_weyl.pkl"),
    ("chi31:38", "zeros_chi31_weyl.pkl"),
)


def load_zeros(fname: str) -> list[float]:
    path = fname if os.path.isabs(fname) else os.path.join(HERE, fname)
    return sorted(float(str(x)) for x in pickle.load(open(path, "rb")))


def n_hats(omega: float, L: float, NB: int) -> int:
    """Hats η_n, n=0..NB, with frequency 2π n/L strictly below omega."""
    return sum(1 for n in range(NB + 1) if 2 * math.pi * n / L < omega)


def D_max(zeros: list[float], mu: float, NB: int) -> float:
    L = math.log(mu)
    nyq = L / (2 * math.pi)
    omax = 2 * math.pi * NB / L
    inb = [g for g in zeros if g < omax]
    cands = [g * nyq - (k + 1) for k, g in enumerate(inb)]
    cands.append(omax * nyq - len(inb))
    return max(cands)


def kernel_lower(zeros: list[float], mu: float, NB: int, omega: float) -> int:
    """dim ker Eval_ω ≥ n(ω) − #{γ < ω}, clipped to [0, n]."""
    L = math.log(mu)
    n = n_hats(omega, L, NB)
    m = sum(1 for g in zeros if g < omega)
    return max(0, n - m)


def D_max_kernel(zeros: list[float], mu: float, NB: int) -> int:
    """Integer lower bound: max_ω (n(ω) − N_Γ(ω))."""
    L = math.log(mu)
    omax = 2 * math.pi * NB / L
    cuts = [g for g in zeros if g < omax] + [omax]
    return max(kernel_lower(zeros, mu, NB, w) for w in cuts)


def gram_ells(zeros, mu, NB):
    """Depths −ln λ_k of the truncated zero Gram (positive eigenvalues)."""
    L = math.log(mu)
    om = np.array([2 * math.pi * n / L for n in range(NB + 1)])
    zz = [g for g in zeros if 0 < g < om[-1] * 1.1]
    if not zz:
        return np.array([])
    rows = []
    sL = math.sqrt(L)
    for g in zz:
        s = math.sin(g * L / 2)
        v = np.empty_like(om)
        v[0] = 2 * s / (g * sL)
        v[1:] = math.sqrt(2 / L) * s * 2 * g / (g * g - om[1:] ** 2)
        rows.append(v)
    Ph = np.array(rows)
    ev = np.linalg.eigvalsh(2 * Ph.T @ Ph)
    pos = ev[ev > 0]
    return np.array([-math.log(x) for x in pos])  # ells[0] = −ln λ_min


def count_above(ells, thresh):
    return int(sum(1 for e in ells if e > thresh))


def main() -> None:
    if len(sys.argv) >= 4:
        name, mu, NB = sys.argv[1], float(sys.argv[2]), int(sys.argv[3])
        zf = f"zeros_{name}_weyl.pkl" if name != "zeta" else "zeros500.pkl"
        Z = load_zeros(zf)
        D = D_max(Z, mu, NB)
        K = D_max_kernel(Z, mu, NB)
        print(f"{name} μ={mu} NB={NB}  D_max={D:.4f}  ker≥{K}  π² D={math.pi**2 * D:.2f}  11 D={11 * D:.2f}")
        return
    rows = {}
    path = os.path.join(ROOT, "report", "edge-value-scan.jsonl")
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            if line.strip():
                r = json.loads(line)
                rows[r["window"]] = r
    pi2 = math.pi**2
    print(f"{'window':14s} {'D_max':7s} {'ker≥':5s} {'ell':8s} {'ell/D':7s} {'π²D':8s} {'11D':8s}")
    for w, zf in WINDOWS:
        r = rows.get(w, {})
        mu = float(r.get("mu", w.split(":")[1]))
        NB = int(r.get("NB", 40))
        Z = load_zeros(zf)
        D = D_max(Z, mu, NB)
        K = D_max_kernel(Z, mu, NB)
        ell = r.get("ell")
        elD = f"{ell / D:7.3f}" if ell else "   —  "
        elS = f"{ell:8.2f}" if ell else "     — "
        print(f"{w:14s} {D:7.3f} {K:5d} {elS} {elD} {pi2 * D:8.2f} {11 * D:8.2f}")


if __name__ == "__main__":
    main()
