<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# I_{[0,1]}: cubic Taylor with a proved |g'''| cap, miss 1.40

Preregistered (`report/prereg-av-I01-gppp.md`): v=(4,−3,1)/√26, χ₅
μ=16. Not a mesh. Not N=8. Not leftover-adaptive. Not Weil. Not RH.

## Inequality

g = 2 e^{−3y/2} − θ_v, six elementary lags. Bound |∂_{yyy} θ_nm| by
replacing every sin and cos with 1:

    Amp_{0j} = 2 ω_j³ / (√2 π j)
    Amp_{nn} = 2 (3 ω_n²/L + ω_n³ + ω_n³/(2π n))
    Amp_{nm} = 2 (n ω_n³ + m ω_m³) / (π |m²−n²|)

Then |θ_v'''| ≤ ∑ |v_n v_m| Amp_nm and

    |g'''| ≤ K = 6.75 + ∑ |v_n v_m| Amp_nm = 50.351.

The sampled max |g'''| on [0,1] is 15.878, under K. Lagrange remainder
after order 2:

    g(y) ≥ g'(0) y + g''(0) y²/2 − (K/6) y³    on [0,1],

with g'(0)=−2.962 and g''(0)=9.636 the shipped jet at 0. a_lo = ½ w g_lo.
True I is ∫ a, same shipped a.

## Execution

`python code/av_I01_gppp.py`
`report/av-I01-gppp.json`

    I_true = −0.700799
    I_lo   = −2.104382
    gap    = +1.403584
    Q_lo   = −1.398

The cubic is a legal lower bound (sample: cubic ≤ g) and misses the
±0.003 A-window by three orders. w ~ 1/y near 0 multiplies the crude
−(K/6) y³. A mesh of g'' already sits inside ±0.003
(`notes/av-I01-n8.md`); this is not that. The elementary |g'''| cap is
too crude to replace the mesh.

## Verdict: KILL

One v, finite μ. Not Weil. Not (∀ L) Q_L ≥ 0. Not RH.

Judge: `tests/test_av_I01_gppp.py`.
