<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# KILL: χ₁₇ dies at μ=8; χ₈ still takes at h=24

Preregistered (`report/prereg-ql-chi817-mu8.md`):
χ₈ and χ₁₇, μ=8, then 11 if χ₁₇
takes. Predicted χ₁₇ still takes
(margin +0.039 at μ=7). Identified
Q_pk. Not RH.

## Execution

`python code/ql_chi817_mu8.py`.
`report/ql-chi817-mu8.json`.
ns(8)=[2,3,4,5,7]. μ=11 not run.

| χ | h=8 | h=16 | h=24 |
|---|---|---|---|
| χ₈ | — ρ=1.05 | — ρ=1.03 | **+2.86×10⁻⁴** ρ=0.89 |
| χ₁₇ | — ρ=1.29 | — ρ=1.27 | — ρ=1.04 |

χ₁₇ has no S_lo>0. The comfortable
even cell dies under T₇. χ₈ (χ(2)=0)
still takes at h=24. The prediction
that χ₁₇ survives is false.

## Verdict: KILL

T₇ kills χ₁₇ at μ=8. χ₈ remains a
sliver take at h=24. Not Weil-positive.
Not (∀ L). Not RH.

Judge: `tests/test_ql_chi817_mu8.py`.
