<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# χ₇ sliver flickers on (5.1, 7]; dead by 6.5

Preregistered (`report/prereg-ql-chi7-mu57.md`):
h=16, 24. Identified Q_pk. Not RH.

## Execution

`python code/ql_chi7_mu57.py`.
`report/ql-chi7-mu57.json`.

| μ | h=16 | h=24 |
|---|---|---|
| 5.1 | — ρ=1.01 | **+0.035** ρ=0.95 |
| 5.5 | — ρ=1.09 | −97 ρ=0.999 |
| **6.0** | −0.044 ρ=0.94 | **+0.010** ρ=0.92 |
| 6.5 | — ρ=1.13 | — ρ=1.03 |
| 7.0 | −1.28 ρ=0.98 | — ρ=1.11 |

Not monotone. ρ hovers at 1. The
sliver at 6.0 is 10⁻², not a
comfortable take. Dead at 6.5 and 7.
Not Weil-positive.

## Verdict: SURVIVE

Death of a stable take is on
(5.1, 6.5]. Not (∀ L). Not RH.

Judge: `tests/test_ql_chi7_mu57.py`.
