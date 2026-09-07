# Neumann Q_pk at μ=5, χ₃: sliver eaten at small h

Preregistered (`report/prereg-ql-schur-pk-mu5.md`):
same Neumann as #67, Q_pk. T infinite.
Not Galerkin of W_L. Not RH.

## Execution

`python code/ql_schur_pk_mu5.py`.
`report/ql-schur-pk-mu5.json`.

| h | λ_H | ρ | S_lo |
|---|---|---|---|
| 2 | +1.85×10⁻⁴ | 0.915 | **−1.31** |
| 4 | +1.43×10⁻⁵ | 0.897 | **−1.19** |
| 8 | +1.04×10⁻⁵ | 0.888 | −8.5×10⁻⁵ |
| 16 | +8.3×10⁻⁶ | 0.873 | +2.5×10⁻⁶ |
| 24 | +7.9×10⁻⁶ | 0.819 | +6.6×10⁻⁶ |

S_lo(2) and S_lo(4) are negative. The
heads that took log 3 and log 3.5 do
not take. The 10⁻⁶ at h≥16 sits under
the archimedean gap (0.6) and is not
a certificate.

## Verdict: SURVIVE

p^k does not give a Neumann take of
W_{log 5} for χ₃ at h=2 or 4. Not RH.

Judge: `tests/test_ql_schur_pk_mu5.py`.
