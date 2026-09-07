<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# χ₃ ρ_far: larger N_NEAR / 3-layer do not take

Preregistered (`report/prereg-ql-chi3-rhofar.md`):
same Neumann split as #61, h=2, T infinite.
Grid N_NEAR=24..80 and a 3-layer split.
Not Galerkin of W_L. Not RH.

Named in `chi3-obstacles.md` item (3).

## Execution

`python code/ql_chi3_rhofar.py`.
`report/ql-chi3-rhofar.json`.

Need ρ<0.41: S_diag=+0.0076 leaves
0.0109 of λ_H=0.0185.

| N | ρ_N | ρ_B | ρ_far | ρ | S_diag | S_lo |
|---|---|---|---|---|---|---|
| 24 | 0.275 | 0.157 | 0.534 | 0.608 | +0.0076 | **−0.0098** |
| 32 | 0.283 | 0.163 | 0.503 | 0.590 | +0.0076 | **−0.0086** |
| 40 | 0.288 | 0.154 | 0.480 | 0.566 | +0.0075 | **−0.0071** |
| 48 | 0.292 | 0.153 | 0.459 | 0.550 | +0.0075 | **−0.0062** |
| 64 | 0.298 | 0.146 | 0.428 | 0.523 | +0.0075 | **−0.0048** |
| 80 | 0.301 | 0.139 | 0.415 | 0.508 | +0.0075 | **−0.0041** |

N=32 reproduces #61 (ρ=0.590, S_lo=−0.0086).
ρ_N climbs (finite Hankel filling toward π).
S_diag is frozen: C is already in the N=24
block (tr CDC 0.060→0.062). ρ_far(80)=0.415
still ≥0.41. Q_nn(80)=5.03; off_far stays
π/2+|w₂|≈2.06.

3-layer n=2..23 / 24..47 / ≥48:

    ρ₁=0.275  ρ₂=0.104  ρ₃=0.459
    ρ=0.552   S_lo=−0.0063

The mid block is small; the 3×3 block-norm
reconstructs the 2-layer ρ at N=48 (0.550).
No gain.

Hankel-only (t₂=0): ρ(32)=0.506, ρ(80)=0.449,
both >0.41. S_lo still negative (−0.0039
at N=32, −0.0016 at N=80). T₂ is not the
only wall; Hilbert π/2 is.

## Verdict: SURVIVE

Larger N_NEAR does not take χ₃. 3-layer
does not take χ₃. The Hilbert π/2 in
off_far is the wall: ρ ≥ ρ_far ≥ 0.41
on this grid, and ρ_N climbing keeps
the block-norm in the 0.50 class.
Same cosine ONB, h=2. Not every χ.
Not (∀ L). Not RH.

Judge: `tests/test_ql_chi3_rhofar.py`.

## Status

| Claim | Status |
|---|---|
| S_lo>0 on χ₃ at N≤80 | **false** |
| ρ_far(80)<0.41 | **false** (0.415) |
| 3-layer ρ<0.41 | **false** (0.552) |
| Hankel-only ρ<0.41 | **false** |
| ρ_N climbs with N | judged |
| S_diag frozen at +0.0075 | judged |
| S_lo>0 on χ₅ | judged (#61) |
| c_L^* ≥ 0 for every χ | **open; not taken** |
| (∀ L) Q_L ≥ 0 | RH; not this note |
