<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# Three coverings of #72

Preregistered (`report/prereg-ql-theta-overlap.md`).
The simplex 2√(αβ)+2√(αμ₂)+μ₁ ≤ √2
is already a theorem. This sitting
identifies that majorant as the
overlap count. Without it the χ₃
μ=5 take is retroactive. Not Weil.
Not RH.

## Count

Even f, θ=2⟨f, T_y f⟩, h=√2 f on
[0, L/2]. For L/3 ≤ y < L/2 the
integrand lives on [y−L/2, L/2]
and splits into five x-intervals,
three covering types:

    AC  A ↔ C by the shift y
        (two copies, + and −)
    AM2 A ↔ M₂ by the even fold
        (two copies)
    M1  M₁ against itself

A=[0, L/2−y], C=[y, L/2],
M₂=[2y−L/2, y], M₁=[L/2−y, 2y−L/2].
Disjoint, union [0, L/2]. Lengths
of the five x-intervals sum to L−y.
Cauchy–Schwarz on each type gives
2√(αβ)+2√(αμ₂)+μ₁.

At μ=5, y=log 2, y/L=0.4307 ∈ (1/3, 1/2).
L/4 ≤ y < L/3 is a degeneration
(M₁ empty, reverse(A) meets A); the
take does not use it.

## Execution

`python code/ql_theta_overlap.py`.
`report/ql-theta-overlap.json`.

Partition and covering hold on a
grid in [L/3, L/2). Pair integrals
sum to ⟨f, T_y f⟩. Constant mode:
θ = 2(L−y)/L = theta_hat₀₀, and
equals the majorant (saturates).
Cosine: |θ| < majorant. Both ≤ √2.

## Verdict: SURVIVE

The overlap count is the missing
geometry of #72. The simplex was
already closed. The √2 cap on the
band is no longer a finite-section
check read backwards. One L (the
take still dies at μ=5.1). Not
(∀ L) Q_L ≥ 0. Not Weil. Not RH.

Judge: `tests/test_ql_theta_overlap.py`.
