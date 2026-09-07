# Gauss–Seidel preconditioner — χ₂₉ Gram

P_GS = D+L, P_SGS = (D+L) D⁻¹ (D+Lᵀ),
SSOR at ω=1.2.

| μ | κ(Q) | κ_GS | ρ_GS | κ_SGS | ρ_SGS | κ_SSOR |
|---|---|---|---|---|---|---|
| 11 | 25 | 2.8 | 0.62 | 2.3 | 0.56 | 2.3 |
| 22 | 1.8e3 | 95 | 0.989 | 86 | 0.988 | 92 |
| 38 | 9.6e5 | 1.1e4 | 0.9999 | 9.9e3 | 0.9999 | 1.1e4 |

GS buys a factor ~85 on κ at μ=38,
better than Jacobi (5.8e4) but far
behind block Jacobi (868).

ρ → 1 because of the well:
P⁻¹Q has one eigenvalue ~10⁻⁴,
so the iteration matrix has
ρ ≥ |1−10⁻⁴| ≈ 1. Symmetric GS
and SSOR do not move that mode.

GS is a smoother for the bulk
(other eigenvalues of P⁻¹Q sit
in [0.45, 1.11]). It is not a
solver for λ₀.

Use it inside a multigrid / CG
on Qx=b. Do not use it to read
the well.
