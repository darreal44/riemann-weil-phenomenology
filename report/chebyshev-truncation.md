# Truncation error of the Chebyshev series of a

On [0,1], |T_n|≤1, so the
uniform tail is

    ‖a − s_n‖_∞ ≤ ∑_{k>n} |c_k|.

    n     tail of a          ρ-bound (crude)
    4     3.10×10^{-4}       3.7×10^{-5}
    8     2.19×10^{-7}       1.4×10^{-9}
   12     4.75×10^{-11}
   16     8×10^{-15}         (float floor)

s₈ already copies a to
2×10^{-7}. The crude
Bernstein majorant
underestimates because
A fitted from c₄ is
loose; the measured tail
is the number to use.

## Truncation of a^{(6)}

Differentiating s_n:

    n     ‖a₆[s_n]‖    ‖a₆ − a₆[s_n]‖
    8     426          279
   12     324.5        5.41
   14     324.5        0.52
   16     324.5        0.17

M=324.5 is a truncation
error of 0.17 at N=16
(relative 5×10^{-4}).
The G₃ remainder moves
by c₆·0.17 ≈ 8×10^{-8}
— invisible next to
1.61×10^{-4}.

## G₃ of the partial sums

Gauss is exact on
polynomials of degree
≤5. So G₃(a)−G₃(s_n)
is the Gauss image of
the tail.

    n     G₃(s_n)         G₃(a)−G₃(s_n)
    4     −0.70080374     1.42×10^{-4}
    8     −0.70066134     1.4×10^{-9}
   12     −0.70066134     7×10^{-12}

The whole 1.61×10^{-4}
remainder of the 3-point
rule *is* the degree-≥6
tail of a: ∑_{k≥6}|c_k|
= 1.91×10^{-4}, same
order as c₆ M.

s₄ (degree 4) already
gives G₃ to 1.4×10^{-4};
s₈ is exact for every
digit we print. The
truncation that matters
for the certificate is
not N=24 versus N=16,
it is “a minus its
degree-5 projection”.
