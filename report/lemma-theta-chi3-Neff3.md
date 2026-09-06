# χ₃ at N_eff = 3.00

    python3 code/scan_s.py chi3 80 24 48
    λ₀ = 5.595×10⁻⁴⁹   −ln λ₀ = 111.1
    N_eff = 3.00   k̄ = 1.02   l₁/l₀ = 2.4×10⁶

µ=80, 25 hats, dps=48. λ₀ still
positive. This is the first Dirichlet
character at the four-mode threshold.

## What moved

| | χ₃ µ=16 NB=8 | χ₃ µ=80 NB=24 | ζ (four-mode) |
|---|---|---|---|
| N_eff | 2.28 | **3.00** | 3.1–3.4 |
| k̄ | 0.63 | 1.02 | ~1.1 |
| v₀/|v₁| vs ONB | — | 0.807 / 0.773 (**+4 %**) | few % |
| C = L λ₀/ε² | 0.12–0.16 | **0.113** | → 0.092 = 1/(4e) |
| a L² / (−ln λ₀) | 0.62 | **0.62** | → 1 |

Signs of v: + − + − + − on the first
six hats (same even-bulk pattern).
Mass: 0.29, 0.45, 0.20, 0.048 on
n=0..3. The fourth hat is on.

## What did not move

C is still the two-mode number, 23 %
above 1/(4e). The Gaussian width in
the bulk is still 62 % of −ln λ₀ —
the leftover decades live at the
edge, not in a. N_eff=3 is necessary
and not sufficient for the ζ limit
of C.

ε in float64 is 10⁻¹⁶ (false zero).
C has to be assembled in mpmath:
ε = 4.65×10⁻²⁴, C = 0.113.

## Next

Same µ, more hats, watch C:

    python3 code/scan_s.py chi3 80 28 52

If C stays at 0.11 while N_eff exceeds
3, the 1/(4e) limit is a ζ phenomenon
(archimedean weight), not a function
of N_eff alone.
