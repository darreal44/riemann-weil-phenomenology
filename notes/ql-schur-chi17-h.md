# Schur χ₁₇: even χ(2)=+1 takes at h=2

Preregistered (`report/prereg-ql-schur-chi17-h.md`):
χ₁₇, q=17, d=17, s₀=1/4, χ(2)=+1,
w₂=+log 2/√2. Grid h=2,4,8,16,20,24.
T infinite. Not Galerkin of W_L. Not RH.

Last empty cell of (s₀, χ(2)) on this
window. Partner of χ₇ (odd +1) and of
χ₅ (even −1).

## Execution

`python code/ql_schur_chi17_h.py`.
`report/ql-schur-chi17-h.json`.

w₂=+0.4901, χ(2)=+1, s₀=1/4.
H₀₀=0.702, λ_H(2)=0.692.

| h | λ_min(H) | ρ | S_exact | S_lo | β |
|---|---|---|---|---|---|
| **2** | 0.6917 | 0.401 | +0.668 | **+0.649** | **+0.343** |
| 4 | 0.6684 | 0.394 | +0.664 | +0.660 | +0.533 |
| 8 | 0.6646 | 0.388 | +0.663 | +0.662 | +0.545 |
| 16 | 0.6634 | 0.379 | +0.663 | +0.663 | +0.552 |
| 20 | 0.6632 | 0.374 | +0.663 | +0.663 | +0.556 |
| 24 | 0.6631 | 0.364 | +0.663 | +0.663 | +0.544 |

Both bounds take at h=2. G_reg>0 and
q=17 make H fat; the atom +1 does not
dig a well. S_exact is a section, not
the certificate.

## Verdict: SURVIVE

This bound takes W_{log 3} for χ₁₇.
The six cells (s₀ ∈ {1/4, 3/4}) ×
(χ(2) ∈ {0, −1, +1}) each have one
representative taken. Not every χ
(other q). Not (∀ L). Not RH.

Judge: `tests/test_ql_schur_chi17_h.py`.

## Status

| Claim | Status |
|---|---|
| S_lo>0 on χ₁₇ at h=2 | judged, this note |
| β>0 on χ₁₇ at h=2 | judged |
| (s₀, χ(2)) table, one each | judged (six cells) |
| c_L^* ≥ 0 for every χ | **open; not taken** |
| (∀ L) Q_L ≥ 0 | RH; not this note |
