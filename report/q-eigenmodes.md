# Eigenmodes of Q_N

Phase: v[0] ≥ 0. Components are hat
indices n = 0,1,2,… Nodes = sign
changes of that list (not of the
continuous function).

## Ground state is the raised cosine, plus a tail

e₁ = (0.816, −0.577, 0).

    χ₅ µ=16 N=9     0.711  −0.681   0.179   0.003 …
    χ₅ µ=16 N=17    0.706  −0.683   0.185   0.003 …
    χ₃ µ=16 N=9     0.666  −0.697   0.264  −0.033 …
    χ₃ µ=80 N=17    0.555  −0.679   0.434  −0.198   0.059 …
    χ₃ µ=80 N=25    0.543  −0.672   0.448  −0.219   0.071 …

On the short window the profile
freezes between N=9 and 17. On
χ₃ µ=80 it spreads: hat-2 grows
from 0.18 to 0.45, hat-3 reaches
0.22. That is the 6 % leak, now
visible as two extra lobes — not
noise.

Overlap with e₁ (first three
coords): 0.99 on χ₅, 0.96 on
χ₃ µ=16, 0.89 on χ₃ µ=80. The
2-plane remains the leading
sketch. The extra lobes are what
buy the 10⁴⁰ in the Rayleigh
quotient.

## The tower is Slepian

χ₅ µ=16 N=17

| k | ℓ | N_eff | kbar | mass 0–2 | sketch n=0..6 |
|---|---|---|---|---|---|
| 0 | 33.1 | 2.14 | 0.54 | 1.000 | +− on hats 0,1 |
| 1 | 19.0 | 2.19 | 1.35 | 0.993 | peaked on hat-2 |
| 2 | 7.3 | 5.35 | 2.83 | 0.560 | spread to n=6 |
| 3 | 1.2 | 2.43 | 5.38 | 0.253 | peaked at n=6 |

Mode 1 is e₂ up to a sign:
e₂ = (−0.365, −0.516, 0.775),
measured (0.53, 0.33, −0.78).
So {v₀, v₁} = {e₁, e₂} on this
window. Mode 2 is the first to
leave the plane (mass 0.56).

χ₃ µ=80 N=25 — four deep modes,
none of k≥1 confined:

| k | ℓ | N_eff | kbar | mass 0–2 |
|---|---|---|---|---|
| 0 | 111 | 3.00 | 1.02 | 0.947 |
| 1 | 96 | 3.63 | 2.47 | 0.376 |
| 2 | 83 | 3.61 | 3.27 | 0.395 |
| 3 | 72 | 5.82 | 6.15 | 0.146 |

Already k=1 has left the 2-plane.
The well is a ladder of oscillating
hats, one new lobe per mode —
discrete prolates on a widening
window. Lemma 2’s two vectors are
v₀ and, on short windows, v₁.
They are not v₂, v₃ of the deep well.

## Ansatz

A test function for the deep well
at µ=80 has to look like

    0.54 h₀ − 0.67 h₁ + 0.45 h₂ − 0.22 h₃ + 0.07 h₄

not like e₁. Truncating after h₂
is the Ritz ℓ=19 calculation.
The closed 2×2 remains the right
object for N_eff ≈ 2 windows
(χ₅ µ=16). It is the wrong
ansatz for the Landau-filled well.

Data: `report/eigenmodes.json`.
