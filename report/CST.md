# CST

The constant sitting next
to D₂ in A:

    GL1:  CST = log(q/π) − γ
                − log(1 − e^{−2L})
    GL2 FIX, per panel:
          CST = (1/2)log N − log π − γ
                − log(1 − e^{−2L})

γ = Euler. q = conductor
(GL1), N = conductor (GL2).

## Pieces

- log(q/π) − γ  is the
  value of the completed
  Gamma / Frullani at the
  critical line, after
  the π^{−s/2} and the
  ψ(s₀) constant term
  (−γ). It does not
  depend on L.

- −log(1−e^{−2L}) is the
  integral of the D₂ tail
  beyond y=L: the piece
  F₀ e^{−2y}/(1−e^{−2y})
  from L to ∞. Closed
  (Frullani). Frozen once
  L≳3 (μ≳20): at μ=16
  already −0.109, at μ=50
  −0.112 (`A00-L.md`).

On χ₅ μ=16, F₀/2·CST =
CST ≈ −0.109. A₀₀=−1.38
is almost all the
integral against D₂, not
CST.

## What CST is not

Not a well. Not the
2-adic mass. Changing
the ncut flag
(GL2_NCUT=0,1,2) only
decides how many times
the Frullani tail is
subtracted per Gamma_R.
Wrong ncut shifts A by
O(0.1), visible, not RH.
