# Connes pairing, unpacked

Theorem 4 (local at 2):

    ⟨τ₂, h⟩ = ∫'_{ℚ₂×} h(u⁻¹) / |1−u|_2  d*u

The prime is a
principal value:
drop a neighbourhood
of u=1 (where
|1−u|_2=0). Units
n=0 are not a
Dirac at 2^{±1}.

Haar: ∫_{ℤ₂*} d*u = 1,
each shell 2ⁿ ℤ₂*
has measure 1.
n=ord₂(u), |u|_2=2⁻ⁿ.

On a shell the
integrand is
constant in the
unit part (for h
radial in |·|_2),
so the integral
collapses to a
sum:

    ⟨τ₂, h⟩ = ∑_{n≠0} h(2ⁿ) · raw(n)

with raw(n) =
1/|1−u|_2 on that
shell: 2^{n} for
n<0, 1 for n>0
(n=−1 → 1/2).

h is the test
function on the
idèle class, pulled
to |u|. Our
h_Λ(λ)=Λ λ⁻¹/² min(1,λ)
is one choice
(`tau2_pairing.py`).
That pairing is
extensive ~2Λ.
The *mass at λ=2*
is the n=−1 (or
n=+1 inverse) term
alone, after one
√λ twist if one
matches ϑ(λ).

Fmat is not this
sum: it is
Tr(P̂ P ϑ(λ)) on a
real slice, then
∫ d*λ in a window.
Different pairing,
different number
(#46, #48).

The details that
matter: the prime
at u=1, the
argument u⁻¹, the
normalization of
d*u, and whether
λ tracks |u| or
|u⁻¹|. Those four
choose 1/√2 vs √2.
They are written.
They are not Fmat.
