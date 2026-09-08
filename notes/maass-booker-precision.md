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

LMFDB/Zenodo encode the Maass symmetry as 0 = even (cosine)
and 1 = odd (sine). 1.0.1.1.1 has symmetry 1. The LMFDB page
for 1.1 says odd. The Fourier series that is automorphic under
z ↦ −1/z with the replica a_n is the sine expansion

    f(x+iy) = √y ∑_{n≥1} a_n K_{iR}(2π n y) sin(2π n x).

At four generic test points the ratio f(z)/f(−1/z) is 1 to a
relative ball of size 10^{-9} through 10^{-11}. The cosine
series with the same a_n is not automorphic: the axis identity
y ∑ a_n K_{iR}(2π n y) = ∑ a_n K_{iR}(2π n /y) fails by a
frozen factor of about 10.24 from n=12 through n=1000, and
off-axis ratios are O(1) and not 1. Extra a_n cannot close
that gap. 1.0.1.3.1 (symmetry 0) is the other way around:
cosine is automorphic, sine is not. The catalog comment that
treated symmetry>0 as even is the wrong encoding for the
Fourier expansion; `code/maass_booker.py` uses the LMFDB
integer as ε.

Booker (2.3) for odd ε=1 is the termwise sine of
2π n u sin θ, which equals −f(i e^{iθ} u) because the
geometric point has x = −u sin θ. The ray integrand in the
evaluator is that termwise sum, equivalently (−1)^ε times
the automorphic pullback. Then, for Re s>1,

    c_θ(s) ∫_0^∞ f_ray(u) u^{s-1/2} du/u = γ_θ(s) L(s),

with c_θ = 4 / (2π i tan θ) and γ_θ the odd Booker factor
(i^{-1} (cos θ)^{1/2-s} Γ_R(s+1±iR) ₂F₁). On 1.0.1.1.1 at
s=2, θ=0.25 this identity holds to about 4·10^{-6}
(`check_s2_identity`). The same ratio holds for the Booker
split at u≥1 of the automorphic sine series, because that
series *is* f. (The cosine-in-FD-then-pullback function was
automorphic by construction and was not γ_θ L: its s=2
ratio depended on θ, about 1.75 at θ=0.25.)

Flint's `hypgeom_2f1` is unusable for the Maass parameters
(it returns ~10^5 where the Gauss series is 0.88). The series
in `hyp2f1_series` is the right ₂F₁, with Abramowitz 15.3.7
when |z|≥0.72. At Booker's large θ (cos θ ≲ (4+|t²-r²|)^{-1/2}
≈ 0.07 at t=17) the split needs a fine grid (nv ≳ 800,
vmax ≳ 5, nmax ≳ 60) or the ratio at s=2 drops to ~0.74 from
truncation, not from a wrong expansion. A moderate ray
θ=1.0 is accurate at s=2 to 10^{-6} and |γ_θ| is large
enough on the critical line that Λ_θ is O(10^{-9}), not
swamped.

On that ray, Re Λ_θ(1/2+it) is positive at 17.024941 and
negative at 17.024943, and the evaluation ball at Table 1
γ₁=17.0249420759926 contains 0 to 10^{-22} once dps=40.
`isolate_maass1_g1` bisects until |b-a|≤10^{-13} with
opposite rigorous signs and 0 outside both endpoint balls.
The balls enclose rounding of the finite trapezoid and of
the FD series. The omitted n-tail in the FD (n>48, y≳√3/2)
and the u-tail (u>e^{4.5}) are exponentially smaller than
10^{-13} in the location. The trapezoid remainder is not a
complete MPFI enclosure of the infinite integral; it is the
Booker–Then *rule* applied to this truncated Λ_θ, and it
recovers their γ₁. Table 1 digits stay their MPFI list.

A Mellin–Barnes AFE and the even-axis Fricke split with
w=−1 are not this evaluator. PARI `lfuncreate` still cannot
take imaginary Γ-shifts. Not Weil.

Cite: Booker–Then 2018; LMFDB Collaboration 2026,
`notes/lmfdb.bib`. Zenodo 15490636 (symmetry 0=even, 1=odd).
