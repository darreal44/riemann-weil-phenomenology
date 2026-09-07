# The constant in O(1/k)

r = D₂ − 1/y + 1/2, r(0⁺)=0, r(L)≈0.0228.

∫_0^L r(y) sin(ω_k y) dy measured:

    k     integral    k · integral
    8     −0.00050    −0.00398
    16    −0.00025    −0.00398
    32    −0.00012    −0.00398
    48    −0.00008    −0.00398

Equals − r(L) L / (2π) to the digits shown (endpoint IPP, the ∫ r′ cos /
ω term is invisible at this precision). So the O(1/k) constant is r(L)
L/(2π) ≈ 0.004, not 0.02. The 0.02 hole in the S_k table was quadrature
of 1/y near 0, not this integral.

n|S_n−S_m| ≤ n · 0.004 · |1/n−1/m| = 0.004 k / m which at n=32, k=1 is
0.00012, negligible against k S_∞≈1.57.

The constant is named. A proof is IPP on r once r′ is bounded on [0,L]
(r is C^∞ on (0,L] and flat at 0).

Not RH.
