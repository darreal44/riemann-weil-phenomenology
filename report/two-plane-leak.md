# Leak out of the 2-plane when N_eff → 3

N_eff counts how many hats carry v₀.
The 2-plane is span{e₁,e₂} inside the
first three hats. Mass2 = ‖P_{e₁e₂} v₀‖².
out = 1 − mass2.

| window | NB | N_eff | ℓ | mass2 | out | hat n=3 |
|---|---|---|---|---|---|---|
| χ₅ µ=16 | 2 | 1.99 | 13.0 | 1.000 | 0 | — |
| χ₅ µ=16 | 16 | 2.14 | 33.1 | 1.000 | 0 | 0 |
| χ₅ µ=38 | 16 | 2.43 | 57.8 | 0.993 | 0.007 | 0.005 |
| χ₃ µ=16 | 16 | 2.32 | 47.9 | 0.998 | 0.002 | 0.002 |
| χ₃ µ=38 | 16 | 2.66 | 70.6 | 0.976 | 0.024 | 0.018 |
| χ₃ µ=80 | 8 | 2.66 | 51.6 | 0.974 | 0.026 | 0.020 |
| χ₃ µ=80 | 16 | 2.91 | 84.7 | 0.948 | 0.052 | 0.039 |
| χ₃ µ=80 | 24 | **3.00** | 111.1 | **0.937** | **0.063** | 0.048 |

## Two different statements

N_eff = 3 means the *participation
ratio* of v₀ is three hats. It does
not mean v₀ has left {e₁,e₂}.

At the certified wall (χ₃ µ=80,
NB=24) the ground state is still
**94 % in the 2-plane**. The missing
6 % is mostly hat n=3 (4.8 %).
Raising the test space from {e₁,e₂}
to {e₁,e₂, hat-3} would pick that
up; it is a 3×3, not a new theory.

What *does* leave the 2-plane is
the *bottom subspace*: at that
window one has six eigenvalues
with ℓ ≥ 52. Lemma 2 on two
vectors controls λ_min, not the
multiplicity. The 2-plane still
captures the ground state to 6 %.

A correction of the 2×2 bound
by the tail:

    λ_min(Q) ≥ λ_min(H) · (mass2) − ‖Q‖ · (out)

is the wrong shape (‖Q‖ is O(1),
out=0.06 would swamp 10⁻⁶). The
right shape is variational:

    λ_min(Q) ≤ v₀ᵀ Q v₀ = λ_min(Q),

and the Rayleigh quotient of the
normalized projection Π v₀ / ‖Π v₀‖
on the 2-plane sits within a
factor mass2⁻¹ ≈ 1.07 of λ_min
if the tail is Q-orthogonal to
leading order. Empirically
λ_min(H_{3}) / λ_min(Q_{25}) is
e^{13}/e^{111} — incomparable,
because H at 3 hats is a different
operator (fewer primes in the
same formula? no: same primes,
different trial space). Comparing
H at NB=2 with Q at NB=24 is
comparing two Galerkin levels,
not a projection of one matrix.

Inside one matrix (NB=24), χ₃ µ=80:

    R(e₁)     = 1.88×10⁻⁵    ℓ = 10.9
    Ritz 2-plane = 3.53×10⁻⁹    ℓ = 19.5
    λ_min(Q)  = 5.59×10⁻⁴⁹   ℓ = 111.1

Support of v₀ is 94 % on the 2-plane
coordinates. The Rayleigh quotient
of those coordinates padded by zero
is 10⁴⁰ above λ_min. The 6 % tail
is the cancellation, not a remainder.
Dropping it destroys the well.

N_eff = 3 is therefore two facts at
once: four modes are deep, *and*
the ground state cannot be certified
from its visible support. Lemma 2
on three hats is a different
Galerkin problem (Q restricted to
dimension 3), not a projection of
the large one. The 2×2 of
`lemma2-2x2.md` controls that small
problem. It does not control χ₃ µ=80.
