<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# χ₄ and χ₅ slivers die at μ=8 under T₇

Preregistered (`report/prereg-ql-chi45-mu8.md`):
slivers at μ=7 h=24. μ=8, T₇ interior.
Identified Q_pk. Not RH.

## Execution

`python code/ql_chi45_mu8.py`.
`report/ql-chi45-mu8.json`.
ns=[2,3,4,5,7].

| χ | h=16 | h=24 |
|---|---|---|
| χ₄ | — ρ=1.20 | — ρ=1.05 |
| χ₅ | — ρ=1.23 | — ρ=1.10 |

No S_lo>0 at any h. ρ≥1 on the
whole grid. Same pattern as χ₁₇
(#77): T₇ kills the μ=7 sliver.
No take at h=2,4,8.

## Verdict: SURVIVE

The 10⁻⁶ slivers do not survive
the next atom. Not Weil-positive.
Not (∀ L). Not RH.

Judge: `tests/test_ql_chi45_mu8.py`.
