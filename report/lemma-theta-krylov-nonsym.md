# Non-symmetric Krylov on (and off) Q

Q is SPD. The non-symmetric toolkit
(GMRES, BiCGSTAB, Arnoldi) is for a
different matrix. Checked by solving
Ax = b with a known x, then again
after adding 5 % skew.

## Ax = b, µ=16 NB=8

| L | A | method | its | relres | ‖x−x★‖ |
|---|---|---|---|---|---|
| χ₅ | Q | CG | 14 | 10⁻¹³ | **0.15** |
| χ₅ | Q | GMRES | 8 | 10⁻¹³ | **0.15** |
| χ₅ | Q | BiCGSTAB | 22 | 10⁻¹³ | **0.15** |
| χ₅ | Q+skew | CG | 40 | 2 | 73 |
| χ₅ | Q+skew | GMRES | 9 | 10⁻¹⁶ | 10⁻¹⁵ |
| χ₅ | Q+skew | BiCGSTAB | 12 | 10⁻¹³ | 10⁻¹¹ |
| χ₁₃ | Q | CG | 10 | 10⁻¹³ | 10⁻¹² |
| χ₁₃ | Q+skew | CG | 40 | 0.09 | 9 |
| χ₁₃ | Q+skew | GMRES | 9 | 10⁻¹⁵ | 10⁻¹⁵ |

On Q, residual ≠ error for χ₅: λ₀ ~
10⁻¹², the component of x along v₀ is
invisible to Ax−b. Every Krylov method
"converges" and still misses that
coordinate. That is the needle, not
the solver.

On Q+skew, CG has no variational
minimum and blows. GMRES (complete
Krylov at dim 9) and BiCGSTAB recover
x. They earn their keep the moment
symmetry dies.

## What to use where

- λ₀ of Q: inverse iteration / Lanczos
  shift-invert, σ=0. Not GMRES.
- Qx = b with Q SPD: CG, knowing the
  v₀-component is lost at κ₂ ~ 10¹².
- T_p on modular symbols, or any
  companion / transfer matrix: GMRES
  or BiCGSTAB, no Lanczos.
- Q⁻¹ treated as a black box that
  float64 has already unsymmetrized:
  Lanczos on the formal inverse still
  forces T=Tᵀ; GMRES on the same
  action also works and costs m².

The lemma does not need a
non-symmetric Krylov method. The
Hecke action on a window that is not
a newform eigenspace does.
