#!/usr/bin/env python3
"""The (log 2, log 3] step: two mechanisms. No RH.

Mechanism A — Connes–Consani 2021 at Λ=1: remainder
N_I = −2ε'(1⁺)(Id − K_I). Works on a window of length log 2
(one eigenvalue of K_I above 1). Does not transport: K_I gets a
second eigenvalue above 1 past L≈1.01, and the semi-local D_S∘Q
is essentially positive (notes/semilocal-step.pdf).

Mechanism B — Connes 1999, Theorem 4, the other nature:
    Tr(R_Λ U(h)) − 2 h(1) log' Λ
        = Σ_{v∈S} ∫'_{k_v^*} h(u^{-1}) / |1−u|_v d*u  + o(1).
The subtracted term is the identity orbit. It vanishes at the
Sonin cutoff Λ=1. The finite part is the S-local Weil pairing,
not a compact remainder, and it does not give positivity for free.

Two logarithms are not interchangeable: 2 h(1) log' Λ is a function
of the cutoff Λ; the HS divergence 0.65 log₂(1/h) is a function of
the cell width at fixed cutoff (code/finite_part_HS.py).

    python code/log2_log3_step.py
"""
from __future__ import annotations

import math

LOG2 = math.log(2)
LOG3 = math.log(3)
SONIN_CUTOFF = 1.0
HS_LOG_COEFF = 0.65  # measured; same as finite_part_HS.C_LOG and δ_S


def log_prime(Lam: float) -> float:
    """Connes log' Λ. He writes 2 log' Λ = ∫_{|λ|∈[Λ^{-1},Λ]} d*λ.

    On ℝ>0 with Haar dλ/λ that integral is 2 ln Λ, so log' Λ = ln Λ.
    """
    return math.log(float(Lam))


def identity_orbit(h1: float, Lam: float) -> float:
    """2 h(1) log' Λ, Connes 1999 Theorem 4."""
    return 2.0 * float(h1) * log_prime(Lam)


def identity_orbit_slice(h1: float, Lam: float) -> float:
    """4 h(1) ln Λ, the slope the slice code fits (trace_formula.py).

    Factor 2 vs identity_orbit: R_Λ = P̂_Λ P_Λ counts both cutoffs
    on a two-sided additive interval. Same Λ-dependence, not 1/h.
    """
    return 4.0 * float(h1) * math.log(float(Lam))


def finite_part_trace(T: float, h1: float, Lam: float, convention: str = "connes") -> float:
    """T minus the identity orbit. Theorem 4: this → Σ_v local Weil."""
    if convention == "connes":
        return float(T) - identity_orbit(h1, Lam)
    if convention == "slice":
        return float(T) - identity_orbit_slice(h1, Lam)
    raise ValueError(convention)


def finite_part_hs(sum_lambda2: float, inv_h: float, c: float | None = None) -> float:
    """Σλ² − c log₂(1/h). UV finite part at fixed cutoff, not log' Λ."""
    if c is None:
        c = HS_LOG_COEFF
    return float(sum_lambda2) - c * math.log2(float(inv_h))


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def interior_primes(mu: float) -> list[int]:
    """Primes p with 1 < p < μ.

    The lag y = log p sits strictly inside a window of length
    L = log μ. A prime at the endpoint p = μ has y = L, and
    θ(L) = 0 for any test function supported in [0, L].
    """
    hi = math.floor(float(mu) - 1e-15)
    return [p for p in range(2, int(hi) + 1) if _is_prime(p)]


def ki_n_above_one(L: float, omega: float = 8e-3):
    """#{λ(K_I) > 1} at window length L. Drives KI_spectrum.eigs_at."""
    import os
    import sys

    import numpy as np

    code = os.path.dirname(os.path.abspath(__file__))
    if code not in sys.path:
        sys.path.insert(0, code)
    from KI_spectrum import eigs_at

    ev, _ = eigs_at(float(L), omega=omega)
    ev = np.asarray(ev, float)
    return int((ev > 1).sum()), ev


def step_is_taken() -> bool:
    """The (log 2, log 3] step for the whole Paley–Wiener class is open."""
    return False


def main() -> None:
    print(f"Sonin cutoff Λ={SONIN_CUTOFF}: identity_orbit(1, 1) = {identity_orbit(1.0, 1.0)}")
    print(f"identity_orbit(1, e) = {identity_orbit(1.0, math.e)}  (2 h(1) log' e = 2)")
    print(f"d/d(ln Λ) identity_orbit = {identity_orbit(1.0, math.e)}")
    print(f"d/d(ln Λ) slice orbit    = {identity_orbit_slice(1.0, math.e)}")
    print(f"HS log₂(1/h) coeff       = {HS_LOG_COEFF}  (not a function of Λ)")
    print(f"interior primes at μ=2: {interior_primes(2.0)}")
    print(f"interior primes at μ=3: {interior_primes(3.0)}")
    print(f"(log 2, log 3] step taken: {step_is_taken()}")


if __name__ == "__main__":
    main()
