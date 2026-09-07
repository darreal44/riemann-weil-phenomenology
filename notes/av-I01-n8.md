<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# I_{[0,1]} uniform N=8 well+rise: gap 0.000405

Preregistered (`report/prereg-av-I01-n8.md`):
v=(4,−3,1)/√26, χ₅ μ=16. Named rate
test (`Oh2-I01.md`,
`error-convergence.md`). Not Kronrod.
Not leftover-adaptive. Not
superconvergence. Not Weil. Not RH.

## Comparison

Uniform N=8 on [0, y_min] and N=8
on [y_min, y_inf]. q_i matches the
1-jet of g, m_i = g''(right). Tail
parabolas of tailq stay. a_lo =
½ w g_lo. True I is ∫ a, same
shipped a.

## Execution

`python code/av_I01_n8.py`.
`report/av-I01-n8.json`.

    n_convex = 16
    cap      = 0.000186   (N=4 was 0.00151; ratio 0.123)
    I_true   = −0.700799
    I_lo     = −0.701203
    gap      = +0.000405
    Q_lo     = +0.0051

Gap inside ±0.003. Origin predicted
~7×10^{-4}; measured 4.05×10^{-4}.
Leftover cap fell by ~8, more than
the factor 2 of the rate test.
The bend O(h²) has set in. One v.

## Verdict: SURVIVE

The I-window for this comparison
on this v is met. (∀ L) Q_L ≥ 0
is the covering lemma; not this
note. Not Weil. Not RH.

Judge: `tests/test_av_I01_n8.py`.
