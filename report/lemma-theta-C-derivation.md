# Derivation of C = λ₀ / ψ(0)²

## Definitions

The hat reconstruction on [0, L] is

    ψ(t) = v₀ L^{−1/2} + ∑_{n≥1} vₙ (2/L)^{1/2} cos(2π n t / L),
    ‖v‖₂ = 1,     Q v = λ₀ v.

At the endpoint

    ψ(0) = L^{−1/2} ( v₀ + √2 ∑_{n≥1} vₙ )  =:  ε / √L.

The signed defect

    ε  =  v₀ + √2 ∑_{n≥1} vₙ

is how far v sits from the hyperplane of
functions that vanish at t=0. Then

    C  :=  λ₀ / ψ(0)²  =  L λ₀ / ε².          (*)

Q almost null on mid-window bumps, so the
quadratic form is a remainder bilinear in
the two tails. Evenness gives ψ(L)=ψ(0)
and λ₀ = C ψ(0)².

## Two-mode formula, exact

Restrict to span{e₀, e₁}. Let

        Q₀₁  =  ( α  β )
                ( β  γ )

Near rank-1 (det ≪ (tr/2)²). Then

    λ_min  ≈  det(Q₀₁) / tr(Q₀₁),
    u      ∝  ( γ − λ ,  −β ) normalized.

For ζ at µ=11:

    α=0.0523, β=0.0750, γ=0.1074,
    det=1.19×10⁻⁶, tr=0.160,
    λ_min = 7.44×10⁻⁶,
    u = (0.820, −0.572).

The two-mode defect is only the first two
terms,

    ε₂  =  u₀ + √2 u₁  =  0.820 − 0.809  =  0.011.

Hence

    C₂  =  L λ_min / ε₂²
        =  2.398 × 7.44×10⁻⁶ / (0.011)²
        =  0.162.

That is the measured two-mode C. It is
not 1/(4e). It is the rank-1 gap of Q₀₁
divided by the mismatch between ker Q₀₁
and the line {v₀ + √2 v₁ = 0}.

The line {ε=0} is the Dirichlet condition
ψ(0)=0. ker Q₀₁ is 1.4° off that line
(ε₂ = 0.011 on a unit vector). A 1.4°
miss at the edge, times a 10⁻⁵ eigenvalue,
gives C₂.

## Four-mode and the drop to 1/(4e)

Each extra hat lets v cancel one more
oscillation of ψ at t=0. ε falls faster
than √λ, so C = Lλ/ε² falls.

| space | λ | ε | C = Lλ/ε² |
|---|---|---|---|
| e₀,e₁ | 7.4×10⁻⁶ | 1.1×10⁻² | 0.162 |
| e₀…e₃ | 3.0×10⁻¹² | 8.0×10⁻⁶ | 0.112 |
| full (30 d) | 8.9×10⁻²² | ∼ 2.3×10⁻¹⁰ | 0.087 |

On ζ the four-mode value sits on 1/(4e)=0.092
to a few percent. Reading of the constant,
not a proof:

    1/(4e)  =  (1/2) · (1/2) · e^{−1}.

Two tails (the 1/2 from evenness already
used if one writes λ = 2κ ψ(0)²), a second
1/2 from the L² mass of a linear Dirichlet
ramp on a scale of length 1, and e^{−1}
from the archimedean weight e^{y/2} taken
at the first unit of the window. This
bookkeeping matches the number; it does
not replace (*).

Off ζ the rungs n=2,3 never turn on
(N_eff frozen at 2), ε cannot shrink
past the two-mode size, and C stays at
C₂ ∈ [0.12, 0.16]. That is the χ₃, χ₄, χ₅
table.

## What C is not

- Not Poisson of the bulk Gaussian. The
  spatial tail exp(−a L²/4) would give a
  residual R growing like (−ln λ)/2.
  Measured R is constant, so the edge is
  a wall, and C = e^{−R} is a kernel mass.
- Not a named constant of the explicit
  formula taken at face value. 1/(4e)
  appears after four modes on ζ only.
- Not the (v_arch, v_towers) 2×2. That
  plane has λ ∼ 10⁻³ and C ∼ 5.

The identity that is proved is (*).
Everything else is the size of ε in the
chosen subspace.
