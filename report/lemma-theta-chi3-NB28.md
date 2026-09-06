# χ₃ µ=80: certified window, and what is not a wall

The −0.82 at every NB was a truncated
Euler product in `spectro.py` (primes
hardcoded to 37). After the sieve:

    scan_s   NB=24 dps=48   λ₀ = +5.60×10⁻⁴⁹   ℓ = 111.1   N_eff = 3.00
    edge     NB=24 dps=50   λ₀ = +4.18×10⁻⁴⁹   ℓ = 111.4   edge = 108.93
                            R = +2.47   ℓ/edge = 1.023

That is the same family as χ₃ µ=38
(ℓ/edge = 1.024, R = 3.32). Do not
compare raw ℓ = 111 to ℓ(µ=38) = 140:
the latter used 66 hats. Here N_eff
has just reached 3; ℓ is still
climbing with NB (52 → 69 → 85 → 98
→ 111 from NB=8 to 24).

## What remains delicate

Older rows before the sieve:

    NB=26 dps=56   λ₀ = +9.3×10⁻⁵²
    NB=28 dps=64   λ₀ = −1.2×10⁻⁵²

Those signs were taken on an
incomplete prime list or on a
quadrature that is not the current
`scan_s`. Production window:

    **NB=24, dps=50.**

µ=90 is no longer forbidden by an
assembly axiom; it still needs a
sieve up to 90 and dps above −ln λ₀.
Default in `edge_value_scan` for
µ≥60 is NB=24 dps=50.
