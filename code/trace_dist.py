# tau_L(lambda) = Tr(Phat_L P_L theta(lambda)) sur la tranche, en fonction de lambda (grille fine).
import numpy as np, sys
sys.path.insert(0, '.')
from trace_formula import Fmat
def tau_curve(Lam, semilocal, lams, cells_per_unit=32):
    R = Lam*lams.max()*1.02
    N_in = int(Lam*cells_per_unit); ein = np.linspace(0, Lam, N_in+1); hc = Lam/N_in
    N_out = int(np.ceil(R/hc)); eout = np.linspace(0, N_out*hc, N_out+1)
    M = Fmat(ein, eout, semilocal); A = 0.5*(M[:N_in,:N_in]+M[:N_in,:N_in].T); W = M.dot(A)
    xin = 0.5*(ein[:-1]+ein[1:])
    out = np.empty(len(lams))
    for k, l in enumerate(lams):
        idx = np.clip(np.floor(xin/l/hc).astype(int), 0, N_out-1)
        out[k] = l**-0.5*np.sum(W[idx, np.arange(N_in)])           # sum_i <e_i | theta(l) Phat e_i>
    return out
if __name__ == '__main__':
    lams = np.concatenate([np.linspace(0.3, 0.9, 61), np.linspace(0.905, 1.095, 77), np.linspace(1.1, 3.3, 221)])
    Lam = 4.0
    tA = tau_curve(Lam, False, lams); tS = tau_curve(Lam, True, lams)
    weil = np.sqrt(lams)/2*(1/(1+lams) + 1/np.abs(1-lams))
    print("lambda   tau_arch   Weil_arch(39)   tau_semilocal   diff(S-A)")
    for l in [0.4, 0.5, 0.6, 0.8, 0.95, 1.05, 1.2, 1.5, 1.9, 2.0, 2.1, 2.5, 3.0]:
        k = np.argmin(np.abs(lams-l))
        print(f"{lams[k]:6.3f}   {tA[k]:8.4f}   {weil[k]:8.4f}      {tS[k]:8.4f}      {tS[k]-tA[k]:8.4f}")
    # poids des pics de la difference autour de 2 et 1/2 (integrale en d*lambda sur une fenetre)
    d = tS - tA
    for c in (0.5, 2.0):
        m = np.abs(lams - c) < 0.12*c
        w = np.trapezoid(d[m]/lams[m], lams[m]) if hasattr(np,'trapezoid') else np.sum(d[m][:-1]/lams[m][:-1]*np.diff(lams[m]))
        print(f"poids du pic de (S-A) autour de lambda={c} : {w:.4f}   (attendu log2/sqrt2 = {np.log(2)/np.sqrt(2):.4f} si terme de Weil 2-adique)")
    # masse totale sous le pic archimedien en 1 : attendu ~ 2 log' Lambda = 4 log Lambda (Connes) ?
    m1 = np.abs(lams-1) < 0.1
    print(f"aire de tau_arch autour de 1 (|l-1|<0.1, d*l) : {np.sum(tA[m1][:-1]/lams[m1][:-1]*np.diff(lams[m1])):.3f}  ; 4 log Lambda = {4*np.log(Lam):.3f}")
