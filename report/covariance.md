# Covariance

The hats Φ (nz × N) are samples of the
window functions at the zeros. Then

    G = 2 Φᵀ Φ

is the covariance (Gram) of those sampling
functionals on the cosine basis. Q is the
same covariance written from primes + arch,
i.e. the explicit formula.

Empirical covariance of the 52 rows of Φ
at μ=11 is therefore G/2. Its spectrum is
λ_G / 2: 0.141, 0.874, 1.26, … — one small
principal component (the desert mode), then
a bulk of size O(1).

The residual covariance G−Q has a single
principal component (σ₀≈1.6, high-k). That
is not a second physical mode of the zeros;
it is the prime-tail / truncation mismatch.

No separate “covariance matrix” is missing
from the repo. Q and G are that object.
