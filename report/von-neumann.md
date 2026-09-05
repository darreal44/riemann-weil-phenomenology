# Von Neumann entropy

For a density ρ, S(ρ) = −Tr ρ log ρ.

## Pure mode

ρ = |v0⟩⟨v0| has S = 0. The number we already quote is the
*Shannon* entropy of the coefficients in the cosine basis,
S_Sh(v0) = −Σ p_n log p_n with p_n = |⟨n|v0⟩|².

At μ=22, N=37:

| | S_Sh(v0) | N_eff |
|---|----------|-------|
| 11a1 | 0.80 | 2.11 |
| χ₂₉ | 0.72 | 1.68 |
| χ₅ | 0.77 | ~2 |

Two to three occupied bars. Not a thermodynamic entropy.

## Spectrum as a state

ρ = G / Tr G (Gram eigenvalues, normalized). Then
S_vN(spec) ≈ 3.4–3.5 against ln N = 3.61. The bulk of G is
almost maximally mixed. λ0 does not contribute to the trace
(it is 10^{-6}–10^{-10} of Tr G). This S is “how many O(1)
modes sit in the window”, i.e. N minus a few, not a
localization diagnostic.

## Status

Von Neumann does not add a scale beyond N_eff and λ1/λ0.
No temperature, no entanglement cut. Do not treat S_vN(spec)
as an entropy of the zeros.
