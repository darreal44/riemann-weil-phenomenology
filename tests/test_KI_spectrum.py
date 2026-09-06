# K_I at log 2 has exactly one eigenvalue > 1; λ2 crosses 1 near L=1.01.
import os, sys, io, contextlib
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from KI_spectrum import eigs_at


def test_KI_log2_one_above_unity():
    ev, _ = eigs_at(np.log(2), omega=8e-3)
    assert ev[0] > 1.04 and ev[0] < 1.07
    assert ev[1] < 0.85
    assert (ev > 1).sum() == 1


def test_KI_lambda2_above_unity_past_1_02():
    ev, _ = eigs_at(1.02, omega=8e-3)
    assert ev[1] > 1.0
    assert (ev > 1).sum() >= 2
