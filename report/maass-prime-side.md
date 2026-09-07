# Prime-side Q for Maass — code path

`code/scan_q_maass.py`

    python code/scan_q_maass.py maass1 6 12 25

## What it does

- Reads Zenodo `maass_an_*.json` (R, N, a_n).
- Archimedean panels: s0 = 1/4 ± i R/2
  (arguments of Γ((s ± iR)/2) at s = 1/2),
  summed as a conjugate pair, real part kept.
- Satake αβ = 1, not p. Recurrence
  a_{p^k} = a_p a_{p^{k-1}} − a_{p^{k-2}}.
- Weil weight Λ_f(n) / √n  (critical line 1/2).

## What it is not

A calibrated match to the zero Gram.
Smoke at μ=6, N=9, dps=20, maass1 (R=9.53):

    lam0 = −0.87    N_eff = 2.41

The Gram at a nearby window is isolated
and positive (`test_maass_q`, μ=6 N=13
on maass2). So this kernel is the right
*shape* and the wrong *scale* or the
wrong Frullani/CST. Do not harvest a
depth from it.

Building the path was the remaining
code item. Matching Gram is a separate
calibration (CST, ncut, Λ_f/n vs /√n),
the same class of work that produced
GL2_FIX for weight 2.
