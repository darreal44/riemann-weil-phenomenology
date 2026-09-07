# ‖Θ‖≤√2 on ℓ² in the mid-band

Claim.
For L/4 ≤ y < L/2,
even f ∈ L²[−L/2, L/2]
with ‖f‖=1,

    |θ(y)|
      = |2 ⟨f, T_y f⟩|
      ≤ √2.

Hence the
Gram Θ(y)
in any
ONB
(the
cosine
head
included)
has
‖Θ(y)‖ ≤ √2.
The
μ=5
χ₃
take
uses
this
at
y=log 2
(L=log 5).

## Partition
(#72)

h = √2 f|_{[0,L/2]}
has
‖h‖=1
by
evenness.
Split
[0, L/2]
at
L/4 ≤ y < L/2:

    A = [0, L/2−y]
    C = [y, L/2]
    M = [L/2−y, y] = M₁ ∪ M₂

A and C
are
disjoint
translates
(shift
y).
M₂
is
the
even
fold
of
A
that
still
meets
the
overlap.
Masses
α=‖h‖_A²,
β=‖h‖_C²,
μ₁=‖h‖_{M₁}²,
μ₂=‖h‖_{M₂}²,
α+β+μ₁+μ₂=1.

Cauchy–Schwarz
on
the
three
overlapping
pairs
gives

    |θ|
      ≤
    2√(αβ) + 2√(α μ₂) + μ₁.

(The
cross
term
on
M₁
is
at
most
the
mass
μ₁,
not
a
geometric
mean.)

## Simplex
(closed)

On
α+β+μ₁+μ₂=1,
all
≥0,

    2√(αβ) + 2√(α μ₂) + μ₁
      ≤ √2.

Proof.
Set
x=√α,
p=√β,
q=√μ₂,
s=p+q,
d=p−q,
r=μ₁.
Then
x²+(s²+d²)/2+r=1
and
the
majorant
is

    φ
      = 2 x s + r
      = 1 − x² + 2 x s − s²/2 − d²/2.

φ
decreases
in
d²,
so
the
max
is
at
d=0.
For
fixed
x,
φ=1−x²+2xs−s²/2
on
0≤s≤√(2(1−x²)).
The
vertex
s=2x
is
feasible
iff
x²≤1/3,
and
then
φ=1+x²≤4/3<√2.
If
x²>1/3
the
max
is
at
the
right
end
s=√(2(1−x²)),

    φ
      = 2√2 \, x √(1−x²)
      ≤ √2,

because
x√(1−x²)≤1/2
(at
x²=1/2).
Equality
at
α=1/2,
β=μ₂=1/4,
μ₁=0,
d=0.

## What
is
still
geometry

The
simplex
is
a
theorem.
The
identification
|θ|≤2√(αβ)+2√(αμ₂)+μ₁
is
the
overlap
count
in
#72.
Finite
sections
saturating
√2
(N≥32
at
y=log 2,
L=log 5)
are
Courant
the
wrong
way
for
a
proof,
and
a
sharpness
check
for
the
cap:
the
bound
cannot
be
lowered.

If
the
overlap
estimate
fails
by
ε,
the
cap
returns
to
2
and
the
χ₃
μ=5
take
dies
(S_lo
at
h=16
was
a
cap
effect,
`cap-effects.md`).

Not
RH.
Not
(∀ L).
