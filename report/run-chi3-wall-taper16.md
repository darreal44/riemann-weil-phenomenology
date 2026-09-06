# χ₃ wall at µ=125, and the honest row

µ=125 / 150 with NB=16 dps=36 is not
N_eff→3. λ₀ = −0.21 / −0.27, N_eff
4–7: the assembly has lost the
cancellation. First break:

    µ=90 NB=12  λ₀ = −7×10⁻²²
    µ=100 NB=8  λ₀ = −0.004

Last stable window: µ=80.

| µ | NB | dps | λ₀ | N_eff | k̄ |
|---|---|---|---|---|---|
| 80 | 8 | 30 | 3.8×10⁻²³ | 2.66 | 0.84 |
| 80 | 12 | 40 | 1.1×10⁻³⁰ | 2.82 | 0.92 |
| 80 | 16 | 40 | 1.7×10⁻³⁷ | 2.91 | 0.97 |
| 80 | 20 | 42 | 2.6×10⁻⁴³ | **2.96** | 1.00 |
| 85 | 16 | 40 | 2.5×10⁻³⁸ | 2.93 | 0.98 |

N_eff=2.96 at µ=80, 21 hats. The four
mode is turning on (k̄=1). Do not
raise µ; raise NB at µ=80:

    python3 code/scan_s.py chi3 80 24 48

## taper16 — already computed (todo 0)

Λ=16, expected mass 0.490.

| cpu | w₂ | peak₂ |
|---|---|---|
| 32 | −0.26 | −17 |
| 48 | −0.13 | +4.5 |
| 80 | +0.14 | 50 |
| 96 | +0.26 | 71 |
| 112 | +0.35 | 89 |
| 128 | +0.44 | 105 |
| 160 | +0.59 | 133 |
| 200 | +0.66 | 148 |
| 400 | +1.08 | 228 |

w₂ crosses 0.49 between cpu 128 and
160. Past 160 the weight overshoots
and does not sit. The 2-adic lock at
Λ=16 is a crossing, not a plateau.
Next is an analytic tail for cpu>160
or Λ=24 with the same cpu grid
(w₂ at Λ=24 cpu=80 is still +0.019).
