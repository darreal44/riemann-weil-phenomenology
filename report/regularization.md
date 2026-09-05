# Regularising the hat tail

Primes on the window are already complete.
The missing piece is ∑_{γ>T} |hat(γ)|².

## Weyl tail (the right one)

Replace the discrete sum by
∫_T^∞ |hat(t)|² ρ_Weyl(t) dt,
ρ = (1/π)(log(q t / 2π)+1).

χ₂₉ μ=11, T=69:

| | λ0 |
|---|-----|
| G discrete T=69 | 0.281 |
| G + Weyl tail →2000 | 0.312 |
| G discrete T=320 | 0.298 |
| Q | 0.303 |

The tail overshoots by ~4 % (density and the
factor 2 in 2ΦᵀΦ). Direction is correct:
it moves 0.281 toward 0.303. Tuning ρ
(one-sided Weyl vs two-sided) would finish it.

## What not to use

Tikhonov Q+εI fills λ0 and destroys the
desert isolation. Spectral damping e^{−εγ}
is a softer tail, same idea as Weyl with
an extra decay. Neither is an off-line zero.
