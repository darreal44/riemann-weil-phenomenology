# Critical points of g'' on [1, y*]

g''' is the same six
kernels, three times
(`th_ppp` in `av_gpp.py`).
Checked against a
central difference of
g'' at y=1.2
(1.09564125 vs 1.09564125).

## Zeros of g'''

Two roots in [1, 1.59]:

    y = 1.03162,  1.45775

Evaluate g'' there and
at the ends:

    y        g''
    1.000   −0.69975
    1.032   −0.70699     min
    1.458   −0.41061     max
    1.590   −0.45002

So on this compact,

    −0.70700 ≤ g'' ≤ −0.41061

The interior min/max
match a 2000-node sample
to 10^{-8}. No other
critical point.

## Status

This is the exact
catalogue of extrema
*once the two roots of
g''' are admitted*.
The roots are simple
(g''' changes sign) and
isolated. Locating them
in isolating intervals
of width 10^{-3} by
two bisections of an
elementary function is
a finite check, in the
same class as G₃.

Then |g''| ≤ 0.707 is
a theorem on [1, 1.59],
and the four-slab
trapezoid error

    4 · (h³/12) · 0.707 · ½ w(1)
    h = 0.59/4 ≈ 0.147
      ≈ 2.1×10^{-3}

falls inside the ±0.003
window — provided one
also accepts the four
trapezoid samples of
g itself.
