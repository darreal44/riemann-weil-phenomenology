# Singular values — χ₅, split after 3 hats

| μ | σ_max(Q) | σ_min(Q) | σ₁(C) | σ₂(C) | σ₃(C) | σ_min(T) | σ₁(C)/σ_min(T) |
|---|---|---|---|---|---|---|---|
| 8 | 3.64 | 9.6×10⁻⁷ | 0.74 | 0.15 | 0.0085 | 1.07 | 0.70 |
| 11 | 3.81 | 1.7×10⁻⁹ | 0.74 | 0.28 | 0.0048 | 0.67 | 1.11 |
| 16 | 4.15 | 1.2×10⁻¹³ | 0.96 | 0.069 | 0.0018 | 0.23 | 4.1 |
| 22 | 4.41 | 1×10⁻¹⁶* | 1.14 | 0.073 | 0.0011 | 0.001 | 2×10³ |

\*float64 floor; mp λ₀ = 1.2×10⁻¹⁷.

## Bulk of Q

μ=8:  3.64, 3.09, 2.95, 2.77, 2.38, 1.96, 1.04, 0.027, 9.6×10⁻⁷
μ=16: 4.15, 3.61, 3.19, 2.97, 2.66, 1.99, 1.56, 0.35, 1.2×10⁻³, 3×10⁻⁸, 1.2×10⁻¹³

Seven to eight singular values
live in [1, 4.2]. They grow
like log μ. The well is the
last one or two, separated
by four to eight orders from
the bulk. SVD of Q *does*
see the well at μ=8 and 16
(σ_min = λ₀ because Q ≻ 0).

## C versus T

σ₁(C) creeps 0.74 → 1.14
(slow, like √log μ).
σ₂, σ₃ shrink: C becomes
cleaner rank-1.
σ_min(T) collapses
1.07 → 0.67 → 0.23 → 0.001.
The ratio σ₁(C)/σ_min(T)
crosses 1 between μ=8 and 11
and is already 4 at μ=16.

That crossing is the
quantitative onset of
‖T⁻¹Cᵀ‖ > 1. After it,
a bound on the Rayleigh
quotient of T⁻¹ along the
leading right vector of C
*is* a bound on the well.
