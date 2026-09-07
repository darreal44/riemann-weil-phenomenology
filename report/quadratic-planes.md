# Piecewise quadratic supports

A
“quadratic
plane”
here
is
not
a
plane
in
R³.
It
is
a
supporting
parabola

    q_i(y)
      = g(y_i) + g'(y_i)(y−y_i)
        + (m_i/2)(y−y_i)²

on
a
subinterval
I_i ⊂ [0, y_min]
with
m_i = inf_{I_i} g''.

#83
is
one
piece
(i=0,
y_i=0,
m=inf_{[0,y_min]} g'').
Splitting
[0, y_min]
into
two
or
three
I_i
raises
each
m_i
toward
the
local
g''
and
keeps
the
true
g'(y_i).
That
is
the
same
idea
as
a
mesh
for
a
convex
function,
one
order
higher.

The
gap
budget:
0.047
left,
±0.003
wanted.
Two
or
three
pieces
can
plausibly
eat
another
0.01–0.02
if
g''
varies
smoothly
from
9.6
to
4.2.
They
will
not
close
the
A-window
unless
the
remaining
error
after
y_min
(floor
+
t_inf
+
chord)
is
already
tiny.
That
tail
was
not
the
dominant
miss
in
#82–#83;
the
origin
was.

Not
a
take
of
W_L.
One
v.
