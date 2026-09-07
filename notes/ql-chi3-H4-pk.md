# χ₃ H₄ with p^k: the 4-plane stays positive

Preregistered (`report/prereg-ql-chi3-H4-pk.md`):
same μ-grid as #68, Q_pk not Q_window.
No Neumann. Not RH.

Origin (`pk-on-4plane.md`) from H₀₀
alone: ΔH₀₀=−0.096, “not a rescue”.
This is the 4×4.

## Execution

`python code/ql_chi3_H4_pk.py`.
`report/ql-chi3-H4-pk.json`.
μ=3.5 matches #68 (no p^k yet).
Gauss 16/32/64 agree at μ=5 to 1e-10.

| μ | n | λ_min(H₂) | λ_min(H₄) |
|---|---|---|---|
| 3.50 | 2,3 | +0.00762 | +0.00268 |
| 4.00 | 2,3 | +0.00298 | +0.00063 |
| 4.25 | 2,3,4 | +0.00141 | +0.00026 |
| 4.75 | 2,3,4 | +0.00016 | +0.00004 |
| **5.00** | 2,3,4 | +0.00019 | **+0.000014** |

H₄(5) was −1.6×10⁻⁴ without 2².
With 2² it is **+1.4×10⁻⁵**. Filling
p^k *does* rescue the 4-plane sign.
H₀₀ still drops (0.166→0.070); the
min eigenvector is not the constant.
No crossing on this grid. μ=4 is
still not a sign change.

## Verdict: SURVIVE

The primes-only H₄<0 at μ=5 was an
artifact of omitting 2². The 4-plane
of Q_pk stays positive through μ=5.
Still not Weil (CST vs Γ). Not (∀ L).
Not RH.

Judge: `tests/test_ql_chi3_H4_pk.py`.
