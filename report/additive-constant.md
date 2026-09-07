# The additive constant

Classical candidate, one Γ_R factor:

    c_Γ = ½ log(q/π) + ½ ψ(s₀)

    ψ(1/4) = −γ − π/2 − 3 log 2
    ψ(3/4) = −γ + π/2 − 3 log 2

Repo CST (`Q_nm`):

    CST = log(q/π) − γ − log(1−e^{−2L})

At L=log 3:

          CST     c_Γ      CST−c_Γ
    χ₃   −0.506   −0.566    +0.060
    χ₄   −0.218   −0.422    +0.204
    χ₅   +0.005   −1.881    +1.887
    χ₈   +0.475   −1.646    +2.122

χ₃ is close (0.06). Even s₀ is not: CST forgot most of ψ(1/4) (the −π/2
−3 log 2 piece) and used −γ in place of ½ψ. Different functional on the
odd and even cells.

The gap 0.728 of #70 is not this table. That was A(φ₀) (CST plus the D₂
integral) versus C_A^{lo} from m_Q. Two constants already disagree
before the integral for s₀=1/4; for χ₃ the constants almost agree and
the 0.728 is in the integral versus the Bochner floor.

So: the additive piece is identified up to 0.06 on χ₃ at this L, and not
identified on χ₅/χ₈. A single formula CST cannot be c_Γ for both
parities.
