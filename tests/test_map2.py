# Two-variable map and the published four-variable formula: lock the chi-23 kill.
# Usage: python3 -m pytest tests/test_map2.py -q
import math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'code'))
import map2


def test_lstsq_recovers_line():
    # y = 2 + 3 x
    X = [[1.0, float(i)] for i in range(4)]
    y = [2 + 3 * i for i in range(4)]
    c = map2.lstsq(X, y)
    assert abs(c[0] - 2) < 1e-9 and abs(c[1] - 3) < 1e-9


def test_two_var_kills_chi23():
    X, y = [], []
    for r in map2.TRAIN:
        X.append([1.0, math.log(r[2]), float(r[1])])
        y.append(math.log(r[-1]))
    c = map2.lstsq(X, y)
    # chi-23 hold-out row
    name, odd, g, gp, d, sc, so = [h for h in map2.HOLD if h[0] == '-23'][0]
    hat = math.exp(c[0] + c[1] * math.log(g) + c[2] * odd)
    err = hat / sc - 1
    assert hat > 1.0
    assert err > 0.80  # published kill was +97% vs Claude's 0.54


def test_four_var_also_misses_chi23_by_more_than_20pct():
    def s4(g1, gap, D, odd):
        return 0.14 * (g1 ** 1.32) * (gap ** 0.45) * math.exp(-0.13 * D) * (1.32 if odd else 1)
    name, odd, g, gp, d, sc, so = [h for h in map2.HOLD if h[0] == '-23'][0]
    hat = s4(g, gp, d, odd)
    assert abs(hat - 0.76) < 0.02
    assert hat / sc - 1 > 0.20


def test_chi8_control_stays_inside_20pct():
    def s4(g1, gap, D, odd):
        return 0.14 * (g1 ** 1.32) * (gap ** 0.45) * math.exp(-0.13 * D) * (1.32 if odd else 1)
    name, odd, g, gp, d, sc, so = [h for h in map2.HOLD if h[0] == '-8'][0]
    hat = s4(g, gp, d, odd)
    assert abs(hat / sc - 1) < 0.20
