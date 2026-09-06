# Where the ground state of Q actually lives

χ₅, eigenvector of Q at λ₀
(mpmath, not float64).

| μ | λ₀ | ‖head‖² | ‖tail‖² | peak |
|---|---|---|---|---|
| 8 | 9.6×10⁻⁷ | 1.000 | ∼5×10⁻⁵ | φ₀ = 0.80 |
| 11 | 1.7×10⁻⁹ | 1.000 | ∼2×10⁻⁴ | φ₀ = 0.75 |
| 16 | 1.2×10⁻¹³ | 1.000 | ∼2×10⁻⁵ | φ₀ = 0.71 |
| 22 | 1.2×10⁻¹⁷ | 1.000 | ∼4×10⁻⁴ | φ₁ = 0.70 |

Weights |v|:

    μ=8   [0.80 0.60 0.04 | 0.007 …]
    μ=11  [0.75 0.65 0.10 | 0.013 …]
    μ=16  [0.71 0.68 0.18 | 0.003 …]
    μ=22  [0.68 0.70 0.24 | 0.018 …]

The well stays in span{φ₀,φ₁}
plus a growing φ₂. It does
*not* leak into T. N_eff =
1.87 → 2.24 is this same
count.

## Correction

The collapsing mode w of T
(report/T-collapse-vs-C.md)
is a tail excitation, not
the ground state of Q. At
μ=22, σ_min(T) = 5×10⁻⁴
and λ₀ = 10⁻¹⁷: two
different small numbers.
w ⊥ v_Q because v_Q has
no tail.

Schur still writes
λ₀ = λ_min(H₃ − C T⁻¹ Cᵀ)
with the gs in the head.
T⁻¹ acts on the *tiny*
tail coordinates of a
variational extension,
not on a mass that moved
into T.
