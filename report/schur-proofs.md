# Schur proofs, written out

Not RH. T>0 is assumed
or measured on the bulk,
not derived for all L.

## 1. Completing the square

Q symmetric, split

    Q = [ H  C ]
        [ Cᵀ T ]

T invertible. Schur
complement of T:

    Δ = H − C T⁻¹ Cᵀ.

Block factorisation

    Q = [ I   C T⁻¹ ] [ Δ  0 ] [ I      0    ]
        [ 0    I    ] [ 0  T ] [ T⁻¹ Cᵀ  I   ]

For x=(u,v),

    ⟨Qx,x⟩
      = ⟨Δ u, u⟩
      + ⟨T (v + T⁻¹ Cᵀ u),
             v + T⁻¹ Cᵀ u⟩.

If T>0 the second term
is ‖T^{1/2}(v+T⁻¹Cᵀu)‖²
≥ 0. Hence

    ⟨Qx,x⟩ ≥ 0  for all x
        ⇔  Δ ≥ 0,

and the same with
strict inequality.
That is the sign
identity.

Proof: expand the
square. No estimate.
No RH.

## 2. Graph Rayleigh

The identity also gives

    λ₀(Q)
      = min_{u≠0}
        ⟨Δu,u⟩ /
        (‖u‖² + ‖T⁻¹ Cᵀ u‖²)
      ≤ λ_min(Δ).

Equality iff a ground
state of Q lives on the
graph v = −T⁻¹ Cᵀ u.
Measured ratio
λ_min(Δ)/λ₀(Q) =
1.000–1.004 on the
lemma-2 windows
(`lemma2-schur-3.md`).
Not an identity for
every split: only when
the well is in the head.

The exact eigenproblem
is nonlinear:

    Δ_λ u = λ u,
    Δ_λ = H − C(T−λI)⁻¹ Cᵀ.

Replacing T−λI by T is
legal once
λ₀ ≪ λ_min(T), the
measured regime
(well vs bulk O(1)).

## 3. What is not proved

    ‖C T⁻¹ Cᵀ‖
        ≤ λ_min(H) − ε.

Δ = H − (PSD). A lower
bound on H is an *upper*
bound on nothing that
helps λ₀. The crude
Frobenius bound
‖C‖_F² / λ_min(T)
was 0.52 against a
v-specific correction
0.004 (`schur-v.md`).
That gap is not closed
by the identity.

## 4. How the repo uses it

Head = first three hats
(or the 2-plane). Tail =
the rest. T is the bulk,
positive by the O(1)
spectrum of Q away from
the well. Then Q>0 on
the whole hat space
*iff* the 3×3 Δ>0.
`code/schur_head.py`
solves T X = Cᵀ rather
than inverting T.

The rational witness
is a vector in the
head. Its Q(v) is not
λ₀(Δ); it is one
Rayleigh number. The
Schur tail correction
on that v was 0.004
against Q_head=0.0055
(`schur-v.md`).
