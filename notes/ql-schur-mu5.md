<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# Schur at μ=5: χ₃ 4-plane is negative

Preregistered (`report/prereg-ql-schur-mu5.md`):
L=log 5. Interior primes {2,3}.
log 2 < L/2, so ‖Θ(log 2)‖≤2.
Six-character quorum, h-grid
2,4,8,16,20,24. T infinite. Not
Galerkin of W_L. Not RH. Not a
disproof of RH.

## Execution

`python code/ql_schur_mu5.py`.
`report/ql-schur-mu5.json`.
Gauss panels 16/32/64 agree on
χ₃ H to 1e-8.

| χ | h=2 S_lo | h=4 | h=8 | λ_H(4) | S_exact |
|---|---|---|---|---|---|
| χ₃ | −0.298 | −0.0005 | −0.0002 | **−1.6×10⁻⁴** | **−0.0002** |
| χ₅ | −1.075 | −3.59 | **+0.0023** | +0.0035 | +0.0032 |
| χ₄ | −0.035 | −0.0016 | **+0.0002** | +0.0013 | +0.0005 |
| χ₈ | **+0.0055** | +0.020 | +0.024 | +0.028 | +0.025 |
| χ₇ | **+0.025** | +0.067 | +0.083 | +0.090 | +0.087 |
| χ₁₇ | **+0.229** | +0.242 | +0.250 | +0.257 | +0.253 |

χ₃: λ_min of the 4×4 cosine block is
negative. That is Q on a subspace of
W_{log 5}, so c_L^*<0 for this
construction. Not a tail majorant.
χ₅ takes at h=8; χ₄ sliver at h=8;
χ₈, χ₇, χ₁₇ at h=2.

## Verdict: SURVIVE

This Q is not ≥0 on W_{log 5} for χ₃.
The same construction was positive at
log 3 and log 3.5. We do not identify
that sign change with a failure of RH.
The other five still have S_lo>0 at
some h. Not (∀ L). Not RH.

Judge: `tests/test_ql_schur_mu5.py`.

## Status

| Claim | Status |
|---|---|
| λ_min(H_4)<0 on χ₃ | judged, this note |
| S_lo>0 on χ₅ at h=8 | judged |
| S_lo>0 on χ₄ at h=8 | judged (sliver) |
| S_lo>0 on χ₈,χ₇,χ₁₇ at h=2 | judged |
| (∀ L) Q_L ≥ 0 | RH; not this note |
