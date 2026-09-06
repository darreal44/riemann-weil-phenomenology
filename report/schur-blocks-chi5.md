# Schur blocks on χ₅ — H, C, T, Δ

Q split after the first three hats
(not the 2-plane {e₁,e₂}; that plane
sits *inside* the 3-hat head).

    Δ = H₃ − C T⁻¹ Cᵀ
    λ₀(Q) = λ_min(Δ)   (identity)

## Where float64 still sees the well

| μ | N | λ₀(Q) mp | λ_min(Δ) | ratio | λ_min(T) | κ(T) | ‖T⁻¹Cᵀ‖ | ‖CTCᵀ‖ |
|---|---|---|---|---|---|---|---|---|
| 8 | 9 | 9.6×10⁻⁷ | 9.6×10⁻⁷ | 1.000 | 1.07 | 3.4 | 0.36 | 0.26 |
| 16 | 11 | 1.2×10⁻¹³ | 1.2×10⁻¹³ | 0.997 | 0.23 | 18 | 0.90 | 0.52 |

Identity holds. T is still
O(1) and well-conditioned.

## Where float64 dies

| μ | λ₀(Q) mp | float Δ | κ(T) | ‖T⁻¹Cᵀ‖ |
|---|---|---|---|---|
| 22 | 1.8×10⁻¹⁶ | noise | 4×10³ | 1.27 |
| 30 | 2.8×10⁻²⁰ | noise | 1.6×10⁶ | 1.87 |
| 38 | 5.4×10⁻²² | noise | 1.2×10⁸ | 2.43 |

κ(T) tracks 1/λ_min(T).
λ_min(T) is itself falling
toward the well: the tail is
not a gap. That is why
‖T⁻¹‖ cannot be bounded
independently of λ₀.

‖CTCᵀ‖ stays O(1) (0.26–0.8).
H₃ is also O(1). Their
difference is 10⁻¹³. The
Schur subtraction is an
O(1)−O(1) cancel to the
well, same shape as A−P
on the 2-plane, one
dimension up.

A bound on λ_min(H_{2-plane})
does not enter this table:
the 3-hat H₃ is not that
2×2, and T has no gap.
