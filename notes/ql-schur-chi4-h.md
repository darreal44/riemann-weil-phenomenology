<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# Schur χ₄ at larger h

Preregistered (`report/prereg-ql-schur-chi4-h.md`):
grid h=2,4,8,16,20,24. Same Off_T as #58.
C Gauss to M=40 plus Hankel tail 1/(2(i+j))²
(w₂=0; |Q|(n+m)≤1/2 on the computed block).
Not Galerkin of W_L. Not RH.

Named next in `chi8-vs-chi4-schur.md`.

## Execution

`python code/ql_schur_chi4_h.py`.
`report/ql-schur-chi4-h.json`.

| h | λ_min(H) | qmin | δ | ‖C‖_F | β |
|---|---|---|---|---|---|
| 2 | 0.0840 | 2.110 | +0.183 | 0.418 | −0.872 |
| 4 | 0.0731 | 2.741 | +0.974 | 0.418 | −0.106 |
| 8 | 0.0706 | 3.403 | +1.714 | 0.418 | −0.031 |
| 16 | 0.0699 | 4.080 | +2.434 | 0.419 | −0.002 |
| **20** | 0.0698 | 4.300 | +2.664 | 0.419 | **+0.0040** |
| 24 | 0.0697 | 4.481 | +2.851 | 0.419 | +0.0082 |

λ_H falls to the ladder floor (~0.070).
qmin is Q_{hh} and still climbing. ‖C‖_F
stays ~0.42 (Hankel tail of C saturates).
The #58 R-inflated C tail plateaus at
β≈−0.012 and would not take; the Hankel
tail is the one locked here.

## Verdict: SURVIVE

h* ∈ (16, 20]. This bound takes
W_{log 3} for χ₄. Together with #58 (χ₈),
both characters with χ(2)=0 on this
window are taken. χ(2)=−1 is another
line. Not (∀ L). Not RH.

Judge: `tests/test_ql_schur_chi4_h.py`.

## Status

| Claim | Status |
|---|---|
| β>0 on χ₄ at h=20 | judged, this note |
| β>0 at h≤16 | **false** |
| χ₈ still taken at h=2 | judged (#58) |
| c_L^* ≥ 0 for χ(2)=−1 | **open; not taken** |
| (∀ L) Q_L ≥ 0 | RH; not this note |
