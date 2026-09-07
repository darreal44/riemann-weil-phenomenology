# Spectrum of A on the lemma-2 2-plane (χ₅ μ=16)

A is the archimedean
Gram in the frame
{e₁, e₂} ⊂ span{φ₀, φ₁}
(`code/det_lemma2.py`).

    A = [[ −1.141  −0.701 ]
         [ −0.701   0.117 ]]

    spec(A) = { −1.454,  +0.430 }
    det A   = −0.625
    tr A    = −1.024

Indefinite. The negative
direction is
(−0.913, −0.408) — mostly
e₁, the combination that
already looks like v₀.

P on the same frame:

    spec(P) = { −1.499,  +0.650 }
    cos(A,P)_F = 0.979

A and P are the same
indefinite form to 2°.
H=A−P is the residual

    spec(H) = { −0.312,  +0.136 }
    det H   = −0.042

so this 2-plane does not
certify positivity
(`det-hand-chi5-mu16.md`).
The cancellation that
makes Q(v)>0 for the
rational witness lives
in the *third* hat and
in the pairing of A
against P at the primes,
not in spec(A) alone.

A without P is not a
positive form. Its
negative eigenvalue
−1.45 is an O(1)
archimedean mass, not a
well.
