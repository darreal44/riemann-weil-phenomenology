# Iterative eigensolvers versus eigsy

Q is 9×9 SPD, λ₀ ~ 0. The right
iterative method is inverse iteration
at σ=0, not a full `eigsy`.

Guess: v = (1, −1, 0, …) / √2
(the 2-hat sign of the lemma).

## µ=16, NB=8, dps=22

| L | method | λ | rel to eigsy | steps |
|---|---|---|---|---|
| χ₅ | eigsy | 1.5837×10⁻¹² | — | all 9 |
| χ₅ | inv σ=0 | same | 8×10⁻¹² | 1 |
| χ₅ | RQI | same | 8×10⁻¹² | 6 |
| χ₃ | eigsy | 7.7132×10⁻¹⁶ | — | all 9 |
| χ₃ | inv σ=0 | same | 3×10⁻⁹ | 1 |
| χ₃ | RQI | same | 3×10⁻⁹ | 6 |
| χ₁₃ | eigsy | 4.7871×10⁻⁵ | — | all 9 |
| χ₁₃ | inv σ=0 | same | 0 | 1 |
| χ₁₃ | RQI | same | 0 | 4 |

Inverse iteration at 0 lands on λ₀ in
one LU because the guess already has
the 2-mode signs and every other
eigenvalue is 10³–10⁶ times larger.
RQI starts from the Rayleigh of that
guess (~10⁻²) and walks down cubically;
it needs the path, not the answer.

Cost at dim 9 is irrelevant (0.02 s).
The reason to keep the iterator is dim
512 (2-adic), where `eigsy` is N³ and
one wants only λ₀. There: factor Q once,
apply inv-iter 3–4 times, stop.

Do not shift into the bulk. σ=0 is the
shift. `eigsy` stays the reference for
the 9×9 lemma.
