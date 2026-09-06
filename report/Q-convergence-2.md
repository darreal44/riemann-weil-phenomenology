# Q looks settled; A and P are not

Q(v) ∈ [0.003, 0.009] from
μ=16 to 80 (`Q-convergence.md`).
That is a cancellation of
two pieces that have *not*
converged:

    A(16)=−0.83   A(80)=−1.45
    P(16)=−0.83   P(80)=−1.45
    P₂+P₃ → −2.25   (limit of Θ=2I)
    A₀₀ → A₀₀(∞)    (D₂ tail)

So Q = (A − A_lead) −
(P − P_lead) + (A_lead −
P_lead) where the last
parenthesis is still
moving. Apparent
convergence of Q is
faster than convergence
of either side.

Two readings:

1. Q has a limit Q_∞>0
   and we are seeing
   χ(p)-noise around it.
2. Q is a slow residual
   of two series that
   will unbalance when
   P₂+P₃ finish their
   march to −2.25 and A
   finishes its e^{−y/2}
   tail.

μ=80 does not distinguish
them. A proof of
convergence of Q is a
proof that the two
unfinished limits match
to better than 0.003.
