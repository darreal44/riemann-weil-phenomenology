# Pre-registration: the mass of the 2-adic peaks in the slice trace distribution (5 September 2026)

Locked before any resolved peak (Λ ≥ 16, h ≲ 1/Λ²) is available.

**Object.** τ_Λ(λ) = Tr(P̂_Λ P_Λ ϑ(λ)) on the ord₂ = 0 slice, ϑ(λ)g(r) = λ^{-1/2} g(r/λ), masses
integrated in d*λ = dλ/λ over a window around λ = 2 and λ = ½ (semi-local minus archimedean).

**Derivation in our convention.** Our archimedean τ_Λ reproduces CC (39), τ_∞(λ) = λ^{1/2}/2·(1/(1+λ) + 1/|1−λ|),
which is Connes' (1999, Thm 4) local term ½(1/|1−u| + 1/(1+u)) *twisted by λ^{1/2}*: ϑ carries the Δ^{1/2}.
Connes' 2-adic term is ∫'_{Q₂*} h(u⁻¹)/|1−u|₂ d*u with d*u normalized to ∫_{Z₂*} d*u = 1. Reading it in
λ = |u|: at |u| = 2 (ord −1), |1−u|₂ = 2, shell measure 1 → weight ½ at λ = 2; at |u| = ½ (ord 1),
|1−u|₂ = 1 → weight 1 at λ = ½. Twisting by λ^{1/2}: ½·√2 = 1/√2 at λ = 2 and 1·(½)^{1/2} = 1/√2 at λ = ½.

**Locked prediction.** mass(λ = 2) = mass(λ = ½) = **1/√2 = 0.7071** in d*λ, symmetric.
**Alternative.** Weil–Bombieri's normalization gives (log 2)/√2 = **0.4901** (the log p from a different d*u).
**Falsifiers.** A resolved mass at 1.0 or 1.41 would mean the twist assignment is wrong (u ↔ u⁻¹);
a mass depending on Λ after resolution would mean the peak is not a point mass of Theorem 4.

**Data so far** (`campaign_2adic_large.csv`, Grok): at Λ = 16, mass(2) = 0.14, 0.26, 0.35, 0.44, 0.59
for h = 1/80 … 1/160 — still climbing, between the two candidates; mass(½) unresolved (far above).
Peak width ~ Λ⁻² = 0.004 at Λ = 16 against h = 0.006: not resolved yet. Decision requires h ≤ 1/400 at Λ = 16.
