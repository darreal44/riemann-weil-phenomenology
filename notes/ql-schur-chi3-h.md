<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# Schur χ₃ at larger h: Neumann, not β

Preregistered (`report/prereg-ql-schur-chi3-h.md`):
grid h=2,4,8,16,20,24, same as χ₄.
Two bounds, same Q_nm, T infinite.
Not Galerkin of W_L. Not RH.

Combine `ql-schur-chi4-h.md` (raise h)
with `ql-schur-neumann.md` (T^{-1} near
D^{-1}). β alone does not copy χ₄.

## Execution

`python code/ql_schur_chi3_h.py`.
`report/ql-schur-chi3-h.json`.

β = λ_H − ‖C‖_F²/δ, Off_T = Hankel π/2
+ HS rem + T₂. C Gauss to M=40 plus
`c_tail_sq`.

| h | λ_min(H) | qmin | δ | ‖C‖_F | β |
|---|---|---|---|---|---|
| 2 | 0.01850 | 1.718 | **−0.699** | 0.416 | — |
| 4 | 0.01123 | 2.101 | **−0.155** | 0.483 | — |
| 8 | 0.00998 | 3.088 | +0.908 | 0.536 | −0.307 |
| 16 | 0.00975 | 3.677 | +1.541 | 0.582 | −0.210 |
| 20 | 0.00972 | 3.752 | +1.626 | 0.621 | −0.228 |
| 24 | 0.00971 | 3.971 | +1.851 | 0.643 | −0.214 |

λ_H falls to the S_exact floor (~0.0097).
‖C‖_F climbs (T₂ in the C tail); it did
not saturate as on χ₄. β never positive.

Neumann S_lo, N_NEAR=max(32,h+16):

| h | N | ρ_N | ρ | S_diag | S_exact | S_lo |
|---|---|---|---|---|---|---|
| 2 | 32 | 0.283 | 0.590 | +0.0076 | +0.0097 | **−0.0086** |
| **4** | 32 | 0.176 | 0.566 | +0.0095 | +0.0097 | **+0.0070** |
| 8 | 32 | 0.134 | 0.553 | +0.0097 | +0.0097 | +0.0092 |
| 16 | 32 | 0.110 | 0.539 | +0.0097 | +0.0097 | +0.0096 |
| 20 | 36 | 0.107 | 0.516 | +0.0097 | +0.0097 | +0.0096 |
| 24 | 40 | 0.103 | 0.513 | +0.0097 | +0.0097 | +0.0096 |

h=2 reproduces #61. Raising h moves
n=2,3 from T into H: ρ_N drops
0.283→0.176, S_diag catches S_exact,
and 1/(1−ρ) no longer eats the sliver.
S_exact is a section, not a certificate
(`chi3-S-exact.md`). S_lo>0 is.

## Verdict: SURVIVE

h* ∈ (2, 4]. This bound takes
W_{log 3} for χ₃. Together with #58
(χ₈), #60 (χ₄), #61 (χ₅), the four
locked characters on this window are
taken. Not every χ. Not (∀ L). Not RH.

Judge: `tests/test_ql_schur_chi3_h.py`.

## Status

| Claim | Status |
|---|---|
| S_lo>0 on χ₃ at h=4 | judged, this note |
| β>0 on χ₃ at h≤24 | **false** (T₂, ‖C‖ climbs) |
| S_lo>0 at h=2 | **false** (#61) |
| χ₈, χ₄, χ₅ still taken | judged (#58,#60,#61) |
| c_L^* ≥ 0 for every χ | **open; not taken** |
| (∀ L) Q_L ≥ 0 | RH; not this note |
