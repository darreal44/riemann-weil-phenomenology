# Why ℓ can be negative on ker Eval

G = 2 Φ* Φ, Φ the analysis
operator (hats sampled at
the zeros). For a unit
coefficient vector x ∈ ℝ^{N+1},

    xᵀ G x = 2 ∑_γ |η_x(γ)|².

There is no reason for this
to be ≤ 1. The cosine hats
are L²-normalised on [0, L],
not at the zeros. Φ is not
a contraction, so spec(G)
is not in (0,1). Negative
depth ℓ = −ln λ just means
λ>1: sample energy larger
than coefficient energy.

On ker Eval_ω* the function
vanishes at the in-band
zeros below ω*. The samples
that remain are the later
zeros. Those can still
align with η_x and push
xᵀ G x above 1. That is
the anti direction
(χ₅: ℓ=−1.23, λ=3.42;
χ₁₃: ℓ=−1.30, λ=3.67).

It is not a concentrated
Slepian mode (those have
λ_limiter ∈ (0,1)). It is
an artefact of using the
coefficient Euclidean
norm as the unit sphere.
Replacing ‖x‖₂ = 1 by
‖η_x‖_{L²[0,L]} = 1 would
force λ(G) into a
different scale and might
kill the anti block — and
would also rescale the
deep wells. That change
of norm is not done.
The cut ℓ>2 is a cut in
the coefficient metric.
