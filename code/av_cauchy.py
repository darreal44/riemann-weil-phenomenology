#!/usr/bin/env python3
"""Cauchy majorant of |a^{(6)}| on [0,1] for the even integrand.

a is holomorphic on dist(z,[0,1]) < π (poles of w at kπi, k≠0).
On the r-neighbourhood, |a^{(6)}| ≤ 6! M / r^6 with M ≥ max |a|.

    python code/av_cauchy.py           # sample |a| on r=2, 32 cores
    python code/av_cauchy.py --bound   # elementary M on the rectangle

Not RH. One v, μ=16.
"""
from __future__ import annotations

import cmath
import concurrent.futures
import json
import math
import multiprocessing
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from av_gauss import (  # noqa: E402
    GAUSS3_REMAINDER_COEFF,
    GAUSS_NODES,
    GAUSS_WEIGHTS,
    L16,
    V,
    a_integrand,
    gauss3_unit,
    kernel_limit_0,
    theta_v_prime_0,
)

R_DEFAULT = 2.0
# Room: A-v-enclose Alo=-0.829387, window lo=-0.8303.
ROOM = 0.00091


def th_c(n, m, z, L):
    om = lambda k: 2.0 * math.pi * k / L
    if n == 0 and m == 0:
        return 2.0 * (L - z) / L
    if n == 0 or m == 0:
        j = max(n, m)
        return -2.0 * cmath.sin(om(j) * z) / (math.sqrt(2.0) * math.pi * j)
    if n == m:
        return 2.0 * (
            (L - z) * cmath.cos(om(n) * z) / L
            - cmath.sin(om(n) * z) / (2.0 * math.pi * n)
        )
    return (
        2.0
        * (n * cmath.sin(om(n) * z) - m * cmath.sin(om(m) * z))
        / (math.pi * (m * m - n * n))
    )


def theta_v_c(z, L=L16, v=V):
    if abs(z) == 0:
        return 2.0
    acc = 0j
    for n in range(3):
        for m in range(3):
            acc += v[n] * v[m] * th_c(n, m, z, L)
    return acc


def a_complex(z, L=L16, v=V):
    """Regularized a(z) = ½ w (2 e^{-3z/2} − θ_v). Holomorphic at 0."""
    z = complex(z)
    if abs(z) < 1e-10:
        return 0.5 * kernel_limit_0(L, v)
    den = 1.0 - cmath.exp(-2.0 * z)
    w = 2.0 * cmath.exp(-0.5 * z) / den
    g = 2.0 * cmath.exp(-1.5 * z) - theta_v_c(z, L, v)
    return 0.5 * w * g


def stadium_points(r: float, ncap: int, nseg: int) -> list[complex]:
    """Boundary of the r-neighbourhood of [0,1]."""
    pts = []
    for k in range(ncap):
        ang = math.pi / 2 + math.pi * k / max(ncap - 1, 1)
        pts.append(r * cmath.exp(1j * ang))
    for k in range(1, nseg):
        x = k / nseg
        pts.append(x + 1j * r)
    for k in range(ncap):
        ang = math.pi / 2 - math.pi * k / max(ncap - 1, 1)
        pts.append(1.0 + r * cmath.exp(1j * ang))
    for k in range(1, nseg):
        x = 1.0 - k / nseg
        pts.append(x - 1j * r)
    return pts


def _chunk_max(zs: list[complex]) -> float:
    m = 0.0
    for z in zs:
        val = abs(a_complex(z))
        if val > m:
            m = val
    return m


def sample_max(r: float = R_DEFAULT, ncap: int = 400, nseg: int = 800) -> dict:
    pts = stadium_points(r, ncap, nseg)
    ncpu = os.cpu_count() or 8
    chunks = [pts[i::ncpu] for i in range(ncpu)]
    t0 = time.time()
    mx = 0.0
    ctx = multiprocessing.get_context("spawn")
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=ncpu, mp_context=ctx
    ) as pool:
        for fut in concurrent.futures.as_completed(
            [pool.submit(_chunk_max, ch) for ch in chunks if ch]
        ):
            mx = max(mx, float(fut.result()))
    m6 = math.factorial(6) * mx / (r ** 6)
    rem1 = GAUSS3_REMAINDER_COEFF * m6
    rem2 = GAUSS3_REMAINDER_COEFF * m6 / 64.0  # two panels of length 1/2
    return {
        "r": r,
        "npts": len(pts),
        "M_sample": mx,
        "M6": m6,
        "rem_1panel": rem1,
        "rem_2panel": rem2,
        "room": ROOM,
        "seconds": round(time.time() - t0, 3),
        "fits_1panel": rem1 <= ROOM,
        "fits_2panel": rem2 <= ROOM,
    }


