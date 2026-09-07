# Cholesky of the hat Gram — χ₂₉

Q = L Lᵀ, L lower triangular.
Pivots = diag(L). det Q = (∏ L_ii)².

| μ | λ₀ | L00 | L11 | L22 | min pivot |
|---|---|---|---|---|---|
| 8 | 0.894 | 1.17 | 1.14 | 1.96 | L11=1.14 |
| 11 | 0.298 | 0.96 | 1.08 | 1.51 | L00=0.96 |
| 18 | 0.026 | 0.65 | 1.49 | 0.56 | L22=0.56 |
| 22 | 0.004 | 0.60 | 1.77 | 0.40 | L22=0.40 |
| 38 | 8e-6 | 0.33 | 1.71 | 0.071 | L22=0.071 |

The small eigenvalue is *not* a small
first pivot. Cholesky eliminates in
coordinate order (n=0, then 1, then 2).
The well appears at the **third** pivot:
after φ₀ and φ₁ are removed, φ₂ is
almost linearly dependent — L22² is
the Schur complement of the leading
2×2 inside H.

L11 stays O(1) and even grows (H11
climbs to the bulk). The tail pivots
stay in [1.4, 2.6]: same rigid T.

μ=38, first three rows:

    L00=0.33
    L10=1.02  L11=1.71
    L20=0.44  L21=−0.20  L22=0.071

That 0.071 is the visible well in
elimination order. λ₀ is smaller still
because the true ground state is a
mix of all three hats, not φ₂ alone.
