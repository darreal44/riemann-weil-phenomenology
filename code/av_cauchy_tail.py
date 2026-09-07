#!/usr/bin/env python3
"""Cauchy |a^{(6)}| majorant on [1, L], μ=16.

Same a as av_cauchy.py. Poles still at kπi; dist([1,L], iπ)=π.
Remainder of 3-node Gauss on an interval of length h is
c₆ M₆ h^7. n equal panels: c₆ M₆ h^7 / n^6.

    python code/av_cauchy_tail.py
    python code/av_cauchy_tail.py --bound

Not RH.
"""
from __future__ import annotations

import cmath
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from av_cauchy import (  # noqa: E402
    R_DEFAULT,
    a_complex,
    elementary_M,
)
from av_gauss import GAUSS3_REMAINDER_COEFF, L16  # noqa: E402

LO, HI = 1.0, float(L16)
H = HI - LO
C6 = GAUSS3_REMAINDER_COEFF


def rem_panels(M6: float, h: float, n: int) -> float:
    return C6 * M6 * (h ** 7) / (n ** 6)


def stadium_segment(lo: float, hi: float, r: float, ncap: int, nseg: int):
    pts = []
    for k in range(ncap):
        ang = math.pi / 2 + math.pi * k / max(ncap - 1, 1)
        pts.append(lo + r * cmath.exp(1j * ang))
    for k in range(1, nseg):
        x = lo + (hi - lo) * k / nseg
        pts.append(x + 1j * r)
    for k in range(ncap):
        ang = math.pi / 2 - math.pi * k / max(ncap - 1, 1)
        pts.append(hi + r * cmath.exp(1j * ang))
    for k in range(1, nseg):
        x = hi - (hi - lo) * k / nseg
        pts.append(x - 1j * r)
    return pts


def sample_M(r=R_DEFAULT, ncap=80, nseg=160) -> float:
    mx = 0.0
    for z in stadium_segment(LO, HI, r, ncap, nseg):
        mx = max(mx, abs(a_complex(z)))
    return mx


def elem_on_segment(lo, hi, r=R_DEFAULT) -> dict:
    """Reuse rectangle majorant of elementary_M, stretched to [lo,hi].

    Patch xmax = hi+r, xmin = lo-r by scaling the [0,1] bound:
    th00 grows with xmax, exp(-1.5 xmin) grows if xmin more negative.
    Call elementary_M then rescale th00-like terms is messy; bound
    |a| by the [0,1] elementary M times the worst extra exp/cosh
    from shifting the segment — cruder: evaluate elementary_M's
    formula with xmax=hi+r, xmin=lo-r copied here.
    """
    from av_cauchy import V

    L = L16
    om1 = 2.0 * math.pi / L
    om2 = 4.0 * math.pi / L
    ch1 = math.cosh(om1 * r)
    ch2 = math.cosh(om2 * r)
    xmax = hi + r
    xmin = lo - r
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
    gmaj = 2.0 * math.exp(-1.5 * xmin) + thv
    sinh_floor = min(abs(math.sin(r)), abs(math.sinh(r)))
    wmaj = math.exp(0.5 * xmax) / sinh_floor
    Ma = 0.5 * wmaj * gmaj
    M6 = math.factorial(6) * Ma / (r ** 6)
    return {"M_elem": Ma, "M6": M6, "thv": thv, "wmaj": wmaj, "xmax": xmax, "xmin": xmin}


def main() -> None:
    r = R_DEFAULT
    print(f"[1,L] L={HI:.6f} h={H:.6f} r={r} c6={C6:.6e}", flush=True)
    t0 = time.time()
    el = elem_on_segment(LO, HI, r)
    print(
        f"elem M={el['M_elem']:.4f} M6={el['M6']:.4e} "
        f"thv={el['thv']:.2f} w={el['wmaj']:.3f}",
        flush=True,
    )
    print(f"{'n':>4} {'h/n':>8} {'rem':>12}", flush=True)
    rows = []
    for n in (1, 2, 4, 8, 16):
        rem = rem_panels(el["M6"], H, n)
        print(f"{n:4d} {H/n:8.4f} {rem:12.4e}", flush=True)
        rows.append({"n": n, "hpanel": H / n, "rem": rem})
    Ms = sample_M(r)
    M6s = math.factorial(6) * Ms / (r ** 6)
    print(f"sample M={Ms:.4f} M6={M6s:.4e} {time.time()-t0:.2f}s", flush=True)
    srows = []
    for n in (1, 2, 4, 8):
        rem = rem_panels(M6s, H, n)
        print(f"  sample n={n} rem={rem:.4e}", flush=True)
        srows.append({"n": n, "rem": rem})
    dest = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "report",
        "av-cauchy-tail.json",
    )
    payload = {
        "lo": LO,
        "hi": HI,
        "h": H,
        "r": r,
        "elementary": el,
        "elem_panels": rows,
        "sample_M": Ms,
        "sample_M6": M6s,
        "sample_panels": srows,
        "seconds": round(time.time() - t0, 3),
    }
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    print("wrote", dest, flush=True)
    # [1,L] currently uses trap remainder in enclose, room unknown.
    # Survive-style: 8 panels elem rem vs 1e-3 ballpark of A digits.
    rem8 = rem_panels(el["M6"], H, 8)
    print(
        "elem 8-panel rem="
        f"{rem8:.4e}  ({'fits 1e-3' if rem8 < 1e-3 else 'needs more panels / better M'})",
        flush=True,
    )


if __name__ == "__main__":
    main()
