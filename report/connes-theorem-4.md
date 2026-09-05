# Connes 1999, Theorem 4

Source: A. Connes, *Trace formula in noncommutative geometry
and the zeros of the Riemann zeta function*, Selecta Math. 5
(1999), 29–106. S-local case, §VII. Local companion is
Theorem 3 (one local field).

## Statement

Let S be a finite set of places of Q, A_S the S-adèles,
C_S = A_S^* / Q_S^* the S-idèle class group (notation of the
paper). Let α = ∏_{v∈S} α_v be a basic character. Let
h ∈ S(C_S) have compact support. Let P_Λ be the cutoff to
|x| ≤ Λ and R_Λ = P̂_Λ P_Λ. Then, as Λ → ∞,

    Tr(R_Λ U(h))
        = 2 h(1) log' Λ
          + Σ_{v∈S} ∫'_{k_v^*} h(u^{-1}) / |1−u|_v  d^*u
          + o(1).

Here 2 log' Λ = ∫_{λ∈C_S, |λ|∈[Λ^{-1},Λ]} d^*λ, each k_v^*
embeds in C_S by u ↦ (1,…,u,…,1), and ∫' is the principal
value: the unique distribution on k_v that agrees with
du/|1−u| off u=1 and whose Fourier transform (relative to
α_v) vanishes at 1.

## What each term is here

S = {∞, 2} in the semi-local notes.

- 2 h(1) log' Λ — the identity orbit, our n=0 / λ=1 term.
  We set w_0 = 0 in τ₂ so as not to mix it with place 2.
- v = ∞ — the integral ∫'_{R^*} h(u^{-1}) / |1−u| d^*u,
  which after the λ^{1/2} twist is CC (39),
  τ_∞(λ) = λ^{1/2}/2 (1/(1+λ) + 1/|1−λ|).
- v = 2 — ∫'_{Q_2^*} h(u^{-1}) / |1−u|_2 d^*u, the local
  pairing of `tau2_local.py` / `connes-h-vs-hLam.md`.
  Shells n=±1 give the masses 1/√2 against h≈1 near
  λ=2^{±1}.

U(h) = ∫ h(λ) ϑ(λ) d^*λ is the integrated dilation. τ_Λ(λ)
of `trace_dist.py` is the density of Tr(R_Λ ϑ(λ)), i.e. the
left-hand side before integrating against h.

## What the theorem does not say

It does not give the zeros of ζ. The zeros appear when
S → all places and the trace is compared to the explicit
formula; RH is equivalent to a global version (absorption
spectrum), not to Theorem 4. Theorem 4 is unconditional
(S finite). Our Fmat check is a finite-Λ illustration of
this S-local identity, not a test of RH.

## Principal value

∫' subtracts the singularity at u=1 so that the Fourier
transform vanishes at 1. That is the same regularization
that isolates 2 log' Λ from the local integrals. Mixing
the λ=1 peak of τ_Λ into the mass at λ=2 is exactly
forgetting ∫'.
