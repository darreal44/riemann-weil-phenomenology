<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# I_{[0,1]}: quadratic support near 0 still misses 0.047

Preregistered (`report/prereg-av-I01-quad.md`):
v=(4,−3,1)/√26, χ₅ μ=16. Not the
chord of θ (miss 0.22). Not the
parent 3-piece (miss 0.224). Not
the switch (miss 0.088). Not the
three-tangent envelope (miss
0.068). Origin named the loose
piece (`report/g-convexity.md`):
g''(0)≈9.6 peels the tangent at 0.
Not Weil. Not RH. Finite μ, one
v. Not a covering lemma.

## Comparison

g = 2 e^{−3y/2} − θ_v, elementary.
g'''<0 on [0, y_min] (shipped
`av_gpp.g_ppp`, 80 nodes plus
ends), so g'' decreases and
inf g'' = g''(y_min) = m = 4.2185.
Taylor:

    q(y) = g'(0) y + (m/2) y²
         ≤ g(y)  on [0, y_min].

q meets the floor at y_q = 0.2100,
with y_sw < y_q < y_min.

g_lo:
  [0, y_q]         q
  [y_q, y_meet]    floor g_min
  [y_meet, y_inf]  tinf
  [y_inf, 1]       chord of g

a_lo = ½ w g_lo. Integrate a_lo,
not a. True I is ∫ a on [0,1],
same shipped a (`av_gauss.a_integrand`).

## Execution

`python code/av_I01_quad.py`.
`report/av-I01-quad.json`.

    I_true = −0.700799
    I_lo   = −0.747934
    gap    = +0.047135

Pieces of I_lo: q −0.3023, floor
−0.2787, tinf −0.1145, chord −0.0525.
Q_lo = CST + I_lo + I_{[1,L]}^{lo} − P
= **−0.0416** < 0. Does not close
the ±0.003 A-window (about 16×).
Tighter than the envelope 0.068,
still a miss.

## Verdict: SURVIVE

The comparison estimate of I_{[0,1]}
is still open. One v, finite μ.
Not Weil positivity (that needs the
admissible class, all lags, all
tests, all L). Not (∀ L) Q_L ≥ 0.
Not RH.

Judge: `tests/test_av_I01_quad.py`.
