# GL2 quorum and quorum laws (notebook 112-114). Recomputing; ~2 min.
import os, sys, io, contextlib, importlib.util, numpy as np, mpmath as mp
CODE = os.path.join(os.path.dirname(__file__), '..', 'code'); sys.path.insert(0, CODE)
from gl2_curves import CURVES, ap_table

def _mat(lab, NP, mu, dps, drop=None):
    os.environ['GL2_FIX'] = '1'; mp.mp.dps = dps
    spec = importlib.util.spec_from_file_location('g', os.path.join(CODE, 'scan_q_gl2.py')); g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
    a, N = CURVES[lab]; ap = dict(ap_table(lab, 80))
    if drop is not None: ap[drop] = None
    g.ellan = lambda label, cap: g.hecke_an({p: v for p, v in ap.items() if v is not None}, N, cap)
    cap = {}; _e = mp.eigsy; mp.eigsy = lambda S, *a_, **k: (cap.setdefault('S', S), _e(S, *a_, **k))[1]
    try:
        with contextlib.redirect_stdout(io.StringIO()): g.assemble(lab, mu, NP-1, dps)
    finally: mp.eigsy = _e
    return np.array([[float(cap['S'][i, j]) for j in range(NP)] for i in range(NP)])

def test_67a1_partial_quorum_at_22_complete_at_38():
    assert np.linalg.eigvalsh(_mat('67a1', 21, 22.0, 30, drop=2))[0] > 0.5        # dispensable at mu=22
    assert np.linalg.eigvalsh(_mat('67a1', 33, 38.0, 40, drop=2))[0] < -0.1       # necessary at mu=38
    assert np.linalg.eigvalsh(_mat('67a1', 33, 38.0, 40))[0] > 0                  # and the full form is PSD

def test_32a1_mute_prime_invisible_and_square_voter_necessary():
    full = np.linalg.eigvalsh(_mat('32a1', 25, 22.0, 30))[0]
    assert abs(np.linalg.eigvalsh(_mat('32a1', 25, 22.0, 30, drop=7))[0]/full - 1) < 1e-6   # 49 > 22: 7 does not vote
    assert np.linalg.eigvalsh(_mat('32a1', 25, 22.0, 30, drop=3))[0] < -0.01              # a_3 = 0 but Lambda_f(9) != 0

def test_silence_law_in_degree_2_uses_d_times_s():
    mu, NP = 22.0, 21; s = 0.614; L = np.log(mu)
    S = _mat('19a1', NP, mu, 30); v = np.linalg.eigh(S)[1][:, 0]
    for p in (11, 13):
        T = S - _mat('19a1', NP, mu, 30, drop=p); d = v.dot(T.dot(v)); w = p*np.log(p)
        coef = -np.log(abs(d))/w
        assert abs(coef - 0.19*2*s) < 0.06, (p, coef)          # 0.233 predicted with d = 2; 0.117 with d = 1
