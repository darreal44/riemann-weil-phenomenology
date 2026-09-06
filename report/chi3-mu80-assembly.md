# χ₃ µ=80: not a basis wall, a truncated Euler product

spectro.py assembled the prime-side Q
from a hardcoded list

    2, 3, 5, …, 37.

At µ=80 that drops ten primes

    41, 43, 47, 53, 59, 61, 67, 71, 73, 79

of total weight Σ (log p)/√p = 5.33.
The hole is O(1) in the matrix, so
λ₀ = −0.82 at NB=26 and at NB=80
alike. Raising the basis cannot
fix a missing Euler factor.

scan_s.py already walks every
n ≤ µ that is a prime power of a
prime ≤ 83. Same window, NB=8,
dps=28:

    λ₀ = 3.75×10⁻²³,  ℓ = 51.6,  N_eff = 2.66

matching the stable row of
`run-chi3-wall-taper16.md`.
Grok’s ℓ = 111 is the same
assembly at larger NB.

## Fix

spectro.py now sieves all primes
≤ µ and builds the towers p^k ≤ µ.
edge_value_scan no longer caps
NB at 26 for µ ≥ 60.

Re-run after pull:

    python code/edge_value_scan.py --workers 8 --force chi3:80
    python code/scan_s.py chi3 80 24 48
