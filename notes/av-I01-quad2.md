<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# I_{[0,1]}: two-piece quadratic still misses 0.024

Preregistered (`report/prereg-av-I01-quad2.md`):
v=(4,−3,1)/√26, χ₅ μ=16. Not the
single-m quadratic of #83 (miss
0.047). Origin: spend nodes near 0
or a quadratic on a short initial
interval (`report/g-convexity.md`).
Not Weil. Not RH. Finite μ, one v.
Not a covering lemma.

## Comparison

g'''<0 on [0, y_min] ⇒ g''
decreases. Split at y_h = y_min/2
= 0.2049.

    m1 = g''(y_h) = 7.3821
    m2 = g''(y_min) = 4.2185
    q1(y) = g'(0) y + (m1/2) y²
    q2 continues from the 1-jet of q1
    with m2, meets the floor at
    y_q = 0.2630 ∈ (y_h, y_min).

Then floor / tinf / chord as in
the envelope. a_lo = ½ w g_lo.
True I is ∫ a on [0,1], same
shipped a (`av_gauss.a_integrand`).

## Execution

`python code/av_I01_quad2.py`.
`report/av-I01-quad2.json`.

    I_true = −0.700799
    I_lo   = −0.724897
    gap    = +0.024098

Pieces of I_lo: q1 −0.2774, q2
−0.0681, floor −0.2124, tinf
−0.1145, chord −0.0525.
Q_lo = CST + I_lo + I_{[1,L]}^{lo} − P
= **−0.0186** < 0. Does not close
the ±0.003 A-window (about 8×).
Tighter than the single-m 0.047,
still a miss.

## Verdict: SURVIVE

The comparison estimate of I_{[0,1]}
is still open. One v, finite μ.
Not Weil positivity (that needs the
admissible class, all lags, all
tests, all L). Not (∀ L) Q_L ≥ 0.
Not RH.

Judge: `tests/test_av_I01_quad2.py`.
