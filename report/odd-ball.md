# Remainder ball for a_odd on [1, L]

Same split as the even
side. G₃ on [0,1] is the
arithmetic check (no
a^{(6)} majorant). 8+8
trapezoid on [1, L] with
sampled max|a''|.

    G₃              −0.010913
    trap[1, 1.59]   +0.061582 ± 0.000098   M=0.366
    trap[1.59, L]   +0.035101 ± 0.000227   M=0.105
    ∫ a_odd         [0.08545, 0.08609]

    python3 code/av_enclose_odd_ball.py

    χ     Qlo     Qhi
    χ₃  0.00574 0.00639
    χ₄  0.01754 0.01819
    χ₇  0.11661 0.11726

χ₃ stays positive. Room
is the same millimetre
as χ₅ on the even side
(0.004–0.006). g_odd''
peaks at −1.55 on [1, L]
(larger than the even
0.71); a'' itself is
milder because w_odd
decays as e^{−3y/2}.

Not RH. Next: Leibniz
endpoint M for a_odd,
as `av_app.py` did for
a_even.
