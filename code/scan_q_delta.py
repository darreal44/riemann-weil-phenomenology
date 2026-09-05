#!/usr/bin/env python3
"""Prime-side Q for Ramanujan Delta (weight 12).

s0 = 1/4 and 23/4  (Gamma_R(s) and Gamma_R(s+11)).
Prime weight tau(n) log p / n^6.

    python code/scan_q_delta.py 11 24 40
    python code/scan_q_delta.py 22 36 50

Needs no gp for n<=30 (table). gp mfcoefs if cap>30.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import time

import mpmath as mp
import numpy.polynomial.legendre as NL

# Ramanujan tau(n), n<=30
TAU = {
    1: 1, 2: -24, 3: 252, 4: -1472, 5: 4830, 6: -6048, 7: -16744,
    8: 84480, 9: -113643, 10: -115920, 11: 534612, 12: -370944,
    13: -577738, 14: 401856, 15: 1217160, 16: 987136, 17: -6905934,
    18: 2727432, 19: 10661420, 20: -7109760, 21: -4219488, 22: -12830688,
    23: 18643272, 24: 21288960, 25: -25499225, 26: 13857712, 27: -73279080,
    28: 24606720, 29: 128406630, 30: -29211840,
}


def tau_n(cap: int) -> dict[int, int]:
    if cap <= 30:
        return {n: t for n, t in TAU.items() if n <= cap}
    if not shutil.which("gp"):
        return {n: t for n, t in TAU.items() if n <= min(cap, 30)}
    script = f"""
default(realprecision, 19);
v = mfcoefs(mfDelta(), {cap});
for(i=1, #v, print(i, " ", v[i]));
"""
    proc = subprocess.run(
        ["gp", "-q", "--default", "parisizemax=512M"],
        input=script, text=True, capture_output=True,
    )
    out = {}
    for line in proc.stdout.splitlines():
        parts = line.split()
        if len(parts) != 2:
            continue
        try:
            out[int(parts[0])] = int(float(parts[1]))
        except ValueError:
            continue
    return out or {n: t for n, t in TAU.items() if n <= 30}


def assemble(mu, NB, dps, DEG=12):
    mp.mp.dps = dps
    t0 = time.time()
    L = mp.log(mp.mpf(mu))
    s0s = (mp.mpf(1) / 4, mp.mpf(23) / 4)
    om = [2 * mp.pi * n / L for n in range(NB + 1)]
    xr0, _ = NL.leggauss(DEG)
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
    NPANEL = 3 * NB + 12
    nodes, wts = [], []
    for p in range(NPANEL):
        aa, bb = L * p / NPANEL, L * (p + 1) / NPANEL
        h = (bb - aa) / 2
        for x, w in zip(xr, wr):
            nodes.append(aa + h * (x + 1))
            wts.append(w * h)
    K = len(nodes)
    SIN = [[mp.sin(om[n] * y) for y in nodes] for n in range(NB + 1)]
    COS = [[mp.cos(om[n] * y) for y in nodes] for n in range(NB + 1)]
    LY = [(L - y) / L for y in nodes]
    panels = []
    for s0 in s0s:
        D2 = [
            wts[k] * 2 * mp.e ** (-2 * s0 * nodes[k]) / (1 - mp.e ** (-2 * nodes[k]))
            for k in range(K)
        ]
        EC = [mp.e ** (-(2 - 2 * s0) * nodes[k]) for k in range(K)]
        CST = mp.log(1 / mp.pi) - mp.euler - mp.log(1 - mp.e ** (-2 * L))
        panels.append((D2, EC, CST))

    def th_nodes(n, m):
        if n == 0 and m == 0:
            return [2 * LY[k] for k in range(K)], mp.mpf(2)
        if n == 0 or m == 0:
            j = max(n, m)
            a2 = -2 / (mp.sqrt(2) * mp.pi * j)
            return [a2 * SIN[j][k] for k in range(K)], mp.mpf(0)
        if n == m:
            return [2 * (LY[k] * COS[n][k] - SIN[n][k] / (2 * mp.pi * n)) for k in range(K)], mp.mpf(2)
        a2 = 2 / (mp.pi * (m * m - n * n))
        return [a2 * (n * SIN[n][k] - m * SIN[m][k]) for k in range(K)], mp.mpf(0)

    def th_at(n, m, y):
        if n == 0 and m == 0:
            return 2 * (L - y) / L
        if n == 0 or m == 0:
            j = max(n, m)
            return -2 * mp.sin(om[j] * y) / (mp.sqrt(2) * mp.pi * j)
        if n == m:
            return 2 * ((L - y) * mp.cos(om[n] * y) / L - mp.sin(om[n] * y) / (2 * mp.pi * n))
        return 2 * (n * mp.sin(om[n] * y) - m * mp.sin(om[m] * y)) / (mp.pi * (m * m - n * n))

    cap = int(float(mp.e ** L) + 1e-9)
    an = tau_n(cap)
    small = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    ppts = []
    for n, a in an.items():
        if n < 2 or a == 0:
            continue
        y2, p = n, None
        for qq in small:
            if y2 % qq == 0:
                p = qq
                while y2 % qq == 0:
                    y2 //= qq
                break
        if p and y2 == 1:
            ppts.append((mp.log(n), mp.mpf(a) * mp.log(p) / (n ** 6)))

    S = mp.matrix(NB + 1)
    for n in range(NB + 1):
        for m in range(n, NB + 1):
            th, F0 = th_nodes(n, m)
            arch = mp.mpf(0)
            for D2, EC, CST in panels:
                arch += F0 / 2 * CST + mp.mpf("0.5") * mp.fsum(
                    D2[k] * (F0 * EC[k] - th[k]) for k in range(K)
                )
            v = arch - mp.fsum(w * th_at(n, m, lg) for lg, w in ppts)
            S[n, m] = v
            S[m, n] = v
    E, V = mp.eigsy(S)
    pairs = sorted([(E[i], i) for i in range(NB + 1)], key=lambda z: float(z[0]))
    lam = [p[0] for p in pairs[:8]]
    ell = [float(-mp.log(abs(l))) if l != 0 else float("inf") for l in lam]
    i0 = pairs[0][1]
    v0 = [float(V[n, i0]) for n in range(NB + 1)]
    p2 = [x * x for x in v0]
    s2 = sum(p2) or 1.0
    p2 = [x / s2 for x in p2]
    neff = 1.0 / sum(x * x for x in p2)
    ratio = float(abs(pairs[1][0] / pairs[0][0])) if pairs[0][0] != 0 else float("inf")
    print(
        f"[delta Q mu={mu} N={NB+1} dps={dps}] lam0={mp.nstr(lam[0],4)}  "
        f"ell={[round(x, 2) for x in ell[:6]]}  "
        f"N_eff={neff:.2f} l1/l0={ratio:.2e}  {time.time()-t0:.0f}s",
        flush=True,
    )
    return float(lam[0]), ell, neff


if __name__ == "__main__":
    mu, NB, dps = float(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    assemble(mu, NB, dps)
