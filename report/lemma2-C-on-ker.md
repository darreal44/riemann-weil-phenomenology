# C restricted to ker ψ(0)

C : hats 0,1,2 → tail. σ(C|ker)
= singular values of that 2×(N−3)
map.

| L | µ | ‖C‖_F | σ₁(C\|ker) | σ₂ | σ₁²/λ_min(T) | H\|ker | λ₀ |
|---|---|---|---|---|---|---|---|
| χ₅ | 16 | 0.95 | **0.082** | 0.003 | 0.028 | 3.2×10⁻⁶ | 1.6×10⁻¹² |
| χ₅ | 38 | 0.82 | **0.069** | 0.001 | 10⁵ | 2.4×10⁻⁷ | 5×10⁻²² |
| χ₃ | 16 | 0.92 | **0.147** | 0.0002 | 35 | 6.3×10⁻⁸ | 8×10⁻¹⁶ |
| χ₈ | 16 | 0.89 | 0.227 | 0.020 | 0.057 | 1.7×10⁻⁴ | 1.1×10⁻⁸ |
| χ₁₃ | 16 | 1.29 | 0.474 | 0.049 | 0.15 | 2.1×10⁻³ | 4.8×10⁻⁵ |
| χ₃₁ | 38 | 0.54 | 0.112 | 0.028 | 0.018 | 2.3×10⁻² | 3.1×10⁻⁴ |

C on ker is 5–15 times smaller
than ‖C‖_F, not 10⁶. The crude
bound σ₁²/λ_min(T) is still
useless when T itself is nearly
singular (χ₅-38, χ₃-16).

On a well-conditioned T
(χ₅-16, χ₈, χ₁₃, χ₃₁) that
bound is 0.02–0.15, while
H|ker is 10⁻⁶ to 10⁻². The
Schur correction on ker is
*smaller* than this bound
because C(ker) is not aligned
with the bottom of T.

## Three numbers that are not the same

    ‖C‖_F           ~ 1
    σ₁(C|ker)       ~ 0.07–0.47
    Corr|ker        ~ H|ker ~ 10⁻⁶ … 10⁻²

Lemma 2 after the 3-hat
reduction is: bound
λ_min(H|ker − (C T⁻¹ Cᵀ)|ker)
from below. The first term
is Arch−Primes. The second
is this restricted coupling.
Neither is ‖C‖_F.
