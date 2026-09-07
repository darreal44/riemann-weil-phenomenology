# Quadrature error on [0,1]

Reference: trapezoid
n=4000 of a, ≈
−0.7007986.

    method          value        error      bound
    G₃ 1 panel    −0.700661     1.37×10⁻⁴   2.17×10⁻²
    G₃ 2 panel    −0.700797     1.12×10⁻⁶   3.39×10⁻⁴
    trap n=8      −0.702306     1.51×10⁻³   —
    trap n=32     −0.700893     9.4×10⁻⁵   —

The elementary R
is ~150–300× the
true Gauss error.
That is M=3889 vs
the sample 221,
and |a^{(6)}(ξ)|
vs max |a^{(6)}|.
The certificate
pays that factor
and still fits
the room.

Trap on the same
[0,1] at n=8 is
worse than one
Gauss panel.
G₃ is the right
rule on the
singular end;
the bound is
just loose, not
wrong.
