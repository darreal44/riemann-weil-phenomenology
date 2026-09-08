<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->

# Power iteration on joint Off = H − w₂ Θ

Finite block `[N, N+M)` of the *joint* kernel, not the triangle
`π/2 + |w₂|`. H_nm = 1/(2(n+m)) off-diagonal, Θ = theta_hat(·,·,log 2, L)
at L = log 3. No R (HS, small). Power iteration matches eigvalsh.

This is a lower bound on the **finite-section** norm. It is not
s₁(ℓ²) and not Off_far. Hartman's ess = π/2 lives at infinity:
a block underestimates ‖Off‖_ess.

    python code/ql_off_power.py --N 32 --M 256

## Results (L = log 3)

    N   M    χ₃=χ₅ |λ|    χ₈ |λ|    ess χ₃    triangle χ₃
   32  64    0.573         0.266      1.081      2.110
   32 128    0.654         0.382      1.081      2.110
   32 256    0.746         0.503      1.081      2.110
   32 512    0.840         0.620      1.081      2.110
   64 256    0.650         0.382      1.081      2.094

χ₃ and χ₅ share |w₂| = 0.490 so the block is identical.
χ₈ has w₂ = 0: only H, growing toward π/2 more slowly.

## Reading

The joint Rayleigh grows with M toward the ess lower bound
(~1.08), **not** toward the triangle 2.11. The |w₂|‖Θ‖ term
in the triangle is largely cancelled by H on this block
(same sign structure). That is the fat in Off_far = 2.11.

It does **not** license s₁ ≤ 0.84 or S_lo > 0: the missing
tail M→∞ can still add ~0.24 to reach 1.08, and R / cutoff
sit on top. Not W_log3. Not RH.

`step_is_taken()` unchanged.
