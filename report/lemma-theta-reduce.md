# reduce_Q.py — the recipe, run

    python3 code/reduce_Q.py NAME µ NB dps

µ=16.

| L | block | λ₀ | v₀/|v₁| | N_eff |
|---|---|---|---|---|
| χ₅ | 2-hat | 5.0×10⁻⁵ | 1.45 | 1.77 |
| χ₅ | 4-hat | 7.2×10⁻⁸ | 1.13 | 2.04 |
| χ₅ | full 17 | 4.2×10⁻¹⁵ | 1.03 | 2.14 |
| χ₃ | 2-hat | 9.3×10⁻⁵ | 1.48 | 1.76 |
| χ₃ | 4-hat | 1.0×10⁻⁹ | 1.05 | 2.14 |
| χ₃ | full 17 | 1.6×10⁻²¹ | 0.96 | 2.32 |
| χ₄ | 2-hat | 4.5×10⁻⁴ | 1.54 | 1.72 |
| χ₄ | 4-hat | 8.1×10⁻⁸ | 1.16 | 2.01 |
| χ₄ | full 9 | 2.9×10⁻¹³ | 1.06 | 2.09 |

2-hat: signs and the first three decades.
4-hat: N_eff has arrived; λ still short of
the full value by 6–12 decades. Extra hats
beyond 4 do not raise N_eff, they only
deepen the edge kill.

χ₃ at dim 17 is the first character to
leave the frozen-2 box (N_eff=2.32,
−ln λ=48). The recipe "r=2 off ζ" is the
interpretation plane, not the production
cutoff once µ and dim are large enough
for rungs to light.
