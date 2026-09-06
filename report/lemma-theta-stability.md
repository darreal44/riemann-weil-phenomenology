# Numerical stability of Q and of λ₀

## Digits of the assembly

µ=16, NB=8. λ₀ versus dps of mpmath.

| L | dps=12 | 16 | 18 | 22 | 28 |
|---|---|---|---|---|---|
| χ₁₃ | 4.787×10⁻⁵ | same | same | same | same |
| χ₅ | 1.617×10⁻¹² | 1.584×10⁻¹² | same | same | same |
| χ₃ | 1.28×10⁻¹³ | 7.62×10⁻¹⁶ | 7.715×10⁻¹⁶ | 7.713×10⁻¹⁶ | same |

χ₁₃ is done at 12 digits. χ₅ moves 2 %
from 12 to 16, then freezes. χ₃ is a
lie at 12 digits (off by 10²) and
settles at 18. Default dps=22 is one
safe notch above that wall.

N_eff and the signs of v do not move
once λ₀ has the right order.

## Entries versus eigenvalues

Q entries are O(1):

    χ₅  min |Q_ij|=5×10⁻³  max=3.3  ‖Q‖_F=7  κ₂=3×10¹²
    χ₃  min |Q_ij|=3×10⁻³  max=2.9  ‖Q‖_F=6  κ₂=4×10¹⁵

λ₀ is not a small entry. It is a
cancellation in v₀ᵀ Q v₀ between
archimedean and prime sums, each O(1).
Losing 12 digits of that difference
is why χ₃ needs dps≥18.

## Weyl on a perturbation of Q

χ₅, 30 random symmetric hits at
relative size ε.

| ε | median |dλ₀| / ‖dQ‖₂ | max |dλ₀| |
|---|---|---|
| 10⁻¹⁶ | 0.85 | 10⁻¹⁵ |
| 10⁻¹² | 0.24 | 2×10⁻¹² |
| 10⁻⁸ | 0.23 | 2×10⁻⁸ |

The bound |dλ₀| ≤ ‖dQ‖₂ is honest
(factor 0.2–0.9). A relative 10⁻¹²
error on Q, the size of float64
roundoff times κ, already moves λ₀
by its own size. That is the χ₃
float64 story again.

## Rules

- Assemble in mpmath, dps ≥ 18 at
  these windows, 22 by default.
- Cast to float64 only for N_eff /
  participation (O(1) coordinates).
- Do not trust numpy λ₀ when
  −ln λ₀ ≳ 30 (χ₃, ζ deep).
- A 10⁻⁸ relative bump on Q is a
  10⁻⁸ bump on λ₀, not a 10⁻⁸ bump
  on −ln λ₀. ell₀ moves by ~20 at
  that noise — the "plateau" of ell
  is only as stable as Q's digits.
