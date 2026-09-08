<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->

# Route B — Q on Slepian-in-cosine (μ=5)

Discrete Slepian kernel on [0, L], L=log 5, first 4 eigenvectors
projected onto cosine hats n=0..11, QR, then

    Q_B = Uᵀ Q_12 U     (4×4)

Same atoms p^k as Q_window. This is a 4-plane inside V_12^cos,
not W_L and not a new θ_nm. Courant the right way: another
subspace can have a larger λmin.

    python  (session REPL; no new driver required)

## λmin(Q_B) vs cosine Q4

    χ     cosine Q4     c=2π (dof~2)   c=4π (dof~4)   c=6π (dof~6)
    χ₃    1.43e-5       5.80e-3        1.42e-4        8.96e-5
    χ₅    1.17e-3       1.88e-3        9.30e-4        2.98e-3

χ₃, c=2π: ×400 vs the first four cosines. mass of p0 on {φ0,φ1}
is still 0.997 — the Slepian 4-plane sits in the 2-plane plus
higher hats, but *avoids* the pinched direction (0.82, −0.57).

χ₅ already had T3; the gain is smaller (×1.6 at c=2π).

## Reading

The fragile object was V_4^cos, not « every 4-plane ».
Route B does not take W_L: U lives in 12 cosines.
c is a bandwidth knob, not a proof parameter.

Not RH. step_is_taken() unchanged.
