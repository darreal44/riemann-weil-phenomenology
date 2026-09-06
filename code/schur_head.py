"""Schur identity on the hat split of Q.

    Q = [ H  C ]
        [ Cᵀ T ]     Δ = H − C T⁻¹ Cᵀ

λ₀(Q) = λ_min(Δ) exactly (block elimination). A bound on λ₀ from
a bound on H still needs a bound on ‖T⁻¹‖ and on C. This module
evaluates the identity; it does not prove the bound.
"""
from __future__ import annotations

import numpy as np


def mp_to_numpy(S):
    n = S.rows
    return np.array([[float(S[i, j]) for j in range(n)] for i in range(n)], dtype=float)


def schur_delta(Q, nhead=3):
    H = Q[:nhead, :nhead]
    C = Q[:nhead, nhead:]
    T = Q[nhead:, nhead:]
    X = np.linalg.solve(T, C.T)
    return H - C @ X


def schur_report(Q, nhead=3):
    evQ = np.linalg.eigvalsh(Q)
    Delta = schur_delta(Q, nhead=nhead)
    evD = np.linalg.eigvalsh(Delta)
    T = Q[nhead:, nhead:]
    kappa = float(np.linalg.cond(T))
    return {
        "lam0": float(evQ[0]),
        "lam_delta": float(evD[0]),
        "ratio": float(evD[0] / evQ[0]) if evQ[0] != 0 else float("nan"),
        "kappa_T": kappa,
        "nhead": nhead,
        "n": Q.shape[0],
    }
