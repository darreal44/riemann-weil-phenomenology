<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# I_{[0,1]}: three-tangent envelope still misses 0.068

Preregistered (`report/prereg-av-I01-envelope.md`):
v=(4,−3,1)/√26, χ₅ μ=16. Not the
chord of θ (miss 0.22). Not the
parent 3-piece (miss 0.224). Not
the tangent/floor switch (miss
0.088). Not Weil. Not RH. Finite
μ, one v. Not a covering lemma.

## Comparison

g = 2 e^{−3y/2} − θ_v, elementary.
Convex on [0, y_inf] ⇒ every
tangent lies below g. Three
supporting lines:

    t0   = g'(0) y
    tmin = g_min
    tinf = g(y_inf) + g'(y_inf)(y − y_inf)

y_sw = g_min/g'(0) = 0.1786.
y_meet from tmin = tinf equals
0.5197, and y_min < y_meet < y_inf.

g_lo:
  [0, y_sw]        t0
  [y_sw, y_meet]   floor g_min
  [y_meet, y_inf]  tinf
  [y_inf, 1]       chord of g

a_lo = ½ w g_lo. Integrate a_lo,
not a. True I is ∫ a on [0,1],
same shipped a (`av_gauss.a_integrand`).

## Execution

`python code/av_I01_envelope.py`.
`report/av-I01-envelope.json`.

    I_true = −0.700799
    I_lo   = −0.768770
    gap    = +0.067971

Pieces of I_lo: t0 −0.2762, floor
−0.3256, tinf −0.1145, chord −0.0525.
Q_lo = CST + I_lo + I_{[1,L]}^{lo} − P
= **−0.0625** < 0. Does not close
the ±0.003 A-window (about 23×).
Tighter than the switch 0.088,
still a miss.

## Verdict: SURVIVE

The comparison estimate of I_{[0,1]}
is still open. One v, finite μ.
Not Weil positivity (that needs the
admissible class, all lags, all
tests, all L). Not (∀ L) Q_L ≥ 0.
Not RH.

Judge: `tests/test_av_I01_envelope.py`.
