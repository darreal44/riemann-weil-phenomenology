<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# CST+Gauss is the classical Γ pairing on W_L

Preregistered (`report/prereg-ql-arch-weil.md`):
two writings of Arch on W_L
(θ=0 for y>L), plus the mixed
(ψ(s₀)+γ)I. Frullani and
Weierstrass, not fitted. Q_pk
4-plane at μ=5. The 10^{-5} is
neither Weil-positive nor
Weil-negative until the term is
classical, and not after.
Not RH.

## Execution

`python code/ql_arch_weil.py`.
`report/ql-arch-weil.json`.

Frullani: ∫_L^∞ D₂ EC = −log(1−e^{−2L}),
error 3×10⁻¹⁷ at L=log 5.

Weierstrass: ∫_0^∞ D₂(EC−1) = ψ(s₀)+γ.

| s₀ | quad | ψ+γ |
|---|---|---|
| 3/4 | −0.508645214884941 | −0.508645214884939 |
| 1/4 | −3.650237868474729 | −3.650237868474732 |

Writing (1) CST+Gauss and writing (3)
(F₀/2) C_A_lo + ½∫ D₂(F₀−θ) agree
to 4×10⁻¹⁵ on both 4-planes.
Off-diagonals agree to 0 (same
integrand). C_A_lo is the *constant*
of (3), not the matrix element:
arch_00 − C_A_lo = +0.619 on χ₃
(the #69 gap). 2 m_Q is a plane
wave (#70), not Q(φ_n).

The mixed writing replaces −γ by
ψ(s₀) while keeping EC. It shifts
every diagonal by ψ+γ and is not
the classical term.

| χ | λ_min CST+p^k | λ_min digamma+p^k | mixed |
|---|---|---|---|
| χ₃ | **+1.43×10⁻⁵** | **+1.43×10⁻⁵** | −0.509 |
| χ₅ | +1.17×10⁻³ | +1.17×10⁻³ | −3.649 |

## Verdict: SURVIVE

CST+Gauss on W_L *is* the classical
Γ pairing. The 10^{-5} of Q_pk H₄
is a 4-plane of that form. It is
not Weil-positive (Courant: a
positive section is not a lower
bound on the class). It is not
Weil-negative (the identified
4-plane is >0). The mixed
negative 4-plane is not a
disproof of RH. Not (∀ L). Not RH.

Judge: `tests/test_ql_arch_weil.py`.
