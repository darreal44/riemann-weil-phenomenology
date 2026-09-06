# Bulk of φ is Gaussian; edge is the 4-term wall

µ=11, cosine reconstruction.

    ψ(L/2) = 1.507
    ψ(t) ≈ 1.507 exp(−8.58 (t − L/2)²)     on 0.25 L … 0.75 L
    sech(5.32 (t−L/2)) is worse in the shoulders.

| t/L | ψ | gauss/ψ | sech/ψ |
|---|---|---|---|
| 0.25 | 0.064 | 1.09 | 1.95 |
| 0.40 | 0.95 | 0.97 | 0.82 |
| 0.50 | 1.51 | 1.00 | 1.00 |
| 0.75 | 0.064 | 1.09 | 1.95 |
| 0.20 | 0.013 | 1.41 | 5.2 |

Autocorrelation of a Gaussian is a Gaussian: that
is the y² side of the lemma, valid in the bulk
of the window.

The y e^y side is the 4-mode Dirichlet wall
that forces ψ(0)=e^{−s/2} instead of the
Gaussian tail e^{−8.58 (L/2)²} ≈ e^{−12.3},
which is in the same decade as the true edge
e^{−23} only after the extra cancellation.
The interpolation in Claude §123 is this
split: Gaussian bulk, 4-mode edge.
