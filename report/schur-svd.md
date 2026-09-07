# SVD of the Schur blocks — χ₅

## μ=8, dim 9

| block | σ |
|---|---|
| Q | 3.64, 3.09, 2.95, 2.77, 2.38, 1.96, … |
| H₃ | 2.56, 0.139, **5.0×10⁻⁵** |
| C (3×6) | 0.744, 0.148, 0.008 |
| T | 3.61 … 1.07 |

C is essentially rank 1
(σ₁/σ₂ = 5). The leading left
vector is spread on the three
hats, (−0.50, −0.72, −0.49),
not on e₁.

σ_max(C)/σ_min(T) = 0.70:
coupling is smaller than the
tail gap. Schur is stable.

## μ=16, dim 11

| block | σ |
|---|---|
| Q | 4.15 … (λ₀ invisible in SVD) |
| H₃ | 0.523, 0.0023, **2.3×10⁻⁶** |
| C (3×8) | 0.957, 0.069, 0.002 |
| T | 4.04 … 0.23 |

C still rank 1 (σ₁/σ₂ = 14).
Same left direction, a bit
more weight on φ₂.

σ_max(C)/σ_min(T) = 4.1:
coupling now *exceeds* the
tail gap. That is the onset
of κ(T) growth. SVD of Q
does not see the well
(σ_min(Q) in float is ~10⁻¹³
and dropped from the first
six).

## Reading

The coupling C is a single
channel from a delocalized
head mode into T. It is not
the 2-plane axis. Compressing
C to its first singular vector
gives a rank-1 Schur
correction σ₁² / (vᵀ T⁻¹ v)
of size O(1), which is exactly
the O(1)−O(1) cancel against
H₃.

A useful bound would be on
that one Rayleigh quotient
of T⁻¹, not on the whole
‖T⁻¹‖.
