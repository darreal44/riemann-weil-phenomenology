<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->

# Session 2026-09-08 — Schur du plateau

Découpe de \(Q_+\):

    Q = [ A  B ]
        [ Bᵀ C ]

A = 2-plan {φ₀,φ₁}, C = chapeaux n≥2.
S = A − B C⁻¹ Bᵀ. Haynsworth: C ≻ 0 ⇒
ν₋(Q) = ν₋(S), et Q ≻ 0 ⇔ S ≻ 0.

Pas W_L. Pas RH.

## μ=5, Q₄⁺

    χ     λ(C)         λmin(A)    λmin(S)=λmin(Q)   ‖corr‖
    χ₃    1.57, 1.92   1.9e-4     1.43e-5           0.061
    χ₅    1.97, 2.57   5.2e-3     1.17e-3           0.005

C n'est pas en danger. Tout le risque est S.

## S complète

χ₃ μ=5:

    A    = [[0.06991, 0.10253], [0.10253, 0.15094]]
    corr = [[0.01731, 0.02750], [0.02750, 0.04388]]
    S    = [[0.05261, 0.07503], [0.07503, 0.10706]]

    λ(S) = 1.43e-5, 0.160     det S = 2.3e-6

χ₃ μ=11: A ≈ corr, il reste

    S ≈ [[5.4, 6.1], [6.1, 6.8]] · 10⁻⁴
    λmin(S) = 1.38e-8

Le crush 0⁺ est A − corr → 0⁺ avec S encore PD, presque rang 1.

χ₅ μ=5: corr ~ 10⁻³, S ≈ A (T₃ tient le 2-plan, le plateau
ne touche presque pas). μ=11: encore A ≈ corr.

## Inertie

    χ₅ plein        ν₋(C)=0  ν₋(S)=0  ν₋(Q)=0
    χ₅ drop-T₃      ν₋(C)=0  ν₋(S)=1  ν₋(Q)=1   (λmin = −0.21)

Un seul mode négatif, et il est dans S. Enlever T₃ n'est
pas un zéro hors droite.

## Conditionnement μ=5

    κ(C) ~ 1.2     κ(A) χ₃ ~ 10³     κ(S) χ₃ ~ 10⁴     κ(Q) χ₃ ~ 10⁵
    κ(C) ~ 1.3     κ(A) χ₅ ~ 170     κ(S) χ₅ ~ 760     κ(Q) χ₅ ~ 2·10³

μ=11: κ(Q) ~ 10⁶–10⁸. Inverser C est stable. Soustraire
A − corr à μ=11 perd 3 chiffres. μ=17, h=8, 10⁻¹⁵ = ulp.
