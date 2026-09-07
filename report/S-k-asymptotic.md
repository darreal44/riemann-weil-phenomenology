# Asymptotic error of S_k

D₂(y) = y^{-1} + R(y)
with
R
bounded
on
(0,L]
(because
1−e^{−2y}=2y−2y²+…,
the
regular
part
absorbs
the
rest).
∫_0^L y^{−1} sin(ω_k y) dy
= Si(ω_k L) → π/2.
π/2
≈1.5708.
Measured
S_k
sits
at
1.55.
The
gap
is
∫ R sin
plus
the
difference
D₂−1/y.

Endpoint
at
L,
one
integration
by
parts:

    ∫ R sin(ω y) dy
      = O(1/ω)
      = O(1/k),
    1/ω
      = L/(2π k)
      ≈0.175/k,
    D₂(L)·L/(2π)
      ≈0.074
    so
    the
    oscillating
    remainder
    is
    O(0.07/k).

Hence
S_k = S_∞ + O(1/k)
with
S_∞
near
π/2
adjusted
by
∫R.
Then
n(S_n−S_m)
= n O(k/(n m))
= O(k/m)
if
S
differs
by
O(|n−m| / n²)
from
a
1/k
expansion
— check
the
sign
of
the
O(1/k)
before
quoting
a
constant.

This
is
the
rate
the
table
wanted.
It
is
not
yet
a
closed
S_∞
or
a
proved
O(1/k)
constant.
Si
and
the
expansion
of
D₂
at
0
are
the
tools.

Not
RH.
