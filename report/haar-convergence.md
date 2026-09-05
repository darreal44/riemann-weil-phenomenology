# Convergence of the Haar filter

H_ε φ(α) = (1/(2ε)) ∫_{α e^{-ε}}^{α e^{ε}} φ(λ) d*λ.

## Against τ₂ (limit distribution)

τ₂ = (1/√2) (δ_{λ=2} + δ_{λ=1/2}) + other shells at 2^{±n}.
The log-gap between shells is log 2.

- ε < log 2: H_ε τ₂(2) = 1/√2 exactly. No sequence, no rate.
- ε > log 2: the window eats n=−2 or n=0 and the value jumps.

There is nothing to converge here. The filter either sees one
atom or several.

## Against τ_Λ (finite cutoff)

Theorem 4: τ_Λ → 2 log'Λ δ_1 + τ_∞ + τ₂ as pairings, Λ→∞.
The right order is

    lim_{ε→0} lim_{Λ→∞} H_ε (τ_Λ − τ_∞ − 2 log'Λ δ_1)(2) = 1/√2.

Fmat did the opposite: Λ=16 fixed, ε ~ h → 0. Then H_ε sees
the Gibbs blob of width Λ^{-2}, whose Haar integral grows like
the height of the ringing, not like a Dirac mass. That is why
w2(h) climbs (0.14 → 1.08) instead of sitting at 0.707.

A rate, if one wanted one, would be |H_ε(τ_Λ−τ₂)(2)| ≲
(width of peak)/ε + tail of o(1) in Theorem 4. At Λ=16 the
peak width is ~0.004 and the o(1) is not small. No useful rate
without larger Λ *before* smaller ε.

## Status

Haar converges in the Theorem-4 order of limits. It does not
converge in the Fmat order. The numeric lock failed because
that order was reversed. No new run.
