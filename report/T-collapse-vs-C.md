# Collapsing mode of T versus the C-channel

w = ground state of T (σ_min).
v₀ = leading right vector of C.

| μ | σ_min(T) | ρ(v₀) | ρ(w)=1/σ_min | |⟨v₀,w⟩| | w peaks | v₀ peaks |
|---|---|---|---|---|---|---|
| 8 | 1.07 | 0.46 | 0.93 | 0.26 | φ₅ | φ₃ |
| 11 | 0.67 | 1.20 | 1.50 | **0.82** | φ₅ | φ₃ |
| 16 | 0.23 | 0.57 | 4.3 | 0.19 | φ₆ | φ₄ |
| 22 | 5×10⁻⁴ | 0.44 | 1.9×10³ | **0.00** | φ₇ | φ₃ |

They coincide at the crossing
μ=11 (σ₁(C)/σ_min(T) ≈ 1,
report/singular-values-chi5.md).
Before and after they live on
different tail hats and the
overlap drops.

At μ=22, w is the well leaking
into the tail (ρ(w) ∼ 1/λ₀
scale in float) and is exactly
orthogonal to the C-channel.
That is why ρ(v₀) stayed 0.44
while σ_min(T) died.

The picture is not “v₀ ⊥ w
always”. It is: they mix at
the crossing, then the well
leaves the channel and hides
in a further hat. A bound on
ρ(v₀) still controls the
rank-1 Schur term; it does
not control λ_min(T).
