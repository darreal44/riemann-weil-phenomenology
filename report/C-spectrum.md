# Spectrum of C — χ₅

C is 3 × (N−3). Its spectrum is
that of the 3×3 CCᵀ (or the
three nonzero eigenvalues of
CᵀC).

## Eigenvalues of CCᵀ

| μ | λ₁(CCᵀ)=σ₁² | λ₂ | λ₃ |
|---|---|---|---|
| 8 | 0.554 | 0.022 | 7×10⁻⁵ |
| 16 | 0.915 | 0.0048 | 3×10⁻⁶ |
| 22 | 1.307 | 0.0053 | 1×10⁻⁶ |

One O(1) channel, two
negligible. Rank-1 is not
a slogan.

## Left vectors (head φ₀,φ₁,φ₂)

| μ | u₀ | u₁ |
|---|---|---|
| 8 | (−0.50, −0.72, −0.49) | (−0.32, −0.38, 0.87) |
| 16 | (−0.42, −0.61, −0.67) | (−0.49, −0.47, 0.74) |
| 22 | (−0.37, −0.56, −0.74) | (−0.54, −0.52, 0.66) |

u₀ drifts toward φ₂. It is
never e₁. The 2-plane axis
and the Schur channel are
different directions.

## Right vectors (tail)

v₀ peaks on the first tail
hat: φ₃ at μ=8 and 22, φ₄
at μ=16. Weight 0.70–0.93
on that one mode, the rest
scattered.

## The Rayleigh that matters

    ρ = v₀ᵀ T⁻¹ v₀

| μ | ρ | σ₁² ρ = ‖CTCᵀ‖ along u₀ |
|---|---|---|
| 8 | 0.46 | 0.26 |
| 16 | 0.57 | 0.52 |
| 22 | 0.44 | 0.57 |

ρ stays O(1) while σ_min(T)
falls 1.07 → 0.001. So v₀
is *not* the collapsing
mode of T. The dangerous
direction of T⁻¹ is
orthogonal to the channel.

A bound on ρ, not on ‖T⁻¹‖,
would control the Schur
correction. Empirically
ρ ∈ (0.4, 0.6) on these
three windows.
