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

def test_completed_L_is_real_and_its_sign_changes_are_the_zeros():
    """harvest_weyl.Lam is the completed L; root number 1 for real primitive chi => real on the line."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("hw", os.path.join(CODE, "harvest_weyl.py"))
    hw = importlib.util.module_from_spec(spec); spec.loader.exec_module(hw)
    spec2 = importlib.util.spec_from_file_location("kr", os.path.join(CODE, "kronecker.py"))
    kr = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(kr)
    mp.mp.dps = 15
    q, tab, a = 5, kr.chi_tab(5, 5), 0
    ts = np.arange(0.5, 30.0, 0.05)
    vals = [float(hw.Lam(mp.mpf(t), q, tab, a)) for t in ts]
    sc = sum(1 for i in range(len(ts)-1) if vals[i]*vals[i+1] < 0)
    assert sc == 11, sc
    assert abs(float(hw.expected_N(30, q)) - 10.4) < 0.5, float(hw.expected_N(30, q))   # one-sided
