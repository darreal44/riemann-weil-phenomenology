<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# χ₇ take dies on (5.1, 7]; survives T₅ as a sliver

Preregistered (`report/prereg-ql-chi7-mu.md`):
μ=3, 3.5, 5, 5.1, 7. #64 vs #76.
Identified Q_pk. Not RH.

## Execution

`python code/ql_chi7_mu.py`.
`report/ql-chi7-mu.json`.
S_lo(2)=+0.276 at μ=3 matches #64.

| μ | taken h | S_lo (best) |
|---|---|---|
| 3.0 | 2..24 | +0.276 (h=2) |
| 3.5 | 2..24 | +0.098 (h=2) |
| 5.0 | 8, 16, 24 | +0.050 (h=24) |
| **5.1** | **24** | **+0.035** |
| 7.0 | — | −1.28 (h=16) |

Unlike χ₃, T₅ arrival does not kill
χ₇: a sliver remains at h=24. The
take is dead by μ=7 (T₅ drifted,
not T₇: 7 is not interior and
χ₇(7)=0). first_dead=7 on this grid.

## Verdict: SURVIVE

Death on (5.1, 7], not at T₅
arrival. Not Weil-positive. Not
(∀ L). Not RH.

Judge: `tests/test_ql_chi7_mu.py`.
