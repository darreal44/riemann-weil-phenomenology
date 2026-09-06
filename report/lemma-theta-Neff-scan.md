# N_eff versus hat cutoff at µ=16

From `scan_s.py` (its own N_eff, not a
re-eigh of the dumped S).

| L | NB | dim | −ln λ₀ | N_eff | k̄ |
|---|---|---|---|---|---|
| χ₅ | 2 | 3 | 13.0 | 1.99 | 0.44 |
| χ₅ | 4 | 5 | 18.9 | 2.07 | 0.49 |
| χ₅ | 8 | 9 | 27.2 | 2.13 | 0.53 |
| χ₅ | 12 | 13 | 31.5 | 2.13 | 0.53 |
| χ₅ | 16 | 17 | 33.1 | 2.14 | 0.54 |
| χ₅ | 24 | 25 | 33.7 | 2.14 | 0.54 |
| χ₃ | 2 | 3 | 17.1 | 2.02 | 0.45 |
| χ₃ | 4 | 5 | 24.1 | 2.19 | 0.56 |
| χ₃ | 8 | 9 | 34.8 | 2.28 | 0.63 |
| χ₃ | 12 | 13 | 42.7 | 2.31 | 0.65 |
| χ₃ | 16 | 17 | 47.9 | 2.32 | 0.65 |
| χ₃ | 24 | 25 | (λ ≲ 0, dps=22 dies) | 2.33 | 0.66 |

χ₅ saturates: −ln λ₀ → 33.7, N_eff locked
at 2.14 past NB=8. Extra hats only polish
the already-killed edge.

χ₃ does not saturate at dps=22: −ln λ₀
keeps climbing 17 → 48 and N_eff creeps
2.02 → 2.33. A third mode is turning on,
slowly. Odd Γ_ℝ + conductor 3 has more
room than even χ₅. This is the first
character to leave the two-mode box at
these windows — still far from ζ's
N_eff ≈ 3.3 and a L² = −ln λ₀.

To see whether χ₃ reaches four-mode
curvature, need dps ≥ 30 and NB ≥ 16,
not more hats at 22 digits.
