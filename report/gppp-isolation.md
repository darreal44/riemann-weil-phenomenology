# Isolating intervals for g''' and the 4-slab trapezoid

## Roots of g'''

Sign chart on [1, 1.59]:
g'''(1.00)<0, g'''(1.03)<0,
g'''(1.04)>0, …, g'''(1.45)>0,
g'''(1.46)<0, g'''(1.59)<0.
Two simple crossings.

    [1.03, 1.04]   g'' ∈ [−0.70698, −0.70653]
    [1.45, 1.46]   g'' ∈ [−0.41077, −0.41062]

On each closed bracket g''
varies by < 5×10⁻⁴, so the
global min of g'' on [1, 1.59]
is in [−0.7070, −0.7065] and
the max in [−0.4108, −0.4106].
Hence

    |g''| ≤ 0.707
    g''  < 0

by evaluating an elementary
function at four dyadic
points plus the two ends,
once the sign chart is
granted (twenty evaluations).

## Trapezoid of a on [1, 1.59]

Four slabs, h = 0.1475.
a = ½ w g.

    y       g        w       a
    1.000  −0.2229  1.403  −0.1563
    1.148  −0.1492  1.253  −0.0935
    1.295  −0.0893  1.132  −0.0505
    1.443  −0.0401  1.030  −0.0206
    1.590   0.0000  0.942   0.0000

    trap(a) = −0.03581

Sampled |a''| ≤ 1.33 gives
a remainder ≤ 1.43×10⁻³
(n h³/12 M). Combined:

    I_{[1,1.59]} ∈ [−0.0373, −0.0344]

True −0.03508. The
positive half I_{[1.59,L]}
is still the 4-box 0.022
of `g-concavity.md`, or
a second trapezoid.

This is the finite-check
shape: four values of
θ_v, four of w, one
arithmetic trap, one
M = max|a''| still
measured rather than
majorised.
