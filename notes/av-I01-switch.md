<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# I_{[0,1]}: tangent/floor switch still misses 0.088

Preregistered (`report/prereg-av-I01-switch.md`):
v=(4,−3,1)/√26, χ₅ μ=16. Not the
chord of θ (miss 0.22). Not the
parent 3-piece that keeps the
tangent until y_min (miss 0.224).
Not RH. Finite μ, one v. Not a
covering lemma.

## Comparison

g = 2 e^{−3y/2} − θ_v, elementary.
g'(0)=−2.962, unique min
y_min=0.4098, g_min=−0.529,
inflection y_inf=0.7715.
Convex on [0, y_inf] ⇒ every
tangent lies below g. The tangent
at 0 is g'(0) y. The tangent at
the min is the floor g_min. They
meet at

    y_sw = g_min / g'(0) = 0.1786 < y_min.

g_lo:
  [0, y_sw]      tangent at 0
  [y_sw, y_inf]  floor g_min
  [y_inf, 1]     chord of g

a_lo = ½ w g_lo. Integrate a_lo,
not a. True I is ∫ a on [0,1],
same shipped a (`av_gauss.a_integrand`).

## Execution

`python code/av_I01_switch.py`.
`report/av-I01-switch.json`.

    I_true = −0.700799
    I_lo   = −0.788633
    gap    = +0.087835

Pieces of I_lo: tangent −0.2762,
floor −0.4600, chord −0.0525.
Q_lo = CST + I_lo + I_{[1,L]}^{lo} − P
= **−0.0823** < 0. Does not close
the ±0.003 A-window (about 30×).
Tighter than the parent 0.224,
still a miss.

## Verdict: SURVIVE

The comparison estimate of I_{[0,1]}
is still open. The switch is a new
lower bound, not the parent 3-piece
and not the chord of θ. It misses
by 0.088. One v, finite μ. Not RH.
(∀ L) Q_L ≥ 0 is the covering
lemma; not this note.

A later three-tangent envelope
misses 0.068 (`notes/av-I01-envelope.md`).
Still not Weil.

Judge: `tests/test_av_I01_switch.py`.
