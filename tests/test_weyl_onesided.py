# One-sided Weyl count vs the chi5 cache on (0,30] (report/weyl-density-check.md).
import os, sys, pickle, numpy as np, mpmath as mp, importlib.util
CODE = os.path.join(os.path.dirname(__file__), '..', 'code')

def _L5():
    spec = importlib.util.spec_from_file_location("kr", os.path.join(CODE, "kronecker.py"))
    kr = importlib.util.module_from_spec(spec); spec.loader.exec_module(kr)
    tab = kr.chi_tab(5, 5)
    def L(t):
        s = mp.mpf('0.5') + 1j*mp.mpf(t)
        return 5**(-s)*mp.fsum(tab[r]*mp.zeta(s, mp.mpf(r)/5) for r in range(1, 5) if tab[r])
    return L

def test_chi5_zero_count_on_0_30_is_one_sided_weyl():
    mp.mp.dps = 15
    L = _L5()
    ts = np.arange(0.5, 30.0, 0.05)
    a2 = np.array([float(abs(L(t)))**2 for t in ts])
    mins = [ts[i] for i in range(1, len(ts)-1) if a2[i] < a2[i-1] and a2[i] < a2[i+1] and a2[i] < 5e-2]
    cache = pickle.load(open(os.path.join(CODE, 'zeros_chi5_150.pkl'), 'rb'))
    ncache = sum(1 for z in cache if float(str(z)) <= 30.0)
    one_sided = 30/(2*np.pi)*np.log(5*30/(2*np.pi*np.e))
    assert len(mins) == ncache == 11, (len(mins), ncache)
    assert abs(len(mins) - one_sided) < 2.5, one_sided      # 10.4 ; the two-sided formula gives 20.7

def test_sign_change_would_double_count():
    mp.mp.dps = 15
    L = _L5()
    ts = np.arange(6.0, 20.0, 0.1)
    re = np.array([float(mp.re(L(t))) for t in ts])
    ab = np.array([float(abs(L(t))) for t in ts])
    sign_changes = int(np.sum(re[1:]*re[:-1] < 0))
    zeros = sum(1 for i in range(1, len(ab)-1) if ab[i] < ab[i-1] and ab[i] < ab[i+1] and ab[i] < 0.05)
    assert sign_changes >= 1.6*zeros, (sign_changes, zeros)
