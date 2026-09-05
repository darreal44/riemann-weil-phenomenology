# Beurling conditions, Fourier coefficients, Laplace transform

## Beurling conditions

A separated set Λ (inf gap ≥ δ>0) samples PW_τ if
D⁻(Λ) > τ/π. Strict inequality. Equality on a lattice works;
equality plus a hole does not.

On our lists: short holes give δ≈0.10–0.28. D⁻ > τ/π holds
for χ₁₇, χ₂₉ at μ≤38, and for χ₅ at μ=11. After removing the
desert it holds for χ₅ at μ=22 (`landau-sampling.md`,
`compact-defects.md`). That is the Beurling *condition*
verified as a numerical inequality on finite T, not the
Beurling theorem applied to the infinite set Γ.

Beurling does not produce A ≥ e^{-C τ |E|}. It produces A>0.

## Fourier coefficients of v0

Dumped Q-modes (`report/mode_*.json`):

| | a0² | next | rest |
|---|-----|------|------|
| χ₂₉ μ=22 | 74 % | a2 21 %, a1 4 % | <1 % |
| χ₂₉ μ=38 | 72 % | a2 28 % | <1 % |
| χ₁₇ μ=22 | 71 % | a1 29 % | <1 % |
| χ₅ μ=38 | a0 39 %, a1 49 %, a2 11 % | | <1 % |

The series is two or three terms. χ₅ uses one more harmonic
(N_eff=2.46), consistent with a wider desert and a larger C.
No energy in n≥4. Talking about “high Fourier modes of the
singlet” is talking about 10^{-3} of ||v0||².

## Laplace transform

The Laplace transform of the even window 1_{[-τ,τ]} is
(2/s) sinh(τ s). On the critical line s=1/2+it this is the
archimedean factor of a degree-1 L-function, up to Γ(s/2)
rewrites. Mellin of e^{-π x²} is π^{-s/2} Γ(s/2), the
completed factor of ζ.

None of that is a new computation in this repo: the
archimedean piece of Q is already that Laplace/Mellin
evaluated on the cosine basis (`scan_s` archimedean panel).
The Laplace transform of *v0* as a function of x is
a0 · (2/s) sinh(τ s)/√L plus one or two cosines, i.e. a
rational combination of exponentials e^{±τ s} and
e^{±i ω_n}. It has no pole on the critical line beyond
what the window already has.

A Laplace analysis of Γ (the zeros as a Dirichlet series)
is the explicit formula we started from. It does not
relocate the charged pair.

## Status

Beurling: condition checked on finite lists after compact
cuts. Fourier: v0 is a0+a1+a2. Laplace: already the
archimedean term of Q.
