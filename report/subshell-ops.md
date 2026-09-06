# Explicit sub-shell operators

One term of the lacunary sum, compressed to [0,1].
R=4, N=80, h=0.05.

| n | scale | ‖F^{(n)}‖_HS² | λ_max |
|---|-------|----------------|-------|
| 0 | 1 | 0.558 | 0.500 |
| 1 | 2 | 0.525 | 0.353 |
| 2 | 4 | 0.494 | 0.250 |
| 3 | 8 | 0.429 | 0.176 |
| 4 | 16 | 0.253 | 0.159 |
| 5 | 32 | 0.096 | 0.120 |
| inv | 1/2 | 0.612 | 0.700 |
| Σ−inv | | 2.643 | 0.918 |

The first four shells are almost equal (~0.5), matching
Claude's 0.55–0.66 per term at coarser K-counts.

∑_n ‖F^{(n)}‖² = 2.43, ‖∑ F^{(n)}‖² = 3.29: the shells
**constructively** interfere. They are not an orthogonal
decomposition of the HS mass.

n≥8 is numerically dead at this h (scale 2^n h ≫ 1).
That is the same cutoff as the VP: n_max ~ log₂(1/h).

`python code/subshell_op.py`
