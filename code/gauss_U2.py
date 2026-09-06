#!/usr/bin/env python3
"""Exact Gauss sums on U2/U4 = {1,5,9,13} mod 16."""
from __future__ import annotations

import cmath
import math

U = (1, 5, 9, 13)
GEN = 5


def chi(m: int, u: int) -> complex:
    t, x = 0, 1
    while x != u:
        x = (x * GEN) % 16
        t += 1
    return cmath.exp(2j * math.pi * m * t / 4)


def tau(m: int, den: int, a: int = 1) -> complex:
    return sum(chi(m, u) * cmath.exp(2j * math.pi * a * u / den) for u in U)


# Conductor-aligned values (exact). ψ(u)=e(a u / 2^k).
TAU = {
    (3, 16, 1): 4 * cmath.exp(1j * math.pi / 8),
    (1, 16, 3): 4 * cmath.exp(3j * math.pi / 8),
    (2, 8, 1): 4 * cmath.exp(1j * math.pi / 4),
}


def main():
    for (m, den, a), exact in TAU.items():
        num = tau(m, den, a)
        print(f"m={m} ψ=e({a}u/{den})  num={num:.8f}  exact={exact:.8f}  err={abs(num-exact):.2e}")


if __name__ == "__main__":
    main()
