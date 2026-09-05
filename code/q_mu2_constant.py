#!/usr/bin/env python3
"""1×1 Q on the constant mode, μ=2 (only p=2).

Q_00 = CST + (1/2)∫ D2(y) (2 e^{-(2-2s0)y} - 2(L-y)/L) dy
     − χ(2) log2 / √2 · θ_00(log 2)

No matrix. Prints the number and a lower bound that
drops the positive D2 remainder when it is positive.
"""
from __future__ import annotations

import math

import mpmath as mp

mp.mp.dps = 40


def Q00(q, a, chi2):
    mu = 2
    L = mp.log(mp.mpf(mu))
    s0 = mp.mpf(1) / 4 + mp.mpf(a) / 2
    CST = mp.log(mp.mpf(q) / mp.pi) - mp.euler - mp.log(1 - mp.e ** (-2 * L))
    y2 = mp.log(mp.mpf(2))

    def integrand(y):
        D2 = 2 * mp.e ** (-2 * s0 * y) / (1 - mp.e ** (-2 * y))
        th = 2 * (L - y) / L
        EC = mp.e ** (-(2 - 2 * s0) * y)
        return D2 * (2 * EC - th)

    arch_int = mp.quad(integrand, [mp.mpf("1e-12"), L])
    arch = CST + mp.mpf("0.5") * arch_int
    prime = chi2 * mp.log(2) / mp.sqrt(2) * (2 * (L - y2) / L)
    return float(CST), float(arch_int), float(arch), float(prime), float(arch - prime)


def main():
    # even χ5: q=5 a=0 χ(2)=((5-1)/2 wait) kronecker(5,2)=?
    # χ5(2) = (5/2) Legendre = -1
    print("chi5 even s0=1/4 χ(2)=-1")
    CST, I, arch, pr, Q = Q00(5, 0, -1)
    print(f"  CST={CST:.6f}  int={I:.6f}  arch={arch:.6f}  prime={pr:.6f}  Q00={Q:.6f}")
    print("chi4 odd  s0=3/4 χ(2)=0 (mod 4)")
    CST, I, arch, pr, Q = Q00(4, 1, 0)
    print(f"  CST={CST:.6f}  int={I:.6f}  arch={arch:.6f}  prime={pr:.6f}  Q00={Q:.6f}")


if __name__ == "__main__":
    main()
