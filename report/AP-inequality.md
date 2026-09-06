# The inequality A − P ≻ 0 on the 2-plane

Split of Q = A − P on χ₅
(A = archimedean + constant,
P = prime-power sum, no zeros).
2-plane = span{φ₀, φ₁}, not the
rotated {f₁,f₂} of Lemma 2.

## Separate pieces are indefinite

| μ | eig A | eig P | eig(A−P) | det(A−P) |
|---|---|---|---|---|
| 8 | −1.04, 1.17 | −1.13, 0.83 | **7.9×10⁻⁴**, 0.43 | 3.4×10⁻⁴ |
| 16 | −1.44, 0.88 | −1.50, 0.65 | **5.0×10⁻⁵**, 0.29 | 1.4×10⁻⁵ |
| 22 | −1.59, 0.76 | −1.65, 0.54 | **1.2×10⁻⁴**, 0.28 | 3.4×10⁻⁵ |

A ⊀ 0 and P ⊀ 0 on the same
plane. The negative direction
of A is almost the negative
direction of P. Their
difference is positive.

## Alignment

    cos(A,P) = 0.965 → 0.987
    angle     15.2° → 9.3°

Two O(1) forms, nine degrees
apart. The residual Frobenius
is 0.43 → 0.28, almost equal
to λ_max(A−P). All the mass
of A−P sits on one axis; the
well is the thin axis.

## Why generic bounds miss the sign

- Weyl: tr(A−P) = 0.43, 0.29, 0.28 > 0
  only sees λ_max.
- Gershgorin on the raw hats
  fails the same way as in
  `det-AP-remaining.md`.
- ‖A−P‖ ≤ ‖A‖+‖P‖ is the
  wrong side (and on the
  *full* matrix ‖A−P‖ > ‖A‖:
  the tail does not cancel).

The sign of λ_min is the sign
of det(A−P). That determinant
is the area of two residuals
of size ~0.1 that are almost
parallel.

## What would prove it

A comparison of quadratic
forms that keeps the angle
θ(A,P) < 20° and ‖A‖, ‖P‖
comparable, plus a lower
bound on the *skew* of the
two negative axes — or a
direct estimate of det in
the {f₁,f₂} frame, where
H₁₁ is 10⁻⁴ and H₁₂ is
10⁻³ (`det-AP-remaining.md`).

No zeros enter. The inequality
is finite and unconditional.
It is also the whole gap:
everything after Schur reduces
to this 2×2.
