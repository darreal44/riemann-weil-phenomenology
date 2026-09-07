<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# Schur Neumann: sharper C, not Frobenius/δ

Preregistered (`report/prereg-ql-schur-neumann.md`):
the move named in `chi5-hankel-not-enough.md`
and `schur-diag-T.md`. T^{-1} near D^{-1}
via Neumann of the scaled Off, not ‖C‖_F²/δ.
Not Galerkin of W_L. Not RH.

## Execution

`python code/ql_schur_neumann.py`.
`report/ql-schur-neumann.json`.

T = D^{1/2}(I+A)D^{1/2}. Split A into near
(n=2..31, Gauss), coupling (Frobenius plus
Hankel tail), far (Hankel+Θ over qmin_far).
ρ = ‖[[ρ_N, ρ_B],[ρ_B, ρ_far]]‖₂. If ρ<1,

    S ≥ H − C D^{-1} C* / (1−ρ).

| χ | ρ | S_diag | S_lo |
|---|---|---|---|
| χ₅ | 0.521 | +0.0417 | **+0.0291** |
| χ₈ | 0.335 | +0.2427 | +0.2350 |
| χ₄ | 0.388 | +0.0680 | +0.0573 |
| χ₃ | 0.590 | +0.0076 | **−0.0086** |

S_diag matches `schur-diag-T.md` (+0.042).
The Frobenius/qmin majorant ate more than
λ_H and declared χ₅ dead even at Off_T=0.
Neumann keeps the actual C D^{-1} C*
(eats 0.011 of λ_H) and inflates by
1/(1−ρ)≈2.09.

## Verdict: SURVIVE

This bound takes W_{log 3} for χ₅ (even,
χ(2)=−1) and for χ₄ at h=2. χ₃ still
S_lo<0 (λ_H=0.0185 is too small). Not
every χ. Not (∀ L). Not RH.

Judge: `tests/test_ql_schur_neumann.py`.

## Status

| Claim | Status |
|---|---|
| S_lo>0 on χ₅ | judged, this note |
| Frobenius/δ was the obstruction, not C | judged (`schur-diag-T`) |
| S_lo>0 on χ₃ | **false** |
| c_L^* ≥ 0 for every χ | **open; not taken** |
| (∀ L) Q_L ≥ 0 | RH; not this note |
