# Sign of D o Q on smooth test functions of I (notebook 84): archimedean essentially negative
# (CC Theorem 3.6: -2 Id + compact, finite positive excess), semi-local essentially positive.
import os, sys, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))

def test_archimedean_DQ_is_essentially_negative():
    import dq_sign as dq
    ev = dq.spectrum_DQ(np.log(2)/2, dq.delta_arch, K=14, M=800)
    assert (ev > 0).sum() <= 3, ev
    assert np.median(ev) < -1.5, np.median(ev)          # the -2 Id of Theorem 3.6

def test_semilocal_DQ_is_essentially_positive_at_log3():
    import dq_sign as dq, remainder as rm, io, contextlib
    rg = np.concatenate([1+np.geomspace(1e-4, 0.3, 60), np.linspace(1.31, 3.05, 90)])
    with contextlib.redirect_stdout(io.StringIO()):
        dS, _ = rm.delta_curve(True, 120, 3.1, rg)
    delta_sl = lambda r: np.interp(np.asarray(r, float), rg, dS)
    ev = dq.spectrum_DQ(np.log(3)/2, delta_sl, K=14, M=800)
    assert (ev > 0).sum() >= 8, ev
    assert ev[0] > 50, ev[0]
