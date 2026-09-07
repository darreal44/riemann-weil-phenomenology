# The remainder R = D₂ − 1/y

s₀=3/4:

    R(0⁺) = 1 − 2 s₀ = −1/2.
    Measured y=0.001 R=−0.5000 y=L R=−0.477.

R is almost flat. Write D₂ = 1/y − 1/2 + r(y) with r(0)=0 and |r| small
on [0,L] (|r(L)|≈0.023).

Then

    S_k = Si(ω_k L) − ½ ∫_0^L sin(ω_k y) dy + ∫ r sin.

ω_k L = 2π k, ∫ sin(ω y) dy vanishes (cos(2π k)=1). Si(2π k) → π/2. The
visible error is ∫ r sin = O(‖r′‖_1 / ω) = O(1/k) once r is C¹.

S_∞ = π/2 on this splitting (the −½ mode is orthogonal to these sines).
The 0.02 gap in the table (1.55 vs 1.57) is ∫ r sin plus quadrature at
0. It does not move the O(1/(k n)) row sum.

Not RH.
