# Spectrum of the residual H = A−P

2-plane coordinates. v₀ = ground state of H.
Q wells from `scan_s` at the same μ
(NB just above N_eff).

## χ₅ — H versus the well of Q

| μ | λ_min(H) | λ₀(Q) | H/Q | λ_max(H) | v₀ |
|---|---|---|---|---|---|
| 8 | 8.5×10⁻⁵ | 9.6×10⁻⁷ | 89 | 0.77 | (0.999, 0.04) |
| 16 | 3.2×10⁻⁶ | 1.6×10⁻¹² | 2×10⁶ | 0.0039 | (0.989, 0.15) |
| 22 | 6.9×10⁻⁷ | 1.0×10⁻¹⁴ | 7×10⁷ | 0.012 | (0.989, 0.15) |
| 30 | 8.7×10⁻⁷ | 9.8×10⁻¹⁹ | 9×10¹¹ | 0.0097 | (0.987, 0.16) |
| 38 | 1.4×10⁻⁶ | 5.4×10⁻²² | 3×10¹⁵ | 0.0022 | (0.983, 0.19) |

λ_min(H) ∼ μ^{−3}. λ₀(Q) is
exponential in L = log μ
(ℓ ≈ 14, 27, 32, 41, 49).
The ratio H/Q is the Schur
factor: how much C T⁻¹ Cᵀ
eats H. Already 10² at μ=8,
10¹⁵ at μ=38.

v₀ stays on e₁. The 10° tilt
at μ=38 (0.19 on e₂) is not
the well direction of Q
(N_eff = 1.87 → 2.41: Q's
ground state is leaving the
plane, not rotating inside it).

λ_max(H) is not monotone
(0.77 → 0.004 → 0.012 → 0.002).
It tracks the residual on e₂
after each new prime power,
the same flips as running det.

## χ₈ / χ₁₃

χ₈: λ_min(H) ∼ μ^{−4.5}, v₀ on e₁.
χ₁₃: λ_min(H) ∼ μ^{−4.8}, v₀
rotates *onto* e₁ (0.81 → 0.998)
as the desert fills. ‖H‖ is O(1);
the 2-plane is easy and is not
where Q lives (N_eff ≈ 3 at
large μ).

## What the note does not give

A theorem λ_min(H) ≥ c μ^{−5}.
The table is compatible with
that power, and the power is
useless for λ₀(Q). Transfer
through Schur needs ‖T⁻¹‖,
which grows like 1/λ₀.
