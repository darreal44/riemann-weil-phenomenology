# LU of the hat Gram — χ₂₉

Q is SPD, so LU without pivoting is
Cholesky in disguise: U_ii = L_ii²
to 10⁻¹³.

| μ | λ₀ | U00 | U11 | U22 | min|U_ii| | growth | min after partial pivot |
|---|---|---|---|---|---|---|---|
| 11 | 0.30 | 0.91 | 1.16 | 2.28 | 0.91 | 0.99 | 0.91 |
| 22 | 4e-3 | 0.35 | 3.13 | 0.16 | 0.16 | 1.00 | 0.53 |
| 38 | 8e-6 | 0.11 | 2.92 | 0.0051 | 0.0051 | 0.94 | 0.046 |

U22 at μ=38 is L22² = 0.071² = 0.005.
Same well, squared, in elimination
order n=0,1,2.

Partial pivoting does *not* help
expose λ₀. It starts at n=24 (largest
column) and the smallest |U_ii|
becomes 0.046 — eight times *larger*
than the unpivoted U22. The well is
hidden, not found.

Growth ≤ 1.03 either way. Residuals
‖LU−Q‖ and ‖PLU−Q‖ are 3–4×10⁻¹⁵.

LU and Cholesky tell the same story
on this matrix. Pivoting is a
stability tool, not a well detector.
