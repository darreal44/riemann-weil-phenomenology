<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# I_{[0,1]} leftover-driven adaptive mesh sits in ±0.003

Preregistered (`report/prereg-av-I01-adapt.md`):
v=(4,−3,1)/√26, χ₅ μ=16. Named in
`report/adaptive-methods.md`. Not
Kronrod on a. Parent tailq gap
0.002793. Not Weil. Not RH.

## Comparison

Uniform N=4 well + N=4 rise, then
eight leftover bisections on
[0, y_inf]. leftover = g''(left)−m_i
with m_i = g''(right) (g'''<0).
First cuts land on the last well
slabs (leftover ~1.6). Tail
parabolas of tailq stay. a_lo =
½ w g_lo. True I is ∫ a, same
shipped a.

## Execution

`python code/av_I01_adapt.py`.
`report/av-I01-adapt.json`.

    n_convex = 16
    I_true   = −0.700799
    I_lo     = −0.701231
    gap      = +0.000433
    Q_lo     = +0.0051

Gap inside the ±0.003 A-window
(about 1/7 of the room). Tighter
than uniform-N=8 rate ~7×10^{-4}
(`Oh2-I01.md`). One v, finite μ.
g'''<0 on [0, y_inf] makes m_i =
g''(right) the inf on each slab
(grid of `g_ppp`). That is this
comparison, not Weil positivity.

## Verdict: SURVIVE

The I-window for this comparison
on this v is met. (∀ L) Q_L ≥ 0
is the covering lemma; not this
note. Not Weil. Not RH.

Judge: `tests/test_av_I01_adapt.py`.
