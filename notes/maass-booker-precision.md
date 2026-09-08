<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# Guaranteeing Booker–Then last-digit precision

Not a take. Not Weil.

Booker–Then (arXiv:1703.08863, IJNT 2018) publish Table 1 to
the last digit, meaning ±1 on that digit, about 13 decimals,
about 10^{-13}. They evaluate a rotated completed L-function
Λ_θ with MPFI and isolate simple zeros by opposite rigorous
signs on a bracket shorter than that width. Completeness up to
height T is Turing/Weyl on their lists, for those L, not ∀L.

That is the bound we have to meet, and to *guarantee*: a
claimed γ sits in an interval (a,b) with |b-a|≤10^{-13} on
which a real ball-valued Hardy Z has opposite signs at the
ends and 0 lies in neither evaluation ball.

The truncated Dirichlet sum |∑_{n≤1000} a_n n^{-1/2-it}| finds
the five Table 1 first zeros, but the tail is a slow bias of
size about 0.02. That locator is not the bound. Those minima
are not certified zeros.

The Fourier series of an even Maass form is
f(x+iy)=√y ∑ a_n K_{iR}(2π n y) cos(2π n x), with a_n the
Hecke eigenvalues (a_1=1, Hecke relations hold on the replica
coefficients). Flint's K_{iR} matches the integral
∫ e^{-x cosh t} cos(R t) dt. Termwise Mellin then gives, for
Re s>1,

    4 ∫_0^∞ f(iy) y^{s-1/2} dy/y = Γ_R(s+iR) Γ_R(s-iR) L(s).

On 1.0.1.1.1 at s=2 this identity holds to about 10^{-4}
(`code/maass_booker.py`, `tests/test_maass_booker.py`). No
Fricke is used there: the Dirichlet series converges, and the
integral is taken on (0.05,10) with 250 coefficients.

On the critical line the same identity is true by continuation,
but |γ(1/2+it)| is about 10^{-12} at t=17, while f(iy) for
y≥1 is a decaying envelope of size 10^{-7}. A trapezoid of
that envelope is size 10^{-8} and swamps Λ=γ L. That is why
Booker rotates the ray (θ with cos θ ≲ (4+|t²-r²|)^{-1/2})
and evaluates f only after moving the point into the
fundamental domain, where the series is accurate, and works
with Λ_θ which stays O(1). Prototypes of that rotation, with
and without pullback, do not yet change sign at Table 1 γ₁.
Until they do, we do not isolate new zeros and we do not
replace Table 1.

Flint's `hypgeom_2f1` is unusable for the Maass parameters
(it returns ~10^5 where the Gauss series is 0.88). The series
in `hyp2f1_series` is the right ₂F₁. With that, the rotated
termwise identity at s=2, θ=0.25 holds to about 10^{-3}:

    4 ∫ f(ie^{iθ} u) u^{s-1/2} du/u = γ_θ(s) L(s).

That is Booker (2.3) without Fricke, integrating the Fourier
series on the ray, not the pullback to the fundamental domain.

The cosine series is the LMFDB knowl and Booker (n≥1, no extra
2). In the fundamental domain it agrees with its S-pullback
(`f_auto`). Off the FD the raw series is not equal to
`f_auto(-1/z)`: at y=2 versus y=1/2 the ratio is about 10, with
tight flint balls, so this is not a truncation or a working-precision
loss. Extra a_n cannot close that gap (at y=1/2 the series has
already converged). PARI `lfuncreate` cannot take imaginary
Γ-shifts (`α_j` must be rational), so it is not this evaluator.

Booker's Λ_θ is the Mellin of the *automorphic* f, with θ large
enough that |γ_θ| stays O(1) (cos θ ≲ (4+|t²-r²|)^{-1/2}). The
split at u≥1 of `f_auto` agrees with the unsplit Mellin of
`f_auto` along the whole ray, and Λ_θ(1/2+it) is real, as in
the paper. That function is not γ_θ L: at s=2 the ratio
depends on θ (about 1.75 at θ=0.25, 1.12 at θ=1). The termwise
Mellin of the raw series on the same ray is γ_θ L to 10^{-4}.
Around Table 1 γ₁ the automorphic Λ_θ does not change sign.

So the guarantee in force today is Booker–Then's own MPFI
list for those five forms (`zeros_maass{1..5}.txt`, stored as
`zeros_hp`). The isolation helper in `maass_booker.py` is the
rule we will apply to any later computation; it refuses a
bracket whose endpoint balls contain 0. Independent
recertification of Table 1 waits on an exponentially convergent
representation of the *termwise* Mellin (the one that equals
γL at s=2) on Re s=1/2, not of the S-extension of the FD
series. Not Weil.

Cite: Booker–Then 2018; LMFDB Collaboration 2026,
`notes/lmfdb.bib`.
