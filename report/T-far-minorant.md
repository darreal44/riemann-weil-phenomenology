# Minorant of T_far

χ₃, n=32…39 (L=log 3):

    Q_nn ∈ [4.19, 5.01]
    nearby off |Q_{n,n+1}| ≲ 0.29 then drops.

Gershgorin says λ_min(T_far) ≥ min_n (Q_nn − ∑_{m≠n}|Q_nm|) if the row
sum is controlled. The shipped bound uses instead

    ρ_far = Off_far / qmin_far
    Off_far ≥ ½π ≈ 1.57 + |w₂|‖Θ‖ + HS.

That 1.57 is already a third of Q_nn, before θ. The true nearest off is
0.29. The gap between a Gershgorin minorant and the Hilbert majorant
*is* the room that ate χ₃’s +0.0076.

A legal Pólya-style minorant: keep the diagonal exact, majorise each row
sum of |Q_nm| by a summable 1/|n−m| plus a far 1/(n+m) *without* putting
π on the whole row. That is 2, not Bochner.

Until that row sum is written with a proof, T_far ≥ (1−ρ)D stays the
envelope and χ₃ stays red.

Not Weil.
