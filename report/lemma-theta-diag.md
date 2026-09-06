# Diagonalization of Q

µ=16, NB=8, S assembled at dps=22 then
cast to float64 for numpy.eigvalsh.

## Spectrum

One needle, one small, then the bulk.

| L | λ₀ (mp) | λ₀ (np) | λ₁ | λ₂…λ₈ | κ₂(Q) |
|---|---|---|---|---|---|
| χ₅ | 1.58×10⁻¹² | same | 2.8×10⁻⁷ | 0.006 … 4.0 | 2.6×10¹² |
| χ₃ | 7.71×10⁻¹⁶ | 9.71×10⁻¹⁶ | 4.6×10⁻¹¹ | 8×10⁻⁷ … 3.6 | 3.7×10¹⁵ |
| χ₄ | 2.92×10⁻¹³ | same | 6.5×10⁻⁸ | 6×10⁻⁴ … 3.8 | 1.3×10¹³ |
| χ₇ | 1.28×10⁻⁸ | same | 3.6×10⁻³ | 0.49 … 4.6 | 3.6×10⁸ |
| χ₈ | 1.07×10⁻⁸ | same | 2.8×10⁻³ | 1.0 … 4.2 | 3.9×10⁸ |
| χ₁₃ | 4.79×10⁻⁵ | same | 0.20 | 1.6 … 5.6 | 1.2×10⁵ |

Q is exactly symmetric after the cast
(‖Q−Qᵀ‖=0). No negative eigenvalue at
this window.

## What float64 can see

eps ≈ 2×10⁻¹⁶. χ₃ has κ₂ ∼ 10¹⁵, so
numpy's λ₀ is a 25 % relative lie
(9.7 vs 7.7 ×10⁻¹⁶). The sign is still
right. χ₅ and above are safe in float64
for λ₀ itself; the eigenvector of χ₃
is not, past the third digit.

scan_s keeps the eigenproblem in mpmath
for that reason. Casting S to numpy is
only for N_eff / participation, which
live on the O(1) coordinates of v.

## What to call

- dim 9, λ₀ ≳ 10⁻¹²: `numpy.linalg.eigh`.
- χ₃ / deeper: mpmath `eigsy` on the
  mp matrix, as assemble already does.
- λ₀ only: inverse iteration from a
  4-hat guess, 3–4 steps. The rest of
  the spectrum is not the lemma.
- Do not SVD. Q is SPD at these windows;
  eigh uses the symmetry.

The bulk {λ₂,…,λ₈} ⊂ [0.3, 5] is the
Haar median ∼ 2. The lemma is the two
(sometimes three) eigenvalues below 10⁻³.
EOF
cd /tmp/rwdiag
# wait don't put token in file - the END is in write only
true
