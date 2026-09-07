# μ* of 37a1 drop-3 on (84, 100]

Preregistered (`report/prereg-37a1-mu-star.md`,
`critical-thresholds.md`): 2-unit grid
86…98. Prime-side Q, NB=80, dps=50. Not
the Gram. Not RH.

Drop-3 is +0.048 at 84 and −0.418 at 100.
The digit of the zero was not sampled.

## Execution

`python code/gl2_drop3_star.py`, 14 jobs,
215 s wall. `report/gl2-37a1-mu-star.json`.

| μ | 89 in? | 97 in? | drop 3 |
|---|---|---|---|
| 84 | no | no | **+0.048** |
| **86** | no | no | **−0.029** |
| 88 | no | no | −0.099 |
| 90 | yes | no | −0.162 |
| 92 | yes | no | −0.220 |
| 94 | yes | no | −0.274 |
| 96 | yes | no | −0.325 |
| 98 | yes | yes | −0.372 |
| 100 | yes | yes | −0.418 |

Full form stays PSD (ℓ 19.8→21.7).

## Verdict: μ* ∈ (84, 86]

The sign change is in the first two
units after 83 arrives. 89 and 97 are
not in the window yet. Prediction of a
late digit (after 86) is dead. Arrival
at 84 is still +, so the threshold is
still not y/L=1; it is the first drift
of 83. After 86 the remainder goes down
smoothly — no jump at 89 or 97. Not a
sixth slope. Not RH.

Judge: `tests/test_gl2_37a1_mu_star.py`.

## Status

| Claim | Status |
|---|---|
| μ* ∈ (84, 100] | judged, refined to (84, 86] |
| drop-3 < 0 at 86 | judged (−0.029) |
| 89 or 97 needed for the flip | **false** |
| late crossing after 86 | **false** |
| (∀ L) Q_L ≥ 0 | RH; not this note |
