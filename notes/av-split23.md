<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# av_split23.py — assemble_AP

Builds the 3×3
    A, P₂₃, P_rest
on {η₀,η₁,η₂} for one
character and one μ.
Unconditional pairing
(no zeros).

    assemble_AP(mu, dps=40, name="chi5")
    P₂₃ = n=2 and n=3 only
          (not 4,8,9)

Consumed by
av_other_v.py,
av_split23 main,
det H, αᵢ.
CHARS from scan_s.
Not Q_L on W_L.
Not a slope.
