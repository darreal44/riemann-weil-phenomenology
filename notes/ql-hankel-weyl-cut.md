<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# Truncated Weyl trial on Hankel [32,M)

Not
Hartman.
Not
a
take.

`report/minorant-weyl-error.md`
saw
‖H x‖≈0.22
on
[32,80)
only.
This
sitting
extends
M
and
fits
the
cutoff
error
e_H(M)=π/2−‖H_M‖.

H_nm
=
½/(n+m)
on
[N,M),
N=32,
including
the
diagonal
(Hilbert
object).
Trial
x_n
=
n^{−1/2}
and
n^{−1/2} cos(τ log n),
τ∈{0, 0.5, 1, 2}.
R(M)=⟨Hx,x⟩,
e_R=π/2−R,
e_σ=π/2−‖H‖₂.
No
GL
CSV
(wrong
Hilbert
space).

    M      σ       eσ      R      τ*
    80     0.227   1.343   0.227  0
    128    0.336   1.234   0.336  0
    256    0.483   1.088   0.483  0
    512    0.612   0.959   0.610  0
    1024   0.723   0.848   0.719  0
    2048   0.818   0.753   0.812  0

τ*=0
always:
oscillation
never
beats
the
plain
n^{−1/2}.
R
saturates
σ
of
the
section
(the
trial
is
essentially
the
top
mode
of
the
cutoff).

Fit
on
the
eight
unions:

    e_σ ≈ 0.658 / log(M/N) + 0.707
      R² = 0.868
    e_R ≈ 0.653 / log(M/N) + 0.711
      R² = 0.871

b→0
would
be
Hartman.
The
intercept
is
0.707,
not
0.
At
M=2048
the
section
is
still
0.75
below
π/2.
No
infinite
Weyl
sequence.
Does
not
exhibit
1.081.
Does
not
license
s₁≤0.8.

Not
taken.
Not
RH.
One
L.
`python code/ql_hankel_weyl_cut.py`
`report/ql-hankel-weyl-cut.json`.
