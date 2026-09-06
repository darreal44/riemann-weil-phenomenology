# Convergence of H₁₂

H = A − P on χ₅. Two readings
of the off-diagonal:

- raw: H_{01} in the hat basis
- frame: e₁ᵀ H e₂, e₁ = (√2,−1)/√3
  (Lemma 2), e₂ its partner in
  {φ₀,φ₁}.

A₁₂ is a single quadrature,
stable. All the motion is P.

## Running cutoff n ≤ n_max

μ=8, primes 2,3,4,7,8

| n_max | H₀₁ raw | H₁₂ frame | ΔP₀₁ |
|---|---|---|---|
| A only | — | −0.880 | — |
| 2 | 0.149 | −0.418 | +0.191 |
| 3 | 0.200 | +0.142 | −0.051 |
| 4 | 0.065 | −0.021 | +0.135 |
| 7 | 0.195 | −0.018 | −0.130 |
| 8 | 0.195 | −0.018 | 0 |

μ=16, last primes 11,13

| n_max | H₀₁ raw | H₁₂ frame | ΔP₀₁ |
|---|---|---|---|
| 2 | 0.138 | −0.572 | +0.221 |
| 7 | 0.281 | +0.017 | −0.316 |
| 11 | −0.012 | −0.009 | +0.244 |
| 13 | 0.133 | −0.0035 | −0.145 |

μ=22, last 17,19

    frame: −0.631 → … → −0.006
    last ΔP₀₁ still ±0.09 to 0.15

## What converges

The *frame* matrix element.
After n=7 it sits at 10⁻²,
after n=13 at 3×10⁻³. That
is the cancellation A ≈ P
in the {f₁,f₂} pairing.
A₁₂ itself does not need a
limit: the Laplace tail is
O(e^{-2L}).

## What does not converge
like a series

The raw increments ΔP₀₁.
They stay O(10⁻¹) up to
n = μ because
θ_{01}(log n) has not gone
to zero (y = log n reaches
L only at the last term)
and n^{-1/2} at n=19 is
still 0.23. This is a
finite sum, not a tail
one can drop.

Dropping n ≥ 5 flips the
sign of the frame H₁₂ at
μ=16 (0.076 → later −0.003).
The remainder is the whole
cancellation.

## Reading

H₁₂^frame converges as a
function of the cutoff
once the last two primes
are in. It does not
converge as a series of
prime terms of decreasing
size. A hand bound must
keep every n ≤ μ, or
group them (2-adic tower,
then 3, then the rest
against θ ≤ θ(0)).
