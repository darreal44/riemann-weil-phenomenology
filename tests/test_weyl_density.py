# Runs after harvest_weyl.py. Skips if the pkl is not there yet.
import math
import os
import pickle

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _load(name):
    p = os.path.join(ROOT, "code", f"zeros_{name}_weyl.pkl")
    if not os.path.exists(p):
        pytest.skip(f"no {p}")
    return sorted(float(x) for x in pickle.load(open(p, "rb")))


def _weyl_ratio(zeros, q, T):
    have = sum(1 for g in zeros if g <= T)
    if T <= 1:
        return 0.0
    # one-sided count (the lists hold gamma > 0 only); (T/pi) would be the two-sided count and read 0.5 on a complete list
    expected = (T / (2 * math.pi)) * math.log(q * T / (2 * math.pi * math.e))
    return have / expected if expected else 0.0


@pytest.mark.parametrize("name,q,Tmin", [("chi5", 5, 80.0), ("chi29", 29, 40.0)])
def test_weyl_ratio_at_checkpoint(name, q, Tmin):
    z = _load(name)
    T = min(Tmin, z[-1])
    assert _weyl_ratio(z, q, T) > 0.9


@pytest.mark.parametrize("name,q", [("chi5", 5), ("chi29", 29)])
def test_weyl_ratio_at_end(name, q):
    z = _load(name)
    assert _weyl_ratio(z, q, z[-1]) > 0.9


@pytest.mark.parametrize("name,g1", [("chi5", 6.64845), ("chi29", 1.79381)])
def test_first_zero_matches_known(name, g1):
    z = _load(name)
    assert abs(z[0] - g1) < 0.02
