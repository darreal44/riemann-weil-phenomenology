# Chebyshev coefficients of a, checked two ways

N=24 extrema of T_N on
[0,1]. Two constructions:

1. `numpy` `Chebyshev.fit`
2. DCT-I
   c_j = (2/N) ∑'' a(y_k) T_j(2y_k−1)
   (endpoints weight 1/2;
   c_0 and c_N halved)

    n      c_n (fit = DCT to 10^{-15})
    0     −0.7313236
    1     +0.6771683
    2     −0.09266299
    3     −0.01497934
    4     +0.005517581
    5     +1.188×10^{-4}
    6     −1.830×10^{-4}
    8     +4.018×10^{-6}
   12     +7.632×10^{-10}
   16     +5.7×10^{-14}

max |fit − DCT-I| = 1.3×10^{-15}.

## Reconstruction

At the three Gauss nodes,
s_{24} copies a to 10^{-15}:

    y        a              s_fit − a
    0.1127   −1.28620585    2×10^{-15}
    0.5000   −0.63295593    4×10^{-16}
    0.8873   −0.22344549    1×10^{-15}

Interpolation residual on
the 25 extrema: 6×10^{-15}.
The table in
`chebyshev-convergence.md`
was |c_n|; signs alternate
in pairs, as a decreasing
negative function requires.
