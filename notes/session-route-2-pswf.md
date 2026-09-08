<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->

# Route 2b — Nyström PSWF (not the raw 401-grid)

Gauss–Legendre Nyström of the Slepian kernel on [-1,1],
mapped to [0, L]. Concentrations λ_K ∈ (0,1). ON error 0.002.
Same θ_ij shift + Q_window arch/atoms. μ=5, 4 PSWF.

    χ     cosine Q4    PSWF c=π         PSWF c=2π        grid #116
    χ₃    +1.43e-5     −0.518           −1.38            −0.42
    χ₅    +1.17e-3     −0.679           −1.59            −0.64

λ_K(c=π) = 0.981, 0.75, 0.24, 0.025 (a real Slepian ladder).

The minus sign of #116 survives the ODE/Nyström. It was not
endpoint noise. Truncated Q on the first 4 PSWF is indefinite.

Not W_L (PSWF are not shown to be type L). Not a Weil hole.
Route 2 closed as a method: the cosine shadow (#114) was PD;
the functions themselves are not a positivity witness at μ=5.

Not RH.
