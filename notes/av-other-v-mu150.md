# Other v at μ=150

Preregistered (`report/prereg-av-other-v-mu150.md`):
the μ=16 pencil of `v-impact.md` stays Q>0 at
μ=150; the 3-plane stays PSD; v_min stays in
the pencil. Kill if any of the five pencil
vectors has Q≤0, or λ_min(H_150)≤0.
χ₅, three hats. Not a sixth slope. Not RH.

#45 ran only v=(4,−3,1)/√26.

## Execution

`python code/av_other_v.py`, two μ in parallel,
one 3×3 assemble each, 0.2 s wall.
`report/av-other-v-mu150.json`.

μ=16 reproduces `v-impact.md` to the printed
digit. μ=150:

| v | pencil | Q(16) | Q(150) |
|---|---|---|---|
| (4,−3,1)/√26 | yes | 0.00551 | **0.00410** |
| (5,−4,1) | yes | 0.00139 | **0.00103** |
| (4,−3,0) | yes | 0.00051 | **0.00029** |
| (1,−1,0) | yes | 0.00942 | **0.00702** |
| (3,−2,1) | yes | 0.01900 | **0.01415** |
| e₀ | no | 0.092 | 0.074 |
| e₁ | no | 0.194 | 0.152 |
| e₂ | no | 0.239 | 0.169 |

λ_min(H): 2.3×10⁻⁶ at 16, 7.8×10⁻⁹ at 150,
both >0. ⟨v_rat, v_min⟩ = 0.994 at 16,
**0.995** at 150 (sign aligned).

A−P₂₃ going through 0 at μ=150 is *this* v,
not the 3-plane: (5,−4,1) and (1,−1,0) still
have A−P₂₃>0. Same pairing, different
direction. Not a sixth slope.

## Verdict: SURVIVE

Every μ=16 pencil witness is still a witness
at μ=150. The ground state of the window did
not leave the pencil. One rational choice
fitted at 16 still rides A−P tracking, and
so do its neighbours in the 3-plane. This
is not (∀ μ) and not RH.

Judge: `tests/test_av_other_v.py`.

## Status

| Claim | Status |
|---|---|
| μ=16 table of v-impact | reproduced |
| pencil Q>0 at μ=150 | judged, five of five |
| λ_min(H_150)>0 | judged (tiny) |
| v_min still in the pencil | judged (overlap 0.995) |
| A−P₂₃<0 at 150 for every v | **false** |
| (∀ μ) Q(v)>0 | open; not this point |
| (∀ L) Q_L ≥ 0 | RH; not this note |
