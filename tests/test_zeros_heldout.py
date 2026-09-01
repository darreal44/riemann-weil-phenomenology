# First zeros of chi_-8, chi_-20, chi_-23: Hurwitz-cross-checked in notebook 18.
# Usage: python3 -m pytest tests/test_zeros_heldout.py -q
import os, pickle

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'code')

# (file, expected first three zeros at 1e-8)
HELD = {
    'zeros_chim8.pkl': (3.576154837, 7.434472957, 9.503201962),
    'zeros_chi20.pkl': (2.358934994, 4.675507750, 7.429109775),
    'zeros_chi23.pkl': (2.871339849, 4.215189804, 6.731189151),
}


def test_heldout_zero_caches_exist_and_match():
    for fname, expected in HELD.items():
        path = os.path.join(BASE, fname)
        assert os.path.exists(path), fname
        zs = pickle.load(open(path, 'rb'))
        assert len(zs) >= 3, fname
        for a, b in zip(zs[:3], expected):
            assert abs(float(a) - b) < 5e-9, (fname, float(a), b)


def test_chi23_gap_is_the_smallest():
    gaps = {}
    for fname, _ in HELD.items():
        zs = pickle.load(open(os.path.join(BASE, fname), 'rb'))
        gaps[fname] = float(zs[1]) - float(zs[0])
    assert gaps['zeros_chi23.pkl'] < gaps['zeros_chim8.pkl']
    assert gaps['zeros_chi23.pkl'] < 1.35
