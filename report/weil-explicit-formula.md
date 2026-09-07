# Weil’s explicit formula

For an
even
test
function
F
(or
θ)
of
sufficient
decay,
and
a
primitive
χ,

    ∑_ρ ˆθ(ρ)
      = θ(0) + θ(1)
        − ∑_{n>1}
          Λ(n) χ(n) n^{−1/2}
          (θ(log n)+θ(−log n))/2
        − A_∞(θ)

ρ runs
over
zeros
of
Λ(s,χ)
(non-trivial
for
ζ).
ˆθ
is
the
Mellin /
Fourier
convention
that
makes
ˆθ(½+it)
the
cosine
transform
of
θ.

A_∞
is
the
pairing
against
W_∞
(`weil-pairing.md`):
Γ'/Γ
plus
log(q/π).

The
quadratic
form
Q
is
this
identity
rewritten
so
the
left
side
is
∑ |ˆθ(γ)|²
or
a
Gram
of
zeros,
and
the
right
side
is
A−P.
On
a
short
window
the
zero
sum
is
empty
or
tiny
(first
γ ≫
Nyquist
at
L=log 3),
so
Q
reduces
to
A−P
on
the
prime
side —
exactly
the
machine
Q_pk
once
A
is
the
true
A_∞.

What
is
proved
as
an
identity:
the
explicit
formula
itself
(Weil,
Guinand,
…),
for
a
precise
class
of
θ.
What
is
not
proved:
A
in
Q_nm
equals
A_∞,
nor
Q≥0.

RH
⇔
Q(θ)≥0
for
all
θ
in
that
class
(Weil’s
criterion).
One
θ
with
Q<0
and
A=A_∞
would
kill
GRH
for
that
χ.
That
is
why
#70
matters:
until
A=A_∞,
a
sign
on
H₄
is
not
the
explicit
formula.
