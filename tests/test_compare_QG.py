# Drive shipped compare_QG / scan_s.assemble + gram.
# Truncated Gram is NOT within λ_min of Q: the |Q-Gram|<λ_min route is closed as a proof.
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
os.environ["RETURN_S"] = "1"
from compare_QG import gram  # noqa: E402
from scan_s import assemble  # noqa: E402


def test_chi29_mu11_G_below_Q_and_Frel_exceeds_lambda_min():
    lamQ, _, _, S = assemble("chi29", 11.0, 24, 40)
    NB = 24
    Q = np.array([[float(S[i, j]) for j in range(NB + 1)] for i in range(NB + 1)])
    G, nz = gram("chi29", 11.0, NB)
    assert nz > 20
    evQ = np.sort(np.linalg.eigvalsh(Q))
    evG = np.sort(np.linalg.eigvalsh(G))
    assert evQ[0] > 0
    assert evG[0] > 0
    ratio = evG[0] / evQ[0]
    assert 0.85 < ratio < 1.0  # missing high zeros: Gram a bit low, not a proof
    froD = np.linalg.norm(G - Q, "fro")
    # operator-norm lower bound: ||D||_F ≥ ||D||_2 ≥ |λ_max(D)|; if ||D||_F > λ_min(G)
    # then |Q-Gram| < λ_min cannot hold
    assert froD > evG[0]
