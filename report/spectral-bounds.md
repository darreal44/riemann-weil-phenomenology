# Spectral bounds on A, P, and H

Plane {e₁,e₂}, µ=16. Intervals are
[λ_min, λ_max].

## Exact spectra

| χ | spec A | spec P | spec H |
|---|---|---|---|
| χ₅ | [−1.182, 0.977] | [−1.183, 0.973] | [3.21×10⁻⁶, 3.95×10⁻³] |
| χ₃ | [−0.688, 0.483] | [−0.690, 0.476] | [6.31×10⁻⁸, 8.98×10⁻³] |
| χ₄ | [−0.401, 0.771] | [−0.414, 0.675] | [1.11×10⁻⁵, 0.109] |
| χ₈ | [−0.712, 1.447] | [−0.938, 0.526] | [1.73×10⁻⁴, 1.15] |
| χ₁₃ | [−0.227, 1.932] | [−0.422, −0.229] | [2.08×10⁻³, 2.35] |

A and P are indefinite (except P on
χ₁₃, negative definite). H is
positive, two to six orders smaller
than A and P on the deep wells.

## Classical envelopes — all too wide

**Weyl.** spec(A−P) ⊂ spec(A) + [−‖P‖, ‖P‖].

    χ₅ : [−2.37, 2.16]
    χ₃ : [−1.38, 1.17]

True H sits in a window of width
10⁻³ inside an interval of width 4.
Weyl cannot see the sign.

**Gershgorin on H.** Disks
H₁₁ ± |H₁₂| and H₂₂ ± |H₁₂|.

    χ₅ : [−5.0×10⁻⁴, 4.4×10⁻³]
    χ₃ : [−1.2×10⁻³, 1.0×10⁻²]

The lower radius is negative: |H₁₂|
exceeds H₁₁. Gershgorin does not
prove positivity either.

**Norm gap.** |‖A‖ − ‖P‖| = 7.7×10⁻⁴
on χ₅, against ‖H‖_F = 3.9×10⁻³.
Same order, wrong object (scalar
norms, not aligned residuals).

## Bound that is sharp

Already recorded: λ_min(H) ≥ det H / tr H,
equality to 10⁻³. That uses the
2×2 closed form, not an embedding
into operator theory.

A spectral-envelope proof of
λ_min(H) > 0 would need an
estimate of ‖A − P‖ in the
*e₁-direction only*, to 10⁻⁴
relative. That is the residual
bookkeeping of `H-lower-bound.md`,
not Weyl or Gershgorin.

Data: `report/spectral-bounds.json`.
