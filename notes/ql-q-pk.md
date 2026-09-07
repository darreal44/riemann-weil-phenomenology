# Q_pk: primes and p^k, 1<n<μ

Preregistered (`report/prereg-ql-q-pk.md`):
Q_pk = A − ∑ Λ(n)χ(n)n^{-1/2} θ(log n)
over 1<n<μ. Not RH.

## Execution

`python code/ql_q_pk.py`.
`report/ql-q-pk.json`.

| μ | interior n | vs |
|---|---|---|
| 3 | [2] | = Q_nm |
| 3.5 | [2, 3] | = Q_window |
| 5 | [2, 3, **4**] | ΔH₀₀=**−0.0961** |

w₄ = log 2 / 2 = 0.347, χ₃(4)=1.
ΔH₀₀ matches `pk-on-4plane.md` (−0.096).
2³=8>5, so 4 is the only extra power
at μ=5.

## Verdict: SURVIVE

The prime side at μ=5 includes 2².
H₀₀ shift is negative. The 4×4 is
the next note. Not Weil (archimedean
still CST+D₂). Not RH.

Judge: `tests/test_ql_q_pk.py`.
