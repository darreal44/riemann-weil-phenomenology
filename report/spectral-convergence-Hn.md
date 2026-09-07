# Spectral convergence of H_n

Galerkin
λ_min(H_n)
is
decreasing
in n
(Courant).
It
converges
to
c_L^*
from
above
if
the
cosine
ONB
is
complete
in W_L.

Measured,
identified
Q_pk,
χ₃:

    μ    n=16         n=48        ratio
    5    +1.4e-5      (take S_lo
                      at h=16)
    7    +4.81e-9     +3.26e-9    0.68
    8    +8.09e-11    +6.00e-11   0.74

From
16
to
48
the
eigenvalue
drops
~30 %,
not
an
order
of
magnitude.
The
well
is
already
in
the
first
sixteen
modes.
Adding
modes
does
not
cross
zero
on
this
grid.

That
is
convergence
of
the
*section*,
not
of
S_lo.
Neumann
at
μ=7,8
has
ρ≥1
(#73):
the
tail
bound
does
not
converge
to
a
positive
number.
Two
different
limits.

No
Weyl
law
for
the
bulk
(`Wlog3-spectrum.md`).
Only
the
bottom.
