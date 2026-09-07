#!/usr/bin/env python3
"""A(v) enclose: Gauss+Cauchy on [0,1] and on [1,L]. No trap, no |g''|.

Even χ₅ and odd χ₃/χ₄/χ₇. Same v, μ=16.

    python code/av_enclose_cauchy.py

Not RH.
"""
from __future__ import annotations

import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from av_cauchy import elementary_M, gauss3_interval  # noqa: E402
from av_cauchy_odd import a_odd, elementary_M_odd  # noqa: E402
from av_cauchy_tail import H as TAIL_H  # noqa: E402
from av_cauchy_tail import HI, LO, elem_on_segment, rem_panels
from av_enclose import CST, WINDOW, p_of_v  # noqa: E402
from av_enclose_odd_ball import cst, p_of  # noqa: E402
from av_gauss import GAUSS3_REMAINDER_COEFF, L16, a_integrand  # noqa: E402
from scan_s import CHARS  # noqa: E402

N01, NTAIL, R = 2, 8, 2.0


def gauss3_panels(f, lo: float, hi: float, n: int) -> float:
    h = (hi - lo) / n
    return sum(gauss3_interval(f, lo + i * h, lo + (i + 1) * h) for i in range(n))


def elem_odd_segment(lo: float, hi: float, r: float = R) -> dict:
    """Odd |a| rectangle bound on the r-neighbourhood of [lo, hi]."""
    from av_gauss import V

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
    gmaj = 2.0 * math.exp(-0.5 * xmin) + thv
    sinh_floor = min(abs(math.sin(r)), abs(math.sinh(r)))
    wmaj = math.exp(-0.5 * xmin) / sinh_floor
    Ma = 0.5 * wmaj * gmaj
    M6 = math.factorial(6) * Ma / (r ** 6)
    return {"M_elem": Ma, "M6": M6, "thv": thv, "wmaj": wmaj}


def enclose_even() -> dict:
    i01 = gauss3_panels(a_integrand, 0.0, 1.0, N01)
    r01 = elementary_M(R)["rem_2panel"]
    i1l = gauss3_panels(a_integrand, LO, HI, NTAIL)
    el = elem_on_segment(LO, HI, R)
    r1l = rem_panels(el["M6"], TAIL_H, NTAIL)
    alo = CST + (i01 - r01) + (i1l - r1l)
    ahi = CST + (i01 + r01) + (i1l + r1l)
    p = p_of_v()
    return {
        "I01": i01,
        "R01": r01,
        "I1L": i1l,
        "R1L": r1l,
        "Alo": alo,
        "Ahi": ahi,
        "P": p,
        "Qlo": alo - p,
        "Qhi": ahi - p,
        "inside_window": WINDOW[0] <= alo and ahi <= WINDOW[1],
        "Qlo_pos": alo - p > 0,
        "window": WINDOW,
        "M6_tail": el["M6"],
    }


def enclose_odd() -> dict:
    i01 = gauss3_panels(a_odd, 0.0, 1.0, N01)
    r01 = elementary_M_odd(R)["rem_2panel"]
    i1l = gauss3_panels(a_odd, LO, HI, NTAIL)
    el = elem_odd_segment(LO, HI, R)
    r1l = rem_panels(el["M6"], TAIL_H, NTAIL)
    rows = {}
    for name in ("chi3", "chi4", "chi7"):
        c, p = cst(CHARS[name]["q"]), p_of(name)
        qlo = c + (i01 - r01) + (i1l - r1l) - p
        qhi = c + (i01 + r01) + (i1l + r1l) - p
        rows[name] = {"Qlo": qlo, "Qhi": qhi, "P": p, "CST": c}
    return {
        "I01": i01,
        "R01": r01,
        "I1L": i1l,
        "R1L": r1l,
        "M6_tail": el["M6"],
        "chi": rows,
        "chi3_pos": rows["chi3"]["Qlo"] > 0,
    }


def main() -> int:
    print("even: 2-panel [0,1] + 8-panel [1,L], Cauchy rem, no trap", flush=True)
    ev = enclose_even()
    print(
        f"  I01={ev['I01']:.9f} +/- {ev['R01']:.4e}  "
        f"I1L={ev['I1L']:.9f} +/- {ev['R1L']:.4e}",
        flush=True,
    )
    print(
        f"  A=[{ev['Alo']:.6f}, {ev['Ahi']:.6f}]  "
        f"Q=[{ev['Qlo']:.6f}, {ev['Qhi']:.6f}]  "
        f"inside={ev['inside_window']}  Qlo>0={ev['Qlo_pos']}",
        flush=True,
    )
    print("odd: same panels", flush=True)
    od = enclose_odd()
    print(
        f"  I01={od['I01']:.9f} +/- {od['R01']:.4e}  "
        f"I1L={od['I1L']:.9f} +/- {od['R1L']:.4e}",
        flush=True,
    )
    for name, row in od["chi"].items():
        print(f"  {name}  Q=[{row['Qlo']:.5f}, {row['Qhi']:.5f}]", flush=True)
    dest = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "report",
        "av-enclose-cauchy-tail.json",
    )
    payload = {"even": ev, "odd": od, "N01": N01, "Ntail": NTAIL, "r": R}
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    print(f"wrote {dest}", flush=True)
    ok = ev["inside_window"] and ev["Qlo_pos"] and od["chi3_pos"]
    print("SURVIVE" if ok else "KILL", flush=True)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
