# Li tail quadrature

λ1 zeros = 0.02064. Need +0.00246 to hit 0.02310.

| T2 | tail | zeros+tail |
|----|------|------------|
| 800 | 0.00259 | 0.02323 |
| 1500 | 0.00354 | 0.02419 |
| 5000 | 0.00443 | 0.02507 |
| 10000 | 0.00465 | 0.02529 |

nq=20 already stable to 10^{-6}. The integral
in t converges (∼∫ log t / t²); T2 is not
the issue. Weyl ρ without oscillations is
too large, same overshoot as G-tail.
Scale 0.55 is ∫_T^∞ (ρ_true−ρ_Weyl) plus
the 2-convention.

Do not push T2. Fit once on λ1, keep s.
