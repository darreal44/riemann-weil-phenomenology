# Ritz of the leading principal blocks

Q_N restricted to hats 0..k−1 is the
Galerkin Q_{k−1}. λ_min of that
block versus λ_min of the full
matrix, and the L² mass of the
true v₀ on those hats.

## χ₅ µ=16, N=17, ℓ_true=33.1

| hats | ℓ_Ritz | mass(v₀) | λ_Ritz / λ_true |
|---|---|---|---|
| 0–1 | 9.9 | 0.966 | 1.2×10¹⁰ |
| 0–2 | 13.0 | 1.000 | 5.4×10⁸ |
| 0–3 | 16.5 | 1.000 | 1.7×10⁷ |
| 0–4 | 18.9 | 1.000 | 1.5×10⁶ |
| 0–5 | 22.5 | 1.000 | 4.3×10⁴ |
| 0–7 | 25.5 | 1.000 | 2.0×10³ |

Mass is 1.000 from three hats.
Depth keeps moving. The printed
1.000 hides a tail that still
shifts ℓ by 20 nats.

## χ₃ µ=16, N=17, ℓ_true=47.9

| hats | ℓ_Ritz | mass(v₀) | λ_Ritz / λ_true |
|---|---|---|---|
| 0–1 | 9.3 | 0.919 | 6.1×10¹⁶ |
| 0–2 | 17.1 | 0.998 | 2.4×10¹³ |
| 0–4 | 24.1 | 1.000 | 2.2×10¹⁰ |
| 0–7 | 33.3 | 1.000 | 2.2×10⁶ |

Same story, worse ratio.

## χ₃ µ=80, N=25, ℓ_true=111.1

| hats | ℓ_Ritz | mass(v₀) | λ_Ritz / λ_true |
|---|---|---|---|
| 0–1 | 11.7 | 0.746 | 1.5×10⁴³ |
| 0–2 | 19.9 | 0.947 | 4.2×10³⁹ |
| 0–3 | 25.7 | 0.995 | 1.2×10³⁷ |
| 0–4 | 32.3 | 1.000 | 1.7×10³⁴ |
| 0–5 | 38.2 | 1.000 | 4.6×10³¹ |
| 0–7 | 47.0 | 1.000 | 6.7×10²⁷ |

The ansatz 0.54 h₀−0.67 h₁+0.45 h₂
−0.22 h₃+0.07 h₄ is the block 0–4:
ℓ=32, not 111. Mass reports 1.000
and eighty nats are still missing.
Those nats live in a tail below
the third decimal of L² — the
same mechanism as the 6 % leak,
one order further down.

ℓ_Ritz grows by ~6 nats per extra
hat on this window (19.9 → 47.0
from 3 to 8 hats). Linear, no
knee. Closing the well at µ=80
is not a better 5-vector. It is
the whole certified range N≤25.

## Consequence

Variational truncation by support
of v₀ fails twice: first at 6 %
(block 0–2), then at <0.1 %
(block 0–4). A proof that picks
a fixed finite test space of hats
caps ℓ at ~4 N. The number 111
is the Galerkin limit of that
space against the hat wall, not
a Rayleigh quotient of a short
ansatz.

Data: `report/ritz-blocks.json`.
