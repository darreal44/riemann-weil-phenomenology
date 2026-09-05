# Variance of Maass a_n (Zenodo, n≤1000)

Sato–Tate for a Maass form (a_p = 2 cos θ): E[a_p]=0, E[a_p²]=1.
All n: products shrink the variance relative to the primes.

| form | R | var(n>1) | E[a_p²] | max\|a_p\| |
|------|---|---------|---------|------------|
| 1.0.1.1.1 | 9.53 | 0.415 | 0.915 | 1.85 |
| 1.0.1.10.1 | 19.48 | 0.998 | 0.940 | 1.94 |
| 1.0.1.100.1 | 45.95 | 1.054 | 1.037 | 1.95 |

168 primes ≤1000. E[a_p²] already near 1. No |a_p|>2
(Ramanujan–Petersson for GL₂).

The first form has smaller var on all n because many
composites sit near 0. That is multiplicativity, not a
different Sato–Tate.

Q would use a_n log p / √n on prime powers only; this
variance is not an input to ell.
