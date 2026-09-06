# Coefficient majorant of |a^{(6)}|

    a(y) = ∑ c_n T_n(2y−1)
    a^{(6)}(y) = 2^6 ∑ c_n T_n^{(6)}(2y−1)

    |T_n^{(k)}| ≤ T_n^{(k)}(1)
    T_n^{(k)}(1) = n²(n²−1)…(n²−(k−1)²) / (1·3·…·(2k−1))

Checked: T₆'(1)=36, T₆''(1)=420.

## Termwise sum, n≤16

    n     |c_n| T_n^{(6)}(1) · 64
    6     270
    7      79
    8     616
    9     122
   10     213
   12      28
   16     0.08

    ∑ = 1370

versus the Chebyshev
max 324.5 (factor 4.2:
the terms do not share
a sign).

## Remainder

    |G₃ − ∫ a| ≤ c₆ · 1370
               = 6.80×10^{-4}

still inside the ±0.003
A-window (room left
2.3×10^{-3}). This bound
uses only the verified
c_n (`chebyshev-coeffs.md`)
and T_n^{(6)}(1). It does
not evaluate a^{(6)}
anywhere.

The working ceiling 325
is tighter; 1370 is the
one that is a sum of
table entries.
