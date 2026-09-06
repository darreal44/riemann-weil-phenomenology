# Monte Carlo on χ₄, χ₈, χ₁₃

Same protocol as χ₅, χ₃, χ₇. µ=16, NB=8.

## Haar, 8000 draws

| L | λ₀ | P(Q<0) | P(Q<10 λ₀) | med | λ₁/λ₀ |
|---|---|---|---|---|---|
| χ₄ | 2.9×10⁻¹³ | 0 | 0 | 1.65 | 2.2×10⁵ |
| χ₈ | 1.1×10⁻⁸ | 0 | 0 | 2.25 | 2.6×10⁵ |
| χ₁₃ | 4.8×10⁻⁵ | 0 | 0 | 2.69 | 4.2×10³ |

Same needle. χ₁₃ has the fattest kernel
(smallest gap) and still zero Haar hits.

## Importance, 4000 draws

On span{v₀, v₁} (the two lowest
eigenvectors) versus on the first four
hats.

| L | plane | P(Q<10 λ₀) | min hit |
|---|---|---|---|
| χ₄ | 2-ev | 0.47 % | 3.3×10⁻¹³ |
| χ₄ | 4-hat | 0 | 6.8×10⁻⁴ |
| χ₈ | 2-ev | 0.43 % | 1.1×10⁻⁸ |
| χ₈ | 4-hat | 0 | 1.1×10⁻³ |
| χ₁₃ | 2-ev | 2.9 % | 4.8×10⁻⁵ |
| χ₁₃ | 4-hat | 0 | 6.3×10⁻³ |

The 2-eigenplane finds the floor; the
4-hat coordinate plane does not, because
the ground state is not axis-aligned in
the hat basis. Importance sampling works
only after you already own v₀ — at which
point you already own λ₀.

Same conclusion as the first three:
MC on v does not discover the lemma.
χ₁₃ is the least thin (gap 4×10³, hit
rate 3 % in the 2-plane) and still
invisible to Haar.
