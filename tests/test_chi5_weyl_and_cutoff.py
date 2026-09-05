# Notebook 92: the server chi5 cache, the missed close pair, and the cutoff dependence of the gap sum.
import os, math, pickle, numpy as np
CODE = os.path.join(os.path.dirname(__file__), '..', 'code')
def _load(name): return sorted(float(str(x)) for x in pickle.load(open(os.path.join(CODE, name), 'rb')))
def _weyl1(T, q): return T/(2*math.pi)*math.log(q*T/(2*math.pi*math.e))

def test_chi5_weyl_cache_complete_one_sided():
    w = _load('zeros_chi5_weyl.pkl')
    assert len(w) >= 200 and w[-1] > 300
    for T in (80.0, 150.0, 250.0, w[-1]):
        n = sum(1 for z in w if z <= T)
        assert abs(n/_weyl1(T, 5) - 1.0) < 0.03, (T, n)
    assert min(np.diff(w)) > 0.04            # no pair inside one scan step

def test_my_chi5_150_cache_missed_exactly_one_close_pair_member():
    w = _load('zeros_chi5_weyl.pkl'); c = _load('zeros_chi5_150.pkl')
    missing = [z for z in w if z <= c[-1] + 0.02 and min(abs(z-x) for x in c) > 0.02]
    extra = [x for x in c if min(abs(x-z) for z in w) > 0.02]
    assert extra == []
    assert len(missing) == 1 and abs(missing[0] - 90.377) < 0.01
    i = w.index(missing[0])
    assert w[i+1] - w[i] < 0.35            # the pair was narrower than the old scan step

def test_gap_excess_sum_grows_with_cutoff_for_zeta():
    Z = _load('zeros500.pkl'); nyq = 2*math.pi/math.log(22)
    def ex(cut):
        z = [x for x in Z if x <= cut]
        return sum(max(z[k+1]-z[k]-nyq, 0.0) for k in range(len(z)-1))
    s150, s320, s811 = ex(150), ex(320), ex(811)
    assert s320 > 1.3*s150 and s811 > 1.25*s320, (s150, s320, s811)

def test_zeta_fit_at_common_cutoff_320():
    Z = [x for x in _load('zeros500.pkl') if x <= 320]
    mes = {3: 16.7, 8: 74.0, 11: 110.2, 16: 167.4}
    rows = []
    for mu, y in mes.items():
        L = math.log(mu); nyq = 2*math.pi/L
        rows.append(([L*max(Z[0]-nyq, 0.0), L*sum(max(Z[k+1]-Z[k]-nyq, 0.0) for k in range(len(Z)-1))], y))
    A = np.array([r[0] for r in rows]); Y = np.array([r[1] for r in rows])
    (a, b), *_ = np.linalg.lstsq(A, Y, rcond=None)
    res = A.dot([a, b])/Y - 1
    assert abs(a - 1.71) < 0.05 and abs(b - 0.97) < 0.05, (a, b)
    assert np.all(np.abs(res) < 0.03), res
