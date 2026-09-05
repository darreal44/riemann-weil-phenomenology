# Prime-side Q for GL(2)

`code/scan_q_gl2.py` — a_n from gp/`ellan`, two attempts
for the archimedean panel copied from scan_s.

Smoke 11a1, μ=11, N=25:

| shift | weight | λ0 |
|-------|--------|----|
| Re=1 | a_n / n | −2.58 |
| Re=1/2 | a_n / √n | −3.55 |

Both indefinite. a_n are not the issue (table matches Cremona).
The Dirichlet archimedean (s0, CST, D2) does not transport to
Γ(s) (2π)^{-s} N^{s/2}. Same class of failure as `scan_s zeta`
with q=1.

Working GL(2) object remains the **zero-side Gram**
(`scan_gl2.py`, `gl2-gram-slopes.md`). Writing Q requires
the explicit formula for L(E,s) with the correct Γ-derivative
panel, not a copy of χ.
