# S_lo>0 after Bochner

Bochner
tried
to
make
the
whole
kernel
PD
on
R.
The
usable
half
of
that
idea
is
a
PD
*minorant
of
T*
so
that
T^{-1}
has
a
PSD
majorant
and
Schur
can
speak
from
below.

Measured
on
the
shipped
Neumann
row
(L=log 3,
HEAD=2,
N_NEAR=32):

    χ     λ_H     s_diag    ρ      S_lo
    χ₅   0.053    +0.042   0.52   +0.029
    χ₈   0.257    +0.243   0.33   +0.235
    χ₄   0.084    +0.068   0.39   +0.057
    χ₃   0.018    +0.0076  0.59   −0.0086

ρ<1
on
all
four.
χ₃
dies
in
the
step
s_diag → S_lo:
the
far
coupling
plus
1/(1−ρ)
eats
the
0.0076.
Not
an
extension
problem.

What
to
do
instead
of
Bochner:

    1. Enlarge
       the
       computed
       near
       block
       (move
       mass
       from
       ρ_far
       to
       ρ_N,
       a
       true
       2-norm).
    2. A
       PD
       minorant
       of
       T_far
       tighter
       than
       (1−ρ)D
       (diagonal
       dominance
       with
       the
       actual
       Q_nn,
       or
       a
       Pólya
       kernel
       one
       can
       invert).
    3. Worst-sign
       tail
       only
       after
       χ₃
       itself
       is
       green.

1
is
compute.
2
is
the
true
heir
of
Bochner.
3
is
(∀χ)
and
comes
last.

Not
Weil.
Not
RH.
