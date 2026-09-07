Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).

# Neumann Q_pk at μ=7 and μ=8: the log 5 take does not extend

Preregistered (`report/prereg-ql-neumann-mu78.md`):
identified Q_pk, cap √2 of #72, χ₃,
heads 2..24. T infinite. Not RH.

## Execution

`python code/ql_schur_mu78.py`.
`report/ql-schur-mu78.json`.
λ_min(H₁₆) matches #72.

| μ | h | λ_H | ρ | S_lo |
|---|---|---|---|---|
| 7 | 2 | +6.9×10⁻⁴ | 1.27 | — |
| 7 | 16 | +4.8×10⁻⁹ | 1.19 | — |
| 7 | **24** | +4.0×10⁻⁹ | 0.957 | **−0.445** |
| 8 | 2 | +3.5×10⁻⁴ | 1.47 | — |
| 8 | 16 | +8.1×10⁻¹¹ | 1.30 | — |
| 8 | 24 | +7.2×10⁻¹¹ | 1.23 | — |

ρ≥1 except (μ=7, h=24). There the
bound exists and is largely negative.
t_atoms grew (T₅ at 7, T₇ at 8).
The sliver 10⁻⁹–10⁻¹¹ cannot carry
1/(1−ρ). Galerkin H_h stays +
(Courant from above). No S_lo>0.

## Verdict: SURVIVE

The take of W_log5 does not extend
to W_log7 or W_log8. Not Weil-positive.
Not Weil-negative. Not (∀ L). Not RH.

Judge: `tests/test_ql_schur_mu78.py`.
