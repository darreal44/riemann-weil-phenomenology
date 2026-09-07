# Lag constraints

A
lag
is
on
when
0 < log n < L
(μ = e^L
in
the
scripts’
usual
units
so
n < μ).
Q_pk
keeps
every
such
n;
Q_window
used
to
drop
powers.

Constraints
that
actually
move
numbers:

- **Support.**
  θ(log n)=0
  if
  log n ≥ L.
  At
  the
  edge
  n↑μ,
  θ is
  O(ε)
  (T₅
  at
  5⁺).
  Mid-band
  lags
  (log 2
  at
  μ=5)
  see
  the
  cap
  √2.

- **χ(n).**
  w_n = χ(n) log n / √n
  (and
  the
  usual
  Λ
  for
  prime
  powers).
  If
  χ(p)=0
  (p
  ramified:
  χ₈(2)=0)
  the
  lag
  p
  is
  absent.
  #80:
  2³
  is
  in
  ns
  at
  μ=8.1
  but
  w₈=0
  for
  χ₈,
  so
  t_atoms
  does
  not
  jump.

- **Sign
  of
  χ(p).**
  χ₃(5)=−1
  lifts
  H₀₀
  and
  dips
  λ_min
  (#75).
  Same
  lag,
  opposite
  χ,
  opposite
  H₀₀.

- **Order.**
  p^k
  at
  k log p.
  2²
  rescued
  H₄
  at
  μ=5
  (#69).
  2³
  killed
  the
  χ₈
  take
  by
  a
  head
  well,
  not
  by
  t_atoms
  (#80).

The
constraint
that
kills
takes
is
not
“too
many
lags”
as
a
count;
it
is
t_atoms
versus
qmin_far
(ρ)
or
a
Schur
well
in
the
head
when
w_n=0.
