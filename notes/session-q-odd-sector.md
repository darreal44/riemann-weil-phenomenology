<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->

# Session 2026-09-08 — secteur impair \(Q_-\)

Sinus \(s_n(t)=\sqrt{2/L}\sin(2\pi n t/L)\), \(n\ge 1\).
Convention \(\theta^-_{nm}(y)=2\int_0^{L-y}s_n(t)s_m(t+y)\,dt\),
calée sur les cosinus (écart \(10^{-6}\) à \(y=\log 2\)).

Formules:

- \(n=m\): \(2(L-y)/L\cos(\omega_n y)+\sin(\omega_n y)/(\pi n)\)
- \(n\neq m\): \(2\bigl(m\sin(\omega_n y)-n\sin(\omega_m y)\bigr)/(\pi(m^2-n^2))\)

Atomes \(p^k\) comme `Q_window`. Pas \(W_L\). Pas RH.

## \(\lambda_{\min}(Q_4^-)\) vs pair

    χ     μ     Q-            Q+            ratio
    χ₃    3     0.30          1.1e-2        27
    χ₃    5     1.9e-3        1.4e-5        130
    χ₃   11     4.1e-8        1.4e-8        3
    χ₅    3     0.80          4.6e-2        17
    χ₅    5     7.6e-2        1.2e-3        65
    χ₅   11     4.0e-5        9.7e-7        41

Aucun λ < 0. L'impair est plus raide au premier cran,
puis rejoint le crush 0⁺.

## Modes, μ=5

χ₃: ψ₀⁻ = (0.999, −0.04, 0.02, −0.02) sur s₁..s₄,
masse s₁ = 0.998, 1 nœud, λ = 1.9e-3.
Excités: 5, 3, 7 nœuds (pas Sturm).

χ₅: ψ₀⁻ ≈ (0.982, 0.17, 0.09, 0), masse s₁ = 0.964,
1 nœud, λ = 0.076.

Le pair pince un 2-plan (0 nœud). L'impair pince l'axe s₁
(déjà 1 nœud). T n'était pas un mensonge qui cachait un
λ < 0 : c'était le secteur le plus fragile (φ₀).

## Stabilité (pair, pour comparaison)

⟨ψ₀(μ=5), ψ₀(μ=11)⟩ = 0.985 (χ₃), 0.975 (χ₅).
⟨h=4, h=8⟩ à μ=5 = 1.000. Direction gelée, énergie non.
