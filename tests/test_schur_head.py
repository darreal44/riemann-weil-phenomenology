# Schur identity λ₀(Q) = λ_min(H − C T⁻¹ Cᵀ). Identity, not a bound on T⁻¹.
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from scan_s import assemble  # noqa: E402
from schur_head import mp_to_numpy, schur_report  # noqa: E402
from H_2plane_independent import H2  # noqa: E402


def _Q(name, mu, NB, dps):
    os.environ["RETURN_S"] = "1"
    try:
        out = assemble(name, mu, NB, dps)
    finally:
        os.environ.pop("RETURN_S", None)
    return mp_to_numpy(out[3])


def test_chi13_mu16_schur_recovers_lambda0():
    Q = _Q("chi13", 16.0, 12, 28)
    r = schur_report(Q, nhead=3)
    assert r["lam0"] > 0
    assert abs(r["ratio"] - 1.0) < 0.02, r
    assert r["kappa_T"] < 1e3, r  # narrow desert: T is well-conditioned


def test_two_plane_does_not_transfer_to_lambda0():
    """H>0 on {e1,e2} is not a bound on λ₀: Schur tail is the rest of the well."""
    _, detH, evH, _ = H2("chi13", 16, 28)
    Q = _Q("chi13", 16.0, 12, 28)
    lminH = float(min(evH))
    l0 = float(np.linalg.eigvalsh(Q)[0])
    assert float(detH) > 0
    assert l0 > 0
    assert lminH / l0 > 10, (lminH, l0)
