"""Semi-local Fourier on the ord₂=0 slice, as a sum of 2-adic sub-shells.

    Fg(ρ) = ½ [ ∑_{n≥0} ĝ(2^n ρ) − ĝ(ρ/2) ]

Each term ½ ĝ(2^n ·) is the contribution of the shell 2^n Z₂*
(lacunary dilation). The n=−1 term is subtracted. Unitarity of F
is `notes/semilocal-step.tex` Proposition 1; this module is the
construction. No RH.

    python code/subshells.py
"""
from __future__ import annotations

import numpy as np


def F_from_shells(hat, xs, nmax=14):
    """Apply the closed-form semi-local transform to a cosine transform `hat`."""
    xs = np.asarray(xs, float)
    out = -hat(xs / 2.0)
    for n in range(nmax):
        out = out + hat((2.0 ** n) * xs)
    return 0.5 * out


def shell_term(hat, xs, n):
    """One sub-shell: n≥0 is +½ ĝ(2^n ρ); n=−1 is −½ ĝ(ρ/2)."""
    xs = np.asarray(xs, float)
    if n == -1:
        return -0.5 * hat(xs / 2.0)
    if n >= 0:
        return 0.5 * hat((2.0 ** n) * xs)
    raise ValueError("n >= -1")


if __name__ == "__main__":
    # reconstruction check on a cosine
    xs = np.array([0.31, 0.77, 1.4, 2.9])

    def hat(xi):
        xi = np.asarray(xi, float)
        return np.exp(-((xi - 1.0) ** 2))

    full = F_from_shells(hat, xs, nmax=12)
    acc = shell_term(hat, xs, -1)
    for n in range(12):
        acc = acc + shell_term(hat, xs, n)
    print("max |sum shells − F|", float(np.max(np.abs(acc - full))))
    print("F", full)
