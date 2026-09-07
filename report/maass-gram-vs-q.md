# Gram vs Q, Maass

11.0.1.1.1 has a_n
(R=2.03) and **no
zeros** in the tree.
Gram cannot run.
Q only:

    μ=8   λ₀=−0.784
    μ=16  λ₀=−0.809

Small R does not
save the prime-side
kernel.

maass1 has both
(zeros 17…115, n=70
and Zenodo a_n).
Same μ:

    μ     Gram           Q
    8    −1.3×10⁻¹⁵     −1.12
   22    −5.6×10⁻¹⁶     −1.49  (server)

Gram is desert
noise around 0
(first γ=17, window
log 22 too short
for a slope). Q is
O(−1) and drifting.
They are not two
readings of one
form. Gram is
empty; Q is the
experimental
kernel, still
INDEF.

To compare for
real: either
harvest γ for
11.0.1.1.1 and
take μ large
enough that Gram
is honestly PSD,
or drop Gram
(desert) and fix
Q from Hejhal.
Do not harvest
30k zeros to
explain a −1.
