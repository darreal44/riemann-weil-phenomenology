#!/usr/bin/env python3
"""Point transfer of the odd integrand (s0=3/4) at mu=16.

Not a remainder ball: G3 + 8+8 trap of a_odd, no |a''| majorant yet.
Checks Q~ > 0 on every odd character in CHARS.

    python3 code/av_enclose_odd.py
"""
from __future__ import annotations
import math
from scan_s import CHARS, chi_tab
from av_gauss import theta_v, GAUSS_NODES, GAUSS_WEIGHTS, L16
from av_enclose import trap

GAMMA = 0.5772156649015329


def w_odd(y):
    return 2.0 * math.exp(-1.5 * y) / (1.0 - math.exp(-2.0 * y))


def a_odd(y):
    return 0.5 * w_odd(y) * (2.0 * math.exp(-0.5 * y) - theta_v(y))


def integral_point():
    g3 = sum(w * a_odd(x) for w, x in zip(GAUSS_WEIGHTS, GAUSS_NODES))
    t1, _ = trap(a_odd, 1.0, 1.59, 8)
    t2, _ = trap(a_odd, 1.59, L16, 8)
    return g3 + t1 + t2


def cst(q):
    return math.log(q / math.pi) - GAMMA - math.log(1.0 - 1.0 / 256.0)


def p_of(name):
    cf = CHARS[name]
    tab = chi_tab(cf["d"], cf["q"])
    acc = 0.0
    for n in range(2, 17):
        y2, p = n, None
        for qq in (2, 3, 5, 7, 11, 13):
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


ODD = tuple(k for k, v in CHARS.items() if v.get("a") == 1)


def main():
    I = integral_point()
    print(f"int a_odd ~ {I:.6f}  (point, no remainder)")
    ok = True
    print(f"{'name':<8} {'q':>3} {'Q~':>10}")
    for name in ODD:
        Q = cst(CHARS[name]["q"]) + I - p_of(name)
        print(f"{name:<8} {CHARS[name]['q']:3d} {Q:10.5f}")
        ok = ok and Q > 0
    print("all Q~>0", ok)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
