# The apparent 1/y at y=0

Weight in A:

    w(y) = 2 e^{-y/2} / (1 − e^{-2y})
         = 1/y + 1/2 + O(y)

Looks non-integrable. It is
not: the other factor
vanishes at 0.

## Cancellation

    θ_v(0) = 2 = 2 e^{0}
    2 e^{-3y/2} − θ_v(y) ∼ c y

    c = −3 − θ_v'(0) ≈ −2.962

so

    w(y) (2e^{-3y/2} − θ_v)
        → c   as y → 0
        ≈ −2.962

The integrand of A is
bounded. Numerically:

    y        w(2EC−θ)
    10^{-6}  −2.9619
    10^{-3}  −2.9586
    10^{-1}  −2.6173

No logarithm.

## What the code does

`scan_s` never evaluates
y=0. Gauss–Legendre on
panels of [0,L], first
panel (0, L/NPANEL).
The leftmost node is
strictly positive
(≈ 0.03 L / NPANEL).
The formula
(F₀ EC − θ) is the
same cancellation,
written per matrix
entry rather than
on v.

CST absorbs the
constant term of the
archimedean expansion
(log and γ). The 1/y
of the raw kernel is
already integrated
into that constant
plus a regular
remainder.

## Gauss on [0,1]

A 3-point rule on [0,1]
has its first node at
½ − √(15)/10 ≈ 0.113.
The integrand there is
smooth and O(1). There
is nothing singular
left to handle; the
1/y was a false alarm
once θ_v(0)=F₀ is used.
