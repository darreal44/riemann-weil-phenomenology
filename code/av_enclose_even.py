#!/usr/bin/env python3
"""Transfer the chi5 mu=16 integral ball to every even character (a=0).

    python3 code/av_enclose_even.py
"""
from __future__ import annotations
import math
from scan_s import CHARS, chi_tab
from av_gauss import theta_v, gauss3_unit, a_integrand, L16
from av_enclose import trap, termwise_M

EVEN = ("chi5", "chi8", "chi12", "chi13", "chi17", "chi21", "chi24e", "chi29")


def integral_ball():
    t1, _ = trap(a_integrand, 1.0, 1.59, 8)
    t2, _ = trap(a_integrand, 1.59, L16, 8)
    M1 = termwise_M(1.0, 1.59, 0.707, 0.5510, 0.2229)
    M2 = termwise_M(1.59, L16, 0.552, 0.2398, 0.0564)
    h1, h2 = 0.59 / 8, (L16 - 1.59) / 8
    e = 8.0 * (h1 ** 3) / 12.0 * M1 + 8.0 * (h2 ** 3) / 12.0 * M2
    g3 = gauss3_unit(a_integrand)
    mid = g3 + t1 + t2
    return mid - e, mid + e


def p_even(name):
    cf = CHARS[name]
    tab = chi_tab(cf["d"], cf["q"])
    small = (2, 3, 5, 7, 11, 13)
    acc = 0.0
    for n in range(2, 17):
        y2, p = n, None
        for qq in small:
            if y2 % qq == 0:
                p = qq
                while y2 % qq == 0:
                    y2 //= qq
                break
        if not (p and y2 == 1):
            continue
        chi = tab[n % cf["q"]]
        if chi == 0:
            continue
        acc += chi * math.log(p) / math.sqrt(n) * theta_v(math.log(n))
    return acc


def cst(q):
    return math.log(q / math.pi) - 0.5772156649015329 - math.log(1.0 - 1.0 / 256.0)


def main():
    Ilo, Ihi = integral_ball()
    ok = True
    print(f"{'name':<8} {'q':>3} {'Qlo':>10} {'Qhi':>10}")
    for name in EVEN:
        q = CHARS[name]["q"]
        P = p_even(name)
        Qlo, Qhi = cst(q) + Ilo - P, cst(q) + Ihi - P
        print(f"{name:<8} {q:3d} {Qlo:10.5f} {Qhi:10.5f}")
        ok = ok and Qlo > 0
    print("all Qlo>0", ok)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
