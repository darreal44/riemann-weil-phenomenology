<!--
Copyright © 2026 Denis Joubert.
This file may be distributed under the GNU GPL v3 or later,
or the Creative Commons Attribution-ShareAlike 4.0 International
License, subject to the binding interpretation in
LICENSE.md (section 3).
-->
# I_{[0,1]} N=4 chords on the concave tail

`python code/av_I01_chord.py`

Well+rise as #86. Broken chords on [y_inf,1]
(g concave ⇒ a chord is a lower bound).
g''<0 on the tail (grid).

    I_true = −0.700799
    I_lo   = −0.703601
    gap    = +0.002802
    Q_lo   = +0.0027

Tighter than #86 (0.00315). The ±0.003
A-window on I is crossed by 0.0002.
That is still one v, finite μ, a comparison
of I_{[0,1]} not of the class.

Verdict: SURVIVE. I_{[0,1]} by a hand
bound is still not Weil positivity.
Not (∀ L) Q_L≥0. Not RH.

Judge: `tests/test_av_I01_chord.py`.
LICENSE.md
