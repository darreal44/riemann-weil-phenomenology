<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->

# Lemma 2 — hand det at χ₅, μ=16, {e₁, e₂}

Frame (independent of χ, μ), from report/lemma2-2x2.md:

    e₁ = (√2, −1, 0)/√3
    e₂ = (−√2, −2, 3)/√15

Machine (report/2plane-certified.md, dps 36–40):

    H₁₁ = 9.31×10⁻⁵    det H = 1.27×10⁻⁸
    λmin(H) = 3.21×10⁻⁶    λmin(Q₃) = 2.26×10⁻⁶

Sign + is not close on χ₅. Already locked by
tests/test_2plane_det.py.

## Why it is not a hand page

Nine atoms n = p^k < 16, χ₅(5)=0:

    2,3,4,7,8,9,11,13     (5 drops)
    Σ|w| = 4.25
    largest |w|: 7, 11, 13 ≈ 0.72

Dropping any n ≤ 11 flips det (remaining-before-rh).
So a hand bound must keep all nine, plus Arch
(10-term Laplace or Gauss). Each Θ_ij(log n) is
O(1). Target: error ≪ 10⁻⁸ on a 2×2 whose
entries are 10⁻⁴–10⁻³.

That is not a page of fractions. It is the
machine we already ran. Reprinting Arb digits
is not a proof « à la main ».

## Status

Lemma 2 on this frame: numerically closed for
five χ at μ=16. Analytically open (no hand
majorant of the nine atoms + Arch that beats
10⁻⁸). Does not transfer to λ₀(Q) without the
Schur tail. Not W_L. Not RH.
