# Maass: zeros and a_n exist; Gram is the shipped path; prime-side Q is not implemented.
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from scan_gl2 import gram, CURVES  # noqa: E402
import scan_q_gl2  # noqa: E402
import scan_s  # noqa: E402

CODE = os.path.join(os.path.dirname(__file__), "..", "code")


def test_maass_inputs_exist_and_q_path_does_not():
    assert "maass1" in CURVES
    assert os.path.exists(os.path.join(CODE, "zeros_maass1_weyl.pkl"))
    assert os.path.exists(os.path.join(CODE, "maass_an_1.0.1.1.1.json"))
    rec = json.load(open(os.path.join(CODE, "maass_an_1.0.1.1.1.json")))
    assert rec["R"] > 9 and len(rec["a_n"]) >= 50
    assert "maass" not in scan_q_gl2.CURVES
    src = open(os.path.join(CODE, "scan_s.py"), encoding="utf-8").read()
    assert "maass" not in src.lower()
    import scan_q_maass
    assert hasattr(scan_q_maass, "assemble")
    rec = scan_q_maass.load_form("maass1")
    assert rec["R"] > 9

    # harvest_maass_zenodo: coefficients feed Γ_R(s±iR), not scan_gl2
    hz = open(os.path.join(CODE, "harvest_maass_zenodo.py"), encoding="utf-8").read()
    assert "Γ_R(s±iR)" in hz or "Gamma_R(s±iR)" in hz or "s±iR" in hz


def test_maass1_gram_indef_maass2_isolated_below_float64_wall():
    lam1, ell1 = gram("maass1", 16.0, 24)
    assert lam1 <= 0 or ell1[0] != ell1[0]  # INDEF or nan depths
    # Table 1 μ=8 N=25 has ℓ≈35, λ~10^{-15}: float64 reports INDEF.
    # A slightly smaller window is isolated in numpy.
    lam2, ell2 = gram("maass2", 6.0, 12)
    assert lam2 > 0, lam2
    assert 20 < ell2[0] < 40, ell2[0]
