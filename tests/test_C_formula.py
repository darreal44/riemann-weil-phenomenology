# C = 2 Lambda(mu) / (pi L sqrt(mu)) (notebook 48).
import math
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))
from endpoint_tail import C_endpoint

MEAS = {11: 0.1899, 13: 0.1770, 9: 0.1036, 16: 0.0422}


def test_new_formula_hits_all_four():
    for mu, C in MEAS.items():
        pred = C_endpoint(mu)
        assert abs(C / pred - 1) < 0.07, (mu, C, pred)


def test_old_formula_fails_mu9():
    old = math.log(3) / (4 * 3)
    assert abs(MEAS[9] / old - 1) > 0.08
