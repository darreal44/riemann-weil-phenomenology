# Step 3: Connes’ h versus h_Λ

## Two different pairings

ϑ(λ)g(r) = λ^{-1/2} g(r/λ). For g = 1_{[0,Λ]},

    h_Λ(λ) = ⟨g, ϑ(λ) g⟩_{L²(dr)} = Λ λ^{-1/2} min(1, λ).

That is *one* matrix element.

The object of `tau_curve` and of Connes’ compressed trace is

    τ_Λ(λ) = Tr(P̂_Λ P_Λ ϑ(λ)),

the trace on the whole of L²[0,Λ], not the pairing against
the single function 1_{[0,Λ]}. In a cell basis that trace is
the sum of the diagonal of W after the dilation index
(`trace_dist.py`). So h_Λ is not τ_Λ, and ⟨τ₂, h_Λ⟩ is not
Tr(P̂ P ϑ) restricted to place 2.

## What Connes calls h

Theorem 4 of Connes (1999) pairs the local distribution
against a test function h on the module (an idèle class
function, pulled back to R_+* × Q_2*). The integral is

    ∫'_{Q₂*} h(u^{-1}) / |1−u|_2 d*u.

Here h is arbitrary Schwartz-class on the module, not the
indicator of an additive interval. The additive cutoff [0,Λ]
enters as the *projections* P_Λ, P̂_Λ that define τ_Λ, not as
the test function of the local integral.

## The identification that closes step 3

- Test function of Theorem 4: any h on R_+*. The Dirac
  pairing ⟨τ₂, h⟩ = Σ_n w_n h(2^{-n}) with w_{±1} = 1/√2
  (`dstar-identification.md`, `tau2_local.py`).
- Additive indicator 1_{[0,Λ]}: defines τ_Λ(·), not h.
- h_Λ is the matrix element of ϑ on that indicator. It is a
  legitimate *choice* of test function in Theorem 4, and
  then ⟨τ₂, h_Λ⟩ = 2Λ (`tau2-pairing.md`). That number is
  the local integral evaluated on that choice. It is not
  the mass of the peak of τ_S − τ_∞ (which is the pairing
  against an approximate identity in λ, i.e. against h≈1
  near λ=2, mass 1/√2).

## Locked

| object | pairing | value |
|--------|---------|-------|
| mass of the shell λ=2 | ⟨τ₂, 1_{near 2}⟩ | 1/√2 |
| matrix element of the indicator | ⟨τ₂, h_Λ⟩ | 2Λ |

Two tests, two numbers. Neither is the Fmat integral.
Step 3 is the table, not a third convention.
