<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# χ₃ take dies at T₅ arrival (μ=5.1)

Preregistered (`report/prereg-ql-chi3-mu51.md`):
μ=5 vs 5.1, h=16 and 24, ρ_far at
N_NEAR=32. Identified Q_pk. Not RH.

## Execution

`python code/ql_chi3_mu51.py`.
`report/ql-chi3-mu51.json`.
t_atoms 1.040 → **1.760** (5 interior).
ρ_far 0.747 → 0.969.

| μ | h=16 | h=24 |
|---|---|---|
| 5.0 | S_lo=**+5.04×10⁻⁶** ρ=0.80 | +7.00×10⁻⁶ ρ=0.75 |
| **5.1** | — ρ=1.024 | **−5.4×10⁻⁵** ρ=0.96 |

The take is gone as soon as n=5 is
interior, even with θ(log 5) at the
edge. Drift of 5 is not required.
Not Weil-positive.

## Verdict: SURVIVE

T₅ arrival kills the W_log5 sliver.
Dead on (5, 5.1]. Not (∀ L). Not RH.

Judge: `tests/test_ql_chi3_mu51.py`.
