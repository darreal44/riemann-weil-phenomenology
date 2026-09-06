# A(v) for the rational witness

v = (4,−3,1)/√26, χ₅, μ=16,
L = log 16 = 4 log 2,
s₀ = 1/4, F₀(v) = 2.

    A(v) = F₀/2 · CST + ½ ∫₀ᴸ
           [2 e^{-y/2}/(1−e^{-2y})]
           (2 e^{-3y/2} − θ_v(y)) dy

## The constant — elementary

    CST = log(5/π) − γ − log(1−e^{-2L})
        = log(5/π) − γ − log(1−1/256)

    F₀/2 · CST = CST = −0.108593739

γ, log 5, log π are
classical. 1/256 is exact.
This piece is a hand
number to 10⁻⁹ from any
short table.

## The integral — 24 panels

    −0.719298

By panel (width L/24 ≈ 0.116):

     y≲0.5   −0.160 −0.136 −0.113 −0.090 −0.070
     0.5–1.2 −0.053 −0.039 −0.028 −0.019 −0.013 −0.008
     1.2–2.0 −0.005 −0.002 −0.000 +0.001 +0.002 +0.002 +0.002
     2.0–L   +0.002 +0.002 +0.002 +0.002 +0.001 +0.001 +0.001

Monotone from −0.16 to a
positive tail of +0.016
after y≈1.6. The kernel
e^{-y/2}/(1−e^{-2y}) drops
from 2.56 to 0.0014.

## A(v)

    −0.10859 − 0.71930 = −0.82789

Room needed for Q(v)>0
(`rational-witness-chi5-mu16.md`):
A(v) ∈ [−0.8303, −0.8244].
The computed value sits
in the middle ±0.003.

## What a hand bound must do

The constant is done.

The integral is a smooth
decreasing-then-small
function on a compact
interval. A 6-point
Gauss panel on [0, L]
already gave the same
Q₀₀ at printed precision
(`legendre.md`). A
hand estimate can split
[0, 1] + [1, L]:

- on [0,1], θ_v and the
  weight are explicit
  (θ_v(0)=2, decreasing
  to θ_v(1)≈0.3);
- on [1,L], the weight
  is ≤ e^{-1/2}/(1−e^{-2})
  ≈ 0.75 and the
  integrand is O(10⁻²),
  length 1.77 ⇒ tail
  O(0.03) before
  cancellation of the
  two terms in
  (2e^{-3y/2}−θ_v).

The O(0.03) is still
larger than the ±0.003
window. The split is
the right shape; the
constants on [1,L]
need one more
tightening (compare
2e^{-3y/2} to θ_v,
they almost cancel).
