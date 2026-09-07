<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# Quorum at μ=7: χ₃ is not alone; χ₈ and χ₁₇ still take

Preregistered (`report/prereg-ql-schur-quorum-mu7.md`):
Q_pk, cap √2, six χ, μ=7, ns=[2,3,4,5].
T infinite. Not RH.

## Execution

`python code/ql_schur_quorum_mu7.py`.
`report/ql-schur-quorum-mu7.json`.
χ₃ H₁₆ matches #73.

| χ | χ(2) | s₀ | taken at h | S_lo (best) |
|---|---|---|---|---|
| χ₃ | −1 | 3/4 | — | −0.45 (h=24) |
| χ₅ | −1 | 1/4 | **24** | +4.0×10⁻⁶ |
| χ₄ | 0 | 3/4 | **24** | +1.1×10⁻⁶ |
| χ₈ | 0 | 1/4 | **8, 16, 24** | +5.0×10⁻⁴ (h=8) |
| χ₇ | +1 | 3/4 | — | −1.28 (h=16) |
| χ₁₇ | +1 | 1/4 | **4, 8, 16, 24** | +0.039 (h=4) |

Four of six still take. χ₃ and χ₇
do not. The method is not dead.
The hard cells at μ=7 are the two
odd characters with a deep well,
not every (s₀, χ(2)) cell. χ₅/χ₄
are slivers at h=24, not comfortable.
A take of χ₈ or χ₁₇ is not
Weil-positive (one L).

## Verdict: SURVIVE

χ₃ is not the unique obstruction.
χ₇ fails too. χ₈ and χ₁₇ take.
Not (∀ χ). Not (∀ L). Not RH.

Judge: `tests/test_ql_schur_quorum_mu7.py`.
