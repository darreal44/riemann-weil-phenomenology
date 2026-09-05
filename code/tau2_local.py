#!/usr/bin/env python3
"""Local 2-adic pairing of Connes (1999) Thm 4, no Fmat grid.

    ∫'_{Q2*}  h(u^{-1}) / |1-u|_2  d*u

Shells n = ord_2(u). Twist λ^{1/2} with λ = |u|_R in the slice
convention of the repository (ϑ carries Δ^{1/2}).

    python3 code/tau2_local.py
"""
from __future__ import annotations

import math

LOG2 = math.log(2)
SQRT2 = math.sqrt(2)

def twisted_mass(p: int) -> float:
    """Twisted shell mass at λ=p and λ=1/p. Connes units."""
    return p ** -0.5


def shell_weight(n: int) -> tuple[float, float]:
    """Raw Connes weight and twisted (λ^{1/2}) weight on the shell 2^n Z2*.

    |u|_2 = 2^{-n}. Slice λ is read as 2^{-n} in the real picture
    used by ϑ(λ)g(r) = λ^{-1/2} g(r/λ) — see prereg-2adic-mass.md.
    """
    abs_u_2 = 2.0 ** (-n)
    if n > 0:
        # |u|_2 < 1, |1-u|_2 = 1, meas(shell) = 1
        raw = 1.0
    elif n < 0:
        # |u|_2 > 1, |1-u|_2 = |u|_2 = 2^{-n}
        raw = 1.0 / abs_u_2
    else:
        # units: |1-u|_2 = 1 on a set of measure 1/2 (odd units ≡ 1 mod 2
        # wait: Z2* = 1+2Z2, |1-u|_2 ≤ 1/2. Standard split:
        # meas{|u|_2=1, |1-u|_2=1} = 0 (units are 1 mod 2, so |1-u|_2≤1/2)
        # This shell is NOT the point masses at 2^{±1}.
        raw = 0.0
    lam = abs_u_2
    twisted = raw * math.sqrt(lam)
    return raw, twisted


def main():
    print(f"{'n':>4} {'|u|_2':>8} {'raw':>10} {'twisted':>10}  shell")
    tot_raw = tot_tw = 0.0
    for n in range(-4, 5):
        raw, tw = shell_weight(n)
        tot_raw += raw
        tot_tw += tw
        tag = ""
        if n == -1:
            tag = "  <- λ=2"
        if n == 1:
            tag = "  <- λ=1/2"
        print(f"{n:4d} {2**(-n):8.4f} {raw:10.4f} {tw:10.4f}{tag}")
    print(f"locked twist at n=±1: {1/SQRT2:.4f} and {1/SQRT2:.4f}")
    print(f"Bombieri (log 2)/sqrt(2) = {LOG2/SQRT2:.4f}")
    print("Grid at Λ=16, h→0 extrapolates to ~1.4 — not a local shell.")
    print("\ngeneral p  twisted mass at p^{±1} (Connes units)")
    for p0 in (2,3,5,7):
        print(f"  p={p0}  {twisted_mass(p0):.4f}")



if __name__ == "__main__":
    main()


def twisted_mass(p: int) -> float:
    """Twisted shell mass at lambda=p and lambda=1/p. Connes units."""
    return p ** -0.5

if __name__ == "__main__" and False:
    pass
