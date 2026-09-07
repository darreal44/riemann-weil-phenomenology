# T₅ on H₄ at μ=5.1: no jump of λ_min

Preregistered (`report/prereg-ql-T5-H4.md`):
Q_pk, μ=5 vs 5.1, six characters, 4×4.
Not Neumann. Not RH.

## Execution

`python code/ql_T5_H4.py`.
`report/ql-T5-H4.json`.
ns(5)=[2,3,4], ns(5.1)=[2,3,4,5].

| χ | H₄(5) | H₄(5.1) | H₀₀ 5→5.1 |
|---|---|---|---|
| χ₃ | +1.4×10⁻⁵ | **+1.3×10⁻⁵** | 0.070→0.078 |
| χ₅ | +0.00117 | +0.00099 | 0.218→0.210 |
| χ₄ | +0.00132 | +0.00102 | 0.298→0.284 |
| χ₈ | +0.0281 | +0.0259 | 0.226→0.238 |
| χ₇ | +0.0572 | +0.0532 | 0.204→0.212 |
| χ₁₇ | +0.210 | +0.200 | 0.326→0.325 |

χ₃ H₀₀ rises (χ(5)=−1, T₅ helps the
constant) but λ_min does not jump by
10⁻². Origin’s +0.017 on H₀₀ does not
move the well. All six H₄ stay >0.
χ₄ H₀₀ falls (χ(5)=+1), as named.

## Verdict: SURVIVE

T₅ is not the cause of μ* and does
not flip H₄ after p^k. Not RH.

Judge: `tests/test_ql_T5_H4.py`.
