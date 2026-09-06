# Lemma Θ_v — consolidated (ζ + Dirichlet + GL₂)

Let v be the ground state of the prime-side truncated
Weil form Q_L on the hat basis of [0, L], L = log µ,
and ψ the cosine reconstruction of v.

## What holds

1. **Bulk.** ψ is even about L/2. When N_eff ≳ 3
   (ζ at these windows),
   ψ(t) ≈ ψ_mid exp(− a (t−L/2)²) with a L² = −ln λ₀.
2. **ONB ratio.** Once −ln λ₀ ≳ 20,
   v₀/|v₁| = 2^{−1/2} exp(π²/(−ln λ₀))
   to a few percent (ζ, χ₃, χ₅; χ₄ a bit worse).
   This is a delta at L/2 against (η₀, η₁), times
   the Gaussian form factor. Not a Weil number.
3. **Edge doubling.** −ln λ₀ = 2 (−ln|ψ(0)|) + O(1)
   with ratio in [2.09, 2.21] for ζ, χ₃, χ₄, χ₅
   and 11a1. Q sees φ ⊗ φ.
4. **Axes.** On ζ the signs +−+− are the mix of
   an archimedean n=1 spike and a tower ≈ e₀,
   almost orthogonal. 2×2 gives the first two
   signs and λ ∼ 10⁻³; rungs n=2,3 take the
   remaining decades. Characters live at N_eff ≈ 2
   in dim 9: only the first two signs.
5. **Θ_v** is the autocorrelation of ψ. y² is the
   bulk; y e^y is the Dirichlet wall near y → L.
   A desert Slepian is the same class, not the
   same function.

## What this does not prove

- Spectral gap after n=3, uniform in µ.
- Positivity of Q on a dense class (RH).
- The same curvature law a L² = −ln λ₀ off ζ
  (needs N_eff ≳ 3, so larger NB or larger µ).

## Files

`theta_v_qpr.py`, `lemma-theta-{profile,weight,modes,signs,who,2x2,phi,edge,bulk,curvature,factor2,deficit,sqrt2,chi5,chi3,chars,edge-chars,11a1}.md`.
