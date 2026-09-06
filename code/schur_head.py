"""Schur complement of the hat split of Q.

    Q = [ H  C ]
        [ Cᵀ T ]     Δ = H − C T⁻¹ Cᵀ

If T > 0 then Q > 0 ⇔ Δ > 0 (completing the square). Variationally
λ₀(Q) ≤ λ_min(Δ), with equality when the ground state lies on the
graph v = −T⁻¹ Cᵀ u (measured to 0.4%). A lower bound on λ₀ from
a lower bound on H still needs ‖C T⁻¹ Cᵀ‖ ≤ λ_min(H) − ε.
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
    C = Q[:nhead, nhead:]
    evT = np.linalg.eigvalsh(T)
    kappa = float(np.linalg.cond(T))
    sigma = float(np.linalg.norm(np.linalg.solve(T, C.T), 2))
    return {
        "lam0": float(evQ[0]),
        "lam_delta": float(evD[0]),
        "lam_T": float(evT[0]),
        "ratio": float(evD[0] / evQ[0]) if evQ[0] != 0 else float("nan"),
        "kappa_T": kappa,
        "sigma": sigma,
        "nhead": nhead,
        "n": Q.shape[0],
    }
