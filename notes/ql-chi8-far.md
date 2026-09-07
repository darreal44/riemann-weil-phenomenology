<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# KILL: 2³ does not jump χ₈ t_atoms (χ₈(8)=0)

Preregistered (`report/prereg-ql-chi8-far.md`):
predicted t_atoms jumps at μ=8.1.
Far pieces N_NEAR=32. Not RH.

## Execution

`python code/ql_chi8_far.py`.
`report/ql-chi8-far.json`.

| μ | ns | t_atoms | qmin_far | ρ_far |
|---|---|---|---|---|
| 8.0 | 2,3,4,5,7 | 2.0895 | 3.914 | 0.948 |
| 8.1 | +8 | **2.0895** | 4.175 | **0.888** |

χ₈(8)=0 (conductor 8), so w₈=0.
2³ is in ns but not in t_atoms.
ρ_far *drops*. The take death at
8.1 (#78, S_lo=−1.32) is a head /
Schur well, not a far-atom wall.
Opposite of T₅ on χ₃.

## Verdict: KILL

The predicted t_atoms jump is false.
Not a take. Not RH.

Judge: `tests/test_ql_chi8_far.py`.
