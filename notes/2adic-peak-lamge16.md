# 2-adic Fmat peak at Λ ≥ 16

Preregistered (`report/prereg-2adic-peak-lamge16.md`): at
Λ=24 and 32, w₂ still climbs with cpu, through Bombieri
0.490, not sitting at 0.707. Same Gibbs window as Λ=16,
not a Dirac. Not RH.

Haar (`haar-convergence.md`) wants Λ→∞ before ε→0. This
run is that direction: larger Λ, not a finer grid at Λ=16.

## Execution

`campaign_2adic_large.py --jobs lamge16`, 4 workers, 927 s
wall. Shipped reader: `code/peak_2adic.py`.

    Λ   cpu    Λ²/cpu     w₂
   16   160      1.60    0.594
   16   400      0.64    1.078
   24   160      3.60    0.828
   24   200      2.88    1.112
   32   128      8.00    0.484
   32   160      6.40    0.918

All three Λ climb. All three pass 0.490. Λ=24/cpu=200 and
Λ=16/cpu=400 are already past 0.707, heading toward
inverse-twist √2 = 1.414. The peak is still a window of
width ~Λ⁻², not resolved as a point mass.

## Verdict: SURVIVE (the climb)

Larger Λ does not freeze w₂ at Bombieri or at the module
twist. The Fmat integral remains the Gibbs pairing of
`2adic-shells.md`, not `mass_at_two`. Closing the grid is
still the wrong lock.

Judge: `tests/test_peak_2adic.py`.

## Status

| Claim | Status |
|---|---|
| Λ=16, w₂ climbs through 0.49 | judged (old) |
| Λ=24 and 32, same climb | judged, this note |
| Fmat = Dirac of Thm 4 | false |
| mass = √2 | open (unresolved peak) |
| (∀ L) Q_L ≥ 0 | RH; not this note |
