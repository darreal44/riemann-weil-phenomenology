# S, the Schur complement

    S
      = H − C T^{-1} C*.

The
lab
never
forms
T^{-1}.
Two
proxies:

    S_diag
      = H − C D^{-1} C*
      (T
      replaced
      by
      its
      diagonal
      on
      the
      computed
      near
      block).
    S_lo
      = λ_min( H − (cdc + cfar) / (1−ρ) )
      if
      ρ<1.

χ₃
at
N_NEAR=32:

    λ_H
      = +0.0185
    S_diag
      = +0.0076
    S_lo
      = −0.0086

The
drop
λ_H → S_diag
is
the
computed
coupling
(0.011).
The
drop
S_diag → S_lo
is
the
far
envelope
(0.016).
That
second
drop
is
the
red
cell.
Deepening
N_NEAR
to
48
moves
S_lo
to
−0.0063
and
leaves
S_diag
frozen.

S≥0
plus
T>0
is
Q̂≥0
on
the
whole
space.
S_lo>0
is
a
sufficient
condition,
not
necessary.
χ₃
can
still
have
S>0
while
S_lo<0.

Not
RH.
