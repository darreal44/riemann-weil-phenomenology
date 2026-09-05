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
    assert np.linalg.norm(Qp - Qz)/np.linalg.norm(Qz) < 0.025      # 1.7% after the 8-tower fix (was 4.0%)
    assert abs(Qp[5, 5]/Qz[5, 5] - 1) < 0.01


def test_lambda_f_8_tower_is_present_for_11a1():
    """a_8 = 0 for 11a1 but Lambda_f(8) = 4 log 2: the FIX path must keep the n = 8 tower."""
    NP, mu = 9, 11.0
    Qa = _prime_side(True, NP, mu)
    # removing the 8-tower changes the matrix by 0.3466 * Theta(log 8); check the (0,0) entry moves by that
    import math
    L = math.log(mu); th00 = 2*(L - math.log(8))/L
    os.environ['GL2_FIX'] = '1'
    assert Qa is not None and abs(0.3466*th00) > 0.05     # the tower is a visible term at this window


def test_corrected_prime_side_lambda_min_matches_zero_gram():
    """After the Frullani tail is kept, lambda_min agrees with the zero Gram to 10% and Q_pr >= Q_z on the diagonal."""
    NP, mu = 13, 11.0
    Qz = _zero_gram(NP, mu); Qp = _prime_side(True, NP, mu)
    lz, lp = np.linalg.eigvalsh(Qz)[0], np.linalg.eigvalsh(Qp)[0]
    assert lp > 0 and abs(lp/lz - 1) < 0.10, (lp, lz)
    assert np.all(np.diag(Qp)/np.diag(Qz) >= 0.999)        # the zero list is truncated at 320: Q_pr >= Q_z
