# Preregistration: Bochner multiplier of Q̂_L on W_log3

Locked before the run. L = log 3. Four characters
χ₅, χ₈, χ₄, χ₃. Not Galerkin. No N. No assemble.
Not a covering lemma. Not RH.

The sufficient operator bound named in
`operator-bound-WL.md` (Fourier of the cutoff
kernel / Bochner, g(0)=0 kept):

    Q(f) = ∫ ρ(t) m_Q(t) dt,   ρ = |ˆf|² ≥ 0,  ∫ ρ = 2
    α_line = 2 inf_{t ≥ 0} m_Q(t)

Closed series, no 1/y split:

    C_A^lo = log(q/π) + ψ(s₀) + ∑_{k≥0} μ^{-2(s₀+k)}/(s₀+k)
    k(t)   = ∑_{m≥0} ∫_0^L e^{-2(s₀+m) y} (1 − cos(t y)) dy
    m_Q(t) = C_A^lo / 2 + k(t) − w₂ cos(t log 2)
    w₂     = χ(2) log 2 / √2

Canonical witnesses for the sign of inf:
t = 0 (χ₅, χ₈, χ₄) and t = π / log 2 (χ₃).

Necessary family: even windowed cosines
(Fourier on the interval). Integer n matches
the diagonal of `scan_s` at μ=3. Not a matrix.

Bernstein of lag against Â: A(constant) on
χ₅ and χ₃. Young on D₂ stays dead.

**Prediction.** α_line < 0 on all four
(the sufficient bound does not take the class).
Cosine family Q > 0 on all four (no cosine
kills the class). A(constant) < 0 on χ₅ and
χ₃ (C_* = ∞). Class not taken.

**Kill.** α_line ≥ 0 on any of the four,
or any sampled cosine has Q ≤ 0.
