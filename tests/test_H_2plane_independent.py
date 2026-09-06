# Independent 2x2 matches cert_2plane. ~8 s.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from H_2plane_independent import H2


def test_independent_2x2_matches_projection():
    ref = {
        "chi5": (9.31467e-5, -5.8859e-4, 3.85503e-3, 1.265e-8),
        "chi3": (2.17859e-4, -1.38112e-3, 8.75825e-3, 5.666e-10),
    }
    for name, (h11, h12, h22, det) in ref.items():
        H, D, ev, _ = H2(name, 16, 24)
        assert abs(float(H[0, 0]) / h11 - 1) < 2e-4
        assert abs(float(H[0, 1]) / h12 - 1) < 2e-4
        assert abs(float(H[1, 1]) / h22 - 1) < 2e-4
        assert abs(float(D) / det - 1) < 5e-3
        assert float(min(ev)) > 0
