# Arnoldi versus Lanczos on Q

Q is SPD. Arnoldi on Q *is* Lanczos:
the Hessenberg H is symmetric to
roundoff, and the Ritz values match
to 10⁻¹⁶.

## Q, unshifted, 2-hat start

| L | m | Arn λ_min | Lan λ_min | |A−L| | ‖H−Hᵀ‖ |
|---|---|---|---|---|---|
| χ₅ | 2 | 2.207×10⁻³ | same | 10⁻¹⁶ | 10⁻¹⁷ |
| χ₅ | 6 | 4.601×10⁻⁵ | same | 10⁻¹⁷ | 10⁻¹⁶ |
| χ₁₃ | 6 | 2.911×10⁻⁴ | same | 10⁻¹⁶ | 10⁻¹⁶ |

Same wrong end of the spectrum as
plain Lanczos. Arnoldi does not help.

## Q⁻¹ (shift-invert, σ=0)

| L | m | 1/θ_max | |A−L| | ‖H−Hᵀ‖ |
|---|---|---|---|---|
| χ₅ | 2 | 1.584×10⁻¹² | 10⁻²³ | **18** |
| χ₁₃ | 2 | 4.787×10⁻⁵ | 10⁻²⁰ | 10⁻¹¹ |

Ritz extrema still agree. H itself
does not, on χ₅: κ₂(Q)~10¹², so the
float64 action of Q⁻¹ is only
"approximately" SPD. Arnoldi records
that loss in a non-symmetric H.
Lanczos forces T = Tᵀ by storing
only (α, β). That is the reason to
keep Lanczos on a true SPD inverse.

## Cost

Arnoldi: m² inner products (Hessenberg
fill). Lanczos: 2m (tridiagonal).
At dim 9 both are free. At dim 512
with m ~ 20, Lanczos is the one that
stays O(m) and keeps symmetry.

Use Lanczos, shift-invert, σ=0.
Arnoldi is for a non-symmetric
Hecke action, which Q is not.
