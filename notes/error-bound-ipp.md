<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# Error bound, by parts

r(y)=D₂(y)−1/y+½. r(0⁺)=0, r(L)=D₂(L)−1/L+½ is explicit (s₀=3/4, L=log
3: 0.02277).

ω_k=2π k/L. Integrate by parts on (0,L]:

    ∫ r sin(ω y) dy = − r(y) cos(ω y)/ω |_0^L + (1/ω) ∫ r′ cos(ω y) dy =
    − r(L)/ω + (1/ω) ∫ r′ cos.

Hence

    |∫ r sin| ≤ ( |r(L)| + ∫_0^L |r′| ) / ω = C L / (2π k)
    C = |r(L)| + ‖r′‖_1.

r is C^∞ on (0,L] and has a finite limit of all derivatives at 0 (the
Laurent part of D₂ is exactly 1/y, so r extends smoothly). ‖r′‖_1 is
therefore finite. A machine bound on this interval: ‖r′‖_∞≤0.071,
‖r′‖_1≤0.037, C≤0.060, so

    |∫ r sin| ≤ 0.0104 / k.

The measured value is 0.00398 / k = r(L) L/(2π k) (the ∫ r′ term cancels
against the endpoint at this precision). The proved envelope is the
0.0104 one, once ‖r′‖_1≤0.037 is accepted as a finite-check or replaced
by a hand bound from the closed form of D₂′.

This closes the O(1/k) in S_k−π/2 up to that ‖r′‖_1 check. It does not
by itself flip S_lo.

Not RH.
