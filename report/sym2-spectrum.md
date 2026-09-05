# Eigenvalues of Sym² E₁₁ vs other Grams

Gram 2ΦᵀΦ, zeros below ~ω_max.

| | μ=22 λ0, λ1, λ2 | λ1/λ0 | μ=38 λ1/λ0 |
|---|---|---|---|
| Sym² E₁₁ | 2.1e-3, 1.34, 8.77 | 646 | 2.6e3 |
| χ₂₉ | 7.3e-3, 2.39, 3.65 | 326 | 2.0e4 |
| Δ⊗χ₄ | 1.7e-2, 3.82, 6.14 | 224 | 2.4e4 |
| 11a1 | 2.8e-10, 3.2e-5, 0.29 | 1.2e5 | 6e5 |
| Δ⊗χ₅ | 2.50, 5.44, 6.37 | 2.2 | 5 |

Sym²: one isolated small eigenvalue, then a bulk starting at O(1).
Same pattern as χ₂₉ / Δ⊗χ₄. 11a1 is much deeper (larger desert).
Δ⊗χ₅ has no gap.

## Weight 14

No list in the repo. S₁₄(SL₂(ℤ)) is 1-dimensional; first
zero expected in the Delta range (γ₁ ≳ 8), so a Gram at
μ=22–38 would likely be indefinite like Δ itself (γ₁=9.22).
That would not be a “weight 14 mode.” It would be the desert
artifact. Harvest `mfinit([1,14])` + `lfunzeros` only if we
want γ₁; it will not produce a cleaner singlet than Sym².
