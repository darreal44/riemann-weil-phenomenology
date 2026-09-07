# Spectrum of P — primes only, no zeros

P_{ij} = Σ_{n≤μ} χ(n) Λ(n) n^{-1/2} θ_{ij}(log n).

## 2-plane, μ=16

| χ | eig P | eig A | cos(v_min) | ‖P‖_F | ‖A‖_F | ‖H‖_F |
|---|---|---|---|---|---|---|
| χ₅ | −1.183, 0.973 | −1.182, 0.977 | 1.000 | 1.532 | 1.534 | 0.0039 |
| χ₃ | −0.690, 0.476 | −0.688, 0.483 | 1.000 | 0.838 | 0.841 | 0.0090 |
| χ₄ | −0.414, 0.675 | −0.401, 0.771 | 1.000 | 0.792 | 0.869 | 0.109 |
| χ₈ | −0.938, 0.526 | −0.712, 1.447 | 0.967 | 1.075 | 1.613 | 1.15 |
| χ₁₃ | −0.421, −0.229 | −0.227, 1.932 | 0.028 | 0.480 | 1.945 | 2.35 |

P is indefinite (one negative
eigenvalue) on every thin
character. A is the same
indefinite form, aligned with
P to 10⁻³ on χ₅ / χ₃
(cos = 1 on the negative
axis). H = A−P is then the
*residual* of two almost
equal indefinite matrices.

On χ₁₃ the desert is large,
P is small and *negative
definite* on the 2-plane,
A is not: cos ≈ 0. The
mismatch *is* H, O(1), easy
det. The hard case is the
aligned pair.

## Full hats, χ₅ μ=16 N=9

eig P =

    −1.88, −1.50, −1.22, −0.76, −0.22,
     0.10,  0.84,  1.43,  2.18

tr P = −1.02. Full rank in
practice (9 of 9 above 0.05).
Not a one-prime update.
κ ~ 10 (bulk, no well).

Largest terms: n=2,3,7,11,13
(‖w θ‖_F = 1.8, 2.1, 1.6, 1.1, 0.8).
n=16 sits at y=L and vanishes.

P does not carry the well.
The well is the misalignment
A−P on one 2-plane direction,
O(10⁻³) on χ₅, invisible in
the spectrum of P alone.
