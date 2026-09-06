# 37a1 at μ=62, the last recalcitrant (p=3)

Preregistered (journal §116, `notes/gl2-prime-side.tex`): 37a1 at
μ=62, removal of 3 → negative. The heaviest tower
(|Λ_f(3)|/3 = log 3, a_3 = −3) was the last dispensable prime
at μ=38 (λ₀ after drop = +0.37). Extrapolation: it yields at
ℓ≈13–15, μ≈50–62.

Executed on the prime-side form `scan_q_gl2.assemble`
(GL2_FIX=1, NB=80, dps=50, a_n from `an_points`). Not the zero
Gram. Not RH.

## Execution

One wall-clock assemble, 19 processes, 216 s on 32 cores
(`code/gl2_quorum_scan.py`, `report/gl2-37a1-mu62-quorum.json`).

| form | λ₀ | voter |
|---|---|---|
| full | 5.258×10⁻⁷ | — |
| drop 2 | −0.633 | necessary |
| drop **3** | **+0.0929** | **dispensable** |
| drop 5 | −0.720 | necessary |
| drop 7, 11, 13 | −0.30, −0.47, −0.14 | necessary |
| drop 17, 19 | = full | mute (a_p=0, p²>62) |
| drop 23…47 | all λ₀<0 | necessary |
| drop 53, 59, 61 | still + | edge, light |

Control at μ=38, NB=16: drop-3 λ₀ = 0.380, matching the journal
+0.37. The full form agrees with the 201 s sequential parallel-run
to every printed digit. Do not identify ℓ_Q=14.46 with the Gram
depth (`tests/test_gl2_37a1_Q_vs_gram.py`).

## Verdict: KILL

3 is still dispensable at μ=62. The preregistration is dead.
The tower is weaker (0.37 → 0.093) but a well of depth 14.46
does not make it necessary. Every other *voting* prime is
already locked (17 and 19 are mute: a_p=0 and p²>μ). Heaviest
last remains the pattern; the μ=62 threshold was wrong.

Shipped: `assemble(..., drop=p)`, `assemble_pair`,
`assemble_drops` (one wall-clock assemble on 32 cores),
`code/gl2_quorum_scan.py`. Judge: `tests/test_gl2_37a1_drop3.py`.

`a_37` in `gl2_curves.BAD_AP` was +1 and is −1 (split
multiplicative, `ellap`). Invisible at μ=11 (N>11); required at
μ=62. Rank-1 conductors 43, 53, 61 corrected the same way.

## Status

| Claim | Status |
|---|---|
| a_3 = −3, \|Λ_f(3)\|/3 = log 3 | theorem |
| μ=38, drop 3 still positive (~0.37) | judged |
| μ=62, full Q PSD, ℓ=14.46 | judged, prime side |
| μ=62, drop 3 → negative | **false** (KILL) |
| 17, 19 mute at μ=62 | judged (a_p=0, drop = full) |
| quorum complete at μ=62 | false; 3 still out |
| (∀ L) Q_L ≥ 0 | RH; not this note |
