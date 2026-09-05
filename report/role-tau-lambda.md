# Role of τ_Λ

    τ_Λ(λ) = Tr(P̂_Λ P_Λ ϑ(λ))

on the ord₂=0 slice (`trace_dist.py`). P_Λ is the cutoff to
the additive interval [0,Λ]. ϑ(λ) is the dilation by λ,
twisted by λ^{-1/2}.

## What it is

A function of the module. Archimedean, it reproduces CC (39)
pointwise to a few percent away from λ=1. Semi-local minus
archimedean, it *locates* the place 2 as peaks at λ=2^{±1}.
Theorem 4 of Connes (1999) says that, as measures on
(R_+*, d*λ),

    τ_Λ  →  2 log' Λ · δ_1  +  τ_∞  +  τ_2

as Λ→∞, in the sense of pairings against test functions on
the module. τ_Λ is that left-hand side, at finite Λ.

## What it is not

- Not Q_L. Q is the truncated Weil form on the critical-line
  window of length L=log μ, assembled from primes and the
  archimedean panel. Different cutoff, different Hilbert
  space, different test functions.
- Not h and not h_Λ. h is the test *against* which τ is
  paired. h_Λ is one matrix element of ϑ. τ_Λ is the trace.
- Not the 2-adic mass. The mass 1/√2 is ⟨τ₂, 1_{near 2}⟩,
  a pairing of the *limit* distribution, not a value of τ_Λ(2).

## Why it exists in the repo

To check Theorem 4 on {∞,2}: location of the peaks (yes),
weight of the peaks (no, Gibbs). Once d*λ = d*u is locked,
τ_Λ’s job for the mass is done. Further values of τ_Λ(λ)
are a numerical illustration of the same trace, not a
second determination of 1/√2.
