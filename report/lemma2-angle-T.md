# Angle of C(ker) with the bottom of T

cos θ_k = overlap of span{C e₁, C e₂}
with the k-th eigenvector of T.

| L | µ | cos θ₀ | cos θ₁ | λ_min(T) | (Cker·v₀)²/λ_min(T) |
|---|---|---|---|---|---|
| χ₅ | 16 | **0.033** | 0.94 | 0.24 | 2.3×10⁻⁵ |
| χ₅ | 38 | **0.000** | 0.000 | 4×10⁻⁸ | 3.4×10⁻⁹ |
| χ₃ | 16 | **0.013** | 0.37 | 6×10⁻⁴ | 6.7×10⁻⁶ |
| χ₈ | 16 | 0.84 | 0.24 | 0.90 | 4.1×10⁻² |
| χ₁₃ | 16 | 0.65 | 0.27 | 1.54 | 2.3×10⁻² |
| χ₃₁ | 38 | 0.63 | 0.15 | 0.69 | 2.6×10⁻³ |

Wide desert: C(ker) ⊥ bottom of T
(cos θ₀ ≤ 0.03). That is why
σ₁²/λ_min(T) is 10⁶ too big —
the image of ker misses the
dangerous modes.

Narrow desert: cos θ₀ ~ 0.6–0.8.
The coupling sees T as O(1),
Schur is a bounded correction,
λ₀ stays comparable to H|ker.

## Geometric Lemma 2

    λ₀
    = λ_min( H|ker − C_ker T⁻¹ C_kerᵀ )
    ≥ λ_min(H|ker) − ‖P_⊥ C|ker‖² / λ_⊥

where P_⊥ is the projection off
the bottom of T and λ_⊥ is the
next T-gap. On χ₅-16, θ₀ ≈ 87°,
the first term 3×10⁻⁶ is eaten
by the second at the same size;
what remains after that
cancellation is λ₀.

The angle is the new object.
A proof that C(ker) stays at a
definite angle from the small
modes of T would turn the
Schur into an O(1) factor
times H|ker — and H|ker is
truncated Weil on 3 hats.
Without the angle, H|ker and
the Schur cancel and the
remainder is invisible.
