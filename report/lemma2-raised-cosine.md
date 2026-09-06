# ker ψ(0) is a raised cosine that vanishes at the ends

Hats on [0, L], L = log μ:

    φ₀(y) = L^{-1/2}
    φₙ(y) = √(2/L) cos(ωₙ y),   ωₙ = 2π n / L.

The edge functional is the point value:

    ψ(0) = f(0) = L^{-1/2} ( v₀ + √2 Σ_{n≥1} vₙ ).

So ker ψ(0) ∩ span{φ₀,φ₁,φ₂} is the
2-plane of combinations that vanish
at y = 0 and y = L.

## The first basis vector

    e₁ ∝ (√2, −1, 0)

    f₁(y) = √(2/L) ( 1 − cos(2π y / L) )
          = √(8/L) sin²(π y / L).

f₁(0) = f₁(L) = 0, peak at mid-window.
‖(√2,−1,0)‖ = √3, so the unit-norm
window function is f₁/√3.

## The second

    e₂ ∝ (√2, 0, −1) minus its e₁ part
      = (√2/3, 2/3, −1)   (before norm)

    f₂(y) ∝ φ₀ − (1/√2) φ₂   + a φ₁ term
          = a combination of
            1, cos(2π y/L), cos(4π y/L)
            that also vanishes at 0, L.

## What H|ker is

    λ_min(H|ker)
    = min { Q(f,f) : f ∈ span{f₁,f₂}, ‖f‖_{L²[0,L]} = 1 }.

Q is the prime-side Weil form
(Arch minus the p^k ≤ μ sum). No
zeros enter. Lemma 2, after the
angle reduction, is a lower bound
for this minimum.

The test function is elementary:
a raised cosine supported on one
window, two frequencies, Dirichlet
condition at the ends. The sum
has ⌊μ⌋ / log μ terms.

## Why Arch ≈ Primes here

f vanishes at 0. The archimedean
pairing of a function that is
zero at the identity is already
small (the diagonal of Arch on
ker is O(1) but cancelled against
the off-diagonal). The primes
see the same vanishing: θ(f,f)(log p)
is the evaluation of this bump at
y = log p. For p near 1 there are
no primes; the first masses are
2 and 3, sitting where sin²(π log p / L)
is not small.

On χ₅, μ=16, L≈2.77:
    f₁(log 2)/‖f₁‖ ~ O(1),
    f₁(log 3) ~ O(1),
and those two terms already make
90 % of Primes|ker. The remaining
digits of the cancellation are
the rest of the short Euler
product against a two-mode bump.

## What to prove

    min_{a,b} Q(a f₁ + b f₂)
    ≥ exp(−C τ γ₁)     or a worse
                       explicit rate.

Unconditional: Q is Weil, f is
given. The zeros are not in the
statement. A lower bound can be
bad (10⁻² instead of 10⁻⁶) and
still be the first written
estimate of Lemma 2. The Schur
factor is then CS × that number,
already reduced.

This is the 3-hat theorem, in
coordinates: positivity of Weil
on the raised-cosine subspace
of PW that vanishes at 0 and L.
