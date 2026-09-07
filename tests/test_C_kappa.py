# Copyright © 2026 Denis Joubert.
# This file may be distributed under the GNU GPL v3 or later,
# or the Creative Commons Attribution-ShareAlike 4.0 International
# License, subject to the binding interpretation in
# LICENSE.md (section 3).
# C is readable, kappa is not on the same Q (notebook 51).
C_SEQ = (7.107e3, 402.0, 119.8, 66.8, 48.1)
C_PUB = 27.8


def test_C_decreases_toward_published():
    assert all(C_SEQ[i] > C_SEQ[i + 1] for i in range(len(C_SEQ) - 1))
    assert C_SEQ[-1] > C_PUB
    assert C_SEQ[-1] / C_PUB < 2.0
