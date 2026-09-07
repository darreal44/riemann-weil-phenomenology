# χ₅: lowering Hankel cannot take the class at h=2

Judged (#59):
    λ_H=0.053  ‖C‖_F=0.417  qmin=2.228
    t₂=0.490   off=2.417    δ=−0.189

Schur:
    β = λ_H − ‖C‖²/δ
    needs  ‖C‖²/λ_H < δ ≤ qmin

    ‖C‖²/λ_H = 3.28 > 2.23 = qmin

Even off=0 (Hankel=R=T₂=0)
gives β=0.053−0.174/2.23
= −0.025 < 0.
The tail operator
is not the
obstruction.
C is too large
for this H.

HEAD=3,4 with
‖Θ‖=1 (same
Q_nm):

    h  λ_H    qmin   ‖C‖    δ      β
    2  0.053  2.228  0.417 −0.19   —
    3  0.049  2.612  0.600 +0.30  −1.13
    4  0.046  2.612  0.483 +0.36  −0.61

λ_H does not
rise (the well
is already in
the 2×2). C
does not fall
enough. This
split will not
take χ₅.

A take would
need a sharper
C (most of the
Frobenius is
overcount) or
a different
ONB, not a
smaller Hilbert
constant.

Executed
(`ql-schur-neumann.md`):
Neumann T^{-1}≤
D^{-1}/(1−ρ),
S_lo(χ₅)=+0.029.
The Frobenius
majorant was the
obstruction, not
C. χ₃ still
S_lo<0. SOS
remains for the
odd χ(2)=−1.
