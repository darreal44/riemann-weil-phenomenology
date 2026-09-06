"""scan_s and spectro are different assemblies. Do not harvest one as the other.

At χ₃ μ=80 NB=32 the two disagreed in sign (scan_s λ₀<0, spectro λ₀>0
and ℓ=135). That number is not judged. This file: source difference,
and a cheap window where both signs are positive.
"""
import inspect
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
import scan_s  # noqa: E402
import spectro  # noqa: E402
from scan_s import assemble  # noqa: E402
import edge_value_scan as ev  # noqa: E402


def test_scan_s_and_spectro_differ_in_quadrature():
    src_s = inspect.getsource(scan_s.assemble)
    src_p = inspect.getsource(spectro.run)
    assert "NPANEL = 3*NB + 12" in src_s
    assert "NPANEL = 5*NB + 20" in src_p
    assert "for _ in range(5):" in src_s
    assert "for _ in range(6):" in src_p


def test_chi3_mu16_NB8_both_assemblies_positive():
    lam_s, ell_s, _ = assemble("chi3", 16.0, 8, 28)[:3]
    rec = ev.one("chi3:16:8:28")
    assert lam_s > 0, lam_s
    assert rec["lambda0"] is not None and rec["lambda0"] > 0, rec
    assert ell_s[0] > 20 and rec["ell"] > 20
    # same sign, not identified: quadrature families differ
    rel = abs(ell_s[0] - rec["ell"]) / max(ell_s[0], rec["ell"])
    assert rel < 0.25, (ell_s[0], rec["ell"], rel)
