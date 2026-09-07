# Odd characters at μ=16: a different integrand

a=1 ⇒ s₀=3/4. Weight and
EC change:

    w  = 2 e^{-3y/2}/(1−e^{-2y})
    2 EC = 2 e^{-y/2}
    a  = ½ w (2 EC − θ_v)

Same θ_v, same v. The
integral of a is *not*
the χ₅ ball.

    ∫ a_odd ~ +0.08577
    (G₃ + 8+8, no |a''| bound)
    ∫ a_even  = −0.71956

    python3 code/av_enclose_odd.py

    χ      q     Q~
    χ₃     3   0.0061     (Rayleigh 0.0059)
    χ₄     4   0.0179     (Rayleigh 0.0177)
    χ₇     7   0.1169
    χ₈⁻    8   0.2486
    χ₁₁   11   0.7758
    χ₁₅   15   0.4656
    χ₁₉   19   1.9397
    χ₂₃   23   0.6473
    χ₂₄ᵒ  24   1.3766
    χ₃₁   31   1.3312

Point estimates, all
positive. χ₃ is the tight
odd window, analogous to
χ₅ on the even side.
Closing a remainder for
a_odd is the same job
already done for a_even
(Leibniz + extrema of
the new g_odd=2e^{-y/2}−θ_v).
