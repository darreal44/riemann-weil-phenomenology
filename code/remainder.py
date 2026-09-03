# Reste delta_S(rho) = Tr(theta(rho^-1) Phat_1 P_1) = sum_n lambda_n <xi_n | theta(rho^-1) eta_n>, eta_n = F xi_n,
# via la decomposition propre de P1 F P1 (cellules, moyenne exacte). Controle archimedien : delta(rho) close (Si).
import numpy as np, sys
from scipy.special import sici
def Si(x): return sici(x)[0]
def avg_Fab(a, b, c, d, s):
    G = lambda x: (Si(2*np.pi*b*s*x) - Si(2*np.pi*a*s*x))/(np.pi*s)
    return (G(d) - G(c))/(d - c)
def Fmat(N_in, R_out, N_out, semilocal, NN=40):
    # matrice (N_out x N_in) : moyenne sur la cellule de sortie i (grille [0,R_out]) de F(1_j), cellules d'entree sur [0,1]
    ein = np.linspace(0, 1, N_in+1); eout = np.linspace(0, R_out, N_out+1)
    M = np.empty((N_out, N_in))
    for j in range(N_in):
        a, b = ein[j], ein[j+1]
        for i in range(N_out):
            c, d = eout[i], eout[i+1]
            if not semilocal: M[i, j] = avg_Fab(a, b, c, d, 1.0)
            else:
                s = -avg_Fab(a, b, c, d, 0.5)
                for n in range(NN): s += avg_Fab(a, b, c, d, 2.0**n)
                M[i, j] = 0.5*s
    return M, ein, eout
def delta_curve(semilocal, N_in=200, R_out=3.0, rhos=None):
    N_out = int(N_in*R_out)
    M, ein, eout = Fmat(N_in, R_out, N_out, semilocal)
    hin = 1.0/N_in
    A = 0.5*(M[:N_in, :N_in] + M[:N_in, :N_in].T)         # P1 F P1 en base orthonormee de cellules
    lam, X = np.linalg.eigh(A)                             # colonnes = xi_n en coefficients de cellules (orthonormes)
    ETA = M.dot(X)                                          # eta_n = F xi_n : coefficients sur les cellules de [0, R_out]
    xin = 0.5*(ein[:-1]+ein[1:]); xout = 0.5*(eout[:-1]+eout[1:])
    # fonctions : xi_n(x) = X[i,n]/sqrt(hin) sur la cellule i ; eta_n(y) = ETA[k,n]/sqrt(hin) sur la cellule k (meme largeur)
    out = []
    for rho in rhos:
        # <xi_n | theta(rho^-1) eta_n> = rho^{1/2} int_0^1 xi_n(x) eta_n(rho x) dx  (approx : valeur de eta au centre rho*x_i)
        idx = np.clip(np.floor(rho*xin/hin).astype(int), 0, N_out-1)
        vals = np.sqrt(rho)*np.sum(X*ETA[idx, :], axis=0)*hin/hin      # (X/sqrt h)(ETA/sqrt h) * h
        out.append(np.sum(lam*vals))
    return np.array(out), lam
if __name__ == '__main__':
    rhos = np.array([1.001, 1.01, 1.03, 1.1, 1.2, 1.4, 1.7, 2.0, 2.5, 2.9])
    dA, lamA = delta_curve(False, 200, 3.0, rhos)
    closed = 2*np.sqrt(rhos)*(Si(2*np.pi*(1+rhos))/(2*np.pi*(1+rhos)) + Si(2*np.pi*(rhos-1))/(2*np.pi*(rhos-1)))
    print("ARCHIMEDIEN  rho :", rhos)
    print("  delta reconstruit :", np.round(dA, 4))
    print("  delta forme close :", np.round(closed, 4), "   (delta(1)=2.2375, delta'(1+)=1)")
    for N in (200, 300):
        dS, lamS = delta_curve(True, N, 3.0, rhos)
        print(f"SEMI-LOCAL N={N} : delta_S =", np.round(dS, 4))
    # comportement pres de 1 : pente et courbure log ?
    rh = np.array([1.002, 1.004, 1.008, 1.016, 1.032, 1.064])
    dS, _ = delta_curve(True, 300, 3.0, rh)
    print("pres de 1 (N=300) : rho-1 =", rh-1, "\n   delta_S =", np.round(dS, 4), "\n   increments par doublement :", np.round(np.diff(dS), 4))
