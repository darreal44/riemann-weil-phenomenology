<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# g_lo at s₀=3/4: the well is not a χ₅ artefact

Preregistered (`report/prereg-av-I01-odd.md`).
Same v=(4,−3,1)/√26, μ=16. Odd Bose
(χ₃, s₀=3/4), not another v on χ₅.
χ itself does not enter g; s₀ does.

    g = 2 e^{−y/2} − θ_v
    w = 2 e^{−3y/2}/(1−e^{−2y})

## Execution

`python code/av_I01_odd.py`.
`report/av-I01-odd.json`.

    gp0    = −0.962     (even −2.962)
    gpp0   = +5.636     (even +9.64)
    ymin   = 0.180      (even 0.410)
    yinf   = 0.6125     (even 0.772)
    I_true = −0.010926
    I_lo   = −0.013765
    gap    = +0.002840  (N=4 well+rise+chord)

The well lives. It is shorter and
shallower, not dead. g_lo ≤ g.
The N=4 gap sits in ±0.003 on this
odd integral (a different scale from
even I_{[0,1]}≈−0.70).

## Verdict: SURVIVE

g_lo is not a χ₅ artefact. It is
an even/odd Bose shape on this v.
e₀ on χ₅ still has no well
(`av-I01-vscan.md`). One v, one L.
Not Weil. Not (∀ L) Q_L ≥ 0. Not RH.

Judge: `tests/test_av_I01_odd.py`.
