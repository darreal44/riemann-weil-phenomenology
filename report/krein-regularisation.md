# Krein on the regularised kernel

G_reg is continuous
on [−L,L]
(`kernel-regularisation.md`).
Krein’s (B1) is
now satisfied.
Convexity is not
required. The
test is PD on
the interval:

    ∫∫ G_reg(x−y) f(x)¯f(y) ≥ 0
    for supp delays ≤ L.

That is Q̂_L on
the continuous
part, modulo
the atom at
log 2 and the
∫ g/y term
already in CST.

No Pólya tail
is asked. An
extension to ℝ
exists iff this
inequality holds.
We do not get
the extension
for free.

Practical
Krein-regularised
tests, all
zero-N in
spirit but
finite in
practice:

1. Toeplitz of
   G_reg(kΔ) for
   kΔ≤L, Δ↓0.
   Same as a
   fine cosine /
   delay family.
   #57’s windowed
   cosines are
   one such
   sample and
   stayed
   positive.
2. Pick / resolvent
   of the string
   (Krein–de
   Branges).
   Heavy. Not
   shipped.
3. Exhibit a
   measure μ≥0
   with ˆμ = G_reg
   on [−L,L]
   (truncated
   trigonometric
   moments).
   Finite
   atomic μ is
   a quadrature
   of the
   moment
   problem.
   If a small
   atomic μ
   matches G_reg
   on a net in
   [0,L] and
   ˆμ ≥ |w₂|
   off the
   atoms, one
   has a
   certificate.

Regularising
for Krein
changed the
function class
(bounded
continuous).
It did not
prove PD.
The atom and
the sign of
C_A^{lo} remain
the likely
obstructions
to a cheap
atomic μ.
