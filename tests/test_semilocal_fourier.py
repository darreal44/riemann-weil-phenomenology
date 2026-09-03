# Semi-local {infinity, 2} Fourier transform on the ord_2 = 0 slice (notebook 82).
# These tests RECOMPUTE the operator; they do not replay frozen numbers, except for the
# archimedean calibration of code/cc_arch.py against Connes-Consani (Selecta 2021).
import os, sys, numpy as np
from numpy.polynomial.legendre import leggauss

CODE = os.path.join(os.path.dirname(__file__), '..', 'code')
sys.path.insert(0, CODE)

# ---------- the operator under test ----------
def _hat_of(gv, r, w):
    def hat(xi):
        xi = np.asarray(xi, float); out = np.zeros_like(xi)
        m = xi < 60.0                      # beyond, |ghat| < 1e-30 for our test functions
        out[m] = 2*np.sum(w*gv*np.cos(2*np.pi*r*xi[m][:, None]), axis=1)
        return out
    return hat

def F_slice(hat, xs, NN=14):
    """Fg(rho) = 1/2 [ sum_{n>=0} ghat(2^n rho) - ghat(rho/2) ]."""
    xs = np.asarray(xs, float)
    out = -hat(xs/2)
    for n in range(NN):
        out = out + hat((2.0**n)*xs)
    return 0.5*out

def _bump(center=0.5, width=0.09, halfsupp=0.3):
    tq, wq = leggauss(400)
    r = 0.5 + 0.5*tq; w = 0.5*wq
    gv = np.exp(-((r-center)/width)**2)*(np.abs(r-center) < halfsupp)
    return gv, r, w

# ---------- 1. the closed form is the honest adelic transform ----------
def test_closed_form_matches_direct_shell_sum():
    """Independent derivation: the 2-adic factor on shells (weights 2^-n/2) applied
    shell by shell must reproduce the lacunary closed form."""
    gv, r, w = _bump(); hat = _hat_of(gv, r, w)
    xs = np.array([0.31, 0.77, 1.4, 2.9])
    direct = np.empty_like(xs)
    for i, x in enumerate(xs):
        # 2-adic Fourier of the indicator of Z_2 evaluated on shell m:
        #   contributes +1 for m >= 0 and -2^{m+1}/2 ... encoded as: sum_{n>=0} - the n=-1 term
        s = -hat(np.array([x/2]))[0]
        for n in range(14):
            s += hat(np.array([(2.0**n)*x]))[0]
        direct[i] = 0.5*s
    assert np.allclose(direct, F_slice(hat, xs), rtol=1e-12, atol=1e-14)

# ---------- 2. unitarity ----------
def test_unitary_on_the_slice():
    gv, r, w = _bump(); hat = _hat_of(gv, r, w)
    rho = np.linspace(1e-4, 130.0, 130001); d = rho[1]-rho[0]
    G = F_slice(hat, rho)
    ratio = np.sum(G**2)*d/np.sum(w*gv**2)
    assert abs(ratio - 1.0) < 0.05, ratio

def test_unitary_for_a_second_test_function():
    gv, r, w = _bump(center=0.42, width=0.06, halfsupp=0.25); hat = _hat_of(gv, r, w)
    rho = np.linspace(1e-4, 130.0, 130001); d = rho[1]-rho[0]
    ratio = np.sum(F_slice(hat, rho)**2)*d/np.sum(w*gv**2)
    assert abs(ratio - 1.0) < 0.06, ratio

# ---------- 3. involution ----------
def test_involution_on_the_support():
    gv, r, w = _bump(); hat = _hat_of(gv, r, w)
    rho = np.linspace(1e-4, 130.0, 130001); d = rho[1]-rho[0]
    G = F_slice(hat, rho)
    def Ghat(xi):
        xi = np.asarray(xi, float); out = np.zeros_like(xi)
        for i, x in enumerate(xi):
            if x < 3.0:
                out[i] = 2*np.sum(G*np.cos(2*np.pi*rho*x))*d
        return out
    xs = np.array([0.4, 0.5, 0.6])
    back = F_slice(Ghat, xs)
    ratio = back/np.array([np.exp(-((x-0.5)/0.09)**2) for x in xs])
    assert np.all(np.abs(ratio - 1.0) < 0.10), ratio

# ---------- 4. structural facts, with EXACT cell averaging (midpoint evaluation aliases) ----------
def test_compression_is_self_adjoint_with_exact_averaging():
    import semilocal2 as s2
    A, h = s2.build_exact(120, True)
    asym = np.abs(A - A.T).max()/np.abs(A).max()
    assert asym < 1e-8, asym

def test_midpoint_evaluation_aliases():
    """The 0.43 'asymmetry' of notebook 82 was aliasing of the lacunary terms."""
    import semilocal as sl
    F, h, mids = sl.build(1.0, 300, True)
    assert np.abs(F - F.T).max()/np.abs(F).max() > 0.2

def test_semilocal_compression_is_not_trace_class():
    """sum lambda^2 = ||P1 F P1||_HS^2 : 2.2375 (finite) at the archimedean place,
    growing with resolution (log-divergent) for {inf, 2}."""
    import semilocal2 as s2
    Aa, _ = s2.build_exact(120, False); sa = np.sum(np.linalg.eigvalsh(0.5*(Aa+Aa.T))**2)
    assert abs(sa - 2.2375) < 0.01, sa
    A1, _ = s2.build_exact(100, True); A2, _ = s2.build_exact(200, True)
    s1 = np.sum(np.linalg.eigvalsh(0.5*(A1+A1.T))**2); s2v = np.sum(np.linalg.eigvalsh(0.5*(A2+A2.T))**2)
    assert s1 > 3.0 and s2v > s1 + 0.2, (s1, s2v)

# ---------- 5. archimedean calibration against Connes-Consani (Selecta 2021) ----------
def test_cc_archimedean_calibration():
    import importlib, io, contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        cc = importlib.import_module('cc_arch')
    assert abs(cc.lam[0] - 0.999971) < 1e-5
    assert abs(cc.lam[1] + 0.979485) < 1e-5
    assert abs(cc.lam[2] - 0.524086) < 1e-5
    assert abs(cc.eps1 - 22.9965) < 1e-3       # CC: epsilon'(1+) = 22.9965
