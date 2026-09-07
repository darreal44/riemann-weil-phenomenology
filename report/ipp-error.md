# Error after one IPP

Exact:

    ∫ r sin = − r(L)/ω + ω^{−1} ∫ r′ cos.

The first term is −0.00398 / k. The second is the IPP error. Its
absolute bound ‖r′‖_1 / ω ≈ 0.0064 / k produces the proved 0.0104 / k.
Measured, the second term is invisible at 10^{−5} on k=8…48 (phase
cancellation in ∫ r′ cos).

So the IPP *error* is much smaller than its *majorant*. Using 0.0104 is
legal and loose. Using 0.00398 as an identity needs ∫ r′ cos = 0 which
is false in general but tiny here.

A second IPP on ∫ r′ cos gives r′(L) cos / ω² + … = O(1/k²) if one wants
a sharper proved constant. Not needed for nΔS at N_NEAR=32.

Not RH.
