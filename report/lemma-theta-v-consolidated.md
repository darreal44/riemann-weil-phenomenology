# Lemma Θ_v — current state

v = ground state of prime-side truncated Weil
Q_L on hats of [0, L], L = log µ.
ψ = cosine reconstruction of v.

## Holds

1. **Even bulk.** ψ(L−t)=ψ(t). On ζ (N_eff ≳ 3)
   ψ(t) ≈ ψ_mid exp(−a (t−L/2)²) with
   a L² = −ln λ₀. Quartic b/a² = 0.06 → 0.03.
2. **ONB ratio.** Once −ln λ₀ ≳ 20,
   v₀/|v₁| = 2^{−1/2} exp(π²/(−ln λ₀))
   to a few percent on ζ, χ₃, χ₅. It is
   ⟨δ_{L/2}, η₀⟩ / ⟨δ_{L/2}, η₁⟩ times the
   Gaussian form factor. Not a Weil number.
3. **Edge doubling.** −ln λ₀ = 2(−ln|ψ(0)|)+R
   with R = 2.40 ± 0.05 nats on ζ
   (ratio 2.09–2.21 on χ₃, χ₄, χ₅, 11a1).
   Q sees φ ⊗ φ. The spatial Gaussian tail
   a L²/4 is not the edge.
4. **C = λ₀ / ψ(0)² = L λ₀ / ε²**,
   ε = v₀ + √2 ∑ vₙ.
   On ζ, C → 1/(4e) after four modes.
   Off ζ, C stays at the two-mode size 0.12–0.16.
   C_bump ≠ C_Riesz = L/(wᵀ Q⁻¹ w): the
   ground state is not the representer of δ₀.
   ε_Q is 10³–10⁴ times smaller than a
   truncated-Gaussian ε. Q kills the edge.
5. **Axes.** Signs +−+− on ζ = arch n=1
   spike mixed with a tower ≈ e₀, 81° apart.
   2×2 of that plane: first two signs, λ ∼ 10⁻³.
   Rungs n=2,3 take the remaining decades on ζ.
6. **N_eff.** ζ: 3.1–3.4. χ₅: frozen 2.14
   past NB=8. χ₃: creeps to 2.32 at NB=16,
   dps=30, v₂=0.28, a L² still only 62 % of
   −ln λ₀. Four-mode curvature needs N_eff ≳ 3.

## Does not hold / not proved

- Spectral gap after n=3, uniform in µ.
- a L² = −ln λ₀ off ζ (χ₃ not there yet).
- Positivity of Q on a dense class (RH).
- Identification of R or 1/(4e) with a
  named constant of the explicit formula.

## Reduction

dim 9 is enough to assemble. Keep hats
n=0..3 on ζ, n=0,1 off ζ for interpretation.
`code/reduce_Q.py NAME µ NB dps`.
Do not invert Q on w to get C.

## Files

profile, weight, modes, signs, who, 2x2,
phi, edge, bulk, curvature, factor2, deficit,
sqrt2, higher, C, C-2x2, C-derivation, C-riesz,
eps, dimred, reduce, Neff-scan,
chi5, chi5-Neff, chi3, chi3-dps30, chars,
edge-chars, 11a1.
