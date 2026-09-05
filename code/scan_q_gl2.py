#!/usr/bin/env python3
"""Prime-side Q for weight-2 newforms (elliptic curves).

Not scan_s: critical line Re=1, coefficients a_n, Gamma(s).
Archimedean is the first-order analogue of the even-Dirichlet
panel (two Gamma_R ~ Gamma(s)): treat as experimental.

    python code/scan_q_gl2.py 11a1 11 24 40
    python code/scan_q_gl2.py 11a1 22 36 50

Needs gp on PATH for a_n. 11a1 has a built-in table for n<=30
so a smoke runs without gp.
"""
from __future__ import annotations

import math
import os
import shutil
import subprocess
import sys
import time

import mpmath as mp
import numpy.polynomial.legendre as NL

CURVES = {
    "11a1": 11,
    "19a1": 19,
    "32a1": 32,
    "37a1": 37,
    "43a1": 43,
    "53a1": 53,
    "61a1": 61,
    "67a1": 67,
}

# a_p for 11a1 from L-factors (LMFDB 11.a). Not the old A11 table.
AP_11 = {
    2: -2, 3: -1, 5: 1, 7: -2, 11: 1, 13: 4, 17: -2, 19: 0, 23: -1,
    29: 0, 31: 7, 37: 3,
}


def hecke_an(ap: dict[int, int], Ncond: int, cap: int) -> dict[int, int]:
    an = {1: 1}
    primes = sorted(ap)
    for p in primes:
        if p > cap:
            continue
        a = [1, ap[p]]
        while True:
            k = len(a)
            pk = p ** k
            if pk > cap:
                break
            if Ncond % p == 0:
                a.append(ap[p] * a[-1])
            else:
                a.append(ap[p] * a[-1] - p * a[-2])
        for k, val in enumerate(a):
            if k == 0:
                continue
            an[p ** k] = val
    # multiplicative fill
    changed = True
    while changed:
        changed = False
        items = list(an.items())
        for n, an_n in items:
            for m, an_m in items:
                if math.gcd(n, m) == 1 and n * m <= cap and n * m not in an:
                    an[n * m] = an_n * an_m
                    changed = True
    return an


def ellan(label: str, cap: int) -> dict[int, int]:
    use_gp = os.environ.get("GL2_USE_GP", "0") == "1"
    if label == "11a1" and not use_gp:
        return hecke_an(AP_11, 11, cap)
    if not shutil.which("gp"):
        if label == "11a1":
            return hecke_an(AP_11, 11, cap)
        raise SystemExit("gp required for a_n")
    script = f"""
default(realprecision, 19);
E = ellinit("{label}");
v = ellan(E, {cap});
for(i=1, #v, print(i, " ", v[i]));
"""
    proc = subprocess.run(
        ["gp", "-q", "--default", "parisizemax=512M"],
        input=script, text=True, capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr[-400:])
    out = {}
    for line in proc.stdout.splitlines():
        parts = line.split()
        if len(parts) != 2:
            continue
        try:
            out[int(parts[0])] = int(float(parts[1]))
        except ValueError:
            continue
    return out


def assemble(name, mu, NB, dps, DEG=12):
    Ncond = CURVES[name]
    mp.mp.dps = dps
    t0 = time.time()
    L = mp.log(mp.mpf(mu))
    # Gamma_C(s) = Gamma_R(s) Gamma_R(s+1): both Dirichlet panels.
    s0s = (mp.mpf(1) / 4, mp.mpf(3) / 4)
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
        ncut = int(os.environ.get("GL2_NCUT", "2"))
        cut = mp.log(1 - mp.e ** (-2 * L)) if ncut > 0 else mp.mpf(0)
        # ncut=2: one cutoff per Gamma_R (old). ncut=1: once. ncut=0: drop.
        CST = mp.log(mp.mpf(Ncond) / mp.pi) - mp.euler
        if ncut >= 2:
            CST -= cut
        elif ncut == 1 and s0 == s0s[0]:
            CST -= cut
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

    cap_mul = float(os.environ.get("GL2_CAP_MUL", "1"))
    cap = int(float(mp.e ** L) * cap_mul + 1e-9)
    an = ellan(name, cap)
    print(f"  cap={cap} ncut={os.environ.get('GL2_NCUT','2')} n_an={len(an)}", flush=True)
    small = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
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
            # Re=1: a_n log p / n
            ppts.append((mp.log(n), mp.mpf(a) * mp.log(p) / n))

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
    kbar = sum(k * p2[k] for k in range(NB + 1))
    ratio = float(abs(pairs[1][0] / pairs[0][0])) if pairs[0][0] != 0 else float("inf")
    print(
        f"[{name} Q mu={mu} N={NB+1} dps={dps}] lam0={mp.nstr(lam[0],4)}  "
        f"ell={[round(x, 2) for x in ell[:6]]}  "
        f"N_eff={neff:.2f} kbar={kbar:.2f} l1/l0={ratio:.2e}  "
        f"{time.time()-t0:.0f}s",
        flush=True,
    )
    return float(lam[0]), ell


if __name__ == "__main__":
    name = sys.argv[1]
    if name not in CURVES:
        sys.exit(f"unknown {name}")
    mu, NB, dps = float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    assemble(name, mu, NB, dps)
