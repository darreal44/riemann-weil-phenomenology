# Kernel of T — χ₅ μ=16 N=12

T = Q on hats φ₃…φ₁₂ (10×10).

## Lags

    k   mean T_{i,i+k}   std
    0   +2.66            0.82
    1   +0.07            0.49
    2   −0.01            0.27
    3   −0.03            0.14
    ≥4  O(0.05)          shrinking

Mean off-diagonal dies by
lag 2. The *scatter* at
lag 1 is 0.49 — larger
than the mean. Signs
oscillate: 0.94, −0.23,
−0.44, 0.66, −0.53, …

## Not Toeplitz

‖T − Toeplitz(mean lags)‖ / ‖T‖
= 0.39. The diagonal itself
is not flat:

    3.01, 2.30, 2.84, 0.56,
    3.32, 3.05, 2.03, 2.83,
    3.05, 3.63

The 0.56 is the collapsing
Slepian sitting on φ₆
(`T-tail-modes.md`). A
translation-invariant
kernel cannot produce that
dip.

## What the kernel is

θ_{nm}(y) of two high hats,
integrated against the
archimedean measure minus
the prime measure, y ∈ [0,L].
High n,m oscillate at
2πn/L. Their Gram is a
Dirichlet kernel of width
~1 in hat index, plus a
diagonal from the constant
term F₀=2 when n=m.

So: a fat diagonal O(2–3),
a nearest-neighbour of
random sign O(0.5), then
noise O(0.1). Short range
in hat number, not a
sinc of (n−m) with a
stable phase.

That is why MP failed:
iid columns would give
a stable off-diagonal
variance and a flat
diagonal. Here the
diagonal *is* the kernel.
