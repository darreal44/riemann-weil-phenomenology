#!/usr/bin/env python3
"""Transfer the chi5 integral ball to chi8 mu=16 (same a(y), new CST and P).

    python3 code/av_enclose_chi8.py
"""
from __future__ import annotations
import math
import av_enclose as ae
from av_gauss import theta_v


def cst8():
    return math.log(8.0 / math.pi) - 0.5772156649015329 - math.log(1.0 - 1.0 / 256.0)


def p8():
    # chi8(n) for odd prime powers <= 16; even n ramified.
    terms = ((3, 3, -1), (5, 5, -1), (7, 7, 1), (9, 3, 1), (11, 11, -1), (13, 13, -1))
    acc = 0.0
    for n, p, chi in terms:
        acc += chi * math.log(p) / math.sqrt(n) * theta_v(math.log(n))
    return acc


def main():
    # reuse chi5 integral enclosure from ae.main pieces
    g3 = __import__("av_gauss", fromlist=["gauss3_unit", "a_integrand"])
    from av_gauss import gauss3_unit, a_integrand, L16
    from av_enclose import trap, termwise_M

    t1, _ = trap(a_integrand, 1.0, 1.59, 8)
    t2, _ = trap(a_integrand, 1.59, L16, 8)
    M1 = termwise_M(1.0, 1.59, 0.707, 0.5510, 0.2229)
    M2 = termwise_M(1.59, L16, 0.552, 0.2398, 0.0564)
    h1, h2 = 0.59 / 8, (L16 - 1.59) / 8
    e1 = 8.0 * (h1 ** 3) / 12.0 * M1
    e2 = 8.0 * (h2 ** 3) / 12.0 * M2
    Ilo, Ihi = t1 + t2 - e1 - e2, t1 + t2 + e1 + e2
    c, p = cst8(), p8()
    g3v = gauss3_unit(a_integrand)
    Alo, Ahi = c + g3v + Ilo, c + g3v + Ihi
    Qlo, Qhi = Alo - p, Ahi - p
    print(f"CST8    {c:.9f}")
    print(f"P8      {p:.9f}")
    print(f"A8      [{Alo:.6f}, {Ahi:.6f}]")
    print(f"Q8      [{Qlo:.6f}, {Qhi:.6f}]")
    print(f"Q8>0    {Qlo > 0}")
    return 0 if Qlo > 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
