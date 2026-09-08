<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->

# Route 2 — Q on grid prolates (not cosine span)

θ_ij(y) = 2 ∫_0^{L-y} ψ_i(t) ψ_j(t+y) dt by shift+interp
on a 401-point Slepian kernel. Same A / atoms as Q_window.
Sanity: on cosine hats, |θ_num − θ_hat| ≤ 5e-3 at y=log 2;
θ(0) ≈ 2I.

μ=5, 4 prolates:

    χ     cosine Q4    grid c=2π      grid c=4π
    χ₃    +1.43e-5     −0.417         −1.38
    χ₅    +1.17e-3     −0.644         −1.60

Route B (#114) stayed PD because U lived in V_12^cos.
Route 2 leaves that span: the discrete Slepian has endpoint
leakage the cosine projection had killed. Truncated Q
(atoms n<μ only) then goes negative.

This is not a Weil hole (tests are not shown to be in W_L).
It is not a take. It says: the ×400 of Route B was a
property of the cosine shadow, not of the prolates.

Not W_L. Not RH.