def elementary_M(r: float = R_DEFAULT) -> dict:
    """Crude |a| ≤ ½ |w| (|2e^{-3z/2}| + |θ_v|) on the rectangle
    Re ∈ [-r, 1+r], |Im| ≤ r, which contains the stadium.

    |sin(ωz)|, |cos(ωz)| ≤ cosh(ω r).
    |sinh(z)|^2 = sinh²x + sin²y. On |Im|≤r<π, sin(y)=0 only at y=0;
    the kernel is regular there. Bound |w| = e^{x/2}/|sinh z| using
    min(sinh²x + sin²y) on the rectangle minus a disk |z|<r/2 where
    we use the regularized a(0) and a Lipschitz (not needed: max
    modulus is on the boundary, where |z|≥r or |Im|=r).
    """
    L = L16
    om1 = 2.0 * math.pi / L
    om2 = 4.0 * math.pi / L
    ch1 = math.cosh(om1 * r)
    ch2 = math.cosh(om2 * r)
    xmax = 1.0 + r
    xmin = -r
    # |θ_nm| majorants
    th00 = 2.0 * (L + xmax) / L
    th01 = 2.0 * ch1 / (math.sqrt(2.0) * math.pi)
    th02 = 2.0 * ch2 / (math.sqrt(2.0) * math.pi * 2.0)
    th11 = 2.0 * ((L + xmax) / L * ch1 + ch1 / (2.0 * math.pi))
    th22 = 2.0 * ((L + xmax) / L * ch2 + ch2 / (4.0 * math.pi))
    th12 = 2.0 * (1.0 * ch1 + 2.0 * ch2) / (math.pi * 3.0)
    a0, a1, a2 = V
    thv = (
        a0 * a0 * th00
        + a1 * a1 * th11
        + a2 * a2 * th22
        + 2 * abs(a0 * a1) * th01
        + 2 * abs(a0 * a2) * th02
        + 2 * abs(a1 * a2) * th12
    )
    exp15 = 2.0 * math.exp(-1.5 * xmin)
    gmaj = exp15 + thv
    # |sinh| on boundary pieces: |Im|=r ⇒ sin²y = sin²r
    # caps |z|=r or |z-1|=r ⇒ |z|≥r, use |sinh z| ≥ |sin(Im)| or sinh|Re|
    sinr = abs(math.sin(r))
    # left/right caps include Im=0: |sinh(x)| with |x|≥r
    sinh_r = abs(math.sinh(r))
    sinh_floor = min(sinr, sinh_r)
    wmaj = math.exp(0.5 * xmax) / sinh_floor
    Ma = 0.5 * wmaj * gmaj
    m6 = math.factorial(6) * Ma / (r ** 6)
    rem1 = GAUSS3_REMAINDER_COEFF * m6
    rem2 = GAUSS3_REMAINDER_COEFF * m6 / 64.0
    return {
        "r": r,
        "thv": thv,
        "gmaj": gmaj,
        "wmaj": wmaj,
        "sinh_floor": sinh_floor,
        "M_elem": Ma,
        "M6": m6,
        "rem_1panel": rem1,
        "rem_2panel": rem2,
        "room": ROOM,
        "fits_1panel": rem1 <= ROOM,
        "fits_2panel": rem2 <= ROOM,
    }


def gauss3_interval(f, a: float, b: float) -> float:
    h = b - a
    return h * sum(w * f(a + h * x) for x, w in zip(GAUSS_NODES, GAUSS_WEIGHTS))


def min_sinh_on_caps(r: float = R_DEFAULT, n: int = 20000) -> float:
    """min |sinh| on the two semicaps. Floor used: |sin r| at ±ri."""
    m = float("inf")
    for k in range(n):
        ang = math.pi / 2 + math.pi * k / (n - 1)
        z = r * cmath.exp(1j * ang)
        m = min(m, abs(cmath.sinh(z)))
        z = 1.0 + r * cmath.exp(1j * (math.pi / 2 - math.pi * k / (n - 1)))
        m = min(m, abs(cmath.sinh(z)))
    return m


