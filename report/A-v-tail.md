# Tail of A(v) on [1, L]

Integrand
    ½ w(y) (2 e^{-3y/2} − θ_v(y))
w(y) = 2 e^{-y/2} / (1−e^{-2y}).

## Split

    ∫_0^1   = −0.70065
    ∫_1^L   = −0.01850
    A_int   = −0.71930
    + CST   = −0.82789

Almost all of the integral
is on [0,1]. The tail is
2.6 % of A(v) and four
times Q(v).

## Cancellation in the tail

2 e^{-3y/2} − θ_v changes
sign at y ≈ 1.59.

    [1, 1.57]   −0.03506
    [1.57, L]   +0.01656

|2e^{-3y/2}−θ_v| ≤ 0.223
on [1, 1.57], ≤ 0.057
on [1.57, L].
w ≤ 1.40 on [1,L], ≤ 0.96
after 1.57.

Crude (no cancellation):
    ½ · 1.40 · 0.223 · 1.77 ≈ 0.28
    — useless.

After the zero:
    ½ · 0.96 · 0.057 · 1.20 ≈ 0.033
against a true +0.017.
Still twice too large
to close the ±0.003
window by itself, but
the *net* tail −0.018
is the difference of
two O(0.03) pieces.

## Hand shape

1. Compute ∫_0^1 by a
   3-point Gauss or a
   comparison with θ_v
   decreasing from 2 to
   θ_v(1)≈0.64. This
   piece is O(1) and
   must be done carefully.
2. On [1,L], keep the
   sign change: lower
   bound the negative
   half, upper bound
   the positive half.
   A 0.02 error here
   is acceptable only
   if ∫_0^1 is known
   to 0.01.

The remaining work is
[0,1], not the far tail.
