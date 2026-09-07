<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# ρ_far crosses 1 between μ=5.5 and 6, χ₃

Preregistered (`report/prereg-ql-rhofar-mu.md`):
far-tail only, N_NEAR=32, cap √2.
No S_lo. Not RH.

## Execution

`python code/ql_rhofar_mu.py`.
`report/ql-rhofar-mu.json`.

| μ | t_atoms | qmin_far | π/2 | ρ_far |
|---|---|---|---|---|
| 5.0 | 1.040 | 3.560 | 1.571 | **0.747** |
| 5.5 | **1.759** | 3.532 | 1.571 | 0.957 |
| 6.0 | 1.760 | 3.223 | 1.571 | **1.049** |
| 6.5 | 1.760 | 3.231 | 1.571 | 1.046 |
| 7.0 | 1.760 | 3.057 | 1.571 | **1.105** |

t_atoms jumps at 5.5 (T₅ interior;
χ₃(3)=0 so no T₃). Hilbert π/2 is
fixed. Then qmin_far falls and ρ_far
crosses 1 on (5.5, 6]. That is why
Neumann has no S_lo on χ₃ after μ=5
on the H₁₆ grid: the far majorant
already exceeds the far diagonal.

## Verdict: SURVIVE

The wall is T₅ in t_atoms plus a
slow drop of qmin_far, not an
unidentified Γ. Not a take. Not RH.

Judge: `tests/test_ql_rhofar_mu.py`.
