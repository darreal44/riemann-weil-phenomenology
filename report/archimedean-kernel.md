# The archimedean kernel

W_∞(y) is the even kernel on (0,∞) whose cosine transform is (up to
normalisation) Re (Γ'/Γ) (s₀ + it) plus the π-power of the conductor.

A standard shape, for Γ_R and s₀=1/4 or 3/4, is a linear combination of

    e^{-2 s₀ y} / (1 − e^{−2y})
    and its y-derivatives or a 1/y piece peeled off as in G_reg.

That is why D₂(y) = 2 e^{−2 s₀ y} / (1 − e^{−2y}) was chosen: it is the
generating function of the poles of Γ at s₀, s₀+1, … (the denominator
1−e^{−2y} packs the arithmetic progression of poles).

It is the right *family*, not automatically the right coefficient and
not the right additive constant.

G_reg = D₂ − 1/y removes the universal singularity at 0. CST then tries
to put back θ(0) times a number that should equal the constant term of
Γ'/Γ + log(q/π).

#70 says that constant (and/or the diagonal matrix elements of D₂
against φ_n) does not match 2 m_Q(ω_n) nor C_A^{lo}. So either D₂ is
missing a second kernel (the other Γ-factor, or a derivative), or the
normalisation of θ (θ(0)=2 on hats) is not the one m_Q uses.

The kernel question is therefore not “is there a function W_∞” but “is
W_∞ equal to this D₂ plus this CST in the same normalisation as θ_hat”.
One χ, n=0, L=log 3 settles the constant. The shape in y needs several n
or a plot of A(θ_y) against y.
