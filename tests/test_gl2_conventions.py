# GL2 prime-side conventions judged by the 11a1 zero Gram (report/scan_q_gl2-review.md).
import os, sys, io, pickle, contextlib, importlib.util, numpy as np, mpmath as mp
CODE = os.path.join(os.path.dirname(__file__), '..', 'code')

def _zero_gram(NP, mu):
    Z = sorted(float(str(x)) for x in pickle.load(open(os.path.join(CODE, 'zeros_11a1_weyl.pkl'), 'rb')))
    L = mp.log(mu); om = [2*mp.pi*n/L for n in range(NP)]
    Q = np.zeros((NP, NP))
    for g in Z:
        g = mp.mpf(g); s = mp.sin(g*L/2)
        c = np.array([float(2*s/(g*mp.sqrt(L)))] + [float(mp.sqrt(2/L)*s*2*g/(g*g-om[n]*om[n])) for n in range(1, NP)])
        Q += 2*np.outer(c, c)
    return Q

def _prime_side(fix, NP, mu):
    os.environ['GL2_FIX'] = '1' if fix else '0'
    spec = importlib.util.spec_from_file_location('scan_q_gl2', os.path.join(CODE, 'scan_q_gl2.py'))
    g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
    cap = {}
    _e = mp.eigsy
    mp.eigsy = lambda S, *a, **k: (cap.setdefault('S', S), _e(S, *a, **k))[1]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            g.assemble('11a1', mu, NP-1, 30)
    finally:
        mp.eigsy = _e
    S = cap['S']
    return np.array([[float(S[i, j]) for j in range(NP)] for i in range(NP)])

def test_original_conventions_disagree_with_zero_gram():
    NP, mu = 13, 11.0
    Qz = _zero_gram(NP, mu); Qp = _prime_side(False, NP, mu)
    assert np.linalg.norm(Qp - Qz)/np.linalg.norm(Qz) > 0.3
    assert Qp[0, 0]/Qz[0, 0] > 5          # the excess conductor constant on the constant function

def test_corrected_conventions_match_zero_gram_to_5_percent():
    NP, mu = 13, 11.0
    Qz = _zero_gram(NP, mu); Qp = _prime_side(True, NP, mu)
    assert np.linalg.norm(Qp - Qz)/np.linalg.norm(Qz) < 0.05
    assert abs(Qp[5, 5]/Qz[5, 5] - 1) < 0.05
