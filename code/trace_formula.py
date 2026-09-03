# Verification numerique du Theoreme 4 de Connes (1999) sur la tranche : T(Lambda) = Tr(Phat_L P_L U(h)),
# U(h) = int h(lambda) theta(lambda) d*lambda, theta(lambda) g(r) = lambda^{-1/2} g(r/lambda). Attendu : T = 4 h(1) log Lambda + sum_v W_v(h) + o(1).
import numpy as np, sys
from scipy.special import sici
def Si(x): return sici(x)[0]
def avg_Fab(a, b, c, d, s):
    G = lambda x: (Si(2*np.pi*b*s*x) - Si(2*np.pi*a*s*x))/(np.pi*s)
    return (G(d) - G(c))/(d - c)
def Fmat(ein, eout, semilocal, NN=40):
    M = np.empty((len(eout)-1, len(ein)-1))
    for j in range(len(ein)-1):
        a, b = ein[j], ein[j+1]
        for i in range(len(eout)-1):
            c, d = eout[i], eout[i+1]
            if not semilocal: M[i, j] = avg_Fab(a, b, c, d, 1.0)
            else:
                s = -avg_Fab(a, b, c, d, 0.5)
                for n in range(NN): s += avg_Fab(a, b, c, d, 2.0**n)
                M[i, j] = 0.5*s
    return M
def trace(Lam, semilocal, h, lam_grid, cells_per_unit):
    R = Lam*float(np.exp(np.max(np.abs(np.log(lam_grid)))))*1.02
    N_in = int(Lam*cells_per_unit); ein = np.linspace(0, Lam, N_in+1); hc = Lam/N_in
    N_out = int(np.ceil(R/hc)); eout = np.linspace(0, N_out*hc, N_out+1)
    M = Fmat(ein, eout, semilocal)                       # F : [0,Lam] -> [0,R]
    A = M[:N_in, :N_in]; A = 0.5*(A+A.T)                 # P_L F P_L
    W = M.dot(A)                                          # Phat_L e_i = F P_L F e_i, sur [0,R], colonnes
    # trace = sum_i <e_i | U(h) Phat e_i> = sum_i int_{cell i} int h(l) l^{-1/2} W_i(r/l) d*l dr
    xin = 0.5*(ein[:-1]+ein[1:]); dlog = np.log(lam_grid[1]/lam_grid[0])
    T = 0.0
    for l in lam_grid:
        idx = np.clip(np.floor(xin/l/hc).astype(int), 0, N_out-1)      # cellule de r/l pour r = centre des cellules d'entree
        vals = W[idx, np.arange(N_in)]                                  # W_i(r_i/l), i = cellule d'entree
        T += h(l)*l**-0.5*np.sum(vals)*hc*dlog                          # int_{cell i} ~ hc * valeur ; d*l = dlog
    return T
if __name__ == '__main__':
    sig = 0.45
    h = lambda l: np.exp(-(np.log(l))**2/(2*sig**2))
    lam_grid = np.exp(np.linspace(-4*sig, 4*sig, 161))
    print(f"h(1) = 1 ; pente attendue 4 h(1) = 4.000 en log Lambda")
    for sl, name in [(False, 'archimedien'), (True, 'semi-local')]:
        Ts = []
        for Lam in (2.0, 4.0, 8.0):
            T = trace(Lam, sl, h, lam_grid, cells_per_unit=32)
            Ts.append(T); print(f"  [{name}] Lambda={Lam:.0f} : T = {T:.4f}")
        b, a = np.polyfit(np.log([2., 4., 8.]), Ts, 1)
        print(f"  [{name}] ajustement T = {a:.4f} + {b:.4f} log Lambda   (pente attendue 4)")
