# Preconditioning Q — χ₂₉ Gram

κ after P⁻¹Q (or congruence).

| μ | κ(Q) | Jacobi | block Jacobi | T⁻¹ only | exact Schur | H⁻¹ only |
|---|---|---|---|---|---|---|
| 11 | 25 | 7.4 | 2.0 | 14 | 13 | 8.7 |
| 22 | 1.8e3 | 363 | 35 | 932 | 860 | 81 |
| 38 | 9.6e5 | 5.8e4 | 868 | 5.1e5 | 4.9e5 | 2.0e3 |

Jacobi (diag scaling) buys a factor
~15. The diagonals of Q are all O(1);
they are not the source of κ.

Block Jacobi P = diag(H, T) is the
best cheap option: κ → 868 at μ=38.
Eigenvalues of P⁻¹Q cluster at 1
except two outliers 0.002 and 2.0 —
the C-coupling of the well.

T⁻¹ only (leave the head raw) barely
moves κ. The tail was already fine.

Exact Schur reduces Q to diag(Δ, T).
κ becomes max(κ(Δ), κ(T)) = κ(Δ) ≈ κ(Q)/2.
The well sits in Δ; a preconditioner
cannot remove it without removing
the observable.

H⁻¹ only (scale the 3-hat plane)
is the second-best cheap choice
(κ → 2e3): it flattens H's two
O(1) directions and leaves the
well + C.

For iterative solves of Qx = b,
use block Jacobi or the Schur
graph transform. For measuring λ₀,
do not precondition: λ₀ *is* the
ill-conditioned direction.
