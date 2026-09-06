# How v hits Q

On the 3-plane, Q(v)
is a Rayleigh
quotient of H.

    Q(v) = λ_min +
           ∑_{k≥2} λ_k ⟨v,u_k⟩²

Near v_min,
Q ≈ λ_min + gap · θ²
(θ = angle to v_min).

μ=16, overlap and Q:

    v          ov     1−ov²      Q
    (5,−4,1)  0.9985  0.0030   0.00139
    (4,−3,1)  0.9944  0.0112   0.00551
    (4,−3,0)  0.9925  0.0150   0.00051
    (1,−1,0)  0.9907  0.0186   0.00942
    (3,−2,1)  0.9806  0.0384   0.01900
    e₀        0.759   0.424    0.092
    e₂        0.108   0.988    0.239

(5,−4,1) is the
closest ray and has
the smallest Q among
the open-hat vectors
with a 3rd component.
(4,−3,0) is closer
to the floor than
its overlap suggests
— it sits nearer the
2-plane kernel of
ψ(0). e₀,e₁,e₂ are
off-pencil: Q jumps
to the diagonal
O(0.1).

μ=150: same order.
v_min itself moved
a little
(0.759,−0.642,0.108)
→ (0.733,−0.665,0.147)
and the rational
ray stayed at
overlap 0.995. So
v controls the
*digit* of Q
(10^{-3} vs 10^{-2})
and does not flip
the sign on this
pencil, at either
μ.

The sign risk is
leaving the pencil
(pure hats still
positive here) or
leaving the 3-plane
(Courant: λ_min of
a larger space can
be smaller — that
is the well, not
these five rays).
