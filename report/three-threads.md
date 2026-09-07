# Three threads: 2-adic mass, Maass primes, odd Chebyshev

## 2-adic mass

Closed as a *grid* failure
(`2adic-numeric-lock.md`).
Λ=16 walked through 0.49 and 0.71
and landed at w2≈1.08. Haar /
Theorem 4 still says 1/√2 against
d*λ. No further Fmat point. The
analytic mass is the lock, not
the integral.

## Maass, prime side

Code path exists
(`scan_q_maass.py`,
`maass-prime-side.md`).
Smoke: lam0=−0.87, N_eff=2.41.
Shape of the kernel is right;
scale / Frullani / CST is not.
Matching Gram is the same class
of work as GL2_FIX. Do not read
a depth from the raw lam0.

## Odd Chebyshev

Even a^{(6)} is locked at 324.5
on (0.05,1) (`a6-chebyshev.md`).
Odd integrand (`av_a6_odd.py`):
max|a^{(6)}| on [0.05,1] *climbs*
with N (3e3 → 2e5 → 4e6) and
sits at the endpoint. Gauss
mid-node stays O(10)–O(50).
Runge at y=1, not a consensus
M. The Gauss-3 remainder for
#90 is not certified by this
Chebyshev.

Not Weil. Not RH.
