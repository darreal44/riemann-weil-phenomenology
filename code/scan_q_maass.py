#!/usr/bin/env python3
"""Prime-side Q for even Maass newforms (weight 0).

Not scan_q_gl2: that path is Gamma_R(s) Gamma_R(s+1) on Re s = 1
with Satake alpha*beta = p. Maass is

    Gamma_R(s + iR) Gamma_R(s - iR)    on Re s = 1/2
    alpha + beta = a_p,  alpha*beta = 1.

Coefficients from Zenodo JSONs written by harvest_maass_zenodo.py.

    python code/scan_q_maass.py maass1 6 12 25
    python code/scan_q_maass.py 1.0.1.1.1 6 12 25

Experimental: the archimedean kernel is the GL2 panel with
complex s0 = 1/4 ± i R/2, summed as a conjugate pair (real Q).
This is a code path, not a covering lemma.
"""
from __future__ import annotations

import json
import math
import os
import sys
import time

import mpmath as mp
import numpy.polynomial.legendre as NL

HERE = os.path.dirname(os.path.abspath(__file__))

# short names -> zenodo slugs already in the tree
ALIAS = {
    "maass1": "1.0.1.1.1",
    "maass2": "1.0.1.10.1",
    "maass3": "1.0.1.100.1",
}


def load_form(name: str) -> dict:
    slug = ALIAS.get(name, name)
    path = os.path.join(HERE, f"maass_an_{slug}.json")
    rec = json.load(open(path))
    rec["slug"] = slug
    rec["an"] = {i + 1: float(a) for i, a in enumerate(rec["a_n"])}
    return rec


def lambda_pts(an: dict[int, float], cap: int, Ncond: int):
    """Hecke Lambda_f(p^k) / n^{1/2} at n = p^k ≤ cap. Satake αβ = 1."""
    primes = [p for p in range(2, cap + 1) if all(p % q for q in range(2, int(p**0.5) + 1))]
    pts = []
    for p in primes:
        if p not in an:
            continue
        ap = an[p]
        # ramified at p | N: recurrence a_{p^k} = a_p a_{p^{k-1}}
        ram = Ncond % p == 0
        seq = [1.0, ap]
        n = p
        k = 1
        while n <= cap:
            af = seq[k]
            if af != 0:
                pts.append((math.log(n), af * math.log(p) / math.sqrt(n)))
            k += 1
            n *= p
            if ram:
                seq.append(ap * seq[-1])
            else:
                seq.append(ap * seq[-1] - seq[-2])
    return pts


def assemble(name, mu, NB, dps, DEG=12):
    rec = load_form(name)
    Ncond = int(rec["N"])
    R = float(rec["R"])
    mp.mp.dps = dps
    t0 = time.time()
    L = mp.log(mp.mpf(mu))
    # Gamma((s ± iR)/2) at s = 1/2  ->  s0 = 1/4 ± i R/2
    s0s = (mp.mpf("0.25") + 1j * mp.mpf(R) / 2, mp.mpf("0.25") - 1j * mp.mpf(R) / 2)
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
    cut = mp.log(1 - mp.e ** (-2 * L))
    CST = mp.log(mp.mpf(Ncond)) / 2 - mp.log(mp.pi) - mp.euler - cut
    panels = []
    for s0 in s0s:
        D2 = [
            wts[k] * 2 * mp.e ** (-2 * s0 * nodes[k]) / (1 - mp.e ** (-2 * nodes[k]))
            for k in range(K)
        ]
        EC = [mp.e ** (-(2 - 2 * s0) * nodes[k]) for k in range(K)]
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
    ppts = [(mp.mpf(y), mp.mpf(w)) for y, w in lambda_pts(rec["an"], cap, Ncond)]
    print(f"  slug={rec['slug']} N={Ncond} R={R:.4f} cap={cap} n_pts={len(ppts)}", flush=True)

    S = mp.matrix(NB + 1)
    for n in range(NB + 1):
        for m in range(n, NB + 1):
            th, F0 = th_nodes(n, m)
            arch = mp.mpf(0)
            for D2, EC, CST_ in panels:
                val = F0 / 2 * CST_ + mp.mpf("0.5") * mp.fsum(
                    D2[k] * (F0 * EC[k] - th[k]) for k in range(K)
                )
                arch += val
            # conjugate pair: keep the real part (even Weil form)
            arch = mp.re(arch)
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
    dt = time.time() - t0
    print(
        f"[{name} Qmaass mu={mu} N={NB+1} dps={dps}] lam0={mp.nstr(lam[0],4)}  "
        f"ell={[round(x, 2) for x in ell[:6]]}  "
        f"N_eff={neff:.2f} kbar={kbar:.2f} l1/l0={ratio:.2e}  {dt:.0f}s"
    )
    return lam[0], ell, dt


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "maass1"
    mu = float(sys.argv[2]) if len(sys.argv) > 2 else 6.0
    NB = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    dps = int(sys.argv[4]) if len(sys.argv) > 4 else 25
    assemble(name, mu, NB, dps)


if __name__ == "__main__":
    main()
