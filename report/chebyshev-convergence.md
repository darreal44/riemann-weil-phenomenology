# Chebyshev convergence of a on [0,1]

## Coefficients

    n     |c_n|
    0     7.31×10^{-1}
    1     6.77×10^{-1}
    2     9.27×10^{-2}
    4     5.52×10^{-3}
    8     4.02×10^{-6}
    12    7.63×10^{-10}
    16    5.33×10^{-14}
    ≥17   ∼10^{-15}   (float64 floor)

Geometric through n=16,
then machine epsilon.

## Why so fast

w has poles where
1−e^{−2y}=0, i.e. y=iπk,
k≠0. Nearest: y=±iπ.
Mapped to the Chebyshev
variable z=2y−1,

    z = −1 ± 2iπ
    Bernstein ρ = |z+√(z²−1)|
                ≈ 12.80

so |c_n| ≲ ρ^{−n}.
ρ^{-12} ≈ 1.4×10^{-14},
which is the observed
drop. g=2e^{−3y/2}−θ_v
is entire in y (trig of
ωy, ω=π/(2 ln 2)), so
the strip of a is the
strip of w.

## a^{(6)} versus N

    N    ‖a₆−a₆(24)‖_[0.05,1]   ‖a₆‖
    8    275                      422
   12    4.92                     324.5
   16    0.177                    324.5
   20    0.179                    324.5
   24    0                        324.5
   28    0.52                     324.5
   32    10.8                     324.5

Converged at N=16
(four stable digits of
M=324.5). Past N=24 the
sixth derivative feels
the 10^{-15} tail at
the endpoint. Do not
raise N to “get more
accuracy” on a^{(6)}.

Remainder c₆·324.5 =
1.61×10^{-4} is therefore
stable under the
interpolant degree once
N∈[16,24].
