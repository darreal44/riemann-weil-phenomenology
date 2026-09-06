# Cholesky pivoting — χ₂₉ Gram

Three elimination orders.

| μ | λ₀ | natural L22 | min-pivot first | hat first | max-pivot first | growth |
|---|---|---|---|---|---|---|
| 11 | 0.30 | 1.51 | 0.96 | n=0 | 2.58 | 1.00 |
| 22 | 4e-3 | 0.40 | 0.60 | n=0 | 2.66 | 1.00 |
| 38 | 8e-6 | 0.071 | 0.33 | n=0 | 2.49 | 0.97 |

Growth = max|L| / √max(diag Q) ≤ 1.
No amplification. Pivoting is optional
for stability.

Min-diagonal pivoting always starts
at n=0: the smallest *diagonal* of Q
is H00. That first pivot is √H00,
still 10⁴ × λ₀ at μ=38.

The well is not a small Q_nn. It is
a near-dependence among {φ₀,φ₁,φ₂}.
No permutation of coordinates puts
λ₀ on the first pivot.

μ=38 min-order: 0, 2, 1, 3, 4, …
second pivot 0.21 (after swapping
in φ₂), still ≫ λ₀. Max-order starts
in the bulk (n=10,17,12) with pivots
≈ 2.5, the Laplace ceiling.
