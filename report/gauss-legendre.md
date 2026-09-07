# Gauss–Legendre n=3, as shipped

Exact for
polynomials of
degree ≤ 5.
Remainder ~ f^{(6)}.

On [−1,1] the
nodes are 0, ±√(3/5).
Mapped to [0,1]
(t=(x+1)/2):

    x = ½(1−√(3/5)),  ½,  ½(1+√(3/5))
    w = 5/18,  8/18,  5/18

`GAUSS_NODES` /
`GAUSS_WEIGHTS` in
av_gauss.py.
√(3/5)=√0.6.

The map [−1,1]→[0,1]
puts a 2⁷ / 2⁶ into
c₆, which collapses
to

    c₆ = (3!)⁴ / (7 (6!)³)
       = 4.960317×10⁻⁷

on the unit interval
(`remainder-R.md`).

n=3 is the smallest
rule whose remainder
is a^{(6)}, the
first even
derivative after
the degree-5
exactness. n=2
would be a^{(4)}
with a larger
typical error on
this a. n=4 wants
a^{(8)} and a
tighter Cauchy
r^{-8}, worse if
M is crude.

Two panels: apply
the same three
nodes on [0,½]
and [½,1]. That
is still n=3 per
panel, not n=6
on [0,1].
