#!/usr/bin/env python3
"""Composite 2-point Gauss of a_odd on [0,1/2]+[1/2,1].

Remainder uses frozen max|a^{(4)}|=23.5 (`report/odd-gauss2.md`).

    python3 code/av_odd_gauss2.py
"""
from __future__ import annotations
import math
from av_enclose_odd_ball import a_odd, cst, p_of
from scan_s import CHARS

M4 = 23.5
C2_HALF = (0.5 ** 5) * (math.factorial(2) ** 4) / (5.0 * math.factorial(4) ** 3)


def gauss2(A, B):
    mid = 0.5 * (A + B)
    h = 0.5 * (B - A)
    s = 1.0 / math.sqrt(3.0)
    return h * (a_odd(mid - h * s) + a_odd(mid + h * s))


def main():
    I = gauss2(0.0, 0.5) + gauss2(0.5, 1.0)
    rem = 2.0 * C2_HALF * M4
    print(f"composite G2+G2  {I:.9f}")
    print(f"remainder        {rem:.9f}  (M4={M4})")
    print(f"I[0,1]           [{I-rem:.6f}, {I+rem:.6f}]")
    ok = True
    print(f"{'name':<8} {'Qlo*':>10} {'Qhi*':>10}")
    # * only the [0,1] piece enclosed this way; [1,L] taken as the
    #   point traps of av_enclose_odd_ball (no extra rem here).
    from av_enclose import trap
    from av_gauss import L16
    from av_enclose_odd_ball import a_odd as ao
    t1, _ = trap(ao, 1.0, 1.59, 8)
    t2, _ = trap(ao, 1.59, L16, 8)
    for name in ("chi3", "chi4", "chi7"):
        c, p = cst(CHARS[name]["q"]), p_of(name)
        Qlo = c + (I - rem) + t1 + t2 - p
        Qhi = c + (I + rem) + t1 + t2 - p
        print(f"{name:<8} {Qlo:10.5f} {Qhi:10.5f}")
        ok = ok and Qlo > 0
    print("Qlo>0", ok)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
