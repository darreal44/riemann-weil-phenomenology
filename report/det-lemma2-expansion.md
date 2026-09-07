# Explicit det(H) in the Lemma 2 frame — χ₅

e₁ = (√2, −1)/√3, e₂ ⊥ e₁ in
{φ₀,φ₁}. H = A − P, both
restricted to that frame.

    det H = H₁₁ H₂₂ − H₁₂²

No zeros. Finite prime-power
sum n ≤ μ.

## The 2×2

| μ | H₁₁ | H₁₂ | H₂₂ | det | λ_min ≈ det/tr |
|---|---|---|---|---|---|
| 8 | 1.53×10⁻³ | −1.78×10⁻² | 0.427 | 3.37×10⁻⁴ | 7.9×10⁻⁴ |
| 16 | 9.31×10⁻⁵ | −3.50×10⁻³ | 0.285 | 1.43×10⁻⁵ | 5.0×10⁻⁵ |
| 22 | 2.46×10⁻⁴ | −6.01×10⁻³ | 0.285 | 3.40×10⁻⁵ | 1.2×10⁻⁴ |

H₁₁ is the thin axis (A₁₁ ≈ P₁₁
to 10⁻⁴). H₂₂ stays O(1).
det lives in H₁₁ H₂₂ minus a
square of size 10⁻⁵.

## A versus grouped P, μ=16

           11        12        22
    A   −0.98695  −0.91895   0.42441
    P₂  −0.53430  −0.07758  −0.24542   (2,4,8,16)
    P₃  −0.42791  −0.59531   0.69784   (3,9)
    Prest −0.02483 −0.24256  −0.31344   (7,11,13)
    P   −0.98704  −0.91545   0.13899
    H    9.3e-5   −3.50e-3   0.28543

On the (11) slot, 2-powers plus
3-powers already make −0.962
against A = −0.987. The rest
is −0.025 and finishes the
10⁻⁴. On (12), 3-powers carry
most of P; the rest is the
same size as 3; they cancel
A₁₂ to 3×10⁻³.

## Prime table, μ=16

 n   w=χΛn^{-1/2}   θ₁₁    P₁₁      θ₁₂    P₁₂
 2      −0.490      1.318  −0.646    0.707  −0.347
 3      −0.634      0.678  −0.430    1.022  −0.648
 4      +0.347      0.333  +0.116    0.943  +0.327
 7      −0.736      0.035  −0.025    0.365  −0.268
 8      −0.245      0.015  −0.004    0.236  −0.058
 9      +0.366      0.006  +0.002    0.144  +0.053
11      +0.723      0.001  +0.001    0.043  +0.031
13      −0.711      0.000  −0.000    0.008  −0.005

θ₁₁(log n) dies by n=7.
θ₁₂ lives longer. That is
why H₁₁ is easy to see and
H₁₂ needs the last primes
(`H12-convergence.md`).

## What a hand proof must check

    H₁₁ > 0,   H₁₁ H₂₂ > H₁₂².

H₂₂ > 0 is cheap (0.28).
H₁₁ > 0 is A₁₁ − P₁₁ with
A₁₁ a 10-term Laplace sum
and P₁₁ dominated by 2 and 3
(θ₁₁ explicit, `theta_f1.py`).
The dangerous piece is H₁₂²
≈ 1.2×10⁻⁵ against H₁₁ H₂₂
≈ 2.7×10⁻⁵ at μ=16: a factor
two, not a factor ten.

JSON: `report/det-lemma2-chi5.json`.
