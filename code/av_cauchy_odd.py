#!/usr/bin/env python3
"""Cauchy majorant of |a_odd^{(6)}| on [0,1] (s₀=3/4).

Same poles kπi as the even side. w_odd = e^{-z/2}/sinh z.

    python code/av_cauchy_odd.py

Not RH. Same v, μ=16. Tight window χ₃.
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
from av_cauchy import (  # noqa: E402
    R_DEFAULT,
    gauss3_interval,
    min_sinh_on_caps,
    stadium_points,
    th_c,
    theta_v_c,
)
from av_enclose_odd_ball import a_odd, cst, p_of  # noqa: E402
from av_gauss import (  # noqa: E402
    GAUSS3_REMAINDER_COEFF,
    GAUSS_NODES,
    GAUSS_WEIGHTS,
    L16,
    V,
    theta_v_prime_0,
)
from av_odd_app import termwise_M  # noqa: E402
from av_enclose import trap  # noqa: E402
from scan_s import CHARS  # noqa: E402

# χ₃ termwise Qlo ≈ 0.00490 (odd-ball.md). Kill if rem2 ≥ this.
ROOM = 0.00490


def kernel_limit_odd(L=L16, v=V) -> float:
    """lim w_odd (2 e^{-y/2} − θ_v) = −1 − θ_v'(0)."""
    return -1.0 - theta_v_prime_0(L, v)


def a_odd_complex(z, L=L16, v=V):
    z = complex(z)
    if abs(z) < 1e-10:
        return 0.5 * kernel_limit_odd(L, v)
    den = 1.0 - cmath.exp(-2.0 * z)
    w = 2.0 * cmath.exp(-1.5 * z) / den
    g = 2.0 * cmath.exp(-0.5 * z) - theta_v_c(z, L, v)
    return 0.5 * w * g


def _chunk_max(zs: list[complex]) -> float:
    m = 0.0
    for z in zs:
        val = abs(a_odd_complex(z))
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
    rem2 = GAUSS3_REMAINDER_COEFF * m6 / 64.0
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


def elementary_M_odd(r: float = R_DEFAULT) -> dict:
    """|a_odd| ≤ ½ |w_odd| (|2e^{-z/2}| + |θ_v|) on the r-rectangle.

    |w_odd| = e^{-x/2}/|sinh z|, max at xmin = -r.
    """
    L = L16
    om1 = 2.0 * math.pi / L
    om2 = 4.0 * math.pi / L
    ch1 = math.cosh(om1 * r)
    ch2 = math.cosh(om2 * r)
    xmax = 1.0 + r
    xmin = -r
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
    exp05 = 2.0 * math.exp(-0.5 * xmin)
    gmaj = exp05 + thv
    sinr = abs(math.sin(r))
    sinh_r = abs(math.sinh(r))
    sinh_floor = min(sinr, sinh_r)
    wmaj = math.exp(-0.5 * xmin) / sinh_floor
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


def enclose_odd(r: float = R_DEFAULT) -> dict:
    g1 = sum(w * a_odd(x) for w, x in zip(GAUSS_WEIGHTS, GAUSS_NODES))
    g2 = gauss3_interval(a_odd, 0.0, 0.5) + gauss3_interval(a_odd, 0.5, 1.0)
    bnd = elementary_M_odd(r)
    rem = bnd["rem_2panel"]
    t1, _ = trap(a_odd, 1.0, 1.59, 8)
    t2, _ = trap(a_odd, 1.59, L16, 8)
    MT1 = termwise_M(1.0, 0.7190, 0.6138, 1.4006)
    MT2 = termwise_M(1.59, 0.7222, 0.2764, 0.6516)
    h1, h2 = 0.59 / 8, (L16 - 1.59) / 8
    rL = 8.0 * (h1 ** 3) / 12.0 * MT1 + 8.0 * (h2 ** 3) / 12.0 * MT2
    rows = {}
    for name in ("chi3", "chi4", "chi7"):
        c, p = cst(CHARS[name]["q"]), p_of(name)
        Qlo = c + (g2 - rem) + t1 + t2 - rL - p
        Qhi = c + (g2 + rem) + t1 + t2 + rL - p
        rows[name] = {"Qlo": Qlo, "Qhi": Qhi, "P": p, "CST": c}
    return {
        "G3": g1,
        "G3_2panel": g2,
        "rem": rem,
        "tail": t1 + t2,
        "tail_rem": rL,
        "chi": rows,
        "chi3_pos": rows["chi3"]["Qlo"] > 0,
    }


def main() -> None:
    r = R_DEFAULT
    print(
        f"odd  r={r}  room={ROOM}  a_odd(0)={0.5 * kernel_limit_odd():.6f}",
        flush=True,
    )
    t0 = time.time()
    samp = sample_max(r)
    print(
        f"sample n={samp['npts']}  M={samp['M_sample']:.4f}  "
        f"M6={samp['M6']:.4e}  rem1={samp['rem_1panel']:.4e}  "
        f"rem2={samp['rem_2panel']:.4e}  {samp['seconds']}s",
        flush=True,
    )
    bnd = elementary_M_odd(r)
    print(
        f"elem  thv={bnd['thv']:.2f}  w={bnd['wmaj']:.3f}  "
        f"M={bnd['M_elem']:.4f}  rem1={bnd['rem_1panel']:.4e}  "
        f"rem2={bnd['rem_2panel']:.4e}",
        flush=True,
    )
    cap = min_sinh_on_caps(r)
    print(f"min |sinh| on caps={cap:.6f}  |sin r|={abs(math.sin(r)):.6f}", flush=True)
    enc = enclose_odd(r)
    print(
        f"G3={enc['G3']:.9f}  G3_2={enc['G3_2panel']:.9f}  rem={enc['rem']:.4e}",
        flush=True,
    )
    for name, row in enc["chi"].items():
        print(f"  {name}  Q=[{row['Qlo']:.5f}, {row['Qhi']:.5f}]", flush=True)
    dest = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "report",
        "av-cauchy-odd.json",
    )
    payload = {
        "r": r,
        "room": ROOM,
        "sample": samp,
        "elementary": bnd,
        "min_sinh_caps": cap,
        "sin_r": abs(math.sin(r)),
        "enclose": enc,
        "seconds": round(time.time() - t0, 3),
    }
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    if not enc["chi3_pos"]:
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
