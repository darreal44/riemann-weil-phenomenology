# 37a1: prime-side Q and the zero Gram are both positive and are not the same matrix.
# Rank-1 Gram includes the central zero; Q does not until the rank is read
# (test_gl2_eight_curves). Do not identify ℓ_Q with ℓ_Gram.
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from scan_gl2 import gram  # noqa: E402
from scan_q_gl2 import assemble  # noqa: E402


def test_37a1_mu11_Q_and_gram_both_positive_not_identified():
    lamQ, ellQ = assemble("37a1", 11.0, 12, 28)
    lamG, ellG = gram("37a1", 11.0, 12)
    assert lamQ > 0, lamQ
    assert lamG > 0, lamG
    # Rank-1 Gram already has a well (central zero on the constant mode).
    # Prime-side Q at μ=11 is positive but shallow: the rank is unread.
    assert ellG[0] > 5, ellG[0]
    assert ellQ[0] < ellG[0], (ellQ[0], ellG[0])
    rel = abs(ellQ[0] - ellG[0]) / max(ellQ[0], ellG[0])
    assert rel > 0.2, (ellQ[0], ellG[0], rel)


def test_37a1_mu62_zero_gram_stays_a_gram():
    """μ=62 Gram is judged here; prime-side Q at this μ is a different matrix.

    Do not quote the Gram depth as a Q-depth (central zero on the Gram,
    rank unread on the prime side until test_gl2_eight_curves).
    """
    lamG, ellG = gram("37a1", 62.0, 80)
    assert lamG > 0
    assert 10 < ellG[0] < 40
