# The trace formula, in this repository

Three writings of one identity.
They do not prove RH. They name
the two sides of the same pairing.

## 1. Guinand–Weil (spectral = geometric)

Admissible even h:

    ∑_ρ ĥ(ρ)
        = ĥ(0)+ĥ(1)
          − ∑_n Λ(n) n^{-1/2} h(log n)
          − Arch_Γ(h).

Left: spectrum of ζ (or L(χ)).
Right: identity orbit + primes +
archimedean place. Unconditional.
This *is* the explicit formula.
Weil’s criterion is the sign of
the left-hand side
(`weil-criterion-proof.md`).

Q_L is the same pairing on
supp h ⊂ [−L,L]:

    Q_L(f) = CST + Arch(f) − P_≤µ(f)
           = ∑_ρ ĥ_f(ρ).

Hats are a basis of that test
class. The 2×2 H = A−P is two
vectors in it.

## 2. Connes 1999, Theorem 4 (S-local)

S a finite set of places, A_S the
S-adèles, U(h) = ∫ h(λ) ϑ(λ) d*λ
the integrated dilation, R_Λ the
cutoff |x|≤Λ. As Λ→∞,

    Tr(R_Λ U(h))
        = 2 h(1) log' Λ
          + ∑_{v∈S} ∫'_{k_v^*} h(u^{-1})/|1−u|_v d*u
          + o(1).

Geometric side only: identity
orbit plus one local integral per
place in S. No zeros. Finite S is
unconditional (`connes-theorem-4.md`).

Our semi-local code
(`trace_formula.py`, `Fmat`,
`tau2_local.py`) is this identity
at S={∞,2}. The slope 4 h(1) in
log Λ is 2 log' Λ after the
λ^{1/2} twist and two real
embeddings of the module. Place 2
is the pairing ⟨τ₂,h⟩ against
shells λ=2^{±n}.

Zeros enter only when S exhausts
every place and the trace is
identified with ∑_ρ. That global
limit is Connes’ absorption-spectrum
form of RH. It is not Theorem 4
and it is not in the Fmat check.

## 3. What is being traced

| writing | operator | test | geometric | spectral |
|---|---|---|---|---|
| Guinand–Weil | none (distribution) | h on ℝ | primes + Γ | zeros |
| Q_L | Gram of hats | f on [0,L] | n≤e^L + Arch | same zeros |
| Connes Thm 4 | R_Λ U(h) | h on C_S | places in S | — (S finite) |
| Connes global | same, S→all | same | all places | zeros |

The “trace” in Connes is an
operator trace on L² of the
adèles with a cutoff. The
“trace” in Weil is a sum over
zeros equal to a sum over primes.
They agree after S is complete
and the cutoff is removed, up
to the regularisation ∫' that
isolates log' Λ from u=1.

d*λ = dλ/λ on the slice is the
push-forward of d*u
(`dstar-identification.md`).
Mixing Lebesgue dλ with d*λ
manufactures the extra log 2
that is not a second local term.

## 4. What a proof would need

- Weil positivity of the spectral
  side for all h: RH.
- The global Connes trace equal
  to ∑_ρ with an absorption gap:
  RH in another language.
- Q_L ≥ 0 for all L: RH on
  compactly supported tests,
  again RH.

S-local traces, 2-adic masses,
and det(A−P) at one µ are
geometric-side computations.
They check the identity, they
do not bound the spectrum.

## 5. Practical dictionary

    h(log n)           ↔  θ_{hats}(log n)
    Λ(n) n^{-1/2}      ↔  weight w of P
    Arch_Γ             ↔  K(y)=2 e^{-2s₀ y}/(1-e^{-2y})
    2 h(1) log' Λ      ↔  n=0 / λ=1 term (w₀=0 in τ₂)
    ∫'_{ℝ^*}           ↔  τ_∞, CC (39)
    ∫'_{ℚ₂^*}          ↔  τ₂, shells 2^{±n}

The code paths `scan_s.assemble`,
`H_2plane_independent`,
`trace_formula.trace` evaluate
these three lines. They are not
three theorems.
