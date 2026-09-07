# Convergence of eigenvalues of H_n

Courant– Fischer for the k-th eigenvalue:

    λ_k(H_n) ≥ λ_k(H_{n+1}) ≥ λ_k(Q̂)

when the spaces are nested and k ≤ n. Each λ_k decreases to some limit ≥
the true λ_k of Q̂ (or to +∞ in the essential spectrum if any).

We only tabulated k=1 (the bottom). The diagonal Q_nn on W_{log 3} was ≳
2 (`Wlog3-spectrum.md`): the bulk stays O(1) while λ_1 sinks with L to
10⁻¹¹. That is a gap opening under the bulk, not the whole spectrum
sliding down.

No rate for λ_k, k≥2. No proof that λ_1(H_n)→c_L^* faster than the 30 %
from n=16 to 48. Interlacing says the sign of λ_1 cannot flip from + to
− by raising n; it can only go down. #74 is that statement numerically.

Essential spectrum of Q̂_L is not identified (PW space is infinite
dimensional; a continuous part is possible). If there is one, Courant
limits for large k need not be discrete eigenvalues.
