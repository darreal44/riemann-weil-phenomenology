# The 1/y weight

w(y) ∼ 1/y as y→0⁺ for both parities (1−e^{−2y}∼2y). a=½ w g with g(y)=c
y + O(y²) so a(0⁺) is finite. Differentiating six times, Leibniz
produces terms w^{(k)} g^{(6−k)}. w^{(k)} ∼ (−1)^k k! y^{−1−k}, and
g^{(6−k)} is bounded near 0 only for small k. The product stays bounded
on (0,1] because g vanishes to order 1, but the constants grow like
factorials. That is why a Chebyshev fit of a can look innocent while
a^{(6)} at the nodes nearest 0 or 1 explodes with N (odd case).

At y=1 there is no 1/y. Odd Runge at y=1 is the usual endpoint
amplification of T_N^{(6)}, not the Bose pole.

Not a new regularisation. The mesh of g already avoids differentiating w
six times.
