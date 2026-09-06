# Θ_v of prime-side Q (zeta, µ=11, dim 9)

Gram ground state is the desert artefact (λ₀<0, Θ changes sign).
Prime-side Q is the right vector: λ₀ = 8.9×10⁻²².

Θ_v(y) = ∑_{n,m} v_n v_m θ_{nm}(y) stays **positive** on (0,L).

| y | Θ | −ln Θ | y e^y | (−ln Θ)/(y e^y) |
|---|-----|-------|-------|-----------------|
| 0.47 | 8.0×10⁻¹ | 0.23 | 0.74 | 0.31 |
| 0.94 | 4.0×10⁻² | 3.23 | 2.41 | 1.34 |
| 1.42 | 1.3×10⁻⁴ | 8.93 | 5.83 | 1.53 |
| 1.73 | 3.1×10⁻⁷ | 14.98 | 9.78 | 1.53 |
| 2.05 | 3.1×10⁻¹¹ | 24.21 | 15.88 | 1.53 |

The ratio locks at **1.53** from y≳1.4.
Shape y e^y, not a Gaussian (that would lock on y²).

Claude's 0.20 s ≈ 2.34 (s≈11.7) is the same
shape at larger N; here N=9 underestimates C.
The lemma is: Θ_v is the autocorrelation of the
Slepian of the desert, whose log is between
y² and y e^y.

`python3 code/theta_v_qpr.py`  (~1 s)
