# Cubic under-estimator of g

Taylor
with
a
floor
on
g''':

    g''' ≥ m₃
    on
    [0, y_min]
    (m₃<0
    by
    #83)

implies

    g''(t)
      ≥
    g''(0) + m₃ t

    g(y)
      ≥
    g'(0) y
    + g''(0) y²/2
    + m₃ y³/6.

That
cubic
is
legal
near
0.
#83
used
the
weaker

    g''(t) ≥ m = inf g''
    ⇒
    q(y)=g'(0)y+(m/2)y²

and
threw
away
g''(0)≈9.6
after
the
first
instant.
The
cubic
keeps
9.6
and
pays
with
m₃ y³/6<0.

Whether
that
beats
0.047
depends
on
|m₃|.
If
|m₃|
is
large,
the
y³
term
kills
the
gain
from
9.6
before
y_q.
If
|m₃|
is
moderate,
the
gap
drops
a
little
and
still
misses
±0.003
(the
history
0.22→0.047
suggests
another
0.01–0.02,
not
a
factor
15).

g'''
is
elementary
(`av_gpp.g_ppp`).
A
locked
campaign
would
be:
compute
m₃=min g'''
on
[0,y_min]
by
the
same
grid
#83
used
for
the
sign,
build
the
cubic,
meet
the
floor,
integrate
a_lo.
Not
run
here.

Not
Weil.
One
v,
one
μ.