def enclose_cauchy(r: float = R_DEFAULT) -> dict:
    """A(v), Q(v) with composite G₃ ± Cauchy rem, same tail as av_enclose."""
    from av_enclose import CST, WINDOW, p_of_v, termwise_M, trap

    g2 = gauss3_interval(a_integrand, 0.0, 0.5) + gauss3_interval(
        a_integrand, 0.5, 1.0
    )
    bnd = elementary_M(r)
    rem = bnd["rem_2panel"]
    t1, _ = trap(a_integrand, 1.0, 1.59, 8)
    t2, _ = trap(a_integrand, 1.59, L16, 8)
    M1 = termwise_M(1.0, 1.59, gpp_max=0.707, gp_max=0.5510, g_max=0.2229)
    M2 = termwise_M(1.59, L16, gpp_max=0.552, gp_max=0.2398, g_max=0.0564)
    e1 = 8.0 * ((0.59 / 8) ** 3) / 12.0 * M1
    e2 = 8.0 * ((L16 - 1.59) / 8) ** 3 / 12.0 * M2
    Ilo, Ihi = t1 + t2 - e1 - e2, t1 + t2 + e1 + e2
    Alo = CST + (g2 - rem) + Ilo
    Ahi = CST + (g2 + rem) + Ihi
    P = p_of_v()
    return {
        "G3_2panel": g2,
        "rem": rem,
        "Alo": Alo,
        "Ahi": Ahi,
        "P": P,
        "Qlo": Alo - P,
        "Qhi": Ahi - P,
        "window": WINDOW,
        "inside_window": WINDOW[0] <= Alo and Ahi <= WINDOW[1],
        "Qlo_pos": Alo - P > 0,
    }


def main() -> None:
    r = R_DEFAULT
    print(f"r={r}  room={ROOM}  poles at k*pi*i, dist={math.pi:.4f}", flush=True)
    t0 = time.time()
    samp = sample_max(r)
    print(
        f"sample n={samp['npts']}  M={samp['M_sample']:.4f}  "
        f"M6={samp['M6']:.4e}  rem1={samp['rem_1panel']:.4e}  "
        f"rem2={samp['rem_2panel']:.4e}  {samp['seconds']}s",
        flush=True,
    )
    bnd = elementary_M(r)
    print(
        f"elem  thv={bnd['thv']:.2f}  w={bnd['wmaj']:.3f}  "
        f"M={bnd['M_elem']:.4f}  M6={bnd['M6']:.4e}  "
        f"rem1={bnd['rem_1panel']:.4e}  rem2={bnd['rem_2panel']:.4e}",
        flush=True,
    )
    g1 = gauss3_unit(a_integrand)
    g2 = gauss3_interval(a_integrand, 0.0, 0.5) + gauss3_interval(
        a_integrand, 0.5, 1.0
    )
    print(f"G3[0,1]={g1:.9f}  G3[0,1/2]+G3[1/2,1]={g2:.9f}", flush=True)
    cap = min_sinh_on_caps(r)
    print(f"min |sinh| on caps={cap:.6f}  |sin r|={abs(math.sin(r)):.6f}", flush=True)
    enc = enclose_cauchy(r)
    print(
        f"A=[{enc['Alo']:.6f}, {enc['Ahi']:.6f}]  "
        f"Q=[{enc['Qlo']:.6f}, {enc['Qhi']:.6f}]  "
        f"inside={enc['inside_window']}  Qlo>0={enc['Qlo_pos']}",
        flush=True,
    )
    dest = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "report",
        "av-cauchy-a6.json",
    )
    payload = {
        "r": r,
        "room": ROOM,
        "sample": samp,
        "elementary": bnd,
        "G3": g1,
        "G3_2panel": g2,
        "min_sinh_caps": cap,
        "sin_r": abs(math.sin(r)),
        "enclose": enc,
        "seconds": round(time.time() - t0, 3),
    }
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    if not enc["inside_window"] or not enc["Qlo_pos"]:
        verd = "KILL-window"
    elif bnd["fits_1panel"]:
        verd = "SURVIVE-1panel"
    elif bnd["fits_2panel"]:
        verd = "SURVIVE-2panel"
    elif samp["fits_2panel"]:
        verd = "KILL-elem-loose"
    else:
        verd = "KILL"
    print(f"wrote {dest}", flush=True)
    print(verd, flush=True)


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
