# The 2×2 on the raised-cosine plane

Orthonormal frame of ker ψ(0) inside
the first three hats, independent of χ
and of µ:

    e₁ = ( √2, −1,  0 ) / √3
    e₂ = ( −√2, −2,  3 ) / √15

(e₂ is hat-2 after Gram–Schmidt against
e₁ and against u ∥ ψ(0).)

    H = ( ⟨Q eᵢ, eⱼ⟩ )_{i,j=1,2}
      = Arch − Σ_{n≤µ} χ(n) Λ(n) n^{-1/2} Θ(log n)

Arch_{ij} is the 10-term Laplace series
of `lemma2-arch-f1.md` (same kernel, two
modes). Θ_{ij}(y) is the 2×2 of lag
kernels built from `th_at` as for θ_{f₁}.

## Numbers at µ=16, three hats only

| χ | H₁₁ | H₁₂ | H₂₂ | λ_min(H) | λ_min(Q|_{3}) |
|---|---|---|---|---|---|
| χ₅ | 9.3×10⁻⁵ | −5.9×10⁻⁴ | 3.9×10⁻³ | 3.2×10⁻⁶ | 2.3×10⁻⁶ |
| χ₃ | 2.2×10⁻⁴ | −1.4×10⁻³ | 8.8×10⁻³ | 6.3×10⁻⁸ | 3.7×10⁻⁸ |
| χ₈ | 1.7×10⁻³ | −4.2×10⁻² | 1.14 | 1.7×10⁻⁴ | 8.1×10⁻⁵ |
| χ₁₃ | 0.212 | 0.670 | 2.14 | 2.1×10⁻³ | 8.6×10⁻⁴ |

λ_min(H) sits 1.4–2.4 above the full
3×3: the Schur tail of hat-space
outside these two directions is
comparable to λ_min itself, not 10¹⁴.
The 10⁴–10¹⁴ factor was the *third
eigenvalue of the 3×3 versus λ_min*,
not the distance from H to Q|_{3}.

## What to prove

    H₁₁ > 0  and  det H > 0.

H₁₁ = Q(f₁,f₁) is one number:
Arch(f₁) minus nine prime-power
terms, all elementary. On χ₅ it
is 9×10⁻⁵; Arch and Primes each
O(1), cancelled to 10⁻⁴.

A bound that ignores H₁₂ fails:
|H₁₂| ≫ H₁₁ on χ₅ and χ₃, so
λ_min ≈ det H / H₂₂, not H₁₁.
The inequality is the determinant,
not the (1,1) entry.

No estimate in this note crosses
from “written” to “≥ c > 0
independent of a computer”. The
object is the 2×2 above.
