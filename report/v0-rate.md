# Rate of convergence of v₀

## In N, at fixed μ=16

Distance in the first three
hats to the N=12 vector:

    N=4   ‖Δ‖ = 4.5×10⁻²
    N=6         1.4×10⁻²
    N=8         6.9×10⁻³
    N=10        1.8×10⁻³

‖Δ‖ N² ≈ 0.7 → 0.18: a bit
faster than 1/N². Step overlap

    1 − ⟨v_N, v_{N-2}⟩
        = 4.7×10⁻⁴, 2.6×10⁻⁵,
          1.3×10⁻⁵, 1.6×10⁻⁶.

The shape is a spectral
projection onto an isolated
eigenvalue. Once N clears
the plunge, the projector
converges exponentially in
the gap, not in 1/N.

λ₀ itself is another story:
−ln λ₀ = 18.9, 24.4, 27.2,
29.8, 31.5. Each two hats
buy 2–5 nats, then less.
That is the well *depth*
eating bandwidth, not the
direction settling.

## In μ, at fixed N=8

Angle of (v₀,v₁):

    μ=8   −37.2°
    11    −40.9°   −11.5° per unit L
    16    −43.8°    −7.8°
    22    −45.4°    −5.1°

The drift slows. 1 − ⟨v(μ),v(8)⟩
= 0, 0.004, 0.017, 0.029 ≈
½ θ(μ)² in radians², as a
pure rotation predicts.

φ₂ / L = 0.017, 0.043, 0.064,
0.075 — still rising, not
a limit yet. The vector is
picking up a slow third
harmonic as the desert
lengthens, not rotating
inside a fixed 2-plane.

## Practical

N=8 is past the shape
knee. Extra hats change
v₀ at 10⁻³ and λ₀ by
factors of ten. For a
frozen witness one may
fix N=8 and spend the
effort on μ (the six
θ(log n) at that N).
