# Journal — κ probe (block 2 × F_∞)

Locked before the server
run. Not RH. Not Thm 4
until κ freezes at 4 or 8
(`report/block2-coefficient.md`).

    m = ∫_{|λ−2|<0.24} τ_lin(λ) d*λ
    τ_lin from W = ½ (B₂ A_∞ + F_∞ (P B₂ P))
    κ = m · 2√2
    κ → 4  module  (1/√2)
    κ → 8  inverse (√2)

## Here (sandbox)

    python code/kappa_block2.py 2 16
    python code/kappa_block2.py 4 24
    python code/kappa_block2.py 4 40

Smoke (this machine):

    Λ=2  cpu=16   m=0.590  κ=1.67   0.0s
    Λ=4  cpu=24   m=1.059  κ=3.00   0.0s
    Λ=4  cpu=40   m=1.109  κ=3.14   0.0s

Already moving toward 4,
not sitting. Not a freeze.

## Server (consign output)

Threadripper, 64 GB. One
process: Fmat is two
N_out×N_in float64.
Do **not** pass --workers
inside one Fmat (that
duplicates the matrix).
`--ladder` is five single
jobs, one process each.
RAM:

    Λ=8  cpu=40    ~0.02 GB
    Λ=16 cpu=80    ~0.3 GB
    Λ=16 cpu=160   ~1.1 GB
    Λ=16 cpu=400   ~6.6 GB
    Λ=24 cpu=200   ~3.7 GB

    python code/kappa_block2.py --ladder

Five jobs, 32 cores,
~9 GB, 10.3 s wall.

    Λ    cpu      m      κ     |k−4|  |k−8|
    8     40   1.514   4.284   0.284   3.716
   16     80   2.008   5.680   1.680   2.320
   16    160   2.091   5.914   1.914   2.086
   16    400   2.116   5.984   1.984   2.016
   24    200   2.567   7.260   3.260   0.740

Kill if κ at Λ=16 cpu=400
is still wandering by
>0.3 versus cpu=160.
Survive if it sits at
4±0.2 or 8±0.2.

**Executed.** Wander
|5.984−5.914|=0.070 < 0.3
(h-grid frozen at Λ=16).
κ=5.984 is not 4±0.2 and
not 8±0.2. **KILL.**

Λ=8 looked like 4; Λ=24
is 7.26, closer to 8.
That is a line through
windows, not a freeze.
Not Thm 4. Not RH.

## Not on this probe

Full S−A peak (#46) —
already run. drop-3
μ≫80, other v at μ=150,
harvest χ — other
scripts, not κ.
