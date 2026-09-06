# Lanczos on Q

Unshifted Lanczos from the 2-hat guess
(1, −1, 0, …). Full reorthogonalization.
Ritz values of the tridiagonal T_m
against eigsy.

## µ=16, NB=8

| L | m | ritz₀ | λ₀ | rel |
|---|---|---|---|---|
| χ₅ | 2 | 2.2×10⁻³ | 1.6×10⁻¹² | 10⁹ |
| χ₅ | 4 | 3.5×10⁻⁴ | | 10⁸ |
| χ₅ | 6 | 4.6×10⁻⁵ | | 10⁷ |
| χ₅ | 9 | 1.6×10⁻¹² | | 10⁻⁴ |
| χ₃ | 6 | 3.0×10⁻⁶ | 9.7×10⁻¹⁶ | 10⁹ |
| χ₃ | 9 | 8.0×10⁻¹⁶ | | 0.18 |
| χ₁₃ | 6 | 2.9×10⁻⁴ | 4.8×10⁻⁵ | 5 |
| χ₁₃ | 9 | 4.8×10⁻⁵ | | 0 |

λ₀ arrives only when m = dim. Lanczos
finds the edges of the *numerical range
of Q*, and those edges are the bulk
{O(1)}, not the needle. The 2-hat
guess looks like a mid-spectrum vector
to Q itself (Rayleigh ~ 10⁻²).

χ₃ at m=9 still has 18 % error on λ₀
in float64 — same κ₂ ~ 10¹⁵ story.

## Shift-invert is inverse iteration

Lanczos on Q⁻¹, one step, is

    T₁ = ⟨v, Q⁻¹ v⟩ / ⟨v,v⟩  =  1 / Rayleigh(Q^{-1}).

That is inverse iteration at σ=0, which
hits λ₀ in one LU. Building a longer
Krylov for Q⁻¹ would recover λ₁, λ₂, …
in a few more matvecs with Q⁻¹. At dim
9 that is `eigsy`. At dim 512 it is the
right tool if several small eigenvalues
are wanted, not just λ₀.

Do not run unshifted Lanczos for the
lemma. The spectrum that matters is the
wrong end of Q.
