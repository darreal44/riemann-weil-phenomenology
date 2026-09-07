# E_C

    E_C(y,s₀) = exp(−2(1−s₀) y)

    s₀=1/4:  e^{−(3/2) y} s₀=3/4:  e^{−(1/2) y}

Identity:

    D₂(y,s₀) E_C(y,s₀) = 2 e^{−2y} / (1−e^{−2y}) = 2 / (e^{2y} − 1)

independent of s₀.

On the diagonal the integrand is

    D₂ (F0 E_C − θ) = F0 · 2/(e^{2y}−1) − D₂ θ

The s₀- dependence on that half sits only in D₂ θ, not in the E_C piece.
E_C is not a cutoff and not 1/y. It is the factor that turns D₂ into the
Bose kernel 2/(e^{2y}−1), the s₀-blind half of the pole family.

G_reg = D₂−1/y is a different regularisation (additive in y). E_C is
multiplicative in the integrand. Both are in A; they do not replace each
other.

Whether Weil’s W_∞ splits this way is exactly the identification still
open. The algebra of E_C inside Q_nm is this identity, nothing more.
