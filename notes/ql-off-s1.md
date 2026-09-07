<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# Proved s₁(Off_Q)

Named in `report/drop-half-pi.md`: replace the Hankel+Θ split by a
certified s₁(Off_Q). The split *was* already that bound (triangle). This
note writes both sides.

Off = H + R − w₂ Θ on ℓ²(n≥N), H_nm=½/(n+m) (n≠m).

    ‖H‖ ≤ π/2            Hilbert 1894; Hartman: tail ess = π/2
    ‖Θ‖ ≤ 1              y = log 2 ≥ L/2
    ‖R‖_F ≤ r_frob(N)    IPP

**Upper** (operator norm):

    s₁(Off_Q) ≤ π/2 + 1/(4N) + r_frob(N) + |w₂|.

χ₃, N=32: 2.110. This *is* Off_far. `ql_schur_neumann.py` now calls
`s1_off_q_upper`. S_lo unchanged (−0.0086).

**Lower** (essential norm):

    ‖A+B‖_ess ≥ ‖A‖_ess − ‖B‖,
    s₁(Off_Q)_ess ≥ π/2 − |w₂| = 1.081 (χ₃).

Hence s₁≤0.6 (PR #93), s₁≤0.8 and s₁≤1.0 (`drop-half-pi.md`) are false.
Dropping ½π flips S_lo by +0.0005 and is false. ½π stays.

Not taken. Not RH. `python code/ql_off_s1.py` `report/ql-off-s1.json`.
