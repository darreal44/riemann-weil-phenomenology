# Two-point Gauss on two halves for a_odd

a_odd^{(6)} does not freeze
(`odd-a6.md`). a_odd^{(4)}
does:

    N     max|a^{(4)}| on [0.05,0.95]
    8     23.59
   12     23.46
   16     23.52

Remainder of 2-point
Gauss on an interval of
length L is

    C₂(L) M₄
    C₂(L) = L⁵ · 16 / (5 · 24³)
          = L⁵ · 7.23×10^{-6} / (½)⁵
          wait: C₂(1)=2.315×10^{-4},
          C₂(½)=C₂(1)/32=7.23×10^{-6}.

Two halves [0,½]+[½,1]:

    bound 2 C₂(½) · 23.5 = 3.40×10^{-4}
    nodes 0.106, 0.394, 0.606, 0.894
    composite G = −0.011065
    trap reference −0.010878
    actual error 1.87×10^{-4}

G₃ was −0.010913. Replacing
it by the composite shifts
I by −1.5×10^{-4} and adds
a 3.4×10^{-4} box from a
*frozen* derivative.

    Q₃ termwise [0.00490, 0.00724]
    → [0.00441, 0.00743] > 0

This is the odd substitute
for the even Markov-on-a^{(6)}
bound. Four evaluations of
a_odd, M₄=23.5 stable.
