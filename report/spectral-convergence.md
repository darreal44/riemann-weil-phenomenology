# Spectral convergence of the Galerkin Q_N

N = NB+1 hats. ell_k = −ln|λ_k|.
n_small = #{λ ∈ (0, 10⁻³)}.

## χ₅ µ=16 — saturation

| N | ℓ₀ | ℓ₁ | ℓ₂ | n_small |
|---|---|---|---|---|
| 3 | 13.0 | 6.1 | 0.7 | 1 |
| 5 | 18.9 | 9.1 | 1.7 | 2 |
| 7 | 24.4 | 13.8 | 4.6 | 2 |
| 9 | 27.2 | 15.1 | 5.2 | 2 |
| 13 | 31.5 | 18.0 | 6.9 | 3 |
| 17 | 33.1 | 19.0 | 7.3 | 3 |

ℓ₀ gains 20 nats from N=3 to 17, then
+1.6 from 13 to 17. N_eff frozen at
2.13–2.14 from N=7. The ground
state has converged as a *shape*;
the value still creeps because each
new hat adds a small variational
correction. This is the window
where the 2-plane is the whole
bottom.

## χ₃ µ=16 — not yet flat

| N | ℓ₀ | n_small | N_eff |
|---|---|---|---|
| 3 | 17.1 | 1 | 2.02 |
| 5 | 24.1 | 3 | 2.19 |
| 9 | 34.8 | 3 | 2.28 |
| 13 | 42.7 | 4 | 2.31 |
| 17 | 47.9 | 4 | 2.32 |

+5 nats from N=13 to 17. Shape
frozen (N_eff), depth not. Edge
value 52.7 at a larger basis
(NB=46) sits 5 nats above 47.9:
the remainder is hats 17–46.

## χ₃ µ=80 — linear plunge, no saturation

| N | ℓ₀ | Δℓ / ΔN | n_small | N_eff |
|---|---|---|---|---|
| 5 | 32.3 | — | 3 | 2.36 |
| 9 | 51.6 | 4.8 | 6 | 2.66 |
| 13 | 69.0 | 4.4 | 7 | 2.82 |
| 17 | 84.7 | 3.9 | 9 | 2.91 |
| 21 | 98.1 | 3.3 | 11 | 2.96 |
| 25 | 111.1 | 3.3 | 12 | 3.00 |

ℓ₀ ≈ 13.2 + 3.9 N for N∈[9,25].
The rate is not slowing enough to
call a limit. n_small ≈ N/2: half
the spectrum is already below 10⁻³
at N=25. That is Landau filling
the well, not a convergent
eigenvalue of a fixed operator.

Galerkin here is not “more digits
of one matrix”. Each N is a
different compression of the same
quadratic form onto a larger
Slepian window. λ_min(Q_N) → 0
exponentially in N until the hat
wall (N=27). There is no spectral
limit inside the certified range
except the shape of v₀ (N_eff → 3).

## What converges, what does not

- **Shape of v₀.** N_eff and the
  94 % mass on hats 0–2 at µ=80.
- **Ratios λ_{k+1}/λ_k** on the
  deep wells, once N ≳ 9.
- **Not λ_min itself**, except on
  short windows (χ₅ µ=16) where
  the Slepian dimension of the
  well is ~2 and extra hats are
  already out of band.
- **Not the 2-plane Ritz inside
  Q_N.** That stays at ℓ~10–20
  while λ_min dives.

A proof that freezes N=3 talks
about a different operator than
the one whose depth is 111 nats.
Spectral convergence in N is
convergence of a family, not of
one compact resolvent.

Data: `report/spectral-convergence.json`.
