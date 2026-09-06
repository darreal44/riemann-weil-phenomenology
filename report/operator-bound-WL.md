# The operator bound on W_L

W_L ⊂ L²(I), I=[−L/2,L/2],
L=log 3. Q_L is a
bounded quadratic form
on that Hilbert space
(`pw-log3.md`: RH-free
half). So there is a
bounded self-adjoint
operator Q̂_L on L²(I)
with

    Q_L(f) = ⟨Q̂_L f, f⟩.

The class step is

    Q̂_L ≥ 0
    i.e.  spec(Q̂_L) ⊂ [0,∞).

That is an operator
inequality, not a
matrix inequality.

## What Galerkin sees

The hats are an ONB of
W_L. The matrix S_N is
the compression
P_N Q̂_L P_N. Courant:

    λ_min(S_N) ↓ λ_min(Q̂_L)
    from above.

Every computed λ_min
is ≥ the number we
need. None of them
is a proof that the
limit is ≥0.

## What a bound would be

An estimate

    ⟨Q̂_L f, f⟩
        ≥ α ‖f‖₂²
    for all f∈W_L

with α≥0 explicit
(α=0 is enough for
the step; α>0 is
the floor). Equivalent
forms:

- χ(2)=0:
    ⟨Â f,f⟩ ≥ 0
- χ(2)=−1:
    ⟨(Â − w₂ Θ̂_{log 2}) f,f⟩ ≥ 0

Θ̂_y is the lag
operator at y
(integral kernel
coming from th).
Â is the
archimedean
convolution (D₂).

Tools that can
produce α, in
principle:
Fourier on the
interval, Young
on the D₂ kernel,
Bernstein for the
lag at one point
*against Â*
(not against I).
None of those
estimates is in
the repo.

A matrix bound
on S_N is not
this. Adding N
is not this.
