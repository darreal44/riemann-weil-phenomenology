<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# Our Maass γ from enclosed Booker Λ_θ

Not a take. Not Weil.

`python code/maass_booker_zeros.py --forms all --T 115` scans Re Λ_θ
on the five Table 1 forms (correct ε: 1.1, 1.2, 1.4, 1.5 odd sine;
1.3 even cosine), then bisects with the n-tail, u-tail, and order-12
trapezoid remainder in the ball.

Sign changes of Re Λ_θ are not all L-zeros. Where |γ_θ| dips to
10^{-19}, Re(γ L) can cross zero while L is O(1). Those lines are
dropped: a midpoint is kept only if |Λ_θ/γ_θ| < 0.05. That is L
small, not a gamma-dip. Booker–Then `zeros_maass{1..5}.txt` are
untouched.

What we have, T=115:

| form | label | ε | L-zeros | certified to 10^{-13} | γ₁ |
|---|---|---|---|---|---|
| maass1 | 1.0.1.1.1 | 1 | 38 | 4 | 17.02494207599258 |
| maass2 | 1.0.1.2.1 | 1 | 45 | 10 | 5.10553130864732 |
| maass3 | 1.0.1.3.1 | 0 | 48 | 16 | 2.89772467827093 |
| maass4 | 1.0.1.4.1 | 1 | 48 | 17 | 3.76470190452597 |
| maass5 | 1.0.1.5.1 | 1 | 48 | 17 | 4.07043016260800 |

γ₁ matches Table 1 to 10^{-13} or better. Higher zeros that
isolated with 0 in a probe ball are still *located* (the bisection
mid) but not last-digit certified: at frozen θ=1 the |γ_θ| envelope
dies with t, so |Λ| at 10^{-13} from the root falls inside the
rounding ball. Booker's θ (cos θ ≲ (4+|t²-R²|)^{-1/2}) keeps |γ_θ|
near 10^{-9} and is the next tightening. Lists:
`code/zeros_maass{1..5}_enclosed.txt`. Not ∀L. Not Weil.

Cite: Booker–Then 2018; LMFDB Collaboration 2026.
