# Isolate 83 on 37a1

Preregistered (`report/prereg-37a1-drop83.md`,
`term-83.md`): drop-3 at μ=82 vs 84, drop-83
at μ=100. Prime-side Q, NB=80, dps=50. Not
the Gram. Not RH.

## Execution

`python code/gl2_drop83.py`, 9 jobs, 9 workers,
211 s wall. Table: `report/gl2-37a1-drop83.json`.
μ=100 full and drop-3 match the hi json to
every printed digit.

| μ | 83 in? | full λ₀ | drop 3 | drop 83 |
|---|---|---|---|---|
| 80 (control) | no | 8.23×10⁻⁹ | **+0.089** | — |
| **82** | no | 5.42×10⁻⁹ | **+0.087** | = full (mute) |
| **84** | just arrived | 3.58×10⁻⁹ | **+0.048** | +3.29×10⁻⁹ (dispensable) |
| **100** | y/L=0.96 | 2.76×10⁻¹⁰ | **−0.418** | **−0.080** |

## Verdict

**83 is a voter at μ=100** (drop-83 < 0). That
kill did not fire.

**83's arrival does not isolate the join of 3.**
Drop-3 is still +0.048 at μ=84. The sign change
is on (84, 100], where 83 drifts in and 89, 97
arrive. Arrival of 83 already moved the plateau
0.087 → 0.048, a hit of 0.04, not through 0 —
as `term-83.md` said, θ≈0 at y/L=1.

Join-before-83 (drop-3 < 0 at 82) did not fire.
This is a decomposition of the cliff, not RH
and not a sixth slope.

Judge: `tests/test_gl2_37a1_drop83.py`.

## Status

| Claim | Status |
|---|---|
| drop-83 = full at μ=82 | judged (mute) |
| drop-3 still + at μ=82 | judged (+0.087) |
| drop-3 < 0 at μ=84 (arrival) | **false** (+0.048) |
| drop-83 < 0 at μ=100 | judged (−0.080) |
| 83 isolates the join of 3 | **false** (join on (84,100]) |
| 83 is necessary at μ=100 | judged |
| (∀ L) Q_L ≥ 0 | RH; not this note |
