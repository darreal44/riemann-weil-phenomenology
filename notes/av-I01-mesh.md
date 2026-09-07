<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# I_{[0,1]}: N=4 quadratic mesh still misses 0.0053

Preregistered (`report/prereg-av-I01-mesh.md`):
v=(4,−3,1)/√26, χ₅ μ=16. Named in
`report/quadratic-mesh.md`. N=1 is
#83 (miss 0.047). N=4 is the h≲0.1
count of `quadratic-error.md`. Not
Weil. Not RH. Finite μ, one v. Not
a covering lemma.

## Comparison

g'''<0 on [0, y_min] ⇒ g''
decreases. Uniform nodes
0, 0.1025, 0.2049, 0.3074, 0.4098.
On each slab m_i = g''(right end)
and q_i matches the 1-jet of g at
the left end. Broken parabolas
(not C¹). Then floor / tinf /
chord after y_min.

a_lo = ½ w g_lo. True I is ∫ a
on [0,1], same shipped a.

## Execution

`python code/av_I01_mesh.py`.
`report/av-I01-mesh.json`.

    I_true = −0.700799
    I_lo   = −0.706051
    gap    = +0.005252

Q_lo = CST + I_lo + I_{[1,L]}^{lo} − P
= **+0.0002**. The I-gap is still
0.0053, about 1.8× the ±0.003
A-window, so the comparison does
not close. A positive Q_lo with
gap > 0.003 is not a hand proof
of Q(v)>0 (P_rest still has ±0.003
room). Tighter than N=1 (0.047),
still a miss of the window.

## Verdict: SURVIVE

The comparison estimate of I_{[0,1]}
is still open. One v, finite μ.
Not Weil positivity (that needs the
admissible class, all lags, all
tests, all L). Not (∀ L) Q_L ≥ 0.
Not RH.

Judge: `tests/test_av_I01_mesh.py`.
