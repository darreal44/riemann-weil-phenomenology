# Journal — κ probe (block 2 × F_∞)

Locked before the server
run. Not RH. Not Thm 4
until κ freezes at 2 or 4
(`report/block2-coefficient.md`).

    m = ∫_{|λ−2|<0.24} τ_lin(λ) d*λ
    τ_lin from W = ½ (B₂ A_∞ + F_∞ (P B₂ P))
    κ = m · 2√2
    κ → 2  module  (1/√2)
    κ → 4  inverse (√2)

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

    Λ    cpu      m      κ
    8     40   1.514   4.284
   16     80   2.008   5.680
   16    160   2.091   5.914
   16    400   2.116   5.984
   24    200   2.567   7.260

h-grid at Λ=16: |5.984−5.914|=0.070
< 0.3, frozen in h. Corrected
targets (module κ=2, inverse κ=4):
5.984 is neither. Old 4/8
targets: neither. **KILL.**

Λ=8 looked like 4; Λ=24 is 7.26.
A line through Λ, not a freeze.
Not Thm 4. Not RH.

## Not on this probe

Full S−A peak (#46) —
already run. drop-3
μ≫80, other v at μ=150,
harvest χ — other
scripts, not κ.
