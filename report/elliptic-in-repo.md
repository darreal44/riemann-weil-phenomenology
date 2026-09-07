# Elliptic curves here

Not BSD. The
object is L(E,s)
as a degree-2
source of a_n
for the same Q
as Dirichlet L.

Eight Cremona
labels in
gl2_curves.py.
a_p by point
counting, a_N
by Atkin–Lehner
(BAD_AP). 37a1
is y²+y=x³−x,
N=37, a₃=−3,
rank 1 over Q
(generator [0,0],
height 0.051).
That rank is
unused in Q.

Why 37a1 for
drop-3: a₃ is
large relative
to 2√3 (ratio
−0.87), P₃<0,
and the 3-less
form actually
crosses 0. On
11a1 a₂=−2 is
the analogue;
drop-3 was the
recalcitrant
prime on 37a1
at μ=62.

Q on E is
prime-side
(scan_q_gl2),
not Gram
(scan_gl2 Gram
is a desert
artifact for
ζ/Δ). μ* and
83 live on
that Q.
Sato–Tate on
11a1 was a
side check of
the a_p, not
of Q.

An elliptic
curve is, in
this repo, a
machine that
emits a_n with
|a_p|≤2√p so
the same
explicit
formula applies.
The arithmetic
of E (tors, rank,
regulator) is
logged and then
left aside.
