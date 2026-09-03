# Semi-local remainder delta_S(rho) (notebook 83). Recomputed, small resolution (fast).
import os, sys, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))
from scipy.special import sici

def test_archimedean_control_reproduces_cc_closed_form():
    import remainder as rm
    rhos = np.array([1.03, 1.4, 2.5])
    d, _ = rm.delta_curve(False, 120, 3.0, rhos)
    closed = 2*np.sqrt(rhos)*(sici(2*np.pi*(1+rhos))[0]/(2*np.pi*(1+rhos)) + sici(2*np.pi*(rhos-1))[0]/(2*np.pi*(rhos-1)))
    assert np.allclose(d, closed, rtol=2e-2), (d, closed)

def test_semilocal_remainder_stable_away_from_singularities():
    import remainder as rm
    d1, _ = rm.delta_curve(True, 120, 3.0, np.array([1.2, 1.4]))
    d2, _ = rm.delta_curve(True, 180, 3.0, np.array([1.2, 1.4]))
    assert np.allclose(d1, d2, rtol=3e-2), (d1, d2)
    assert 1.7 < d1[0] < 2.2 and 1.4 < d1[1] < 1.9, d1

def test_semilocal_remainder_log_divergent_at_one():
    import remainder as rm
    rh = np.array([1.016, 1.032, 1.064, 1.128])
    d, _ = rm.delta_curve(True, 180, 3.0, rh)
    inc = np.diff(d)                    # per doubling of rho-1
    assert np.all(inc < -0.25), inc     # archimedean would be ~ +0.016 (kink, finite)

def test_semilocal_remainder_spikes_at_two():
    import remainder as rm
    d, _ = rm.delta_curve(True, 180, 3.0, np.array([1.8, 2.0, 2.3]))
    assert d[1] > 2.0*max(d[0], d[2]), d
