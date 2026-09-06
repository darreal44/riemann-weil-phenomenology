# κ probe (block 2 × F_∞): ladder

Preregistered (`notes/journal-kappa-block2.md`):
κ = m · 2√2 from the linearised block(2) cross on
A_∞. Freeze at 4 → module 1/√2; at 8 → inverse √2.
Kill if Λ=16 cpu=400 still wanders by >0.3 versus
cpu=160. Survive if it sits at 4±0.2 or 8±0.2.
Not RH. Not Thm 4.

## Execution

`python code/kappa_block2.py --ladder`, 5 processes
on 32 cores (threads 1,1,2,18,10 by (Λ cpu)²),
~9 GB, 10.3 s wall. Two Si-blocks, not the full
S−A Fmat of #46 (that was 1383 s at 16/400).
Table: `report/kappa-block2-ladder.json`.

| Λ | cpu | m | κ |
|---|---|---|---|
| 8 | 40 | 1.514 | 4.284 |
| 16 | 80 | 2.008 | 5.680 |
| 16 | 160 | 2.091 | 5.914 |
| **16** | **400** | 2.116 | **5.984** |
| 24 | 200 | 2.567 | 7.260 |

## Verdict: KILL

cpu=160 → 400 at Λ=16: wander 0.070, so the
h-grid has frozen. It froze at κ≈6, not at 4
and not at 8. Survive does not fire.

Λ still moves: 4.28 → 5.98 → 7.26. A line
through three windows is not a limit (same
warning as #44, #45, Young on D2, κ at Λ=4).
Unlike #46, this linearised probe *does*
converge in h at Λ=16; the remaining motion
is in Λ. That is not a shell freeze.

Judge: `tests/test_kappa_block2.py`.

## Status

| Claim | Status |
|---|---|
| sandbox toward 4 at Λ=2..4 | judged (old) |
| Λ=16, cpu 160 vs 400 wander >0.3 | **false** (0.070) |
| κ sits at 4±0.2 or 8±0.2 | **false** (KILL) |
| κ = 4 or 8 picks the shell | open; not this ladder |
| Fmat w₂ = this κ | false (different operator) |
| (∀ L) Q_L ≥ 0 | RH; not this note |
