# Schur: Q>0 ⇔ T>0 and Δ>0. Courant: λ_min(H) ≥ λ₀(Q). Not a bound on T⁻¹.
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from scan_s import assemble  # noqa: E402
from schur_head import mp_to_numpy, schur_delta, schur_report  # noqa: E402
from H_2plane_independent import H2  # noqa: E402


def _Q(name, mu, NB, dps):
    os.environ["RETURN_S"] = "1"
    try:
        out = assemble(name, mu, NB, dps)
    finally:
        os.environ.pop("RETURN_S", None)
    return mp_to_numpy(out[3])


def test_chi13_Q_positive_iff_T_and_delta():
    Q = _Q("chi13", 16.0, 12, 28)
    r = schur_report(Q, nhead=3)
    assert r["lam_T"] > 0
    assert r["lam_delta"] > 0
    assert r["lam0"] > 0
    # variational: graph Rayleigh ≤ λ_min(Δ)
    assert r["lam0"] <= r["lam_delta"] * (1 + 1e-6)
    # the measured near-equality is the graph correction, not an identity of matrices
    assert abs(r["ratio"] - 1.0) < 0.02


def test_courant_two_plane_is_necessary_not_sufficient():
    _, detH, evH, _ = H2("chi13", 16, 28)
    Q = _Q("chi13", 16.0, 12, 28)
    lminH = float(min(evH))
    l0 = float(np.linalg.eigvalsh(Q)[0])
    l3 = float(np.linalg.eigvalsh(Q[:3, :3])[0])
    assert float(detH) > 0
    assert lminH >= l3 - 1e-12  # restriction to a 2-plane inside 3 hats
    assert l3 >= l0 - 1e-12  # Cauchy interlacing / compression
    assert lminH / l0 > 10  # necessary, far from sufficient
