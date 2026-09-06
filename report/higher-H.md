# Higher hats n=3,4,5 (χ₅ μ=16)

    n     A_nn     P_nn     H_nn
    0    −1.383   −1.475    0.092
    1     0.820    0.627    0.194
    2     1.405    1.166    0.239
    3     1.771   −1.242    3.013
    4     2.038   −0.264    2.302
    5     2.249   −0.594    2.843

For n≥3, P_nn stays
negative. A_nn grows
slowly (~2). H_nn stays
O(1) bulk. No second
well on the diagonal.

Coupling head→tail
C = H[{0,1,2},{3,4,5}]:

        φ₃    φ₄    φ₅
    φ₀  0.08  0.34  0.16
    φ₁  0.11  0.49  0.22
    φ₂  0.04  0.56  0.22

    ‖C‖_F = 0.90
    spec(T) = {1.56, 2.93, 3.67}
    ‖C‖² / λ_min(T) = 0.52

That Schur majorant is
100× Q(v). It is a bound
on the *whole* 3-plane,
not on v. Q(v) padded
by zeros in φ₃,φ₄,φ₅
is still 0.00551.

Higher-order terms are
bulk walls plus O(0.5)
mixers. They do not
build a second well and
they do not flip the
sign of this v. A proof
that uses Schur on the
whole tail needs a
better constant than
‖C‖_F²/λ_min(T).
