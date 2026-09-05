# Mass of v0 and ∂ell/∂γ on the zero Gram (5 September 2026)

Zero-side Gram G_nm = 2 Σ_k φ_n(γ_k) φ_m(γ_k) in the cosine window
basis of scan_s / music_zeros. Finite difference ε = 0.02 on each γ.

## χ₂₉, μ = 22, N = 25 (ell_G = 5.65 against Q ell = 5.49)

| k | γ | mass | ∂ell/∂γ |
|---|---|------|---------|
| 1 | 1.79 | 0.1 % | −1.30 |
| 2 | 5.32 | 1.0 % | −1.20 |
| 3 | 6.76 | 3.1 % | −0.97 |
| 4 | 8.63 | 6.6 % | −1.04 |
| 5 | 10.42 | **33 %** | −1.64 |
| 6 | 11.20 | **28 %** | +1.18 |
| 7 | 13.07 | 2.6 % | +0.33 |

Desert γ₁ is invisible to v0. The cost sits on the close pair
(10.42, 11.20), gap 0.78 against ν = 2.03 — *under* Nyquist, mid-band
(Nyquist edge of the basis ~ 49).

## χ₁₇, μ = 22, N = 25 (ell_G = 12.68 against Q ~ 12.3)

Same picture. Desert 3.73: mass 0.0 %. Pair (15.64, 16.27): 21 % + 22 %.

## χ₅, μ = 11, N = 21

Desert 6.65: mass 0. Mass on 28.5–29.7 (band, not cutoff ~ 53).

## Reading

The term is not |E_L| and not (γ₁−ν)_+. The bottom mode of the Gram
lives on a mid-band tight pair. Opening that pair changes ell by
O(1) per unit of γ; moving γ₁ does almost nothing to the Rayleigh
quotient of v0 (the derivative is the constraint of the *other*
eigenvectors).

C(χ) in ell ~ C(χ) L|E| is a proxy for “where the first tight pair
sits in the window”, not a second length functional. Next: the same
profile at two N, to kill a cutoff artefact, and one plot of mass
versus (gap/ν).

## Two N (cutoff check) and mass vs gap/ν

χ₂₉ μ=22: pair (10.42, 11.20) holds 65→60 % of v0 from N=17 to 41.
ell_G = 5.76 → 5.59. Not a cutoff artefact.

χ₁₇ μ=22: pair (15.64, 16.27) holds 35→45 % over the same N.

gap/ν on χ₂₉, N=33: the charged pair has gap/ν = 0.38. A tighter pair
at 17.81–18.51 (gap/ν = 0.34) carries 3 %. Tightness is not enough;
the pair has to sit where the bottom mode of the *window* can live.
