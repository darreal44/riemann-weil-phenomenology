# g is concave on [1, y*] — the triangle goes the wrong way

    g(y) = 2 e^{-3y/2} − θ_v(y)
    y* ≈ 1.590,   g(1) = −0.223,   g(y*) = 0

On [1, y*] (sampled 400
nodes, Δy≈0.0015):

    g'  ∈ (0.24, 0.55)     always +
    g'' ∈ (−0.71, −0.41)   always −

g is *concave*. |g| = −g
is *convex*. The chord
from (1, g(1)) to (y*, 0)
lies *below* g (g − chord
∈ [0, 0.022]). So the
triangle of `A-v-tail-comparison.md`
is a *lower* bound on |g|,
not an upper bound. It
cannot certify I₋.

## What does certify

The box |g| ≤ |g(1)|:

    |I₋| ≤ ½ w(1) · 0.223 · 0.590 = 0.092

A 4-piece box (max |g| on
each slab, w at the left
endpoint):

    |I₋| ≤ 0.047
    I₊  ≤ 0.022
    I_{[1,L]} ∈ [−0.047, 0.022]

True −0.0185. Still three
times the ±0.003 window.

## A remainder that would close it

Trapezoid on n equal slabs
of [1, y*], with
|g''| ≤ 0.71:

    error on one slab of
    length h ≤ (h³/12)·0.71·½ w(1)

n=4, h≈0.147 ⇒ per slab
4.5×10⁻⁴, total ~2×10⁻³.
That *would* sit in the
window, provided the
trapezoid values of g
(four sines) are accepted
as hand numbers and
|g''|≤0.71 is proved
(θ_v'' is a trig
polynomial of order 4π/L,
boundable).

The sampled g''<0 is not
that proof. Writing
θ_v'' from the six
kernels and majorising
it on [1, 1.59] is the
next finite calculation.
