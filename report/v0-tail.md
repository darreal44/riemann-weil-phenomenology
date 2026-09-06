# Where the missing nats live

Split the Rayleigh quotient of the
true v₀ at a cut k:

    λ = v_Hᵀ Q_{HH} v_H + 2 v_Hᵀ Q_{HT} v_T + v_Tᵀ Q_{TT} v_T
      = H + C + T.

## The identity

χ₅ µ=16, N=17, k=5, λ=4.17×10⁻¹⁵

    H =  9.15471×10⁻⁷
    T =  9.15471×10⁻⁷
    C = −1.83094×10⁻⁶ = −2 H
    H + C + T = λ

χ₃ µ=80, N=25, k=5, λ=5.59×10⁻⁴⁹

    H =  9.69573×10⁻⁵
    T =  9.69573×10⁻⁵
    C = −1.93915×10⁻⁴ = −2 H

χ₃ µ=80, k=8

    H = T = 1.903×10⁻⁸
    C = −2 H

At every cut that was tried,
H = T and C = −2H to the working
precision. The well is

    λ = (√H − √T)²

with √H = √T at all visible digits.
Eighty nats are the residual of
that identity, not a piece of T
that one could drop.

## Decay of the profile

log₁₀ |v_n|

    χ₅ µ=16:   −0.15 −0.17 −0.73 −2.46 −2.49 −3.21 −3.24 −4.85 …
    χ₃ µ=80:   −0.27 −0.17 −0.35 −0.66 −1.15 −1.97 −2.71 −2.96 −4.06 …

After the first three hats, about
half a decimal per hat on the deep
window. The tail that matches H
to 10⁻⁵ is |v| ~ 10⁻² to 10⁻³
(hats 5–8), invisible at three
decimals of L² mass and enough
to cancel a 10⁻⁴ quadratic form
down to 10⁻⁴⁹.

## What a bound must control

Not ‖v_T‖ (small) and not Q_{TT}
(O(1)). The combination

    √(v_Hᵀ Q_{HH} v_H) − √(v_Tᵀ Q_{TT} v_T)

and the phase that makes C exactly
−2√(HT). That is a discrete
prolate statement: the Slepian
vector of a well of this width
has a head and a tail with the
same Dirichlet energy, opposite
phase. Lemma 2 on three hats
never sees the second well.

Data: `report/v0-tail.json` (float
profile; splits above in mpmath).
