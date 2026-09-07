# Gershgorin on T_far does not converge

Gershgorin needs ∑_{m≠n} |T_nm| < ∞ for each n, then λ_min ≥ min (T_nn −
row_sum). On T_far the model |Q_nm| is O(1/(2n+k)) plus |w₂| O(1/k).
Both row sums are harmonic and diverge.

A finite section n,m ≤ M has a Gershgorin disk that moves with M (the
partial row at n=32, M=47 was 0.67 and still growing like log M). There
is no limit disk inside (0,∞) from this test.

That is why the lab uses an operator norm (Hilbert π) instead of
Gershgorin on the tail. Deepening N_NEAR is a finite-section move, not a
convergent Gershgorin argument.

Not a campaign to sum |Q| farther.
