# Hermite interpolation error

On
I_i
of
length
h,
the
unique
cubic
that
matches
g
and
g'
at
both
ends
has

    g(y) − H(y)
      = g^{(4)}(ξ) / 4!
        · (y−y_i)² (y−y_{i+1})²

and
|(y−y_i)(y−y_{i+1})| ≤ h²/4,
so

    |g−H|
      ≤ |g^{(4)}| h⁴ / 384.

That
is
the
1/384
already
listed.
g^{(4)}
is
O(ω₂⁴)∼400
(`higher-derivatives-g.md`),
so
the
unsigned
cap
on
h=0.10
is
~400×10⁻⁴/384≈0.01
pointwise
— worse
than
the
supporting
parabola’s
endpoint
cap
0.006
unless
one
uses
the
true
ξ
and
the
weight
(y−a)²(y−b)²
which
vanishes
at
the
ends.

The
signed
problem
is
untouched:
g−H
changes
sign
with
g^{(4)}
and
with
the
hump
of
(y−a)²(y−b)².
Subtracting
the
cap
gives
a
legal
lower
bound
worse
than
q_i
on
this
h.

Not
used
in
the
running
bound.
