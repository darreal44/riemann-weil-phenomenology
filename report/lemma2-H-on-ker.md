# H on ker ψ(0), then the Schur

H = Q restricted to hats 0,1,2.
ker = plane v₀ + √2(v₁+v₂) = 0.

| L | µ | λ_min(H) | H\|ker | vᵀHv | λ₀ | Hker/λ₀ |
|---|---|---|---|---|---|---|
| χ₅ | 16 | 2.3×10⁻⁶ | 3.2×10⁻⁶ | 3.0×10⁻⁵ | 1.6×10⁻¹² | 2×10⁶ |
| χ₅ | 38 | 1.7×10⁻⁷ | 2.4×10⁻⁷ | 9.8×10⁻⁴ | 5.3×10⁻²² | 10¹⁴ |
| χ₃ | 16 | 3.7×10⁻⁸ | 6.3×10⁻⁸ | 1.0×10⁻³ | 7.7×10⁻¹⁶ | 10⁸ |
| χ₈ | 16 | 8.1×10⁻⁵ | 1.7×10⁻⁴ | 6.2×10⁻⁴ | 1.1×10⁻⁸ | 10⁴ |
| χ₁₃ | 16 | 8.6×10⁻⁴ | 2.1×10⁻³ | 1.5×10⁻³ | 4.8×10⁻⁵ | 43 |
| χ₃₁ | 38 | 6.4×10⁻³ | 2.3×10⁻² | 6.5×10⁻³ | 3.1×10⁻⁴ | 77 |

Two steps, both large:

1. H is already nearly singular on
   ker ψ(0). That is the 3-hat
   cancellation at y=0, visible
   without the tail.
2. C T⁻¹ Cᵀ subtracts that almost
   exactly. Δ = H − C T⁻¹ Cᵀ
   drops another 10⁴–10¹⁴.

The subtraction is not a
perturbation. On a wide desert
it *is* the exponent.

## What to bound

    λ_min(H) ≥ exp(−c τγ₁)

is already false as a *tight*
stand-in for λ₀ (factor 10⁶),
but it is the first factor one
can hope to write by hand:
three hats, explicit kernel.
The second factor is
‖T⁻¹‖ · ‖C‖² on that plane —
C is the prime-side pairing of
{h₀,h₁,h₂} against {h_n, n≥3}.

A proof that only treats H
gives ell within log(Hker/λ₀)
≈ 14–32 nats of the truth on
χ₅/χ₃, and within 4 nats on
χ₁₃/χ₃₁. That is the gap
between “3-hat Lemma 2” and
Lemma 2.
