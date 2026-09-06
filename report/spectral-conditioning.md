# Spectral conditioning — χ₂₉ Gram

κ(M) = λ_max(M)/λ_min(M).

| μ | L | λ₀ | λ₁ | λ_max | κ(Q) | λ₁/λ₀ | κ(H) | κ(T) | κ(Δ) |
|---|---|---|---|---|---|---|---|---|---|
| 11 | 2.40 | 0.298 | 1.75 | 7.44 | 25 | 6 | 12 | 2.9 | 13 |
| 22 | 3.09 | 4.1e-3 | 1.21 | 7.37 | 1.8e3 | 295 | 99 | 4.0 | 860 |
| 38 | 3.64 | 7.9e-6 | 0.12 | 7.52 | 9.6e5 | 1.6e4 | 3.1e3 | 7.3 | 4.9e5 |

λ_max is pinned at 7.5 (Laplace bulk
of the window). So

    κ(Q) ∼ 7.5 / λ₀.

The whole blow-up is the well.
κ(T) stays O(1): the tail is never
the source of ill-conditioning.

λ₁ stays O(1) down to μ=22 then
drops, but remains 10⁴ × λ₀ at
μ=38. The well is simple: one
isolated eigenvalue.

κ(Δ) ≈ κ(Q)/2. The 3×3 Schur
inherits the well and an O(1)
ceiling, so it is the smallest
matrix that carries the full
condition number.

float64: κ=10⁶ leaves ~10 digits
on λ₀. The next wall is not κ
but the T=320 truncation (9 %
on λ₀ at μ=38).
