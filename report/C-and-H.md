# Coupling C and head H — χ₂₉ Gram

Q = [ H C ; Cᵀ T ], H is 3×3.

| μ | λ_min(H) | λ_max(H) | det H | ‖C‖₂ | uᵀHu | uᵀSu |
|---|---|---|---|---|---|---|
| 8 | 0.950 | 4.05 | 6.79 | 0.68 | 0.951 | 0.045 |
| 11 | 0.338 | 4.05 | 2.43 | 0.52 | 0.338 | 0.037 |
| 18 | 0.056 | 3.45 | 0.29 | 0.80 | 0.056 | 0.030 |
| 38 | 0.0013 | 3.99 | 0.002 | 1.26 | 0.0017 | 0.0017 |

H has one collapsing eigenvalue, two
O(1) ones. That collapsing direction
*is* u (the 2-level IR vector):
λ_min(H) = uᵀHu to three digits.

C does not collapse. ‖C‖₂ stays 0.5–1.3.
Strongest columns are the first tail
hats (n=3,4,5,6), not the far UV.

So S = C T⁻¹ Cᵀ stays O(10⁻²) while H
on u falls through it. The well is
λ_min(H(μ)) − O(1)·‖C‖² / λ_mid(T).
