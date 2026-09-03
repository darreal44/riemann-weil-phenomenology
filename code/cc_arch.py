# Reconstruction de la place archimedienne de Connes-Consani (Selecta 2021) : prolates c=2pi,
# xi_n, epsilon'(1+), Q eps(rho) via (99), et l'operateur compact K_I (Toeplitz, q -> 1).
import numpy as np
from scipy.special import pro_ang1
from numpy.polynomial.legendre import leggauss
c = 2*np.pi
NQ = 400
tq, wq = leggauss(NQ)                       # noeuds sur [-1,1]
def phi(n, x):                              # prolate angulaire PS_{2n,0}(2pi, x), |x|<=1
    return pro_ang1(0, 2*n, c, np.clip(x, -1, 1))[0]
NMAX = 8
lam = np.zeros(NMAX); xi = []               # xi_n normalise : int_0^1 xi^2 = 1
for n in range(NMAX):
    f = phi(n, tq)
    # valeur propre de la transformee de Fourier finie : int_{-1}^1 phi(t) e^{2pi i t w} dt = lam phi(w) ; prendre w = 0.3
    w0 = 0.3
    lam[n] = np.sum(wq*f*np.cos(c*tq*w0))/phi(n, w0)
    nrm = np.sqrt(np.sum(wq*f*f)/2)         # int_0^1 f^2 = (1/2) int_{-1}^1 f^2
    xi.append(f/nrm)
print("lambda(n) :", np.round(lam[:6], 6), "  (CC : 0.999971, -0.979485, 0.524086, -0.0589766, 0.00273233, -7.63e-5)")
def xi_an(n, x):                            # continuation analytique : (1/lam) int_{-1}^1 xi(t) cos(2pi t x) dt
    x = np.atleast_1d(x); return np.array([np.sum(wq*xi[n]*np.cos(c*tq*xx)) for xx in x])/lam[n]
def dxi_an(n, x):
    x = np.atleast_1d(x); return np.array([np.sum(wq*xi[n]*(-c*tq)*np.sin(c*tq*xx)) for xx in x])/lam[n]
xi1 = np.array([xi_an(n, 1.0)[0] for n in range(NMAX)])
tn = lam**2/(1-lam**2)*xi1**2
print("t(n) = lam^2/(1-lam^2) xi_n(1)^2 :", np.round(tn[:5], 5), " (CC : 11.9719, 8.77574, 2.20528, 0.0433983, 0.000125)")
eps1 = tn.sum(); print(f"epsilon'(1+) = {eps1:.4f}   (CC : 22.9965)")
def Qeps(rho):                              # formule (99) : Q eps(rho) = sum lam^2/(1-lam^2) C_n(rho), rho > 1
    if abs(rho-1) < 1e-12: return 0.0
    ts, ws = leggauss(120); a, b = 1/rho, 1.0
    x = (a+b)/2 + (b-a)/2*ts; w = (b-a)/2*ws
    tot = 0.0
    for n in range(NMAX):
        if tn[n] < 1e-14: break
        d1 = dxi_an(n, x); d2 = dxi_an(n, rho*x)
        Cn = np.sqrt(rho)*np.sum(w*x*d1*rho*x*d2) + rho**-1.5*dxi_an(n, 1/rho)[0]*xi1[n] - rho**1.5*xi1[n]*dxi_an(n, rho)[0]
        tot += lam[n]**2/(1-lam[n]**2)*Cn
    return tot
if __name__ == '__main__':
    xs = np.linspace(0, np.log(2), 8)
    print("Q eps(e^x)/(2 eps') sur [0,log2] :", np.round([Qeps(np.exp(x))/(2*eps1) for x in xs], 3), " (CC fig.10 : de ~-1 a ~3)")
    # Toeplitz : I = [-log2/2, log2/2], pas omega ; T[j,k] = Q eps(q^{|j-k|}) ; matrice (omega/(2 eps')) T
    for L, label in [(np.log(2), "log 2"), (np.log(3), "log 3")]:
        omega = 2e-3; N = int(L/omega)+1
        vals = np.array([Qeps(np.exp(k*omega)) for k in range(N)])
        from scipy.linalg import toeplitz, eigvalsh
        T = toeplitz(vals)*omega/(2*eps1)
        ev = np.sort(eigvalsh(T))[::-1]
        print(f"I de longueur {label} (N={N}) : valeurs propres de K_I : {np.round(ev[:5], 5)}   nb > 1 : {(ev > 1).sum()}")
    print("(CC a log 2 : lambda_max = 1.05158, lambda_2 = 0.686494, lambda_3 = 0.0288921)")
