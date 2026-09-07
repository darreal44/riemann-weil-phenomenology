# 3-point Gauss of A(v) on [0, 1]

Origin (`report/A-v-01.md`, `report/singular-integral.md`) named the
remaining hand piece of the rational witness: a 3-point Gauss–Legendre
rule of the explicit integrand on [0,1]. Linear comparisons miss by
fifty times the ±0.003 window. This note records the shipped check.

v = (4, −3, 1)/√26, χ₅, μ=16. Not a covering lemma, not RH.

## θ_v is elementary

    θ_v(y) = ∑_{n,m=0}^{2} v_n v_m θ_{nm}(y)

with the six lag kernels of `H_2plane_independent.th` (1, cos(2π y/L),
cos(4π y/L), and the two sines). Judge: `test_closed_theta_v_matches_theta_vec`.
θ_v(0)=2, θ_v'(0)= (−24 + 16√2)/(13 L) ≈ −0.03808.

## The 1/y is cancelled

    w(y) = 2 e^{−y/2}/(1−e^{−2y}) ∼ 1/y
    2 e^{−3y/2} − θ_v(y) ∼ (−3 − θ_v'(0)) y

so w(2e^{−3y/2}−θ_v) → −3 − θ_v'(0) ≈ −2.9619 at y=0
(`kernel_limit_0`, `test_kernel_limit_is_minus_three_minus_theta_prime`).
The A-integrand a(y) = ½ of that is bounded; a(0)≈−1.481.

## Gauss

Nodes ½ ± √(3/5)/2, ½; weights 5/18, 8/18, 5/18. First node ≈ 0.1127.

    gauss3(a) = −0.700661

against mpmath quadrature of the *same* shipped a (not a hardcoded
−0.70065 as oracle). Origin’s I_{[0,1]}≈−0.70065 is this number.

Remainder of 3-point Gauss on [0,1] is
coeff × a^{(6)}(ξ) with coeff = (3!)^4 / (7 (6!)^3) ≈ 4.96×10^{-7}.
A 6th-difference estimate of max|a^{(6)}| on 241 samples is ~326,
giving remainder ~1.6×10^{-4}, *inside* ±0.003. That estimate is
not a majorant of |a^{(6)}|. The Gauss value is the finite arithmetic
check; Q(v)>0 is not closed as a hand proof by this remainder.

## Status

| piece | status |
|---|---|
| θ_v closed, six elementary functions | identity (`av_gauss.theta_v`) |
| integrand regular at 0 | identity (`kernel_limit_0`) |
| 3-point Gauss of a on [0,1] | arithmetic check, agrees with ∫ a |
| rigorous |a^{(6)}| majorant | Cauchy, two panels (`notes/av-cauchy-a6.md`) |
| comparison bound of I_{[0,1]} | still open (chord misses by 0.22) |
| (∀ L) Q_L ≥ 0 | RH; not this note |
