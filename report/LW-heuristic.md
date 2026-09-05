# Additive Slepian on every sub-Nyquist gap

sum_j −log(1−λ₊(|gap_j|,τ)), gaps in t<80.

| μ | K | ∑ Slepian | ∑+log K | ell |
|---|---|-----------|---------|-----|
| 8 | 1 | 1.90 | 1.90 | 0.16 |
| 11 | 1 | 2.31 | 2.31 | 1.26 |
| 18 | 5 | 9.70 | 11.3 | 3.75 |
| 22 | 6 | 12.3 | 14.1 | 5.60 |
| 38 | 12 | 25.8 | 28.3 | 12.2 |

The sum *overcounts* by ~2 (holes are not
independent). log K is only O(1) and does
not close the gap. Landau–Widom’s log K is
a count of eigenvalues near 1, not a formula
for λ_min(Gram).

Useful: the one-hole bound fails when K>1;
the naive sum is a loose ceiling, not ell.
A union operator χ_E P χ_E with E=all
sub-Nyquist gaps is the next matrix to build
if we continue — not a sum of 1-D Slepians.
