# Impact of κ

κ is the Si-matrix
element of block(2)
on P F_∞ P, after
the three explicit
factors ½, 2^{−1/2},
d*λ
(`block2-coefficient.md`).

    m_lin = κ / (2√2)

Three exits on the
server ladder.

## A. Freeze at 4±0.2

m_lin → 1/√2.
The linearised
slice is the
**module** shell
n=−1. Then:

- `tau_curve`’s
  dilation-by-λ was
  the right name
- #46’s climb to √2
  is *not* this
  shell: it is the
  other scales and
  the B₂P B₂ square
- Bombieri 0.490
  stays the wrong
  Haar for w₂
- Thm 4 is still
  not Fmat: only
  the linear piece
  matches one
  number

Impact: rewrite
the working target
of `peak_2adic.py`
(today: inverse).
Do not rerun
Λ=64.

## B. Freeze at 8±0.2

m_lin → √2.
Linearised slice
is the **inverse**
shell. Then
ϑ(λ)g=λ^{−1/2}g(r/λ)
dilates by λ but
the Haar mass is
the u⁻¹ twist.
#46 and the
linear probe
*agree*. The
dictionary
d*λ ↔ d*u is
still one
identification
step (the same
number, two
measures).

Impact: keep
`mass_at_two
('inverse')`.
Write the
Jacobians that
turn ½·2^{−1/2}
into √2 as
κ=8, not as a
new grid.

## C. No freeze
(|Δκ|>0.3 from
cpu=160 to 400
at Λ=16)

κ is not a
constant of the
kernel. Then
neither 4 nor 8
is a theorem.
Fmat’s Si-average
does not settle
on a shell.
Larger Λ / finer
h will move m_lin
the same way w₂
moves. Reading
(2) of
`2adic-after-46.md`
wins: Fmat is not
Thm 4.

Impact: stop
the Fmat lock.
The analytic
pairing
`tau2_local`
stays; the grid
does not.

## What κ does
not impact

Q(v), (∀L) on
W_L, drop-3,
Courant, Schur,
Young, Fourier
ψ. Those are
other operators.
A 4 or an 8
does not raise
c_L^*.
