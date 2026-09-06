# Closed form of the angle C(ker) ∠ T

Under the zero-side reading (RH, tail in T
absorbed into the 7–9 % already measured)

    Q = Eval^* Eval,
    H = Eval_low^* Eval_low,
    T = Eval_high^* Eval_high,
    C = Eval_low^* Eval_high.

For e ∈ ker ψ(0) ⊂ ℝ³ and v in the tail,

    eᵀ C v  =  ⟨ Eval_low e , Eval_high v ⟩.

That is the pairing. The cosine against
the bottom mode v_T of T is therefore

    cos θ₀
    = ‖ P_{C(ker)} v_T ‖
    = ‖ Cker⁺ (Cker v_T) ‖
    ≤ ‖ Eval_low |ker ‖ · √λ_min(T)
      / σ₁(C|ker).

Cauchy–Schwarz on the two Eval images.

## Check

| L | µ | ‖E_low|ker‖ | √λ_min(T) | σ₁ | CS | cos θ₀ |
|---|---|---|---|---|---|---|
| χ₅ | 16 | 6.3×10⁻² | 0.49 | 0.082 | 0.37 | **0.033** |
| χ₅ | 38 | 4.0×10⁻² | 2×10⁻⁴ | 0.069 | **0.000** | **0.000** |
| χ₃ | 16 | 9.5×10⁻² | 0.025 | 0.147 | **0.016** | **0.013** |
| χ₈ | 16 | 1.07 | 0.95 | 0.23 | >1 | 0.84 |
| χ₁₃ | 16 | 1.53 | 1.24 | 0.47 | >1 | 0.65 |
| χ₃₁ | 38 | 1.61 | 0.83 | 0.11 | >1 | 0.63 |

On a wide desert the bound is small and
sharp (χ₃-16: 0.016 vs 0.013; χ₅-38:
both 0). On a narrow desert T has no
near-kernel, CS > 1, the angle is O(1).

## What it says

C(ker) ⊥ bottom of T *exactly when*
Eval_high has a near-kernel on the tail
hats. That near-kernel is the same
phenomenon as H|ker ≈ 0 on the first
three hats: a combination of hats that
vanishes on the in-band zeros. The
two almost-kernels couple through
⟨E_low e, E_high v⟩, which is the
product of two small residuals.

The angle is not a new arithmetic
constant. It is

    ⟨ residual of 3 hats , residual of the tail ⟩
    / (size of C|ker).

On a wide desert both residuals are
small; their inner product is smaller
still if they are not aligned. χ₃-16
shows they *are* almost aligned
(CS nearly saturated). χ₅-16 has a
factor 10 of misalignment.

## What a proof still needs

A bound on ‖Eval_high v‖ = √λ_min(T)
for v the bottom of T, *or* a bound
on the residual of the 3-hat ker,
without listing the zeros. That is
H|ker = Arch − Primes again.

The angle does not replace that
estimate. It converts a small
Eval_high residual into
orthogonality of C, so the crude
σ₁² / λ_min(T) can be replaced by

    Corr|ker  ≲  ‖E_low|ker‖²
              =  λ_max(H|ker)

which is the right order on χ₅-16
(0.004 vs Corr 3×10⁻⁶, still 10³
of alignment) and the exact order
of H itself. The Schur is then a
bounded factor times H|ker, and
Lemma 2 reduces to truncated Weil
on three hats.

That last reduction is conditional
on CS being O(1) or better — true
on every window here, and < 1
precisely on the deep ones.
