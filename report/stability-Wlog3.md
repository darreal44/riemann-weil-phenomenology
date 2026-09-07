# Numerical stability on W_{log 3}

Different machine from `numerical-stability.md` (χ₂₉ hats). Here: Q_nm
by Gauss, 2×2 to 24×24 H, T sections ~30, S_lo ~10⁻².

Q_nm is a smooth integrand after G_reg (analytic strip width π). float64
Gauss (16 panels) is not the error that decides a sign at 10⁻².

S_lo(χ₃) at h=4 is +0.007. A 10⁻⁴ relative error on H would still leave
the sign. The take is not a last bit.

Atomic fits of G_reg (χ₈): lstsq on 60 points, 4–5 columns, κ of the
cosine Vandermonde on [0,L] with t≤20 is moderate (well- separated t).
rms 10⁻⁴ is the model error, not rounding.

What is unstable on purpose: folding C_A^{lo} onto one atom (m₀ crosses
0 by 0.04). That is algebra, not float64.

κ(Q) blow-up at large μ is another window (`numerical-stability.md`).
Not this L.
