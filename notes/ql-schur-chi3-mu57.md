<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# χ₃ Neumann take on (5, 7] dies at μ=5.5

Preregistered (`report/prereg-ql-schur-chi3-mu57.md`):
identified Q_pk, cap √2, h=16 and 24.
T infinite. Not RH.

## Execution

`python code/ql_schur_chi3_mu57.py`.
`report/ql-schur-chi3-mu57.json`.
H₁₆ matches #72/#75.

| μ | h=16 S_lo | h=24 S_lo | ρ(16) |
|---|---|---|---|
| **5.0** | **+5.04×10⁻⁶** | **+7.00×10⁻⁶** | 0.80 |
| 5.5 | — (ρ=1.02) | — (ρ=1.00) | 1.02 |
| 6.0 | — | −17.3 (ρ=0.997) | 1.11 |
| 6.5 | — | — | 1.11 |
| 7.0 | — | −0.45 | 1.19 |

take_mu at h=16 is **{5}** only.
Already dead at 5.5, the first grid
point with 5 interior. Not Weil-positive.

## Verdict: SURVIVE

The W_log5 take does not live on
(5, 7]. It is a single-L sliver.
Not (∀ L). Not RH.

Judge: `tests/test_ql_schur_chi3_mu57.py`.
