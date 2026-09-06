# Quorum metrics (GL2 prime-side Q)

One drop per prime p < μ.
Metric on the same
assemble (`gl2_quorum_scan.py`).

    necessary  :  λ₀(drop p) < 0
    optional   :  λ₀(drop p) > 0
    mute       :  a_p = 0  (drop = full)
    edge       :  p ≈ μ, light voter
    depth      :  −λ₀(drop p)   (how
                  hard the prime locks)
    complete   :  every interior
                  voting prime is
                  necessary

## 37a1 μ=62  (prereg drop-3: KILL)

    full λ₀ = 5.26×10^{-7}   ℓ=14.46
    necessary 12 / 18
    optional   6
    worst drop: p=5, λ₀=−0.72

drop 3 stayed *positive*
(+0.093): the
preregistration died.

## 67a1 μ=74  (prereg complete: SURVIVE)

    full λ₀ = 4.92×10^{-8}   ℓ=16.83
    necessary 17 / 21
    optional   4  (41, 71 mute;
                   67, 73 edge)
    worst drop: p=3, λ₀=−1.25
    2, 5, 13: −0.42, −1.02, −0.14
    (deeper than at μ=38)

## What the metrics are not

λ₀(full) is 10^{-7}–10^{-8},
the well of Q, not a
vote count. Completeness
is a pattern on the
*drops*, not a theorem
that every prime is
needed for RH. Depth is
not an exponent
(`quorum-exponents.tex`
is a different object).
Gram ℓ₀ of the zeros is
not this Q.
