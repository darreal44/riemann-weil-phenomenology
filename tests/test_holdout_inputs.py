# map2 HOLD gamma1 must match the harvested zero caches.
import os, pickle, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'code'))
import map2

CACHE = {
    '-8': 'zeros_chim8.pkl',
    '-20': 'zeros_chi20.pkl',
    '-23': 'zeros_chi23.pkl',
}
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'code')


def test_hold_gamma1_matches_pickle():
    hold = {row[0]: row for row in map2.HOLD}
    for name, fname in CACHE.items():
        zs = pickle.load(open(os.path.join(BASE, fname), 'rb'))
        g1 = float(zs[0])
        gap = float(zs[1]) - float(zs[0])
        assert abs(hold[name][2] - g1) < 1e-6, (name, hold[name][2], g1)
        assert abs(hold[name][3] - gap) < 1e-3, (name, hold[name][3], gap)


def test_chi23_is_odd_with_small_gap():
    row = [r for r in map2.HOLD if r[0] == '-23'][0]
    assert row[1] == 1
    assert row[3] < 1.4
