# 37a1 μ=62 was preregistered (journal §116). Drive shipped scan_gl2.gram.
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from scan_gl2 import gram  # noqa: E402


def test_37a1_mu62_zero_gram_isolated():
    lam0, ell = gram("37a1", 62.0, 80)
    assert lam0 > 0, lam0
    assert ell[0] > 10, ell[0]
    # Rank-1: Gram includes the central zero; shallower than a rank-0 well of similar conductor
    assert ell[0] < 40, ell[0]
