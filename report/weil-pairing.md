# Weil’s pairing

Two sides, one even test θ supported in [−L,L].

Prime side (now Q_pk when every n with log n < L is kept):

    ∑_{n>1} Λ(n) χ(n) n^{-1/2} θ(log n)

That is the lag expansion. #69 filled p^k. This side is identified.

Archimedean side — the pairing. Classically it is the additive
contribution of the Γ-factor of Λ(s,χ) (or of ξ). In delay coordinates
it is a kernel W_∞(y) against θ(y):

    A(θ) = c_χ θ(0) + ∫_0^L W_∞(y) θ(y) dy

W_∞ comes from (Γ'/Γ)(s₀ + it) by Fourier in t, or from the Mellin
transform of the completed factor. For the trivial character one has the
standard combination of Γ_R(s)=π^{-s/2}Γ(s/2) and its logarithmic
derivative. For χ the shift is s₀ ∈ {0,1}/2 plus the conductor in the
π^{-s} power (log q).

What this repo uses instead (`Q_nm`):

    A = ½ F0 · CST + ½ ∫ D₂(y) (F0 E_C(y) − θ(y)) dy

CST = log(q/π) − γ − log(1−e^{−2L}) is a constant tuned to a window, not
Γ'/Γ term by term. D₂(y) = 2 e^{−2 s₀ y} / (1−e^{−2y}) is a model of
W_∞, not a proof that W_∞ = D₂.

#70: on φ₀, χ₃, L=log 3, this A gives −0.134; C_A^{lo} (the Bochner
constant from m_Q) gives −0.862. Gap 0.728. On the 4-plane at μ=5,
replacing the diagonal by 2 m_Q flips the sign of λ_min. So the pairing
in use and the symbol m_Q are not the same functional on the same θ.

To identify: write W_∞ from Γ'/Γ (s₀ + it) for one χ, one n=0, L=log 3,
and compare the number to Q_nm arch-only. That is the pairing, not a
harvest.
