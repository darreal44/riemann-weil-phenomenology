# One set, not aL + bL (5 September 2026)

The geometric law splits two pieces and adds them:

    -ln c_L ≈ a L (γ₁ − ν)_+ + b L Σ (gap − ν)_+ ,   ν = 2π/L.

That split is why the hold-out at T₀ = 320 overpredicts narrow deserts
by ×1.4–1.8. The sampling problem never saw two terms. It saw one set.

## The set

For a window of type τ = L/2 let

    E_L = (−γ₁, γ₁)  ∪  ∪ { (γ_k, γ_{k+1}) : γ_{k+1} − γ_k > ν }.

This is the desert and every later sub-Nyquist gap, as a *single*
measurable set. Landau's necessary count on that set is

    n_L(E) = (L / 2π) |E| = (L / π) |E ∩ R_+|.

Beurling's D^− of a separated subset of Γ is still infinite globally,
so Theorem 1 of *sampling-floor* is untouched: c_L > 0 under RH. The
size of c_L is the sampling constant of Γ for PW_τ, which is the
constant of the complement of E_L together with the short gaps. It is
not a linear form in |desert| and Σ excess.

## What the union Slepian already said

*sampling-floor* §4 computed 1 − λ₀(E, τ) for ζ at μ = 11: −ln = 74
against a measured −ln c_L = 110. At μ = 3 the same object *under*-shot
by a factor 25. Treating E as a free concentration set (Slepian on a
union of intervals) ignores that the endpoints are zeros and that gaps
just below ν still degrade the frame. So even the one-set Slepian is
not c_L. The sharp one-set object is the bottom eigenvalue of the zero
Gram — which *is* c_L.

## What can still be read off E

At T₀ = 320, one-sided |E ∩ R_+| and Landau n_L(E):

| χ | μ | |E+| | excess (the b-term) | n_L(E) |
|---|---|------|---------------------|--------|
| ζ | 11 | 137 | 40 | 105 |
| ζ | 22 | 310 | 83 | 305 |
| χ₅ | 22 | 64 | 15 | 63 |
| χ₁₇ | 22 | 21 | 5 | 21 |
| χ₂₉ | 22 | 19 | 3 | 18 |
| χ₂₄ᵒ | 22 | 9 | 0.9 | 9 |

The law's two terms weight desert and excess differently (a ≠ b).
On a narrow desert the first term is almost zero and the second is a
handful of modest gaps; n_L(E) is then a small integer (χ₂₉ : 18 at
μ = 22). Adding aL + bL as if the pieces were independent overcounts
that small set: the same measure cannot hide two independent Slepian
factors. That is the ×1.4–1.8, read on one set.

## What would close it

A theorem that bounds the sampling constant of Γ by a function of E_L
*as a set* — not of two additive functionals of E_L — for example a
Landau–Widom expansion of the concentration operator on a finite union
of intervals with Dirichlet conditions at the zeros, or a Beurling
density of the weighted set Γ with a hole kernel. Until that exists,
a and b stay frozen and the overprediction on narrow deserts is the
measurement of the missing term, not a reason to refit.
