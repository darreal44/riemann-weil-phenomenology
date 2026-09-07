# Geometry of the mid-band simplex

Masses
on
[0, L/2]:

    α = ‖h‖_A²      A=[0, L/2−y]
    β = ‖h‖_C²      C=[y, L/2]
    μ₂= ‖h‖_{M₂}²   even fold of A
    μ₁= ‖h‖_{M₁}²   the leftover middle

α+β+μ₁+μ₂=1.

The
majorant
2√(αβ)+2√(αμ₂)+μ₁
is
three
possible
overlaps:
A↔C
(shift
y),
A↔M₂
(the
fold),
and
M₁
against
itself
(no
CS
gain).

Equality
to
√2
at
α=1/2,
β=μ₂=1/4,
μ₁=0,
and
p=q
(the
two
small
masses
equal).
Geometrically:

- M₁
  empty:
  all
  mass
  lives
  in
  A ∪ C ∪ M₂,
  no
  leftover
  middle.
- Half
  the
  mass
  on
  A
  (the
  unique
  interval
  that
  touches
  both
  C
  and
  M₂).
- The
  other
  half
  split
  equally
  between
  the
  two
  partners
  of
  A.

That
is
a
function
supported
on
three
blocks
of
lengths
L/2−y,
L/2−y,
and
2y−L/2,
with
the
first
block
carrying
half
the
L²
mass.
At
y→(L/4)⁺
the
middle
2y−L/2→0
and
M₁
is
automatically
small.
At
y→(L/2)⁻
A
and
C
shrink
to
points
and
the
#59
cap
1
takes
over
(different
partition).

The
finite
sections
of
Θ
that
hit
√2
are
trying
to
realise
this
three-block
profile
in
the
cosine
ONB.
They
succeed
to
machine
precision
at
N≥32
for
y=log 2,
L=log 5.
That
does
not
construct
the
L²
extremiser
in
closed
form;
it
says
the
cap
is
sharp
in
the
ONB
already.

μ₁>0
strictly
lowers
the
majorant
(the
r
term
in
φ
is
dominated
by
the
lost
cross
terms).
Putting
mass
in
the
leftover
middle
is
never
optimal
for
the
bound.
