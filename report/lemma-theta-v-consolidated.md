# Lemma Θ_v — consolidated

## Statement

Let Q_L be the prime-side truncated Weil form on the
hat basis of the window [0, L], L = log µ, and let v
be its ground state. The associated test function
Θ_v(y) = ∑_{n,m} v_n v_m θ_{nm}(y) is the
autocorrelation of the time-side reconstruction

    ψ(t) = v₀ L^{−1/2} + ∑_{n≥1} v_n (2/L)^{1/2} cos(2π n t / L).

Then, for ζ at µ ∈ {8, 11, 16} and dim 9:

1. v = (v₀, −v₁, +v₂, −v₃, …) with k̄ ∈ [0.76, 0.88].
   The pattern is the Q-compromise of two almost
   orthogonal axes (archimedean n=1 spike, prime-2
   tower ≈ e₀). A 2×2 on those axes already gives
   the first two signs and λ ∼ 10⁻³; rungs n=2,3
   take λ to 10⁻²¹.
2. ψ is a bump even about L/2. Its bulk is Gaussian

       ψ(t) ≈ ψ_mid exp( − a (t − L/2)² ),
       a L² = −ln λ₀   (rel. err. < 4 %).

3. Its edge is twice the Gaussian tail:
   −ln|ψ(0)| ≈ (−ln λ₀)/2, hence −ln λ₀ ≈ 2 (−ln|ψ(0)|).
   That doubling is the 4-mode Dirichlet wall.
4. Θ_v > 0 on (0,L), Θ_v(L)=0. In the bulk of y,
   autocorr of (2) is Gaussian (the y² side).
   Near y → L the wall dominates and the empirical
   envelope is y e^y (the other side of §123).
5. A desert Slepian of [0,γ₁], or any spectral
   weight e^{−αω} on the desert, has the same
   *class* but not the same function: y e^y is
   the time-edge, not the desert.

## What this does not prove

- Why Q selects exactly four modes (a spectral
  gap after n=3, uniform in µ).
- Why the wall doubles the Gaussian tail
  (a calculation in span{η₀…η₃}, doable).
- The same identities for L-functions other than ζ
  (χ₅ is the first check).
- RH. The lemma locates Θ_v as autocorr of a
  mid-window Gaussian with a Dirichlet wall.
  Positivity of Q on a dense class is still open.

## Files

`theta_v_qpr.py`, `theta_vs_slepian.py`,
`lemma-theta-{profile,weight,modes,signs,who,2x2,phi,edge,bulk,curvature}.md`.
