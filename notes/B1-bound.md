<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# Bound on B₁ (written)

## Theorem

Let B be the symmetric codiagonal on ℓ²({n≥N}) with weights a_n = −w₂
θ̂_{n,n+1}(log 2) (the Θ-piece of B₁). Then

    ‖B‖ ≤ 4 |w₂| / π.

## Proof

1. Weighted shift. ⟨Bx,x⟩ = 2 ∑ a_n x_n x_{n+1} ≤ 2 M ∑ |x_n x_{n+1}| ≤
M ∑ (x_n² + x_{n+1}²) ≤ 2 M ‖x‖², M = sup_{n≥N} |a_n|. Hence ‖B‖ ≤ 2M.

2. Cap on θ̂_{n,n+1}(y). For n≥1, m=n+1, y=log 2,

    θ̂ = 2 (n sin(ω_n y) − (n+1) sin(ω_{n+1} y)) / (π (2n+1)).

|n sin − (n+1) sin| ≤ n+(n+1) = 2n+1, so |θ̂| ≤ 2/π. Thus M ≤ |w₂| · 2/π
and ‖B‖ ≤ 4 |w₂| / π.

For χ₃, |w₂|≈0.490, 4|w₂|/π ≈ 0.624.

## What is not written

‖B‖≤0.45 for all N. Sections up to n=80 sit at 0.397 because {n log 2 /
log 3} is dense and a_n flips sign often (~74 % of consecutive products
negative on n=2…200). That slack is not turned into a constant <2 in
front of M. A two-step Gershgorin on B² gives ‖B‖ ≤ M √(2+2ρ) with ρ =
sup |a_n a_{n+1}| / M² ≈ 0.59 on that range, i.e. ≈0.61, not 0.45.

The theorem is 0.624. The section is 0.397. Equidistribution explains
the gap; it does not close it to 0.45.

Not RH.
