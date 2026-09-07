# Schur complement, for this Q

Split the hat Gram (or the prime-side Q)
after the first three hats:

        [ H   C ]
    Q = [ Cᵀ  T ]

H is 3×3 (n=0,1,2), T is the tail
(n≥3), C the rectangle that couples
them.

## Completing the square

For a vector (u, w):

    (u,w) Q (u,w) = uᵀ H u + 2 uᵀ C w + wᵀ T w.

If T > 0 one can minimise in w at fixed u:

    w⋆ = − T⁻¹ Cᵀ u

and the minimum is

    uᵀ (H − C T⁻¹ Cᵀ) u.

The matrix

    Δ := H − C T⁻¹ Cᵀ

is the Schur complement of T in Q.

## Exact dictionary

- T > 0 and Δ > 0  ⇔  Q > 0.
- λ₀(Q) = min_{u≠0} uᵀ Δ u / (uᵀu + ‖T⁻¹ Cᵀ u‖²)
  so λ₀(Q) ≤ λ_min(Δ), with equality
  when the ground state already sits
  on the graph w = −T⁻¹ Cᵀ u.
- On χ₂₉ we measured λ_min(Δ)/λ₀(Q) = 1.006–1.012.
  The well *is* Δ.

## What each piece does here

- H carries one collapsing eigenvalue,
  equal to uᵀHu on the 2-level IR vector.
  Independent of N.
- T is a rigid bulk, spectrum in [1, 7.5],
  no well.
- C stays O(1), strongest on n=3–6.
- S := C T⁻¹ Cᵀ is therefore O(10⁻²) and
  almost constant. The well is H falling
  through a fixed S:

        Δ(u,u) = uᵀHu − uᵀSu  →  λ₀.

The operator-norm test ‖S‖₂ < λ_min(H)
fails at μ≈16 because S has mass off u.
The quadratic form on u stays positive.

## Why not invert λ_min(T)

uᵀSu = Σ_k (u · C w_k)² / λ_k(T)
is carried by mid-spectrum modes of T
(λ≈4–5), not by λ_min(T). A bound that
only uses the floor of T aims at the
wrong end.
