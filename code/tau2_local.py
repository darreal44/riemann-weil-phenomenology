#!/usr/bin/env python3
"""Local 2-adic pairing of Connes (1999) Thm 4, by shells. No Fmat grid.

    ⟨τ₂, h⟩ = ∫'_{Q₂*} h(u^{-1}) / |1−u|_2  d*u

Haar: ∫_{Z₂*} d*u = 1, each shell 2^n Z₂* has measure 1.
n = ord₂(u), |u|_2 = 2^{-n}.

    python code/tau2_local.py
"""
from __future__ import annotations

import math

LOG2 = math.log(2)
SQRT2 = math.sqrt(2)


def lambda_module(n: int) -> float:
    """λ = |u|_2 on the shell of order n."""
    return 2.0 ** (-n)


def abs_1_minus_u(n: int) -> float | None:
    """|1−u|_2 on 2^n Z₂*. Units (n=0) are not a Dirac at 2^{±1}."""
    if n > 0:
        return 1.0
    if n < 0:
        return 2.0 ** (-n)
    return None


def raw_weight(n: int) -> float:
    """meas(shell) / |1−u|_2. Zero on units."""
    a = abs_1_minus_u(n)
    if a is None:
        return 0.0
    return 1.0 / a


def twisted_module(n: int) -> float:
    """Twist √λ with λ = |u|_2. At n=±1 this is 1/√2."""
    return raw_weight(n) * math.sqrt(lambda_module(n))


def twisted_inverse(n: int) -> float:
    """Twist √λ with λ = |u^{-1}|_2. At n=+1 (slice λ=2) this is √2."""
    lam = lambda_module(n)
    if lam == 0:
        return 0.0
    return raw_weight(n) * math.sqrt(1.0 / lam)


def mass_at_two(convention: str = "module") -> float:
    """Dirac mass of the peak the slice sees at λ=2.

    module:  λ = |u|_2, peak is n=−1, mass 1/√2.
    inverse: λ = |u^{-1}|_2, peak is n=+1, mass √2.
    """
    if convention == "module":
        return twisted_module(-1)
    if convention == "inverse":
        return twisted_inverse(1)
    raise ValueError(convention)


def bombieri() -> float:
    """(log 2)/√2: same 1/√2 read in dλ instead of d*λ=dλ/λ, or Weil–Bombieri."""
    return LOG2 / SQRT2


def lebesgue_jacobian_at_two() -> float:
    """δ(λ−2) dλ = 2 δ_{λ=2} d*λ, so (1/√2)×2 = √2."""
    return 2.0 * mass_at_two("module")


def shell_weight(n: int) -> tuple[float, float]:
    """Raw Connes weight and module-twisted weight. Kept for tau2_pairing."""
    return raw_weight(n), twisted_module(n)


def twisted_mass(p: int) -> float:
    """Twisted shell mass at λ=p and λ=1/p, Connes units (p^{-1/2})."""
    return p ** -0.5


def main() -> None:
    print(f"{'n':>4} {'|u|_2':>8} {'raw':>10} {'mod-twist':>10} {'inv-twist':>10}")
    for n in range(-4, 5):
        print(
            f"{n:4d} {lambda_module(n):8.4f} {raw_weight(n):10.4f} "
            f"{twisted_module(n):10.4f} {twisted_inverse(n):10.4f}"
        )
    print(f"mass at λ=2, module twist:  {mass_at_two('module'):.6f}  = 1/√2")
    print(f"mass at λ=2, inverse twist: {mass_at_two('inverse'):.6f}  = √2")
    print(f"Lebesgue Jacobian 2·(1/√2): {lebesgue_jacobian_at_two():.6f}  = √2")
    print(f"Bombieri (log 2)/√2:        {bombieri():.6f}")
    print("Fmat grid at Λ=16 walks through 0.49 toward ~1.4; not a local shell.")


if __name__ == "__main__":
    main()
