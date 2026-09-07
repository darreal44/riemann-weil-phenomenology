# Romberg on [0,1]

Richardson on the
trapezoid. Table
for a even, μ=16:

    n      T(h)        T_extr
    4   −0.706869
    8   −0.702306    −0.700785
   16   −0.701175    −0.700799
   32   −0.700893    −0.700799
   64   −0.700822    −0.700799

It hits the
trap-4000 reference
immediately. As a
*number*, Romberg
is better than
G₃ 1-panel and
matches G₃ 2-panel.

As a *proof*, each
column j needs a
bound on a^{(2j)}.
Column 2 already
wants a^{(4)};
column 3 wants
a^{(6)} — the same
derivative Gauss
uses, with a
different constant,
plus the lower
columns’ errors.
One does not get
a smaller M₆ for
free. The
certificate stays
G₃ + Cauchy M₆
(#52), where the
remainder is one
term.

Useful to check
the quadrature.
Not a second
majorant.
