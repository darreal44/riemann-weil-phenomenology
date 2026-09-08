<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->

# Three Off tries (2026-09-08)

## (1) Joint ess cap < 1.72

Failed as a proof. The tail n ≥ N+M still has
‖H‖_ess = π/2, so any « block + triangle(tail) » bound
reinjects ~2.08 (naive split gave 3.60). Nehari does not
apply (joint is not Hankel; Hankel remainder ‖R‖₂ ≈ 0.50).
Encadrement stays 1.081 ≤ ess ≤ 2.110.

## (2) Larger block Rayleigh

Vectorised assemble of H − w₂ Θ, χ₃, L = log 3, N = 32:

    M     |λ|     Δ to 1.081    C=Δ√M
    256   0.746   0.335         5.36
    512   0.840   0.240         5.44
   1024   0.930   0.150         4.81

C fell at M=1024: the 5.5 « constant » was not settled.
Still a section, still below ess. Not s₁(ℓ²).

## (3) S_lo elsewhere

Already in report/head3-chi3.md (same majorant, only HEAD
moves). At L = log 3, N_NEAR=32:

    HEAD=2  S_lo = −0.008
    HEAD=3  S_lo = +0.004
    HEAD=4  S_lo = +0.007   (χ₅ +0.040, χ₈ +0.241, χ₄ +0.067)

Sign flip is the 2-plane leaving T, not Off_far.
step_is_taken() stays False: one L, finite H. Not W_L.
Not (∀ L). Not RH.

code/ql_off_power.py (M=256 path) + this note.
