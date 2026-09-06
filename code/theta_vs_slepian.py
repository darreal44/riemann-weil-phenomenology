#!/usr/bin/env python3
"""Θ_v (prime-side Q) versus autocorrelation of the desert Slepian.

    python3 code/theta_vs_slepian.py
"""
from __future__ import annotations

import math
import time

import mpmath as mp
import numpy as np

mp.mp.dps = 25
Lm = mp.log(11)
L = float(Lm)
G1 = 14.134725141734695
NP = 9
om = [2 * mp.pi * n / Lm for n in range(NP)]
CR = mp.euler + mp.log(4 * mp.pi * (mp.e**Lm - 1) / (mp.e**Lm + 1))


def theta(n, m, y):
    if n == 0 and m == 0:
        return 2 * (Lm - y) / Lm
    if n == 0 or m == 0:
        j = max(n, m)
        return -2 * mp.sin(om[j] * y) / (mp.sqrt(2) * mp.pi * j)
    if n == m:
        return 2 * ((Lm - y) * mp.cos(om[n] * y) / Lm - mp.sin(om[n] * y) / (2 * mp.pi * n))
    return 2 * (n * mp.sin(om[n] * y) - m * mp.sin(om[m] * y)) / (mp.pi * (m * m - n * n))


def q_vector():
    towers = []
    for p in (2, 3, 5, 7):
        k = 1
        while p**k <= 11:
            towers.append((mp.log(p**k), mp.log(p) / mp.sqrt(p**k)))
            k += 1
    Q = mp.matrix(NP)
    for n in range(NP):
        for m in range(n, NP):
            F0 = mp.mpf(2) if n == m else mp.mpf(0)
            pol = mp.quad(lambda y: theta(n, m, y) * (mp.e ** (y / 2) + mp.e ** (-y / 2)), [0, Lm])
            ig = mp.quad(
                lambda y: (mp.e ** (y / 2) * theta(n, m, y) - F0) / (mp.e**y - mp.e ** (-y)),
                [0, Lm],
            )
            tw = mp.fsum(w * theta(n, m, lg) for lg, w in towers)
            Q[n, m] = Q[m, n] = pol - (F0 / 2 * CR + ig) - tw
    ev = mp.eigsy(Q, eigvals_only=False)
    lams = [float(ev[0][i]) for i in range(NP)]
    idx = int(np.argmin(lams))
    v = np.array([float(ev[1][i, idx]) for i in range(NP)])
    return v if v[0] >= 0 else -v


def slepian_auto():
    M = 240
    t = np.linspace(0.0, L, M)
    dt = t[1] - t[0]
    W = np.sinc(G1 * (t[:, None] - t[None, :]) / math.pi) * (G1 / math.pi) * dt
    ew, U = np.linalg.eigh(W)
    psi = U[:, -1]
    if psi[len(psi) // 4] < 0:
        psi = -psi
    psi = psi / np.linalg.norm(psi)

    def auto(y):
        k = int(round(y / dt))
        if k >= M:
            return 0.0
        return float(psi[: M - k] @ psi[k:]) * dt

    return auto, float(ew[-1])


if __name__ == "__main__":
    t0 = time.time()
    v = q_vector()
    auto, conc = slepian_auto()
    print(f"Slepian concentration {conc:.6f}  ({time.time()-t0:.0f}s)")
    print(f"{'y':>6} {'Θ_Q':>11} {'Θ_Sl':>11} {'rQ':>7} {'rS':>7}")
    for y in np.linspace(0.2, L * 0.9, 12):
        tq = sum(v[n] * v[m] * float(theta(n, m, mp.mpf(float(y)))) for n in range(NP) for m in range(NP))
        ts = auto(y)
        yey = y * math.exp(y)
        rq = -math.log(tq) / yey if tq > 0 else float("nan")
        rs = -math.log(ts) / yey if ts > 0 else float("nan")
        print(f"{y:6.3f} {tq:11.3e} {ts:11.3e} {rq:7.3f} {rs:7.3f}")
