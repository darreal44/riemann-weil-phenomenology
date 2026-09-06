# Leibniz of a^{(6)} at the max

    a = ½ w g
    a^{(6)} = ½ ∑_{k=0}^{6} C(6,k) w^{(k)} g^{(6−k)}

At y=1/2 (the Chebyshev
max, a^{(6)}≈−320.63):

    w, w', w'' analytic
    2.464, −4.100, 15.897

    w^{(3)} FD stable  −96
    w^{(4)} FD ~ 770
    w^{(6)} not stable
    (10^4–10^6 with h)

g^{(n)} by FD is stable
through n=4 (20.51) and
breaks at n=6.

So the large k terms of
Leibniz cannot be summed
from differences. The
number that does not
move is the Chebyshev
derivative of a itself
(`a6-chebyshev.md`):

    a^{(6)}(1/2) = −320.63
    a^{(6)}(0.113) = +11.18
    a^{(6)}(0.887) = +47.49

A closed recurrence for
w^{(n)} (logarithmic
derivative r=−1/2−2e/(1−e),
e=e^{−2y}) would make
Leibniz a proof. It is
not written. Until then
M=325 is a Chebyshev
consensus on a C^∞
function whose series
coeffs die at degree 12,
not a termwise bound.
