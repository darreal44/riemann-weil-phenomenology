# Monte Carlo on Q

Q at these windows is 9×9 and already
diagonalized. Haar sampling does not
replace that. It answers a different
question: how large is the near-kernel
as a subset of the sphere?

## Haar, 8000 draws, µ=16 NB=8

| L | λ₀ | P(Q<0) | P(Q<10 λ₀) | median Q | 1 % |
|---|---|---|---|---|---|
| χ₅ | 1.6×10⁻¹² | 0 | 0 | 1.73 | 0.34 |
| χ₃ | 7.7×10⁻¹⁶ | 0 | 0 | 1.29 | 0.20 |
| χ₇ | 1.3×10⁻⁸ | 0 | 0 | 2.01 | 0.58 |

Zero hits. The ground state is a needle
of solid angle

    vol ~ ∏_{i≥1} √(ε / λ_i)   on S^{8}.

λ₁/λ₀ ∼ 10⁴–10⁶, so the set {Q < 10 λ₀}
has measure ≲ 10⁻¹⁰. 8000 Haar points
never see it. Positivity on a random
test function is cheap and uninformative.

## Where MC would pay

1. **Importance sampling on the 2–4 hat
   plane.** Draw v = a v̂₂ + b v̂_⊥ with
   a concentrated, not Haar. That is
   just the 2×2 we already have.
2. **2-adic campaign, dim 512×1700.**
   Hutchinson / Nyström / random
   probing of the trace and the
   smallest Ritz values. There the
   matrix is too big to factor at
   every Λ.
3. **Random characters at fixed µ.**
   Monte Carlo over χ, not over v:
   the law of N_eff(q) and of C(χ).
   That is a survey, not an integral.

The integrals that build Q (archimedean
weight, Hadamard finite part) are
one-dimensional and already done by
mp.quad. Replacing them by MC adds
variance and no new digit.

Haar-on-v is the wrong measure for the
lemma. The lemma lives on a 2-to-4
dimensional subset that eigensolve
finds in one shot.
