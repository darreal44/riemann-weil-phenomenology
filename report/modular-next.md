# Modular objects not yet in Q

## 1. Weight k ≠ 2 — doable

Δ = Ramanujan Δ, weight 12, level 1, τ(n).
Γ-factor Γ_C(s)^{k/2} wait: Λ(s)=(2π)^{-s} Γ(s) L(Δ,s)
shifted so the critical line is Re=6. Zeros usually listed
as 6+iγ. harvest: PARI `lfunzeros(mfLfun, T)` or
`lfuncreate` of the newform in S_12(SL2(Z)).
Different desert, different Weyl. Not a copy of scan_q_gl2
(s0 panels must follow weight).

## 2. Imprimitive level

Oldforms at level M|N, lifts of lower level. Their L is
the same as the primitive newform up to Euler factors at
p|N. Harvesting them is a duplicate list. Skip.

## 3. Nebentypus χ

S_k(Γ0(N), χ), χ ≠ 1. L(f,s) has an extra Dirichlet twist
in the functional equation (root number, conductor N·q_χ).
Needs a newform with character (e.g. weight 1 dihedral, or
weight 2 with χ). gp `mfinit([N,k,chi])`. New script, new
zeros. Not 11a1.

## 4. Hecke acting on Q / on v0 — not defined

T_p acts on S_k: (T_p f)(z) = … . v0 lives in a cosine
basis of a Weil window, not in S_k. There is no diagram

    T_p : PW_{L/2} → PW_{L/2}

that commutes with the Gram or with Q. Inserting a_p as
a multiplier on coefficients of v0 is not T_p.
The a_n already sit in Q as Weil prime weights. That is
the only Hecke input this operator sees.

## Order

If we add one object: Δ zeros + Gram, to see whether
N_eff≈2 survives weight 12. Not T_p·v0.
