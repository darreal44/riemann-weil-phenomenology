# Block norms (near / coupling / far)

    ρ_N
      = ‖A_near‖₂
      A_near
        = D^{-1/2} Off_T D^{-1/2}
      on
      hats
      HEAD…N_NEAR
      (computed).
    ρ_B
      = √(∑_{n near, m far} Q_nm² /(Q_nn Q_mm)
         + Hilbert
         + θ
         remainders)
      coupling
      of
      the
      computed
      near
      block
      to
      the
      uncomputed
      far.
    ρ_far
      = Off_far / qmin_far
      Off_far
        = ½π + 1/(4 N_NEAR) + HS
          + |w₂| ‖Θ‖
      a
      majorant,
      not
      a
      matrix
      2-norm.

ρ
=
block_norm(ρ_N, ρ_B, ρ_far)
=
λ_max
of
the
2×2
[[ρ_N, ρ_B],[ρ_B, ρ_far]]
(the
code’s
3-number
pack
is
that
2-norm).
It
is
≥
each
piece.
If
ρ_far
is
the
largest
and
≥1,
the
series
dies
even
when
the
computed
near
block
is
tame.

That
is
the
usual
killer:
ρ_far
carries
Hilbert
π
and
|w₂|√2.
A
sharper
far
norm
(not
a
sharper
π)
is
the
only
legal
way
to
push
ρ
back
below
1
at
larger
L.

Not
Weil.
