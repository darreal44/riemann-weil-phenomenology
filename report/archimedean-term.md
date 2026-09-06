# The archimedean term

Place ∞ of the explicit formula.
One kernel, three writings, no zeros.

## From Γ′/Γ

The completed L-function of a
primitive character of conductor q
and parity a ∈ {0,1} has Gamma
factor

    γ(s) = (q/π)^{(s+a)/2} Γ((s+a)/2).

The archimedean side of Weil is
the pairing of h against
(γ′/γ)(1/2 + it) + (γ′/γ)(1/2 − it),
which is even. After Fourier
transform in t and restriction
to a window of length L, this
becomes a constant plus an
integral of the lag kernel θ
against a positive measure on
[0, L].

Parity enters only through

    s₀ = 1/4 + a/2
       = 1/4 (even χ) or 3/4 (odd χ).

ζ is the even case with a pole
handled separately.

## The window kernel

    K(y) = 2 e^{-2 s₀ y} / (1 − e^{-2y}),
    y ∈ (0, L].

Geometric series

    K(y) = 2 ∑_{m≥0} e^{-(2s₀+2m) y}.

At y=0, K(y) ∼ 1/y. Alone it is
not integrable against a constant.
Against the combination
F₀ e^{-(2−2s₀)y} − θ(y), which
vanishes at 0, the integrand is
O(1). Splitting the two pieces
and Laplace-transforming them
apart produces a harmonic series
and is illegal (`H11-independent.md`).

The assembled matrix element is

    Arch(f,g)
        = (F₀/2) CST
          + ½ ∫_0^L K(y) (F₀ e^{-(2−2s₀)y} − θ_{f,g}(y)) dy,

    CST = log(q/π) − γ_Euler − log(1−e^{-2L}),
    F₀  = 2 ⟨f,1⟩⟨g,1⟩ in the hat
          coordinates (2 on the
          diagonal, 0 off).

This is exact on the window: the
Γ-tail beyond L is absorbed into
the last log, which is 1/256 at
µ=16.

## Size

O(1), independent of the zeros.
On unit e₁ at µ=16:

| χ | s₀ | q | Arch | P | A−P |
|---|---|---|---|---|---|
| χ₅ | 1/4 | 5 | −0.98695 | −0.98704 | 9.3×10⁻⁵ |
| χ₃ | 3/4 | 3 | −0.62477 | −0.62498 | 2.2×10⁻⁴ |
| χ₄ | 3/4 | 4 | −0.337 | −0.338 | 1.2×10⁻³ |
| χ₁₃ | 1/4 | 13 | −0.031 | −0.243 | 0.212 |

Wide desert: Arch tracks P to
10⁻⁴. Narrow desert: they miss,
Arch stays O(1), the difference
does not dive. That is why
λ_min(H) stops shrinking on χ₁₃
(`lemma2-H-arch-primes.md`).

At µ=2 the prime sum is almost
empty (θ(log 2) on the constant
hat vanishes at the endpoint).
What remains is pure Arch,
+0.4 to +0.7 depending on q
(`archimedean-compact.md`).

## Connes’ place ∞

Theorem 4, v=∞:

    ∫'_{ℝ^*} h(u^{-1}) / |1−u| d*u.

After the λ^{1/2} twist this is
τ_∞(λ) = (√λ)/2 (1/(1+λ) + 1/|1−λ|)
(CC 39). The principal value ∫'
removes u=1, which is already
split off as 2 h(1) log' Λ.

K(y) is that same local integral
written additively, y = log λ,
restricted to λ ∈ [1, µ] and
paired against hats. The factor
e^{-2 s₀ y} is the weight of the
Gamma shift (s₀=1/4 is ξ, not
the raw Γ(s/2) of ζ). They are
not two archimedean terms.

Connes–Consani’s compact operator
K_I (`cc_arch.py`, prolates at
c=2π) is a different object: a
Toeplitz of Qε on an interval of
length log 2 or log 3. It is the
archimedean contribution to their
scaling-site trace, not the
matrix ARCH of scan_s.

## What Arch does not do

- It does not see zeros.
- It is not a Slepian eigenvalue.
- It does not produce the
  exponential in ℓ. That is
  Arch − P, after cancellation
  of two O(1) terms.
- A bound on Arch alone cannot
  prove det(A−P)>0: Arch is
  indefinite on the 2-plane
  (det A ≈ −1.15 on χ₅).
  The primes supply the rest.

## Code

    scan_s.assemble     D2-panels of K
    H11_independent     quad of the regular integrand
    H_2plane_independent same, full 2×2
    cc_arch.py          Connes–Consani K_I, not ARCH
    trace_formula.py    S-local Thm 4, v=∞ inside Fmat
