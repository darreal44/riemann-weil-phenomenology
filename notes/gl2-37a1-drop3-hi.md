# 37a1 drop 3 at μ ≫ 80: 3 joins

Preregistered (`report/prereg-37a1-drop3-hi.md`): drop-3 λ₀
stays positive, O(0.1), on μ = 100, 110, …, 250; the full
well stays PSD and deepens. Kill: any μ with drop-3 λ₀ < 0.
Prime-side Q, NB=80, dps=50. Not the Gram. Not RH.

The previous plateau +0.09 at μ=62–80 (`gl2-37a1-mu74.md`)
was computed with `ppts_of` capped at 67, so primes 71 and 73
never entered the explicit sum. At μ=74, drop-71 and drop-73
equal the full form to every printed digit. This run uses
`prime_power_prime` (every p^k).

## Execution

`python code/gl2_drop3_hi.py`, 32 jobs, 32 workers, 264.8 s
wall (estimate was ~240 s). Table:
`report/gl2-37a1-drop3-hi.json`.

| μ | full λ₀ | full ℓ | drop 3 λ₀ |
|---|---|---|---|
| 74 (ppts with 71) | 3.616×10⁻⁸ | 17.14 | **+0.090** |
| 80 (ppts with 71, 73) | 8.228×10⁻⁹ | 18.62 | **+0.089** |
| **100** | 2.759×10⁻¹⁰ | 22.01 | **−0.418** |
| 110 | 4.611×10⁻¹¹ | 23.80 | −0.646 |
| 120 | 1.215×10⁻¹¹ | 25.13 | −0.750 |
| 130 | 2.376×10⁻¹² | 26.77 | −0.796 |
| 140 | 3.405×10⁻¹³ | 28.71 | −0.819 |
| 150 | 6.947×10⁻¹⁴ | 30.30 | −0.826 |
| 160 | 1.718×10⁻¹⁴ | 31.70 | −0.827 |
| 170 | 3.184×10⁻¹⁵ | 33.38 | −0.827 |
| 180 | 7.229×10⁻¹⁶ | 34.86 | −0.828 |
| 190 | 1.485×10⁻¹⁶ | 36.45 | −0.835 |
| 200 | 2.716×10⁻¹⁷ | 38.14 | −0.849 |
| 210 | 6.358×10⁻¹⁸ | 39.60 | −0.869 |
| 220 | 2.226×10⁻¹⁸ | 40.65 | −0.897 |
| 230 | 7.877×10⁻¹⁹ | 41.69 | −0.931 |
| 240 | 2.584×10⁻¹⁹ | 42.80 | −0.969 |
| **250** | 6.929×10⁻²⁰ | 44.12 | **−1.016** |

16/16 drop-3 negative. The full form stays PSD; ℓ goes
22 → 44. Drop-3 does not stall at +0.09: it is already
−0.42 at μ=100 and keeps going down, with a shelf near
−0.827 on 150–180.

Heavy primes that the old list missed or that sit past 80:
a_71 = 9, a_73 = −1 (almost mute), a_83 = −15 (relative
0.82, first new interior prime in (80, 100]), a_103 = 18.

## Control (μ=74 and 80, ppts with 71+)

`python code/gl2_drop3_hi.py --control`, 4 jobs, 206 s.
`report/gl2-37a1-drop3-control.json`.

Putting 71 (a_71=9) and 73 (a_73=−1) into the sum deepens
the full well (μ=80: ℓ 17.37 → 18.62) but drop-3 stays
+0.090 / +0.089. The old plateau was not an artifact of
the cap at 67. 3 is still dispensable at μ=80.

The cliff is (80, 100]. New interior primes: 83, 89, 97.
a_83 = −15 (relative 0.82), a_89 = a_97 = 4. Isolated
(`notes/gl2-37a1-drop83.md`): drop-3 still +0.048 at
μ=84 (83 just arrived); drop-83 < 0 at μ=100. 83 is a
voter on the cliff window, not the sign change of 3.

## Verdict: KILL (the plateau)

The O(0.1) prediction is dead. 3 is necessary on every
window μ=100..250. Heaviest last still holds: 3 was the last
recalcitrant at μ=62, and it has joined by μ=100. This is
not a sixth slope and not RH.

Judge: `tests/test_gl2_37a1_drop3_hi.py`,
`tests/test_prime_power_prime.py`.

## Status

| Claim | Status |
|---|---|
| drop-3 plateau O(0.1) on 100..250 | **false** (KILL) |
| any drop-3 λ₀ < 0 on the grid | judged, 16/16 |
| full Q PSD, well deepens | judged (ℓ 22→44) |
| ppts include p>67 | judged (`prime_power_prime`) |
| drop-3 still +0.09 at 74/80 with 71+ | judged (control) |
| 3 necessary at μ≥100 | judged, prime side |
| (∀ L) Q_L ≥ 0 | RH; not this note |
