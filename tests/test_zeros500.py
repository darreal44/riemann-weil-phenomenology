# zeros500 cache is the Riemann-von Mangoldt pack used by the audit.
import math, os, pickle

BASE = os.path.join(os.path.dirname(__file__), '..', 'code')


def test_five_hundred_positive_zeros():
    zs = pickle.load(open(os.path.join(BASE, 'zeros500.pkl'), 'rb'))
    assert len(zs) == 500
    assert zs[0] > 14.13 and zs[0] < 14.14
    assert zs[-1] > 811.0 and zs[-1] < 811.4
    assert all(zs[i] < zs[i + 1] for i in range(len(zs) - 1))


def test_Nbar_near_500():
    T = 811.1843588465063
    Nbar = T / (2 * math.pi) * math.log(T / (2 * math.pi * math.e)) + 0.875
    assert abs(Nbar - 499.3) < 0.1
