<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# CST 4-plane vs 2 m_Q(ω_n): signs disagree

Preregistered (`report/prereg-ql-arch-4plane.md`):
χ₃, μ=5. Diagonals Q_nn^{arch} vs
2 m_Q(ω_n). Hybrid = 2 m_Q on the
diag, CST off-diag, plus p^k.
Not Fourier of θ. Not RH.

## Execution

`python code/ql_arch_4plane.py`.
`report/ql-arch-4plane.json`.

| n | ω_n | 2 m_Q | Q_nn^{arch} | gap |
|---|---|---|---|---|
| 0 | 0 | −1.011 | −0.392 | **−0.619** |
| 1 | 3.90 | +0.636 | +0.869 | −0.233 |
| 2 | 7.81 | +1.319 | +1.440 | −0.121 |
| 3 | 11.7 | +1.722 | +1.804 | −0.082 |

λ_min(H₄) CST+p^k = **+1.43×10⁻⁵** (#69).
λ_min(H₄) hybrid = **−0.577**.

Signs disagree. The p^k rescue of the
4-plane lives in CST+D₂, not in the
Bochner/C_A diagonals. Gaps shrink
with n (high modes agree more).

## Verdict: SURVIVE

The 4-plane sign is not identified
with m_Q. Still not Weil. Not RH.

Judge: `tests/test_ql_arch_4plane.py`.
