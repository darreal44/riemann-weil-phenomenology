<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# CST+Gauss is not C_A_lo on φ₀

Preregistered (`report/prereg-ql-cst-gamma.md`):
archimedean identification named in
`Qnm-is-not-Weil.md`. Constant mode.
Not RH.

## Execution

`python code/ql_cst_gamma.py`.
`report/ql-cst-gamma.json`.

arch_00 = Q_nm(0,0) with w₂=0
(CST + Gauss of D₂ against θ₀₀).
C_A_lo = log(q/π)+ψ(s₀)+∑_k e^{-2(s₀+k)L}/(s₀+k).
Γ∞ = log(q/π)+ψ(s₀).

| χ | μ | arch_00 | C_A_lo | gap | Γ∞ |
|---|---|---|---|---|---|
| χ₃ | 3 | −0.134 | −0.862 | **+0.728** | −1.132 |
| χ₃ | 5 | −0.392 | −1.011 | +0.619 | −1.132 |
| χ₅ | 3 | −0.159 | −1.399 | **+1.239** | −3.763 |
| χ₅ | 5 | −0.647 | −1.959 | +1.313 | −3.763 |

Gap is O(1). C_A_lo sits between
arch_00 and Γ∞ and moves toward Γ∞
as L grows. CST+Gauss on φ₀ is not
the Bochner constant and not ψ(s₀).

## Verdict: SURVIVE

The archimedean piece of Q_nm is not
identified with the classical Γ
pairing on the constant mode. p^k
filled the prime side at μ=5; this
piece is still open. Not RH.

Judge: `tests/test_ql_cst_gamma.py`.
