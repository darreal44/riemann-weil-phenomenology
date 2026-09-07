# Coefficient bound on a_odd^{(4)}

Same identity as the even
a^{(6)} bound:

    |a^{(4)}| ≤ 2⁴ ∑ |c_n| T_n^{(4)}(1)

    N     Markov M₄     last |c_n|
    8     55.9          1.1×10^{-6}
   12     59.7          7×10^{-9}
   16     71.1          6×10^{-9}

Stable near 60 (sampled
interior max 23.5, factor
2.5). Composite remainder
2 C₂(½) M₄:

    M₄=23.5   rem=3.40×10^{-4}   Q₃≥0.00441
    M₄=60     rem=8.68×10^{-4}   Q₃≥0.00388

still positive. M₄=60 is
the table-sum analogue of
even M₆=1370. The script
`av_odd_gauss2.py` keeps
23.5 as the working
ceiling; 60 is the one
that only uses c_n and
T_n^{(4)}(1).
