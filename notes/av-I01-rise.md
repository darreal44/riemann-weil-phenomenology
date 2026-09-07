<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# I_{[0,1]}: mesh on the convex rise still misses 0.00315

Preregistered (`report/prereg-av-I01-rise.md`):
v=(4,−3,1)/√26, χ₅ μ=16. The N=4
well mesh left ~0.0029 of gap on
[y_min, 1] because of the floor.
g is still convex on [y_min, y_inf].
Extend the broken parabolas, drop
the floor. Not Weil. Not RH.

## Comparison

N=4 well mesh on [0, y_min], then
N=4 uniform nodes on [y_min, y_inf]
= 0.4098 … 0.7715. On each rise
slab m_i = g''(right end), q_i
matches the 1-jet of g. Chord on
[y_inf, 1]. No floor, no tinf.

## Execution

`python code/av_I01_rise.py`.
`report/av-I01-rise.json`.

    I_true = −0.700799
    I_lo   = −0.703950
    gap    = +0.003151

Q_lo = **+0.0023**. The I-gap is
0.00315, just outside the ±0.003
A-window (about 1.05×). Tighter
than the well-only 0.0053, still
a miss. A positive Q_lo with gap
> 0.003 is not a hand proof of
Q(v)>0.

## Verdict: SURVIVE

The comparison estimate of I_{[0,1]}
is still open. One v, finite μ.
Not Weil positivity. Not (∀ L) Q_L ≥ 0.
Not RH.

Judge: `tests/test_av_I01_rise.py`.
