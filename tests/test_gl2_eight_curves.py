# Eight elliptic curves: corrected prime-side Q vs each zero Gram at mu=11 (notebook 111).
# The prime side detects the analytic rank: the central zero (once) is needed for rank 1 and wrong for rank 0.
import os, sys, io, pickle, contextlib, importlib.util, numpy as np, mpmath as mp
CODE = os.path.join(os.path.dirname(__file__), '..', 'code'); sys.path.insert(0, CODE)
from gl2_curves import CURVES, ap_table
RANK1 = {'37a1', '43a1', '53a1', '61a1'}

def _gram(lab, NP, mu, central):
    Z = sorted(float(str(x)) for x in pickle.load(open(os.path.join(CODE, f'zeros_{lab}_weyl.pkl'), 'rb')))
    L = np.log(mu); om = np.array([2*np.pi*n/L for n in range(NP)]); Q = np.zeros((NP, NP))
    for x in Z:
        s = np.sin(x*L/2); c = np.empty(NP); c[0] = 2*s/(x*np.sqrt(L)); c[1:] = np.sqrt(2/L)*s*2*x/(x*x-om[1:]**2); Q += 2*np.outer(c, c)
    if central:
        c0 = np.zeros(NP); c0[0] = np.sqrt(L); Q += np.outer(c0, c0)
    return Q

def _prime(lab, NP, mu):
    os.environ['GL2_FIX'] = '1'; mp.mp.dps = 25
    spec = importlib.util.spec_from_file_location('g', os.path.join(CODE, 'scan_q_gl2.py')); g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
    a, N = CURVES[lab]; ap = ap_table(lab, 40); g.ellan = lambda label, cap: g.hecke_an(ap, N, cap)
    cap = {}; _e = mp.eigsy; mp.eigsy = lambda S, *a_, **k: (cap.setdefault('S', S), _e(S, *a_, **k))[1]
    try:
        with contextlib.redirect_stdout(io.StringIO()): g.assemble(lab, mu, NP-1, 25)
    finally: mp.eigsy = _e
    return np.array([[float(cap['S'][i, j]) for j in range(NP)] for i in range(NP)])

def test_eight_curves_match_their_zero_grams_with_rank_detection():
    NP, mu = 11, 11.0
    for lab in CURVES:
        Qp = _prime(lab, NP, mu)
        good = _gram(lab, NP, mu, central=(lab in RANK1)); bad = _gram(lab, NP, mu, central=(lab not in RANK1))
        e_good = np.linalg.norm(Qp-good)/np.linalg.norm(good); e_bad = np.linalg.norm(Qp-bad)/np.linalg.norm(bad)
        assert e_good < 0.03, (lab, e_good)
        assert e_bad > 2*e_good, (lab, e_good, e_bad)
        lp, lz = np.linalg.eigvalsh(Qp)[0], np.linalg.eigvalsh(good)[0]
        assert lp > 0 and abs(lp/lz - 1) < 0.10, (lab, lp, lz)
