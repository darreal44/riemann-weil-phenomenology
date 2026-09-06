# The Schur lemma used here

Not the representation-theory
statement (irreducible ⇒ intertwiners
are scalars). The linear-algebra
one: block elimination.

## Identity

Let Q be symmetric, split as

        [ H   C ]
    Q = [ Cᵀ  T ]

with T invertible. The Schur
complement of T is

    Δ = H − C T⁻¹ Cᵀ.

Block factorization

    Q = [ I    C T⁻¹ ] [ Δ   0 ]
        [ 0      I   ] [ 0   T ]
                       [ I    0 ]
                       [ T⁻¹ Cᵀ  I ]

gives, for the quadratic form,

    ⟨Qx,x⟩ = ⟨Δ u, u⟩ + ⟨T (v + T⁻¹ Cᵀ u), …⟩

where x = (u,v). The second term is
≥ λ_min(T) ‖…‖². If T>0 then

    min_{x≠0} ⟨Qx,x⟩ / ‖x‖²
        = min_{u≠0} ⟨Δ u,u⟩ / (‖u‖² + ‖T⁻¹ Cᵀ u‖²)
        ≤ λ_min(Δ).

If the ground state of Q is
supported on the head (v ≈ −T⁻¹ Cᵀ u),
the denominator correction is
already included in the variational
characterisation and one has the
exact identity used in the repo:

    λ₀(Q) = λ_min(Δ)

when that minimizer lives in the
graph of −T⁻¹ Cᵀ. Numerically it
holds to 0–0.4 % on the eight
windows of `lemma2-schur-3.md`
(χ₅ µ=16: ratio 1.000; χ₅ µ=38:
1.004 even at κ(T)∼10⁸).

`code/schur_head.py` evaluates Δ
by solving T X = Cᵀ, not by
inverting T.

## What the identity says

The smallest eigenvalue of the
whole hat matrix is the smallest
eigenvalue of a 3×3 built from
the first three hats, after the
tail has been eliminated. The
other Schur (eliminate the head,
keep T) is 200–50 000 times
larger: λ₀ does not live in the
tail.

On the model windows (N_eff≤2.2)
the 3-hat head is essentially
ker ψ(0), i.e. the 2-plane of
raised cosines plus a small third
coordinate. Then Lemma 2 is

    λ₀(Q) = λ_min( H_{2×2} − (Schur tail) ).

H_{2×2} = A−P is the explicit
finite formula. The tail is the
correction C T⁻¹ Cᵀ.

## What it does not say

A lower bound on H does not give
a lower bound on Δ. One still
needs

    ‖ C T⁻¹ Cᵀ ‖  ≤  λ_min(H) − ε.

That is an upper bound on ‖T⁻¹‖
(a gap of T) and a bound on C.
Neither is proved. Measured:

- H on the 2-plane is 10⁻⁴ to
  10⁻⁶; λ₀ is 10⁻⁸ to 10⁻⁴⁹.
  The factor *is* the Schur term.
- On χ₁₃ µ=16, λ_min(H)/λ₀ > 10
  (`test_two_plane_does_not_transfer_to_lambda0`).
  Positivity of the 2-plane does
  not transfer to λ₀.
- At χ₃ µ=80, N_eff=3, overlap
  of v₀ with the 2-plane ~0.83.
  The identity with nhead=3 still
  holds as linear algebra; the
  *model* “2-plane plus small
  tail” does not.

## Why T can be ill-conditioned
and the ratio still 1

κ(T)∼10⁸ on χ₅ µ=38 means T has
small eigenvalues of its own.
Those directions are almost
orthogonal to the range of Cᵀ
that the ground state uses, so
T⁻¹ Cᵀ stays moderate and Δ
tracks λ₀. Conditioning of T is
not the missing bound; the
missing bound is a uniform
control of C T⁻¹ Cᵀ on the
particular 2-plane.

## One-line dictionary

    Schur (groups)     intertwiners of an irrep
    Schur (here)       Δ = H − C T⁻¹ Cᵀ
    identity           λ₀(Q) = λ_min(Δ)  (measured)
    missing lemma      ‖C T⁻¹ Cᵀ‖ < λ_min(H)
    not RH             one window, finite hats

Exact sign reduction \(Q>0\Leftrightarrow\Delta>0\) (given \(T>0\)),
Courant \(\lambda_{\min}(H)\ge\lambda_0\), and the graph Rayleigh
\(\lambda_0\le\lambda_{\min}(\Delta)\): `notes/demonstrations.md`.
The missing bound on \(\|CT^{-1}C^T\|\) is unchanged.
