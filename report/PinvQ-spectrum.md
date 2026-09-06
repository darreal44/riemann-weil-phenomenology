# Spectrum of P⁻¹Q — χ₂₉, μ=38, n=25

| P | λ_min | médiane | λ_max | # in [0.5,1.5] | κ |
|---|---|---|---|---|---|
| I (raw Q) | 7.9e-6 | 4.51 | 7.52 | 2 | 9.6e5 |
| Jacobi D | 5.0e-5 | 1.00 | 2.88 | 19 | 5.8e4 |
| Gauss–Seidel | 9.9e-5 | 0.97 | 1.11 | 21 | 1.1e4 |
| block Jacobi | 2.3e-3 | 1.00 | 2.00 | 21 | 868 |

Raw Q is a bulk [1, 7.5] plus one
well. Every preconditioner leaves
that well isolated and packs the
bulk toward 1.

Block Jacobi is the sharpest pack:
21 of 25 eigenvalues equal 1 to
three digits. Four outliers remain:

    0.0023,  0.32,  1.68,  2.00

— the C-coupling of the 3-hat plane
to T. GS packs almost as tightly
(max 1.11) but the well stays at
10⁻⁴, so ρ(I−P⁻¹Q) = 0.9999.

The isolated small eigenvalue of
P⁻¹Q tracks λ₀(Q) times a slow
factor:

| μ | λ₀(Q) | GS₀ | BJ₀ |
|---|---|---|---|
| 11 | 0.30 | 0.38 | 0.66 |
| 22 | 4.1e-3 | 0.011 | 0.056 |
| 38 | 7.9e-6 | 9.9e-5 | 2.3e-3 |

P⁻¹Q never hides the well. It
makes the bulk trivial and leaves
one (GS, Jacobi) or four (block J)
non-trivial modes — exactly the
IR plane we already isolate by
Schur.
