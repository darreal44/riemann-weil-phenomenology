# D_max against Q, not only against the zero Gram

Claude’s count

    D_max = max_γ (γ L/2π − N_Γ(γ))

is discrete Landau on the zero Gram.
The same number, run on the same
windows, against Q_N (prime-side):

| fenêtre | N | D_max | #{ℓ_Q>2}* | ℓ_Q | ℓ_Q/D | 11 D |
|---|---|---|---|---|---|---|
| χ₅ µ=16 | 17 | 3.08 | 3 | 33.1 | **10.77** | 33.8 |
| χ₅ µ=16 | 9 | 3.08 | 3 | 27.2 | 8.84 | 33.8 |
| χ₃ µ=16 | 17 | 5.00 | 5 | 47.9 | 9.59 | 55.0 |
| χ₈ µ=16 | 9 | 2.00 | 2 | 18.4 | 9.18 | 22.0 |
| χ₁₃ µ=16 | 9 | 1.19 | 1 | 9.9 | 8.35 | 13.1 |
| χ₃ µ=80 | 9 | 6.00 | 6 | 51.6 | 8.61 | 66 |
| χ₃ µ=80 | 17 | 11.00 | 8† | 84.7 | 7.70 | 121 |
| χ₃ µ=80 | 25 | 14.00 | 8† | 111.1 | 7.94 | 154 |

\* first eight eigenvalues only, the
list `assemble` returns. † truncated
by that cap: the full count at N=25
is 12 modes with λ<10⁻³
(`spectral-convergence.md`).

## Two regimes

On a resolved short window (χ₅ µ=16,
N=17) the law transfers to Q:
D_max = 3 = number of deep Q-modes,
ℓ_Q / D = 10.77 against 11.0. The
zero Gram and the prime-side form
see the same free dimension.

On χ₃ µ=80, D_max tracks the empty
Nyquist volume and grows with N
(6, 11, 14) because ω_max = 2π N/L
sweeps more desert. Q’s depth grows
too (52, 85, 111) but slower:
ℓ_Q / D stays at 8, not 11.
11 D_max = 154 would be the Gram
prediction at N=25; Q is 28 % short.
That is the Galerkin remainder
already measured (ℓ still climbing
3.9 nats/hat at the wall).

So the constant 11 is a property of
the *saturated* Gram. Q agrees with
it once the hat space resolves the
well (χ₅). It does not agree while
the well is still eating new hats
(χ₃ µ=80). D_max itself is not
wrong; it counts dimensions the
window will eventually free, not
the ones Q_N has already paid for.

N_eff of v₀ is another object:
it stays near 3 at µ=80 while
D_max = 14. Participation of the
ground state ≠ number of small
eigenvalues. Landau counts the
ladder; N_eff describes the first
rung’s support.

Data: `report/Dmax-vs-Q.json`.
