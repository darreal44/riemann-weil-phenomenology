# Espace semi-local {inf, 2} sur la tranche ord_2 = 0 : fonctions g sur [0, inf), base de cellules.
# Fourier semi-local : Fg(rho) = 1/2 [ sum_{n>=0} ghat(2^n rho) - ghat(rho/2) ],  ghat(xi) = 2 int_0^inf g cos(2 pi r xi) dr
# Fourier archimedien (controle) : Fg(rho) = ghat(rho).
import numpy as np
from scipy.special import sici
def Fab(a, b, xi):                       # ghat de 1_{[a,b]} : [sin(2 pi b xi) - sin(2 pi a xi)]/(pi xi), xi > 0
    xi = np.asarray(xi, float); out = np.empty_like(xi)
    z = xi > 1e-14
    out[z] = (np.sin(2*np.pi*b*xi[z]) - np.sin(2*np.pi*a*xi[z]))/(np.pi*xi[z]); out[~z] = 2*(b-a)
    return out
def F_cell(a, b, rho, semilocal=True, NN=48):
    if not semilocal: return Fab(a, b, rho)
    s = -Fab(a, b, rho/2)
    for n in range(NN): s = s + Fab(a, b, (2.0**n)*rho)
    return 0.5*s
def build(R, N, semilocal=True):
    # cellules de largeur h = R/N sur [0,R] ; matrice F_ij = (F 1_j)(rho_i) (point milieu), base orthonormee e_j = h^{-1/2} 1_j
    h = R/N; edges = np.linspace(0, R, N+1); mids = 0.5*(edges[:-1]+edges[1:])
    F = np.empty((N, N))
    for j in range(N): F[:, j] = F_cell(edges[j], edges[j+1], mids, semilocal)
    return F, h, mids
if __name__ == '__main__':
    for sl, name in [(False, "archimedien"), (True, "semi-local {inf,2}")]:
        R, N = 6.0, 1200; F, h, mids = build(R, N, sl); n1 = int(N/R)   # cellules dans [0,1]
        # unitarite sur les fonctions supportees dans [0,1] : ||F e_j||^2 sur [0,R]
        nrm = (F[:, :n1]**2).sum(axis=0)       # (F e_j)(rho_i)^2 * h
        # involution : (F F e_j) restreint a [0,1] vs e_j
        FF = F.dot(F)
        inv = np.abs(FF[:n1, :n1] - np.eye(n1)).max()
        # prolates : A = P1 F P1, symetrique ; valeurs propres
        A = F[:n1, :n1]
        A = 0.5*(A+A.T); ev = np.sort(np.linalg.eigvalsh(A))
        top = sorted(ev, key=lambda x: -abs(x))[:7]
        print(f"[{name}] R={R}, h={h:.4f} : ||F e_j||^2 moyen sur [0,1] = {nrm.mean():.4f} (min {nrm.min():.4f}) ; max|FF-I| sur [0,1] = {inv:.3f}")
        print(f"   valeurs propres de P1 F P1 (par |.| decroissant) : {np.round(top, 5)}")
    print("   (archimedien attendu : 0.99997, -0.97949, 0.52409, -0.05898, 0.00273, -0.00008)")
