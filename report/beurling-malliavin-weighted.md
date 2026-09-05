# Weighted Beurling–Malliavin, as far as a script goes

## Classical densities on the harvested lists (T≈320)

Sliding windows of length r=50:

| χ | D⁻ | D⁺ |
|---|----|----|
| χ₅ | 0.42 | 0.88 |
| χ₁₇ | 0.62 | 1.06 |
| χ₂₉ | 0.70 | 1.16 |

Weyl says the *mean* density at height T is (1/2π) log(qT/2π),
which at T=320 is already ~0.6–0.8. D⁻ is pulled down by the
desert: it is a global min, so it sees γ₁. That is why D⁻(χ₅)
is the smallest.

## Sampling vs type

PW_τ is sampled by Γ when D⁻(Γ) > τ/π (Beurling). τ/π = L/(2π)
= log μ / (2π): 0.38 at μ=11, 0.49 at μ=22, 0.58 at μ=38.

At μ=11, D⁻ > τ/π on the three hold-outs (even χ₅: 0.42 > 0.38).
At μ=22, χ₅ has 0.42 < 0.49: the *windowed* D⁻ computed on [0,320]
is no longer a sampling certificate, because the desert is a
finite defect and BM density ignores compact perturbations.
The correct object is the Beurling–Malliavin *exterior* density,
which does not see [0,γ₁] once it is compact. We have not computed
that exterior density (it is a limsup of harmonic measures, not
a sliding count).

## Weight 1_{E_L}

E_L is open, finite measure, compact if one cuts at T₀. Γ ⊂ ∂E ∪ S,
S = R_+ \ E. Every zero sits in S (the gaps that are ≤ ν) or on ∂E.
Sampling of PW_τ is sampling by S ∪ ∂E. The weight 1_{E_L} does
not remove zeros; it removes the *hiding set* from the domain of
concentration. The BM density that would close
c_L ≥ exp(−C τ |E|) is the density of Γ for the space
PW_τ ∩ {functions small on E}, i.e. a multiplier radius for the
outer function of E.

## Multiplier radius — not computed

Beurling–Malliavin: a real set Λ has radius of completeness
R(Λ) = π D_BM(Λ). For Λ=Γ and a hole E, one wants

    R(Γ; E) ≥ τ − C |E|

or the opposite sign depending on convention. A numerical D⁻
is not D_BM. No radius is produced here. The script
`code/bm_density.py` stops at D± and at the comparison D⁻ ≷ τ/π.

## Status

Named object: written. Sliding densities: measured. Exterior BM
density and the multiplier of E: open, still the article.
