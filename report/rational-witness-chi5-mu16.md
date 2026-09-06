# Rational witness at χ₅ μ=16

    v = (4/5, −3/5, 1/5) / √(26/25)
      = (4, −3, 1) / √26

Overlap with measured v₀: 0.993.
Three hats, no machine
eigenvector.

## Identity

    Q(v) = A(v) − Σ_{n≤16} χ(n) Λ(n) n^{-1/2} θ_v(log n)

θ_v = ∑_{n,m=0}^{2} v_n v_m θ_{nm},
θ_{nm} elementary
(`theta_f1.py` and the
usual table).

## The nine terms

 n   t=log n / L     w          θ_v        w θ_v
 2   1/4          −0.49013    1.12176    −0.54981
 3   log3/(2 log2) −0.63428    0.55686    −0.35321
 4   1/2          +0.34657    0.30769    +0.10664
 7   log7 / log16 −0.73548    0.05470    −0.04023
 8   3/4          −0.24506    0.03209    −0.00786
 9   log3 / log4  +0.36620    0.02078    +0.00761
11   log11/log16  +0.72299    0.01197    +0.00866
13   log13/log16  −0.71139    0.00731    −0.00520
16   1            +0.17329    0          0

Powers of two have rational
t. The other four t are
log p / (4 log 2).

    P_head(2,3,4) = −0.79637
    P_rest(7…16)  = −0.03703
    P(v)          = −0.83340
    A(v)          = −0.82789
    Q(v)          = +0.00551 > 0

## What is still machine

A(v): 10-term Laplace
quadrature, dps=30. Not a
closed form. The value is
stable under DEG=4…16
(`legendre.md`).

The six rest θ_v: elementary
sines at known t. They can
be bounded by hand once
log 7, log 11, log 13 sit
in intervals of width 10⁻³
(any standard log table).
A 10⁻³ error on each θ_v
moves P_rest by
∑|w|·10⁻³ ≈ 0.003, still
less than Q(v)=0.0055.

## Interval sketch for the rest

If each of the five nonzero
rest θ_v is known to ±0.001,

    P_rest ∈ −0.03703 ± 0.0030
           = [−0.0400, −0.0340]

Then

    Q(v) = A(v) − P_head − P_rest
         ∈ A(v) + 0.79637 + [0.0340, 0.0400]

Needs A(v) ∈ [−0.8303, −0.8244]
to keep Q>0 throughout.
The computed A(v)=−0.82789
sits in the middle, with
room ±0.003. A Laplace
tail O(e^{-2L})=1/256≈0.004
is the same size: one must
keep ten terms or estimate
the tail, not drop it.

## Verdict

The rational vector is a
numerical certificate
(Q=5.5×10⁻³, no eigensolver).
It is not yet a hand
certificate: A(v) and four
logs remain analytic
inputs. They are the
whole remaining list.
