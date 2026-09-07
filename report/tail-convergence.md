# Convergence of the tail

Far block in
#61: n ≥ N_NEAR
=32. Bound

    off_far = π/2 + 1/(4 N)
              + r_HS(N)
              + |w₂| ‖Θ‖
    ρ_far = off_far / qmin_far

qmin_far is
min_{n=32..39} Q_nn
(χ₃: 4.19).
As N→∞, Q_nn
grows (more
oscillations
of θ against
D₂, positive
on the
diagonal
once n is
large).
off_far → π/2
+ |w₂| : the
Hilbert
constant does
not go to 0.

So ρ_far
decreases
like 1/qmin
but has a
floor
(π/2+|w₂|)/
sup Q_nn
that we have
not shown
is small.
On the
computed
window
qmin is
still O(1–4),
ρ_far=0.50
(χ₃).

r_HS(N)
~ 1/N. That
piece does
converge to
0. The
Hankel π/2
and the atom
do not.

Raising
N_NEAR
moves modes
from far
into the
exact T
(where
χ₃ is
already
+0.010).
That is
the only
convergence
that helps
S_lo: not
a better
π, a
smaller
far set.
