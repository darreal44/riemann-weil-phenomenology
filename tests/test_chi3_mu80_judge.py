# Judge for χ₃ μ=80: scan_s at the certified window. Sign at larger NB is NOT settled
# (scan_s and spectro/edge_value disagreed at NB=32 dps=70 — do not harvest that).
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from scan_s import assemble  # noqa: E402


def test_scan_s_chi3_mu80_NB24_positive_ell_near_111():
    lam, ell, dt = assemble("chi3", 80.0, 24, 50)[:3]
    assert lam > 0, lam
    assert 108.0 < ell[0] < 114.0, ell[0]


def test_scan_s_chi3_mu80_NB8_positive():
    lam, ell, dt = assemble("chi3", 80.0, 8, 28)[:3]
    assert lam > 0, lam
    assert ell[0] > 40, ell[0]


def test_scan_s_chi3_mu80_NB32_unsaturated_negative():
    """Galerkin/quadrature unsaturated on scan_s at NB=32 dps=70.

    spectro/edge_value at the same (NB,dps) gave λ₀>0 and ℓ=135 — a
    different assembly (see test_chi3_assemblies). Do not harvest ℓ=135.
    The negative scan_s eigenvalue is not a sign of Q_L.
    """
    lam, ell, dt = assemble("chi3", 80.0, 32, 70)[:3]
    assert lam < 0, lam
