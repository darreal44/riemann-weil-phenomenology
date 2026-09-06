# Eigenvalues of H on {e₁, e₂}

Three-hat window, H = Q restricted to
ker ψ(0). Frame fixed:

    e₁ = (√2, −1, 0)/√3
    e₂ = (−√2, −2, 3)/√15

Angle = argument of the λ_min
eigenvector in that frame (0° = e₁).
H/S = λ_min(H) / λ_min(Q|_{3}).

## µ = 16

| χ | λ_min(H) | λ_max(H) | cond | H/S | angle |
|---|---|---|---|---|---|
| χ₅ | 3.21×10⁻⁶ | 3.95×10⁻³ | 1.2×10³ | 1.42 | 9° |
| χ₃ | 6.31×10⁻⁸ | 8.98×10⁻³ | 1.4×10⁵ | 1.71 | 9° |
| χ₄ | 1.11×10⁻⁵ | 1.09×10⁻¹ | 9.8×10³ | 1.97 | 6° |
| χ₈ | 1.73×10⁻⁴ | 1.15 | 6.6×10³ | 2.14 | 2° |
| χ₇ | 2.72×10⁻⁵ | 1.74 | 6.4×10⁴ | 2.09 | 180° |
| χ₁₃ | 2.08×10⁻³ | 2.35 | 1.1×10³ | 2.42 | 163° |
| χ₂₉ | 0.566 | 1.78 | 3.1 | 5.48 | 113° |

## µ = 22

| χ | λ_min(H) | λ_max(H) | cond | H/S | angle |
|---|---|---|---|---|---|
| χ₅ | 6.88×10⁻⁷ | 1.16×10⁻² | 1.7×10⁴ | 1.46 | 8° |
| χ₃ | 5.51×10⁻⁸ | 5.28×10⁻⁴ | 9.6×10³ | 1.17 | 11° |
| χ₄ | 7.60×10⁻⁷ | 8.66×10⁻⁴ | 1.1×10³ | 1.59 | 8° |
| χ₈ | 3.22×10⁻⁵ | 0.518 | 1.6×10⁴ | 1.79 | 4° |
| χ₇ | 1.59×10⁻⁴ | 1.14 | 7.2×10³ | 2.08 | 3° |
| χ₁₃ | 1.27×10⁻³ | 2.80 | 2.2×10³ | 2.76 | 169° |
| χ₂₉ | 0.150 | 1.85 | 12 | 3.91 | 120° |

## What the spectrum says

1. Two regimes. Deep wells (χ₅, χ₃, χ₄,
   χ₈): ground state of H is e₁ to
   10°. Shallow wells (χ₁₃, χ₂₉): it
   sits on e₂ (160° / 115°). χ₇
   switches between the two as µ
   goes 16 → 22.

2. Conditioning is the depth. cond(H)
   = λ_max/λ_min tracks ℓ: χ₃ at
   10⁵, χ₂₉ at 3. The 2×2 is ill-conditioned
   exactly where cancellation in Q(f₁)
   is tight. A bound on det H must
   survive that.

3. H does not lose the sign of Q|_{3}.
   H/S ∈ [1.17, 2.8] except χ₂₉
   (shallow, 4–5). The Schur tail
   outside the 2-plane is a factor
   two, not 10¹⁴. Proving λ_min(H)>0
   is the same problem as Lemma 2
   at three hats, up to that factor.

4. λ_max(H) is O(10⁻³) to O(1),
   never the small number. The
   large eigenvalue is the direction
   that did *not* cancel. On deep
   wells that direction is e₂.

5. Growing µ from 16 to 22 multiplies
   cond by ~10 on χ₅ (deeper well,
   same angle). The eigenvector
   does not rotate; only the gap
   opens. A proof can freeze the
   test vector at e₁ for those χ
   and lose a factor ~1/cos²10° ≈ 1.03.
   That fails for χ₁₃ / χ₂₉.

Data: `report/H-spectrum.json`.
