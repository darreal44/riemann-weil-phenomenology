# Regularising G at 0

On W_L every
admissible g is
even with g(0)=0
(θ(0)=2 is the
normalisation of
the hats, the
test in y vanishes
at 0 after the
usual even
extension). Then

    ∫_0^L D₂(y) g(y) dy
      = ∫_0^L (D₂(y)−1/y) g(y) dy
        + ∫_0^L g(y)/y dy

The second piece
is regular
(g(y)/y → g′(0)).
D₂(y)−1/y tends
to a finite limit
at 0
(s₀-dependent).
So the pairing
depends only on
a *bounded*
even kernel

    G_reg(y) = D₂(y) − 1/y    (y≠0)
    G_reg(0) = lim (D₂−1/y)

plus the
functional
g ↦ ∫ g(y)/y dy
which, under
g(0)=0, is
bounded on W_L
and can be
moved into CST
/ the ψ(s₀)
constant
already in
C_A^{lo}.

G_reg is
continuous on
[−L,L] if one
sets the value
at 0. It is
the object
Pólya and
Krein may
see. Whether
it is convex
near 0 is a
separate
check
(1/y was the
convex
singular
part; G_reg
may lose
convexity).

The atom at
log 2 is
untouched.
Regularisation
does not
create a PD
extension. It
only puts G
in the
function class
those
theorems
assume.

A computation:
tabulate
G_reg on
[0,L], test
convexity,
then try a
Pólya tail.
If G_reg is
already not
convex on
[0,L], Pólya
on the whole
line is
impossible
without
changing
values *inside*
(0,L), which
would change
Q.
