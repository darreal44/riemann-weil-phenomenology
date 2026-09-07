# The third hat on χ₅ μ=16

Hats {φ₀, φ₁, φ₂}, same
archimedean integral as
`det_lemma2.py`, n≤16 in P.

            A                    P                    H=A−P
    [[−1.383  0.359  0.177]  [[−1.475  0.226  0.030]  [[ 0.092  0.133  0.147]
     [ 0.359  0.820  0.165]   [ 0.226  0.627 −0.049]   [ 0.133  0.194  0.214]
     [ 0.177  0.165  1.405]]  [ 0.030 −0.049  1.166]]  [ 0.147  0.214  0.239]]

    spec(A) = {−1.448,  0.817,  1.474}
    spec(P) = {−1.499,  0.647,  1.170}
    spec(H) = { 0.000,  0.002,  0.522}

A stays indefinite; the
negative mode is 99% φ₀
(−0.987, 0.152, 0.053).
H on the 3-plane is
positive semidefinite.
λ_min(H) ~ 0 is the head
of Q (the well, at this
truncation).

## What φ₂ does

    H₂₂ = 0.239
    H₀₂ = 0.147    H₁₂ = 0.214
    ‖row₂‖ = 0.353

The 2×2 of {φ₀, φ₁} already
has det H = 1.4×10^{-5}>0
and λ_min = 1.0×10^{-4}.
Adding φ₂ does not create
positivity — it was there
in the raw 2-plane — it
rotates the ground state
and adds a bulk eigenvalue
0.52.

Ground vector of H:
    (−0.759,  0.642, −0.108)
Rational v:
    ( 0.784, −0.588,  0.196)
Overlap 0.993 after a
global sign. φ₂ is a
20% correction, not the
carrier of the sign.

The lemma-2 frame {e₁, e₂}
was a rotation *inside*
span{φ₀, φ₁} that made
det H negative. The raw
coordinate 2-plane is
already H≻0 at 10^{-4}.
The third hat is why v
is not in that 2-plane;
it is not why Q(v)>0.
