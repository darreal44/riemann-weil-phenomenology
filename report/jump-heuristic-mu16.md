# Jump heuristic versus λ₀, μ=16 N=30

    S = ∑_{γ > ω_max} 8 ψ(0)² sin²(γ L/2) / γ²

    χ      λ₀         S          S/λ₀   n_out
    χ₁₃   1.21e-5    1.13e-5     0.93    237
    χ₄    5.48e-16   5.59e-16    1.02    190
    χ₈    1.14e-9    4.32e-9     3.78    218
    χ₅    2.7e-16    4.6e-14      170    199   (float64 floor)
    χ₃    <1e-30     2.7e-13       —     179   (underflow)

On the two windows where
λ₀ is comfortably above
10^{-16}, S matches λ₀
to 7% (χ₁₃) and 2% (χ₄).
χ₈ is a factor 4. χ₅ and
χ₃ are past float64.

remaining §2 quoted
∼1.5 on ζ μ=11. Here the
factor is 0.93–3.8 when
the eigenvalue is
resolved. Still not an
O(1) derived remainder:
S uses the measured ψ(0)
of the same eigenvector,
so it is a consistency
check of the jump shape,
not an a priori bound.
