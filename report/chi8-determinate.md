# Determinate vs indeterminate, χ₈

G_reg only (w₂=0, s₀=1/4). 3 / 4 / 5 positive atoms, same greedy grid.

    n  rms_in     max |out_n−out_{n+1}|
    3  3.3×10⁻⁴   4.1×10⁻⁴
    4  2.3×10⁻⁴   2.7×10⁻⁴
    5  1.7×10⁻⁴

The prediction on (L,3L] stabilises. New atoms refine one extension,
they do not produce a second one. That is how a *determinate*
restriction looks numerically.

Not a Carleman proof. Not full G (CST on t=0 still flips m₀). Not
Nevanlinna abcd.

Working guess: G_reg on [−L,L] has at most one PD extension that is a
small atomic measure with t-support in [0,25]. Whether the true
\(\mathcal{M}\) of the full kernel is a singleton stays open; Schur only
said nonempty.
