# Kronecker tables for the three held-out characters + regression of the mod-8 rule.
# Usage: python3 -m pytest tests/test_kronecker.py -q
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'code'))
from kronecker import kronecker, chi_tab, jacobi


def test_chi_m8_table():
    assert chi_tab(-8, 8) == [0, 1, 0, 1, 0, -1, 0, -1]


def test_chi_m8_odd():
    assert chi_tab(-8, 8)[7] == -1  # chi(-1) = -1


def test_chi_m20_matches_dscan():
    t20 = [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, -1, 0, -1, 0, 0, 0, -1, 0, -1]
    assert chi_tab(-20, 20) == t20


def test_chi_m23_ends():
    t = chi_tab(-23, 23)
    assert t[0] == 0 and t[1] == 1 and t[22] == -1
    assert all(v in (-1, 0, 1) for v in t)


def test_mod8_rule_on_2():
    # (d/2) = (-1)^((d^2-1)/8) for odd d
    assert kronecker(5, 2) == -1
    assert kronecker(17, 2) == 1
    assert kronecker(-7, 2) == 1


def test_jacobi_rejects_even_modulus():
    try:
        jacobi(3, 8)
    except ValueError:
        return
    raise AssertionError('jacobi must reject even modulus')
