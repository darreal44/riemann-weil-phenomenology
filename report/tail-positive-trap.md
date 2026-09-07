# Trapezoid of a on [y*, L]

y* = 1.59, L = log 16 ≈ 2.773,
length 1.183. Four slabs,
h = 0.2956.

    y       g        a
    1.590   0.000    0.000
    1.886   0.049    0.0196
    2.181   0.054    0.0184
    2.477   0.039    0.0114
    2.773   0.031    0.0078

    trap(a) = +0.01572
    true    = +0.01658

Sampled |a''| ≤ 0.344
⇒ remainder ≤ 2.97×10⁻³.
So

    I_{[1.59,L]} ∈ [0.0128, 0.0187]

g'' on this half is *not*
signed: it runs
[−0.55, +0.15], with
g''' zeros at 1.83 and
2.57. No concavity to
lean on. The box of
`g-concavity.md` (I₊≤0.022)
is the comparison bound;
the trapezoid is tighter
and still measured-M.

## Both halves together

    I_{[1,1.59]} ∈ [−0.0373, −0.0344]
    I_{[1.59,L]} ∈ [ 0.0128,  0.0187]
    I_{[1,L]}    ∈ [−0.0245, −0.0157]

True −0.0185. Width 0.009,
three times the ±0.003
A-window. Halving h
(eight slabs) would cut
the h³ remainder by 8
and close the window,
at the price of five
more evaluations of θ_v.

CST + G₃ + this interval:

    A ∈ −0.10859 − 0.70066 + [−0.0245, −0.0157]
      = [−0.8338, −0.8250]

which *meets* the window
[−0.8303, −0.8244] on the
right and overshoots by
0.0035 on the left. One
more split of the positive
half finishes the
arithmetic enclosure
without Arb.
