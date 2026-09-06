"""Edge value of the ground state of a hat-basis matrix Q.

    ψ(0) = L^{−1/2} (v₀ + √2 ∑_{n≥1} v_n)
    ell  = −ln|λ₀|
    edge = −2 ln|ψ(0)|
    R    = ell − edge

The measured statement is R = O(1) and edge/ell ∈ [0.82, 0.98]
on the windows of `report/edge-value-scan.md`. That is not a proof
of −ln|ψ(0)|_min = ℓ/2 + O(1) as an extremal lemma.
"""
from __future__ import annotations

import math

import numpy as np


def from_Q(Q, mu):
    L = math.log(float(mu))
    ev, evec = np.linalg.eigh(Q)
    lam0 = float(ev[0])
    v = evec[:, 0]
    psi0 = (v[0] + math.sqrt(2.0) * float(v[1:].sum())) / math.sqrt(L)
    ell = -math.log(abs(lam0)) if lam0 != 0 else float("inf")
    edge = -2.0 * math.log(abs(psi0)) if psi0 != 0 else float("inf")
    return {
        "lam0": lam0,
        "ell": ell,
        "psi0": float(psi0),
        "edge": edge,
        "R": ell - edge,
        "v": v,
    }
