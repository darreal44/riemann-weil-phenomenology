# Landau sampling sets

## The theorem (Landau 1967)

For the Paley–Wiener space PW_τ:

- if Λ is a sampling set, then D⁻(Λ) ≥ τ/π;
- if Λ is an interpolating set, then D⁺(Λ) ≤ τ/π.

Density is the Beurling lower/upper density (sliding counts).
The constant τ/π is Nyquist: one point per Nyquist cell
ν = π/τ on average. The statement is *necessary*, not
sufficient. A lattice of spacing exactly ν samples; a set
with D⁻ ≥ τ/π and a large hole need not.

## Against the lists

τ/π = log μ / (2π). Sliding D⁻ at r=50 (`bm_density.py`):

| χ | D⁻ | μ=11 (0.38) | μ=22 (0.49) | μ=38 (0.58) |
|---|-----|-------------|-------------|-------------|
| χ₅ | 0.42 | ≥ | < | < |
| χ₁₇ | 0.62 | ≥ | ≥ | ≥ |
| χ₂₉ | 0.70 | ≥ | ≥ | ≥ |

Landau *forbids* sampling of PW_{log 22 / 2} by χ₅ if one
believes D⁻=0.42 is the true lower density. It does not,
once the desert is treated as a compact defect
(`compact-defects.md`): D⁻ after γ₁ is 0.50, which meets
0.49. Landau on the raw list is a certificate only after
the compact piece is removed, or after one uses BM exterior
density (which Landau does not).

D⁺ is 0.88–1.16 > τ/π at these μ. Landau then says Γ is
*not* interpolating for those PW_τ — too many points in
the rich windows. We do not need interpolation; we need
sampling (a lower bound on Σ |F(γ)|²).

## Landau vs Beurling vs BM

- Landau: necessary D⁻ ≥ τ/π. No construction, no constant A.
- Beurling: a *separated* set with D⁻ > τ/π is sampling.
  Strict inequality, plus δ>0. Our short holes give δ.
- Duffin–Schaeffer: gap *upper* bound ≤ ν, not a density.
  Stronger locally, silent on large holes.
- Beurling–Malliavin: necessary *and* sufficient in terms
  of the exterior density. The object we have not computed.

On S (short holes only) Landau is satisfied with room:
mean short gap ~ ν/2, so local density ~ 2 τ/π. On Γ
including E, Landau is the inequality D⁻ ≥ τ/π which the
desert can violate in a sliding count and which the
exterior density should restore.

## What we do not get

A Landau density of E_L itself. E is a union of intervals,
not a point set. Landau on the endpoints ∂E is a count of
n_∂ / T → 0. The hiding set is not a sampling set; it is
the complement of one.
