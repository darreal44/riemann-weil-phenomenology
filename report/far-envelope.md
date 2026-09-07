# Far envelope term

S_lo
=
λ_min( H − (C D^{-1} C* + C_far) / (1−ρ) )
when
ρ<1.

On
χ₃,
N_NEAR=32
(`ql-schur-neumann.json`):

    λ_H
      = +0.01850
    drop
    to
    S_diag
      = 0.01093
    S_diag
      = +0.00756
    tr C_far
      = 0.00060
    ρ
      = 0.590
    1/(1−ρ)
      = 2.441
    S_lo
      = −0.00857

C_far
is
not
the
term.
The
far
envelope
is
ρ_far
lifting
ρ
from
ρ_N=0.283
to
0.590,
which
inflates
the
*already
computed*
CDC
by
2.44.
Threshold
for
S_lo>0:
ρ<0.41
(prereg
`prereg-ql-chi3-rhofar.md`).
ρ_far(80)
still
≥0.41.

    ρ_far
      = s1_off_q_upper / qmin_far
      = (π/2 + 1/(4N) + r_F + |w₂|) / qmin
      = 2.110 / 4.192
      = 0.503

π/2
alone
already
puts
ρ_far
above
the
threshold
(Hankel-only
ρ=0.415
at
N=32
still
kills
after
λ_H
has
fallen).
S_T
of
the
computed
block
is
+0.0097:
the
finite
section
is
green;
S_lo
is
red
only
under
this
majorant.

Not
taken.
Not
RH.
