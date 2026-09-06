# χ₃ µ=80: certified window, Galerkin wall at NB=28

The −0.82 at every NB was a truncated
Euler product in spectro.py (primes
to 37). After the sieve, scan_s:

    NB=8  dps=28   λ₀ = +3.75×10⁻²³   ℓ = 51.6   N_eff = 2.66
    NB=24 dps=48   λ₀ = +5.60×10⁻⁴⁹   ℓ = 111.1   N_eff = 3.00
    NB=26 dps=56   λ₀ = +9.30×10⁻⁵²   ℓ = 117.5   N_eff = 3.01
    NB=28 dps=64   λ₀ = −1.18×10⁻⁵²            N_eff = 3.03

edge_value NB=24 dps=50: ℓ = 111.4,
edge = 108.93, R = +2.47, ℓ/edge = 1.023.

N_eff saturates at 3.00–3.01. Raising
dps does not flip NB=28 back to SPD.
Hats n≳27 see the cutoff µ=80 as a
hard wall; the Galerkin form picks up
a negative direction. This is *not*
a missing prime.

Last certified SPD window: **NB=26**.
Do not raise NB past 26 at µ=80.
µ=90 is a different cutoff; same
discipline (stop when N_eff has sat
and λ₀ changes sign).
