#!/usr/bin/env python3
"""Q00 vs G00 for Maass, three s0 conventions × two prime weights.

    python code/calibrate_maass_q.py
"""
from __future__ import annotations

import json
import math
import os
import pickle

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss

HERE = os.path.dirname(os.path.abspath(__file__))


def G00(zeros_pkl, mu):
    L = math.log(mu)
    z = np.array(sorted(float(x) for x in pickle.load(open(zeros_pkl, "rb"))))
    z = z[z > 1e-12]
    s = np.sin(z * L / 2)
    phi = 2 * s / (z * math.sqrt(L))
    return float(2 * phi @ phi)


def arch00(mu, R, Ncond, kind, dps=20, DEG=12, NB=8):
    mp.mp.dps = dps
    L = mp.log(mp.mpf(mu))
    if kind == "halfR":
        s0s = (mp.mpf("0.5") + 1j * mp.mpf(R), mp.mpf("0.5") - 1j * mp.mpf(R))
    elif kind == "quarter":
        s0s = (mp.mpf("0.25") + 1j * mp.mpf(R) / 2, mp.mpf("0.25") - 1j * mp.mpf(R) / 2)
    else:
        s0s = (mp.mpf("0.5"), mp.mpf(1))
    xr0, _ = leggauss(DEG)
    xr, wr = [], []
    for x0 in xr0:
        x = mp.mpf(float(x0))
        for _ in range(5):
            P = mp.legendre(DEG, x)
            Pm = mp.legendre(DEG - 1, x)
            dP = DEG * (x * P - Pm) / (x * x - 1)
            x = x - P / dP
        P = mp.legendre(DEG, x)
        Pm = mp.legendre(DEG - 1, x)
        dP = DEG * (x * P - Pm) / (x * x - 1)
        xr.append(x)
        wr.append(2 / ((1 - x * x) * dP * dP))
    NP = 3 * NB + 12
    nodes, wts = [], []
    for p in range(NP):
        aa, bb = L * p / NP, L * (p + 1) / NP
        h = (bb - aa) / 2
        for x, w in zip(xr, wr):
            nodes.append(aa + h * (x + 1))
            wts.append(w * h)
    K = len(nodes)
    th = [2 * (L - y) / L for y in nodes]
    F0 = mp.mpf(2)
    cut = mp.log(1 - mp.e ** (-2 * L))
    CST = mp.log(mp.mpf(Ncond)) / 2 - mp.log(mp.pi) - mp.euler - cut
    arch = mp.mpf(0)
    for s0 in s0s:
        D2 = [wts[k] * 2 * mp.e ** (-2 * s0 * nodes[k]) / (1 - mp.e ** (-2 * nodes[k])) for k in range(K)]
        EC = [mp.e ** (-(2 - 2 * s0) * nodes[k]) for k in range(K)]
        arch += F0 / 2 * CST + mp.mpf("0.5") * mp.fsum(D2[k] * (F0 * EC[k] - th[k]) for k in range(K))
    return float(mp.re(arch))


def prim00(an, mu, exp):
    L = math.log(mu)
    cap = int(math.exp(L) + 1e-9)
    s = 0.0
    for n, a in an.items():
        if n < 2 or n > cap:
            continue
        p = None
        for q in range(2, int(n**0.5) + 1):
            if n % q == 0:
                p = q
                break
        if p is None:
            p = n
        m = n
        while m % p == 0:
            m //= p
        if m != 1:
            continue
        th = 2 * (L - math.log(n)) / L
        s += (a * math.log(p) / (n**exp)) * th
    return s


def main():
    rec = json.load(open(os.path.join(HERE, "maass_an_1.0.1.1.1.json")))
    an = {i + 1: float(a) for i, a in enumerate(rec["a_n"])}
    R, Ncond = rec["R"], rec["N"]
    mu = 6.0
    G = G00(os.path.join(HERE, "zeros_maass1_weyl.pkl"), mu)
    print(f"maass1 mu={mu} G00={G:.4f}")
    print(f"{'s0':>10} {'exp':>4} {'arch':>8} {'prim':>8} {'Q00':>8}")
    for kind in ("halfR", "quarter", "gl2"):
        a = arch00(mu, R, Ncond, kind)
        for exp in (0.5, 1.0):
            p = prim00(an, mu, exp)
            print(f"{kind:>10} {exp:4.1f} {a:8.3f} {p:8.3f} {a-p:8.3f}")


if __name__ == "__main__":
    main()
