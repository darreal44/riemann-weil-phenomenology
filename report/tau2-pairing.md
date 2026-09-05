# Pairing ⟨τ₂, h_Λ⟩

Additive test on the slice: g = 1_{[0,Λ]}. Then

    h_Λ(λ) = ⟨g, ϑ(λ) g⟩ = Λ λ^{-1/2} min(1, λ).

This is the same kernel that `tau_curve` samples pointwise (the
λ^{-1/2} min comes from ϑ and the overlap of two intervals).

## Pairing on shells

⟨τ₂, h_Λ⟩ = Σ_n w_n h_Λ(2^{-n}), w_n the twisted Connes masses
(`tau2_local.py`).

- Only the two visible peaks n=±1: each contributes Λ/2 × 2 / 1
  wait: at Λ=4, each peak contributes 2, sum **Λ**.
- All shells n ≠ 0: geometric series  Σ_{m≥1} Λ 2^{-m}  twice
  (positive and negative orders) = **2Λ**.

`python3 code/tau2_pairing.py`: 1.992 Λ at truncation ±8
(limit 2Λ). Linear in the cutoff, as a local trace.

## What this is not

Not the Fmat integral ∫ (τ_S−τ_A) d*λ. That integral tries to
read one Dirac. The pairing already *is* the Dirac sum, evaluated
on h_Λ. No cell size.

n=0 (units, λ=1) is the 2 log' Λ δ_1 term of Theorem 4, excluded
from τ₂. We set w_0 = 0.

## Number to lock

Against the indicator of [0,Λ], the 2-adic place contributes
2Λ if every shell is kept, or Λ if only λ=2^{±1} — the two
peaks the difference τ_S−τ_∞ is allowed to see. Both are exact.
The grid is not asked.
