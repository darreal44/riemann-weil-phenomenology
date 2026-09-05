# Error convergence

## Slepian Nyström (χ₂₉, μ=11)

| M | λ₊ | Δ |
|---|-----|---|
| 40 | 0.6180 | |
| 80 | 0.6120 | −6.0e-3 |
| 160 | 0.6091 | |
| 240 | 0.6081 | |
| 320 | 0.6076 | −5e-4 |

Δ ∼ 1/M. M=240 is enough for two digits of
1−λ₊=0.392. A≈0.72 is not a discretisation
artefact.

## G−Q (already)

Frel 6.5→5.4→4.1 %. σ₀ of D grows 1.62→1.88.
Relative bulk error falls; operator residual
does not. Different from the Slepian grid error
(that one *does* go to 0).

## Lemma slack

ell_Gram − (−log(1−λ₊)) = 1.27−0.94 = 0.33
at μ=11 = log(1/A) with A≈0.72. That slack
is stable if A is; we have one window only.
