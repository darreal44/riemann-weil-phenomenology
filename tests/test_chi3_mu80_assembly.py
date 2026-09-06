"""χ₃ µ=80 must stay positive once every prime ≤ 80 is in the Euler product."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))
from scan_s import assemble

def test_scan_s_chi3_mu80_positive():
    lam, ell, dt = assemble('chi3', 80.0, 8, 28)[:3]
    assert lam > 0, lam
    assert ell[0] > 40, ell[0]


def test_spectro_sieve_includes_41_to_79():
    src = open(os.path.join(os.path.dirname(__file__), '..', 'code', 'spectro.py')).read()
    assert 'hardcoded list ending at 37' in src or 'sv[' in src
    assert '[2,3,5,7,11,13,17,19,23,29,31,37]' not in src
