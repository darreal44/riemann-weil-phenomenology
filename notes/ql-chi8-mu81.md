<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# χ₈ take dies at 2³ (μ=8.1)

Preregistered (`report/prereg-ql-chi8-mu81.md`):
last quorum cell still taking at μ=8
h=24. μ=8, 8.1, 9.1. Identified Q_pk.
Not RH.

## Execution

`python code/ql_chi8_mu81.py`.
`report/ql-chi8-mu81.json`.
μ=8 h=24 matches #77 (+2.86×10⁻⁴).

| μ | ns | h=16 | h=24 |
|---|---|---|---|
| 8.0 | 2,3,4,5,7 | — ρ=1.03 | **+2.86×10⁻⁴** |
| **8.1** | +8=2³ | −4.63 ρ=0.98 | **−1.32** ρ=0.98 |
| 9.1 | +9=3² | — ρ=1.20 | — ρ=1.10 |

The take is gone as soon as 2³ is
interior. 3² is after a corpse.
Not Weil-positive.

## Verdict: SURVIVE

No tracked quorum take survives
μ=8.1. Not (∀ L). Not RH.

Judge: `tests/test_ql_chi8_mu81.py`.
