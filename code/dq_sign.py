# Signe de D o Q sur L^2(I), I=[-a,a] : D o Q(xi_i * xi_j~) = int (Q_+ f)(v) delta(e^{|v|}) dv, f = correlation.
# Q_+ = -d^2/dv^2 + 1/4 applique a la fonction test lisse ; delta : archimedien (forme close) ou semi-local (remainder.py).
import numpy as np, sys, io, contextlib
from scipy.special import sici
sys.path.insert(0, '.')
import remainder as rm
def delta_arch(rho):
    rho = np.asarray(rho, float)
    return 2*np.sqrt(rho)*(sici(2*np.pi*(1+rho))[0]/(2*np.pi*(1+rho)) + sici(2*np.pi*(rho-1))[0]/(2*np.pi*(rho-1)))
def spectrum_DQ(a, delta_of_rho, K=20, M=1600):
    x = np.linspace(-a, a, M+1); dx = x[1]-x[0]
    B = np.array([np.sin(k*np.pi*(x+a)/(2*a)) for k in range(1, K+1)])           # base sinus (Dirichlet), lisse
    G = B.dot(B.T)*dx                                                              # matrice de Gram
    v = np.arange(-M, M+1)*dx                                                      # correlation sur [-2a, 2a]
    dv = np.abs(v); rho = np.exp(dv); dl = delta_of_rho(np.maximum(rho, 1+1e-9))
    corr = lambda f, g: np.correlate(g, f, mode='full')*dx                        # int f(x) g(x+v) dx
    DQ = np.empty((K, K))
    for i in range(K):
        for j in range(i, K):
            f = corr(B[i], B[j])
            Qf = -np.gradient(np.gradient(f, dx), dx) + 0.25*f
            val = np.sum(Qf*dl)*dx
            DQ[i, j] = DQ[j, i] = val
    from scipy.linalg import eigh
    ev = eigh(DQ, G, eigvals_only=True)
    return np.sort(ev)[::-1]
if __name__ == '__main__':
    # controle archimedien a log 2 : CC (Rem. 3.9) : D o Q n'est pas negatif sur [1/2, 2] mais l'exces est de petite dimension
    for L in (np.log(2), np.log(3)):
        ev = spectrum_DQ(L/2, delta_arch)
        print(f"[archimedien, I de longueur {L:.3f}] valeurs propres de D o Q (rel. Gram) : nb>0 = {(ev>0).sum()}/{len(ev)} ; les 4 plus grandes {np.round(ev[:4],3)} ; les 3 plus petites {np.round(ev[-3:],3)}")
    # semi-local : delta_S sur une grille de rho, interpolee
    rg = np.concatenate([1+np.geomspace(1e-4, 0.3, 120), np.linspace(1.31, 3.05, 200)])
    with contextlib.redirect_stdout(io.StringIO()):
        dS, _ = rm.delta_curve(True, 200, 3.1, rg)
    delta_sl = lambda r: np.interp(np.asarray(r, float), rg, dS)
    for L in (np.log(2), np.log(3)):
        ev = spectrum_DQ(L/2, delta_sl)
        print(f"[semi-local,  I de longueur {L:.3f}] valeurs propres de D_S o Q (rel. Gram) : nb>0 = {(ev>0).sum()}/{len(ev)} ; les 4 plus grandes {np.round(ev[:4],3)} ; les 3 plus petites {np.round(ev[-3:],3)}")
