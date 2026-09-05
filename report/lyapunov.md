# Lyapunov exponents

On ℓ²(Z), the Lyapunov exponent of a transfer matrix T_n(E) is

    γ(E) = lim (1/N) log ||T_N ⋯ T_1||.

γ>0 ⇒ exponential decay of generalized eigenfunctions.

## On v0

The dumped modes have |a_n| / ||v0|| at n=0,1,2 already
carrying >99 %. The ratio −log|a_{n+1}/a_n| is not a limit.
For χ₂₉ μ=22: |a0|=0.86, |a2|=0.46, |a1|=0.21, then <0.06.
There is no N→∞ to take. Quoting γ≈log(0.86/0.06) as a
Lyapunov is a two-point slope, not γ(E).

## On Q as a Jacobi matrix

Tridiagonalizing Q (Lanczos) gives a finite Jacobi matrix
of size N. Products of 2×2 transfers along that path have
a finite-N growth rate (1/N) log ||P_N||. At N=33 that
number exists and depends on the energy in the bulk of Q.
It is not an infinite-volume Lyapunov and it has not been
needed for C(χ), τ₂, or the singlet.

## Status

No γ(E) in the repository. Computing one on these dumps
would be a plot of a finite product, not Anderson 1D.
The decay of v0 is already N_eff≈1.7.
