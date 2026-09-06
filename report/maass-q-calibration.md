# Maass Q calibration — Q00 versus G00

`python code/calibrate_maass_q.py`

maass1, μ=6, first zero γ₁=17.0, G00=0.066.

| s0 convention | Λ weight | arch | prim | Q00 |
|---|---|---|---|---|
| ½ ± iR (Γ_R arg) | /√n | 2.22 | −0.89 | 3.10 |
| ½ ± iR | /n | 2.22 | −0.59 | 2.81 |
| ¼ ± iR/2 (Γ(s/2) arg) | /√n | 0.82 | −0.89 | 1.71 |
| ¼ ± iR/2 | /n | 0.82 | −0.59 | 1.41 |
| GL2 real (½, 1) | /√n | −3.19 | −0.89 | −2.30 |

No cell is within a factor 10 of G00=0.066.
The prime piece is O(1); the Gram constant
mode is O(10⁻²). Recycling the Dirichlet /
weight-2 panel cannot cancel that.

λ₀ of `scan_q_maass` is negative for the
same reason: the form is not the Maass
Weil pairing, only a transplanted kernel.

Next calibration step that could work:
write the archimedean term from
ψ((½ + it ± iR)/2) directly (digamma),
not from the e^{-2 s0 y}/(1−e^{-2y})
panel built for Γ_R(s) Γ_R(s+1).
