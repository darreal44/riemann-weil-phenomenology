# Spectral convergence of the hat Galerkin

Q_NB is the compression of Q_L onto
hats n=0…NB. Min-max: λ_k(NB) decreases
in NB. The eigenfunction is analytic in
the bulk and only rough at the edge, so
the rate is exponential in NB until the
edge layer is resolved, then a plateau.

## −ln λ₀(NB), µ=16

    ell_0(NB)  ≈  ell_∞ − A exp(−NB / τ)

| L | ell_∞ | A | τ (hats) | seen at NB=16 |
|---|---|---|---|---|
| χ₁₃ | 10.8 | 4.3 | 5.4 | 10.6 |
| χ₅ | 33.9 | 32 | 4.8 | 33.1 |
| χ₃ | 60? | 52 | 11 | 47.9, still climbing |

χ₁₃ has already arrived. χ₅ is one hat
from the wall. χ₃'s ell_∞ is an
extrapolation through a regime where
float64 / dps=22 already loses λ₀
(sign flip at NB=16 in numpy). Trust
the shape, not the 60.

## The rest of the spectrum

χ₅, λ_k(NB):

| NB | λ₀ | λ₁ | λ₂ |
|---|---|---|---|
| 2 | 2.3×10⁻⁶ | 2.3×10⁻³ | 0.52 |
| 8 | 1.6×10⁻¹² | 2.8×10⁻⁷ | 5.7×10⁻³ |
| 16 | 4.3×10⁻¹⁵ | 5.6×10⁻⁹ | 7.1×10⁻⁴ |

Each new pair of hats peels another
decade off the small end and leaves
the bulk O(1) in place. λ₂ stays in
the Haar median; it is not converging
to zero. Only the needle and the first
rung keep dropping.

## What "converged" means

N_eff saturates by NB=8 (τ≈3).
ell_0 saturates 4–6 hats later (τ≈5).
The operator on L²[0,L] still has a
continuous family of larger modes; the
hat basis is complete, those modes are
just not the lemma.

Do not read χ₃'s climbing ell_0 as
"Q_L has λ₀=0". It is the edge layer
asking for more hats and more digits,
the same phenomenon as C → 1/(4e)
wanting four modes on ζ.
