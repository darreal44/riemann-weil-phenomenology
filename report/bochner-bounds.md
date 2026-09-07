# Bochner bounds on W_{log 3}

    m_Q(t) = C_A^{lo}/2 + k(t) − w₂ cos(t log 2)
    α_line = 2 inf_{t≥0} m_Q(t)

k(t)=∑_m ∫_0^L e^{-2(s₀+m)y}(1−cos(ty)) dy
≥ 0, =0 at t=0.
w₂ = χ(2) log 2 / √2.

If inf is at t=0
(χ₅, χ₈, χ₄):

    α_line = C_A^{lo}
    C_A^{lo} = log(q/π)+ψ(s₀)
               + ∑ μ^{-2(s₀+k)}/(s₀+k)

That sum is ~10^{-117}
at μ=3. So α_line is
just log(q/π)+ψ(s₀),
negative because
ψ(1/4)≈−8.22,
ψ(3/4)≈−1.96.

χ₃: χ(2)=−1, w₂<0,
−w₂ cos can go
negative away from
0. inf at t=3.7,
α_line=−0.205 >
C_A^{lo}=−0.862
(the cosine of 2
*helps* at t=0 and
hurts at t=π/log 2).

Why the bound is
loose: Bochner
allows every even
L² density ρ=|ˆf|²,
not only those with
supp ˆf in the
PW band of W_L
(or g(0)=0 beyond
the global θ(0)=2).
The negative dip
of m_Q is used by
a ρ that W_L
cannot carry.
Hence α_line < 0
< Q_cos, and the
sandwich does not
close
(`W-log3-convergence.md`).

Tails of the ψ
series are
numerically zero.
The bound is not
waiting on more
k in the sum.
