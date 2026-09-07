<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# χ₇ vs χ₁₇ at μ=7: same t_atoms, split is qmin_far (s₀)

Preregistered (`report/prereg-ql-chi7-vs-chi17.md`):
far pieces N_NEAR=32. Both χ(2)=+1.
χ₇(7)=0. Not a take. Not RH.

## Execution

`python code/ql_chi7_vs_chi17.py`.
`report/ql-chi7-vs-chi17.json`.

| | χ₇ | χ₁₇ |
|---|---|---|
| s₀ | 3/4 | 1/4 |
| χ(2) | +1 | +1 |
| χ(7) | **0** | −1 |
| t_atoms | 2.394 | **2.394** |
| qmin_far | 4.494 | **5.381** |
| ρ_far | 0.893 | 0.746 |

t_atoms identical: same |w| on
{2,3,4,5}. T₇ is not in ns at μ=7
and would be zero on χ₇ anyway.
Both ρ_far<1 at N_NEAR=32. The gap
is qmin_far (arch diagonals, s₀).
χ₇'s failure at h=16 (#76, S_lo=−1.28)
is a deep head well, not a far wall
and not T₇. χ₁₇ dies later, at μ=8,
when T₇ is interior (`ql-chi817-mu8`).

## Verdict: SURVIVE

The +1 pair splits on s₀, not on
t_atoms. Not a take. Not RH.

Judge: `tests/test_ql_chi7_vs_chi17.py`.
