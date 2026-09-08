<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->

# Session 2026-09-08 — quadrature et mpmath

Intégrande de A_nm:

    D₂(y,s₀) (F₀ E_C(y,s₀) − θ_nm(y))

    D₂ = 2 e^{-2 s₀ y} / (1 − e^{-2y}) ~ 1/y   près de 0
    E_C = e^{-(2−2s₀)y}

F₀ θ(0) s'annulent: F₀ E_C(0) = θ(0) = 2 sur la diagonale,
θ_nm(0)=0 hors diagonale. Donc D₂ · O(y) = O(1).
Pas de pôle à intégrer. 4 panneaux Gauss suffisent.

Pas W_L. Pas RH.

## Variation N_PANELS × N_GAUSS (float64, S χ₃)

    μ    P   G     λmin(S)
    5    4   8     1.428545e-5
    5    8  16     1.428545e-5
    5   16  32     1.428545e-5
    5   32  32     1.428545e-5
   11    4   8     1.379935e-8
   11   32  32     1.379934e-8

Erreur de quadrature ≪ 10⁻¹⁴. Le défaut n'est pas Gauss.

## mpmath dps=40, quad [0,L], θ et D₂ en mp

    μ     S float64        S mpmath           chiffres
    5     1.428545e-5      1.428544997e-5     10
   11     1.379935e-8      1.37993454e-8      8

Signe + confirmé à μ=11. float64 honnête pour le signe
jusque-là. μ=17 / h=8 / 10⁻¹⁵ reste interdit.

Pôle de ζ (s=1) absent: χ₃, χ₅ non principaux.
Le constant de Q_nm est Γ / conducteur / cutoff L.
