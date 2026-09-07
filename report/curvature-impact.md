# Impact of curvature by region

g''
controls
how
much
a
supporting
parabola
can
beat
a
tangent
or
a
chord.

    region          g''              Δgap when curvature used
    well [0,0.41]   +9.6 → +4.2      0.047 → 0.0053  (N=1→4)
    rise [0.41,0.77]+4.2 → 0         0.0053 → 0.00315
    tail [0.77,1]   0 → −0.70        0.00315 → 0.00280 (chords)
                                     → 0.00279 (parabolas)

Where
|g''|
is
large
and
positive,
m_i
moves
the
integral.
Where
g''
crosses
zero
and
stays
O(1),
the
legal
under-estimator
is
already
almost
g
(chords
≈
parabolas).
The
remaining
0.0028
is
the
well+rise
mesh
with
m_i=g''(right)
still
below
the
true
g''
on
the
left
of
each
slab
— plus
I_{[1,L]}
which
is
not
in
this
integral.

Raising
N
on
the
well
and
rise
is
the
only
curvature
lever
left
on
I_{[0,1]}.
The
tail
is
spent.
